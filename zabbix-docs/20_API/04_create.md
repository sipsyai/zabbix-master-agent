---
title: action.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/action/create
downloaded: 2025-11-14 10:39:58
---

# action.create  
  
### Description

`object action.create(object/array actions)`

This method allows to create new actions.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Actions to create.

Additionally to the [standard action properties](object#action), the method accepts the following parameters.

filter | object | [Action filter](/documentation/current/en/manual/api/reference/action/object#action-filter) object for the action.  
---|---|---  
operations | array | [Action operations](/documentation/current/en/manual/api/reference/action/object#action-operation) to create for the action.  
recovery_operations | array | [Action recovery operations](/documentation/current/en/manual/api/reference/action/object#action-recovery-operation) to create for the action.  
update_operations | array | [Action update operations](/documentation/current/en/manual/api/reference/action/object#action-update-operation) to create for the action.  
  
### Return values

`(object)` Returns an object containing the IDs of the created actions under the `actionids` property. The order of the returned IDs matches the order of the passed actions.

### Examples

#### Create a trigger action

Create a trigger action that will begin once a trigger (with the word "memory" in its name) from host "10084" goes into a PROBLEM state. The action will have 4 configured operations. The first and immediate operation will send a message to all users in user group "7" via media type "1". If the event is not resolved in 30 minutes, the second operation will run [script](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts#configuring-a-global-script) "5" (script with scope "Action operation") on all hosts in group "2". If the event is resolved, a recovery operation will notify all users who received any messages regarding the problem. If the event is updated, an acknowledge/update operation will notify (with a custom subject and message) all users who received any messages regarding the problem.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.create",
               "params": {
                   "name": "Trigger action",
                   "eventsource": 0,
                   "esc_period": "30m",
                   "filter": {
                       "evaltype": 0,
                       "conditions": [
                           {
                               "conditiontype": 1,
                               "operator": 0,
                               "value": "10084"
                           },
                           {
                               "conditiontype": 3,
                               "operator": 2,
                               "value": "memory"
                           }
                       ]
                   },
                   "operations": [
                       {
                           "operationtype": 0,
                           "esc_step_from": 1,
                           "esc_step_to": 1,
                           "opmessage_grp": [
                               {
                                   "usrgrpid": "7"
                               }
                           ],
                           "opmessage": {
                               "default_msg": 1,
                               "mediatypeid": "1"
                           }
                       },
                       {
                           "operationtype": 1,
                           "esc_step_from": 2,
                           "esc_step_to": 2,
                           "opconditions": [
                               {
                                   "conditiontype": 14,
                                   "operator": 0,
                                   "value": "0"
                               }
                           ],
                           "opcommand_grp": [
                               {
                                   "groupid": "2"
                               }
                           ],
                           "opcommand": {
                               "scriptid": "5"
                           }
                       }
                   ],
                   "recovery_operations": [
                       {
                           "operationtype": "11",
                           "opmessage": {
                               "default_msg": 1
                           }
                       }
                   ],
                   "update_operations": [
                       {
                           "operationtype": "12",
                           "opmessage": {
                               "default_msg": 0,
                               "message": "Custom update operation message body",
                               "subject": "Custom update operation message subject"
                           }
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       "17"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create a discovery action

Create a discovery action that will link template "10001" to discovered hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.create",
               "params": {
                   "name": "Discovery action",
                   "eventsource": 1,
                   "filter": {
                       "evaltype": 0,
                       "conditions": [
                           {
                               "conditiontype": 21,
                               "operator": 0,
                               "value": "1"
                           },
                           {
                               "conditiontype": 10,
                               "operator": 0,
                               "value": "2"
                           }
                       ]
                   },
                   "operations": [
                       {
                           "operationtype": 6,
                           "optemplate": [
                               {
                                   "templateid": "10001"
                               }
                           ]
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       "18"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Using a custom expression filter

Create a trigger action that uses a custom expression - "A and (B or C)" - for evaluating action conditions. Once a trigger with a severity higher or equal to "Warning" from host "10084" or host "10106" goes into a PROBLEM state, the action will send a message to all users in user group "7" via media type "1". The formula IDs "A", "B" and "C" have been chosen arbitrarily.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.create",
               "params": {
                   "name": "Trigger action",
                   "eventsource": 0,
                   "esc_period": "15m",
                   "filter": {
                       "evaltype": 3,
                       "formula": "A and (B or C)",
                       "conditions": [
                           {
                               "conditiontype": 4,
                               "operator": 5,
                               "value": "2",
                               "formulaid": "A"
                           },
                           {
                               "conditiontype": 1,
                               "operator": 0,
                               "value": "10084",
                               "formulaid": "B"
                           },
                           {
                               "conditiontype": 1,
                               "operator": 0,
                               "value": "10106",
                               "formulaid": "C"
                           }
                       ]
                   },
                   "operations": [
                       {
                           "operationtype": 0,
                           "esc_step_from": 1,
                           "esc_step_to": 1,
                           "opmessage_grp": [
                               {
                                   "usrgrpid": "7"
                               }
                           ],
                           "opmessage": {
                               "default_msg": 1,
                               "mediatypeid": "1"
                           }
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       "18"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create agent autoregistration rule

Create an autoregistration action that adds a host to host group "2" when the host name contains "SRV" or metadata contains "AlmaLinux".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.create",
               "params": {
                   "name": "Register Linux servers",
                   "eventsource": "2",
                   "filter": {
                       "evaltype": "2",
                       "conditions": [
                           {
                               "conditiontype": "22",
                               "operator": "2",
                               "value": "SRV"
                           },
                           {
                               "conditiontype": "24",
                               "operator": "2",
                               "value": "AlmaLinux"
                           }
                       ]
                   },
                   "operations": [
                       {
                           "operationtype": "4",
                           "opgroup": [
                               {
                                   "groupid": "2"
                               }
                           ]
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       19
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create agent autoregistration rule with host tags

Create an autoregistration action that adds a host to host group "2" and adds two host tags.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.create",
               "params": {
                   "name": "Register Linux servers with tags",
                   "eventsource": "2",
                   "operations": [
                       {
                           "operationtype": "4",
                           "opgroup": [
                               {
                                   "groupid": "2"
                               }
                           ]
                       },
                       {
                           "operationtype": "13",
                           "optag": [
                               {
                                   "tag": "location",
                                   "value": "office"
                               },
                               {
                                   "tag": "city",
                                   "value": "Riga"
                               }
                           ]
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "actionids": [
                       20
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Action filter](object#action-filter)
  * [Action operation](object#action-operation)
  * [Script](/documentation/current/en/manual/api/reference/script/object)

### Source

CAction::create() in _ui/include/classes/api/services/CAction.php_.