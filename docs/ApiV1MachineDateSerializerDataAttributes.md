# ApiV1MachineDateSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**usage** | **int** |  | [optional] 
**machine_id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**time_offset** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**large_leak** | **int** |  | [optional] 
**ahi_summary** | **object** |  | [optional] 
**pressure_summary** | **object** |  | [optional] 
**leak_rate_summary** | **object** |  | [optional] 
**flow_limit_summary** | **object** |  | [optional] 
**resp_rate_summary** | **object** |  | [optional] 
**epap_summary** | **object** |  | [optional] 
**machine_settings** | **object** |  | [optional] 
**pulse_rate_summary** | **object** |  | [optional] 
**spo2_summary** | **object** |  | [optional] 
**movement_summary** | **object** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_date_serializer_data_attributes import ApiV1MachineDateSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineDateSerializerDataAttributes from a JSON string
api_v1_machine_date_serializer_data_attributes_instance = ApiV1MachineDateSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineDateSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_machine_date_serializer_data_attributes_dict = api_v1_machine_date_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1MachineDateSerializerDataAttributes from a dict
api_v1_machine_date_serializer_data_attributes_from_dict = ApiV1MachineDateSerializerDataAttributes.from_dict(api_v1_machine_date_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


