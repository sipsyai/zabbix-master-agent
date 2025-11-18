---
title: Problem object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/problem/object
downloaded: 2025-11-14 10:43:39
---

# Problem object

The following objects are directly related to the `problem` API.

### Problem

Problems are created by the Zabbix server and cannot be modified via the API.

The problem object has the following properties.

eventid | ID | ID of the problem event.  
---|---|---  
source | integer | Type of the problem event.  
  
Possible values:  
0 - event created by a trigger;  
3 - internal event;  
4 - event created on service status update.  
object | integer | Type of object that is related to the problem event.  
  
Possible values if `source` is set to "event created by a trigger":  
0 - trigger.  
  
Possible values if `source` is set to "internal event":  
0 - trigger;  
4 - item;  
5 - LLD rule.  
  
Possible values if `source` is set to "event created on service status update":  
6 - service.  
objectid | ID | ID of the related object.  
clock | timestamp | Time when the problem event was created.  
ns | integer | Nanoseconds when the problem event was created.  
r_eventid | ID | ID of the recovery event.  
r_clock | timestamp | Time when the recovery event was created.  
r_ns | integer | Nanoseconds when the recovery event was created.  
cause_eventid | ID | ID of the cause event.  
correlationid | ID | ID of the correlation rule if this event was recovered by a global correlation rule.  
userid | ID | ID of the user that closed the problem (if the problem was closed manually).  
name | string | Resolved problem name.  
acknowledged | integer | Acknowledge state for problem.  
  
Possible values:  
0 - not acknowledged;  
1 - acknowledged.  
severity | integer | Problem current severity.  
  
Possible values:  
0 - not classified;  
1 - information;  
2 - warning;  
3 - average;  
4 - high;  
5 - disaster.  
suppressed | integer | Whether the problem is suppressed.  
  
Possible values:  
0 - problem is in normal state;  
1 - problem is suppressed.  
opdata | string | Operational data with expanded macros.  
urls | array | Active [media type URLs](/documentation/current/en/manual/api/reference/problem/object#media-type-url).  
  
#### Media type URL

The media type URL object has the following properties.

name | string | Media type defined URL name.  
---|---|---  
url | string | Media type defined URL value.  
  
Results will contain entries only for active media types with enabled event menu entry. Macro used in properties will be expanded, but if one of the properties contains an unexpanded macro, both properties will be excluded from results. For supported macros, see [_Supported macros_](/documentation/current/en/manual/appendix/macros/supported_by_location).

### Problem tag

The problem tag object has the following properties.

tag | string | Problem tag name.  
---|---|---  
value | string | Problem tag value.