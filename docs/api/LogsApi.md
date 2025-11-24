# ionoscloud_dbaas_mongo.LogsApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_logs_get**](LogsApi.md#clusters_logs_get) | **GET** /clusters/{clusterId}/logs | Get logs of your cluster


# **clusters_logs_get**
> ClusterLogs clusters_logs_get(cluster_id, start=start, end=end, direction=direction, limit=limit)

Get logs of your cluster

Retrieves MongoDB logs based on the given parameters.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.cluster_logs import ClusterLogs
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
    api_instance = ionoscloud_dbaas_mongo.LogsApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    start = '2013-10-20T19:20:30+01:00' # datetime | The start time for the query in RFC3339 format. Must not be more than 30 days ago but before the end parameter. The default is 30 days ago. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | The end time for the query in RFC3339 format. Must not be greater than now. The default is the current timestamp. (optional)
    direction = BACKWARD # str | The direction in which to scan through the logs. The logs are returned in order of the direction. (optional) (default to BACKWARD)
    limit = 100 # int | The maximal number of log lines to return.  If the limit is reached then log lines will be cut at the end (respecting the scan direction). (optional) (default to 100)

    try:
        # Get logs of your cluster
        api_response = api_instance.clusters_logs_get(cluster_id, start=start, end=end, direction=direction, limit=limit)
        print("The response of LogsApi->clusters_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->clusters_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **start** | **datetime**| The start time for the query in RFC3339 format. Must not be more than 30 days ago but before the end parameter. The default is 30 days ago. | [optional] 
 **end** | **datetime**| The end time for the query in RFC3339 format. Must not be greater than now. The default is the current timestamp. | [optional] 
 **direction** | **str**| The direction in which to scan through the logs. The logs are returned in order of the direction. | [optional] [default to BACKWARD]
 **limit** | **int**| The maximal number of log lines to return.  If the limit is reached then log lines will be cut at the end (respecting the scan direction). | [optional] [default to 100]

### Return type

[**ClusterLogs**](ClusterLogs.md)

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

