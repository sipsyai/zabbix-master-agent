---
title: itemprototype.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/itemprototype/create
downloaded: 2025-11-14 10:42:52
---

# itemprototype.create

### Description

`object itemprototype.create(object/array itemPrototypes)`

This method allows to create new item prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Item prototype to create.

Additionally to the [standard item prototype properties](object#item-prototype), the method accepts the following parameters.

ruleid | ID | ID of the [LLD rule](/documentation/current/en/manual/api/reference/discoveryrule/object#lld-rule) that the item belongs to.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
preprocessing | array | [Item prototype preprocessing](/documentation/current/en/manual/api/reference/itemprototype/object#item-prototype-preprocessing) options.  
tags | array | [Item prototype tags](/documentation/current/en/manual/api/reference/itemprototype/object#item-prototype-tag).  
  
### Return values

`(object)` Returns an object containing the IDs of the created item prototypes under the `itemids` property. The order of the returned IDs matches the order of the passed item prototypes.

### Examples

#### Creating an item prototype

Create an item prototype to monitor free disk space on a discovered file system. Discovered items should be numeric Zabbix agent items updated every 30 seconds.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.create",
               "params": {
                   "name": "Free disk space on {#FSNAME}",
                   "key_": "vfs.fs.size[{#FSNAME},free]",
                   "hostid": "10197",
                   "ruleid": "27665",
                   "type": 0,
                   "value_type": 3,
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
                       "27666"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating an item prototype with preprocessing

Create an item using change per second and a custom multiplier as a second step.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.create",
               "params": {
                   "name": "Incoming network traffic on {#IFNAME}",
                   "key_": "net.if.in[{#IFNAME}]",
                   "hostid": "10001",
                   "ruleid": "27665",
                   "type": 0,
                   "value_type": 3,
                   "delay": "60s",
                   "units": "bps",
                   "interfaceid": "1155",
                   "preprocessing": [
                       {
                           "type": 10,
                           "params": "",
                           "error_handler": 0,
                           "error_handler_params": ""
                       },
                       {
                           "type": 1,
                           "params": "8",
                           "error_handler": 2,
                           "error_handler_params": "10"
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

#### Creating dependent item prototype

Create Dependent item prototype for Master item prototype with ID 44211. Only dependencies on same host (template/discovery rule) are allowed, therefore Master and Dependent item should have same hostid and ruleid.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.create",
               "params": {
                 "hostid": "10001",
                 "ruleid": "27665",
                 "name": "Dependent test item prototype",
                 "key_": "dependent.prototype",
                 "type": 18,
                 "master_itemid": "44211",
                 "value_type": 3
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
                       "44212"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create HTTP agent item prototype

Create item prototype with URL using user macro, query fields and custom headers.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.create",
               "params": {
                   "type": "19",
                   "hostid": "10254",
                   "ruleid": "28256",
                   "interfaceid": "2",
                   "name": "api item prototype example",
                   "key_": "api_http_item",
                   "value_type": 3,
                   "url": "{$URL_PROTOTYPE}",
                   "query_fields": [
                       {
                           "name": "min",
                           "value": "10"
                       },
                       {
                           "name": "max",
                           "value" "100"
                       }
                   ],
                   "headers": [
                       {
                           "name": "X-Source",
                           "value": "api"
                       }
                   ],
                   "delay": "35"
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
                       "28305"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create script item prototype

Create a simple data collection using a script item prototype.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.create",
               "params": {
                   "name": "Script example",
                   "key_": "custom.script.itemprototype",
                   "hostid": "12345",
                   "type": 21,
                   "value_type": 4,
                   "params": "var request = new HttpRequest();\nreturn request.post(\"https://postman-echo.com/post\", JSON.parse(value));",
                   "parameters": [
                       {
                           "name": "host",
                           "value": "{HOST.CONN}"
                       }
                   ],
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

### Source

CItemPrototype::create() in _ui/include/classes/api/services/CItemPrototype.php_.