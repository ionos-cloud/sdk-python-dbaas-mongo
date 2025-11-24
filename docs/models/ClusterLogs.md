# ClusterLogs

The logs of the MongoDB cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**list[ClusterLogsInstancesInner]**](ClusterLogsInstancesInner.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.cluster_logs import ClusterLogs

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogs from a JSON string
cluster_logs_instance = ClusterLogs.from_json(json)
# print the JSON string representation of the object
print(ClusterLogs.to_json())

# convert the object into a dict
cluster_logs_dict = cluster_logs_instance.to_dict()
# create an instance of ClusterLogs from a dict
cluster_logs_from_dict = ClusterLogs.from_dict(cluster_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


