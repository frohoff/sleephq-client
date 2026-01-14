# sleephq.MachineDatesApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_machine_dates_id**](MachineDatesApi.md#get_v1_machine_dates_id) | **GET** /v1/machine_dates/{id} | 
[**get_v1_machines_machine_id_machine_dates**](MachineDatesApi.md#get_v1_machines_machine_id_machine_dates) | **GET** /v1/machines/{machine_id}/machine_dates | 
[**get_v1_machines_machine_id_machine_dates_date**](MachineDatesApi.md#get_v1_machines_machine_id_machine_dates_date) | **GET** /v1/machines/{machine_id}/machine_dates/{date} | 
[**put_v1_machine_dates_id**](MachineDatesApi.md#put_v1_machine_dates_id) | **PUT** /v1/machine_dates/{id} | 


# **get_v1_machine_dates_id**
> ApiV1MachineDateSerializer get_v1_machine_dates_id(id)

Retrieve a Machine Date

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_machine_date_serializer import ApiV1MachineDateSerializer
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
    api_instance = sleephq.MachineDatesApi(api_client)
    id = 56 # int | Machine Date ID

    try:
        api_response = api_instance.get_v1_machine_dates_id(id)
        print("The response of MachineDatesApi->get_v1_machine_dates_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineDatesApi->get_v1_machine_dates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Machine Date ID | 

### Return type

[**ApiV1MachineDateSerializer**](ApiV1MachineDateSerializer.md)

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

# **get_v1_machines_machine_id_machine_dates**
> ApiV1MachineDateSerializerList get_v1_machines_machine_id_machine_dates(machine_id, sort_order=sort_order, page=page, per_page=per_page)

List Machine Dates

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_machine_date_serializer_list import ApiV1MachineDateSerializerList
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
    api_instance = sleephq.MachineDatesApi(api_client)
    machine_id = 56 # int | Machine ID
    sort_order = desc # str | Sort Order defaults to desc so the most recent record will be first (optional) (default to desc)
    page = 1 # int | Page of results to fetch. (optional) (default to 1)
    per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

    try:
        api_response = api_instance.get_v1_machines_machine_id_machine_dates(machine_id, sort_order=sort_order, page=page, per_page=per_page)
        print("The response of MachineDatesApi->get_v1_machines_machine_id_machine_dates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineDatesApi->get_v1_machines_machine_id_machine_dates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **machine_id** | **int**| Machine ID | 
 **sort_order** | **str**| Sort Order defaults to desc so the most recent record will be first | [optional] [default to desc]
 **page** | **int**| Page of results to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**ApiV1MachineDateSerializerList**](ApiV1MachineDateSerializerList.md)

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

# **get_v1_machines_machine_id_machine_dates_date**
> ApiV1MachineDateSerializer get_v1_machines_machine_id_machine_dates_date(machine_id, var_date)

Find a Machine Date

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_machine_date_serializer import ApiV1MachineDateSerializer
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
    api_instance = sleephq.MachineDatesApi(api_client)
    machine_id = 56 # int | Machine ID
    var_date = '2013-10-20' # date | Date

    try:
        api_response = api_instance.get_v1_machines_machine_id_machine_dates_date(machine_id, var_date)
        print("The response of MachineDatesApi->get_v1_machines_machine_id_machine_dates_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineDatesApi->get_v1_machines_machine_id_machine_dates_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **machine_id** | **int**| Machine ID | 
 **var_date** | **date**| Date | 

### Return type

[**ApiV1MachineDateSerializer**](ApiV1MachineDateSerializer.md)

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

# **put_v1_machine_dates_id**
> ApiV1MachineDateSerializer put_v1_machine_dates_id(id, time_offset=time_offset)

Update a Machine Date

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_machine_date_serializer import ApiV1MachineDateSerializer
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
    api_instance = sleephq.MachineDatesApi(api_client)
    id = 56 # int | Machine Date ID
    time_offset = 56 # int | Time Offset (optional)

    try:
        api_response = api_instance.put_v1_machine_dates_id(id, time_offset=time_offset)
        print("The response of MachineDatesApi->put_v1_machine_dates_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineDatesApi->put_v1_machine_dates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Machine Date ID | 
 **time_offset** | **int**| Time Offset | [optional] 

### Return type

[**ApiV1MachineDateSerializer**](ApiV1MachineDateSerializer.md)

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

