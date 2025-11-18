---
title: discoveryrule.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryrule/update
downloaded: 2025-11-14 10:43:01
---

# discoveryrule.update

### Description

`object discoveryrule.update(object/array lldRules)`

This method allows to update existing LLD rules.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` LLD rule properties to be updated.

The `itemid` property must be defined for each LLD rule, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard LLD rule properties](object#lld-rule), the method accepts the following parameters.

filter | object | [LLD rule filter](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-filter) to replace the existing filter.  
---|---|---  
preprocessing | object/array | [LLD rule preprocessing](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-preprocessing) options to replace the existing preprocessing options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
lld_macro_paths | object/array | LLD rule [lld_macro_path](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-macro-path) options to replace the existing lld_macro_path options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
overrides | object/array | [LLD rule overrides](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-overrides) options to replace the existing overrides options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
  
### Return values

`(object)` Returns an object containing the IDs of the updated LLD rules under the `itemids` property.

### Examples

#### Adding a filter to an LLD rule

Add a filter so that the contents of the _{#FSTYPE}_ macro would match the _@File systems for discovery_ regexp.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.update",
               "params": {
                   "itemid": "22450",
                   "filter": {
                       "evaltype": 1,
                       "conditions": [
                           {
                               "macro": "{#FSTYPE}",
                               "value": "@File systems for discovery"
                           }
                       ]
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
                   "itemids": [
                       "22450"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Adding LLD macro paths

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.update",
               "params": {
                   "itemid": "22450",
                   "lld_macro_paths": [
                       {
                           "lld_macro": "{#MACRO1}",
                           "path": "$.json.path"
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
                   "itemids": [
                       "22450"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Disable trapping

Disable LLD trapping for discovery rule.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.update",
               "params": {
                   "itemid": "28336",
                   "allow_traps": 0
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "itemids": [
                       "28336"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating LLD rule preprocessing options

Update an LLD rule with preprocessing rule “JSONPath”.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.update",
               "params": {
                   "itemid": "44211",
                   "preprocessing": [
                       {
                           "type": 12,
                           "params": "$.path.to.json",
                           "error_handler": 2,
                           "error_handler_params": "5"
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
                   "itemids": [
                       "44211"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating LLD rule script

Update an LLD rule script with a different script and remove unnecessary parameters that were used by previous script.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.update",
               "params": {
                   "itemid": "23865",
                   "parameters": [],
                   "script": "Zabbix.log(3, 'Log test');\nreturn 1;"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "itemids": [
                       "23865"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating LLD rule lifetime

Update LLD rule to disable no-longer discovered entity after 12 hours and to delete it after 7 days.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.update",
               "params": {
                   "itemid": "46864",
                   "lifetime_type": 0, 
                   "lifetime": "7d",
                   "enabled_lifetime_type": 0,
                   "enabled_lifetime": "12h"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "itemids": [
                       "46864"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CDiscoveryRule::update() in _ui/include/classes/api/services/CDiscoveryRule.php_.