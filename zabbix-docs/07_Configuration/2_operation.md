---
title: Operations
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/action/operation
downloaded: 2025-11-14 10:36:20
---

# 2 Operations

#### Overview

You can define the following operations for all events:

  * Send a message
  * Execute a remote command

Zabbix server does not create alerts if access to the host is explicitly "denied" for the user defined as action operation recipient or if the user has no rights defined to the host at all.

For discovery and autoregistration events, additional operations are available:

  * [Add host](/documentation/current/en/manual/config/notifications/action/operation/other#adding-host)
  * Remove host
  * Enable host
  * Disable host
  * Add to host group
  * Remove from host group
  * Add host tags
  * Remove host tags
  * Link template
  * Unlink template
  * Set host inventory mode

#### Configuring an operation

To configure an operation, go to the _Operations_ tab in [action](/documentation/current/en/manual/config/notifications/action) configuration.

![](/documentation/current/assets/en/manual/config/notifications/action_operation2.png)

General operation attributes:

_Default operation step duration_ | Duration of one operation step by default (60 seconds to 1 week).  
For example, an hour-long step duration means that if an operation is carried out, an hour will pass before the next step.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 60s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
---|---  
_Operations_ | Action operations (if any) are displayed, with these details:  
**Steps** \- escalation step(s) to which the operation is assigned.  
**Details** \- type of operation and its recipient/target.  
The operation list also displays the media type (email, SMS or script) used as well as the name and surname (in parentheses after the username) of a notification recipient.  
**Start in** \- how long after an event the operation is performed.  
**Duration (sec)** \- step duration is displayed. _Default_ is displayed if the step uses default duration, and a time is displayed if custom duration is used.  
**Actions** \- links for editing and removing an operation are displayed.  
_Recovery operations_ | Action operations (if any) are displayed, with these details:  
**Details** \- type of operation and its recipient/target.  
The operation list also displays the media type (email, SMS or script) used as well as the name and surname (in parentheses after the username) of a notification recipient.  
**Actions** \- links for editing and removing an operation are displayed.  
_Update operations_ | Action operations (if any) are displayed, with these details:  
**Details** \- type of operation and its recipient/target.  
The operation list also displays the media type (email, SMS or script) used as well as the name and surname (in parentheses after the username) of a notification recipient.  
**Actions** \- links for editing and removing an operation are displayed.  
_Pause operations for symptom problems_ | Mark this checkbox to pause operations (after the first operation) for symptom problems.  
Note that this setting affects only problem escalations; recovery and update operations will not be affected.  
This option is available for _Trigger actions_ only.  
_Pause operations for suppressed problems_ | Mark this checkbox to delay the start of operations for the duration of a maintenance period. When operations are started, after the maintenance, all operations are performed including those for the events during the maintenance.  
Note that this setting affects only problem escalations; recovery and update operations will not be affected.  
If you unmark this checkbox, operations will be executed without delay even during a maintenance period.  
This option is not available for _Service actions_.  
_Notify about canceled escalations_ | Unmark this checkbox to disable notifications about canceled escalations (when host, item, trigger or action is disabled).  
  
All mandatory input fields are marked with a red asterisk.

To configure details of a new operation, click on ![](/documentation/current/assets/en/manual/config/add_link.png) in the _Operations_ block. To edit an existing operation, click on ![](/documentation/current/assets/en/manual/config/edit_link.png) next to the operation. A pop-up window will open where you can edit the operation step details.

#### Operation details

![](/documentation/current/assets/en/manual/config/operation_details.png)

_Operation_ | Select the operation:  
**Send message** \- send message to user.  
**< remote command name>** \- execute a remote command. Commands are available for execution if previously defined in [global scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts#configuring-a-global-script) with _Action operation_ selected as its scope.  
More operations are available for discovery and autoregistration based events (see above).  
---|---  
_Steps_ | Select the step(s) to assign the operation to in an [escalation](escalations) schedule:  
**From** \- execute starting with this step.  
**To** \- execute until this step (0=infinity, execution will not be limited).  
_Step duration_ | Custom duration for these steps (0=use default step duration).  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 60s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
Several operations can be assigned to the same step. If these operations have different step duration defined, the shortest one is taken into account and applied to the step.  
Operation type: [send message](/documentation/current/en/manual/config/notifications/action/operation/message)  
| _Send to user groups_ | Select user groups to send the message to.  
The user group must have at least "read" [permissions](/documentation/current/en/manual/config/users_and_usergroups/permissions) to the host in order to be notified.  
_Send to users_ | Select users to send the message to.  
The user must have at least "read" [permissions](/documentation/current/en/manual/config/users_and_usergroups/permissions) to the host in order to be notified.  
_Send to media type_ | Send message to all available (configured and enabled) media types or a specific one only.  
_Custom message_ | If selected, the custom message can be configured.  
For notifications about internal events via [webhooks](/documentation/current/en/manual/config/notifications/media/webhook), custom message is mandatory.  
| _Subject_ | Subject of the custom message. The subject may contain macros. It is limited to 255 characters.  
_Message_ | The custom message. The message may contain macros. It is limited to certain amount of characters depending on the type of database (see [Sending message](/documentation/current/en/manual/config/notifications/action/operation/message) for more information).  
Operation type: [remote command](/documentation/current/en/manual/config/notifications/action/operation/remote_command)  
| _Target list_ | Select targets to execute the command on:  
**Current host** \- command is executed on the host of the trigger that caused the problem event. This option will not work if there are multiple hosts in the trigger.  
**Host** \- select host(s) to execute the command on.  
**Host group** \- select host group(s) to execute the command on. Specifying a parent host group implicitly selects all nested host groups. Thus the remote command will also be executed on hosts from nested groups.  
A command on a host is executed only once, even if the host matches more than once (e.g. from several host groups; individually and from a host group).  
The target list is meaningless if a custom script is executed on Zabbix server. Selecting more targets in this case only results in the script being executed on the server more times.  
Note that for global scripts, the target selection also depends on the _Host group_ setting in global script [configuration](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts#configuring-a-global-script).  
_Target list_ option is not available for _Service actions_ because in this case remote commands are always executed on Zabbix server.  
_Conditions_ | Condition for performing the operation:  
**Event is not acknowledged** \- only when the event is unacknowledged.  
**Event is acknowledged** \- only when the event is acknowledged.  
_Conditions_ option is only available for _Trigger actions_.  
  
When done, click _Add_ to add the operation to the list of _Operations_.