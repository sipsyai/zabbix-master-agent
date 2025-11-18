---
title: hostgroup.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/delete
downloaded: 2025-11-14 10:42:06
---

# hostgroup.delete

### Description

`object hostgroup.delete(array hostGroupIds)`

This method allows to delete host groups.

A host group cannot be deleted if:

  * it contains hosts that belong to this group only;
  * it is marked as internal;
  * it is used by a host prototype;
  * it is used in a global script;
  * it is used in a correlation condition.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the host groups to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted host groups under the `groupids` property.

### Examples

#### Deleting multiple host groups

Delete two host groups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "hostgroup.delete",
               "params": [
                   "107824",
                   "107825"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "groupids": [
                       "107824",
                       "107825"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHostGroup::delete() in _ui/include/classes/api/services/CHostGroup.php_.