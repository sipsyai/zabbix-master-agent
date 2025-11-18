---
title: discoveryruleprototype.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryruleprototype/create
downloaded: 2025-11-14 10:43:04
---

# discoveryruleprototype.create  
  
### Description

`object discoveryruleprototype.create(object/array lldRules)`

This method allows to create new LLD rule prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` LLD rule prototypes to create.

Additionally to the [standard LLD rule prototype properties](object#lld-rule-prototype), the method accepts the following parameters.

filter | object | [LLD rule prototype filter](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-rule-filter) for the LLD rule.  
---|---|---  
preprocessing | object/array | [LLD rule prototype preprocessing](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-rule-preprocessing) options.  
lld_macro_paths | object/array | LLD rule prototype [lld_macro_path](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-macro-path) options.  
overrides | object/array | [LLD rule prototype overrides](/documentation/current/en/manual/api/reference/discoveryruleprototype/object#lld-rule-overrides) options.  
  
### Return values

`(object)` Returns an object containing the IDs of the created LLD rule prototypes under the `itemids` property. The order of the returned IDs matches the order of the passed LLD rule prototypes.

### Examples

#### Creating an LLD rule prototype

Create an LLD rule prototype (Type: Nested) to discover tablespaces in database instance.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryruleprototype.create",
               "params": {
                   "name": "Discover tablespaces for {#DB}",
                   "key_": "db.tablespace.discovery[{#DB}]",
                   "hostid": "10084",
                   "ruleid": "47251",
                   "type": 23
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
                       "47252"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [LLD rule prototype filter](object#lld-rule-prototype-filter)
  * [LLD macro paths](object#lld-macro-path)
  * [LLD rule prototype preprocessing](object#lld-rule-prototype-preprocessing)

### Source

CDiscoveryRulePrototype::create() in _ui/include/classes/api/services/CDiscoveryRulePrototype.php_.