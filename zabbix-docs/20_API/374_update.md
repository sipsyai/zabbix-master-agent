---
title: valuemap.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/valuemap/update
downloaded: 2025-11-14 10:46:07
---

# valuemap.update

### Description

`object valuemap.update(object/array valuemaps)`

This method allows to update existing value maps.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Value map properties](object#value-map) to be updated.

The `valuemapid` property must be defined for each value map, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

### Return values

`(object)` Returns an object containing the IDs of the updated value maps under the `valuemapids` property.

### Examples

#### Changing value map name

Change value map name to "Device status".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "valuemap.update",
               "params": {
                   "valuemapid": "2",
                   "name": "Device status"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "valuemapids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Changing mappings for one value map.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "valuemap.update",
               "params": {
                   "valuemapid": "2",
                   "mappings": [
                       {
                           "type": "0",
                           "value": "0",
                           "newvalue": "Online"
                       },
                       {
                           "type": "0",
                           "value": "1",
                           "newvalue": "Offline"
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
                   "valuemapids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CValueMap::update() in _ui/include/classes/api/services/CValueMap.php_.