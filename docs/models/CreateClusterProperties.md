# CreateClusterProperties

The properties with all data needed to create a new MongoDB cluster. 
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **template_id** | **str** | The unique ID of the template, which specifies the number of cores, storage size, and memory.  |  |
| **mongo_db_version** | **str** | The MongoDB version of your cluster. | [optional]  |
| **instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondaries).  |  |
| **connections** | [**list[Connection]**](Connection.md) |  |  |
| **location** | **str** | The physical location where the cluster will be created. This is the location where all your instances will be located. This property is immutable.  |  |
| **display_name** | **str** | The name of your cluster. |  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |


