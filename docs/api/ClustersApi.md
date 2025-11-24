# ionoscloud_dbaas_mongo.ClustersApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_delete**](ClustersApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a Cluster
[**clusters_find_by_id**](ClustersApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Get a cluster by id
[**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | Get Clusters
[**clusters_patch**](ClustersApi.md#clusters_patch) | **PATCH** /clusters/{clusterId} | Patch a cluster
[**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | Create a Cluster
[**clusters_versions_get**](ClustersApi.md#clusters_versions_get) | **GET** /clusters/{clusterId}/versions | Get available MongoDB versions for this cluster


# **clusters_delete**
> ClusterResponse clusters_delete(cluster_id)

Delete a Cluster

Deletes a MongoDB cluster.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.cluster_response import ClusterResponse
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
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.

    try:
        # Delete a Cluster
        api_response = api_instance.clusters_delete(cluster_id)
        print("The response of ClustersApi->clusters_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cluster to be deleted is automatically set to &#x60;state &#x3D; DESTROYING&#x60;.  |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance)  |  * Content-Type - The content type of the response. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_find_by_id**
> ClusterResponse clusters_find_by_id(cluster_id)

Get a cluster by id

Get a cluster by id.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.cluster_response import ClusterResponse
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
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.

    try:
        # Get a cluster by id
        api_response = api_instance.clusters_find_by_id(cluster_id)
        print("The response of ClustersApi->clusters_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

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

# **clusters_get**
> ClusterList clusters_get(limit=limit, offset=offset, filter_name=filter_name)

Get Clusters

Retrieves a list of MongoDB clusters.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.cluster_list import ClusterList
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
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    limit = 100 # int | The maximum number of elements to return. Use together with 'offset' for pagination. (optional) (default to 100)
    offset = 0 # int | The first element to return. Use together with 'limit' for pagination. (optional) (default to 0)
    filter_name = 'filter_name_example' # str | Response filter to list only the MongoDB clusters that contain the specified name. The value is case insensitive and matched on the 'displayName' field.  (optional)

    try:
        # Get Clusters
        api_response = api_instance.clusters_get(limit=limit, offset=offset, filter_name=filter_name)
        print("The response of ClustersApi->clusters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements to return. Use together with &#39;offset&#39; for pagination. | [optional] [default to 100]
 **offset** | **int**| The first element to return. Use together with &#39;limit&#39; for pagination. | [optional] [default to 0]
 **filter_name** | **str**| Response filter to list only the MongoDB clusters that contain the specified name. The value is case insensitive and matched on the &#39;displayName&#39; field.  | [optional] 

### Return type

[**ClusterList**](ClusterList.md)

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

# **clusters_patch**
> ClusterResponse clusters_patch(cluster_id, patch_cluster_request)

Patch a cluster

Patch attributes of a MongoDB cluster.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.cluster_response import ClusterResponse
from ionoscloud_dbaas_mongo.models.patch_cluster_request import PatchClusterRequest
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
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    patch_cluster_request = ionoscloud_dbaas_mongo.PatchClusterRequest() # PatchClusterRequest | Part of the cluster which should be modified.

    try:
        # Patch a cluster
        api_response = api_instance.clusters_patch(cluster_id, patch_cluster_request)
        print("The response of ClustersApi->clusters_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 
 **patch_cluster_request** | [**PatchClusterRequest**](PatchClusterRequest.md)| Part of the cluster which should be modified. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance)  |  * Content-Type - The content type of the response. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_post**
> ClusterResponse clusters_post(create_cluster_request)

Create a Cluster

Creates a new MongoDB cluster.


### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.cluster_response import ClusterResponse
from ionoscloud_dbaas_mongo.models.create_cluster_request import CreateClusterRequest
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
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    create_cluster_request = ionoscloud_dbaas_mongo.CreateClusterRequest() # CreateClusterRequest | The cluster to be created.

    try:
        # Create a Cluster
        api_response = api_instance.clusters_post(create_cluster_request)
        print("The response of ClustersApi->clusters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cluster_request** | [**CreateClusterRequest**](CreateClusterRequest.md)| The cluster to be created. | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created cluster is returned and is automatically set to &#x60;state &#x3D; BUSY&#x60;.  |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type), 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance)  |  * Content-Type - The content type of the response. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_versions_get**
> MongoDBVersionList clusters_versions_get(cluster_id)

Get available MongoDB versions for this cluster

Retrieves all MongoDB versions currently selectable for this cluster.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.mongo_db_version_list import MongoDBVersionList
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
    api_instance = ionoscloud_dbaas_mongo.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.

    try:
        # Get available MongoDB versions for this cluster
        api_response = api_instance.clusters_versions_get(cluster_id)
        print("The response of ClustersApi->clusters_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->clusters_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The unique ID of the cluster. | 

### Return type

[**MongoDBVersionList**](MongoDBVersionList.md)

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

