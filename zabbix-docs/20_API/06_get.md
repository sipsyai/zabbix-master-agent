---
title: action.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/action/get
downloaded: 2025-11-14 10:40:00
---

# action.get

### Description

`integer/array action.get(object parameters)`

The method allows to retrieve actions according to the given parameters.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

actionids | ID/array | Return only actions with the given IDs.  
---|---|---  
groupids | ID/array | Return only actions that use the given host groups in action conditions.  
hostids | ID/array | Return only actions that use the given hosts in action conditions.  
triggerids | ID/array | Return only actions that use the given triggers in action conditions.  
mediatypeids | ID/array | Return only actions that use the given media types to send messages.  
usrgrpids | ID/array | Return only actions that are configured to send messages to the given user groups.  
userids | ID/array | Return only actions that are configured to send messages to the given users.  
scriptids | ID/array | Return only actions that are configured to run the given scripts.  
selectFilter | query | Return a [`filter`](/documentation/current/en/manual/api/reference/action/object#action-filter) property with the action condition filter.  
selectOperations | query | Return an [`operations`](/documentation/current/en/manual/api/reference/action/object#action-operation) property with action operations.  
selectRecoveryOperations | query | Return a [`recovery_operations`](/documentation/current/en/manual/api/reference/action/object#action-recovery-operation) property with action recovery operations.  
selectUpdateOperations | query | Return an [`update_operations`](/documentation/current/en/manual/api/reference/action/object#action-update-operation) property with action update operations.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `actionid`, `name`, `status`.  
countOutput | boolean | These parameters are described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
excludeSearch | boolean  
filter | object  
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
  * the count of retrieved objects, if the `countOutput` parameter has been used.

### Examples

#### Retrieve trigger actions

Retrieve all configured trigger actions together with action conditions and operations.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.get",
               "params": {
                   "output": "extend",
                   "selectOperations": "extend",
                   "selectRecoveryOperations": "extend",
                   "selectUpdateOperations": "extend",
                   "selectFilter": "extend",
                   "filter": {
                       "eventsource": 0
                   }
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
                       "actionid": "3",
                       "name": "Report problems to Zabbix administrators",
                       "eventsource": "0",
                       "status": "1",
                       "esc_period": "1h",
                       "pause_suppressed": "1",
                       "filter": {
                           "evaltype": "0",
                           "formula": "",
                           "conditions": [],
                           "eval_formula": ""
                       },
                       "operations": [
                           {
                               "operationid": "3",
                               "actionid": "3",
                               "operationtype": "0",
                               "esc_period": "0",
                               "esc_step_from": "1",
                               "esc_step_to": "1",
                               "evaltype": "0",
                               "opconditions": [],
                               "opmessage": [
                                   {
                                       "default_msg": "1",
                                       "subject": "",
                                       "message": "",
                                       "mediatypeid" => "0"
                                   }
                               ],
                               "opmessage_grp": [
                                   {
                                       "usrgrpid": "7"
                                   }
                               ]
                           }
                       ],
                       "recovery_operations": [
                           {
                               "operationid": "7",
                               "actionid": "3",
                               "operationtype": "11",
                               "evaltype": "0",
                               "opconditions": [],
                               "opmessage": {
                                   "default_msg": "0",
                                   "subject": "{TRIGGER.STATUS}: {TRIGGER.NAME}",
                                   "message": "Trigger: {TRIGGER.NAME}\r\nTrigger status: {TRIGGER.STATUS}\r\nTrigger severity: {TRIGGER.SEVERITY}\r\nTrigger URL: {TRIGGER.URL}\r\n\r\nItem values:\r\n\r\n1. {ITEM.NAME1} ({HOST.NAME1}:{ITEM.KEY1}): {ITEM.VALUE1}\r\n2. {ITEM.NAME2} ({HOST.NAME2}:{ITEM.KEY2}): {ITEM.VALUE2}\r\n3. {ITEM.NAME3} ({HOST.NAME3}:{ITEM.KEY3}): {ITEM.VALUE3}\r\n\r\nOriginal event ID: {EVENT.ID}",
                                   "mediatypeid": "0"
                               }
                           }
                       ],
                       "update_operations": [
                           {
                               "operationid": "31",
                               "operationtype": "12",
                               "evaltype": "0",
                               "opmessage": {
                                   "default_msg": "1",
                                   "subject": "",
                                   "message": "",
                                   "mediatypeid": "0"
                               }
                           },
                           {
                               "operationid": "32",
                               "operationtype": "0",
                               "evaltype": "0",
                               "opmessage": {
                                   "default_msg": "0",
                                   "subject": "Updated: {TRIGGER.NAME}",
                                   "message": "{USER.FULLNAME} updated problem at {EVENT.UPDATE.DATE} {EVENT.UPDATE.TIME} with the following message:\r\n{EVENT.UPDATE.MESSAGE}\r\n\r\nCurrent problem status is {EVENT.STATUS}",
                                   "mediatypeid": "1"
                               },
                               "opmessage_grp": [
                                   {
                                       "usrgrpid": "7"
                                   }
                               ],
                               "opmessage_usr": []
                           },
                           {
                               "operationid": "33",
                               "operationtype": "1",
                               "evaltype": "0",
                               "opcommand": {
                                   "scriptid": "3"
                               },
                               "opcommand_hst": [
                                   {
                                       "hostid": "10084"
                                   }
                               ],
                               "opcommand_grp": []
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

#### Retrieve discovery actions

Retrieve all configured discovery actions together with action conditions and operations. The filter uses the "and" evaluation type, so the `formula` property is empty and `eval_formula` is generated automatically.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "action.get",
               "params": {
                   "output": "extend",
                   "selectOperations": "extend",
                   "selectFilter": "extend",
                   "filter": {
                       "eventsource": 1
                   }
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
                       "actionid": "2",
                       "name": "Auto discovery. Linux servers.",
                       "eventsource": "1",
                       "status": "1",
                       "esc_period": "0s",
                       "pause_suppressed": "1",
                       "filter": {
                           "evaltype": "0",
                           "formula": "",
                           "conditions": [
                               {
                                   "conditiontype": "10",
                                   "operator": "0",
                                   "value": "0",
                                   "value2": "",
                                   "formulaid": "B"
                               },
                               {
                                   "conditiontype": "8",
                                   "operator": "0",
                                   "value": "9",
                                   "value2": "",
                                   "formulaid": "C"
                               },
                               {
                                   "conditiontype": "12",
                                   "operator": "2",
                                   "value": "Linux",
                                   "value2": "",
                                   "formulaid": "A"
                               }
                           ],
                           "eval_formula": "A and B and C"
                       },
                       "operations": [
                           {
                               "operationid": "1",
                               "actionid": "2",
                               "operationtype": "6",
                               "esc_period": "0s",
                               "esc_step_from": "1",
                               "esc_step_to": "1",
                               "evaltype": "0",
                               "opconditions": [],
                               "optemplate": [
                                   {
                                       "templateid": "10001"
                                   }
                               ]
                           },
                           {
                               "operationid": "2",
                               "actionid": "2",
                               "operationtype": "4",
                               "esc_period": "0s",
                               "esc_step_from": "1",
                               "esc_step_to": "1",
                               "evaltype": "0",
                               "opconditions": [],
                               "opgroup": [
                                   {
                                       "groupid": "2"
                                   }
                               ]
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Action filter](object#action-filter)
  * [Action operation](object#action-operation)

### Source

CAction::get() in _ui/include/classes/api/services/CAction.php_.