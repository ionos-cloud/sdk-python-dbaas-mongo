# CreateRestoreRequest

The restore request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_id** | **str** | The unique ID of the snapshot you want to restore. | [optional] 
**recovery_target_time** | **datetime** | If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp.  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.create_restore_request import CreateRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRestoreRequest from a JSON string
create_restore_request_instance = CreateRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRestoreRequest.to_json())

# convert the object into a dict
create_restore_request_dict = create_restore_request_instance.to_dict()
# create an instance of CreateRestoreRequest from a dict
create_restore_request_from_dict = CreateRestoreRequest.from_dict(create_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


