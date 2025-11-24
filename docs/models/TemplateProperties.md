# TemplateProperties

The properties of a MongoDB template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the template. | [optional] 
**edition** | **str** | The edition of the template (e.g. enterprise) | [optional] 
**cores** | **int** | The number of CPU cores. | [optional] 
**ram** | **int** | The amount of memory in MB. | [optional] 
**storage_size** | **int** | The amount of storage size in GB. | [optional] 

## Example

```python
from ionoscloud_dbaas_mongo.models.template_properties import TemplateProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateProperties from a JSON string
template_properties_instance = TemplateProperties.from_json(json)
# print the JSON string representation of the object
print(TemplateProperties.to_json())

# convert the object into a dict
template_properties_dict = template_properties_instance.to_dict()
# create an instance of TemplateProperties from a dict
template_properties_from_dict = TemplateProperties.from_dict(template_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


