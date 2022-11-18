# PatchClusterProperties

Properties of the payload to change a cluster.
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **display_name** | **str** | The name of your cluster. | [optional]  |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **instances** | **int** | The total number of instances in the cluster (one primary and n-1 secondaries).  | [optional]  |
| **connections** | [**list[Connection]**](Connection.md) |  | [optional]  |
| **template_id** | **str** | The unique ID of the template, which specifies the number of cores, storage size, and memory. You cannot downgrade to a smaller template or minor edition (e.g. from business to playground). To get a list of all templates to confirm the changes use the /templates endpoint.  | [optional]  |


