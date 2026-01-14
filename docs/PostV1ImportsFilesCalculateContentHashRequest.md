# PostV1ImportsFilesCalculateContentHashRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file | 
**file** | **bytearray** | The file to calculate the content hash for | 

## Example

```python
from sleephq.models.post_v1_imports_files_calculate_content_hash_request import PostV1ImportsFilesCalculateContentHashRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostV1ImportsFilesCalculateContentHashRequest from a JSON string
post_v1_imports_files_calculate_content_hash_request_instance = PostV1ImportsFilesCalculateContentHashRequest.from_json(json)
# print the JSON string representation of the object
print(PostV1ImportsFilesCalculateContentHashRequest.to_json())

# convert the object into a dict
post_v1_imports_files_calculate_content_hash_request_dict = post_v1_imports_files_calculate_content_hash_request_instance.to_dict()
# create an instance of PostV1ImportsFilesCalculateContentHashRequest from a dict
post_v1_imports_files_calculate_content_hash_request_from_dict = PostV1ImportsFilesCalculateContentHashRequest.from_dict(post_v1_imports_files_calculate_content_hash_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


