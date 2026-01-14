# ApiV1ImportSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1ImportSerializerDataAttributes**](ApiV1ImportSerializerDataAttributes.md) |  | [optional] 
**relationships** | [**ApiV1ImportSerializerDataRelationships**](ApiV1ImportSerializerDataRelationships.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_import_serializer_data import ApiV1ImportSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportSerializerData from a JSON string
api_v1_import_serializer_data_instance = ApiV1ImportSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportSerializerData.to_json())

# convert the object into a dict
api_v1_import_serializer_data_dict = api_v1_import_serializer_data_instance.to_dict()
# create an instance of ApiV1ImportSerializerData from a dict
api_v1_import_serializer_data_from_dict = ApiV1ImportSerializerData.from_dict(api_v1_import_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


