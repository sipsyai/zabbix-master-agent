---
title: usergroup.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/usergroup/delete
downloaded: 2025-11-14 10:45:50
---

# usergroup.delete

### Description

`object usergroup.delete(array userGroupIds)`

This method allows to delete user groups.

[Deprovisioned](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#configuration) users group (the user group specified for `disabled_usrgrpid` in [Authentication](/documentation/current/en/manual/api/reference/authentication/object)) cannot be deleted.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the user groups to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted user groups under the `usrgrpids` property.

### Examples

#### Deleting multiple user groups

Delete two user groups.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "usergroup.delete",
               "params": [
                   "20",
                   "21"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "usrgrpids": [
                       "20",
                       "21"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserGroup::delete() in _ui/include/classes/api/services/CUserGroup.php_.