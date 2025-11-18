---
title: hostinterface.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/update
downloaded: 2025-11-14 10:42:21
---

# hostinterface.update

### Description

`object hostinterface.update(object/array hostInterfaces)`

This method allows to update existing host interfaces.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Host interface properties](object#host-interface) to be updated.

The `interfaceid` property must be defined for each host interface, all other properties are optional. Only the given properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated host interfaces under the `interfaceids` property.

### Examples

#### Changing a host interface port

Change the port of a host interface.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.update",
               "params": {
                   "interfaceid": "30048",
                   "port": "30050"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "interfaceids": [
                       "30048"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHostInterface::update() in _ui/include/classes/api/services/CHostInterface.php_.