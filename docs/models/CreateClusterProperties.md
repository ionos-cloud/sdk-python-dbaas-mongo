# CreateClusterProperties

The properties with all data needed to create a new MongoDB cluster. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The cluster type, either &#x60;replicaset&#x60; or &#x60;sharded-cluster&#x60;.  | [optional] 
**template_id** | **str** | The unique ID of the template, which specifies the number of cores, storage size, and memory. You cannot downgrade to a smaller template or minor edition (e.g. from business to playground). To get a list of all templates to confirm the changes use the /templates endpoint.  | [optional] 
**mongo_db_version** | **str** | The MongoDB version of your cluster. | 
**instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondaries).  | 
**shards** | **int** | The total number of shards in the cluster.  | [optional] 
**connections** | [**list[Connection]**](Connection.md) |  | 
**location** | **str** | The physical location where the cluster will be created. This is the location where all your instances will be located. This property is immutable.  | 
**backup** | [**BackupProperties**](BackupProperties.md) |  | [optional] 
**display_name** | **str** | The name of your cluster. | 
**maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**bi_connector** | [**BiConnectorProperties**](BiConnectorProperties.md) |  | [optional] 
**from_backup** | [**CreateRestoreRequest**](CreateRestoreRequest.md) |  | [optional] 
**edition** | **str** | The cluster edition. | [optional] 
**cores** | **int** | The number of CPU cores per instance. | [optional] 
**ram** | **int** | The amount of memory per instance in megabytes. Has to be a multiple of 1024. | [optional] 
**storage_size** | **int** | The amount of storage per instance in megabytes. | [optional] 
**storage_type** | [**StorageType**](StorageType.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.create_cluster_properties import CreateClusterProperties

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterProperties from a JSON string
create_cluster_properties_instance = CreateClusterProperties.from_json(json)
# print the JSON string representation of the object
print(CreateClusterProperties.to_json())

# convert the object into a dict
create_cluster_properties_dict = create_cluster_properties_instance.to_dict()
# create an instance of CreateClusterProperties from a dict
create_cluster_properties_from_dict = CreateClusterProperties.from_dict(create_cluster_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


