---
title: valuemap.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/valuemap/create
downloaded: 2025-11-14 10:46:04
---

# valuemap.create

### Description

`object valuemap.create(object/array valuemaps)`

This method allows to create new value maps.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Value maps to create.

The method accepts value maps with the [standard value map properties](object#value-map).

### Return values

`(object)` Returns an object containing the IDs of the created value maps the `valuemapids` property. The order of the returned IDs matches the order of the passed value maps.

### Examples

#### Creating a value map

Create one value map with two mappings.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "valuemap.create",
               "params": {
                   "hostid": "50009",
                   "name": "Service state",
                   "mappings": [
                       {
                           "type": "1",
                           "value": "1",
                           "newvalue": "Up"
                       },
                       {
                           "type": "5",
                           "newvalue": "Down"
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
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CValueMap::create() in _ui/include/classes/api/services/CValueMap.php_.