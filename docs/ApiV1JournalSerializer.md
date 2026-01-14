# ApiV1JournalSerializer

Api_V1_JournalSerializer model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1JournalSerializerData**](ApiV1JournalSerializerData.md) |  | [optional] 

## Example

```python
from sleephq.models.api_v1_journal_serializer import ApiV1JournalSerializer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1JournalSerializer from a JSON string
api_v1_journal_serializer_instance = ApiV1JournalSerializer.from_json(json)
# print the JSON string representation of the object
print(ApiV1JournalSerializer.to_json())

# convert the object into a dict
api_v1_journal_serializer_dict = api_v1_journal_serializer_instance.to_dict()
# create an instance of ApiV1JournalSerializer from a dict
api_v1_journal_serializer_from_dict = ApiV1JournalSerializer.from_dict(api_v1_journal_serializer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


