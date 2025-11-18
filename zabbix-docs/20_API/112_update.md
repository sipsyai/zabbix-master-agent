---
title: graphprototype.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/graphprototype/update
downloaded: 2025-11-14 10:41:46
---

# graphprototype.update

### Description

`object graphprototype.update(object/array graphPrototypes)`

This method allows to update existing graph prototypes.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Graph prototype properties to be updated.

The `graphid` property must be defined for each graph prototype, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard graph prototype properties](object#graph-prototype), the method accepts the following parameters.

gitems | array | [Graph items](/documentation/current/en/manual/api/reference/graphitem/object) to replace existing graph items. If a graph item has the `gitemid` property defined it will be updated, otherwise a new graph item will be created.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated graph prototypes under the `graphids` property.

### Examples

#### Changing the size of a graph prototype

Change the size of a graph prototype to 1100 to 400 pixels.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "graphprototype.update",
               "params": {
                   "graphid": "439",
                   "width": 1100,
                   "height": 400
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "graphids": [
                       "439"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CGraphPrototype::update() in _ui/include/classes/api/services/CGraphPrototype.php_.