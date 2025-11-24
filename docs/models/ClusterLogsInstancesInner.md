# ClusterLogsInstancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the MongoDB instance. | [optional] 
**messages** | [**list[ClusterLogsInstancesInnerMessagesInner]**](ClusterLogsInstancesInnerMessagesInner.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.cluster_logs_instances_inner import ClusterLogsInstancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogsInstancesInner from a JSON string
cluster_logs_instances_inner_instance = ClusterLogsInstancesInner.from_json(json)
# print the JSON string representation of the object
print(ClusterLogsInstancesInner.to_json())

# convert the object into a dict
cluster_logs_instances_inner_dict = cluster_logs_instances_inner_instance.to_dict()
# create an instance of ClusterLogsInstancesInner from a dict
cluster_logs_instances_inner_from_dict = ClusterLogsInstancesInner.from_dict(cluster_logs_instances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


