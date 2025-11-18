---
title: trigger.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/trigger/update
downloaded: 2025-11-14 10:45:21
---

# trigger.update

### Description

`object trigger.update(object/array triggers)`

This method allows to update existing triggers.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Trigger properties to be updated.

The `triggerid` property must be defined for each trigger, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard trigger properties](object#trigger) the method accepts the following parameters.

dependencies | array | [Triggers](/documentation/current/en/manual/api/reference/trigger/object#trigger) that the trigger is dependent on.  
  
The triggers must have only the `triggerid` property defined.  
---|---|---  
tags | array | [Trigger tags](/documentation/current/en/manual/api/reference/trigger/object#trigger-tag).  
  
The trigger expression has to be given in its expanded form.

### Return values

`(object)` Returns an object containing the IDs of the updated triggers under the `triggerids` property.

### Examples

#### Enabling a trigger

Enable a trigger, that is, set its status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "trigger.update",
               "params": {
                   "triggerid": "13938",
                   "status": 0
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "triggerids": [
                       "13938"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Replacing triggers tags

Replace tags for trigger.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "trigger.update",
               "params": {
                   "triggerid": "13938",
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
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "triggerids": [
                       "13938"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Replacing dependencies

Replace dependencies for trigger.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "trigger.update",
               "params": {
                   "triggerid": "22713",
                   "dependencies": [
                       {
                           "triggerid": "22712"
                       },
                       {
                           "triggerid": "22772"
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
                   "triggerids": [
                       "22713"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTrigger::update() in _ui/include/classes/api/services/CTrigger.php_.