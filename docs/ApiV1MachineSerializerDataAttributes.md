# ApiV1MachineSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**model** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_serializer_data_attributes import ApiV1MachineSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineSerializerDataAttributes from a JSON string
api_v1_machine_serializer_data_attributes_instance = ApiV1MachineSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_machine_serializer_data_attributes_dict = api_v1_machine_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1MachineSerializerDataAttributes from a dict
api_v1_machine_serializer_data_attributes_from_dict = ApiV1MachineSerializerDataAttributes.from_dict(api_v1_machine_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


