---
title: Aggregate calculations
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate
downloaded: 2025-11-14 10:35:08
---

# 1 Aggregate calculations

#### Overview

Aggregate calculations are a [calculated item](/documentation/current/en/manual/config/items/itemtypes/calculated) type allowing to collect information from several items by Zabbix server and then calculate an aggregate, depending on the aggregate function used.

Aggregate calculations do not require any agent running on the host being monitored.

#### Syntax

To retrieve aggregates use one of the supported [aggregate functions](/documentation/current/en/manual/appendix/functions/aggregate#aggregate-functions-1): `avg`, `max`, `min`, `sum`, etc. Then add the **foreach** function as the only parameter and its item filter to select the required items:
    
    
    aggregate_function(function_foreach(/host/key?[group="host group"],timeperiod))

Copy

✔ Copied

A **foreach** function (e.g. _avg_foreach_ , _count_foreach_ , etc.) returns one aggregate value for each selected item. Items are selected by using the item filter (`/host/key?[group="host group"]`), from item history. For more details, see [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach).

If some of the items have no data for the requested period, they are ignored in the calculation. If no items have data, the function will return an error.

Alternatively you may list several items as parameters for aggregation:
    
    
    aggregate_function(function(/host/key,parameter),function(/host2/key2,parameter),...)

Copy

✔ Copied

Note that `function` here must be a history/trend function.

If the aggregate results in a float value it will be trimmed to an integer if the aggregated item type of information is _Numeric (unsigned)_.

User macros and low-level discovery macros are supported in:

  * item key parameters
  * function parameters
  * filter conditions (host group name and tag name)
  * expression constants

An aggregate calculation may become unsupported if:

  * none of the referenced items is found (which may happen if the item key is incorrect, none of the items exists or all included groups are incorrect)
  * no data to calculate a function

#### Usage examples

Examples of keys for aggregate calculations.

##### Example 1

Total disk space of host group 'MySQL Servers'.
    
    
    sum(last_foreach(/*/vfs.fs.size[/,total]?[group="MySQL Servers"]))

Copy

✔ Copied

##### Example 2

Sum of latest values of all items matching net.if.in[*] on the host.
    
    
    sum(last_foreach(/host/net.if.in[*]))

Copy

✔ Copied

##### Example 3

Average processor load of host group 'MySQL Servers'.
    
    
    avg(last_foreach(/*/system.cpu.load[,avg1]?[group="MySQL Servers"]))

Copy

✔ Copied

##### Example 4

5-minute average of the number of queries per second for host group 'MySQL Servers'.
    
    
    avg(avg_foreach(/*/mysql.qps?[group="MySQL Servers"],5m))

Copy

✔ Copied

##### Example 5

Average CPU load on all hosts in multiple host groups that have the specific tags.
    
    
    avg(last_foreach(/*/system.cpu.load?[(group="Servers A" or group="Servers B" or group="Servers C") and (tag="Service:" or tag="Importance:High")]))

Copy

✔ Copied

##### Example 6

Calculation used on the latest item value sums of a whole host group.
    
    
    sum(last_foreach(/*/net.if.out[eth0,bytes]?[group="video"])) / sum(last_foreach(/*/nginx_stat.sh[active]?[group="video"])) 

Copy

✔ Copied

##### Example 7

The total number of unsupported items in host group 'Zabbix servers'.
    
    
    sum(last_foreach(/*/zabbix[host,,items_unsupported]?[group="Zabbix servers"]))

Copy

✔ Copied

##### Examples of correct/incorrect syntax

Expressions (including function calls) cannot be used as history, trend, or foreach [function](/documentation/current/en/manual/appendix/functions) parameters. However, those functions themselves can be used in other (non-historical) function parameters.

Valid | `avg(last(/host/key1),last(/host/key2)*10,last(/host/key1)*100)`  
`max(avg(avg_foreach(/*/system.cpu.load?[group="Servers A"],5m)),avg(avg_foreach(/*/system.cpu.load?[group="Servers B"],5m)),avg(avg_foreach(/*/system.cpu.load?[group="Servers C"],5m)))`  
---|---  
Invalid | `sum(/host/key,10+2)`  
`sum(/host/key, avg(10,2))`  
`sum(/host/key,last(/host/key2))`  
  
Note that in an expression like:
    
    
    sum(sum_foreach(//resptime[*],5m))/sum(count_foreach(//resptime[*],5m))

Copy

✔ Copied

it cannot be guaranteed that both parts of the equation will always have the same set of values. While one part of the expression is evaluated, a new value for the requested period may arrive and then the other part of the expression will have a different set of values.