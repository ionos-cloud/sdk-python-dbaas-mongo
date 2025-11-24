# TemplateList

List of MongoDB templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0).  | [optional] [default to 0]
**limit** | **int** | The limit specified in the request (if none was specified, the default limit is 100).  | [optional] [default to 100]
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 
**type** | [**ResourceType**](ResourceType.md) |  | [optional] 
**id** | **str** | The unique ID of the resource. | [optional] 
**items** | [**list[TemplateResponse]**](TemplateResponse.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.template_list import TemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateList from a JSON string
template_list_instance = TemplateList.from_json(json)
# print the JSON string representation of the object
print(TemplateList.to_json())

# convert the object into a dict
template_list_dict = template_list_instance.to_dict()
# create an instance of TemplateList from a dict
template_list_from_dict = TemplateList.from_dict(template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


