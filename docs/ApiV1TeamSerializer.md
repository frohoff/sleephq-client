# ApiV1TeamSerializer

Api_V1_TeamSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1TeamSerializerData**](ApiV1TeamSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_team_serializer import ApiV1TeamSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TeamSerializer from a JSON string
api_v1_team_serializer_instance = ApiV1TeamSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1TeamSerializer.to_json())

# convert the object into a dict
api_v1_team_serializer_dict = api_v1_team_serializer_instance.to_dict()
# create an instance of ApiV1TeamSerializer from a dict
api_v1_team_serializer_from_dict = ApiV1TeamSerializer.from_dict(api_v1_team_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


