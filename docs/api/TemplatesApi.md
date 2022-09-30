# TemplatesApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**templates_get**](TemplatesApi.md#templates_get) | **GET** /templates | Get Templates |


# **templates_get**
> TemplateList templates_get()

Get Templates

Retrieves a list of valid templates. These templates can be used to create MongoDB clusters; they contain properties, such as number of cores, RAM, and the storage size. 

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
    api_instance = ionoscloud_dbaas_mongo.TemplatesApi(api_client)
    try:
        # Get Templates
        api_response = api_instance.templates_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling TemplatesApi.templates_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplateList**](../models/TemplateList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

