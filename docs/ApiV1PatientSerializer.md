# ApiV1PatientSerializer

Api_V1_PatientSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1PatientSerializerData**](ApiV1PatientSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_patient_serializer import ApiV1PatientSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatientSerializer from a JSON string
api_v1_patient_serializer_instance = ApiV1PatientSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatientSerializer.to_json())

# convert the object into a dict
api_v1_patient_serializer_dict = api_v1_patient_serializer_instance.to_dict()
# create an instance of ApiV1PatientSerializer from a dict
api_v1_patient_serializer_from_dict = ApiV1PatientSerializer.from_dict(api_v1_patient_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


