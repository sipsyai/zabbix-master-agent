---
title: SLA object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/sla/object
downloaded: 2025-11-14 10:44:31
---

# SLA object

The following objects are directly related to the `sla` (Service Level Agreement) API.

### SLA

The SLA object has the following properties.

slaid | ID | ID of the SLA.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the SLA.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
period | integer | Reporting period of the SLA.  
  
Possible values:  
0 - daily;  
1 - weekly;  
2 - monthly;  
3 - quarterly;  
4 - annually.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
slo | float | Minimum acceptable Service Level Objective expressed as a percent. If the Service Level Indicator (SLI) drops lower, the SLA is considered to be in problem/unfulfilled state.  
  
Possible values: 0-100 (up to 4 fractional digits).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
effective_date | integer | Effective date of the SLA.  
  
Possible values: date timestamp in UTC.  
timezone | string | Reporting time zone, for example: `Europe/London`, `UTC`.  
  
For the full list of supported time zones please refer to [PHP documentation](https://www.php.net/manual/en/timezones.php).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
status | integer | Status of the SLA.  
  
Possible values:  
0 - _(default)_ disabled SLA;  
1 - enabled SLA.  
description | string | Description of the SLA.  
  
### SLA schedule

The SLA schedule object defines periods where the connected service(s) are scheduled to be in working order. It has the following properties.

period_from | integer | Starting time of the recurrent weekly period of time (inclusive).  
  
Possible values: number of seconds (counting from Sunday).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
period_to | integer | Ending time of the recurrent weekly period of time (exclusive).  
  
Possible values: number of seconds (counting from Sunday).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### SLA excluded downtime

The excluded downtime object defines periods where the connected service(s) are scheduled to be out of working order, without affecting SLI, e.g., undergoing planned maintenance. It has the following properties.

name | string | Name of the excluded downtime.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
period_from | integer | Starting time of the excluded downtime (inclusive).  
  
Possible values: timestamp.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
period_to | integer | Ending time of the excluded downtime (exclusive).  
  
Possible values: timestamp.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### SLA service tag

The SLA service tag object links services to include in the calculations for the SLA. It has the following properties.

tag | string | SLA service tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
operator | integer | SLA service tag [operator](/documentation/current/en/manual/it_services/sla#configuration).  
  
Possible values:  
0 - _(default)_ Equals;  
2 - Contains.  
value | string | SLA service tag value.