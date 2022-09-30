# ClusterProperties

Properties of a database cluster.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **display_name** | **str** | The name of your cluster. | [optional]  |
| **mongo_db_version** | **str** | The MongoDB version of your cluster. | [optional]  |
| **location** | **str** | The physical location where the cluster will be created. This is the location where all your instances will be located. This property is immutable.  | [optional]  |
| **instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondaries).  | [optional]  |
| **connections** | [**list[Connection]**](Connection.md) |  | [optional]  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **template_id** | **str** | The unique ID of the template, which specifies the number of cores, storage size, and memory.  | [optional]  |
| **connection_string** | **str** | The connection string for your cluster. | [optional]  |


