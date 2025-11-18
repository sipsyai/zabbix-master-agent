---
title: Trend object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/trend/object
downloaded: 2025-11-14 10:45:14
---

# Trend object

The following objects are directly related to the `trend` API.

Trend objects differ depending on the item's type of information. They are created by the Zabbix server and cannot be modified via the API.

### Float trend

The float trend object has the following properties.

clock | timestamp | Timestamp of an hour for which the value was calculated. For example, timestamp of "04:00:00" means values calculated for period "04:00:00-04:59:59".  
---|---|---  
itemid | ID | ID of the related item.  
num | integer | Number of values that were available for the hour.  
value_min | float | Hourly minimum value.  
value_avg | float | Hourly average value.  
value_max | float | Hourly maximum value.  
  
### Integer trend

The integer trend object has the following properties.

clock | timestamp | Timestamp of an hour for which the value was calculated. For example, timestamp of "04:00:00" means values calculated for period "04:00:00-04:59:59".  
---|---|---  
itemid | ID | ID of the related item.  
num | integer | Number of values that were available for the hour.  
value_min | integer | Hourly minimum value.  
value_avg | integer | Hourly average value.  
value_max | integer | Hourly maximum value.