# Fix non-standard types in SleepHQ Swagger spec

# Fix non-standard types
walk(if type == "object" then
  if .type == "datetime" then .type = "string" | .format = "date-time"
  elif .type == "date" then .type = "string" | .format = "date"
  elif .type == "jsonb" then .type = "object"
  elif .type == "text" then .type = "string"
  else . end
else . end)

# Prefer HTTPS in swagger v2 by forcing schemes
| if .swagger? and .host? then
    .schemes = ["https"]
  else
    .
  end

# Fix JSON:API array responses: change array of Serializer to just Serializer
| walk(if type == "object" and .type == "array" and .items["$ref"]? and (.items["$ref"] | test("Serializer$"))
  then .items | del(.type)
  else . end)

# Split list vs detail serializers for JSON:API `data`
| . as $root
  | ([
      .paths | to_entries[] as $p
      | $p.key as $path
      | $p.value | to_entries[]
      | select(.key | ascii_downcase == "get")
      | .value.responses["200"]?.schema["$ref"]?
      | select($path | endswith("}") | not)
      | select($path != "/v1/me")
      | select(test("Serializer$"))
    ] | unique) as $list_refs
  | .paths |= with_entries(
      .key as $path
      | .value |= with_entries(
          if (.key | ascii_downcase) == "get"
             and ($path | endswith("}") | not)
             and ($path != "/v1/me")
             and (.value.responses["200"]?.schema["$ref"]? != null)
          then
            .value.responses["200"].schema["$ref"] as $ref
            | if ($ref | test("Serializer$")) then
                .value.responses["200"].schema["$ref"] = ("#/definitions/" + ($ref | split("/") | last) + "List")
              else .
              end
          else .
          end
      )
    )
  | .definitions as $defs
  | (reduce $list_refs[] as $ref ({}; 
        ($ref | split("/") | last) as $name
        | ($name + "List") as $list_name
        | if .[$list_name]? then .
          else
            . + { ($list_name): (
                $defs[$name]
                | if .properties.data? == null then
                    .
                  else
                    .properties.data as $data
                    | if ($data["$ref"]?) then
                        .properties.data = {type: "array", items: {"$ref": $data["$ref"]}}
                      elif ($data.type == "array") then
                        .
                      else
                        .properties.data = {type: "array", items: $data}
                      end
                  end
              ) }
          end
    )) as $list_defs
  | .definitions |= . + $list_defs

# Fix /v1/me response shape (not JSON:API)
| if .paths? and .paths["/v1/me"]?.get?.responses["200"]?.schema? then
    .paths["/v1/me"].get.responses["200"].schema = {"$ref": "#/definitions/V1MeResponse"}
  else
    .
  end
| .definitions |= (
    if .definitions? and .definitions.V1MeResponse? then
      .
    else
      . + {
        "V1MeResponse": {
          "type": "object",
          "properties": {
            "data": {
              "type": "object",
              "additionalProperties": true
            }
          }
        }
      }
    end
  )

# Fix JSON:API id fields: they're strings not integers
| .definitions |= walk(
  if type == "object" and .properties?.id?.type == "integer" and .properties?.type?.type == "string"
  then .properties.id.type = "string"
  else . end
)

# Fix incorrect attribute types in swagger v2 definitions
| if .definitions? and .definitions["Api_V1_MachineDateSerializer"]? then
    .definitions["Api_V1_MachineDateSerializer"]
      .properties.data.properties.attributes.properties.usage.type = "integer"
  else
    .
  end
| if .definitions? and .definitions["Api_V1_MachineDateSerializerList"]? then
    .definitions["Api_V1_MachineDateSerializerList"]
      .properties.data.items.properties.attributes.properties.usage.type = "integer"
  else
    .
  end
| if .definitions? and .definitions["Api_V1_ImportSerializer"]? then
    .definitions["Api_V1_ImportSerializer"]
      .properties.data.properties.attributes.properties.status.type = "string"
  else
    .
  end
| if .definitions? and .definitions["Api_V1_ImportSerializerList"]? then
    .definitions["Api_V1_ImportSerializerList"]
      .properties.data.items.properties.attributes.properties.status.type = "string"
  else
    .
  end
