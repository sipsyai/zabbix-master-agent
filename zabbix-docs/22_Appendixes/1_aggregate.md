---
title: Aggregate functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/aggregate
downloaded: 2025-11-14 10:47:38
---

# 1 Aggregate functions

Except where stated otherwise, all functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

Aggregate functions can work with either:

  * history of items, for example, `min(/host/key,1h)`
  * [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach) as the only parameter, for example, `min(last_foreach(/*/key))` (only in calculated items; cannot be used in triggers)

The functions are listed without additional information. Click on the function to see the full details.

avg | The average value of an item within the defined evaluation period.  
---|---  
bucket_percentile | Calculates the percentile from the buckets of a histogram.  
count | The count of values in an array returned by a foreach function.  
histogram_quantile | Calculates the φ-quantile from the buckets of a histogram.  
item_count | The count of existing items in configuration that match the filter criteria.  
kurtosis | The "tailedness" of the probability distribution in collected values within the defined evaluation period.  
mad | The median absolute deviation in collected values within the defined evaluation period.  
max | The highest value of an item within the defined evaluation period.  
min | The lowest value of an item within the defined evaluation period.  
skewness | The asymmetry of the probability distribution in collected values within the defined evaluation period.  
stddevpop | The population standard deviation in collected values within the defined evaluation period.  
stddevsamp | The sample standard deviation in collected values within the defined evaluation period.  
sum | The sum of collected values within the defined evaluation period.  
sumofsquares | The sum of squares in collected values within the defined evaluation period.  
varpop | The population variance of collected values within the defined evaluation period.  
varsamp | The sample variance of collected values within the defined evaluation period.  
  
#### Common parameters

  * `/host/key` is a common mandatory first parameter for the functions referencing the host item history
  * `(sec|#num)<:time shift>` is a common second parameter for the functions referencing the host item history, where: 
    * **sec** \- maximum [evaluation period](/documentation/current/en/manual/config/triggers#evaluation-period) in seconds (time [suffixes](/documentation/current/en/manual/appendix/suffixes) can be used), or
    * **#num** \- maximum [evaluation range](/documentation/current/en/manual/config/triggers#evaluation-period) in latest collected values (if preceded by a hash mark)
    * **time shift** (optional) allows to move the evaluation point back in time. See [more details](/documentation/current/en/manual/config/triggers/expression#time-shift) on specifying time shift.

### Function details

Some general notes on function parameters:

  * Function parameters are separated by a comma
  * Optional function parameters (or parameter parts) are indicated by `<` `>`
  * Function-specific parameters are described with each function
  * `/host/key` and `(sec|#num)<:time shift>` parameters must never be quoted

##### avg(/host/key,(sec|#num)<:time shift>)

The average value of an item within the defined evaluation period.  
Supported value types: _Float_ , _Integer_.  
Supported [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _avg_foreach_ , _count_foreach_ , _exists_foreach_ , _last_foreach_ , _max_foreach_ , _min_foreach_ , _sum_foreach_.

Parameters: see common parameters.

Time shift is useful when there is a need to compare the current average value with the average value some time ago.

Examples:
    
    
    avg(/host/key,1h) #the average value for the last hour until now
           avg(/host/key,1h:now-1d) #the average value for an hour from 25 hours ago to 24 hours ago from now
           avg(/host/key,#5) #the average value of the five latest values
           avg(/host/key,#5:now-1d) #the average value of the five latest values excluding the values received in the last 24 hours

Copy

✔ Copied

##### bucket_percentile(item filter,time period,percentage)

Calculates the percentile from the buckets of a histogram.  

Parameters:

  * **item filter** \- see [item filter](/documentation/current/en/manual/appendix/functions/aggregate/foreach#item-filter-syntax);  

  * **time period** \- see [time period](/documentation/current/en/manual/appendix/functions/aggregate/foreach#time-period);  

  * **percentage** \- percentage (0-100).

Comments:

  * Supported only in calculated items;
  * This function is an alias for `histogram_quantile(percentage/100, bucket_rate_foreach(item filter, time period, 1))`.

##### count(func_foreach(item filter,<time period>),<operator>,<pattern>)

The count of values in an array returned by a foreach function.  
Supported [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _avg_foreach_ , _count_foreach_ , _exists_foreach_ , _last_foreach_ , _max_foreach_ , _min_foreach_ , _sum_foreach_.

Parameters:

  * **func_foreach** \- foreach function for which the number of returned values should be counted. See [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach) for details. Note that count_foreach and bucket_rate_foreach support [additional parameters](/documentation/current/en/manual/appendix/functions/aggregate/foreach#additional-parameters).
  * **item filter** \- see [item filter](/documentation/current/en/manual/appendix/functions/aggregate/foreach#item-filter-syntax);  

  * **time period** \- see [time period](/documentation/current/en/manual/appendix/functions/aggregate/foreach#time-period);  

  * **operator** (must be double-quoted). Supported `operators`:  
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

  * **pattern** \- the required pattern (string arguments must be double-quoted); supported if _operator_ is specified in the third parameter.

Comments:

  * Using **count()** with a history-related foreach function (max_foreach, avg_foreach, etc.) may lead to performance implications, whereas using **exists_foreach()** , which works only with configuration data, will not have such effect.
  * Optional parameters _operator_ or _pattern_ can't be left empty after a comma, only fully omitted.
  * With _bitand_ as the third parameter, the fourth `pattern` parameter can be specified as two numbers, separated by '/': **number_to_compare_with/mask**. count() calculates "bitwise AND" from the value and the _mask_ and compares the result to _number_to_compare_with_. If the result of "bitwise AND" is equal to _number_to_compare_with_ , the value is counted.  
If _number_to_compare_with_ and _mask_ are equal, only the _mask_ need be specified (without '/').
  * With _regexp_ or _iregexp_ as the third parameter, the fourth `pattern` parameter can be an ordinary or [global](/documentation/current/en/manual/regular_expressions#global-regular-expressions) (starting with '@') regular expression. In case of global regular expressions case sensitivity is inherited from global regular expression settings. For the purpose of regexp matching, float values will always be represented with 4 decimal digits after '.'. Also note that for large numbers difference in decimal (stored in database) and binary (used by Zabbix server) representation may affect the 4th decimal digit.

Examples:
    
    
    count(max_foreach(/*/net.if.in[*],1h)) #the number of net.if.in items that received data in the last hour until now
           count(last_foreach(/*/vfs.fs.dependent.size[*,pused]),"gt",95) #the number of file systems with over 95% of disk space used

Copy

✔ Copied

##### histogram_quantile(quantile,bucket1,value1,bucket2,value2,...)

Calculates the φ-quantile from the buckets of a histogram.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _bucket_rate_foreach_.

Parameters:

  * **quantile** \- 0 ≤ φ ≤ 1;  

  * **bucketN, valueN** \- manually entered pairs (>=2) of parameters or the response of [bucket_rate_foreach](/documentation/current/en/manual/appendix/functions/aggregate/foreach).

Comments:

  * Supported only in calculated items;
  * Functionally corresponds to '[histogram_quantile](https://prometheus.io/docs/prometheus/latest/querying/functions/#histogram_quantile)' of PromQL;
  * Returns -1 if values of the last 'Infinity' bucket (_"+inf"_) are equal to 0.

Examples:
    
    
    histogram_quantile(0.75,1.0,last(/host/rate_bucket[1.0]),"+Inf",last(/host/rate_bucket[Inf]))
           histogram_quantile(0.5,bucket_rate_foreach(//item_key,30s))

Copy

✔ Copied

##### item_count(item filter)

The count of existing items in configuration that match the filter criteria.  
Supported value type: _Integer_.

Parameter:

  * **item filter** \- criteria for item selection, allows referencing by host group, host, item key, and tags. Wildcards are supported. See [item filter](/documentation/current/en/manual/appendix/functions/aggregate/foreach#item-filter-syntax) for more details.  

Comments:

  * Supported only in calculated items;
  * Works as an alias for the _count(exists_foreach(item_filter))_ function.

Examples:
    
    
    item_count(/*/agent.ping?[group="Host group 1"]) #the number of hosts with the *agent.ping* item in the "Host group 1"

Copy

✔ Copied

##### kurtosis(/host/key,(sec|#num)<:time shift>)

The "tailedness" of the probability distribution in collected values within the defined evaluation period. See also: [Kurtosis](https://en.wikipedia.org/wiki/Kurtosis).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

Example:
    
    
    kurtosis(/host/key,1h) #kurtosis for the last hour until now

Copy

✔ Copied

##### mad(/host/key,(sec|#num)<:time shift>)

The median absolute deviation in collected values within the defined evaluation period. See also: [Median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

Example:
    
    
    mad(/host/key,1h) #median absolute deviation for the last hour until now

Copy

✔ Copied

##### max(/host/key,(sec|#num)<:time shift>)

The highest value of an item within the defined evaluation period.  
Supported value types: _Float_ , _Integer_.  
Supported [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _avg_foreach_ , _count_foreach_ , _exists_foreach_ , _last_foreach_ , _max_foreach_ , _min_foreach_ , _sum_foreach_.

Parameters: see common parameters.

Example:
    
    
    max(/host/key,1h) - min(/host/key,1h) #calculate the difference between the maximum and minimum values within the last hour until now (the delta of values)

Copy

✔ Copied

##### min(/host/key,(sec|#num)<:time shift>)

The lowest value of an item within the defined evaluation period.  
Supported value types: _Float_ , _Integer_.  
Supported [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _avg_foreach_ , _count_foreach_ , _exists_foreach_ , _last_foreach_ , _max_foreach_ , _min_foreach_ , _sum_foreach_.

Parameters: see common parameters.

Example:
    
    
    max(/host/key,1h) - min(/host/key,1h) #calculate the difference between the maximum and minimum values within the last hour until now (the delta of values)

Copy

✔ Copied

##### skewness(/host/key,(sec|#num)<:time shift>)

The asymmetry of the probability distribution in collected values within the defined evaluation period. See also: [Skewness](https://en.wikipedia.org/wiki/Skewness).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

Example:
    
    
    skewness(/host/key,1h) #the skewness for the last hour until now

Copy

✔ Copied

##### stddevpop(/host/key,(sec|#num)<:time shift>)

The population standard deviation in collected values within the defined evaluation period. See also: [Standard deviation](https://en.wikipedia.org/wiki/Standard_deviation).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

Example:
    
    
    stddevpop(/host/key,1h) #the population standard deviation for the last hour until now

Copy

✔ Copied

##### stddevsamp(/host/key,(sec|#num)<:time shift>)

The sample standard deviation in collected values within the defined evaluation period. See also: [Standard deviation](https://en.wikipedia.org/wiki/Standard_deviation).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

At least two data values are required for this function to work.

Example:
    
    
    stddevsamp(/host/key,1h) #the sample standard deviation for the last hour until now

Copy

✔ Copied

##### sum(/host/key,(sec|#num)<:time shift>)

The sum of collected values within the defined evaluation period.  
Supported value types: _Float_ , _Integer_.  
Supported [foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _avg_foreach_ , _count_foreach_ , _exists_foreach_ , _last_foreach_ , _max_foreach_ , _min_foreach_ , _sum_foreach_.

Parameters: see common parameters.

Example:
    
    
    sum(/host/key,1h) #the sum of values for the last hour until now

Copy

✔ Copied

##### sumofsquares(/host/key,(sec|#num)<:time shift>)

The sum of squares in collected values within the defined evaluation period.  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

Example:
    
    
    sumofsquares(/host/key,1h) #the sum of squares for the last hour until now

Copy

✔ Copied

##### varpop(/host/key,(sec|#num)<:time shift>)

The population variance of collected values within the defined evaluation period. See also: [Variance](https://en.wikipedia.org/wiki/Variance).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

Example:
    
    
    varpop(/host/key,1h) #the population variance for the last hour until now

Copy

✔ Copied

##### varsamp(/host/key,(sec|#num)<:time shift>)

The sample variance of collected values within the defined evaluation period. See also: [Variance](https://en.wikipedia.org/wiki/Variance).  
Supported value types: _Float_ , _Integer_.  
Supported [foreach function](/documentation/current/en/manual/appendix/functions/aggregate/foreach): _last_foreach_.

Parameters: see common parameters.

At least two data values are required for this function to work.

Example:
    
    
    varsamp(/host/key,1h) #the sample variance for the last hour until now

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).