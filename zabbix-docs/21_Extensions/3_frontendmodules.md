---
title: Frontend modules
source: https://www.zabbix.com/documentation/current/en/manual/extensions/frontendmodules
downloaded: 2025-11-14 10:46:21
---

# 3 Frontend modules  
  
#### Overview

It is possible to enhance Zabbix frontend functionality by adding third-party modules or by developing your own modules without the need to change the source code of Zabbix.

Note that the module code will run with the same privileges as Zabbix source code. This means:

  * third-party modules can be harmful. You must trust the modules you are installing;
  * Errors in a third-party module code may crash the frontend. If this happens, just remove the module code from the frontend. As soon as you reload Zabbix frontend, you'll see a note saying that some modules are absent. Go to [Module administration](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#modules) (in _Administration_ → _General_ → _Modules_) and click _Scan directory_ again to remove non-existent modules from the database.

#### Installation

Please always read the installation manual for a particular module. It is recommended to install new modules one by one to catch failures easily.

Just before you install a module:

  * Make sure you have downloaded the module from a trusted source. Installation of harmful code may lead to consequences, such as data loss
  * Different versions of the same module (same ID) can be installed in parallel, but only a single version can be enabled at once

Steps to install a module:

  * Unpack your module within its own folder in the `modules` folder of the Zabbix frontend
  * Ensure that your module folder contains at least the manifest.json file
  * Navigate to [Module administration](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#modules) and click the _Scan directory_ button
  * New module will appear in the list along with its version, author, description and status
  * Enable module by clicking on its status

Troubleshooting:

_Module did not appear in the list_ | If your module didn't appear in the list, make sure manifest.json exists in modules/your-module/. If it doesn't, you might have unpacked the module to the wrong directory. If it does, the module might not be compatible with your Zabbix version. Also, check that the web server user has at least read and search access (`r-x`) to the module folder and all subdirectories, and read access (`r--`) to all files inside.  
---|---  
_Frontend crashed_ | The module code is not compatible with the current Zabbix version or server configuration. Please delete module files and reload the frontend. You'll see a notice that some modules are absent. Go to [Module administration](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#modules) and click _Scan directory_ again to remove non-existent modules from the database.  
_Error message about identical namespace, ID or actions appears_ | New module tried to register a namespace, ID or actions which are already registered by other enabled modules. Disable the conflicting module (mentioned in error message) prior to enabling the new one.  
_Technical error messages appear_ | Report errors to the developer of the module.  
  
#### Developing modules

For information about developing custom modules, see [Developer center](/documentation/current/en/devel/modules).