# BiConnectorProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data analysis.  | [optional] [default to False]
**host** | **str** | The host where this new BI Connector is installed.  | [optional] [readonly] 
**port** | **str** | Port number used when connecting to this new BI Connector.  | [optional] [readonly] 

## Example

```python
from ionoscloud_dbaas_mongo.models.bi_connector_properties import BiConnectorProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BiConnectorProperties from a JSON string
bi_connector_properties_instance = BiConnectorProperties.from_json(json)
# print the JSON string representation of the object
print(BiConnectorProperties.to_json())

# convert the object into a dict
bi_connector_properties_dict = bi_connector_properties_instance.to_dict()
# create an instance of BiConnectorProperties from a dict
bi_connector_properties_from_dict = BiConnectorProperties.from_dict(bi_connector_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


