---
title: Module object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/module/object
downloaded: 2025-11-14 10:43:33
---

# Module object

The following objects are directly related to the `module` API.

### Module

The module object has the following properties.

moduleid | ID | ID of the module as stored in the database.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
id | string | Unique module ID as defined by a developer in the [manifest.json](/documentation/current/en/manual/extensions/frontendmodules#reference) file of the module.  
  
Possible values for built-in modules:  
see property "type" description in [Dashboard widget](/documentation/current/en/manual/api/reference/dashboard/object#dashboard-widget).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
relative_path | string | Path to the directory of the module relative to the directory of the Zabbix frontend.  
  
Possible values:  
`widgets/*` \- for built-in widget modules;  
`modules/*` \- for third-party modules.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
status | integer | Whether the module is enabled or disabled.  
  
Possible values:  
0 - _(default)_ Disabled;  
1 - Enabled.  
config | object | [Module configuration](/documentation/current/en/manual/extensions/frontendmodules#reference).