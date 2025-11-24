# ClusterLogsInstancesInnerMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.cluster_logs_instances_inner_messages_inner import ClusterLogsInstancesInnerMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogsInstancesInnerMessagesInner from a JSON string
cluster_logs_instances_inner_messages_inner_instance = ClusterLogsInstancesInnerMessagesInner.from_json(json)
# print the JSON string representation of the object
print(ClusterLogsInstancesInnerMessagesInner.to_json())

# convert the object into a dict
cluster_logs_instances_inner_messages_inner_dict = cluster_logs_instances_inner_messages_inner_instance.to_dict()
# create an instance of ClusterLogsInstancesInnerMessagesInner from a dict
cluster_logs_instances_inner_messages_inner_from_dict = ClusterLogsInstancesInnerMessagesInner.from_dict(cluster_logs_instances_inner_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


