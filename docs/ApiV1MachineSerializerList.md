# ApiV1MachineSerializerList

Api_V1_MachineSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1MachineSerializerData]**](ApiV1MachineSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_serializer_list import ApiV1MachineSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineSerializerList from a JSON string
api_v1_machine_serializer_list_instance = ApiV1MachineSerializerList.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineSerializerList.to_json())

# convert the object into a dict
api_v1_machine_serializer_list_dict = api_v1_machine_serializer_list_instance.to_dict()
# create an instance of ApiV1MachineSerializerList from a dict
api_v1_machine_serializer_list_from_dict = ApiV1MachineSerializerList.from_dict(api_v1_machine_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


