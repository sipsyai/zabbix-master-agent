---
title: History functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/history
downloaded: 2025-11-14 10:47:42
---

# 4 History functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

The functions are listed without additional information. Click on the function to see the full details.

change | The amount of difference between the previous and latest value.  
---|---  
changecount | The number of changes between adjacent values within the defined evaluation period.  
count | The number of values within the defined evaluation period.  
countunique | The number of unique values within the defined evaluation period.  
find | Find a value match within the defined evaluation period.  
first | The first (the oldest) value within the defined evaluation period.  
firstclock | The timestamp of the first (the oldest) value within the defined evaluation period.  
fuzzytime | Check how much the passive agent time differs from the Zabbix server/proxy time.  
last | The most recent value.  
lastclock | The timestamp of the Nth most recent value within the defined evaluation period.  
logeventid | Check if the event ID of the last log entry matches a regular expression.  
logseverity | The log severity of the last log entry.  
logsource | Check if log source of the last log entry matches a regular expression.  
logtimestamp | The log message timestamp of the Nth most recent log item value.  
monodec | Check if there has been a monotonous decrease in values.  
monoinc | Check if there has been a monotonous increase in values.  
nodata | Check for no data received.  
percentile | The P-th percentile of a period, where P (percentage) is specified by the third parameter.  
rate | The per-second average rate of the increase in a monotonically increasing counter within the defined time period.  
  
##### Common parameters

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

##### change(/host/key)

The amount of difference between the previous and latest value.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.  
For strings returns: 0 - values are equal; 1 - values differ.

Parameters: see common parameters.

Comments:

  * Numeric difference will be calculated, as seen with these incoming example values ('previous' and 'latest' value = difference):  
'1' and '5' = `+4`  
'3' and '1' = `-2`  
'0' and '-2.5' = `-2.5`  

  * See also: [abs](/documentation/current/en/manual/appendix/functions/math#abs) for comparison.

Examples:
    
    
    change(/host/key)>10

Copy

✔ Copied

##### changecount(/host/key,(sec|#num)<:time shift>,<mode>)

The number of changes between adjacent values within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters;  

  * **mode** (must be double-quoted) - possible values: _all_ \- count all changes (default); _dec_ \- count decreases; _inc_ \- count increases

For non-numeric value types, the _mode_ parameter is ignored.

Examples:
    
    
    changecount(/host/key,1w) #the number of value changes for the last week until now
           changecount(/host/key,#10,"inc") #the number of value increases (relative to the adjacent value) among the last 10 values
           changecount(/host/key,24h,"dec") #the number of value decreases (relative to the adjacent value) for the last 24 hours until now

Copy

✔ Copied

##### count(/host/key,(sec|#num)<:time shift>,<operator>,<pattern>)

The number of values within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters;  

  * **operator** (must be double-quoted). Supported `operators`:  
_eq_ \- equal (default for integer, float)  
_ne_ \- not equal  
 _gt_ \- greater  
 _ge_ \- greater or equal  
 _lt_ \- less  
 _le_ \- less or equal  
 _like_ (default for string, text, log) - matches if contains pattern (case-sensitive)  
_bitand_ \- bitwise AND  
 _regexp_ \- case-sensitive match of the regular expression given in `pattern`  
 _iregexp_ \- case-insensitive match of the regular expression given in `pattern`  

  * **pattern** \- the required pattern (string arguments must be double-quoted).

Comments:

  * Float items match with the precision of 2.22e-16;
  * _like_ is not supported as operator for integer values;
  * _like_ and _bitand_ are not supported as operators for float values;
  * For string, text, and log values only _eq_ , _ne_ , _like_ , _regexp_ and _iregexp_ operators are supported;
  * With _bitand_ as operator, the fourth `pattern` parameter can be specified as two numbers, separated by '/': **number_to_compare_with/mask**. count() calculates "bitwise AND" from the value and the _mask_ and compares the result to _number_to_compare_with_. If the result of "bitwise AND" is equal to _number_to_compare_with_ , the value is counted.  
If _number_to_compare_with_ and _mask_ are equal, only the _mask_ need be specified (without '/').
  * With _regexp_ or _iregexp_ as operator, the fourth `pattern` parameter can be an ordinary or [global](/documentation/current/en/manual/regular_expressions#global-regular-expressions) (starting with '@') regular expression. In case of global regular expressions case sensitivity is inherited from global regular expression settings. For the purpose of regexp matching, float values will always be represented with 4 decimal digits after '.'. Also note that for large numbers difference in decimal (stored in database) and binary (used by Zabbix server) representation may affect the 4th decimal digit.

Examples:
    
    
    count(/host/key,10m) #the values for the last 10 minutes until now
           count(/host/key,10m,"like","error") #the number of values for the last 10 minutes until now that contain 'error'
           count(/host/key,10m,,12) #the number of values for the last 10 minutes until now that equal '12'
           count(/host/key,10m,"gt",12) #the number of values for the last 10 minutes until now that are over '12'
           count(/host/key,#10,"gt",12) #the number of values within the last 10 values until now that are over '12'
           count(/host/key,10m:now-1d,"gt",12) #the number of values between 24 hours and 10 minutes and 24 hours ago from now that were over '12'
           count(/host/key,10m,"bitand","6/7") #the number of values for the last 10 minutes until now having '110' (in binary) in the 3 least significant bits
           count(/host/key,10m:now-1d) #the number of values between 24 hours and 10 minutes and 24 hours ago from now

Copy

✔ Copied

##### countunique(/host/key,(sec|#num)<:time shift>,<operator>,<pattern>)

The number of unique values within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters;  

  * **operator** (must be double-quoted). Supported `operators`:  
_eq_ \- equal (default for integer, float)  
_ne_ \- not equal  
 _gt_ \- greater  
 _ge_ \- greater or equal  
 _lt_ \- less  
 _le_ \- less or equal  
 _like_ (default for string, text, log) - matches if contains pattern (case-sensitive)  
_bitand_ \- bitwise AND  
 _regexp_ \- case-sensitive match of the regular expression given in `pattern`  
 _iregexp_ \- case-insensitive match of the regular expression given in `pattern`  

  * **pattern** \- the required pattern (string arguments must be double-quoted).

Comments:

  * Float items match with the precision of 2.22e-16;
  * _like_ is not supported as operator for integer values;
  * _like_ and _bitand_ are not supported as operators for float values;
  * For string, text, and log values only _eq_ , _ne_ , _like_ , _regexp_ and _iregexp_ operators are supported;
  * With _bitand_ as operator, the fourth `pattern` parameter can be specified as two numbers, separated by '/': **number_to_compare_with/mask**. countunique() calculates "bitwise AND" from the value and the _mask_ and compares the result to _number_to_compare_with_. If the result of "bitwise AND" is equal to _number_to_compare_with_ , the value is counted.  
If _number_to_compare_with_ and _mask_ are equal, only the _mask_ need be specified (without '/').
  * With _regexp_ or _iregexp_ as operator, the fourth `pattern` parameter can be an ordinary or [global](/documentation/current/en/manual/regular_expressions#global-regular-expressions) (starting with '@') regular expression. In case of global regular expressions case sensitivity is inherited from global regular expression settings. For the purpose of regexp matching, float values will always be represented with 4 decimal digits after '.'. Also note that for large numbers difference in decimal (stored in database) and binary (used by Zabbix server) representation may affect the 4th decimal digit.

Examples:
    
    
    countunique(/host/key,10m) #the number of unique values for the last 10 minutes until now
           countunique(/host/key,10m,"like","error") #the number of unique values for the last 10 minutes until now that contain 'error'
           countunique(/host/key,10m,,12) #the number of unique values for the last 10 minutes until now that equal '12'
           countunique(/host/key,10m,"gt",12) #the number of unique values for the last 10 minutes until now that are over '12'
           countunique(/host/key,#10,"gt",12) #the number of unique values within the last 10 values until now that are over '12'
           countunique(/host/key,10m:now-1d,"gt",12) #the number of unique values between 24 hours and 10 minutes and 24 hours ago from now that were over '12'
           countunique(/host/key,10m,"bitand","6/7") #the number of unique values for the last 10 minutes until now having '110' (in binary) in the 3 least significant bits
           countunique(/host/key,10m:now-1d) #the number of unique values between 24 hours and 10 minutes and 24 hours ago from now

Copy

✔ Copied

##### find(/host/key,(sec|#num)<:time shift>,<operator>,<pattern>)

Find a value match within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.  
Returns: 1 - found; 0 - otherwise.

Parameters:

  * See common parameters;  

  * **sec** or **#num** (optional) - defaults to the latest value if not specified
  * **operator** (must be double-quoted). Supported `operators`:  
_eq_ \- equal (default for integer, float)  
_ne_ \- not equal  
 _gt_ \- greater  
 _ge_ \- greater or equal  
 _lt_ \- less  
 _le_ \- less or equal  
 _like_ (default for string, text, log) - matches if contains the string given in `pattern` (case-sensitive)  
_bitand_ \- bitwise AND  
 _regexp_ \- case-sensitive match of the regular expression given in `pattern`  
 _iregexp_ \- case-insensitive match of the regular expression given in `pattern`  

  * **pattern** \- the required pattern (string arguments must be double-quoted); [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE) regular expression if `operator` is _regexp_ , _iregexp_.

Comments:

  * If more than one value is processed, '1' is returned if there is at least one matching value;
  * _like_ is not supported as operator for integer values;
  * _like_ and _bitand_ are not supported as operators for float values;
  * For string, text, and log values only _eq_ , _ne_ , _like_ , _regexp_ and _iregexp_ operators are supported;
  * With _regexp_ or _iregexp_ as operator, the fourth `pattern` parameter can be an ordinary or [global](/documentation/current/en/manual/regular_expressions#global-regular-expressions) (starting with '@') regular expression. In case of global regular expressions case sensitivity is inherited from the global regular expression settings.

Example:
    
    
    find(/host/key,10m,"like","error") #find a value that contains 'error' within the last 10 minutes until now

Copy

✔ Copied

##### first(/host/key,sec<:time shift>)

The first (the oldest) value within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters.

See also last().

Example:
    
    
    first(/host/key,1h) #retrieve the oldest value within the last hour until now

Copy

✔ Copied

##### firstclock(/host/key,sec<:time shift>)

The timestamp of the oldest value within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters.

The function fails with an error if no data has been collected in the given period.

See also lastclock().

Example:
    
    
    firstclock(/host/key,1h) #retrieve the timestamp of the oldest value within the last hour until now
           firstclock(/host/key,1h:now-24h) #retrieve the timestamp of the oldest value within the last hour a day ago

Copy

✔ Copied

##### fuzzytime(/host/key,sec)

Check how much the passive agent time differs from the Zabbix server/proxy time.  
Supported value types: _Float_ , _Integer_.  
Returns: 1 - difference between the passive item value (as timestamp) and Zabbix server/proxy timestamp (the clock of value collection) is less than or equal to _sec_ seconds; 0 - otherwise.

Parameters:

  * See common parameters.

Comments:

  * Usually used with the 'system.localtime' item to check that local time is in sync with the local time of Zabbix server. _Note_ that 'system.localtime' must be configured as a [passive check](/documentation/current/en/manual/appendix/items/activepassive#passive-checks).
  * Can be used also with the `vfs.file.time[/path/file,modify]` key to check that the file did not get updates for long time;
  * This function is not recommended for use in complex trigger expressions (with multiple items involved), because it may cause unexpected results (time difference will be measured with the most recent metric), e.g. in `fuzzytime(/Host/system.localtime,60s)=0 or last(/Host/trap)<>0`.

Example:
    
    
    fuzzytime(/host/key,60s)=0 #detect a problem if the time difference is over 60 seconds  
      
    

Copy

✔ Copied

##### last(/host/key,<#num<:time shift>>)

The most recent value.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters;  

  * **#num** (optional) - the Nth most recent value.

Comments:

  * Take note that a hash-tagged time period (#N) works differently here than with many other functions. For example: `last(/host/key)` is always equal to `last(/host/key,#1)`; `last(/host/key,#3)` \- the third most recent value (_not_ three latest values);
  * Zabbix does not guarantee the exact order of values if more than two values exist within one second in history;
  * See also first().

Example:
    
    
    last(/host/key) #retrieve the last value
           last(/host/key,#2) #retrieve the previous value
           last(/host/key,#1) <> last(/host/key,#2) #the last and previous values differ

Copy

✔ Copied

##### lastclock(/host/key,<#num<:time shift>>)

The timestamp of the Nth most recent value within the defined evaluation period.  
Supported value types: _Float_ , _Integer_ , _String_ , _Text_ , _Log_.

Parameters:

  * See common parameters;  

  * **#num** (optional) - the Nth most recent value.

The function fails with an error if no data has been collected in the given period or no Nth value has been collected.

See also firstclock().

Example:
    
    
    lastclock(/host/key) #retrieve the timestamp of the latest value
           lastclock(/host/key,#2) #retrieve the timestamp of the 2nd latest value
           lastclock(/host/key,#3:now-1d) #retrieve the timestamp of the 3rd latest value a day ago

Copy

✔ Copied

##### logeventid(/host/key,<#num<:time shift>>,<pattern>)

Check if the event ID of the last log entry matches a regular expression.  
Supported value types: _Log_.  
Returns: 0 - does not match; 1 - matches.

Parameters:

  * See common parameters;  

  * **#num** (optional) - the Nth most recent value;  

  * **pattern** (optional) - the regular expression describing the required pattern, [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE) style (string arguments must be double-quoted).

##### logseverity(/host/key,<#num<:time shift>>)

Log severity of the last log entry.  
Supported value types: _Log_.  
Returns: 0 - default severity; N - severity (integer, useful for Windows event logs: 1 - Information, 2 - Warning, 4 - Error, 7 - Failure Audit, 8 - Success Audit, 9 - Critical, 10 - Verbose).

Parameters:

  * See common parameters;  

  * **#num** (optional) - the Nth most recent value.

Zabbix takes log severity from the **Information** field of Windows event log.

##### logsource(/host/key,<#num<:time shift>>,<pattern>)

Check if log source of the last log entry matches a regular expression.  
Supported value types: _Log_.  
Returns: 0 - does not match; 1 - matches.

Parameters:

  * See common parameters;  

  * **#num** (optional) - the Nth most recent value;  

  * **pattern** (optional) - the regular expression describing the required pattern, [Perl Compatible Regular Expression](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (PCRE) style (string arguments must be double-quoted).

Normally used for Windows event logs.

Example:
    
    
    logsource(/host/key,,"VMware Server")

Copy

✔ Copied

##### logtimestamp(/host/key,<#num<:time shift>>)

The log message timestamp of the Nth most recent log item value.  
Supported value types: _Log_.

Parameters:

  * See common parameters;  

  * **#num** (optional) - the Nth most recent value.

Comments:

  * Calculation of time shift is based on the item value clock, not on the log message timestamp;
  * The function fails with an error if: 
    * a non-log type item is received;
    * no data has been collected in the given period;
    * no Nth value has been collected;
    * log message does not contain a timestamp value.

Example:
    
    
    logtimestamp(/host/key) #retrieve the timestamp of the latest log message
           logtimestamp(/host/key,#2) #retrieve the timestamp of the 2nd latest log message
           logtimestamp(/host/key,#3:now-1d) #retrieve the timestamp of the 3rd latest log message a day ago

Copy

✔ Copied

##### monodec(/host/key,(sec|#num)<:time shift>,<mode>)

Check if there has been a monotonous decrease in values.  
Supported value types: _Integer_.  
Returns: 1 - if all elements in the time period continuously decrease; 0 - otherwise.

Parameters:

  * See common parameters;  

  * **mode** (must be double-quoted) - _weak_ (every value is smaller or the same as the previous one; default) or _strict_ (every value has decreased).

Example:
    
    
    monodec(/Host1/system.swap.size[all,free],60s) + monodec(/Host2/system.swap.size[all,free],60s) + monodec(/Host3/system.swap.size[all,free],60s) #calculate in how many hosts there has been a decrease in free swap size

Copy

✔ Copied

##### monoinc(/host/key,(sec|#num)<:time shift>,<mode>)

Check if there has been a monotonous increase in values.  
Supported value types: _Integer_.  
Returns: 1 - if all elements in the time period continuously increase; 0 - otherwise.

Parameters:

  * See common parameters;  

  * **mode** (must be double-quoted) - _weak_ (every value is bigger or the same as the previous one; default) or _strict_ (every value has increased).

Example:
    
    
    monoinc(/Host1/system.localtime,#3,"strict")=0 #check if the system local time has been increasing consistently

Copy

✔ Copied

##### nodata(/host/key,sec,<mode>)

Check for no data received.  
Supported value types: _Integer_ , _Float_ , _Character_ , _Text_ , _Log_.  
Returns: 1 - if no data received during the defined period of time; 0 - otherwise.

Parameters:

  * See common parameters;  

  * **sec** \- the period should not be less than 30 seconds because the history syncer process calculates this function only every 30 seconds; `nodata(/host/key,0)` is disallowed.
  * **mode** \- if set to _strict_ (double-quoted), this function will be insensitive to proxy availability (see comments for details).

Comments:

  * the 'nodata' triggers monitored by proxy are, by default, sensitive to proxy availability - if proxy becomes unavailable, the 'nodata' triggers will not fire immediately after a restored connection, but will skip the data for the delayed period. Note that for passive proxies suppression is activated if connection is restored more than 15 seconds and no less than 2 seconds later. For active proxies suppression is activated if connection is restored more than 15 seconds later. To turn off sensitiveness to proxy availability, use the third parameter, e.g.: `nodata(/host/key,5m,"strict")`; in this case the function will fire as soon as the evaluation period (five minutes) without data has past.  

  * This function will display an error if, within the period of the 1st parameter:  
\- there's no data and Zabbix server was restarted  
\- there's no data and maintenance was completed  
\- there's no data and the item was added or re-enabled  

  * Errors are displayed in the _Info_ column in trigger [configuration](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/triggers);  

  * This function may not work properly if there are time differences between Zabbix server, proxy and agent. See also: [Time synchronization requirement](/documentation/current/en/manual/installation/requirements#time-synchronization);  

  * nodata() function cannot be used in the expression by itself; at least one function from [another group](/documentation/current/en/manual/appendix/functions), referencing the host item, must be included in the expression (except [date and time functions](/documentation/current/en/manual/appendix/functions/time)). For detailed information on how the nodata() function works within expressions, see [Calculation time](/documentation/current/en/manual/config/triggers#calculation-time).

##### percentile(/host/key,(sec|#num)<:time shift>,percentage)

The P-th percentile of a period, where P (percentage) is specified by the third parameter.  
Supported value types: _Float_ , _Integer_.

Parameters:

  * See common parameters;  

  * **percentage** \- a floating-point number between 0 and 100 (inclusive) with up to 4 digits after the decimal point.

##### rate(/host/key,sec<:time shift>)

The per-second average rate of the increase in a monotonically increasing counter within the defined time period.  
Supported value types: _Float_ , _Integer_.

Parameters:

  * See common parameters.

Functionally corresponds to '[rate](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate)' of PromQL.

Example:
    
    
    rate(/host/key,30s) #if the monotonic increase over 30 seconds is 20, this function will return 0.67.

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).