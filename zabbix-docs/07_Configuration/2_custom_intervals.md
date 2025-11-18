---
title: Custom intervals
source: https://www.zabbix.com/documentation/current/en/manual/config/items/item/custom_intervals
downloaded: 2025-11-14 10:34:43
---

# 2 Custom intervals

#### Overview

It is possible to create custom rules regarding the times when an item is checked. The two methods for that are _Flexible intervals_ , which allow to redefine the default update interval, and _Scheduling_ , whereby an item check can be executed at a specific time or sequence of times.

#### Flexible intervals

Flexible intervals allow to redefine the default update interval for specific time periods. A flexible interval is defined with _Interval_ and _Period_ where:

  * _Interval_ – the update interval for the specified time period. [Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g., 30s, 1m, 2h, 1d.
  * _Period_ – the time period when the flexible interval is active (see the [time periods](/documentation/current/en/manual/appendix/time_period) for detailed description of the _Period_ format)

If multiple flexible intervals overlap, the smallest _Interval_ value is used for the overlapping period. Note that if the smallest value of overlapping flexible intervals is '0', no polling will take place. Outside the flexible intervals the default update interval is used.

Note that if the flexible interval equals the length of the period, the item will be checked exactly once. If the flexible interval is greater than the period, the item might be checked once or it might not be checked at all (thus such configuration is not recommended). If the flexible interval is less than the period, the item will be checked at least once.

If the flexible interval is set to '0', the item is not polled during the flexible interval period and resumes polling according to the default _Update interval_ once the period is over. Examples:

10 | 1-5,09:00-18:00 | Item will be checked every 10 seconds during working hours.  
---|---|---  
0 | 1-7,00:00-7:00 | Item will not be checked during the night.  
0 | 7-7,00:00-24:00 | Item will not be checked on Sundays.  
60 | 1-7,12:00-12:01 | Item will be checked at 12:00 every day. Note that this was used as a workaround for scheduled checks and it is recommended to use scheduling intervals for such checks.  
  
#### Scheduling intervals

Scheduling intervals are used to check items at specific times. While flexible intervals are designed to redefine the default item update interval, the scheduling intervals are used to specify an independent checking schedule, which is executed in parallel.

A scheduling interval is defined as: `md<filter>wd<filter>h<filter>m<filter>s<filter>` where:

  * **md** \- month days
  * **wd** \- week days
  * **h** \- hours
  * **m** \- minutes
  * **s** – seconds

`<filter>` is used to specify values for its prefix (days, hours, minutes, seconds) and is defined as: `[<from>[-<to>]][/<step>][,<filter>]` where:

  * `<from>` and `<to>` define the range of matching values (included). If `<to>` is omitted then the filter matches a `<from> - <from>` range. If `<from>` is also omitted then the filter matches all possible values.
  * `<step>` defines the skips of the number value through the range. By default `<step>` has the value of 1, which means that all values of the defined range are matched.

While the filter definitions are optional, at least one filter must be used. A filter must either have a range or the _< step>_ value defined.

An empty filter matches either '0' if no lower-level filter is defined or all possible values otherwise. For example, if the hour filter is omitted then only '0' hour will match, provided minute and seconds filters are omitted too, otherwise an empty hour filter will match all hour values.

Valid `<from>` and `<to>` values for their respective filter prefix are:

md | Month days | 1-31 | 1-31  
---|---|---|---  
wd | Week days | 1-7 | 1-7  
h | Hours | 0-23 | 0-23  
m | Minutes | 0-59 | 0-59  
s | Seconds | 0-59 | 0-59  
  
The `<from>` value must be less or equal to `<to>` value. The `<step>` value must be greater or equal to 1 and less or equal to `<to>` \- `<from>`.

Single digit month days, hours, minutes and seconds values can be prefixed with 0. For example `md01-31` and `h/02` are valid intervals, but `md01-031` and `wd01-07` are not.

In Zabbix frontend, multiple scheduling intervals are entered in separate rows. In Zabbix API, they are concatenated into a single string with a semicolon `;` as a separator.

If a time is matched by several intervals it is executed only once. For example, `wd1h9;h9` will be executed only once on Monday at 9am.

Examples:

m0-59 | every minute  
---|---  
h9-17/2 | every 2 hours starting with 9:00 (9:00, 11:00 ...)  
m0,30 or m/30 | hourly at hh:00 and hh:30  
m0,5,10,15,20,25,30,35,40,45,50,55 or m/5 | every five minutes  
wd1-5h9 | every Monday till Friday at 9:00  
wd1-5h9-18 | every Monday till Friday at 9:00,10:00,...,18:00  
h9,10,11 or h9-11 | every day at 9:00, 10:00 and 11:00  
md1h9m30 | every 1st day of each month at 9:30  
md1wd1h9m30 | every 1st day of each month at 9:30 if it is Monday  
h9m/30 | every day at 9:00, 9:30  
h9m0-59/30 | every day at 9:00, 9:30  
h9,10m/30 | every day at 9:00, 9:30, 10:00, 10:30  
h9-10m30 | every day at 9:30, 10:30  
h9m10-40/30 | every day at 9:10, 9:40  
h9,10m10-40/30 | every day at 9:10, 9:40, 10:10, 10:40  
h9-10m10-40/30 | every day at 9:10, 9:40, 10:10, 10:40  
h9m10-40 | every day at 9:10, 9:11, 9:12, ... 9:40  
h9m10-40/1 | every day at 9:10, 9:11, 9:12, ... 9:40  
h9-12,15 | every day at 9:00, 10:00, 11:00, 12:00, 15:00  
h9-12,15m0 | every day at 9:00, 10:00, 11:00, 12:00, 15:00  
h9-12,15m0s30 | every day at 9:00:30, 10:00:30, 11:00:30, 12:00:30, 15:00:30  
h9-12s30 | every day at 9:00:30, 9:01:30, 9:02:30 ... 12:58:30, 12:59:30  
h9m/30;h10 (_API-specific syntax_) | every day at 9:00, 9:30, 10:00  
h9m/30  
h10 (_add this as another row in frontend_) | every day at 9:00, 9:30, 10:00  
  
##### Aligning time zones for proxies and agent

Note that Zabbix proxies and agent use their local time zones when processing scheduling intervals.

For this reason, when scheduling intervals are applied to items monitored by Zabbix proxy or agent active items, it is recommended to set the time zone of the respective proxies or agent the same as Zabbix server, otherwise the [queue](/documentation/current/en/manual/config/items/queue) may report item delays incorrectly.

The time zone for Zabbix proxy or agent can be set using the environment variable `TZ` in the `systemd` unit file:
    
    
    [Service]
           ...
           Environment="TZ=Europe/Amsterdam"

Copy

✔ Copied