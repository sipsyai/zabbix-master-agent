---
title: triggerprototype.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/triggerprototype/create
downloaded: 2025-11-14 10:45:24
---

# triggerprototype.create  
  
### Description

`object triggerprototype.create(object/array triggerPrototypes)`

This method allows to create new trigger prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Trigger prototypes to create.

Additionally to the [standard trigger prototype properties](object#trigger-prototype) the method accepts the following parameters.

dependencies | array | [Triggers](/documentation/current/en/manual/api/reference/trigger/object#trigger) and [trigger prototypes](/documentation/current/en/manual/api/reference/triggerprototype/object#trigger-prototype) that the trigger prototype is dependent on.  
  
The triggers must have only the `triggerid` property defined.  
---|---|---  
tags | array | [Trigger prototype tags](/documentation/current/en/manual/api/reference/triggerprototype/object#trigger-prototype-tag).  
  
The trigger expression has to be given in its expanded form and must contain at least one item prototype.

### Return values

`(object)` Returns an object containing the IDs of the created trigger prototypes under the `triggerids` property. The order of the returned IDs matches the order of the passed trigger prototypes.

### Examples

#### Creating a trigger prototype

Create a trigger prototype to detect when a file system has less than 20% free disk space.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "triggerprototype.create",
               "params": {
                   "description": "Free disk space is less than 20% on volume {#FSNAME}",
                   "expression": "last(/Zabbix server/vfs.fs.size[{#FSNAME},pfree])<20",
                   "tags": [
                       {
                           "tag": "volume",
                           "value": "{#FSNAME}"
                       },
                       {
                           "tag": "type",
                           "value": "{#FSTYPE}"
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
                       "17372"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTriggerPrototype::create() in _ui/include/classes/api/services/CTriggerPrototype.php_.