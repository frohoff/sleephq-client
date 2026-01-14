# sleephq.ImportFilesApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v1_imports_files_id**](ImportFilesApi.md#delete_v1_imports_files_id) | **DELETE** /v1/imports/files/{id} | 
[**get_v1_imports_files_id**](ImportFilesApi.md#get_v1_imports_files_id) | **GET** /v1/imports/files/{id} | 
[**get_v1_imports_import_id_files**](ImportFilesApi.md#get_v1_imports_import_id_files) | **GET** /v1/imports/{import_id}/files | 
[**get_v1_teams_team_id_files**](ImportFilesApi.md#get_v1_teams_team_id_files) | **GET** /v1/teams/{team_id}/files | 
[**post_v1_imports_files_calculate_content_hash**](ImportFilesApi.md#post_v1_imports_files_calculate_content_hash) | **POST** /v1/imports/files/calculate_content_hash | 
[**post_v1_imports_import_id_files**](ImportFilesApi.md#post_v1_imports_import_id_files) | **POST** /v1/imports/{import_id}/files | 


# **delete_v1_imports_files_id**
> delete_v1_imports_files_id(id)

Delete a File

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
    api_instance = sleephq.ImportFilesApi(api_client)
    id = 56 # int | File id

    try:
        api_instance.delete_v1_imports_files_id(id)
    except Exception as e:
        print("Exception when calling ImportFilesApi->delete_v1_imports_files_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File id | 

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
**204** | Delete a File |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_imports_files_id**
> ApiV1ImportsFileSerializer get_v1_imports_files_id(id)

Retrieve a File. Note: the download_url param is a signed URL that will expire in 5 minutes.

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_imports_file_serializer import ApiV1ImportsFileSerializer
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
    api_instance = sleephq.ImportFilesApi(api_client)
    id = 56 # int | File id

    try:
        api_response = api_instance.get_v1_imports_files_id(id)
        print("The response of ImportFilesApi->get_v1_imports_files_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportFilesApi->get_v1_imports_files_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| File id | 

### Return type

[**ApiV1ImportsFileSerializer**](ApiV1ImportsFileSerializer.md)

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

# **get_v1_imports_import_id_files**
> ApiV1ImportsFileSerializerList get_v1_imports_import_id_files(import_id, page=page, per_page=per_page)

List files

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_imports_file_serializer_list import ApiV1ImportsFileSerializerList
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
    api_instance = sleephq.ImportFilesApi(api_client)
    import_id = 56 # int | The id of the Import
    page = 1 # int | Page of results to fetch. (optional) (default to 1)
    per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

    try:
        api_response = api_instance.get_v1_imports_import_id_files(import_id, page=page, per_page=per_page)
        print("The response of ImportFilesApi->get_v1_imports_import_id_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportFilesApi->get_v1_imports_import_id_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **int**| The id of the Import | 
 **page** | **int**| Page of results to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**ApiV1ImportsFileSerializerList**](ApiV1ImportsFileSerializerList.md)

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

# **get_v1_teams_team_id_files**
> ApiV1ImportsFileSerializerList get_v1_teams_team_id_files(team_id, page=page, per_page=per_page)

List files

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_imports_file_serializer_list import ApiV1ImportsFileSerializerList
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
    api_instance = sleephq.ImportFilesApi(api_client)
    team_id = 56 # int | Team ID
    page = 1 # int | Page of results to fetch. (optional) (default to 1)
    per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

    try:
        api_response = api_instance.get_v1_teams_team_id_files(team_id, page=page, per_page=per_page)
        print("The response of ImportFilesApi->get_v1_teams_team_id_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportFilesApi->get_v1_teams_team_id_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 
 **page** | **int**| Page of results to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**ApiV1ImportsFileSerializerList**](ApiV1ImportsFileSerializerList.md)

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

# **post_v1_imports_files_calculate_content_hash**
> post_v1_imports_files_calculate_content_hash(post_v1_imports_files_calculate_content_hash_request)

Calculate the content hash of a file when testing your content_hash algorithm.
Note - do not use this end point to calculate the content in your finished application.
This end point is only for use when validating your own implementation of the content_hash algorithm.
Excessive use of this end point may result in your account being rate limited.
The content_hash is a MD5 hash of the file's content and name joined together.
For example, if the file's name is "file.txt" and the file's content is "Hello, World!",
the content_hash would be the MD5 hash of the string "Hello, World!file.txt"
Do not include the file's path when calculating the content hash.


### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.post_v1_imports_files_calculate_content_hash_request import PostV1ImportsFilesCalculateContentHashRequest
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
    api_instance = sleephq.ImportFilesApi(api_client)
    post_v1_imports_files_calculate_content_hash_request = sleephq.PostV1ImportsFilesCalculateContentHashRequest() # PostV1ImportsFilesCalculateContentHashRequest | 

    try:
        api_instance.post_v1_imports_files_calculate_content_hash(post_v1_imports_files_calculate_content_hash_request)
    except Exception as e:
        print("Exception when calling ImportFilesApi->post_v1_imports_files_calculate_content_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_v1_imports_files_calculate_content_hash_request** | [**PostV1ImportsFilesCalculateContentHashRequest**](PostV1ImportsFilesCalculateContentHashRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_imports_import_id_files**
> ApiV1ImportsFileSerializer post_v1_imports_import_id_files(import_id, name, path, content_hash, file=file)

Add a New File

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_imports_file_serializer import ApiV1ImportsFileSerializer
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
    api_instance = sleephq.ImportFilesApi(api_client)
    import_id = 56 # int | The id of the Import
    name = 'name_example' # str | The name of the file
    path = 'path_example' # str | The path to the file relative to the SD card root.
    content_hash = 'content_hash_example' # str | The calculated content_hash of the file. See the /v1/imports/files/calculate_content_hash endpoint for more information
    file = None # bytearray | The file object. Optional if the file has already been uploaded. (optional)

    try:
        api_response = api_instance.post_v1_imports_import_id_files(import_id, name, path, content_hash, file=file)
        print("The response of ImportFilesApi->post_v1_imports_import_id_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportFilesApi->post_v1_imports_import_id_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **int**| The id of the Import | 
 **name** | **str**| The name of the file | 
 **path** | **str**| The path to the file relative to the SD card root. | 
 **content_hash** | **str**| The calculated content_hash of the file. See the /v1/imports/files/calculate_content_hash endpoint for more information | 
 **file** | **bytearray**| The file object. Optional if the file has already been uploaded. | [optional] 

### Return type

[**ApiV1ImportsFileSerializer**](ApiV1ImportsFileSerializer.md)

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

