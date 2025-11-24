# SnapshotProperties

Properties of a snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The MongoDB version this backup was created from. | [optional] 
**size** | **int** | The size of the snapshot in Mebibytes. | [optional] 
**creation_time** | **datetime** | The date the resource was created. | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.snapshot_properties import SnapshotProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotProperties from a JSON string
snapshot_properties_instance = SnapshotProperties.from_json(json)
# print the JSON string representation of the object
print(SnapshotProperties.to_json())

# convert the object into a dict
snapshot_properties_dict = snapshot_properties_instance.to_dict()
# create an instance of SnapshotProperties from a dict
snapshot_properties_from_dict = SnapshotProperties.from_dict(snapshot_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


