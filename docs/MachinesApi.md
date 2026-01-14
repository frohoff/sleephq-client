# sleephq.MachinesApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_machines_id**](MachinesApi.md#get_v1_machines_id) | **GET** /v1/machines/{id} | 
[**get_v1_teams_team_id_machines**](MachinesApi.md#get_v1_teams_team_id_machines) | **GET** /v1/teams/{team_id}/machines | 


# **get_v1_machines_id**
> ApiV1MachineSerializer get_v1_machines_id(id)

Retrieve a Machine

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_machine_serializer import ApiV1MachineSerializer
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
    api_instance = sleephq.MachinesApi(api_client)
    id = 56 # int | Machine ID

    try:
        api_response = api_instance.get_v1_machines_id(id)
        print("The response of MachinesApi->get_v1_machines_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachinesApi->get_v1_machines_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Machine ID | 

### Return type

[**ApiV1MachineSerializer**](ApiV1MachineSerializer.md)

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

# **get_v1_teams_team_id_machines**
> ApiV1MachineSerializerList get_v1_teams_team_id_machines(team_id, page=page, per_page=per_page)

List Machines

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_machine_serializer_list import ApiV1MachineSerializerList
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
    api_instance = sleephq.MachinesApi(api_client)
    team_id = 56 # int | Team ID
    page = 1 # int | Page of results to fetch. (optional) (default to 1)
    per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

    try:
        api_response = api_instance.get_v1_teams_team_id_machines(team_id, page=page, per_page=per_page)
        print("The response of MachinesApi->get_v1_teams_team_id_machines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachinesApi->get_v1_teams_team_id_machines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 
 **page** | **int**| Page of results to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**ApiV1MachineSerializerList**](ApiV1MachineSerializerList.md)

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

