# PostV1ActiveStorageBlobsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blob_filename** | **str** | The name of the file including extension. | 
**blob_content_type** | **str** | The content type of the file. | 
**blob_byte_size** | **int** | The size of the file in bytes. | 
**blob_checksum** | **str** | The base64 encoded MD5 checksum of the file. | 

## Example

```python
from sleephq.models.post_v1_active_storage_blobs_request import PostV1ActiveStorageBlobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostV1ActiveStorageBlobsRequest from a JSON string
post_v1_active_storage_blobs_request_instance = PostV1ActiveStorageBlobsRequest.from_json(json)
# print the JSON string representation of the object
print(PostV1ActiveStorageBlobsRequest.to_json())

# convert the object into a dict
post_v1_active_storage_blobs_request_dict = post_v1_active_storage_blobs_request_instance.to_dict()
# create an instance of PostV1ActiveStorageBlobsRequest from a dict
post_v1_active_storage_blobs_request_from_dict = PostV1ActiveStorageBlobsRequest.from_dict(post_v1_active_storage_blobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


