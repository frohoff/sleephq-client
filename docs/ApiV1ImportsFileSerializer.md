# ApiV1ImportsFileSerializer

Api_V1_Imports_FileSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1ImportsFileSerializerData**](ApiV1ImportsFileSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_imports_file_serializer import ApiV1ImportsFileSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportsFileSerializer from a JSON string
api_v1_imports_file_serializer_instance = ApiV1ImportsFileSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportsFileSerializer.to_json())

# convert the object into a dict
api_v1_imports_file_serializer_dict = api_v1_imports_file_serializer_instance.to_dict()
# create an instance of ApiV1ImportsFileSerializer from a dict
api_v1_imports_file_serializer_from_dict = ApiV1ImportsFileSerializer.from_dict(api_v1_imports_file_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


