---
title: Date and time functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/time
downloaded: 2025-11-14 10:47:41
---

# 3 Date and time functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

Date and time functions cannot be used in the expression by themselves; at least one function from [another group](/documentation/current/en/manual/appendix/functions), referencing the host item, must be included in the expression (except the [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) function). For detailed information on how date and time functions work within expressions, see [Calculation time](/documentation/current/en/manual/config/triggers#calculation-time).

The functions are listed without additional information. Click on the function to see the full details.

date | The current date in YYYYMMDD format.  
---|---  
dayofmonth | The day of month in range of 1 to 31.  
dayofweek | The day of week in range of 1 to 7.  
now | The number of seconds since the Epoch (00:00:00 UTC, January 1, 1970).  
time | The current time in HHMMSS format.  
  
### Function details

##### date

The current date in YYYYMMDD format.

Example:
    
    
    date()<20220101

Copy

✔ Copied

##### dayofmonth

The day of month in range of 1 to 31.

Example:
    
    
    dayofmonth()=1

Copy

✔ Copied

##### dayofweek

The day of week in range of 1 to 7 (Mon - 1, Sun - 7).

Example (only weekdays):
    
    
    dayofweek()<6

Copy

✔ Copied

Example (only weekend):
    
    
    dayofweek()>5

Copy

✔ Copied

##### now

The number of seconds since the Epoch (00:00:00 UTC, January 1, 1970).

Example:
    
    
    now()<1640998800

Copy

✔ Copied

##### time

The current time in HHMMSS format.

Example (only nighttime, 00:00-06:00):
    
    
    time()<060000

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).