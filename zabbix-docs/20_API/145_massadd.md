---
title: hostinterface.massadd
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/massadd
downloaded: 2025-11-14 10:42:18
---

# hostinterface.massadd

### Description

`object hostinterface.massadd(object parameters)`

This method allows to simultaneously add host interfaces to multiple hosts.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the host interfaces to be created on the given hosts.

The method accepts the following parameters.

interfaces | object/array | [Host interfaces](/documentation/current/en/manual/api/reference/hostinterface/object) to create on the given hosts.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hosts | object/array | [Hosts](/documentation/current/en/manual/api/reference/host/object) to be updated.  
  
The hosts must have only the `hostid` property defined.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(object)` Returns an object containing the IDs of the created host interfaces under the `interfaceids` property.

### Examples

#### Creating interfaces

Create an interface on two hosts.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.massadd",
               "params": {
                   "hosts": [
                       {
                           "hostid": "30050"
                       },
                       {
                           "hostid": "30052"
                       }
                   ],
                   "interfaces": {
                       "dns": "",
                       "ip": "127.0.0.1",
                       "main": 0,
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
                       "30069",
                       "30070"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [hostinterface.create](create)
  * [host.massadd](/documentation/current/en/manual/api/reference/host/massadd)
  * [Host](/documentation/current/en/manual/api/reference/host/object#host)

### Source

CHostInterface::massAdd() in _ui/include/classes/api/services/CHostInterface.php_.