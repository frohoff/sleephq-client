# PostV1TeamsTeamIdImportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**programatic** | **bool** | Deprecated. | [optional] 
**device_id** | **int** | The device type that the data is from. Find a list of device ids using the /devices endpoint. | [optional] 
**name** | **str** | The name of the import to show in the UI. | [optional] 

## Example

```python
from sleephq.models.post_v1_teams_team_id_imports_request import PostV1TeamsTeamIdImportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostV1TeamsTeamIdImportsRequest from a JSON string
post_v1_teams_team_id_imports_request_instance = PostV1TeamsTeamIdImportsRequest.from_json(json)
# print the JSON string representation of the object
print(PostV1TeamsTeamIdImportsRequest.to_json())

# convert the object into a dict
post_v1_teams_team_id_imports_request_dict = post_v1_teams_team_id_imports_request_instance.to_dict()
# create an instance of PostV1TeamsTeamIdImportsRequest from a dict
post_v1_teams_team_id_imports_request_from_dict = PostV1TeamsTeamIdImportsRequest.from_dict(post_v1_teams_team_id_imports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


