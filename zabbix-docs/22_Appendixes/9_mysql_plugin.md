---
title: MySQL plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mysql_plugin
downloaded: 2025-11-14 10:47:00
---

# 9 MySQL plugin

#### Overview

This section lists parameters supported in the MySQL Zabbix agent 2 plugin configuration file (mysql.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.Mysql.CallTimeout | no | 1-30 | global timeout | The maximum amount of time in seconds to wait for a request to be done.  
---|---|---|---|---  
Plugins.Mysql.CustomQueriesPath | no |  | `/usr/local/share/zabbix/custom-queries/mysql` for Unix systems  
  
`*:\Program Files\Zabbix Agent 2\Custom Queries\Mysql` for Windows systems, where `*` is the drive name from the `ProgramFiles` environment variable | Full pathname of a directory containing `.sql` files with custom queries.  
Plugins.Mysql.CustomQueriesEnabled | no |  | false | If set, enables the execution of the `mysql.custom.query` item key. If disabled, no queries will be loaded from the custom query directory path.  
Plugins.Mysql.Default.Password | no |  |  | Default password for connecting to MySQL; used if no value is specified in an item key or named session.  
Plugins.Mysql.Default.TLSCAFile | no  
(yes, if Plugins.Mysql.Default.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification for encrypted communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Plugins.Mysql.Default.TLSCertFile | no  
(yes, if Plugins.Mysql.Default.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the agent certificate or certificate chain for encrypted communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Plugins.Mysql.Default.TLSConnect | no |  |  | Encryption type for communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
  
Supported values:  
_required_ \- require TLS connection;  
_verify_ca_ \- verify certificates;  
_verify_full_ \- verify certificates and IP address.  
Plugins.Mysql.Default.TLSKeyFile | no  
(yes, if Plugins.Mysql.Default.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the database private key for encrypted communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Plugins.Mysql.Default.Uri | no |  | tcp://localhost:3306 | Default URI for connecting to MySQL; used if no value is specified in an item key or named session.   
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`; a scheme can be omitted.  
A port can be omitted (default=3306).  
Examples: `tcp://localhost:3306`  
`localhost`  
`unix:/var/run/mysql.sock`  
Plugins.Mysql.Default.User | no |  |  | Default username for connecting to MySQL; used if no value is specified in an item key or named session.  
Plugins.Mysql.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.Mysql.Sessions.<SessionName>.Password | no |  |  | Named session password.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Mysql.Sessions.<SessionName>.TLSCAFile | no  
(yes, if Plugins.Mysql.Sessions.<SessionName>.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Mysql.Sessions.<SessionName>.TLSCertFile | yes, if Plugins.Mysql.Sessions.<SessionName>.TLSKeyFile is specified |  |  | Full pathname of a file containing the agent certificate or certificate chain, used for encrypted communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Mysql.Sessions.<SessionName>.TLSConnect | no |  |  | Encryption type for communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Supported values:  
_required_ \- require TLS connection;  
_verify_ca_ \- verify certificates;  
_verify_full_ \- verify certificates and IP address.  
Plugins.Mysql.Sessions.<SessionName>.TLSKeyFile | yes, if Plugins.Mysql.Sessions.<SessionName>.TLSCertFile is specified |  |  | Full pathname of a file containing the database private key used for encrypted communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Mysql.Sessions.<SessionName>.Uri | no |  |  | Connection string of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`; a scheme can be omitted.  
A port can be omitted (default=3306).  
Examples: `tcp://localhost:3306`  
`localhost`  
`unix:/var/run/mysql.sock`  
Plugins.Mysql.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.Mysql.Timeout | no | 1-30 | global timeout | The maximum time in seconds for waiting when a connection has to be established.  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)