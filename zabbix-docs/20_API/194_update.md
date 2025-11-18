---
title: discoveryruleprototype.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryruleprototype/update
downloaded: 2025-11-14 10:43:07
---

# discoveryruleprototype.update

### Description

`object discoveryruleprototype.update(object/array lldRules)`

This method allows to update existing LLD rule prototypes.

Note that the updating of already discovered prototypes is limited.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` LLD rule prototype properties to be updated.

The `itemid` property must be defined for each LLD rule prototype, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard LLD rule prototype properties](object#lld-rule-prototype), the method accepts the following parameters.

filter | object | [LLD rule prototype filter](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-filter) to replace the existing filter.  
---|---|---  
preprocessing | object/array | [LLD rule prototype preprocessing](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-preprocessing) options to replace the existing preprocessing options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
lld_macro_paths | object/array | LLD rule prototype [lld_macro_path](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-macro-path) options to replace the existing lld_macro_path options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
overrides | object/array | [LLD rule prototype overrides](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-rule-prototype-overrides) options to replace the existing overrides options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
  
### Return values

`(object)` Returns an object containing the IDs of the updated LLD rule prototypes under the `itemids` property.

### Examples

#### Updating LLD rule prototype preprocessing options

Update an LLD rule prototype with a JSONPath preprocessing rule. [Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryruleprototype.update",
               "params": {
                   "itemid": "47253",
                   "preprocessing": [
                       {
                           "type": 12,
                           "params": "$.tablespaces",
                           "error_handler": 1
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
                       "47253"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CDiscoveryRulePrototype::update() in _ui/include/classes/api/services/CDiscoveryRulePrototype.php_.