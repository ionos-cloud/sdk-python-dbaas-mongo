# PatchUserProperties

MongoDB database user patch request properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**roles** | [**list[UserRoles]**](UserRoles.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.patch_user_properties import PatchUserProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUserProperties from a JSON string
patch_user_properties_instance = PatchUserProperties.from_json(json)
# print the JSON string representation of the object
print(PatchUserProperties.to_json())

# convert the object into a dict
patch_user_properties_dict = patch_user_properties_instance.to_dict()
# create an instance of PatchUserProperties from a dict
patch_user_properties_from_dict = PatchUserProperties.from_dict(patch_user_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


