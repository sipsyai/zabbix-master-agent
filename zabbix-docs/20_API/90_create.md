---
title: drule.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/drule/create
downloaded: 2025-11-14 10:41:24
---

# drule.create  
  
### Description

`object drule.create(object/array discoveryRules)`

This method allows to create new discovery rules.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Discovery rules to create.

Additionally to the [standard discovery rule properties](object#discovery-rule), the method accepts the following parameters.

dchecks | array | [Discovery checks](/documentation/current/en/manual/api/reference/dcheck/object) to create for the discovery rule.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created discovery rules under the `druleids` property. The order of the returned IDs matches the order of the passed discovery rules.

### Examples

#### Create a discovery rule

Create a discovery rule to find machines running the Zabbix agent in the local network. The rule must use a single Zabbix agent check on port 10050.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "drule.create",
               "params": {
                   "name": "Zabbix agent discovery",
                   "iprange": "192.168.1.1-255",
                   "concurrency_max": "10",
                   "dchecks": [
                       {
                           "type": "9",
                           "key_": "system.uname",
                           "ports": "10050",
                           "uniq": "0"
                       }
                   ]
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

CDRule::create() in _ui/include/classes/api/services/CDRule.php_.