---
title: Calculated items
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/calculated
downloaded: 2025-11-14 10:35:07
---

# 7 Calculated items

#### Overview

A calculated item allows to create a calculation based on the values of some existing items. For example, you may want to calculate the hourly average of some item value or to calculate the total value for a group of items. That is what a calculated item is for.

Calculations may use both:

  * single values of individual items
  * a complex filter to select multiple items for aggregation (see [aggregate calculations](/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate) for details)

Calculated items are a way of creating virtual data sources. All calculations are done by Zabbix server only. The values are periodically calculated based on the arithmetical expression used.

The resulting data is stored in the Zabbix database as for any other item; both history and trend values are stored and graphs can be generated.

If the calculation result is a float value it will be trimmed to an integer if the calculated item type of information is _Numeric (unsigned)_.

Also, if there is no recent data in the cache and there is no defined querying period in the function, Zabbix will by default go as far back in the past as one week to query the database for historical values.

Calculated items share their syntax with trigger [expressions](/documentation/current/en/manual/config/triggers/expression). Comparison to strings is allowed in calculated items. Calculated items may be referenced by macros or other entities same as any other item type.

To use calculated items, choose the item type **Calculated**.

#### Configurable fields

The **key** is a unique item identifier (per host). You can create any key name using supported symbols.

The calculation definition should be entered in the **Formula** field. There is no connection between the formula and the key. The key parameters are not used in the formula in any way.

The syntax of a simple formula is:
    
    
    function(/host/key,<parameter1>,<parameter2>,...)

Copy

✔ Copied

where:

_function_ | One of the [supported functions](/documentation/current/en/manual/appendix/functions): last, min, max, avg, count, etc  
---|---  
_host_ | Host of the item that is used for calculation.  
The current host can be omitted (i.e. as in `function(//key,parameter,...)`).  
_key_ | Key of the item that is used for calculation.  
_parameter(s)_ | Parameters of the function, if required.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) and [memory size suffixes](/documentation/current/en/manual/appendix/suffixes#memory-size-suffixes) are supported.  
  
[User macros](/documentation/current/en/manual/config/macros/user_macros) in the formula will be expanded if used to reference a function parameter, item filter parameter, or a constant. User macros will NOT be expanded if referencing a function, host name, item key, item key parameter or operator.

A more complex formula may use a combination of functions, operators and brackets. You can use all functions and [operators](/documentation/current/en/manual/config/triggers/expression#operators) supported in trigger expressions. The logic and operator precedence are exactly the same.

Unlike trigger expressions, Zabbix processes calculated items according to the item update interval, not upon receiving a new value.

All items that are referenced by history functions in the calculated item formula must exist and be collecting data. Also, if you change the item key of a referenced item, you have to manually update any formulas using that key.

A calculated item may become unsupported in several cases:

  * referenced item(s) 
    * is not found
    * is disabled
    * belongs to a disabled host
    * is not supported (except with nodata() function and [operators](/documentation/current/en/manual/config/triggers/expression#operators) with unknown values)
  * no data to calculate a function
  * division by zero
  * incorrect syntax used

#### Usage examples

##### Example 1

Calculating percentage of free disk space on '/'.

Use of function **last** :
    
    
    100*last(//vfs.fs.size[/,free])/last(//vfs.fs.size[/,total])

Copy

✔ Copied

Zabbix will take the latest values for free and total disk spaces and calculate percentage according to the given formula.

##### Example 2

Calculating a 10-minute average of the number of values processed by Zabbix.

Use of function **avg** :
    
    
    avg(/Zabbix Server/zabbix[wcache,values],10m)

Copy

✔ Copied

Note that extensive use of calculated items with long time periods may affect performance of Zabbix server.

##### Example 3

Calculating total bandwidth on eth0.

Sum of two functions:
    
    
    last(//net.if.in[eth0,bytes])+last(//net.if.out[eth0,bytes])

Copy

✔ Copied

##### Example 4

Calculating percentage of incoming traffic.

More complex expression:
    
    
    100*last(//net.if.in[eth0,bytes])/(last(//net.if.in[eth0,bytes])+last(//net.if.out[eth0,bytes]))

Copy

✔ Copied

See also: [Examples of aggregate calculations](/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate#usage-examples)