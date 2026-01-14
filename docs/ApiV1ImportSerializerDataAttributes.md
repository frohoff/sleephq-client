# ApiV1ImportSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**progress** | **int** |  | [optional] 
**machine_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**programatic** | **bool** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_import_serializer_data_attributes import ApiV1ImportSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ImportSerializerDataAttributes from a JSON string
api_v1_import_serializer_data_attributes_instance = ApiV1ImportSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1ImportSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_import_serializer_data_attributes_dict = api_v1_import_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1ImportSerializerDataAttributes from a dict
api_v1_import_serializer_data_attributes_from_dict = ApiV1ImportSerializerDataAttributes.from_dict(api_v1_import_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


