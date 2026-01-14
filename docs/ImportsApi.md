# sleephq.ImportsApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v1_imports_id**](ImportsApi.md#delete_v1_imports_id) | **DELETE** /v1/imports/{id} | 
[**get_v1_imports_id**](ImportsApi.md#get_v1_imports_id) | **GET** /v1/imports/{id} | 
[**get_v1_teams_team_id_imports**](ImportsApi.md#get_v1_teams_team_id_imports) | **GET** /v1/teams/{team_id}/imports | 
[**post_v1_imports_id_process_files**](ImportsApi.md#post_v1_imports_id_process_files) | **POST** /v1/imports/{id}/process_files | 
[**post_v1_teams_team_id_imports**](ImportsApi.md#post_v1_teams_team_id_imports) | **POST** /v1/teams/{team_id}/imports | 


# **delete_v1_imports_id**
> delete_v1_imports_id(id, purge_files=purge_files)

Delete a Import

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
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
    api_instance = sleephq.ImportsApi(api_client)
    id = 56 # int | Import ID
    purge_files = True # bool | If true, the files associated with the import will be deleted. Defaults to false. (optional)

    try:
        api_instance.delete_v1_imports_id(id, purge_files=purge_files)
    except Exception as e:
        print("Exception when calling ImportsApi->delete_v1_imports_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import ID | 
 **purge_files** | **bool**| If true, the files associated with the import will be deleted. Defaults to false. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete a Import |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_imports_id**
> ApiV1ImportSerializer get_v1_imports_id(id)

Retrieve a Import

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_import_serializer import ApiV1ImportSerializer
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
    api_instance = sleephq.ImportsApi(api_client)
    id = 56 # int | Import ID

    try:
        api_response = api_instance.get_v1_imports_id(id)
        print("The response of ImportsApi->get_v1_imports_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->get_v1_imports_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import ID | 

### Return type

[**ApiV1ImportSerializer**](ApiV1ImportSerializer.md)

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

# **get_v1_teams_team_id_imports**
> ApiV1ImportSerializerList get_v1_teams_team_id_imports(team_id, page=page, per_page=per_page)

List Imports

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_import_serializer_list import ApiV1ImportSerializerList
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
    api_instance = sleephq.ImportsApi(api_client)
    team_id = 56 # int | Team ID
    page = 1 # int | Page of results to fetch. (optional) (default to 1)
    per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

    try:
        api_response = api_instance.get_v1_teams_team_id_imports(team_id, page=page, per_page=per_page)
        print("The response of ImportsApi->get_v1_teams_team_id_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->get_v1_teams_team_id_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 
 **page** | **int**| Page of results to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**ApiV1ImportSerializerList**](ApiV1ImportSerializerList.md)

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

# **post_v1_imports_id_process_files**
> ApiV1ImportSerializer post_v1_imports_id_process_files(id)

Start processing the files from the import

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_import_serializer import ApiV1ImportSerializer
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
    api_instance = sleephq.ImportsApi(api_client)
    id = 56 # int | Import ID

    try:
        api_response = api_instance.post_v1_imports_id_process_files(id)
        print("The response of ImportsApi->post_v1_imports_id_process_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->post_v1_imports_id_process_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import ID | 

### Return type

[**ApiV1ImportSerializer**](ApiV1ImportSerializer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **post_v1_teams_team_id_imports**
> ApiV1ImportSerializer post_v1_teams_team_id_imports(team_id, programatic=programatic, device_id=device_id, name=name)

Add a New Import

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_import_serializer import ApiV1ImportSerializer
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
    api_instance = sleephq.ImportsApi(api_client)
    team_id = 56 # int | Team ID
    programatic = True # bool | Deprecated. (optional)
    device_id = 56 # int | The device type that the data is from. Find a list of device ids using the /devices endpoint. (optional)
    name = 'name_example' # str | The name of the import to show in the UI. (optional)

    try:
        api_response = api_instance.post_v1_teams_team_id_imports(team_id, programatic=programatic, device_id=device_id, name=name)
        print("The response of ImportsApi->post_v1_teams_team_id_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsApi->post_v1_teams_team_id_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 
 **programatic** | **bool**| Deprecated. | [optional] 
 **device_id** | **int**| The device type that the data is from. Find a list of device ids using the /devices endpoint. | [optional] 
 **name** | **str**| The name of the import to show in the UI. | [optional] 

### Return type

[**ApiV1ImportSerializer**](ApiV1ImportSerializer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Missing or Bad Parameters |  -  |
**401** | Not Authorized |  -  |
**403** | Permission Denied |  -  |
**406** | Validation Errors |  -  |
**422** | Record Not Saved |  -  |
**429** | API Rate Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

