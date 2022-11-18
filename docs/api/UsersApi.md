# UsersApi

All URIs are relative to *https://api.ionos.com/databases/mongodb*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_users_delete**](UsersApi.md#clusters_users_delete) | **DELETE** /clusters/{clusterId}/users/{database}/{username} | Delete a MongoDB User by ID |
| [**clusters_users_find_by_id**](UsersApi.md#clusters_users_find_by_id) | **GET** /clusters/{clusterId}/users/{database}/{username} | Get a MongoDB User by ID |
| [**clusters_users_get**](UsersApi.md#clusters_users_get) | **GET** /clusters/{clusterId}/users | Get a Cluster Users |
| [**clusters_users_patch**](UsersApi.md#clusters_users_patch) | **PATCH** /clusters/{clusterId}/users/{database}/{username} | Patch a MongoDB User by ID |
| [**clusters_users_post**](UsersApi.md#clusters_users_post) | **POST** /clusters/{clusterId}/users | Create MongoDB User |


# **clusters_users_delete**
> User clusters_users_delete(cluster_id, database, username)

Delete a MongoDB User by ID

Deletes a MongoDB user specified by its ID.

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
    api_instance = ionoscloud_dbaas_mongo.UsersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    database = 'database_example' # str | The authentication database.
    username = 'username_example' # str | The authentication username.
    try:
        # Delete a MongoDB User by ID
        api_response = api_instance.clusters_users_delete(cluster_id, database, username)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.clusters_users_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **database** | **str**| The authentication database. |  |
| **username** | **str**| The authentication username. |  |

### Return type

[**User**](../models/User.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_users_find_by_id**
> User clusters_users_find_by_id(cluster_id, database, username)

Get a MongoDB User by ID

Retrieves the MongoDB user identified by the username and database parameters.

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
    api_instance = ionoscloud_dbaas_mongo.UsersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    database = 'database_example' # str | The authentication database.
    username = 'username_example' # str | The authentication username.
    try:
        # Get a MongoDB User by ID
        api_response = api_instance.clusters_users_find_by_id(cluster_id, database, username)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.clusters_users_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **database** | **str**| The authentication database. |  |
| **username** | **str**| The authentication username. |  |

### Return type

[**User**](../models/User.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_users_get**
> UsersList clusters_users_get(cluster_id)

Get a Cluster Users

Retrieves a list of MongoDB users.

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
    api_instance = ionoscloud_dbaas_mongo.UsersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    try:
        # Get a Cluster Users
        api_response = api_instance.clusters_users_get(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.clusters_users_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |

### Return type

[**UsersList**](../models/UsersList.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_users_patch**
> User clusters_users_patch(cluster_id, database, username, patch_user_request)

Patch a MongoDB User by ID

Patches a MongoDB user specified by its ID.

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
    api_instance = ionoscloud_dbaas_mongo.UsersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    database = 'database_example' # str | The authentication database.
    username = 'username_example' # str | The authentication username.
    patch_user_request = ionoscloud_dbaas_mongo.PatchUserRequest() # PatchUserRequest | Part of the MongoDB user which should be modified.
    try:
        # Patch a MongoDB User by ID
        api_response = api_instance.clusters_users_patch(cluster_id, database, username, patch_user_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.clusters_users_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **database** | **str**| The authentication database. |  |
| **username** | **str**| The authentication username. |  |
| **patch_user_request** | [**PatchUserRequest**](../models/PatchUserRequest.md)| Part of the MongoDB user which should be modified. |  |

### Return type

[**User**](../models/User.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **clusters_users_post**
> User clusters_users_post(cluster_id, user)

Create MongoDB User

Creates a MongoDB user. 

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
    api_instance = ionoscloud_dbaas_mongo.UsersApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster.
    user = ionoscloud_dbaas_mongo.User() # User | The user to be created.
    try:
        # Create MongoDB User
        api_response = api_instance.clusters_users_post(cluster_id, user)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UsersApi.clusters_users_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | **str**| The unique ID of the cluster. |  |
| **user** | [**User**](../models/User.md)| The user to be created. |  |

### Return type

[**User**](../models/User.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

