---
title: Report object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/report/object
downloaded: 2025-11-14 10:44:00
---

# Report object

The following objects are directly related to the `report` API.

### Report

The report object has the following properties:

reportid | ID | ID of the report.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
userid | ID | ID of the user who created the report.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Unique name of the report.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
dashboardid | ID | ID of the dashboard that the report is based on.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
period | integer | Period for which the report will be prepared.  
  
Possible values:  
0 - _(default)_ previous day;  
1 - previous week;  
2 - previous month;  
3 - previous year.  
cycle | integer | Period repeating schedule.  
  
Possible values:  
0 - _(default)_ daily;  
1 - weekly;  
2 - monthly;  
3 - yearly.  
start_time | integer | Time of the day, in seconds, when the report will be prepared for sending.  
  
Default: 0.  
weekdays | integer | Days of the week for sending the report.  
  
Possible bitmap values:  
1 - Monday;  
2 - Tuesday;  
4 - Wednesday;  
8 - Thursday;  
16 - Friday;  
32 - Saturday;  
64 - Sunday.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 21 for Monday, Wednesday, and Friday).  
  
Default: 0.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `cycle` is set to "weekly".  
active_since | string | On which date to start.  
  
Possible values:  
empty string - _(default)_ not specified (stored as 0);  
specific date in YYYY-MM-DD format (stored as a timestamp of the beginning of a day (00:00:00)).  
active_till | string | On which date to end.  
  
Possible values:  
empty string - _(default)_ not specified (stored as 0);  
specific date in YYYY-MM-DD format (stored as a timestamp of the end of a day (23:59:59)).  
subject | string | Report message subject.  
message | string | Report message text.  
status | integer | Whether the report is enabled or disabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
description | text | Description of the report.  
state | integer | State of the report.  
  
Possible values:  
0 - _(default)_ report was not yet processed;  
1 - report was generated and successfully sent to all recipients;  
2 - report generating failed; "info" contains error information;  
3 - report was generated, but sending to some (or all) recipients failed; "info" contains error information.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
lastsent | timestamp | Unix timestamp of the last successfully sent report.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
info | string | Error description or additional information.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
  
### Users

The users object has the following properties:

userid | ID | ID of user to send the report to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
access_userid | ID | ID of user on whose behalf the report will be generated.  
  
0 - _(default)_ Generate report by recipient.  
exclude | integer | Whether to exclude the user from mailing list.  
  
Possible values:  
0 - _(default)_ Include;  
1 - Exclude.  
  
### User groups

The user groups object has the following properties:

usrgrpid | ID | ID of user group to send the report to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
access_userid | ID | ID of user on whose behalf the report will be generated.  
  
0 - _(default)_ Generate report by recipient.