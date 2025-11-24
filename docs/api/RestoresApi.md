# ionoscloud_dbaas_mongo.RestoresApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_restore_post**](RestoresApi.md#clusters_restore_post) | **POST** /clusters/{clusterId}/restore | In-place restore of a cluster


# **clusters_restore_post**
> clusters_restore_post(cluster_id, create_restore_request)

In-place restore of a cluster

Triggers an in-place restore of the given MongoDB cluster.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.create_restore_request import CreateRestoreRequest
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
    api_instance = ionoscloud_dbaas_mongo.RestoresApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    create_restore_request = ionoscloud_dbaas_mongo.CreateRestoreRequest() # CreateRestoreRequest | The restore request to create.

    try:
        # In-place restore of a cluster
        api_instance.clusters_restore_post(cluster_id, create_restore_request)
    except Exception as e:
        print("Exception when calling RestoresApi->clusters_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **create_restore_request** | [**CreateRestoreRequest**](CreateRestoreRequest.md)| The restore request to create. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation. |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance)  |  * Content-Type - The content type of the response. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

