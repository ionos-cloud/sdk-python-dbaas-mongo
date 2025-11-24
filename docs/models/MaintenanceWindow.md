# MaintenanceWindow

A weekly window of 4 hours during which maintenance work can be performed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | 
**day_of_the_week** | [**DayOfTheWeek**](DayOfTheWeek.md) |  | 

## Example

```python
from ionoscloud_dbaas_mongo.models.maintenance_window import MaintenanceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceWindow from a JSON string
maintenance_window_instance = MaintenanceWindow.from_json(json)
# print the JSON string representation of the object
print(MaintenanceWindow.to_json())

# convert the object into a dict
maintenance_window_dict = maintenance_window_instance.to_dict()
# create an instance of MaintenanceWindow from a dict
maintenance_window_from_dict = MaintenanceWindow.from_dict(maintenance_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


