# sleephq.ActiveStorageApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v1_active_storage_blobs**](ActiveStorageApi.md#post_v1_active_storage_blobs) | **POST** /v1/active_storage/blobs | 


# **post_v1_active_storage_blobs**
> post_v1_active_storage_blobs(post_v1_active_storage_blobs_request)

Direct upload blobs

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.post_v1_active_storage_blobs_request import PostV1ActiveStorageBlobsRequest
from sleephq.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sleephq.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sleephq.Configuration(
    host = "https://sleephq.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sleephq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sleephq.ActiveStorageApi(api_client)
    post_v1_active_storage_blobs_request = sleephq.PostV1ActiveStorageBlobsRequest() # PostV1ActiveStorageBlobsRequest | 

    try:
        api_instance.post_v1_active_storage_blobs(post_v1_active_storage_blobs_request)
    except Exception as e:
        print("Exception when calling ActiveStorageApi->post_v1_active_storage_blobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_v1_active_storage_blobs_request** | [**PostV1ActiveStorageBlobsRequest**](PostV1ActiveStorageBlobsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Direct upload blobs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

