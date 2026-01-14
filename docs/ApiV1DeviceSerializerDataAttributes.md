# ApiV1DeviceSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_device_serializer_data_attributes import ApiV1DeviceSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DeviceSerializerDataAttributes from a JSON string
api_v1_device_serializer_data_attributes_instance = ApiV1DeviceSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1DeviceSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_device_serializer_data_attributes_dict = api_v1_device_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1DeviceSerializerDataAttributes from a dict
api_v1_device_serializer_data_attributes_from_dict = ApiV1DeviceSerializerDataAttributes.from_dict(api_v1_device_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


