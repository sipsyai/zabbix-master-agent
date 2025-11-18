---
title: Foreach functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/aggregate/foreach
downloaded: 2025-11-14 10:47:39
---

# 1 Foreach functions

### Overview

Foreach functions are used in [aggregate calculations](/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate) to return one aggregate value for each item that is selected by the used **item filter**. An array of values is returned.

For example, the _avg_foreach_ function will return an array of values, where each value is the _average_ history value of the selected item, during the time interval that is specified.

The item filter is part of the syntax used by foreach functions. The use of wildcards is supported in the item filter, thus the required items can be selected quite flexibly.

### Supported functions

_avg_foreach_ | Returns the average value for each item.  
---|---  
_bucket_rate_foreach_ | Returns pairs (bucket upper bound, rate value) suitable for use in the [histogram_quantile()](/documentation/current/en/manual/appendix/functions/aggregate#histogram-quantile) function, where "bucket upper bound" is the value of item key parameter defined by the <parameter number> parameter.  
_count_foreach_ | Returns the number of values for each item.  
_exists_foreach_ | Returns '1' for each enabled item.  
_last_foreach_ | Returns the last value for each item.  
_max_foreach_ | Returns the maximum value for each item.  
_min_foreach_ | Returns the minimum value for each item.  
_sum_foreach_ | Returns the sum of values for each item.  
  
### Function syntax

Foreach functions support two common parameters: `item filter` (see details below) and `time period`:
    
    
    foreach_function(item filter,time period)

Copy

✔ Copied

For example:

`avg_foreach(/*/mysql.qps?[group="MySQL Servers"],5m)`

will return the five-minute average of each 'mysql.qps' item in the MySQL server group.

Note that some functions support additional parameters.

#### Item filter syntax

The item filter:
    
    
    /host/key[parameters]?[conditions]

Copy

✔ Copied

consists of four parts, where:

  * host - host name
  * key - item key (without parameters)
  * parameters - item key parameters
  * conditions - host group and/or item tag based conditions (as expression)

Spaces are allowed only inside the conditions expression.

**Wildcard usage**

  * Wildcard can be used to replace the host name, item key or an individual item key parameter.
  * Either the host or item key must be specified without wildcard. So `/host/*` and `/*/key` are valid filters, but `/*/*` is invalid.
  * Wildcard cannot be used for a _part_ of host name, item key, item key parameter.
  * Wildcard does not match more than a single item key parameter. So a wildcard must be specified for each parameter in separation (i.e. `key[abc,*,*]`).

**Conditions expression**

The conditions expression supports:

  * operands: 
    * group - host group
    * tag - item tag
    * `"<text>"` \- string constant, with the `\` escape character to escape `"` and `\`
  * case-sensitive string comparison operators: `=`, `<>`
  * logical operators: `and`, `or`, `not`
  * grouping with parentheses: `(` `)`

Quotation of string constants is mandatory. Only case-sensitive full string comparison is supported.

When specifying tags in the filter (i.e. `tag="tagname:value"`), the colon ":" is used as a delimiter. Everything after it is considered the tag value. Thus it is currently not supported to specify a tag name containing ":" in it.

**Examples**

A complex filter may be used, referencing the item key, host group and tags, as illustrated by the examples:

`/host/key[abc,*]` | Matches similar items on this host.  
---|---  
`/*/key` | Matches the same item of any host.  
`/*/key?[group="ABC" and tag="tagname:value"]` | Matches the same item of any host from the ABC group having 'tagname:value' tags.  
`/*/key[a,*,c]?[(group="ABC" and tag="Tag1") or (group="DEF" and (tag="Tag2" or tag="Tag3:value"))]` | Matches similar items of any host from the ABC or DEF group with the respective tags.  
  
All referenced items must exist and collect data. Only enabled items on enabled hosts are included in the calculations. Items in the unsupported state are not included.

If the item key of a referenced item is changed, the filter must be updated manually.

Specifying a parent host group includes the parent group and all nested host groups with their items.

#### Time period

The **second** parameter allows to specify the time period for aggregation. The time period can only be expressed as time, the amount of values (prefixed with **#**) is not supported.

[Supported unit symbols](/documentation/current/en/manual/appendix/suffixes) can be used in this parameter for convenience, for example, '5m' (five minutes) instead of '300s' (300 seconds) or '1d' (one day) instead of '86400' (86400 seconds).

For the _last_foreach_ function time period is an optional parameter (supported since Zabbix 7.0), which can be omitted:
    
    
    last_foreach(/*/key?[group="host group"])

Copy

✔ Copied

Time period is not supported with the _exists_foreach_ function.

#### Additional parameters

**bucket_rate_foreach**

A third optional parameter is supported by the _bucket_rate_foreach_ function:
    
    
    bucket_rate_foreach(item filter,time period,<parameter number>)

Copy

✔ Copied

where <parameter number> is the position of the "bucket" value in the item key. For example, if the "bucket" value in myItem[aaa,0.2] is '0.2', then its position is 2.

The default value of <parameter number> is '1'.

**count_foreach**

Third and fourth optional parameters are supported by the _count_foreach_ function:
    
    
    count_foreach(item filter,time period,<operator>,<pattern>)

Copy

✔ Copied

Where:

  * **operator** is the conditional operator for item values (must be double-quoted). Supported `operators`:  
_eq_ \- equal  
 _ne_ \- not equal  
 _gt_ \- greater  
 _ge_ \- greater or equal  
 _lt_ \- less  
 _le_ \- less or equal  
 _like_ \- matches if contains pattern (case-sensitive)  
_bitand_ \- bitwise AND  
 _regexp_ \- case-sensitive match of the regular expression given in `pattern`  
 _iregexp_ \- case-insensitive match of the regular expression given in `pattern`  

  * **pattern** is the required pattern (string arguments must be double-quoted); supported if _operator_ is specified in the third parameter.

Comments:

  * Optional parameters _operator_ or _pattern_ can't be left empty after a comma, only fully omitted.
  * With _bitand_ as the third parameter, the fourth `pattern` parameter can be specified as two numbers, separated by '/': **number_to_compare_with/mask**. count_foreach() calculates "bitwise AND" from the value and the _mask_ and compares the result to _number_to_compare_with_. If the result of "bitwise AND" is equal to _number_to_compare_with_ , the value is counted.  
If _number_to_compare_with_ and _mask_ are equal, only the _mask_ need be specified (without '/').
  * With _regexp_ or _iregexp_ as the third parameter, the fourth `pattern` parameter can be an ordinary or [global](/documentation/current/en/manual/regular_expressions#global-regular-expressions) (starting with '@') regular expression. In case of global regular expressions case sensitivity is inherited from global regular expression settings. For the purpose of regexp matching, float values will always be represented with 4 decimal digits after '.'. Also note that for large numbers difference in decimal (stored in database) and binary (used by Zabbix server) representation may affect the 4th decimal digit.

See [aggregate calculations](/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate) for more details and examples on using foreach functions.

#### Behavior depending on availability

The following table illustrates how each function behaves in cases of limited availability of host/item and history data.

_avg_foreach_ | ignore | return avg | ignore | ignore | ignore | ignore  
---|---|---|---|---|---|---  
_bucket_rate_foreach_ | ignore | return bucket rate | ignore | ignore | ignore | ignore  
_count_foreach_ | ignore | return count | 0 | ignore | ignore | ignore  
_exists_foreach_ | ignore | 1 | 1 | ignore | 1 | n/a  
_last_foreach_ | ignore | return last | ignore | ignore | ignore | ignore  
_max_foreach_ | ignore | return max | ignore | ignore | ignore | ignore  
_min_foreach_ | ignore | return min | ignore | ignore | ignore | ignore  
_sum_foreach_ | ignore | return sum | ignore | ignore | ignore | ignore  
  
If the item is _ignored_ , nothing is added to the aggregation.