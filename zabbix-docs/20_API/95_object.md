---
title: Event object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/event/object
downloaded: 2025-11-14 10:41:29
---

# Event object

The following objects are directly related to the `event` API.

### Event

Events are created by the Zabbix server and cannot be modified via the API.

The event object has the following properties.

eventid | ID | ID of the event.  
---|---|---  
source | integer | Type of the event.  
  
Possible values:  
0 - event created by a trigger;  
1 - event created by a discovery rule;  
2 - event created by active agent autoregistration;  
3 - internal event;  
4 - event created on service status update.  
object | integer | Type of object that is related to the event.  
  
Possible values if `source` is set to "event created by a trigger":  
0 - trigger.  
  
Possible values if `source` is set to "event created by a discovery rule":  
1 - discovered host;  
2 - discovered service.  
  
Possible values if `source` is set to "event created by active agent autoregistration":  
3 - auto-registered host.  
  
Possible values if `source` is set to "internal event":  
0 - trigger;  
4 - item;  
5 - LLD rule.  
  
Possible values if `source` is set to "event created on service status update":  
6 - service.  
objectid | ID | ID of the related object.  
acknowledged | integer | Whether the event has been acknowledged.  
clock | timestamp | Time when the event was created.  
ns | integer | Nanoseconds when the event was created.  
name | string | Resolved event name.  
value | integer | State of the related object.  
  
Possible values if `source` is set to "event created by a trigger" or "event created on service status update":  
0 - OK;  
1 - problem.  
  
Possible values if `source` is set to "event created by a discovery rule":  
0 - host or service up;  
1 - host or service down;  
2 - host or service discovered;  
3 - host or service lost.  
  
Possible values if `source` is set to "internal event":  
0 - "normal" state;  
1 - "unknown" or "not supported" state.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `source` is set to "event created by a trigger", "event created by a discovery rule", "internal event", or "event created on service status update"  
severity | integer | Event current severity.  
  
Possible values:  
0 - not classified;  
1 - information;  
2 - warning;  
3 - average;  
4 - high;  
5 - disaster.  
r_eventid | ID | ID of the recovery event.  
c_eventid | ID | ID of the event that was used to override (close) current event under global correlation rule. See `correlationid` to identify exact correlation rule.  
This parameter is only defined when the event is closed by global correlation rule.  
cause_eventid | ID | ID of the cause event.  
correlationid | ID | ID of the correlation rule that generated closing of the problem.  
This parameter is only defined when the event is closed by global correlation rule.  
userid | ID | ID of the user that closed the event (if the event was closed manually).  
suppressed | integer | Whether the event is suppressed.  
  
Possible values:  
0 - event is in normal state;  
1 - event is suppressed.  
opdata | string | Operational data with expanded macros.  
urls | array | Active [media type URLs](/documentation/current/en/manual/api/reference/problem/object#media-type-url).  
  
### Event tag

The event tag object has the following properties.

tag | string | Event tag name.  
---|---|---  
value | string | Event tag value.  
  
### Media type URL

The media type URL object has the following properties.

name | string | Media type defined URL name.  
---|---|---  
url | string | Media type defined URL value.  
  
Results will contain entries only for active media types with enabled event menu entry. Macro used in properties will be expanded, but if one of the properties contains an unexpanded macro, both properties will be excluded from results. For supported macros, see [_Supported macros_](/documentation/current/en/manual/appendix/macros/supported_by_location).