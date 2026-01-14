# sleephq.JournalsApi

All URIs are relative to *https://sleephq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_journals_id**](JournalsApi.md#get_v1_journals_id) | **GET** /v1/journals/{id} | 
[**get_v1_teams_team_id_journals**](JournalsApi.md#get_v1_teams_team_id_journals) | **GET** /v1/teams/{team_id}/journals | 
[**post_v1_teams_team_id_journals**](JournalsApi.md#post_v1_teams_team_id_journals) | **POST** /v1/teams/{team_id}/journals | 
[**put_v1_journals_id**](JournalsApi.md#put_v1_journals_id) | **PUT** /v1/journals/{id} | 


# **get_v1_journals_id**
> ApiV1JournalSerializer get_v1_journals_id(id)

Retrieve a Journal

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_journal_serializer import ApiV1JournalSerializer
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
    api_instance = sleephq.JournalsApi(api_client)
    id = 56 # int | Journal ID

    try:
        api_response = api_instance.get_v1_journals_id(id)
        print("The response of JournalsApi->get_v1_journals_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->get_v1_journals_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Journal ID | 

### Return type

[**ApiV1JournalSerializer**](ApiV1JournalSerializer.md)

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

# **get_v1_teams_team_id_journals**
> ApiV1JournalSerializerList get_v1_teams_team_id_journals(team_id, page=page, per_page=per_page)

List Journals

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_journal_serializer_list import ApiV1JournalSerializerList
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
    api_instance = sleephq.JournalsApi(api_client)
    team_id = 56 # int | Team ID
    page = 1 # int | Page of results to fetch. (optional) (default to 1)
    per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

    try:
        api_response = api_instance.get_v1_teams_team_id_journals(team_id, page=page, per_page=per_page)
        print("The response of JournalsApi->get_v1_teams_team_id_journals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->get_v1_teams_team_id_journals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 
 **page** | **int**| Page of results to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**ApiV1JournalSerializerList**](ApiV1JournalSerializerList.md)

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

# **post_v1_teams_team_id_journals**
> ApiV1JournalSerializer post_v1_teams_team_id_journals(team_id, var_date=var_date, step_count=step_count, weight_grams=weight_grams, feeling_score=feeling_score, active_energy_joules=active_energy_joules, notes=notes, sleep_stages=sleep_stages)

Add a New Journal

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_journal_serializer import ApiV1JournalSerializer
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
    api_instance = sleephq.JournalsApi(api_client)
    team_id = 56 # int | Team ID
    var_date = '2013-10-20' # date | Date (optional)
    step_count = 'step_count_example' # str | Step Count (optional)
    weight_grams = 56 # int | Weight (Grams) (optional)
    feeling_score = 'feeling_score_example' # str | Feeling Score (optional)
    active_energy_joules = 56 # int | Active Energy (Joules) (optional)
    notes = 'notes_example' # str | Notes (optional)
    sleep_stages = 'sleep_stages_example' # str | Sleep Stages (optional)

    try:
        api_response = api_instance.post_v1_teams_team_id_journals(team_id, var_date=var_date, step_count=step_count, weight_grams=weight_grams, feeling_score=feeling_score, active_energy_joules=active_energy_joules, notes=notes, sleep_stages=sleep_stages)
        print("The response of JournalsApi->post_v1_teams_team_id_journals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->post_v1_teams_team_id_journals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| Team ID | 
 **var_date** | **date**| Date | [optional] 
 **step_count** | **str**| Step Count | [optional] 
 **weight_grams** | **int**| Weight (Grams) | [optional] 
 **feeling_score** | **str**| Feeling Score | [optional] 
 **active_energy_joules** | **int**| Active Energy (Joules) | [optional] 
 **notes** | **str**| Notes | [optional] 
 **sleep_stages** | **str**| Sleep Stages | [optional] 

### Return type

[**ApiV1JournalSerializer**](ApiV1JournalSerializer.md)

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

# **put_v1_journals_id**
> ApiV1JournalSerializer put_v1_journals_id(id, var_date=var_date, step_count=step_count, weight_grams=weight_grams, feeling_score=feeling_score, active_energy_joules=active_energy_joules, notes=notes, sleep_stages=sleep_stages)

Update a Journal

### Example

* OAuth Authentication (oauth2):

```python
import sleephq
from sleephq.models.api_v1_journal_serializer import ApiV1JournalSerializer
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
    api_instance = sleephq.JournalsApi(api_client)
    id = 56 # int | Journal ID
    var_date = '2013-10-20' # date | Date (optional)
    step_count = 'step_count_example' # str | Step Count (optional)
    weight_grams = 56 # int | Weight (Grams) (optional)
    feeling_score = 'feeling_score_example' # str | Feeling Score (optional)
    active_energy_joules = 56 # int | Active Energy (Joules) (optional)
    notes = 'notes_example' # str | Notes (optional)
    sleep_stages = 'sleep_stages_example' # str | Sleep Stages (optional)

    try:
        api_response = api_instance.put_v1_journals_id(id, var_date=var_date, step_count=step_count, weight_grams=weight_grams, feeling_score=feeling_score, active_energy_joules=active_energy_joules, notes=notes, sleep_stages=sleep_stages)
        print("The response of JournalsApi->put_v1_journals_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalsApi->put_v1_journals_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Journal ID | 
 **var_date** | **date**| Date | [optional] 
 **step_count** | **str**| Step Count | [optional] 
 **weight_grams** | **int**| Weight (Grams) | [optional] 
 **feeling_score** | **str**| Feeling Score | [optional] 
 **active_energy_joules** | **int**| Active Energy (Joules) | [optional] 
 **notes** | **str**| Notes | [optional] 
 **sleep_stages** | **str**| Sleep Stages | [optional] 

### Return type

[**ApiV1JournalSerializer**](ApiV1JournalSerializer.md)

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

