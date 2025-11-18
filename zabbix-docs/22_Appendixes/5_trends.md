---
title: Trend functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/trends
downloaded: 2025-11-14 10:47:43
---

# 5 Trend functions

Trend functions, in contrast to [history functions](/documentation/current/en/manual/appendix/functions/history), use [trend](/documentation/current/en/manual/config/items/history_and_trends#keeping-trends) data for calculations.

Trends store hourly aggregate values. Trend functions use these hourly averages, and thus are useful for long-term analysis.

Trend function results are cached so multiple calls to the same function with the same parameters fetch info from the database only once. The trend function cache is controlled by the [TrendFunctionCacheSize](/documentation/current/en/manual/appendix/config/zabbix_server#trendfunctioncachesize) server parameter.

Triggers that reference trend functions **only** are evaluated once per the smallest time period in the expression. For instance, a trigger like
    
    
    trendavg(/host/key,1d:now/d) > 1 or trendavg(/host/key2,1w:now/w) > 2

Copy

✔ Copied

will be evaluated once per day. If the trigger contains both trend and history (or [date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata)) functions, it is calculated in accordance with the [usual principles](/documentation/current/en/manual/config/triggers#calculation-time).

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

The functions are listed without additional information. Click on the function to see the full details.

baselinedev | Returns the number of deviations (by stddevpop algorithm) between the last data period and the same data periods in preceding seasons.  
---|---  
baselinewma | Calculates the baseline by averaging data from the same timeframe in multiple equal time periods ('seasons') using the weighted moving average algorithm.  
trendavg | The average of trend values within the defined time period.  
trendcount | The number of successfully retrieved history values used to calculate the trend value within the defined time period.  
trendmax | The maximum in trend values within the defined time period.  
trendmin | The minimum in trend values within the defined time period.  
trendstl | Returns the rate of anomalies during the detection period - a decimal value between 0 and 1 that is `((the number of anomaly values)/(total number of values))`.  
trendsum | The sum of trend values within the defined time period.  
  
##### Common parameters

  * `/host/key` is a common mandatory first parameter
  * `time period:time shift` is a common second parameter, where: 
    * **time period** \- the time period (minimum '1h'), defined as <N><time unit> where `N` \- the number of time units, `time unit` \- h (hour), d (day), w (week), M (month) or y (year).
    * **time shift** \- the [time period offset](/documentation/current/en/manual/config/triggers/expression#time-shift) (see function examples)

### Function details

Some general notes on function parameters:

  * Function parameters are separated by a comma
  * Optional function parameters (or parameter parts) are indicated by `<` `>`
  * Function-specific parameters are described with each function
  * `/host/key` and `time period:time shift` parameters must never be quoted

##### baselinedev(/host/key,data period:time shift,season unit,num seasons)

Returns the number of deviations (by stddevpop algorithm) between the last data period and the same data periods in preceding seasons.  

Parameters:

  * See common parameters;  

  * **data period** \- the data gathering period within a season, defined as <N><time unit> where:  
`N` \- the number of time units  
`time unit` \- h (hour), d (day), w (week), M (month) or y (year), must be equal to or less than season  

  * **season unit** \- the duration of one season (h, d, w, M, y), cannot be smaller than data period;
  * **num seasons** \- the number of seasons to evaluate.

Examples:
    
    
    baselinedev(/host/key,1d:now/d,"M",6) #calculating the number of standard deviations (population) between the previous day and the same day in the previous 6 months. If the date doesn't exist in a previous month, the last day of the month will be used (Jul,31 will be analysed against Jan,31, Feb, 28,... June, 30)
           baselinedev(/host/key,1h:now/h,"d",10)  #calculating the number of standard deviations (population) between the previous hour and the same hours over the period of ten days before yesterday

Copy

✔ Copied

##### baselinewma(/host/key,data period:time shift,season unit,num seasons)

Calculates the baseline by averaging data from the same timeframe in multiple equal time periods ('seasons') using the weighted moving average algorithm.  

Parameters:

  * See common parameters;  

  * **data period** \- the data gathering period within a season, defined as <N><time unit> where:  
`N` \- the number of time units  
`time unit` \- h (hour), d (day), w (week), M (month) or y (year), must be equal to or less than season  
Time shift - the time period offset, defines the end of data gathering time frame in seasons (see examples);  

  * **season unit** \- the duration of one season (h, d, w, M, y), cannot be smaller than data period;  

  * **num seasons** \- the number of seasons to evaluate.

Examples:
    
    
    baselinewma(/host/key,1h:now/h,"d",3) #calculating the baseline based on the last full hour within a 3-day period that ended yesterday. If "now" is Monday 13:30, the data for 12:00-12:59 on Friday, Saturday, and Sunday will be analyzed
           baselinewma(/host/key,2h:now/h,"d",3) #calculating the baseline based on the last two hours within a 3-day period that ended yesterday. If "now" is Monday 13:30, the data for 11:00-12:59 on Friday, Saturday, and Sunday will be analyzed
           baselinewma(/host/key,1d:now/d,"M",4) #calculating the baseline based on the same day of month as 'yesterday' in the 4 months preceding the last full month. If the required date doesn't exist, the last day of month is taken. If today is September 1st, the data for July 31st, June 30th, May 31st, April 30th will be analyzed.

Copy

✔ Copied

##### trendavg(/host/key,time period:time shift)

The average of trend values within the defined time period.

Parameters:

  * See common parameters.

Examples:
    
    
    trendavg(/host/key,1h:now/h) #the average for the previous hour (e.g. 12:00-13:00)
           trendavg(/host/key,1h:now/h-1h) #the average for two hours ago (11:00-12:00)
           trendavg(/host/key,1h:now/h-2h) #the average for three hours ago (10:00-11:00)
           trendavg(/host/key,1M:now/M-1y) #the average for the previous month a year ago

Copy

✔ Copied

##### trendcount(/host/key,time period:time shift)

The number of successfully retrieved history values used to calculate the trend value within the defined time period.

Parameters:

  * See common parameters.

Examples:
    
    
    trendcount(/host/key,1h:now/h) #the value count for the previous hour (e.g. 12:00-13:00)
           trendcount(/host/key,1h:now/h-1h) #the value count for two hours ago (11:00-12:00)
           trendcount(/host/key,1h:now/h-2h) #the value count for three hours ago (10:00-11:00)
           trendcount(/host/key,1M:now/M-1y) #the value count for the previous month a year ago

Copy

✔ Copied

##### trendmax(/host/key,time period:time shift)

The maximum in trend values within the defined time period.

Parameters:

  * See common parameters.

Examples:
    
    
    trendmax(/host/key,1h:now/h) #the maximum for the previous hour (e.g. 12:00-13:00)
           trendmax(/host/key,1h:now/h) - trendmin(/host/key,1h:now/h) → calculate the difference between the maximum and minimum values (trend delta) for the previous hour (12:00-13:00)
           trendmax(/host/key,1h:now/h-1h) #the maximum for two hours ago (11:00-12:00)
           trendmax(/host/key,1h:now/h-2h) #the maximum for three hours ago (10:00-11:00)
           trendmax(/host/key,1M:now/M-1y) #the maximum for the previous month a year ago

Copy

✔ Copied

##### trendmin(/host/key,time period:time shift)

The minimum in trend values within the defined time period.

Parameters:

  * See common parameters.

Examples:
    
    
    trendmin(/host/key,1h:now/h) #the minimum for the previous hour (e.g. 12:00-13:00)
           trendmax(/host/key,1h:now/h) - trendmin(/host/key,1h:now/h) → calculate the difference between the maximum and minimum values (trend delta) for the previous hour (12:00-13:00)
           trendmin(/host/key,1h:now/h-1h) #the minimum for two hours ago (11:00-12:00)
           trendmin(/host/key,1h:now/h-2h) #the minimum for three hours ago (10:00-11:00)
           trendmin(/host/key,1M:now/M-1y) #the minimum for the previous month a year ago

Copy

✔ Copied

##### trendstl(/host/key,eval period:time shift,detection period,season,<deviations>,<devalg>,<s window>)

Returns the rate of anomalies during the detection period - a decimal value between 0 and 1 that is `((the number of anomaly values)/(total number of values))`.

Parameters:

  * See common parameters;  

  * **eval period** \- the time period that must be decomposed (minimum '1h'), defined as <N><time unit> where  
`N` \- the number of time units  
`time unit` \- h (hour), d (day), w (week), M (month) or y (year)  

  * **detection period** \- the time period before the end of eval period for which anomalies are calculated (minimum '1h', cannot be longer than eval period), defined as <N><time unit> where  
`N` \- the number of time units  
`time unit` \- h (hour), d (day), w (week)  

  * **season** \- the shortest time period where a repeating pattern ("season") is expected (minimum '2h', cannot be longer than eval period, the number of entries in the eval period must be greater than the two times of the resulting frequency (season/h)), defined as <N><time unit> where  
`N` \- the number of time units  
`time unit` \- h (hour), d (day), w (week)
  * **deviations** \- the number of deviations (calculated by devalg) to count as anomaly (can be decimal), (must be greater than or equal to 1, default is 3);
  * **devalg** (must be double-quoted) - the deviation algorithm, can be _stddevpop_ , _stddevsamp_ or _mad_ (default);
  * **s window** \- the span (in lags) of the loess window for seasonal extraction (default is 10 * number of entries in eval period + 1)

Examples:
    
    
    trendstl(/host/key,100h:now/h,10h,2h) #analyse the last 100 hours of trend data, find the anomaly rate for the last 10 hours of that period, expecting the periodicity to be 2h, the remainder series values of the evaluation period are considered anomalies if they reach the value of 3 deviations of the MAD of that remainder series
           trendstl(/host/key,100h:now/h-10h,100h,2h,2.1,"mad") #analyse the period of 100 hours of trend data, up to 10 hours ago, find the anomaly rate for that entire period expecting the periodicity to be 2h, the remainder series values of the evaluation period are considered anomalies if they reach the value of 2,1 deviations of the MAD of that remainder series
           trendstl(/host/key,100d:now/d-1d,10d,1d,4,,10) #analyse 100 days of trend data up to a day ago, find the anomaly rate for the period of last 10d of that period, expecting the periodicity to be 1d, the remainder series values of the evaluation period are considered anomalies if they reach the value of 4 deviations of the MAD of that remainder series, overriding the default span of the loess window for seasonal extraction of "10 * number of entries in eval period + 1" with the span of 10 lags
           trendstl(/host/key,1M:now/M-1y,1d,2h,,"stddevsamp") #analyse the previous month a year ago, find the anomaly rate of the last day of that period expecting the periodicity to be 2h, the remainder series values of the evaluation period are considered anomalies if they reach the value of 3 deviation of the sample standard deviation of that remainder series

Copy

✔ Copied

##### trendsum(/host/key,time period:time shift)

The sum of trend values within the defined time period.

Parameters:

  * See common parameters.

Examples:
    
    
    trendsum(/host/key,1h:now/h) #the sum for the previous hour (e.g. 12:00-13:00)
           trendsum(/host/key,1h:now/h-1h) #the sum for two hours ago (11:00-12:00)
           trendsum(/host/key,1h:now/h-2h) #the sum for three hours ago (10:00-11:00)
           trendsum(/host/key,1M:now/M-1y) #the sum for the previous month a year ago

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).