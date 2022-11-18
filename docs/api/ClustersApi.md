# ClustersApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_delete**](ClustersApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a Cluster |
| [**clusters_find_by_id**](ClustersApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Get a cluster by id |
| [**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | Get Clusters |
| [**clusters_patch**](ClustersApi.md#clusters_patch) | **PATCH** /clusters/{clusterId} | Patch a cluster |
| [**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | Create a Cluster |


# **clusters_delete**
> ClusterResponse clusters_delete(cluster_id)

Delete a Cluster

Deletes a MongoDB cluster.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/databases/mongodb
configuration = ionoscloud_dbaas_mongo.Configuration(
    host = 'https://api.ionos.com/databases/mongodb',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dbaas_mongo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # Delete a Cluster
        api_response = api_instance.clusters_delete(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_find_by_id**
> ClusterResponse clusters_find_by_id(cluster_id)

Get a cluster by id

Get a cluster by id.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/databases/mongodb
configuration = ionoscloud_dbaas_mongo.Configuration(
    host = 'https://api.ionos.com/databases/mongodb',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dbaas_mongo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # Get a cluster by id
        api_response = api_instance.clusters_find_by_id(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_get**
> ClusterList clusters_get(filter_name=filter_name)

Get Clusters

Retrieves a list of MongoDB clusters.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/databases/mongodb
configuration = ionoscloud_dbaas_mongo.Configuration(
    host = 'https://api.ionos.com/databases/mongodb',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dbaas_mongo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    try:
        # Get Clusters
        api_response = api_instance.clusters_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter_name** | **str**| Response filter to list only the MongoDB clusters that contain the specified name. The value is case insensitive and matched on the &#39;displayName&#39; field.  | [optional]  |

### Return type

[**ClusterList**](../models/ClusterList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_patch**
> ClusterResponse clusters_patch(cluster_id, patch_cluster_request)

Patch a cluster

Patch attributes of a MongoDB cluster.

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/databases/mongodb
configuration = ionoscloud_dbaas_mongo.Configuration(
    host = 'https://api.ionos.com/databases/mongodb',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dbaas_mongo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    patch_cluster_request = ionoscloud_dbaas_mongo.PatchClusterRequest() # PatchClusterRequest | Part of the cluster which should be modified.
    try:
        # Patch a cluster
        api_response = api_instance.clusters_patch(cluster_id, patch_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **patch_cluster_request** | [**PatchClusterRequest**](../models/PatchClusterRequest.md)| Part of the cluster which should be modified. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **clusters_post**
> ClusterResponse clusters_post(create_cluster_request)

Create a Cluster

Creates a new MongoDB cluster. 

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/databases/mongodb
configuration = ionoscloud_dbaas_mongo.Configuration(
    host = 'https://api.ionos.com/databases/mongodb',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dbaas_mongo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    create_cluster_request = ionoscloud_dbaas_mongo.CreateClusterRequest() # CreateClusterRequest | The cluster to be created.
    try:
        # Create a Cluster
        api_response = api_instance.clusters_post(create_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ClustersApi.clusters_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_cluster_request** | [**CreateClusterRequest**](../models/CreateClusterRequest.md)| The cluster to be created. |  |

### Return type

[**ClusterResponse**](../models/ClusterResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

