# ApiV1MachineDateSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1MachineDateSerializerDataAttributes**](ApiV1MachineDateSerializerDataAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_date_serializer_data import ApiV1MachineDateSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineDateSerializerData from a JSON string
api_v1_machine_date_serializer_data_instance = ApiV1MachineDateSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineDateSerializerData.to_json())

# convert the object into a dict
api_v1_machine_date_serializer_data_dict = api_v1_machine_date_serializer_data_instance.to_dict()
# create an instance of ApiV1MachineDateSerializerData from a dict
api_v1_machine_date_serializer_data_from_dict = ApiV1MachineDateSerializerData.from_dict(api_v1_machine_date_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


