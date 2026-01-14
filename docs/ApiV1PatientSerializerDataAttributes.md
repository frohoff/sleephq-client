# ApiV1PatientSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_patient_serializer_data_attributes import ApiV1PatientSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatientSerializerDataAttributes from a JSON string
api_v1_patient_serializer_data_attributes_instance = ApiV1PatientSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatientSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_patient_serializer_data_attributes_dict = api_v1_patient_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1PatientSerializerDataAttributes from a dict
api_v1_patient_serializer_data_attributes_from_dict = ApiV1PatientSerializerDataAttributes.from_dict(api_v1_patient_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


