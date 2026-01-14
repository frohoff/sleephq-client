# ApiV1TeamSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1TeamSerializerDataAttributes**](ApiV1TeamSerializerDataAttributes.md) |  | [optional] 
**relationships** | [**ApiV1PatientSerializerDataRelationships**](ApiV1PatientSerializerDataRelationships.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_team_serializer_data import ApiV1TeamSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TeamSerializerData from a JSON string
api_v1_team_serializer_data_instance = ApiV1TeamSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1TeamSerializerData.to_json())

# convert the object into a dict
api_v1_team_serializer_data_dict = api_v1_team_serializer_data_instance.to_dict()
# create an instance of ApiV1TeamSerializerData from a dict
api_v1_team_serializer_data_from_dict = ApiV1TeamSerializerData.from_dict(api_v1_team_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


