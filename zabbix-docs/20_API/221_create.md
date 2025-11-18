---
title: module.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/module/create
downloaded: 2025-11-14 10:43:34
---

# module.create  
  
### Description

`object module.create(object/array modules)`

This method allows to install new frontend modules.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

Module files must be unpacked manually in the correct subdirectories, matching the `relative_path` property of the modules.

### Parameters

`(object/array)` Modules to create.

The method accepts modules with the [standard module properties](object#module).

### Return values

`(object)` Returns an object containing the IDs of the installed modules under the `moduleids` property. The order of the returned IDs matches the order of the passed modules.

### Examples

#### Installing a module

Install a module with the status "Enabled".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "module.create",
               "params": {
                   "id": "example_module",
                   "relative_path": "modules/example_module",
                   "status": 1
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

CModule::create() in _ui/include/classes/api/services/CModule.php_.