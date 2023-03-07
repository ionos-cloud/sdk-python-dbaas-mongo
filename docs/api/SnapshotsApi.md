# SnapshotsApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_snapshots_get**](SnapshotsApi.md#clusters_snapshots_get) | **GET** /clusters/{clusterId}/snapshots | Get the snapshots of your cluster |


# **clusters_snapshots_get**
> SnapshotList clusters_snapshots_get(cluster_id, limit=limit, offset=offset)

Get the snapshots of your cluster

Retrieves MongoDB snapshots.

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
    api_instance = ionoscloud_dbaas_mongo.SnapshotsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # Get the snapshots of your cluster
        api_response = api_instance.clusters_snapshots_get(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.clusters_snapshots_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100] |
| **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0] |

### Return type

[**SnapshotList**](../models/SnapshotList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

