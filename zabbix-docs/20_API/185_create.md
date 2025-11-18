---
title: discoveryrule.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/discoveryrule/create
downloaded: 2025-11-14 10:42:58
---

# discoveryrule.create  
  
### Description

`object discoveryrule.create(object/array lldRules)`

This method allows to create new LLD rules.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` LLD rules to create.

Additionally to the [standard LLD rule properties](object#lld-rule), the method accepts the following parameters.

filter | object | [LLD rule filter](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-filter) for the LLD rule.  
---|---|---  
preprocessing | object/array | [LLD rule preprocessing](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-preprocessing) options.  
lld_macro_paths | object/array | LLD rule [lld_macro_path](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-macro-path) options.  
overrides | object/array | [LLD rule overrides](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule-overrides) options.  
  
### Return values

`(object)` Returns an object containing the IDs of the created LLD rules under the `itemids` property. The order of the returned IDs matches the order of the passed LLD rules.

### Examples

#### Creating an LLD rule

Create a Zabbix agent LLD rule to discover mounted file systems. Discovered items will be updated every 30 seconds.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "Mounted filesystem discovery",
                   "key_": "vfs.fs.discovery",
                   "hostid": "10197",
                   "type": 0,
                   "interfaceid": "112",
                   "delay": "30s"
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
                       "27665"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Using a filter

Create an LLD rule with a set of conditions to filter the results by. The conditions will be grouped together using the logical "and" operator.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "Filtered LLD rule",
                   "key_": "lld",
                   "hostid": "10116",
                   "type": 0,
                   "interfaceid": "13",
                   "delay": "30s",
                   "filter": {
                       "evaltype": 1,
                       "conditions": [
                           {
                               "macro": "{#MACRO1}",
                               "value": "@regex1"
                           },
                           {
                               "macro": "{#MACRO2}",
                               "value": "@regex2",
                               "operator": "9"
                           },
                           {
                               "macro": "{#MACRO3}",
                               "value": "",
                               "operator": "12"
                           },
                           {
                               "macro": "{#MACRO4}",
                               "value": "",
                               "operator": "13"
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
                       "27665"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating an LLD rule with macro paths

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "LLD rule with LLD macro paths",
                   "key_": "lld",
                   "hostid": "10116",
                   "type": 0,
                   "interfaceid": "13",
                   "delay": "30s",
                   "lld_macro_paths": [
                       {
                           "lld_macro": "{#MACRO1}",
                           "path": "$.path.1"
                       },
                       {
                           "lld_macro": "{#MACRO2}",
                           "path": "$.path.2"
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
                       "27665"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Using a custom expression filter

Create an LLD rule with a filter that will use a custom expression to evaluate the conditions. The LLD rule must only discover objects the "{#MACRO1}" macro value of which matches both regular expression "regex1" and "regex2", and the value of "{#MACRO2}" matches either "regex3" or "regex4". The formula IDs "A", "B", "C" and "D" have been chosen arbitrarily.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "Filtered LLD rule",
                   "key_": "lld",
                   "hostid": "10116",
                   "type": 0,
                   "interfaceid": "13",
                   "delay": "30s",
                   "filter": {
                       "evaltype": 3,
                       "formula": "(A and B) and (C or D)",
                       "conditions": [
                           {
                               "macro": "{#MACRO1}",
                               "value": "@regex1",
                               "formulaid": "A"
                           },
                           {
                               "macro": "{#MACRO1}",
                               "value": "@regex2",
                               "formulaid": "B"
                           },
                           {
                               "macro": "{#MACRO2}",
                               "value": "@regex3",
                               "formulaid": "C"
                           },
                           {
                               "macro": "{#MACRO2}",
                               "value": "@regex4",
                               "formulaid": "D"
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
                       "27665"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Using custom query fields and headers

Create LLD rule with custom query fields and headers.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "hostid": "10257",
                   "interfaceid": "5",
                   "type": 19,
                   "name": "API HTTP agent",
                   "key_": "api_discovery_rule",
                   "delay": "5s",
                   "url": "http://127.0.0.1?discoverer.php",
                   "query_fields": [
                       {
                           "name": "mode",
                           "value": "json"
                       },
                       {
                           "name": "elements",
                           "value": "2"
                       }
                   ],
                   "headers": [
                       {
                           "name": "X-Type",
                           "value": "api"
                       },
                       {
                           "name": "Authorization",
                           "value": "Bearer mF_A.B5f-2.1JcM"
                       }
                   ],
                   "allow_traps": 1,
                   "trapper_hosts": "127.0.0.1"
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

#### Creating an LLD rule with preprocessing

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "Discovery rule with preprocessing",
                   "key_": "lld.with.preprocessing",
                   "hostid": "10001",
                   "ruleid": "27665",
                   "type": 0,
                   "delay": "60s",
                   "interfaceid": "1155",
                   "preprocessing": [
                       {
                           "type": 20,
                           "params": "20",
                           "error_handler": 0,
                           "error_handler_params": ""
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

#### Creating an LLD rule with overrides

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "Discover database host",
                   "key_": "lld.with.overrides",
                   "hostid": "10001",
                   "type": 0,
                   "delay": "60s",
                   "interfaceid": "1155",
                   "overrides": [
                       {
                           "name": "Discover MySQL host",
                           "step": "1",
                           "stop": "1",
                           "filter": {
                               "evaltype": "2",
                               "conditions": [
                                   {
                                       "macro": "{#UNIT.NAME}",
                                       "operator": "8",
                                       "value": "^mysqld\\.service$"
                                   },
                                   {
                                       "macro": "{#UNIT.NAME}",
                                       "operator": "8",
                                       "value": "^mariadb\\.service$"
                                   }
                               ]
                           },
                           "operations": [
                               {
                                   "operationobject": "3",
                                   "operator": "2",
                                   "value": "Database host",
                                   "opstatus": {
                                       "status": "0"
                                   },
                                   "optemplate": [
                                       {
                                           "templateid": "10170"
                                       }
                                   ],
                                   "optag": [
                                       {
                                           "tag": "database",
                                           "value": "mysql"
                                       }
                                   ]
                               }
                           ]
                       },
                       {
                           "name": "Discover PostgreSQL host",
                           "step": "2",
                           "stop": "1",
                           "filter": {
                               "evaltype": "0",
                               "conditions": [
                                   {
                                       "macro": "{#UNIT.NAME}",
                                       "operator": "8",
                                       "value": "^postgresql\\.service$"
                                   }
                               ]
                           },
                           "operations": [
                               {
                                   "operationobject": "3",
                                   "operator": "2",
                                   "value": "Database host",
                                   "opstatus": {
                                       "status": "0"
                                   },
                                   "optemplate": [
                                       {
                                           "templateid": "10263"
                                       }
                                   ],
                                   "optag": [
                                       {
                                           "tag": "database",
                                           "value": "postgresql"
                                       }
                                   ]
                               }
                           ]
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
                       "30980"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create script LLD rule

Create a simple data collection using a script LLD rule.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "Script example",
                   "key_": "custom.script.lldrule",
                   "hostid": "12345",
                   "type": 21,
                   "params": "var request = new HttpRequest();\nreturn request.post(\"https://postman-echo.com/post\", JSON.parse(value));",
                   "parameters": [{
                       "name": "host",
                       "value": "{HOST.CONN}"
                   }],
                   "timeout": "6s",
                   "delay": "30s"
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

#### Create LLD rule with a specified time period for disabling and no deletion

Create an LLD rule with custom time period for disabling entity after it is no longer discovered, with the setting that it will never be deleted.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "discoveryrule.create",
               "params": {
                   "name": "lld disable after 1h",
                   "key_": "lld.disable",
                   "hostid": "10001",
                   "type": 2,
                   "lifetime_type": 1,
                   "enabled_lifetime_type": 0, 
                   "enabled_lifetime": "1h"
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

### See also

  * [LLD rule filter](object#lld-rule-filter)
  * [LLD macro paths](object#lld-macro-path)
  * [LLD rule preprocessing](object#lld-rule-preprocessing)

### Source

CDiscoveryRule::create() in _ui/include/classes/api/services/CDiscoveryRule.php_.