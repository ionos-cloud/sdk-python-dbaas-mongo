# SnapshotResponse

A database snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResourceType**](ResourceType.md) |  | [optional] 
**id** | **str** | The unique ID of the resource. | [optional] 
**properties** | [**SnapshotProperties**](SnapshotProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.snapshot_response import SnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResponse from a JSON string
snapshot_response_instance = SnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotResponse.to_json())

# convert the object into a dict
snapshot_response_dict = snapshot_response_instance.to_dict()
# create an instance of SnapshotResponse from a dict
snapshot_response_from_dict = SnapshotResponse.from_dict(snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


