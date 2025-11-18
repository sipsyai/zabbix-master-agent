---
title: drule.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/drule/delete
downloaded: 2025-11-14 10:41:25
---

# drule.delete

### Description

`object drule.delete(array discoveryRuleIds)`

This method allows to delete discovery rules.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the discovery rules to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted discovery rules under the `druleids` property.

### Examples

#### Delete multiple discovery rules

Delete two discovery rules.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "drule.delete",
               "params": [
                   "4",
                   "6"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "druleids": [
                       "4",
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CDRule::delete() in _ui/include/classes/api/services/CDRule.php_.