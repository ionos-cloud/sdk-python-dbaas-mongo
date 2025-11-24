# TemplateResponse

A MongoDB template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResourceType**](ResourceType.md) |  | [optional] 
**id** | **str** | The unique ID of the resource. | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**properties** | [**TemplateProperties**](TemplateProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.template_response import TemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResponse from a JSON string
template_response_instance = TemplateResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateResponse.to_json())

# convert the object into a dict
template_response_dict = template_response_instance.to_dict()
# create an instance of TemplateResponse from a dict
template_response_from_dict = TemplateResponse.from_dict(template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


