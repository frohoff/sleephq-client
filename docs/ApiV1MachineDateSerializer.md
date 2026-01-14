# ApiV1MachineDateSerializer

Api_V1_MachineDateSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1MachineDateSerializerData**](ApiV1MachineDateSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_date_serializer import ApiV1MachineDateSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineDateSerializer from a JSON string
api_v1_machine_date_serializer_instance = ApiV1MachineDateSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineDateSerializer.to_json())

# convert the object into a dict
api_v1_machine_date_serializer_dict = api_v1_machine_date_serializer_instance.to_dict()
# create an instance of ApiV1MachineDateSerializer from a dict
api_v1_machine_date_serializer_from_dict = ApiV1MachineDateSerializer.from_dict(api_v1_machine_date_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


