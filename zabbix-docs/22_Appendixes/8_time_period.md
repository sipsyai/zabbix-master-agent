---
title: Time period syntax
source: https://www.zabbix.com/documentation/current/en/manual/appendix/time_period
downloaded: 2025-11-14 10:47:53
---

# 8 Time period syntax

#### Overview

To set a time period, the following format has to be used:
    
    
    d-d,hh:mm-hh:mm

Copy

✔ Copied

where the symbols stand for the following:

_d_ | Day of the week: 1 - Monday, 2 - Tuesday ,... , 7 - Sunday  
---|---  
_hh_ | Hours: 00-24  
_mm_ | Minutes: 00-59  
  
You can specify more than one time period using a semicolon (;) separator:
    
    
    d-d,hh:mm-hh:mm;d-d,hh:mm-hh:mm...

Copy

✔ Copied

Leaving the time period empty equals 1-7,00:00-24:00, which is the default value.

The upper limit of a time period is not included. Thus, if you specify 09:00-18:00 the last second included in the time period is 17:59:59.

#### Examples

Working hours. Monday - Friday from 9:00 till 18:00:
    
    
    1-5,09:00-18:00

Copy

✔ Copied

Working hours plus weekend. Monday - Friday from 9:00 till 18:00 and Saturday, Sunday from 10:00 till 16:00:
    
    
    1-5,09:00-18:00;6-7,10:00-16:00

Copy

✔ Copied