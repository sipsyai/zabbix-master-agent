---
title: hostinterface.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/create
downloaded: 2025-11-14 10:42:15
---

# hostinterface.create  
  
### Description

`object hostinterface.create(object/array hostInterfaces)`

This method allows to create new host interfaces.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Host interfaces to create.

The method accepts host interfaces with the [standard host interface properties](object#host-interface).

### Return values

`(object)` Returns an object containing the IDs of the created host interfaces under the `interfaceids` property. The order of the returned IDs matches the order of the passed host interfaces.

### Examples

#### Create a new interface

Create a secondary IP agent interface on host "30052."

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.create",
               "params": {
                   "hostid": "30052",
                   "main": "0",
                   "type": "1",
                   "useip": "1",
                   "ip": "127.0.0.1",
                   "dns": "",
                   "port": "10050"
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
                       "30062"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create an interface with SNMP details

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.create",
               "params": {
                   "hostid": "10456",
                   "main": "0",
                   "type": "2",
                   "useip": "1",
                   "ip": "127.0.0.1",
                   "dns": "",
                   "port": "1601",
                   "details": {
                       "version": "2",
                       "bulk": "1",
                       "community": "{$SNMP_COMMUNITY}"
                   }
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
                       "30063"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [hostinterface.massadd](massadd)
  * [host.massadd](/documentation/current/en/manual/api/reference/host/massadd)

### Source

CHostInterface::create() in _ui/include/classes/api/services/CHostInterface.php_.