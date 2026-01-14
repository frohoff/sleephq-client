# PostV1MeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 

## Example

```python
from sleephq.models.post_v1_me_request import PostV1MeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostV1MeRequest from a JSON string
post_v1_me_request_instance = PostV1MeRequest.from_json(json)
# print the JSON string representation of the object
print(PostV1MeRequest.to_json())

# convert the object into a dict
post_v1_me_request_dict = post_v1_me_request_instance.to_dict()
# create an instance of PostV1MeRequest from a dict
post_v1_me_request_from_dict = PostV1MeRequest.from_dict(post_v1_me_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


