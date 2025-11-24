# ionoscloud_dbaas_mongo.SnapshotsApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_snapshots_get**](SnapshotsApi.md#clusters_snapshots_get) | **GET** /clusters/{clusterId}/snapshots | Get the snapshots of your cluster


# **clusters_snapshots_get**
> SnapshotList clusters_snapshots_get(cluster_id, limit=limit, offset=offset)

Get the snapshots of your cluster

Retrieves MongoDB snapshots.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.snapshot_list import SnapshotList
from ionoscloud_dbaas_mongo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/databases/mongodb
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dbaas_mongo.Configuration(
    host = "https://api.ionos.com/databases/mongodb"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ionoscloud_dbaas_mongo.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dbaas_mongo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dbaas_mongo.SnapshotsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    limit = 100 # int | The maximum number of elements to return. Use together with 'offset' for pagination. (optional) (default to 100)
    offset = 0 # int | The first element to return. Use together with 'limit' for pagination. (optional) (default to 0)

    try:
        # Get the snapshots of your cluster
        api_response = api_instance.clusters_snapshots_get(cluster_id, limit=limit, offset=offset)
        print("The response of SnapshotsApi->clusters_snapshots_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->clusters_snapshots_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100]
 **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0]

### Return type

[**SnapshotList**](SnapshotList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance)  |  * Content-Type - The content type of the response. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

