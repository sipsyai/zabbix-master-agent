---
title: Predictive functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/prediction
downloaded: 2025-11-14 10:47:46
---

# 8 Predictive functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

The functions are listed without additional information. Click on the function to see the full details.

forecast | The future value, max, min, delta or avg of the item.  
---|---  
timeleft | The time in seconds needed for an item to reach the specified threshold.  
  
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

##### forecast(/host/key,(sec|#num)<:time shift>,time,<fit>,<mode>)

The future value, max, min, delta or avg of the item.  
Supported value types: _Float_ , _Integer_.

Parameters:

  * See common parameters;  

  * **time** \- the forecasting horizon in seconds (time suffixes can be used); negative values are supported;  

  * **fit** (optional; must be double-quoted) - the function used to fit historical data. Supported fits:  
_linear_ \- linear function (default)  
_polynomialN_ \- polynomial of degree N (1 <= N <= 6)  
_exponential_ \- exponential function  
 _logarithmic_ \- logarithmic function  
 _power_ \- power function  
Note that _polynomial1_ is equivalent to _linear_ ;
  * **mode** (optional; must be double-quoted) - the demanded output. Supported modes:  
_value_ \- value (default)  
_max_ \- maximum  
 _min_ \- minimum  
 _delta_ \- _max_ -_min_  
 _avg_ \- average  
Note that _value_ estimates the item value at the moment `now` \+ `time`; _max_ , _min_ , _delta_ and _avg_ investigate the item value estimate on the interval between `now` and `now` \+ `time`.

Comments:

  * If the value to return is larger than 1.7976931348623158E+308 or less than -1.7976931348623158E+308, the return value is cropped to 1.7976931348623158E+308 or -1.7976931348623158E+308 correspondingly;
  * Becomes unsupported only if misused in the expression (wrong item type, invalid parameters), otherwise returns -1 in case of errors;
  * See also additional information on [predictive trigger functions](/documentation/current/en/manual/config/triggers/prediction).

Examples:
    
    
    forecast(/host/key,#10,1h) #forecast the item value in one hour based on the last 10 values
           forecast(/host/key,1h,30m) #forecast the item value in 30 minutes based on the last hour data
           forecast(/host/key,1h:now-1d,12h) #forecast the item value in 12 hours based on one hour one day ago
           forecast(/host/key,1h,10m,"exponential") #forecast the item value in 10 minutes based on the last hour data and exponential function
           forecast(/host/key,1h,2h,"polynomial3","max") #forecast the maximum value the item can reach in the next two hours based on last hour data and cubic (third degree) polynomial
           forecast(/host/key,#2,-20m) #estimate the item value 20 minutes ago based on the last two values (this can be more precise than using last(), especially if the item is updated rarely, say, once an hour)

Copy

✔ Copied

##### timeleft(/host/key,(sec|#num)<:time shift>,threshold,<fit>)

The time in seconds needed for an item to reach the specified threshold.  
Supported value types: _Float_ , _Integer_.

Parameters:

  * See common parameters;  

  * **threshold** \- the value to reach ([unit suffixes](/documentation/current/en/manual/appendix/suffixes) can be used);
  * **fit** (optional; must be double-quoted) - see forecast().

Comments:

  * If the value to return is larger than 1.7976931348623158E+308, the return value is cropped to 1.7976931348623158E+308;
  * Returns 1.7976931348623158E+308 if the threshold cannot be reached;
  * Becomes unsupported only if misused in the expression (wrong item type, invalid parameters), otherwise returns -1 in case of errors;
  * See also additional information on [predictive trigger functions](/documentation/current/en/manual/config/triggers/prediction).

Examples:
    
    
    timeleft(/host/key,#10,0) #the time until the item value reaches zero based on the last 10 values
           timeleft(/host/key,1h,100) #the time until the item value reaches 100 based on the last hour data
           timeleft(/host/key,1h:now-1d,100) #the time until the item value reaches 100 based on one hour one day ago
           timeleft(/host/key,1h,200,"polynomial2") #the time until the item value reaches 200 based on the last hour data and assumption that the item behaves like a quadratic (second degree) polynomial

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).