# Connection

The network connection  details for your cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter_id** | **str** | The datacenter to which your cluster will be connected. | 
**lan_id** | **str** | The numeric LAN ID with which you connect your cluster. | 
**cidr_list** | **list[str]** | The list of IPs for your cluster. All IPs must be in a /24 network. Note the following unavailable IP ranges: 10.233.114.0/24  | 

## Example

```python
from ionoscloud_dbaas_mongo.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


