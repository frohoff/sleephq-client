# ApiV1DeviceSerializer

Api_V1_DeviceSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1DeviceSerializerData**](ApiV1DeviceSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_device_serializer import ApiV1DeviceSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DeviceSerializer from a JSON string
api_v1_device_serializer_instance = ApiV1DeviceSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1DeviceSerializer.to_json())

# convert the object into a dict
api_v1_device_serializer_dict = api_v1_device_serializer_instance.to_dict()
# create an instance of ApiV1DeviceSerializer from a dict
api_v1_device_serializer_from_dict = ApiV1DeviceSerializer.from_dict(api_v1_device_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


