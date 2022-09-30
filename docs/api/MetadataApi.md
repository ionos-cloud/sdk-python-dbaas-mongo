# MetadataApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**infos_version_get**](MetadataApi.md#infos_version_get) | **GET** /infos/version | Get API Version |
| [**infos_versions_get**](MetadataApi.md#infos_versions_get) | **GET** /infos/versions | Get All API Versions |


# **infos_version_get**
> APIVersion infos_version_get()

Get API Version

Retrieves the current version of the responding API.

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
    api_instance = ionoscloud_dbaas_mongo.MetadataApi(api_client)
    try:
        # Get API Version
        api_response = api_instance.infos_version_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_version_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIVersion**](../models/APIVersion.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **infos_versions_get**
> list[APIVersion] infos_versions_get()

Get All API Versions

Retrieves all available versions of the responding API.

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
    api_instance = ionoscloud_dbaas_mongo.MetadataApi(api_client)
    try:
        # Get All API Versions
        api_response = api_instance.infos_versions_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling MetadataApi.infos_versions_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[APIVersion]**](../models/APIVersion.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

