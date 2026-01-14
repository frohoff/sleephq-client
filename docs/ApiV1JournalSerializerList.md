# ApiV1JournalSerializerList

Api_V1_JournalSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1JournalSerializerData]**](ApiV1JournalSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_journal_serializer_list import ApiV1JournalSerializerList

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1JournalSerializerList from a JSON string
api_v1_journal_serializer_list_instance = ApiV1JournalSerializerList.from_json(json)
# print the JSON string representation of the object
print(ApiV1JournalSerializerList.to_json())

# convert the object into a dict
api_v1_journal_serializer_list_dict = api_v1_journal_serializer_list_instance.to_dict()
# create an instance of ApiV1JournalSerializerList from a dict
api_v1_journal_serializer_list_from_dict = ApiV1JournalSerializerList.from_dict(api_v1_journal_serializer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


