---
title: Modbus plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/modbus_plugin
downloaded: 2025-11-14 10:46:56
---

# 5 Modbus plugin

#### Overview

This section lists parameters supported in the Modbus Zabbix agent 2 plugin configuration file (modbus.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.Modbus.Sessions.<SessionName>.Endpoint | no |  |  | Endpoint is a connection string consisting of a protocol scheme, a host address and a port or serial port name and attributes.  
**< SessionName>** \- define name of a session for using in item keys.  
---|---|---|---|---  
Plugins.Modbus.Sessions.<SessionName>.SlaveID | no |  |  | Slave ID of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
Example: `Plugins.Modbus.Sessions.MB1.SlaveID=20`  
 _Note_ that this named session parameter is checked only if the value provided in the [item key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#modbus) slave ID parameter is empty.  
Plugins.Modbus.Sessions.<SessionName>.Timeout | no |  |  | Timeout of a named session in seconds.  
**< SessionName>** \- define name of a session for using in item keys.  
Example: `Plugins.Modbus.Sessions.MB1.Timeout=2`  
  
If you need to set the request execution timeout (how long to wait for a request to complete before shutting it down), use the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form.

See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)