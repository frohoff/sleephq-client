# ApiV1TeamSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**energy_unit** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**teams_type** | **str** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_team_serializer_data_attributes import ApiV1TeamSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TeamSerializerDataAttributes from a JSON string
api_v1_team_serializer_data_attributes_instance = ApiV1TeamSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1TeamSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_team_serializer_data_attributes_dict = api_v1_team_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1TeamSerializerDataAttributes from a dict
api_v1_team_serializer_data_attributes_from_dict = ApiV1TeamSerializerDataAttributes.from_dict(api_v1_team_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


