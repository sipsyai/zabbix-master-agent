---
title: iconmap.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/iconmap/update
downloaded: 2025-11-14 10:42:37
---

# iconmap.update

### Description

`object iconmap.update(object/array iconMaps)`

This method allows to update existing icon maps.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Icon map properties to be updated.

The `iconmapid` property must be defined for each icon map, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard icon map properties](object#icon-map), the method accepts the following parameters.

mappings | array | [Icon mappings](/documentation/current/en/manual/api/reference/iconmap/object#icon-mapping) to replace the existing icon mappings.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the updated icon maps under the `iconmapids` property.

### Examples

#### Rename icon map

Rename an icon map to "OS icons".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "iconmap.update",
               "params": {
                   "iconmapid": "1",
                   "name": "OS icons"
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
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Icon mapping](object#icon-mapping)

### Source

CIconMap::update() in _ui/include/classes/api/services/CIconMap.php_.