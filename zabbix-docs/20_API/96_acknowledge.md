---
title: event.acknowledge
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/event/acknowledge
downloaded: 2025-11-14 10:41:30
---

# event.acknowledge

### Description

`object event.acknowledge(object/array parameters)`

This method allows to update events. The following update actions can be performed:

  * Close event. If event is already resolved, this action will be skipped.
  * Acknowledge event. If event is already acknowledged, this action will be skipped.
  * Unacknowledge event. If event is not acknowledged, this action will be skipped.
  * Add message.
  * Change event severity. If event already has same severity, this action will be skipped.
  * Suppress event. If event is already suppressed, this action will be skipped.
  * Unsuppress event. If event is not suppressed, this action will be skipped.

Only trigger events can be updated.  
Only problem events can be updated.  
Read/Write rights for trigger are required to close the event or to change event's severity.  
To close an event, manual close should be allowed in the trigger.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Parameters containing the IDs of the events and update operations that should be performed.

eventids | ID/array | IDs of the [events](/documentation/current/en/manual/api/reference/event/object#event) to acknowledge.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
action | integer | Event update action(s).  
  
Possible bitmap values:  
1 - close problem;  
2 - acknowledge event;  
4 - add message;  
8 - change severity;  
16 - unacknowledge event;  
32 - suppress event;  
64 - unsuppress event;  
128 - change event rank to cause;  
256 - change event rank to symptom.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 34 for acknowledge and suppress event).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
cause_eventid | ID | Cause event ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `action` contains the "change event rank to symptom" bit  
message | string | Text of the message.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `action` contains the "add message" bit  
severity | integer | New severity for events.  
  
Possible values:  
0 - not classified;  
1 - information;  
2 - warning;  
3 - average;  
4 - high;  
5 - disaster.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `action` contains the "change severity" bit  
suppress_until | integer | Unix timestamp until which event must be suppressed.  
  
If set to "0", the suppression will be indefinite.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `action` contains the "suppress event" bit  
  
### Return values

`(object)` Returns an object containing the IDs of the updated events under the `eventids` property.

### Examples

#### Acknowledging an event

Acknowledge a single event and leave a message.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "event.acknowledge",
               "params": {
                   "eventids": "20427",
                   "action": 6,
                   "message": "Problem resolved."
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "eventids": [
                       "20427"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Changing event's severity

Change severity for multiple events and leave a message.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "event.acknowledge",
               "params": {
                   "eventids": ["20427", "20428"],
                   "action": 12,
                   "message": "Maintenance required to fix it.",
                   "severity": 4
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "eventids": [
                       "20427",
                       "20428"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CEvent::acknowledge() in _ui/include/classes/api/services/CEvent.php_.