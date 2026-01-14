# ApiV1ImportSerializer

Api_V1_ImportSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1ImportSerializerData**](ApiV1ImportSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_import_serializer import ApiV1ImportSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportSerializer from a JSON string
api_v1_import_serializer_instance = ApiV1ImportSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportSerializer.to_json())

# convert the object into a dict
api_v1_import_serializer_dict = api_v1_import_serializer_instance.to_dict()
# create an instance of ApiV1ImportSerializer from a dict
api_v1_import_serializer_from_dict = ApiV1ImportSerializer.from_dict(api_v1_import_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


