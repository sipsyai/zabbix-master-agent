---
title: Recovery operations
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/action/recovery_operations
downloaded: 2025-11-14 10:36:25
---

# 3 Recovery operations

### Overview

Recovery operations allow you to be notified when problems are resolved.

Both messages and remote commands are supported in recovery operations. While several operations can be added, escalation is not supported - all operations are assigned to a single step and therefore will be performed simultaneously.

### Use cases

Some use cases for recovery operations are as follows:

  1. Notify on a recovery all users that were notified on the problem: 
     * Select _Notify all involved_ as operation type.
  2. Have multiple operations upon recovery: send a notification and execute a remote command: 
     * Add operation types for sending a message and executing a command.
  3. Open a ticket in external helpdesk/ticketing system and close it when the problem is resolved: 
     * Create an external script that communicates with the helpdesk system.
     * Create an action having operation that executes this script and thus opens a ticket.
     * Have a recovery operation that executes this script with other parameters and closes the ticket.
     * Use the {EVENT.ID} macro to reference the original problem.

### Configuring a recovery operation

To configure a recovery operation, go to the _Operations_ tab in [action](/documentation/current/en/manual/config/notifications/action) configuration.

![](/documentation/current/assets/en/manual/config/notifications/action_operation.png)

To configure details of a new recovery operation, click on ![](/documentation/current/assets/en/manual/config/add_link.png) in the _Recovery operations_ block. To edit an existing operation, click on ![](/documentation/current/assets/en/manual/config/edit_link.png) next to the operation. A pop-up window will open where you can edit the operation step details.

#### Recovery operation details

![](/documentation/current/assets/en/manual/config/recovery_operation_details.png)

Three operation types are available for recovery events:

  * **Send message** \- send recovery message to specified user;
  * **Notify all involved** \- send recovery message to all users who were notified on the problem event;
  * **< remote command name>** \- execute a remote command. Commands are available for execution if previously defined in [global scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts#configuring-a-global-script) with _Action operation_ selected as its scope.

Parameters for each operation type are described below. All mandatory input fields are marked with a red asterisk. When done, click on _Add_ to add operation to the list of _Recovery operations_.

Note that if the same recipient is defined in several operation types without specified _Custom message_ , duplicate notifications are not sent.

#### Operation type: [send message](/documentation/current/en/manual/config/notifications/action/operation/message)

_Send to user groups_ | Select user groups to send the recovery message to.  
The user group must have at least "read" [permissions](/documentation/current/en/manual/config/users_and_usergroups/permissions) to the host in order to be notified.  
---|---  
_Send to users_ | Select users to send the recovery message to.  
The user must have at least "read" [permissions](/documentation/current/en/manual/config/users_and_usergroups/permissions) to the host in order to be notified.  
_Send to media type_ | Send default recovery message to all available (configured and enabled) media types or a specific one only.  
_Custom message_ | If selected, a custom message can be defined.  
| _Subject_ | Subject of the custom message. The subject may contain macros.  
_Message_ | The custom message. The message may contain macros.  
  
#### Operation type: [remote command](/documentation/current/en/manual/config/notifications/action/operation/remote_command)

_Target list_ | Select targets to execute the command on:  
**Current host** \- command is executed on the host of the trigger that caused the problem event. This option will not work if there are multiple hosts in the trigger.  
**Host** \- select host(s) to execute the command on.  
**Host group** \- select host group(s) to execute the command on. Specifying a parent host group implicitly selects all nested host groups. Thus the remote command will also be executed on hosts from nested groups.  
A command on a host is executed only once, even if the host matches more than once (e.g. from several host groups; individually and from a host group).  
The target list is meaningless if the command is executed on Zabbix server. Selecting more targets in this case only results in the command being executed on the server more times.  
Note that for global scripts, the target selection also depends on the _Host group_ setting in global script [configuration](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts#configuring-a-global-script).  
---|---  
  
#### Operation type: notify all involved

_Custom message_ | If selected, a custom message can be defined.  
---|---  
| _Subject_ | Subject of the custom message. The subject may contain macros.  
_Message_ | The custom message. The message may contain macros.