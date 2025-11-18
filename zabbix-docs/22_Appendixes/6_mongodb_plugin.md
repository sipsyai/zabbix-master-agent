---
title: MongoDB plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mongodb_plugin
downloaded: 2025-11-14 10:46:57
---

# 6 MongoDB plugin

#### Overview

This section lists parameters supported in the MongoDB Zabbix agent 2 plugin configuration file (mongo.conf).

The MongoDB plugin is a loadable plugin and is available and fully described in the [MongoDB plugin repository](https://git.zabbix.com/projects/AP/repos/mongodb/browse).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files.
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark).
  * Comments starting with "#" are only supported at the beginning of the line.

#### Options

-V --version | Print the plugin version and license information.  
---|---  
-h --help | Print help information (shorthand).  
  
#### Parameters

Plugins.MongoDB.Default.Password | no |  |  | Default password for connecting to MongoDB; used if no value is specified in an item key or named session.  
---|---|---|---|---  
Plugins.MongoDB.Default.Uri | no |  |  | Default URI for connecting to MongoDB; used if no value is specified in an item key or named session.   
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Only `tcp` scheme is supported; a scheme can be omitted.  
A port can be omitted (default=27017).  
Examples: `tcp://127.0.0.1:27017`, `tcp:localhost`, `localhost`  
Plugins.MongoDB.Default.User | no |  |  | Default username for connecting to MongoDB; used if no value is specified in an item key or named session.  
Plugins.MongoDB.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.MongoDB.Sessions.<SessionName>.Password | no |  |  | Named session password.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MongoDB.Sessions.<SessionName>.TLSCAFile | no   
(yes, if Plugins.MongoDB.Sessions.<SessionName>.TLSConnect is set to one of: verify_ca, verify_full) |  |  | Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MongoDB.Sessions.<SessionName>.TLSCertFile | yes, if Plugins.MongoDB.Sessions.<SessionName>.TLSKeyFile is specified |  |  | Full pathname of a file containing the agent certificate or certificate chain, used for encrypted communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MongoDB.Sessions.<SessionName>.TLSConnect | no |  |  | Encryption type for communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Supported values:  
_required_ \- require TLS connection;  
_verify_ca_ \- verify certificates;  
_verify_full_ \- verify certificates and IP address.   
  
Supported since plugin version 1.2.1  
Plugins.MongoDB.Sessions.<SessionName>.TLSKeyFile | yes, if Plugins.MongoDB.Sessions.<SessionName>.TLSCertFile is specified |  |  | Full pathname of a file containing the database private key used for encrypted communications between Zabbix agent 2 and monitored databases.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MongoDB.Sessions.<SessionName>.Uri | no |  |  | Connection string of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Only `tcp` scheme is supported; a scheme can be omitted.  
A port can be omitted (default=27017).  
Examples: `tcp://127.0.0.1:27017`, `tcp:localhost`, `localhost`  
Plugins.MongoDB.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MongoDB.System.Path | no |  |  | Path to the MongoDB plugin executable.  
Example usage: `Plugins.MongoDB.System.Path=/usr/libexec/zabbix/zabbix-agent2-plugin-mongodb`  
Plugins.MongoDB.Timeout | no | 1-30 | global timeout | Request execution timeout (the duration, in seconds, to wait for a request to complete before shutting it down).  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)