---
title: Predictive trigger functions
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/prediction
downloaded: 2025-11-14 10:35:38
---

# 7 Predictive trigger functions

#### Overview

Sometimes there are signs of the upcoming problem. These signs can be spotted so that actions may be taken in advance to prevent or at least minimize the impact of the problem.

Zabbix has tools to predict the future behavior of the monitored system based on historic data. These tools are realized through predictive trigger functions.

#### Functions

Before setting a trigger, it is necessary to define what a problem state is and how much time is needed to take action. Then there are two ways to set up a trigger signaling about a potential unwanted situation. First: the trigger must fire when the system is expected to be in a problem state after "time to act". Second: the trigger must fire when the system is going to reach the problem state in less than "time to act". Corresponding trigger functions to use are **forecast** and **timeleft**. Note that underlying statistical analysis is basically identical for both functions. You may set up a trigger whichever way you prefer with similar results.

#### Parameters

Both functions use almost the same set of parameters. Use the list of [supported functions](/documentation/current/en/manual/appendix/functions) for reference.

##### Time interval

First of all, you should specify the historic period Zabbix should analyze to come up with the prediction. You do it in a familiar way by means of the `time period` parameter and optional time shift like you do it with **avg** , **count** , **delta** , **max** , **min** and **sum** functions.

##### Forecasting horizon

(**forecast** only)  
Parameter `time` specifies how far in the future Zabbix should extrapolate dependencies it finds in historic data. No matter if you use `time_shift` or not, `time` is always counted starting from the current moment.

##### Threshold to reach

(**timeleft** only)  
Parameter `threshold` specifies a value the analyzed item has to reach, no difference if from above or from below. Once we have determined f(t) (see below), we should solve equation f(t) = `threshold` and return the root which is closer to now and to the right from now or 1.7976931348623158E+308 if there is no such root.

When item values approach the threshold and then cross it, **timeleft** assumes that intersection is already in the past and therefore switches to the next intersection with `threshold` level, if any. Best practice should be to use predictions as a complement to ordinary problem diagnostics, not as a substitution.1

##### Fit functions

Default `fit` is the _linear_ function. But if your monitored system is more complicated you have more options to choose from.

_linear_ | x = a + b*t  
---|---  
_polynomialN_2 | x = a0 \+ a1*t + a2*t2 \+ ... + an*tn  
_exponential_ | x = a*exp(b*t)  
_logarithmic_ | x = a + b*log(t)  
_power_ | x = a*tb  
  
##### Modes

(**forecast** only)  
Every time a trigger function is evaluated, it gets data from the specified history period and fits a specified function to the data. So, if the data is slightly different, the fitted function will be slightly different. If we simply calculate the value of the fitted function at a specified time in the future, you will know nothing about how the analyzed item is expected to behave between now and that moment in the future. For some `fit` options (like _polynomial_) a simple value from the future may be misleading.

_value_ | f(now + `time`)  
---|---  
_max_ | maxnow <= t <= now + `time` f(t)  
_min_ | minnow <= t <= now + `time` f(t)  
_delta_ | _max_ \- _min_  
_avg_ | average of f(t) (now <= t <= now + `time`) according to [definition](https://en.wikipedia.org/wiki/Mean_of_a_function)  
  
#### Details

To avoid calculations with huge numbers, we consider the timestamp of the first value in specified period plus 1 ns as a new zero-time (current epoch time is of order 109, epoch squared is 1018, double precision is about 10-16). 1 ns is added to provide all positive time values for _logarithmic_ and _power_ fits which involve calculating log(t). Time shift does not affect _linear_ , _polynomial_ , _exponential_ (apart from easier and more precise calculations) but changes the shape of _logarithmic_ and _power_ functions.

#### Potential errors

Functions return -1 in such situations:

  * specified evaluation period contains no data;
  * result of mathematical operation is not defined3;
  * numerical complications (unfortunately, for some sets of input data range and precision of double-precision floating-point format become insufficient)4.

No warnings or errors are flagged if chosen fit poorly describes provided data or there is just too few data for accurate prediction.

#### Examples and dealing with errors

To get a warning when you are about to run out of free disk space on your host, you may use a trigger expression like this:
    
    
    timeleft(/host/vfs.fs.size[/,free],1h,0)<1h

Copy

✔ Copied

However, error code -1 may come into play and put your trigger in a problem state. Generally it's good because you get a warning that your predictions don't work correctly and you should look at them more thoroughly to find out why. But sometimes it's bad because -1 can simply mean that there was no data about the host free disk space obtained in the last hour. If you are getting too many false positive alerts, consider using more complicated trigger expression 5:
    
    
    timeleft(/host/vfs.fs.size[/,free],1h,0)<1h and timeleft(/host/vfs.fs.size[/,free],1h,0)<>-1

Copy

✔ Copied

The situation is a bit more difficult with **forecast**. First of all, -1 may or may not put the trigger in a problem state depending on whether you have expression like `forecast(/host/item,(...))<...` or like `forecast(/host/item,(...))>...`

Furthermore, -1 may be a valid forecast if it's normal for the item value to be negative. But probability of this situation in the real world situation is negligible (see [how](/documentation/current/en/manual/config/triggers/expression) the operator **=** works). So add `... or forecast(/host/item,(...))=-1` or `... and forecast(/host/item,(...))<>-1` if you want or don't want to treat -1 as a problem respectively.

#### Footnotes

**1** For example, a simple trigger like `timeleft(/host/item,1h,X) < 1h` may go into problem state when the item value approaches X and then suddenly recover once value X is reached. If the problem is item value being below X, use: `last(/host/item) < X or timeleft(/host/item,1h,X) < 1h` If the problem is item value being above X use: `last(/host/item) > X or timeleft(/host/item,1h,X) < 1h`

**2** Polynomial degree can be from 1 to 6, _polynomial1_ is equivalent to _linear_. However, use higher degree polynomials [with caution](https://en.wikipedia.org/wiki/Runge's_phenomenon). If the evaluation period contains less points than needed to determine polynomial coefficients, polynomial degree will be lowered (e.g., _polynomial5_ is requested, but there are only 4 points, therefore _polynomial3_ will be fitted).

**3** For example, fitting _exponential_ or _power_ functions involves calculating log() of item values. If data contains zeros or negative numbers, you will get an error since log() is defined for positive values only.

**4** For _linear_ , _exponential_ , _logarithmic_ and _power_ fits all necessary calculations can be written explicitly. For _polynomial_ only _value_ can be calculated without any additional steps. Calculating _avg_ involves computing polynomial antiderivative (analytically). Computing _max_ , _min_ and _delta_ involves computing polynomial derivative (analytically) and finding its roots (numerically). Solving f(t) = 0 involves finding polynomial roots (numerically).

**5** But in this case -1 can cause your trigger to recover from the problem state. To be fully protected use: `timeleft(/host/vfs.fs.size[/,free],1h,0)<1h and ({TRIGGER.VALUE}=0 and timeleft(/host/vfs.fs.size[/,free],1h,0)<>-1 or {TRIGGER.VALUE}=1)`