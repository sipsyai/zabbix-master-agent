---
title: Oracle plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/oracle_plugin
downloaded: 2025-11-14 10:47:02
---

# 11 Oracle plugin

#### Overview

This section lists parameters supported in the Oracle Zabbix agent 2 plugin configuration file (oracle.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.Oracle.CallTimeout | no | 1-30 | global timeout | The maximum wait time in seconds for a request to be completed.  
---|---|---|---|---  
Plugins.Oracle.ConnectTimeout | no | 1-30 | global timeout | The maximum wait time in seconds for a connection to be established.  
Plugins.Oracle.CustomQueriesPath | no |  | `/usr/local/share/zabbix/custom-queries/oracle` for Unix systems  
  
`*:\Program Files\Zabbix Agent 2\Custom Queries\Oracle` for Windows systems, where `*` is the drive name from the `ProgramFiles` environment variable | Full pathname of a directory containing `.sql` files with custom queries.  
Example: `/etc/zabbix/oracle/sql`  
Plugins.Oracle.CustomQueriesEnabled | no |  | false | If set, enables the execution of the `oracle.custom.query` item key. If disabled, no queries will be loaded from the custom query directory path.  
Plugins.Oracle.Default.Password | no |  |  | Default password for connecting to Oracle; used if no value is specified in an item key or named session.  
Plugins.Oracle.Default.Service | no |  |  | Default service name for connecting to Oracle (SID is not supported); used if no value is specified in an item key or named session.  
Plugins.Oracle.Default.Uri | no |  | tcp://localhost:1521 | Default URI for connecting to Oracle; used if no value is specified in an item key or named session.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Only `tcp` scheme is supported; a scheme can be omitted.  
A port can be omitted (default=1521).  
Since **Zabbix 7.4.3** it is also possible to specify the TNS key or TNS value as the connection string. The TNS value must be composed without whitespaces.  
Examples: `tcp://127.0.0.1:1521`  
`localhost`  
`zbx_tns_example` (TNS key)  
`(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=xe)))` (TNS value)  
Plugins.Oracle.Default.User | no |  |  | Default username for connecting to Oracle; used if no value is specified in an item key or named session.  
Plugins.Oracle.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.Oracle.ResolveTNS | no | true / false | false | The option specifies how to interpret connection string (ConnString) in metrics key 'commonParams' to connect to Oracle server.  
If it is set to false the default schema and port will be added to ConnString (if absent). If the option is set to true, the default schema and port will be omitted (unless explicitly specified in ConnString), and ConnString will be passed to Oracle client as is. If Oracle client finds ConnString in tnsnames.ora file, the connection description found will be used to connect to Oracle server.  
This parameter is supported since Zabbix 7.4.3.  
Plugins.Oracle.Sessions.<SessionName>.Password | no |  |  | Named session password.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Oracle.Sessions.<SessionName>.Service | no |  |  | Named session service name to be used for connection (SID is not supported).  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Oracle.Sessions.<SessionName>.Uri | no |  |  | Named session connection string for Oracle.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Only `tcp` scheme is supported; a scheme can be omitted.  
A port can be omitted (default=1521).  
Since **Zabbix 7.4.3** it is also possible to specify the TNS key or TNS value as the connection string. The TNS value must be composed without whitespaces.  
Examples: `tcp://127.0.0.1:1521`  
`localhost`  
`zbx_tns_example` (TNS key)  
`(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=xe)))` (TNS value)  
Plugins.Oracle.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)