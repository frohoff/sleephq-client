# PostV1ImportsImportIdFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the file | 
**path** | **str** | The path to the file relative to the SD card root. | 
**file** | **bytearray** | The file object. Optional if the file has already been uploaded. | [optional] 
**content_hash** | **str** | The calculated content_hash of the file. See the /v1/imports/files/calculate_content_hash endpoint for more information | 

## Example

```python
from sleephq.models.post_v1_imports_import_id_files_request import PostV1ImportsImportIdFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostV1ImportsImportIdFilesRequest from a JSON string
post_v1_imports_import_id_files_request_instance = PostV1ImportsImportIdFilesRequest.from_json(json)
# print the JSON string representation of the object
print(PostV1ImportsImportIdFilesRequest.to_json())

# convert the object into a dict
post_v1_imports_import_id_files_request_dict = post_v1_imports_import_id_files_request_instance.to_dict()
# create an instance of PostV1ImportsImportIdFilesRequest from a dict
post_v1_imports_import_id_files_request_from_dict = PostV1ImportsImportIdFilesRequest.from_dict(post_v1_imports_import_id_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


