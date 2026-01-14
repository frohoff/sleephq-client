# ApiV1UserSerializer

Api_V1_UserSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1UserSerializerData**](ApiV1UserSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_user_serializer import ApiV1UserSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UserSerializer from a JSON string
api_v1_user_serializer_instance = ApiV1UserSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1UserSerializer.to_json())

# convert the object into a dict
api_v1_user_serializer_dict = api_v1_user_serializer_instance.to_dict()
# create an instance of ApiV1UserSerializer from a dict
api_v1_user_serializer_from_dict = ApiV1UserSerializer.from_dict(api_v1_user_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


