---
title: drule.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/drule/update
downloaded: 2025-11-14 10:41:27
---

# drule.update

### Description

`object drule.update(object/array discoveryRules)`

This method allows to update existing discovery rules.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Discovery rule properties to be updated.

The `druleid` property must be defined for each discovery rule, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard discovery rule properties](object#discovery-rule), the method accepts the following parameters.

dchecks | array | [Discovery checks](/documentation/current/en/manual/api/reference/dcheck/object) to replace existing checks.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated discovery rules under the `druleids` property.

### Examples

#### Change the IP range of a discovery rule

Change the IP range of a discovery rule to "192.168.2.1-255".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "drule.update",
               "params": {
                   "druleid": "6",
                   "iprange": "192.168.2.1-255"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "druleids": [
                       "6"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Discovery check](/documentation/current/en/manual/api/reference/dcheck/object#discovery-check)

### Source

CDRule::update() in _ui/include/classes/api/services/CDRule.php_.