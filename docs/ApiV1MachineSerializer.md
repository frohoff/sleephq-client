# ApiV1MachineSerializer

Api_V1_MachineSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1MachineSerializerData**](ApiV1MachineSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_serializer import ApiV1MachineSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineSerializer from a JSON string
api_v1_machine_serializer_instance = ApiV1MachineSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineSerializer.to_json())

# convert the object into a dict
api_v1_machine_serializer_dict = api_v1_machine_serializer_instance.to_dict()
# create an instance of ApiV1MachineSerializer from a dict
api_v1_machine_serializer_from_dict = ApiV1MachineSerializer.from_dict(api_v1_machine_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


