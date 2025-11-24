# APIVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**swagger_url** | **str** |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.api_version import APIVersion

# TODO update the JSON string below
json = "{}"
# create an instance of APIVersion from a JSON string
api_version_instance = APIVersion.from_json(json)
# print the JSON string representation of the object
print(APIVersion.to_json())

# convert the object into a dict
api_version_dict = api_version_instance.to_dict()
# create an instance of APIVersion from a dict
api_version_from_dict = APIVersion.from_dict(api_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


