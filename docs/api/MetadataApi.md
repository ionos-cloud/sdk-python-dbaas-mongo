# ionoscloud_dbaas_mongo.MetadataApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infos_version_get**](MetadataApi.md#infos_version_get) | **GET** /infos/version | Get API Version
[**infos_versions_get**](MetadataApi.md#infos_versions_get) | **GET** /infos/versions | Get All API Versions
[**versions_get**](MetadataApi.md#versions_get) | **GET** /versions | Get available MongoDB versions


# **infos_version_get**
> APIVersion infos_version_get()

Get API Version

Retrieves the current version of the responding API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.api_version import APIVersion
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
    api_instance = ionoscloud_dbaas_mongo.MetadataApi(api_client)

    try:
        # Get API Version
        api_response = api_instance.infos_version_get()
        print("The response of MetadataApi->infos_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->infos_version_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIVersion**](APIVersion.md)

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

# **infos_versions_get**
> list[APIVersion] infos_versions_get()

Get All API Versions

Retrieves all available versions of the responding API.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dbaas_mongo
from ionoscloud_dbaas_mongo.models.api_version import APIVersion
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
    api_instance = ionoscloud_dbaas_mongo.MetadataApi(api_client)

    try:
        # Get All API Versions
        api_response = api_instance.infos_versions_get()
        print("The response of MetadataApi->infos_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->infos_versions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**list[APIVersion]**](APIVersion.md)

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

# **versions_get**
> MongoDBVersionList versions_get()

Get available MongoDB versions

Retrieves all MongoDB versions available for new MongoDB clusters.

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
    api_instance = ionoscloud_dbaas_mongo.MetadataApi(api_client)

    try:
        # Get available MongoDB versions
        api_response = api_instance.versions_get()
        print("The response of MetadataApi->versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->versions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

