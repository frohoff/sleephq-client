# PostV1TeamsTeamIdJournalsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date | [optional] 
**step_count** | **str** | Step Count | [optional] 
**weight_grams** | **int** | Weight (Grams) | [optional] 
**feeling_score** | **str** | Feeling Score | [optional] 
**active_energy_joules** | **int** | Active Energy (Joules) | [optional] 
**notes** | **str** | Notes | [optional] 
**sleep_stages** | **str** | Sleep Stages | [optional] 

## Example

```python
from sleephq.models.post_v1_teams_team_id_journals_request import PostV1TeamsTeamIdJournalsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostV1TeamsTeamIdJournalsRequest from a JSON string
post_v1_teams_team_id_journals_request_instance = PostV1TeamsTeamIdJournalsRequest.from_json(json)
# print the JSON string representation of the object
print(PostV1TeamsTeamIdJournalsRequest.to_json())

# convert the object into a dict
post_v1_teams_team_id_journals_request_dict = post_v1_teams_team_id_journals_request_instance.to_dict()
# create an instance of PostV1TeamsTeamIdJournalsRequest from a dict
post_v1_teams_team_id_journals_request_from_dict = PostV1TeamsTeamIdJournalsRequest.from_dict(post_v1_teams_team_id_journals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


