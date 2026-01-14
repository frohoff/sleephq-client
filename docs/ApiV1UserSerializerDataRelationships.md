# ApiV1UserSerializerDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**ApiV1UserSerializerDataRelationshipsTeams**](ApiV1UserSerializerDataRelationshipsTeams.md) |  | [optional] 
**memberships** | [**ApiV1UserSerializerDataRelationshipsTeams**](ApiV1UserSerializerDataRelationshipsTeams.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_user_serializer_data_relationships import ApiV1UserSerializerDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UserSerializerDataRelationships from a JSON string
api_v1_user_serializer_data_relationships_instance = ApiV1UserSerializerDataRelationships.from_json(json)
# print the JSON string representation of the object
print(ApiV1UserSerializerDataRelationships.to_json())

# convert the object into a dict
api_v1_user_serializer_data_relationships_dict = api_v1_user_serializer_data_relationships_instance.to_dict()
# create an instance of ApiV1UserSerializerDataRelationships from a dict
api_v1_user_serializer_data_relationships_from_dict = ApiV1UserSerializerDataRelationships.from_dict(api_v1_user_serializer_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


