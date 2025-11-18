---
title: iconmap.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/iconmap/create
downloaded: 2025-11-14 10:42:34
---

# iconmap.create  
  
### Description

`object iconmap.create(object/array iconMaps)`

This method allows to create new icon maps.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Icon maps to create.

Additionally to the [standard icon map properties](object#icon-map), the method accepts the following parameters.

mappings | array | [Icon mappings](/documentation/current/en/manual/api/reference/iconmap/object#icon-mapping) to be created for the icon map.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created icon maps under the `iconmapids` property. The order of the returned IDs matches the order of the passed icon maps.

### Examples

#### Create an icon map

Create an icon map to display hosts of different types.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "iconmap.create",
               "params": {
                   "name": "Type icons",
                   "default_iconid": "2",
                   "mappings": [
                       {
                           "inventory_link": 1,
                           "expression": "server",
                           "iconid": "3"
                       },
                       {
                           "inventory_link": 1,
                           "expression": "switch",
                           "iconid": "4"
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
                   "iconmapids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Icon mapping](object#icon-mapping)

### Source

CIconMap::create() in _ui/include/classes/api/services/CIconMap.php_.