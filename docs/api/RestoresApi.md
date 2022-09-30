# RestoresApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_restore_post**](RestoresApi.md#clusters_restore_post) | **POST** /clusters/{clusterId}/restore | In-place restore of a cluster |


# **clusters_restore_post**
> clusters_restore_post(cluster_id, create_restore_request)

In-place restore of a cluster

Triggers an in-place restore of the given MongoDB cluster.

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
    api_instance = ionoscloud_dbaas_mongo.RestoresApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    create_restore_request = ionoscloud_dbaas_mongo.CreateRestoreRequest() # CreateRestoreRequest | The restore request to create.
    try:
        # In-place restore of a cluster
        api_instance.clusters_restore_post(cluster_id, create_restore_request)
    except ApiException as e:
        print('Exception when calling RestoresApi.clusters_restore_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **create_restore_request** | [**CreateRestoreRequest**](CreateRestoreRequest.md)| The restore request to create. |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

