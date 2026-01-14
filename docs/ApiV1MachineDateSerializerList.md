# ApiV1MachineDateSerializerList

Api_V1_MachineDateSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1MachineDateSerializerData]**](ApiV1MachineDateSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_machine_date_serializer_list import ApiV1MachineDateSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1MachineDateSerializerList from a JSON string
api_v1_machine_date_serializer_list_instance = ApiV1MachineDateSerializerList.from_json(json)
# print the JSON string representation of the object
print(ApiV1MachineDateSerializerList.to_json())

# convert the object into a dict
api_v1_machine_date_serializer_list_dict = api_v1_machine_date_serializer_list_instance.to_dict()
# create an instance of ApiV1MachineDateSerializerList from a dict
api_v1_machine_date_serializer_list_from_dict = ApiV1MachineDateSerializerList.from_dict(api_v1_machine_date_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


