# ApiV1JournalSerializerDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**step_count** | **int** |  | [optional] 
**weight_grams** | **int** |  | [optional] 
**feeling_score** | **int** |  | [optional] 
**sleep_stages** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_journal_serializer_data_attributes import ApiV1JournalSerializerDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1JournalSerializerDataAttributes from a JSON string
api_v1_journal_serializer_data_attributes_instance = ApiV1JournalSerializerDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiV1JournalSerializerDataAttributes.to_json())

# convert the object into a dict
api_v1_journal_serializer_data_attributes_dict = api_v1_journal_serializer_data_attributes_instance.to_dict()
# create an instance of ApiV1JournalSerializerDataAttributes from a dict
api_v1_journal_serializer_data_attributes_from_dict = ApiV1JournalSerializerDataAttributes.from_dict(api_v1_journal_serializer_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


