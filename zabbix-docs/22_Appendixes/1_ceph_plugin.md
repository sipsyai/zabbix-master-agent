---
title: Ceph plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/ceph_plugin
downloaded: 2025-11-14 10:46:52
---

# 1 Ceph plugin

#### Overview

This section lists parameters supported in the Ceph Zabbix agent 2 plugin configuration file (ceph.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.Ceph.Default.ApiKey | no |  |  | Default API key for connecting to Ceph; used if no value is specified in an item key or named session.  
---|---|---|---|---  
Plugins.Ceph.Default.User | no |  |  | Default username for connecting to Ceph; used if no value is specified in an item key or named session.  
Plugins.Ceph.Default.Uri | no |  | https://localhost:8003 | Default URI for connecting to Ceph; used if no value is specified in an item key or named session.   
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Only `https` scheme is supported; a scheme can be omitted.  
A port can be omitted (default=8003).  
Examples: `https://127.0.0.1:8003`  
`localhost`  
Plugins.Ceph.InsecureSkipVerify | no | false / true | false | Determines whether an http client should verify the server's certificate chain and host name.  
If _true_ , TLS accepts any certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks (should be used only for testing).  
Plugins.Ceph.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.Ceph.Sessions.<SessionName>.ApiKey | no |  |  | Named session API key.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Ceph.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Ceph.Sessions.<SessionName>.Uri | no |  |  | Connection string of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Only `https` scheme is supported; a scheme can be omitted.  
A port can be omitted (default=8003).  
Examples: `https://127.0.0.1:8003`  
`localhost`  
Plugins.Ceph.Timeout | no | 1-30 | global timeout | Request execution timeout (the duration, in seconds, to wait for a request to complete before shutting it down).  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)