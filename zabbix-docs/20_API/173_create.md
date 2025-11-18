---
title: item.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/item/create
downloaded: 2025-11-14 10:42:46
---

# item.create

### Description

`object item.create(object/array items)`

This method allows to create new items.

Web items cannot be created via the Zabbix API.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Items to create.

Additionally to the [standard item properties](object#host), the method accepts the following parameters.

preprocessing | array | [Item preprocessing](/documentation/current/en/manual/api/reference/item/object#item-preprocessing) options.  
---|---|---  
tags | array | [Item tags](/documentation/current/en/manual/api/reference/item/object#item-tag).  
  
### Return values

`(object)` Returns an object containing the IDs of the created items under the `itemids` property. The order of the returned IDs matches the order of the passed items.

### Examples

#### Creating an item

Create a numeric Zabbix agent item with 2 item tags to monitor free disk space on host with ID "30074".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.create",
               "params": {
                   "name": "Free disk space on /home/joe/",
                   "key_": "vfs.fs.size[/home/joe/,free]",
                   "hostid": "30074",
                   "type": 0,
                   "value_type": 3,
                   "interfaceid": "30084",
                   "tags": [
                       {
                           "tag": "component",
                           "value": "storage"
                       },
                       {
                           "tag": "equipment",
                           "value": "workstation"
                       }
                   ],
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
                       "24758"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a host inventory item

Create a Zabbix agent item to populate the host's "OS" inventory field.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.create",
               "params": {
                   "name": "uname",
                   "key_": "system.uname",
                   "hostid": "30021",
                   "type": 0,
                   "interfaceid": "30007",
                   "value_type": 1,
                   "delay": "10s",
                   "inventory_link": 5
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
                       "24759"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating an item with preprocessing

Create an item using custom multiplier.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.create",
               "params": {
                   "name": "Device uptime",
                   "key_": "sysUpTime",
                   "hostid": "10084",
                   "type": 20,
                   "snmp_oid": "SNMPv2-MIB::sysUpTime.0",
                   "value_type": 1,
                   "delay": "60s",
                   "interfaceid": "83",
                   "preprocessing": [
                       {
                           "type": 1,
                           "params": "0.01",
                           "error_handler": 1,
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
                       "44210"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating dependent item

Create a dependent item for the master item with ID 24759. Only dependencies on the same host are allowed, therefore master and the dependent item should have the same hostid.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.create",
               "params": {
                 "hostid": "30074",
                 "name": "Dependent test item",
                 "key_": "dependent.item",
                 "type": 18,
                 "master_itemid": "24759",
                 "value_type": 2
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

#### Create HTTP agent item

Create POST request method item with JSON response preprocessing.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.create",
               "params": {
                   "url":"http://127.0.0.1/http.php",
                   "query_fields": [
                       {
                           "name": "mode",
                           "value": "json"
                       },
                       {
                           "name": "min",
                           "value": "10"
                       },
                       {
                           "name": "max",
                           "value": "100"
                       }
                   ],
                   "interfaceid": "1",
                   "type": 19,
                   "hostid": "10254",
                   "delay": "5s",
                   "key_": "json",
                   "name": "HTTP agent example JSON",
                   "value_type": 0,
                   "output_format": 1,
                   "preprocessing": [
                       {
                           "type": 12,
                           "params": "$.random",
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
                       "23865"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create script item

Create a simple data collection using a script item.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.create",
               "params": {
                   "name": "Script example",
                   "key_": "custom.script.item",
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

CItem::create() in _ui/include/classes/api/services/CItem.php_.