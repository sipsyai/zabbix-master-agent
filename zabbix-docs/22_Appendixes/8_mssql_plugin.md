---
title: MSSQL plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mssql_plugin
downloaded: 2025-11-14 10:46:59
---

# 8 MSSQL plugin

#### Overview

This section lists parameters supported in the MSSQL Zabbix agent 2 plugin configuration file (mssql.conf).

The MSSQL plugin is a loadable plugin and is available and fully described in the [MSSQL plugin repository](https://git.zabbix.com/projects/AP/repos/mssql/browse).

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

Plugins.MSSQL.CustomQueriesDir | no |  | `/usr/local/share/zabbix/custom-queries/mssql` for Unix systems  
  
`*:\Program Files\Zabbix Agent 2\Custom Queries\MSSQL` for Windows systems, where `*` is the drive name from the `ProgramFiles` environment variable | Specifies the file path to a directory containing user-defined .sql files with custom queries that the plugin can execute. The plugin loads all available .sql files in the configured directory at startup. This means that any changes to the custom query files will not be reflected until the plugin is restarted. The plugin is started and stopped together with Zabbix agent 2.  
---|---|---|---|---  
Plugins.MSSQL.CustomQueriesEnabled | no |  | false | If set, enables the execution of the `mssql.custom.query` item key. If disabled, no queries will be loaded from the custom query directory path.  
Plugins.MSSQL.Default.CACertPath | no |  |  | The default file path to the public key certificate of the certificate authority (CA) that issued the certificate of the MSSQL server. The certificate must be in PEM format.  
Plugins.MSSQL.Default.Database | no |  |  | The default database name to connect to.  
Plugins.MSSQL.Default.Encrypt | no |  |  | Specifies the default connection encryption type. Possible values are:  
_true_ \- data sending between plugin and server is encrypted;  
_false_ \- data sending between plugin and server is not encrypted beyond the login packet;  
_strict_ \- data sending between plugin and server is encrypted E2E using [TDS8](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/tds-8?view=sql-server-ver16);  
_disable_ \- data sending between plugin and server is not encrypted.  
Plugins.MSSQL.Default.HostNameInCertificate | no |  |  | The common name (CN) of the certificate of the MSSQL server by default.  
Plugins.MSSQL.Default.Password | no |  |  | The password to be sent to a protected MSSQL server by default.  
Plugins.MSSQL.Default.TLSMinVersion | no |  |  | The minimum TLS version to use by default. Possible values are: `1.0`, `1.1`, `1.2`, `1.3`.  
Plugins.MSSQL.Default.TrustServerCertificate | no |  |  | Whether the plugin should trust the server certificate without validating it by default. Possible values: `true`, `false`.  
Plugins.MSSQL.Default.Uri | no |  | sqlserver://localhost:1433 | The default URI to connect. The only supported schema is `sqlserver://`. A schema can be omitted. Embedded credentials will be ignored.  
Plugins.MSSQL.Default.User | no |  |  | The default username to be sent to a protected MSSQL server.  
Plugins.MSSQL.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.MSSQL.Sessions.<SessionName>.CACertPath | no |  |  | The file path to the public key certificate of the certificate authority (CA) that issued the certificate of the MSSQL server for the named session. The certificate must be in PEM format.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.Database | no |  |  | The database name to connect to for the named session.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.Encrypt | no |  |  | Specifies the connection encryption type for the named session. Possible values are:  
_true_ \- data sending between plugin and server is encrypted;  
_false_ \- data sending between plugin and server is not encrypted beyond the login packet;  
_strict_ \- data sending between plugin and server is encrypted E2E using [TDS8](https://learn.microsoft.com/en-us/sql/relational-databases/security/networking/tds-8?view=sql-server-ver16);  
_disable_ \- data sending between plugin and server is not encrypted.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.HostNameInCertificate | no |  |  | The common name (CN) of the certificate of the MSSQL server for the named session.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.Password | no |  |  | The password to be sent to a protected MSSQL server for the named session.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.TLSMinVersion | no |  |  | The minimum TLS version to use for the named session. Possible values are: `1.0`, `1.1`, `1.2`, `1.3`.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.TrustServerCertificate | no |  |  | Whether the plugin should trust the server certificate without validating it for the named session. Possible values: `true`, `false`.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.Uri | no |  | sqlserver://localhost:1433 | The URI to connect, for the named session. The only supported schema is `sqlserver://`. A schema can be omitted. Embedded credentials will be ignored.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.Sessions.<SessionName>.User | no |  |  | The username to be sent to a protected MSSQL server for the named session.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MSSQL.System.Path | no |  |  | Path to the MSSQL plugin executable.  
Global setting for the MSSQL plugin. Applied to all connections.  
Example usage: `Plugins.MSSQL.System.Path=/usr/libexec/zabbix/zabbix-agent2-plugin-mssql`  
Plugins.MSSQL.Timeout | no | 1-30 | global timeout | The duration, in seconds, to wait for a server to respond when first connecting and on follow-up operations in the session.  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)