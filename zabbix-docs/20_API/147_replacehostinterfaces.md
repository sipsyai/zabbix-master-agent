---
title: hostinterface.replacehostinterfaces
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/replacehostinterfaces
downloaded: 2025-11-14 10:42:20
---

# hostinterface.replacehostinterfaces

### Description

`object hostinterface.replacehostinterfaces(object parameters)`

This method allows to replace all host interfaces on a given host.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the ID of the host to be updated and the new host interfaces.

interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to replace the current host interfaces with.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hostid | ID | ID of the host to be updated.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the created host interfaces under the `interfaceids` property.

### Examples

#### Replacing host interfaces

Replace all host interfaces with a single agent interface.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.replacehostinterfaces",
               "params": {
                   "hostid": "30052",
                   "interfaces": {
                       "dns": "",
                       "ip": "127.0.0.1",
                       "main": 1,
                       "port": "10050",
                       "type": 1,
                       "useip": 1
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
                       "30081"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [host.update](/documentation/current/en/manual/api/reference/host/update)
  * [host.massupdate](/documentation/current/en/manual/api/reference/host/massupdate)

### Source

CHostInterface::replaceHostInterfaces() in _ui/include/classes/api/services/CHostInterface.php_.