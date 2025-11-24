# MongoDBVersionList

List of MongoDB versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[MongoDBVersionListDataInner]**](MongoDBVersionListDataInner.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.mongo_db_version_list import MongoDBVersionList

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBVersionList from a JSON string
mongo_db_version_list_instance = MongoDBVersionList.from_json(json)
# print the JSON string representation of the object
print(MongoDBVersionList.to_json())

# convert the object into a dict
mongo_db_version_list_dict = mongo_db_version_list_instance.to_dict()
# create an instance of MongoDBVersionList from a dict
mongo_db_version_list_from_dict = MongoDBVersionList.from_dict(mongo_db_version_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


