# ApiV1ImportsFileSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**added_by_id** | **int** |  | [optional] 
**added_by_type** | **str** |  | [optional] 
**content_hash** | **str** |  | [optional] 
**team_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**fingerprint_base64** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**download_url** | **str** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_imports_file_serializer_data_attributes import ApiV1ImportsFileSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportsFileSerializerDataAttributes from a JSON string
api_v1_imports_file_serializer_data_attributes_instance = ApiV1ImportsFileSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportsFileSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_imports_file_serializer_data_attributes_dict = api_v1_imports_file_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1ImportsFileSerializerDataAttributes from a dict
api_v1_imports_file_serializer_data_attributes_from_dict = ApiV1ImportsFileSerializerDataAttributes.from_dict(api_v1_imports_file_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


