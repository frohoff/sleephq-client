# sleephq.CurrentUserApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_me**](CurrentUserApi.md#get_v1_me) | **GET** /v1/me | 
[**post_v1_me**](CurrentUserApi.md#post_v1_me) | **POST** /v1/me | 


# **get_v1_me**
> V1MeResponse get_v1_me()

Details about the current user

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.v1_me_response import V1MeResponse
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
    api_instance = sleephq.CurrentUserApi(api_client)

    try:
        api_response = api_instance.get_v1_me()
        print("The response of CurrentUserApi->get_v1_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrentUserApi->get_v1_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1MeResponse**](V1MeResponse.md)

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
**403** | Permission Denied |  -  |
**404** | Record Not Found |  -  |
**429** | API Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_me**
> ApiV1UserSerializer post_v1_me(first_name=first_name, last_name=last_name, email=email)

Update the current user

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_user_serializer import ApiV1UserSerializer
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
    api_instance = sleephq.CurrentUserApi(api_client)
    first_name = 'first_name_example' # str | First name (optional)
    last_name = 'last_name_example' # str | Last name (optional)
    email = 'email_example' # str | Email (optional)

    try:
        api_response = api_instance.post_v1_me(first_name=first_name, last_name=last_name, email=email)
        print("The response of CurrentUserApi->post_v1_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrentUserApi->post_v1_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| First name | [optional] 
 **last_name** | **str**| Last name | [optional] 
 **email** | **str**| Email | [optional] 

### Return type

[**ApiV1UserSerializer**](ApiV1UserSerializer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Missing or Bad Parameters |  -  |
**401** | Not Authorized |  -  |
**403** | Permission Denied |  -  |
**404** | Record Not Found |  -  |
**406** | Validation Errors |  -  |
**422** | Record Not Saved |  -  |
**429** | API Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

