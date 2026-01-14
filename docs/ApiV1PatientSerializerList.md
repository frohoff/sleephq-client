# ApiV1PatientSerializerList

Api_V1_PatientSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1PatientSerializerData]**](ApiV1PatientSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_patient_serializer_list import ApiV1PatientSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatientSerializerList from a JSON string
api_v1_patient_serializer_list_instance = ApiV1PatientSerializerList.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatientSerializerList.to_json())

# convert the object into a dict
api_v1_patient_serializer_list_dict = api_v1_patient_serializer_list_instance.to_dict()
# create an instance of ApiV1PatientSerializerList from a dict
api_v1_patient_serializer_list_from_dict = ApiV1PatientSerializerList.from_dict(api_v1_patient_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


