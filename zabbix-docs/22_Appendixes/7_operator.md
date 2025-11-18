---
title: Operator functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/operator
downloaded: 2025-11-14 10:47:45
---

# 7 Operator functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

The functions are listed without additional information. Click on the function to see the full details.

between | Check if the value belongs to the given range.  
---|---  
in | Check if the value is equal to at least one of the listed values.  
  
### Function details

Some general notes on function parameters:

  * Function parameters are separated by a comma
  * Expressions are accepted as parameters

##### between(value,min,max)

Check if the value belongs to the given range.  
Supported value types: _Integer_ , _Float_.  
Returns: 1 - in range; 0 - otherwise.

Parameters:

  * **value** \- the value to check;  

  * **min** \- the minimum value;  

  * **max** \- the maximum value.

Example:
    
    
    between(last(/host/key),1,10)=1 #trigger if the value is between 1 and 10

Copy

✔ Copied

##### in(value,value1,value2,...valueN)

Check if the value is equal to at least one of the listed values.  
Supported value types: _Integer_ , _Float_ , _Character_ , _Text_ , _Log_.  
Returns: 1 - if equal; 0 - otherwise.

Parameters:

  * **value** \- the value to check;  

  * **valueX** \- listed values (string values must be double-quoted).

The value is compared to the listed values as numbers, if all of these values can be converted to numeric; otherwise compared as strings.

Example:
    
    
    in(last(/host/key),5,10)=1 #trigger if the last value is equal to 5 or 10
           in("text",last(/host/key),last(/host/key,#2))=1 #trigger if "text" is equal to either of the last 2 values

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).