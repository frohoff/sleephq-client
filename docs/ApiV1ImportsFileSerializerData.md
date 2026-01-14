# ApiV1ImportsFileSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1ImportsFileSerializerDataAttributes**](ApiV1ImportsFileSerializerDataAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_imports_file_serializer_data import ApiV1ImportsFileSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportsFileSerializerData from a JSON string
api_v1_imports_file_serializer_data_instance = ApiV1ImportsFileSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportsFileSerializerData.to_json())

# convert the object into a dict
api_v1_imports_file_serializer_data_dict = api_v1_imports_file_serializer_data_instance.to_dict()
# create an instance of ApiV1ImportsFileSerializerData from a dict
api_v1_imports_file_serializer_data_from_dict = ApiV1ImportsFileSerializerData.from_dict(api_v1_imports_file_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


