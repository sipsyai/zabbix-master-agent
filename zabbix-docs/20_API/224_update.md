---
title: module.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/module/update
downloaded: 2025-11-14 10:43:37
---

# module.update

### Description

`object module.update(object/array modules)`

This method allows to update existing modules.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Module properties to be updated.

The `moduleid` property must be defined for each module, all other properties are optional. Only the specified properties will be updated.

The method accepts modules with the [standard module properties](object#module).

### Return values

`(object)` Returns an object containing the IDs of the updated modules under the `moduleids` property.

### Examples

#### Disabling a module

Disable module "25".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "module.update",
               "params": {
                   "moduleid": "25",
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
                   "moduleids": [
                       "25"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Module](object#module)
  * [Frontend modules](/documentation/current/en/manual/extensions/frontendmodules)

### Source

CModule::update() in _ui/include/classes/api/services/CModule.php_.