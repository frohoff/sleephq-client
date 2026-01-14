# ApiV1MachineSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1MachineSerializerDataAttributes**](ApiV1MachineSerializerDataAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_serializer_data import ApiV1MachineSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineSerializerData from a JSON string
api_v1_machine_serializer_data_instance = ApiV1MachineSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineSerializerData.to_json())

# convert the object into a dict
api_v1_machine_serializer_data_dict = api_v1_machine_serializer_data_instance.to_dict()
# create an instance of ApiV1MachineSerializerData from a dict
api_v1_machine_serializer_data_from_dict = ApiV1MachineSerializerData.from_dict(api_v1_machine_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


