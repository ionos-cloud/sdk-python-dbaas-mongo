# MongoDBVersionListDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The MongoDB version of your cluster. | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.mongo_db_version_list_data_inner import MongoDBVersionListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBVersionListDataInner from a JSON string
mongo_db_version_list_data_inner_instance = MongoDBVersionListDataInner.from_json(json)
# print the JSON string representation of the object
print(MongoDBVersionListDataInner.to_json())

# convert the object into a dict
mongo_db_version_list_data_inner_dict = mongo_db_version_list_data_inner_instance.to_dict()
# create an instance of MongoDBVersionListDataInner from a dict
mongo_db_version_list_data_inner_from_dict = MongoDBVersionListDataInner.from_dict(mongo_db_version_list_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


