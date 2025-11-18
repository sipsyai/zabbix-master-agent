---
title: itemprototype.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/itemprototype/update
downloaded: 2025-11-14 10:42:55
---

# itemprototype.update

### Description

`object itemprototype.update(object/array itemPrototypes)`

This method allows to update existing item prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Item prototype properties to be updated.

The `itemid` property must be defined for each item prototype, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard item prototype properties](object#item-prototype), the method accepts the following parameters.

preprocessing | array | [Item prototype preprocessing](/documentation/current/en/manual/api/reference/itemprototype/object#item-prototype-preprocessing) options to replace the current preprocessing options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects  
---|---|---  
tags | array | [Item prototype tags](/documentation/current/en/manual/api/reference/itemprototype/object#item-prototype-tag).  
  
### Return values

`(object)` Returns an object containing the IDs of the updated item prototypes under the `itemids` property.

### Examples

#### Changing the interface of an item prototype

Change the host interface that will be used by discovered items.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.update",
               "params": {
                   "itemid": "27428",
                   "interfaceid": "132"
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
                       "27428"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Update dependent item prototype

Update Dependent item prototype with new Master item prototype ID. Only dependencies on same host (template/discovery rule) are allowed, therefore Master and Dependent item should have same hostid and ruleid.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.update",
               "params": {
                   "master_itemid": "25570",
                   "itemid": "189030"
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
                       "189030"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Update HTTP agent item prototype

Change query fields and remove all custom headers.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.update",
               "params": {
                   "itemid":"28305",
                   "query_fields": [
                       {
                           "name": "random",
                           "value": "qwertyuiopasdfghjklzxcvbnm"
                       }
                   ],
                   "headers": []
               }
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

#### Updating item preprocessing options

Update an item prototype with item preprocessing rule “Custom multiplier”.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.update",
               "params": {
                   "itemid": "44211",
                   "preprocessing": [
                       {
                           "type": 1,
                           "params": "4",
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

#### Updating a script item prototype

Update a script item prototype with a different script and remove unnecessary parameters that were used by previous script.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "itemprototype.update",
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

### Source

CItemPrototype::update() in _ui/include/classes/api/services/CItemPrototype.php_.