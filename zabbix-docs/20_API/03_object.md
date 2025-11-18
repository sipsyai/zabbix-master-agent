---
title: Action object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/action/object
downloaded: 2025-11-14 10:39:57
---

# Action object

The following objects are directly related to the `action` API.

### Action

The action object has the following properties.

actionid | ID | ID of the action.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
esc_period | string | Default operation step duration. Must be at least 60 seconds. Accepts seconds, time unit with suffix, or a user macro.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` is set to "event created by a trigger", "internal event", or "event created on service status update"  
eventsource | integer | Type of events that the action will handle.  
  
Refer to the [event `source` property](/documentation/current/en/manual/api/reference/event/object#event) for a list of supported event types.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
name | string | Name of the action.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
status | integer | Whether the action is enabled or disabled.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
pause_symptoms | integer | Whether to pause escalation if event is a symptom event.  
  
Possible values:  
0 - Don't pause escalation for symptom problems;  
1 - _(default)_ Pause escalation for symptom problems.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` is set to "event created by a trigger"  
pause_suppressed | integer | Whether to pause escalation during maintenance periods or not.  
  
Possible values:  
0 - Don't pause escalation;  
1 - _(default)_ Pause escalation.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` is set to "event created by a trigger"  
notify_if_canceled | integer | Whether to notify when escalation is canceled.  
  
Possible values:  
0 - Don't notify when escalation is canceled;  
1 - _(default)_ Notify when escalation is canceled.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` is set to "event created by a trigger"  
  
### Action operation

The action operation object defines an operation that will be performed when an action is executed. It has the following properties.

operationtype | integer | Type of operation.  
  
Possible values:  
0 - send message;  
1 - global script;  
2 - add host;  
3 - remove host;  
4 - add to host group;  
5 - remove from host group;  
6 - link template;  
7 - unlink template;  
8 - enable host;  
9 - disable host;  
10 - set host inventory mode;  
13 - add host tags;  
14 - remove host tags.  
  
Possible values if `eventsource` of Action object is set to "event created by a trigger" or "event created on service status update":  
0 - "send message";  
1 - "global script".  
  
Possible values if `eventsource` of Action object is set to "internal event":  
0 - "send message".  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
esc_period | string | Duration of an escalation step in seconds. Must be greater than 60 seconds. Accepts seconds, time unit with suffix, or a user macro. If set to 0 or 0s, the default action escalation period will be used.  
  
Default: 0s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` of Action object is set to "event created by a trigger", "internal event", or "event created on service status update"  
esc_step_from | integer | Step to start escalation from.  
  
Default: 1.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` of Action object is set to "event created by a trigger", "internal event", or "event created on service status update"  
esc_step_to | integer | Step to end escalation at.  
  
Default: 1.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `eventsource` of Action object is set to "event created by a trigger", "internal event", or "event created on service status update"  
evaltype | integer | Operation condition [evaluation method](/documentation/current/en/manual/config/notifications/action/conditions#type-of-calculation).  
  
Possible values:  
0 - _(default)_ And/Or;  
1 - And;  
2 - Or.  
opcommand | object | Global script to execute.  
  
The global script must have the `scriptid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "global script"  
opcommand_grp | array | Host groups to run global scripts on.  
  
The host groups must have the `groupid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "global script" and `opcommand_hst` is not set  
opcommand_hst | array | Host to run global scripts on.  
  
The hosts must have the `hostid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "global script" and `opcommand_grp` is not set  
opconditions | array | Operation conditions used for trigger actions.  
  
The operation condition object is [described in detail below](/documentation/current/en/manual/api/reference/action/object#action-operation-condition).  
opgroup | array | Host groups to add hosts to.  
  
The host groups must have the `groupid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "add to host group" or "remove from host group"  
opmessage | object | Object containing the data about the message sent by the operation.  
  
The operation message object is [described in detail below](/documentation/current/en/manual/api/reference/action/object#action-operation-message).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message"  
opmessage_grp | array | User groups to send messages to.  
  
The user groups must have the `usrgrpid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message" and `opmessage_usr` is not set  
opmessage_usr | array | Users to send messages to.  
  
The users must have the `userid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message" and `opmessage_grp` is not set  
optemplate | array | Templates to link to the hosts.  
  
The templates must have the `templateid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "link template" or "unlink template"  
opinventory | object | Inventory mode set host to.  
  
The inventory must have the `inventory_mode` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "set host inventory mode"  
optag | array | Host tags to add or remove.  
  
Tags must have `tag` property defined.  
The `value` property is optional.   
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `operationtype` is set to "add host tags" or "remove host tags".  
  
#### Action operation message

The operation message object contains data about the message that will be sent by the operation. It has the following properties.

default_msg | integer | Whether to use the default action message text and subject.  
  
Possible values:  
0 - use the data from the operation;  
1 - _(default)_ use the data from the media type.  
---|---|---  
mediatypeid | ID | ID of the media type that will be used to send the message.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `operationtype` of Action operation object, Action recovery operation object, or Action update operation object is set to "send message", or if `operationtype` of Action update operation object is set to "notify all involved"  
message | string | Operation message text.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `default_msg` is set to "use the data from the operation"  
subject | string | Operation message subject.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `default_msg` is set to "use the data from the operation"  
  
#### Action operation condition

The action operation condition object defines a condition that must be met to perform the current operation. It has the following properties.

conditiontype | integer | Type of condition.  
  
Possible values:  
14 - event acknowledged.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Value to compare with.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
operator | integer | Condition operator.  
  
Possible values:  
0 - _(default)_ =  
  
The following operators and values are supported for each operation condition type.

14 | Event acknowledged | = | Whether the event is acknowledged.  
  
Possible values:  
0 - not acknowledged;  
1 - acknowledged.  
---|---|---|---  
  
### Action recovery operation

The action recovery operation object defines an operation that will be performed when a problem is resolved. Recovery operations are possible **only** for trigger, internal and service actions. It has the following properties.

operationtype | integer | Type of operation.  
  
Possible values if `eventsource` of Action object is set to "event created by a trigger" or "event created on service status update":  
0 - send message;  
1 - global script;  
11 - notify all involved.  
  
Possible values if `eventsource` of Action object is set to "internal event":  
0 - send message;  
11 - notify all involved.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
opcommand | object | Global script to execute.  
  
The global script must have the `scriptid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "global script"  
opcommand_grp | array | Host groups to run global scripts on.  
  
The host groups must have the `groupid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `eventsource` of Action object is set to "event created by a trigger", and `operationtype` is set to "global script", and `opcommand_hst` is not set  
opcommand_hst | array | Host to run global scripts on.  
  
The hosts must have the `hostid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `eventsource` of Action object is set to "event created by a trigger", and `operationtype` is set to "global script", and `opcommand_grp` is not set  
opmessage | object | Object containing the data about the message sent by the recovery operation.  
  
The operation message object is [described in detail above](/documentation/current/en/manual/api/reference/action/object#action-operation-message).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message"  
opmessage_grp | array | User groups to send messages to.  
  
The user groups must have the `usrgrpid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message" and `opmessage_usr` is not set  
opmessage_usr | array | Users to send messages to.  
  
The users must have the `userid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message" and `opmessage_grp` is not set  
  
### Action update operation

The action update operation object defines an operation that will be performed when a problem is updated (commented upon, acknowledged, severity changed, or manually closed). Update operations are possible **only** for trigger and service actions. It has the following properties.

operationtype | integer | Type of operation.  
  
Possible values:  
0 - send message;  
1 - global script;  
12 - notify all involved.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
opcommand | object | Global script to execute.  
  
The global script must have the `scriptid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "global script"  
opcommand_grp | array | Host groups to run global scripts on.  
  
The host groups must have the `groupid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `eventsource` of Action object is set to "event created by a trigger", and `operationtype` is set to "global script", and `opcommand_hst` is not set  
opcommand_hst | array | Host to run global scripts on.  
  
The hosts must have the `hostid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `eventsource` of Action object is set to "event created by a trigger", and `operationtype` is set to "global script", and `opcommand_grp` is not set  
opmessage | object | Object containing the data about the message sent by the update operation.  
  
The operation message object is [described in detail above](/documentation/current/en/manual/api/reference/action/object#action-operation-message).  
opmessage_grp | array | User groups to send messages to.  
  
The user groups must have the `usrgrpid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message" and `opmessage_usr` is not set  
opmessage_usr | array | Users to send messages to.  
  
The users must have the `userid` property defined.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `operationtype` is set to "send message" and `opmessage_grp` is not set  
  
### Action filter

The action filter object defines a set of conditions that must be met to perform the configured action operations. It has the following properties.

conditions | array | Set of filter conditions to use for filtering results. The conditions will be sorted in the order of their placement in the formula.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
evaltype | integer | Filter condition [evaluation method](/documentation/current/en/manual/config/notifications/action/conditions#type-of-calculation).  
  
Possible values:  
0 - And/Or;  
1 - And;  
2 - Or;  
3 - Custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
eval_formula | string | Generated expression that will be used for evaluating filter conditions. The expression contains IDs that reference specific filter conditions by its `formulaid`. The value of `eval_formula` is equal to the value of `formula` for filters with a custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
formula | string | User-defined expression to be used for evaluating conditions of filters with a custom expression. The expression must contain IDs that reference specific filter conditions by its `formulaid`. The IDs used in the expression must exactly match the ones defined in the filter conditions: no condition can remain unused or omitted.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `evaltype` is set to "custom expression"  
  
#### Action filter condition

The action filter condition object defines a specific condition that must be checked before running the action operations.

conditiontype | integer | Type of condition.  
  
Possible values if `eventsource` of Action object is set to "event created by a trigger":  
0 - host group;  
1 - host;  
2 - trigger;  
3 - event name;  
4 - trigger severity;  
6 - time period;  
13 - host template;  
16 - problem is suppressed;  
25 - event tag;  
26 - event tag value.  
  
Possible values if `eventsource` of Action object is set to "event created by a discovery rule":  
7 - host IP;  
8 - discovered service type;  
9 - discovered service port;  
10 - discovery status;  
11 - uptime or downtime duration;  
12 - received value;  
18 - discovery rule;  
19 - discovery check;  
20 - proxy;  
21 - discovery object.  
  
Possible values if `eventsource` of Action object is set to "event created by active agent autoregistration":  
20 - proxy;  
22 - host name;  
24 - host metadata.  
  
Possible values if `eventsource` of Action object is set to "internal event":  
0 - host group;  
1 - host;  
13 - host template;  
23 - event type;  
25 - event tag;  
26 - event tag value.  
  
Possible values if `eventsource` of Action object is set to "event created on service status update":  
25 - event tag;  
26 - event tag value;  
27 - service;  
28 - service name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Value to compare with.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
value2 | string | Secondary value to compare with.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `eventsource` of Action object is set to "event created by a trigger", `conditiontype` is set to any possible value for trigger actions, and the type of condition (see below) is "26"  
\- _required_ if `eventsource` of Action object is set to "internal event", `conditiontype` is set to any possible value for internal actions, and the type of condition (see below) is "26"  
\- _required_ if `eventsource` of Action object is set to "event created on service status update", `conditiontype` is set to any possible value for service actions, and the type of condition (see below) is "26"  
formulaid | string | Arbitrary unique ID that is used to reference the condition from a custom expression. Can only contain capital-case letters. The ID must be defined by the user when modifying filter conditions, but will be generated anew when requesting them afterward.  
operator | integer | Condition [operator](/documentation/current/en/manual/config/notifications/action/conditions).  
  
Possible values:  
0 - _(default)_ equals;  
1 - does not equal;  
2 - contains;  
3 - does not contain;  
4 - in;  
5 - is greater than or equals;  
6 - is less than or equals;  
7 - not in;  
8 - matches;  
9 - does not match;  
10 - Yes;  
11 - No.  
  
To better understand how to use filters with various types of expressions, see examples on the [action.get](get#retrieve-discovery-actions) and [action.create](create#using-a-custom-expression-filter) method pages.

The following operators and values are supported for each condition type.

0 | Host group | equals,  
does not equal | Host group ID.  
---|---|---|---  
1 | Host | equals,  
does not equal | Host ID.  
2 | Trigger | equals,  
does not equal | Trigger ID.  
3 | Event name | contains,  
does not contain | Event name.  
4 | Trigger severity | equals,  
does not equal,  
is greater than or equals,  
is less than or equals | Trigger severity. Refer to the [trigger `severity` property](/documentation/current/en/manual/api/reference/trigger/object#trigger) for a list of supported trigger severities.  
5 | Trigger value | equals | Trigger value. Refer to the [trigger `value` property](/documentation/current/en/manual/api/reference/trigger/object#trigger) for a list of supported trigger values.  
6 | Time period | in, not in | Time when the event was triggered as a [time period](/documentation/current/en/manual/appendix/time_period).  
7 | Host IP | equals,  
does not equal | One or several IP ranges to check, separated by commas. Refer to the [network discovery configuration](/documentation/current/en/manual/discovery/network_discovery/rule) section for more information on supported formats of IP ranges.  
8 | Discovered service type | equals,  
does not equal | Type of discovered service. The type of service matches the type of the discovery check used to detect the service. Refer to the [discovery check `type` property](/documentation/current/en/manual/api/reference/dcheck/object#discovery-check) for a list of supported types.  
9 | Discovered service port | equals,  
does not equal | One or several port ranges, separated by commas.  
10 | Discovery status | equals | Status of a discovered object.  
  
Possible values:  
0 - host or service up;  
1 - host or service down;  
2 - host or service discovered;  
3 - host or service lost.  
11 | Uptime or downtime duration | is greater than or equals,  
is less than or equals | Time indicating how long has the discovered object been in the current status in seconds.  
12 | Received values | equals,  
does not equal,  
is greater than or equals,  
is less than or equals,  
contains,  
does not contain | Value returned when performing a Zabbix agent, SNMPv1, SNMPv2 or SNMPv3 discovery check.  
13 | Host template | equals,  
does not equal | Linked template ID.  
16 | Problem is suppressed | Yes, No | No value required: using the "Yes" operator means that problem must be suppressed, "No" - not suppressed.  
18 | Discovery rule | equals,  
does not equal | ID of the discovery rule.  
19 | Discovery check | equals,  
does not equal | ID of the discovery check.  
20 | Proxy | equals,  
does not equal | ID of the proxy.  
21 | Discovery object | equals | Type of object that triggered the discovery event.  
  
Possible values:  
1 - discovered host;  
2 - discovered service.  
22 | Host name | contains,  
does not contain,  
matches,  
does not match | Host name.  
Using a regular expression is supported for operators _matches_ and _does not match_ in autoregistration conditions.  
23 | Event type | equals | Specific internal event.  
  
Possible values:  
0 - item in "not supported" state;  
1 - item in "normal" state;  
2 - LLD rule in "not supported" state;  
3 - LLD rule in "normal" state;  
4 - trigger in "unknown" state;  
5 - trigger in "normal" state.  
24 | Host metadata | contains,  
does not contain,  
matches,  
does not match | Metadata of the auto-registered host.  
Using a regular expression is supported for operators _matches_ and _does not match_.  
25 | Tag | equals,  
does not equal,  
contains,  
does not contain | Event tag.  
26 | Tag value | equals,  
does not equal,  
contains,  
does not contain | Event tag value.  
27 | Service | equals,  
does not equal | Service ID.  
28 | Service name | equals,  
does not equal | Service name.