---
title: Maintenance object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/maintenance/object
downloaded: 2025-11-14 10:43:09
---

# Maintenance object

The following objects are directly related to the `maintenance` API.

### Maintenance

The maintenance object has the following properties.

maintenanceid | ID | ID of the maintenance.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the maintenance.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
active_since | timestamp | Time when the maintenance becomes active (inclusive).  
  
The given value will be rounded down to minutes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
active_till | timestamp | Time when the maintenance stops being active (exclusive).  
  
The given value will be rounded down to minutes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
description | string | Description of the maintenance.  
maintenance_type | integer | Type of maintenance.  
  
Possible values:  
0 - _(default)_ with data collection;  
1 - without data collection.  
tags_evaltype | integer | Problem tag [evaluation method](/documentation/current/en/manual/maintenance#configuration).  
  
Possible values:  
0 - _(default)_ And/Or;  
2 - Or.  
  
### Time period

The time period object is used to define periods when the maintenance must come into effect. It has the following properties.

period | integer | Duration of the maintenance period in seconds.  
  
The given value will be rounded down to minutes.  
  
Default: 3600.  
---|---|---  
timeperiod_type | integer | Type of time period.  
  
Possible values:  
0 - _(default)_ one time only;  
2 - daily;  
3 - weekly;  
4 - monthly.  
start_date | timestamp | Date when the maintenance period must come into effect.  
The given value will be rounded down to minutes.  
  
Default: current date.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `timeperiod_type` is set to "one time only"  
start_time | integer | Time of day when the maintenance starts in seconds.  
The given value will be rounded down to minutes.  
  
Default: 0.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `timeperiod_type` is set to "daily", "weekly", or "monthly"  
every | integer | For daily and weekly periods `every` defines the day or week intervals at which the maintenance must come into effect.  
Default value if `timeperiod_type` is set to "daily" or "weekly": 1.  
  
For monthly periods when `day` is set, the `every` property defines the day of the month when the maintenance must come into effect.  
Default value if `timeperiod_type` is set to "monthly" and `day` is set: 1.  
  
For monthly periods when `dayofweek` is set, the `every` property defines the week of the month when the maintenance must come into effect.  
Possible values if `timeperiod_type` is set to "monthly" and `dayofweek` is set:  
1 - _(default)_ first week;  
2 - second week;  
3 - third week;  
4 - fourth week;  
5 - last week.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `timeperiod_type` is set to "daily", "weekly", or "monthly"  
dayofweek | integer | Days of the week when the maintenance must come into effect.  
  
Possible bitmap values:  
1 - Monday;  
2 - Tuesday;  
4 - Wednesday;  
8 - Thursday;  
16 - Friday;  
32 - Saturday;  
64 - Sunday.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 21 for Monday, Wednesday, and Friday).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `timeperiod_type` is set to "weekly" or if `timeperiod_type` is set to "monthly" and `day` is not set  
day | integer | Day of the month when the maintenance must come into effect.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `timeperiod_type` is set to "monthly" and `dayofweek` is not set  
month | integer | Months when the maintenance must come into effect.  
  
Possible bitmap values:  
1 - January;  
2 - February;  
4 - March;  
8 - April;  
16 - May;  
32 - June;  
64 - July;  
128 - August;  
256 - September;  
512 - October;  
1024 - November;  
2048 - December.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 585 for January, April, July, and October).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `timeperiod_type` is set to "monthly"  
  
### Problem tag

The problem tag object is used to define which problems must be suppressed when the maintenance comes into effect. Tags can only be specified if `maintenance_type` of Maintenance object is set to "with data collection". It has the following properties.

tag | string | Problem tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
operator | integer | Condition [operator](/documentation/current/en/manual/maintenance#configuration).  
  
Possible values:  
0 - Equals;  
2 - _(default)_ Contains.  
value | string | Problem tag value.