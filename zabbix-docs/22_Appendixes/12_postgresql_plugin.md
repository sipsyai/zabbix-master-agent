---
title: PostgreSQL plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/postgresql_plugin
downloaded: 2025-11-14 10:47:03
---

# 12 PostgreSQL plugin

#### Overview

This section lists parameters supported in the PostgreSQL Zabbix agent 2 plugin configuration file (postgresql.conf).

The PostgreSQL plugin is a loadable plugin and is available and fully described in the [PostgreSQL plugin repository](https://git.zabbix.com/projects/AP/repos/postgresql/browse).

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

Plugins.PostgreSQL.Default.CacheMode | no |  | prepare | Cache mode for the PostgreSQL connection.  
Supported values:  
_prepare_ (default) - will create prepared statements on the PostgreSQL server;  
_describe_ \- will use the anonymous prepared statement to describe a statement without creating a statement on the server.  
Note that "describe" is primarily useful when the environment does not allow prepared statements such as when running a connection pooler like PgBouncer.  
---|---|---|---|---  
Plugins.PostgreSQL.CallTimeout | no | 1-30 | global timeout | Maximum wait time (in seconds) for a request to be completed.  
Plugins.PostgreSQL.CustomQueriesPath | no |  | `/usr/local/share/zabbix/custom-queries/postgreSQL` for Unix systems  
  
`*:\Program Files\Zabbix Agent 2\Custom Queries\PostgreSQL` for Windows systems, where `*` is the drive name from the `ProgramFiles` environment variable | Full pathname of a directory containing `.sql` files with custom queries.  
Plugins.PostgreSQL.CustomQueriesEnabled | no |  | false | If set, enables the execution of the `postgresql.custom.query` item key. If disabled, no queries will be loaded from the custom query directory path.  
Plugins.PostgreSQL.Default.Database | no |  |  | Default database for connecting to PostgreSQL; used if no value is specified in an item key or named session.  
Plugins.PostgreSQL.Default.Password | no |  |  | Default password for connecting to PostgreSQL; used if no value is specified in an item key or named session.  
Plugins.PostgreSQL.Default.TLSCAFile | no  
(yes, if Plugins.PostgreSQL.Default.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the top-level CA(s) certificate for peer certificate verification for encrypted communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Plugins.PostgreSQL.Default.TLSCertFile | no  
(yes, if Plugins.PostgreSQL.Default.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the PostgreSQL certificate or certificate chain for encrypted communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Plugins.PostgreSQL.Default.TLSConnect | no |  |  | Encryption type for communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Supported values:  
_required_ \- connect using TLS as transport mode without identity checks;  
_verify_ca_ \- connect using TLS and verify certificate;  
_verify_full_ \- connect using TLS, verify certificate and verify that database identity (CN) specified by DBHost matches its certificate.  
Undefined encryption type means unencrypted connection.  
Plugins.PostgreSQL.Default.TLSKeyFile | no  
(yes, if Plugins.PostgreSQL.Default.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the PostgreSQL private key for encrypted communications between Zabbix agent 2 and monitored databases; used if no value is specified in a named session.  
Plugins.PostgreSQL.Default.Uri | no |  |  | Default URI for connecting to PostgreSQL; used if no value is specified in an item key or named session.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`.  
Examples: `tcp://127.0.0.1:5432`  
`tcp://localhost`  
`unix:/var/run/postgresql/.s.PGSQL.5432`  
Plugins.PostgreSQL.Default.User | no |  |  | Default username for connecting to PostgreSQL; used if no value is specified in an item key or named session.  
Plugins.PostgreSQL.KeepAlive | no | 60-900 | 300 | Maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.PostgreSQL.Sessions.<SessionName>.CacheMode | no |  | prepare | Cache mode for the PostgreSQL connection.  
**< SessionName>** \- define name of a session for using in item keys.  
Supported values:  
_prepare_ (default) - will create prepared statements on the PostgreSQL server;  
_describe_ \- will use the anonymous prepared statement to describe a statement without creating a statement on the server.  
Note that "describe" is primarily useful when the environment does not allow prepared statements such as when running a connection pooler like PgBouncer.  
Plugins.PostgreSQL.Sessions.<SessionName>.Database | no |  |  | Database for session connection.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.PostgreSQL.Sessions.<SessionName>.Password | no | Must match the password format. |  | Password for session connection.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.PostgreSQL.Sessions.<SessionName>.TLSCAFile | no  
(yes, if Plugins.PostgreSQL.Sessions.<SessionName>.TLSConnect is set to _verify_ca_ or _verify_full_) |  |  | Full pathname of a file containing the top-level CA(s) certificate peer certificate verification.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.PostgreSQL.Sessions.<SessionName>.TLSCertFile | yes, if Plugins.PostgreSQL.Sessions.<SessionName>.TLSKeyFile is specified |  |  | Full pathname of a file containing the PostgreSQL certificate or certificate chain.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.PostgreSQL.Sessions.<SessionName>.TLSConnect | no |  |  | Encryption type for PostgreSQL connection.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Supported values:  
_required_ \- connect using TLS as transport mode without identity checks;  
_verify_ca_ \- connect using TLS and verify certificate;  
_verify_full_ \- connect using TLS, verify certificate and verify that database identity (CN) specified by DBHost matches its certificate.  
Undefined encryption type means unencrypted connection.  
Plugins.PostgreSQL.Sessions.<SessionName>.TLSKeyFile | yes, if Plugins.PostgreSQL.Sessions.<SessionName>.TLSCertFile is specified |  |  | Full pathname of a file containing the PostgreSQL private key.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.PostgreSQL.Sessions.<SessionName>.Uri | no |  |  | Connection string of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`.  
Examples: `tcp://127.0.0.1:5432`  
`tcp://localhost`  
`unix:/var/run/postgresql/.s.PGSQL.5432`  
Plugins.PostgreSQL.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.PostgreSQL.System.Path | yes |  |  | Path to the PostgreSQL plugin executable.  
Example usage: `Plugins.PostgreSQL.System.Path=/usr/libexec/zabbix/zabbix-agent2-plugin-postgresql`  
Plugins.PostgreSQL.Timeout | no | 1-30 | global timeout | Request execution timeout (the duration, in seconds, to wait for a request to complete before shutting it down).  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)