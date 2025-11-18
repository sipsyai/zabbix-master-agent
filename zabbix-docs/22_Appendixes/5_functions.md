---
title: Supported functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions
downloaded: 2025-11-14 10:47:37
---

# 5 Supported functions

Click on the respective function group to see more details.

[Aggregate functions](/documentation/current/en/manual/appendix/functions/aggregate) | avg, bucket_percentile, count, histogram_quantile, item_count, kurtosis, mad, max, min, skewness, stddevpop, stddevsamp, sum, sumofsquares, varpop, varsamp  
---|---  
| [Foreach functions](/documentation/current/en/manual/appendix/functions/aggregate/foreach) | avg_foreach, bucket_rate_foreach, count_foreach, exists_foreach, last_foreach, max_foreach, min_foreach, sum_foreach  
[Bitwise functions](/documentation/current/en/manual/appendix/functions/bitwise) | bitand, bitlshift, bitnot, bitor, bitrshift, bitxor  
[Date and time functions](/documentation/current/en/manual/appendix/functions/time) | date, dayofmonth, dayofweek, now, time  
[History functions](/documentation/current/en/manual/appendix/functions/history) | change, changecount, count, countunique, find, first, firstclock, fuzzytime, last, lastclock, logeventid, logseverity, logsource, logtimestamp, monodec, monoinc, nodata, percentile, rate  
[Trend functions](/documentation/current/en/manual/appendix/functions/trends) | baselinedev, baselinewma, trendavg, trendcount, trendmax, trendmin, trendstl, trendsum  
[Mathematical functions](/documentation/current/en/manual/appendix/functions/math) | abs, acos, asin, atan, atan2, avg, cbrt, ceil, cos, cosh, cot, degrees, e, exp, expm1, floor, log, log10, max, min, mod, pi, power, radians, rand, round, signum, sin, sinh, sqrt, sum, tan, truncate  
[Operator functions](/documentation/current/en/manual/appendix/functions/operator) | between, in  
[Predictive functions](/documentation/current/en/manual/appendix/functions/prediction) | forecast, timeleft  
[String functions](/documentation/current/en/manual/appendix/functions/string) | ascii, bitlength, bytelength, char, concat, insert, jsonpath, left, length, ltrim, mid, repeat, replace, right, rtrim, trim, xmlxpath  
  
Except where stated otherwise, these functions are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

Foreach functions are supported only for [aggregate calculations](/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate).