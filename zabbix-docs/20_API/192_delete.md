---
title: discoveryruleprototype.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryruleprototype/delete
downloaded: 2025-11-14 10:43:05
---

# discoveryruleprototype.delete

### Description

`object discoveryruleprototype.delete(array lldRuleIds)`

This method allows to delete LLD rule prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the LLD rule prototypes to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted LLD rule prototypes under the `ruleids` property.

### Examples

#### Deleting multiple LLD rule prototypes

Delete two LLD rule prototypes.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryruleprototype.delete",
               "params": [
                   "47252",
                   "47253"
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
                       "47252",
                       "47253"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CDiscoveryRulePrototype::delete() in _ui/include/classes/api/services/CDiscoveryRulePrototype.php_.