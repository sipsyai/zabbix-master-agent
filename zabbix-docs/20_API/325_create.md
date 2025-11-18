---
title: trigger.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/trigger/create
downloaded: 2025-11-14 10:45:18
---

# trigger.create  
  
### Description

`object trigger.create(object/array triggers)`

This method allows to create new triggers.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Triggers to create.

Additionally to the [standard trigger properties](object#trigger) the method accepts the following parameters.

dependencies | array | [Triggers](/documentation/current/en/manual/api/reference/trigger/object#trigger) that the trigger is dependent on.  
  
The triggers must have only the `triggerid` property defined.  
---|---|---  
tags | array | [Trigger tags](/documentation/current/en/manual/api/reference/trigger/object#trigger-tag).  
  
The trigger expression has to be given in its expanded form.

### Return values

`(object)` Returns an object containing the IDs of the created triggers under the `triggerids` property. The order of the returned IDs matches the order of the passed triggers.

### Examples

#### Creating a trigger

Create a trigger with a single trigger dependency.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "trigger.create",
               "params": [
                   {
                       "description": "Processor load is too high on {HOST.NAME}",
                       "expression": "last(/Linux server/system.cpu.load[percpu,avg1])>5",
                       "dependencies": [
                           {
                               "triggerid": "17367"
                           }
                       ]
                   },
                   {
                       "description": "Service status",
                       "expression": "length(last(/Linux server/log[/var/log/system,Service .* has stopped]))<>0",
                       "dependencies": [
                           {
                               "triggerid": "17368"
                           }
                       ],
                       "tags": [
                           {
                               "tag": "service",
                               "value": "{{ITEM.VALUE}.regsub(\"Service (.*) has stopped\", \"\\1\")}"
                           },
                           {
                               "tag": "error",
                               "value": ""
                           }
                       ]
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "triggerids": [
                       "17369",
                       "17370"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTrigger::create() in _ui/include/classes/api/services/CTrigger.php_.