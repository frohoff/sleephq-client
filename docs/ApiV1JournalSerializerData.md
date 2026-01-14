# ApiV1JournalSerializerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiV1JournalSerializerDataAttributes**](ApiV1JournalSerializerDataAttributes.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from sleephq.models.api_v1_journal_serializer_data import ApiV1JournalSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1JournalSerializerData from a JSON string
api_v1_journal_serializer_data_instance = ApiV1JournalSerializerData.from_json(json)
# print the JSON string representation of the object
print(ApiV1JournalSerializerData.to_json())

# convert the object into a dict
api_v1_journal_serializer_data_dict = api_v1_journal_serializer_data_instance.to_dict()
# create an instance of ApiV1JournalSerializerData from a dict
api_v1_journal_serializer_data_from_dict = ApiV1JournalSerializerData.from_dict(api_v1_journal_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


