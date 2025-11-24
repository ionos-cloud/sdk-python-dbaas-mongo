# UserRoles

a list of mongodb user role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**database** | **str** |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.user_roles import UserRoles

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoles from a JSON string
user_roles_instance = UserRoles.from_json(json)
# print the JSON string representation of the object
print(UserRoles.to_json())

# convert the object into a dict
user_roles_dict = user_roles_instance.to_dict()
# create an instance of UserRoles from a dict
user_roles_from_dict = UserRoles.from_dict(user_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


