---
title: event.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/event/get
downloaded: 2025-11-14 10:41:31
---

# event.get

### Description

`integer/array event.get(object parameters)`

The method allows to retrieve events according to the given parameters.

This method may return events of a deleted entity if these events have not been removed by the housekeeper yet.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

eventids | ID/array | Return only events with the given IDs.  
---|---|---  
groupids | ID/array | Return only events created by objects that belong to the given host groups.  
hostids | ID/array | Return only events created by objects that belong to the given hosts.  
objectids | ID/array | Return only events created by the given objects.  
source | integer | Return only events with the given type.  
  
Refer to the [event object page](object#event) for a list of supported event types.  
  
Default: 0 - trigger events.  
object | integer | Return only events created by objects of the given type.  
  
Refer to the [event object page](object#event) for a list of supported object types.  
  
Default: 0 - trigger.  
acknowledged | boolean | If set to `true` return only acknowledged events.  
action | integer | Return only events for which the given [event update actions](/documentation/current/en/manual/api/reference/event/acknowledge#parameters) have been performed. For multiple actions, use a sum of any acceptable bitmap values as bitmask (for example, 34 for acknowledge and suppress event).  
action_userids | ID/array | Return only events with the given IDs of users who performed the event update actions.  
suppressed | boolean | `true` \- return only suppressed events;  
`false` \- return events in the normal state.  
symptom | boolean | `true` \- return only symptom events;  
`false` \- return only cause events.  
severities | integer/array | Return only events with the given event severities. Applies only if object is trigger.  
trigger_severities | integer/array | Return only events with the given trigger severities. Applies only if object is trigger.  
evaltype | integer | Tag [evaluation method](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#using-filter).  
  
Possible values:  
0 - _(default)_ And/Or;  
2 - Or.  
tags | array | Return only events with the given tags.  
Format: `[{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...]`.  
An empty array returns all events.  
  
Possible [operator](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#using-filter) values:  
0 - _(default)_ Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
eventid_from | string | Return only events with IDs greater or equal to the given ID.  
eventid_till | string | Return only events with IDs less or equal to the given ID.  
time_from | timestamp | Return only events that have been created after or at the given time.  
time_till | timestamp | Return only events that have been created before or at the given time.  
problem_time_from | timestamp | Returns only events that were in the problem state from `problem_time_from` regardless of their current status. Applies only when the source is a trigger event and the object is a trigger. This parameter is mandatory if `problem_time_till` is specified.  
problem_time_till | timestamp | Returns only events that were in the problem state up to `problem_time_till` regardless of their current status. Applies only when the source is a trigger event and the object is a trigger. This parameter is mandatory if `problem_time_from` is specified.  
value | integer/array | Return only events with the given values.  
selectAcknowledges | query | Return an `acknowledges` property with event updates. Event updates are sorted in reverse chronological order.  
  
The event update object has the following properties:  
`acknowledgeid` \- `(ID)` acknowledgment's ID;  
`userid` \- `(ID)` ID of the user that updated the event;  
`clock` \- `(timestamp)` time when the event was updated;  
`message` \- `(string)` text of the message;  
`action` \- `(integer)` update action that was performed, see [`event.acknowledge`](/documentation/current/en/manual/api/reference/event/acknowledge);  
`old_severity` \- `(integer)` event severity before this update action;  
`new_severity` \- `(integer)` event severity after this update action;  
`suppress_until` \- `(timestamp)` time till event will be suppressed;  
`taskid` \- `(ID)` ID of task if current event is undergoing a rank change;  
`username` \- `(string)` username of the user that updated the event;  
`name` \- `(string)` name of the user that updated the event;  
`surname` \- `(string)` surname of the user that updated the event.  
  
Supports `count`.  
selectAlerts | query | Return an [`alerts`](/documentation/current/en/manual/api/reference/alert/object) property with alerts generated by the event. Alerts are sorted in reverse chronological order.  
selectHosts | query | Return a [`hosts`](/documentation/current/en/manual/api/reference/host/object) property with hosts containing the object that created the event. Supported only for events generated by triggers, items or LLD rules.  
selectRelatedObject | query | Return a `relatedObject` property with the object that created the event. The type of object returned depends on the event type.  
selectSuppressionData | query | Return a `suppression_data` property with the list of active maintenances and manual suppressions:  
`maintenanceid` \- `(ID)` ID of the maintenance;  
`userid` \- `(ID)` ID of user who suppressed the event;  
`suppress_until` \- `(integer)` time until the event is suppressed.  
selectTags | query | Return a [`tags`](/documentation/current/en/manual/api/reference/event/object#event-tag) property with event tags.  
filter | object | Return only those results that exactly match the given filter.  
  
Accepts an object, where the keys are property names, and the values are either a single value or an array of values to match against.  
  
Does not support properties of `text` [data type](/documentation/current/en/manual/api/reference_commentary#data-types).  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `eventid`, `objectid`, `clock`.  
  
Possible values when used together with `groupBy`: `objectid`.  
  
Possible values when used together with `countOutput` and `groupBy`: `objectid`, `rowscount`.  
groupBy | string/array | Group the results by the given properties. The specified properties will be returned in the results.  
  
Possible values: `objectid`.  
countOutput | boolean | These parameters are described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
editable | boolean  
excludeSearch | boolean  
limit | integer  
output | query  
preservekeys | boolean  
search | object  
searchByAny | boolean  
searchWildcardsEnabled | boolean  
sortorder | string/array  
startSearch | boolean  
  
### Return values

`(integer/array)` Returns either:

  * an array of objects;
  * the count of retrieved objects, if the `countOutput` parameter has been used, but the `groupBy` parameter has not been used;
  * an array of objects with aggregation results, if the `groupBy` parameter has been used.

### Examples

#### Retrieving trigger events

Retrieve the latest events from trigger "22395".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "event.get",
               "params": {
                   "output": "extend",
                   "selectAcknowledges": "extend",
                   "selectSuppressionData": "extend",
                   "selectTags": "extend",
                   "objectids": "22395",
                   "sortfield": ["clock", "eventid"],
                   "sortorder": "DESC"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "eventid": "20",
                       "source": "0",
                       "object": "0",
                       "objectid": "22395",
                       "clock": "1728658089",
                       "value": "0",
                       "acknowledged": "0",
                       "ns": "461809482",
                       "name": "Load average is too high (per CPU load over 1.5 for 5m)",
                       "severity": "0",
                       "r_eventid": "0",
                       "c_eventid": "0",
                       "correlationid": "0",
                       "userid": "0",
                       "cause_eventid": "0",
                       "acknowledges": [],
                       "opdata": "Load averages(1m 5m 15m): (1.6328 3.0522 2.2515), # of CPUs: 2",
                       "suppression_data": [],
                       "suppressed": "0",
                       "tags": [
                           {
                               "tag": "scope",
                               "value": "capacity"
                           },
                           {
                               "tag": "scope",
                               "value": "performance"
                           },
                           {
                               "tag": "component",
                               "value": "cpu"
                           },
                           {
                               "tag": "class",
                               "value": "os"
                           },
                           {
                               "tag": "target",
                               "value": "linux"
                           }
                       ],
                       "urls": []
                   },
                   {
                       "eventid": "4",
                       "source": "0",
                       "object": "0",
                       "objectid": "22395",
                       "clock": "1728657737",
                       "value": "1",
                       "acknowledged": "1",
                       "ns": "460759366",
                       "name": "Load average is too high (per CPU load over 1.5 for 5m)",
                       "severity": "3",
                       "r_eventid": "20",
                       "c_eventid": "0",
                       "correlationid": "0",
                       "userid": "0",
                       "cause_eventid": "0",
                       "acknowledges": [
                           {
                               "acknowledgeid": "1",
                               "userid": "1",
                               "clock": "1728657938",
                               "message": "Testing environment. Please disregard this alert.",
                               "action": "38",
                               "old_severity": "0",
                               "new_severity": "0",
                               "suppress_until": "1728744338",
                               "taskid": "0",
                               "username": "Admin",
                               "name": "Zabbix",
                               "surname": "Administrator"
                           }
                       ],
                       "opdata": "Load averages(1m 5m 15m): (1.6328 3.0522 2.2515), # of CPUs: 2",
                       "suppression_data": [
                           {
                               "maintenanceid": "0",
                               "suppress_until": "1728744338",
                               "userid": "1"
                           }
                       ],
                       "suppressed": "1",
                       "tags": [
                           {
                               "tag": "scope",
                               "value": "capacity"
                           },
                           {
                               "tag": "scope",
                               "value": "performance"
                           },
                           {
                               "tag": "component",
                               "value": "cpu"
                           },
                           {
                               "tag": "class",
                               "value": "os"
                           },
                           {
                               "tag": "target",
                               "value": "linux"
                           }
                       ],
                       "urls": []
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

#### Retrieving events by time period

Retrieve all events that have been created between October 17 and 18, 2012, in reverse chronological order.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "event.get",
               "params": {
                   "output": "extend",
                   "time_from": "1350432000",
                   "time_till": "1350518400",
                   "sortfield": ["clock", "eventid"],
                   "sortorder": "DESC"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "eventid": "20617",
                       "source": "0",
                       "object": "0",
                       "objectid": "14282",
                       "clock": "1350477816",
                       "value": "1",
                       "acknowledged": "0",
                       "ns": "0",
                       "name": "Less than 25% free in the history cache",
                       "severity": "3",
                       "r_eventid": "0",
                       "c_eventid": "0",
                       "correlationid": "0",
                       "userid": "0",
                       "cause_eventid": "0",
                       "opdata": "",
                       "suppressed": "0",
                       "urls": []
                   },
                   {
                       "eventid": "20616",
                       "source": "0",
                       "object": "0",
                       "objectid": "14281",
                       "clock": "1350477814",
                       "value": "0",
                       "acknowledged": "0",
                       "ns": "0",
                       "name": "Zabbix trapper processes more than 75% busy",
                       "severity": "0",
                       "r_eventid": "0",
                       "c_eventid": "0",
                       "correlationid": "0",
                       "userid": "0",
                       "cause_eventid": "0",
                       "opdata": "",
                       "suppressed": "0",
                       "urls": []
                   },
                   {
                       "eventid": "20615",
                       "source": "0",
                       "object": "0",
                       "objectid": "14281",
                       "clock": "1350477541",
                       "value": "1",
                       "acknowledged": "0",
                       "ns": "0",
                       "name": "Zabbix trapper processes more than 75% busy",
                       "severity": "3",
                       "r_eventid": "20616",
                       "c_eventid": "0",
                       "correlationid": "0",
                       "userid": "0",
                       "cause_eventid": "0",
                       "opdata": "",
                       "suppressed": "0",
                       "urls": []
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

#### Retrieving events acknowledged by specified user

Retrieving events acknowledged by user with ID=10

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "event.get",
               "params": {
                   "output": "extend",
                   "action": 2,
                   "action_userids": [10],
                   "selectAcknowledges": ["userid", "action"],
                   "sortfield": ["eventid"],
                   "sortorder": "DESC"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "eventid": "503",
                       "source": "0",
                       "object": "0",
                       "objectid": "23162",
                       "clock": "1747212236",
                       "value": "1",
                       "acknowledged": "1",
                       "ns": "413470863",
                       "name": "Number of installed packages has been changed",
                       "severity": "2",
                       "r_eventid": "0",
                       "c_eventid": "0",
                       "correlationid": "0",
                       "userid": "0",
                       "cause_eventid": "0",
                       "acknowledges": [
                           {
                               "userid": "10",
                               "action": "2"
                           }
                       ],
                       "opdata": "",
                       "suppressed": "0",
                       "urls": []
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

#### Retrieving top triggers with problem event count

Retrieve the top 5 triggers that have severities "Warning", "Average", "High", or "Disaster", together with the number of problem events within a specified time period.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "event.get",
               "params": {
                   "countOutput": true,
                   "groupBy": "objectid",
                   "source": 0,
                   "object": 0,
                   "value": 1,
                   "time_from": 1672531200,
                   "time_till": 1677628800,
                   "trigger_severities": [2, 3, 4, 5],
                   "sortfield": ["rowscount"],
                   "sortorder": "DESC",
                   "limit": 5
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "objectid": "232124",
                       "rowscount": "27"
                   },
                   {
                       "objectid": "29055",
                       "rowscount": "23"
                   },
                   {
                       "objectid": "253731",
                       "rowscount": "18"
                   },
                   {
                       "objectid": "254062",
                       "rowscount": "11"
                   },
                   {
                       "objectid": "23216",
                       "rowscount": "7"
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Alert](/documentation/current/en/manual/api/reference/alert/object#alert)
  * [Item](/documentation/current/en/manual/api/reference/item/object#item)
  * [Host](/documentation/current/en/manual/api/reference/host/object#host)
  * [LLD rule](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule)
  * [Service](/documentation/current/en/manual/api/reference/service/object#service)
  * [Trigger](/documentation/current/en/manual/api/reference/trigger/object#trigger)

### Source

CEvent::get() in _ui/include/classes/api/services/CEvent.php_.