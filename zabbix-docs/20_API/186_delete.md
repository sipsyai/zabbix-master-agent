---
title: discoveryrule.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryrule/delete
downloaded: 2025-11-14 10:42:59
---

# discoveryrule.delete

### Description

`object discoveryrule.delete(array lldRuleIds)`

This method allows to delete LLD rules.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the LLD rules to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted LLD rules under the `ruleids` property.

### Examples

#### Deleting multiple LLD rules

Delete two LLD rules.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.delete",
               "params": [
                   "27665",
                   "27668"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "ruleids": [
                       "27665",
                       "27668"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CDiscoveryRule::delete() in _ui/include/classes/api/services/CDiscoveryRule.php_.