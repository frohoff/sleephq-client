# ApiV1UserSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1UserSerializerDataAttributes**](ApiV1UserSerializerDataAttributes.md) |  | [optional] 
**relationships** | [**ApiV1UserSerializerDataRelationships**](ApiV1UserSerializerDataRelationships.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_user_serializer_data import ApiV1UserSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UserSerializerData from a JSON string
api_v1_user_serializer_data_instance = ApiV1UserSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1UserSerializerData.to_json())

# convert the object into a dict
api_v1_user_serializer_data_dict = api_v1_user_serializer_data_instance.to_dict()
# create an instance of ApiV1UserSerializerData from a dict
api_v1_user_serializer_data_from_dict = ApiV1UserSerializerData.from_dict(api_v1_user_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


