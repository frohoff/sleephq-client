# sleephq.DevicesApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_devices**](DevicesApi.md#get_v1_devices) | **GET** /v1/devices | 


# **get_v1_devices**
> ApiV1DeviceSerializerList get_v1_devices()

List Devices

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_device_serializer_list import ApiV1DeviceSerializerList
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
    api_instance = sleephq.DevicesApi(api_client)

    try:
        api_response = api_instance.get_v1_devices()
        print("The response of DevicesApi->get_v1_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_v1_devices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1DeviceSerializerList**](ApiV1DeviceSerializerList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Not Authorized |  -  |
**429** | API Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

