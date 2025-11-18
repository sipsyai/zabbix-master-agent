---
title: triggerprototype.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/triggerprototype/update
downloaded: 2025-11-14 10:45:27
---

# triggerprototype.update

### Description

`object triggerprototype.update(object/array triggerPrototypes)`

This method allows to update existing trigger prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Trigger prototype properties to be updated.

The `triggerid` property must be defined for each trigger prototype, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard trigger prototype properties](object#trigger-prototype) the method accepts the following parameters.

dependencies | array | [Triggers](/documentation/current/en/manual/api/reference/trigger/object#trigger) and [trigger prototypes](/documentation/current/en/manual/api/reference/triggerprototype/object#trigger-prototype) that the trigger prototype is dependent on.  
  
The triggers must have only the `triggerid` property defined.  
---|---|---  
tags | array | [Trigger prototype tags](/documentation/current/en/manual/api/reference/triggerprototype/object#trigger-prototype-tag).  
  
The trigger expression has to be given in its expanded form and must contain at least one item prototype.

### Return values

`(object)` Returns an object containing the IDs of the updated trigger prototypes under the `triggerids` property.

### Examples

#### Enabling a trigger prototype

Enable a trigger prototype, that is, set its status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "triggerprototype.update",
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

#### Replacing trigger prototype tags

Replace tags for one trigger prototype.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "triggerprototype.update",
               "params": {
                   "triggerid": "17373",
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
                       "17373"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTriggerPrototype::update() in _ui/include/classes/api/services/CTriggerPrototype.php_.