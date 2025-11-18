---
title: hostinterface.massremove
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/massremove
downloaded: 2025-11-14 10:42:19
---

# hostinterface.massremove

### Description

`object hostinterface.massremove(object parameters)`

This method allows to remove host interfaces from the given hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the IDs of the hosts to be updated and the interfaces to be removed.

interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to remove from the given hosts.  
  
The host interface object must have only the `ip`, `dns` and `port` properties defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hostids | ID/array | IDs of the hosts to be updated.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the deleted host interfaces under the `interfaceids` property.

### Examples

#### Removing interfaces

Remove the "127.0.0.1" SNMP interface from two hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.massremove",
               "params": {
                   "hostids": [
                       "30050",
                       "30052"
                   ],
                   "interfaces": {
                       "dns": "",
                       "ip": "127.0.0.1",
                       "port": "161"
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
                       "30069",
                       "30070"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [hostinterface.delete](delete)
  * [host.massremove](/documentation/current/en/manual/api/reference/host/massremove)

### Source

CHostInterface::massRemove() in _ui/include/classes/api/services/CHostInterface.php_.