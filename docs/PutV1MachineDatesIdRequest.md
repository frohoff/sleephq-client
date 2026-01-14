# PutV1MachineDatesIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_offset** | **int** | Time Offset | [optional] 

## Example

```python
from sleephq.models.put_v1_machine_dates_id_request import PutV1MachineDatesIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutV1MachineDatesIdRequest from a JSON string
put_v1_machine_dates_id_request_instance = PutV1MachineDatesIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutV1MachineDatesIdRequest.to_json())

# convert the object into a dict
put_v1_machine_dates_id_request_dict = put_v1_machine_dates_id_request_instance.to_dict()
# create an instance of PutV1MachineDatesIdRequest from a dict
put_v1_machine_dates_id_request_from_dict = PutV1MachineDatesIdRequest.from_dict(put_v1_machine_dates_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


