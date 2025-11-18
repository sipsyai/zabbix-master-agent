---
title: hostinterface.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/delete
downloaded: 2025-11-14 10:42:16
---

# hostinterface.delete

### Description

`object hostinterface.delete(array hostInterfaceIds)`

This method allows to delete host interfaces.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the host interfaces to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted host interfaces under the `interfaceids` property.

### Examples

#### Delete a host interface

Delete the host interface with ID 30062.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostinterface.delete",
               "params": [
                   "30062"
               ],
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

### See also

  * [hostinterface.massremove](massremove)
  * [host.massremove](/documentation/current/en/manual/api/reference/host/massremove)

### Source

CHostInterface::delete() in _ui/include/classes/api/services/CHostInterface.php_.