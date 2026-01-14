# ApiV1ImportsFileSerializerList

Api_V1_Imports_FileSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1ImportsFileSerializerData]**](ApiV1ImportsFileSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_imports_file_serializer_list import ApiV1ImportsFileSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportsFileSerializerList from a JSON string
api_v1_imports_file_serializer_list_instance = ApiV1ImportsFileSerializerList.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportsFileSerializerList.to_json())

# convert the object into a dict
api_v1_imports_file_serializer_list_dict = api_v1_imports_file_serializer_list_instance.to_dict()
# create an instance of ApiV1ImportsFileSerializerList from a dict
api_v1_imports_file_serializer_list_from_dict = ApiV1ImportsFileSerializerList.from_dict(api_v1_imports_file_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


