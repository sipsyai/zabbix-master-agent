---
title: Memcached plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/memcached_plugin
downloaded: 2025-11-14 10:46:55
---

# 4 Memcached plugin

#### Overview

This section lists parameters supported in the Memcached Zabbix agent 2 plugin configuration file (memcached.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.Memcached.Default.Password | no |  |  | Default password for connecting to Memcached; used if no value is specified in an item key or named session.  
---|---|---|---|---  
Plugins.Memcached.Default.Uri | no |  | tcp://localhost:11211 | Default URI for connecting to Memcached; used if no value is specified in an item key or named session.   
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`; a scheme can be omitted.  
A port can be omitted (default=11211).  
Examples: `tcp://localhost:11211`  
`localhost`  
`unix:/var/run/memcached.sock`  
Plugins.Memcached.Default.User | no |  |  | Default username for connecting to Memcached; used if no value is specified in an item key or named session.  
Plugins.Memcached.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.Memcached.Sessions.<SessionName>.Password | no |  |  | Named session password.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Memcached.Sessions.<SessionName>.Uri | no |  |  | Connection string of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`; a scheme can be omitted.  
A port can be omitted (default=11211).  
Examples: `tcp://localhost:11211`  
`localhost`  
`unix:/var/run/memcached.sock`  
Plugins.Memcached.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Memcached.Timeout | no | 1-30 | global timeout | Request execution timeout (the duration, in seconds, to wait for a request to complete before shutting it down).  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)