---
title: item.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/item/update
downloaded: 2025-11-14 10:42:49
---

# item.update

### Description

`object item.update(object/array items)`

This method allows to update existing items.

Web items cannot be updated via the Zabbix API.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Item properties to be updated.

The `itemid` property must be defined for each item, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard item properties](object#item), the method accepts the following parameters.

preprocessing | array | [Item preprocessing](/documentation/current/en/manual/api/reference/item/object#item-preprocessing) options to replace the current preprocessing options.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for inherited objects or discovered objects  
---|---|---  
tags | array | [Item tags](/documentation/current/en/manual/api/reference/item/object#item-tag).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _read-only_ for discovered objects  
  
### Return values

`(object)` Returns an object containing the IDs of the updated items under the `itemids` property.

### Examples

#### Enabling an item

Enable an item, that is, set its status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.update",
               "params": {
                   "itemid": "10092",
                   "status": 0
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
                       "10092"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Update dependent item

Update Dependent item name and Master item ID. Only dependencies on same host are allowed, therefore Master and Dependent item should have same hostid.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.update",
               "params": {
                   "name": "Dependent item updated name",
                   "master_itemid": "25562",
                   "itemid": "189019"
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
                       "189019"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Update HTTP agent item

Enable item value trapping.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.update",
               "params": {
                   "itemid": "23856",
                   "allow_traps": 1
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
                       "23856"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating an item with preprocessing

Update an item with item preprocessing rule "In range".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.update",
               "params": {
                   "itemid": "23856",
                   "preprocessing": [
                       {
                           "type": 13,
                           "params": "\n100",
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
                       "23856"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Updating a script item

Update a script item with a different script and remove unnecessary parameters that were used by previous script.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "item.update",
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

CItem::update() in _ui/include/classes/api/services/CItem.php_.