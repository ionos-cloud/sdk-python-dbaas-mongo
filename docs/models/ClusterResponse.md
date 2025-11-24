# ClusterResponse

A database cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResourceType**](ResourceType.md) |  | [optional] 
**id** | **str** | The unique ID of the resource. | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**properties** | [**ClusterProperties**](ClusterProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.cluster_response import ClusterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResponse from a JSON string
cluster_response_instance = ClusterResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterResponse.to_json())

# convert the object into a dict
cluster_response_dict = cluster_response_instance.to_dict()
# create an instance of ClusterResponse from a dict
cluster_response_from_dict = ClusterResponse.from_dict(cluster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


