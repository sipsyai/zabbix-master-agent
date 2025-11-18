---
title: Zabbix server
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_server
downloaded: 2025-11-14 10:46:45
---

# 1 Zabbix server

### Overview

The parameters supported by the Zabbix server configuration file (zabbix_server.conf) are listed in this section.

The parameters are listed without additional information. Click on the parameter to see the full details.

AlertScriptsPath | The location of custom alert scripts.  
---|---  
AllowRoot | Allow the server to run as 'root'.  
AllowSoftwareUpdateCheck | Allow Zabbix UI to receive information about software updates from zabbix.com.  
AllowUnsupportedDBVersions | Allow the server to work with unsupported database versions.  
CacheSize | The size of the configuration cache.  
CacheUpdateFrequency | This parameter determines how often Zabbix will perform the configuration cache update in seconds.  
DBHost | The database host name.  
DBName | The database name.  
DBPassword | The database password.  
DBPort | The database port when not using local socket.  
DBSchema | The database schema name. Used for PostgreSQL.  
DBSocket | The path to the MySQL socket file.  
DBUser | The database user.  
DBTLSConnect | Setting this option to the specified value enforces to use a TLS connection to the database.  
DBTLSCAFile | The full pathname of a file containing the top-level CA(s) certificates for database certificate verification.  
DBTLSCertFile | The full pathname of a file containing the Zabbix server certificate for authenticating to database.  
DBTLSKeyFile | The full pathname of a file containing the private key for authenticating to database.  
DBTLSCipher | The list of encryption ciphers that Zabbix server permits for TLS protocols up through TLS v1.2. Supported only for MySQL.  
DBTLSCipher13 | The list of encryption ciphersuites that Zabbix server permits for the TLS v1.3 protocol. Supported only for MySQL, starting from version 8.0.16.  
DebugLevel | Specify the debug level.  
EnableGlobalScripts | Enable global scripts on Zabbix server.  
ExportDir | The directory for real-time export of events, history and trends in newline-delimited JSON format. If set, enables the real-time export.  
ExportFileSize | The maximum size per export file in bytes.  
ExportType | The list of comma-delimited entity types (events, history, trends) for real-time export (all types by default).  
ExternalScripts | The location of external scripts.  
Fping6Location | The location of fping6.  
FpingLocation | The location of fping.  
FrontendAllowedIP | A comma-separated list of IP addresses or CIDR ranges that are permitted to connect from the frontend.  
HANodeName | The high availability cluster node name.  
HistoryCacheSize | The size of the history cache.  
HistoryIndexCacheSize | The size of the history index cache.  
HistoryStorageDateIndex | Enable preprocessing of history values in history storage to store values in different indices based on date.  
HistoryStorageURL | The history storage HTTP[S] URL.  
HistoryStorageTypes | A comma-separated list of value types to be sent to the history storage.  
HousekeepingFrequency | This parameter determines how often Zabbix will perform the housekeeping procedure in hours.  
Include | You may include individual files or all files in a directory in the configuration file.  
JavaGateway | The IP address (or hostname) of Zabbix Java gateway.  
JavaGatewayPort | The port that Zabbix Java gateway listens on.  
ListenBacklog | The maximum number of pending connections in the TCP queue.  
ListenIP | A list of comma-delimited IP addresses that the trapper should listen on.  
ListenPort | The listen port for trapper.  
LoadModule | The module to load at server startup.  
LoadModulePath | The full path to the location of server modules.  
LogFile | The name of the log file.  
LogFileSize | The maximum size of the log file.  
LogSlowQueries | Determines how long a database query may take before being logged in milliseconds.  
LogType | The type of the log output.  
MaxConcurrentChecksPerPoller | The maximum number of asynchronous checks that can be executed at once by each HTTP agent poller, agent poller or SNMP poller.  
MaxHousekeeperDelete | No more than 'MaxHousekeeperDelete' rows (corresponding to [tablename], [field], [value]) will be deleted per one task in one housekeeping cycle.  
NodeAddress | The IP or hostname with optional port to override how the frontend should connect to the server.  
PidFile | The name of the PID file.  
ProblemHousekeepingFrequency | Determines how often Zabbix will delete problems for deleted triggers.  
ProxyConfigFrequency | Determines how often Zabbix server sends configuration data to a Zabbix proxy.  
ProxyDataFrequency | Determines how often Zabbix server requests history data from a Zabbix proxy.  
ServiceManagerSyncFrequency | Determines how often Zabbix will synchronize the configuration of a service manager.  
SMSDevices | A list of comma-delimited modem files allowed to use Zabbix server.  
SNMPTrapperFile | The temporary file used for passing data from the SNMP trap daemon to the server.  
SocketDir | The directory to store the IPC sockets used by internal Zabbix services.  
SourceIP | The source IP address.  
SSHKeyLocation | The location of public and private keys for SSH checks and actions.  
SSLCertLocation | The location of SSL client certificate files for client authentication.  
SSLKeyLocation | The location of SSL private key files for client authentication.  
SSLCALocation | Override the location of certificate authority (CA) files for SSL server certificate verification.  
StartAgentPollers | The number of pre-forked instances of asynchronous Zabbix agent pollers.  
StartAlerters | The number of pre-forked instances of alerters.  
StartBrowserPollers | The number of pre-forked instances of browser item pollers.  
StartConnectors | The number of pre-forked instances of connector workers.  
StartDBSyncers | The number of pre-forked instances of history syncers.  
StartDiscoverers | The number of pre-forked instances of discovery workers.  
StartEscalators | The number of pre-forked instances of escalators.  
StartHistoryPollers | The number of pre-forked instances of history pollers.  
StartHTTPAgentPollers | The number of pre-forked instances of asynchronous HTTP agent pollers.  
StartHTTPPollers | The number of pre-forked instances of HTTP pollers.  
StartIPMIPollers | The number of pre-forked instances of IPMI pollers.  
StartJavaPollers | The number of pre-forked instances of Java pollers.  
StartLLDProcessors | The number of pre-forked instances of low-level discovery (LLD) workers.  
StartODBCPollers | The number of pre-forked instances of ODBC pollers.  
StartPingers | The number of pre-forked instances of ICMP pingers.  
StartPollersUnreachable | The number of pre-forked instances of pollers for unreachable hosts (including IPMI and Java).  
StartPollers | The number of pre-forked instances of pollers.  
StartPreprocessors | The number of pre-started instances of preprocessing workers.  
StartProxyPollers | The number of pre-forked instances of pollers for passive proxies.  
StartReportWriters | The number of pre-forked instances of report writers.  
StartSNMPPollers | The number of pre-forked instances of asynchronous SNMP pollers.  
StartSNMPTrapper | If set to 1, an SNMP trapper process will be started.  
StartTimers | The number of pre-forked instances of timers.  
StartTrappers | The number of pre-forked instances of trappers.  
StartVMwareCollectors | The number of pre-forked VMware collector instances.  
StatsAllowedIP | A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of external Zabbix instances. The stats request will be accepted only from the addresses listed here.  
Timeout | Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix proxy, agent, web service, and for SNMP checks (except SNMP `walk[OID]` and `get[OID]` items) and `icmpping[*]` item.  
TLSCAFile | The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.  
TLSCertFile | The full pathname of a file containing the server certificate or certificate chain, used for encrypted communications between Zabbix components.  
TLSCipherAll | The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption.  
TLSCipherAll13 | The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption.  
TLSCipherCert | The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate-based encryption.  
TLSCipherCert13 | The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate-based encryption.  
TLSCipherPSK | The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for PSK-based encryption.  
TLSCipherPSK13 | The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for PSK-based encryption.  
TLSCRLFile | The full pathname of a file containing revoked certificates. This parameter is used for encrypted communications between Zabbix components.  
TLSFrontendAccept | What incoming connections to accept from frontend.  
TLSFrontendCertIssuer | Allowed frontend certificate issuer.  
TLSFrontendCertSubject | Allowed frontend certificate subject.  
TLSKeyFile | The full pathname of a file containing the server private key, used for encrypted communications between Zabbix components.  
TLSListen | Controls TLS on the trapper socket.  
TmpDir | The temporary directory.  
TrapperTimeout | Specifies timeout in seconds for:  
\- retrieval of historical data from Zabbix proxy;  
\- sending configuration data to Zabbix proxy;  
\- global script execution or remote command execution on Zabbix server.  
TrendCacheSize | The size of the trend cache.  
TrendFunctionCacheSize | The size of the trend function cache.  
UnavailableDelay | Determines how often host is checked for availability during the unavailability period.  
UnreachableDelay | Determines how often host is checked for availability during the unreachability period.  
UnreachablePeriod | Determines after how many seconds of unreachability treats a host as unavailable.  
User | Drop privileges to a specific, existing user on the system.  
ValueCacheSize | The size of the history value cache.  
Vault | Specifies the vault provider.  
VaultDBPath | Specifies a location, from where database credentials should be retrieved by keys.  
VaultPrefix | Custom prefix for the vault path or query.  
VaultTLSCertFile | The name of the SSL certificate file used for client authentication.  
VaultTLSKeyFile | The name of the SSL private key file used for client authentication.  
VaultToken | The HashiCorp vault authentication token.  
VaultURL | The vault server HTTP[S] URL.  
VMwareCacheSize | The shared memory size for storing VMware data.  
VMwareFrequency | The delay in seconds between data gathering from a single VMware service.  
VMwarePerfFrequency | The delay in seconds between performance counter statistics retrieval from a single VMware service.  
VMwareTimeout | The maximum number of seconds a vmware collector will wait for a response from VMware service.  
WebDriverURL | WebDriver interface HTTP[S] URL.  
WebServiceURL | HTTP[S] URL to Zabbix web service in the format <host:port>/report.  
  
All parameters are non-mandatory unless explicitly stated that the parameter is mandatory.

Note that:

  * The default values reflect daemon defaults, not the values in the shipped configuration files.
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables).
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark).
  * Comments starting with "#" are only supported in the beginning of the line.

### Parameter details

##### AlertScriptsPath

The location of [custom alert scripts](/documentation/current/en/manual/config/notifications/media/script) (depends on the _datadir_ compile-time installation variable).

Default: `/usr/local/share/zabbix/alertscripts`

##### AllowRoot

Allow the server to run as 'root'. If disabled and the server is started by 'root', the server will try to switch to the 'zabbix' user instead. Has no effect if started under a regular user.

Default: `0`  
Values: 0 - do not allow; 1 - allow

##### AllowSoftwareUpdateCheck

Allow Zabbix UI to receive information about software updates from zabbix.com.

Default: `1`  
Values: 0 - do not allow; 1 - allow

##### AllowUnsupportedDBVersions

Allow the server to work with unsupported database versions.

Default: `0`  
Values: 0 - do not allow; 1 - allow

##### CacheSize

The size of the configuration cache, in bytes. The shared memory size for storing host, item and trigger data.

Default: `32M`  
Range: 128K-64G

##### CacheUpdateFrequency

This parameter determines how often Zabbix will perform the configuration cache update in seconds. See also [runtime control](/documentation/current/en/manual/concepts/server#runtime-control) options.

Default: `10`  
Range: 1-3600

##### DBHost

The database host name.  
With MySQL `localhost` or empty string results in using a socket. With PostgreSQL only empty string results in attempt to use socket.

Default: `localhost`

##### DBName

The database name.

Mandatory: Yes

##### DBPassword

The database password. Comment this line if no password is used.

##### DBPort

The database port when not using local socket.**[3](zabbix_server#footnotes)**

Default for MySQL: `3306`

Default for PostgreSQL: `5432`

Range: 1024-65535

##### DBSchema

The database schema name. Used for PostgreSQL.

##### DBSocket

The path to the MySQL socket file.**[3](zabbix_server#footnotes)**

##### DBUser

The database user.

##### DBTLSConnect

Setting this option to the following values enforces to use a TLS connection to the database:  
_required_ \- connect using TLS  
 _verify_ca_ \- connect using TLS and verify certificate  
 _verify_full_ \- connect using TLS, verify certificate and verify that database identity specified by DBHost matches its certificate  
  
With MySQL, starting from 5.7.11, and PostgreSQL the following values are supported: `required`, `verify_ca`, `verify_full`.  
With MariaDB, starting from version 10.2.6, the `required` and `verify_full` values are supported.  
By default not set to any option and the behavior depends on database configuration.

##### DBTLSCAFile

The full pathname of a file containing the top-level CA(s) certificates for database certificate verification.

Mandatory: no (yes, if DBTLSConnect set to _verify_ca_ or _verify_full_)

##### DBTLSCertFile

The full pathname of a file containing the Zabbix server certificate for authenticating to database.

##### DBTLSKeyFile

The full pathname of a file containing the private key for authenticating to database.

##### DBTLSCipher

The list of encryption ciphers that Zabbix server permits for TLS protocols up through TLS v1.2. Supported only for MySQL.

##### DBTLSCipher13

The list of encryption ciphersuites that Zabbix server permits for the TLS v1.3 protocol. Supported only for MySQL, starting from version 8.0.16.

##### DebugLevel

Specify the debug level:  
_0_ \- basic information about starting and stopping of Zabbix processes  
 _1_ \- critical information;  
_2_ \- error information;  
_3_ \- warnings;  
_4_ \- for debugging (produces lots of information);  
_5_ \- extended debugging (produces even more information).  
See also [runtime control](/documentation/current/en/manual/concepts/server#runtime-control) options.

Default: `3`  
Range: 0-5

##### EnableGlobalScripts

Enable global scripts on Zabbix server.  
Note: Global script execution is enabled by default. However, for new installations starting with Zabbix 7.0, EnableGlobalScripts is explicitly set to 0 (disabled).

Default: `1`  
Values: 0 - disable; 1 - enable

##### ExportDir

The directory for [real-time export](/documentation/current/en/manual/config/export/files) of events, history and trends in newline-delimited JSON format. If set, enables the real-time export.

##### ExportFileSize

The maximum size per export file in bytes. Used for rotation if `ExportDir` is set.

Default: `1G`  
Range: 1M-1G

##### ExportType

The list of comma-delimited entity types (events, history, trends) for [real-time export](/documentation/current/en/manual/config/export/files) (all types by default). Valid only if ExportDir is set.  
_Note_ that if ExportType is specified, but ExportDir is not, then this is a configuration error and the server will not start.

Example for history and trends export:
    
    
    ExportType=history,trends

Copy

✔ Copied

Example for event export only:
    
    
    ExportType=events

Copy

✔ Copied

##### ExternalScripts

The location of external scripts (depends on the `datadir` compile-time installation variable).

Default: `/usr/local/share/zabbix/externalscripts`

##### Fping6Location

The location of fping6. Make sure that the fping6 binary has root ownership and the SUID flag set. Make empty ("Fping6Location=") if your fping utility is capable to process IPv6 addresses.

Default: `/usr/sbin/fping6`

##### FpingLocation

The location of fping. Make sure that the fping binary has root ownership and the SUID flag set.

Default: `/usr/sbin/fping`

##### FrontendAllowedIP

A comma-separated list of IP addresses or CIDR ranges that are permitted to connect from the frontend. Frontend connection will be accepted only from the addresses listed here if this parameter is set. By default all connections are accepted for frontend requests If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated equally and '::/0' will allow any IPv4 or IPv6 address. '0.0.0.0/0' can be used to allow any IPv4 address.

Example:
    
    
    FrontendAllowedIP=127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.example.com

Copy

✔ Copied

##### HANodeName

The high availability cluster node name. When empty the server is working in standalone mode and a node with empty name is created.

##### HistoryCacheSize

The size of the history cache, in bytes. The shared memory size for storing history data.

Default: `16M`  
Range: 128K-16G

##### HistoryIndexCacheSize

The size of the history index cache, in bytes. The shared memory size for indexing the history data stored in history cache. The index cache size needs roughly 100 bytes to cache one item.

Default: `4M`  
Range: 128K-16G

##### HistoryStorageDateIndex

Enable preprocessing of history values in history storage to store values in different indices based on date.

Default: `0`  
Values: 0 - disable; 1 - enable

##### HistoryStorageURL

The history storage HTTP[S] URL. This parameter is used for [Elasticsearch](/documentation/current/en/manual/appendix/install/elastic_search_setup) setup.

##### HistoryStorageTypes

A comma-separated list of value types to be sent to the history storage. This parameter is used for [Elasticsearch](/documentation/current/en/manual/appendix/install/elastic_search_setup) setup.

Default: `uint,dbl,str,log,text`

##### HousekeepingFrequency

This parameter determines how often Zabbix will perform the housekeeping procedure in hours. Housekeeping is removing outdated information from the database.  
_Note_ : To prevent housekeeper from being overloaded (for example, when history and trend periods are greatly reduced), no more than 4 times HousekeepingFrequency hours of outdated information are deleted in one housekeeping cycle, for each item. Thus, if HousekeepingFrequency is 1, no more than 4 hours of outdated information (starting from the oldest entry) will be deleted per cycle.  
_Note_ : To lower load on server startup housekeeping is postponed for 30 minutes after server start. Thus, if HousekeepingFrequency is 1, the very first housekeeping procedure after server start will run after 30 minutes, and will repeat with one hour delay thereafter.  
It is possible to disable automatic housekeeping by setting HousekeepingFrequency to 0. In this case the housekeeping procedure can only be started by _housekeeper_execute_ runtime control option and the period of outdated information deleted in one housekeeping cycle is 4 times the period since the last housekeeping cycle, but not less than 4 hours and not greater than 4 days.  
See also [runtime control](/documentation/current/en/manual/concepts/server#runtime-control) options.

Default: `1`  
Range: 0-24

##### Include

You may include individual files or all files in a directory in the configuration file. To only include relevant files in the specified directory, the asterisk wildcard character is supported for pattern matching. See [special notes](special_notes_include) about limitations.

Example:
    
    
    Include=/absolute/path/to/config/files/*.conf

Copy

✔ Copied

##### JavaGateway

The IP address (or hostname) of Zabbix Java gateway. Only required if Java pollers are started.

##### JavaGatewayPort

The port that Zabbix Java gateway listens on.

Default: `10052`  
Range: 1024-32767

##### ListenBacklog

The maximum number of pending connections in the TCP queue.  
The default value is a hard-coded constant, which depends on the system.  
The maximum supported value depends on the system, too high values may be silently truncated to the 'implementation-specified maximum'.

Default: `SOMAXCONN`  
Range: 0 - INT_MAX

##### ListenIP

A list of comma-delimited IP addresses that the trapper should listen on.  
Trapper will listen on all network interfaces if this parameter is missing.

Default: `0.0.0.0`

##### ListenPort

The listen port for trapper.

Default: `10051`  
Range: 1024-32767

##### LoadModule

The module to load at server startup. Modules are used to extend the functionality of the server. The module must be located in the directory specified by LoadModulePath or the path must precede the module name. If the preceding path is absolute (starts with '/') then LoadModulePath is ignored.  
Formats:  
LoadModule=<module.so>  
LoadModule=<path/module.so>  
LoadModule=</abs_path/module.so>  
It is allowed to include multiple LoadModule parameters.

##### LoadModulePath

The full path to the location of server modules. The default depends on compilation options.

##### LogFile

The name of the log file.

Mandatory: Yes, if LogType is set to _file_ ; otherwise no

##### LogFileSize

The maximum size of the log file in MB.  
0 - disable automatic log rotation.  
_Note_ : If the log file size limit is reached and file rotation fails, for whatever reason, the existing log file is truncated and started anew.

Default: `1`  
Range: 0-1024  
Mandatory: Yes, if LogType is set to _file_ ; otherwise no

##### LogSlowQueries

Determines how long a database query may take before being logged in milliseconds.  
0 - don't log slow queries.  
This option becomes enabled starting with DebugLevel=3.

Default: `0`  
Range: 0-3600000

##### LogType

The type of the log output:  
_file_ \- write log to file specified by LogFile parameter;  
_system_ \- write log to syslog;  
_console_ \- write log to standard output.

Default: `file`

##### MaxConcurrentChecksPerPoller

The maximum number of asynchronous checks that can be executed at once by each HTTP agent poller, agent poller or SNMP poller. See StartHTTPAgentPollers, StartAgentPollers, and StartSNMPPollers.

Default: `1000`  
Range: 1-1000

##### MaxHousekeeperDelete

No more than 'MaxHousekeeperDelete' rows (corresponding to [tablename], [field], [value]) will be deleted per one task in one housekeeping cycle.  
If set to 0 then no limit is used at all. In this case you must know what you are doing, so as not to [overload the database!](zabbix_server#footnotes) **[2](zabbix_server#footnotes)**  
This parameter applies only to deleting history and trends of already deleted items.

Default: `5000`  
Range: 0-1000000

##### NodeAddress

IP or hostname with optional port to override how the frontend should connect to the server.  
Format: <address>[:<port>]  
  
If IP or hostname is not set, the value of ListenIP will be used. If ListenIP is not set, the value `localhost` will be used.  
If port is not set, the value of ListenPort will be used. If ListenPort is not set, the value `10051` will be used.  
  
This option can be overridden by the address specified in the frontend configuration.  
  
See also: HANodeName parameter; [Enabling high availability](/documentation/current/en/manual/concepts/server/ha#enabling-high-availability).

Default: `localhost:10051`

##### PidFile

Name of the PID file.

Default: `/tmp/zabbix_server.pid`

##### ProblemHousekeepingFrequency

Determines how often Zabbix will delete problems for deleted triggers in seconds.

Default: `60`  
Range: 1-3600

##### ProxyConfigFrequency

Determines how often Zabbix server sends configuration data to a Zabbix proxy in seconds. Used only for proxies in a passive mode.

Default: `10`  
Range: 1-604800

##### ProxyDataFrequency

Determines how often Zabbix server requests history data from a Zabbix proxy in seconds. Used only for proxies in the passive mode.

Default: `1`  
Range: 1-3600

##### ServiceManagerSyncFrequency

Determines how often Zabbix will synchronize the configuration of a service manager in seconds.

Default: `60`  
Range: 1-3600

##### SMSDevices

A list of comma-delimited modem files allowed to use Zabbix server.  
SMS sending is not possible if this parameter is not set.

Example:
    
    
    SMSDevices=/dev/ttyUSB0,/dev/ttyUSB1

Copy

✔ Copied

##### SNMPTrapperFile

Temporary file used for passing data from the SNMP trap daemon to the server.  
Must be the same as in zabbix_trap_receiver.pl or SNMPTT configuration file.

Default: `/tmp/zabbix_traps.tmp`

##### SocketDir

Directory to store IPC sockets used by internal Zabbix services.

Default: `/tmp`

##### SourceIP

Source IP address for:

  * outgoing connections to Zabbix proxy and Zabbix agent;
  * agentless connections (VMware, SSH, JMX, SNMP, Telnet and simple checks);
  * HTTP agent connections;
  * script item JavaScript HTTP requests;
  * preprocessing JavaScript HTTP requests;
  * sending notification emails (connections to SMTP server);
  * webhook notifications (JavaScript HTTP connections);
  * connections to the Vault

##### SSHKeyLocation

Location of public and private keys for SSH checks and actions.

##### SSLCertLocation

Location of SSL client certificate files for client authentication.  
This parameter is used in web monitoring only.

##### SSLKeyLocation

Location of SSL private key files for client authentication.  
This parameter is used in web monitoring only.

##### SSLCALocation

Override the location of certificate authority (CA) files for SSL server certificate verification. If not set, system-wide directory will be used.  
Note that the value of this parameter will be set as libcurl option CURLOPT_CAPATH. For libcurl versions before 7.42.0, this only has effect if libcurl was compiled to use OpenSSL. For more information see [cURL web page](http://curl.haxx.se/libcurl/c/CURLOPT_CAPATH.html).  
This parameter is used in web monitoring and in SMTP authentication.

##### StartAgentPollers

The number of pre-forked instances of Zabbix agent [pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads). See MaxConcurrentChecksPerPoller.

Default: `1`  
Range: 0-1000

##### StartAlerters

The number of pre-forked instances of [alerters](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).

Default: `3`  
Range: 1-100

##### StartBrowserPollers

The number of pre-forked instances of browser item [pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).

Default: `1`  
Range: 0-1000

##### StartConnectors

The number of pre-forked instances of [connector workers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads). The connector manager process is started automatically when a connector worker is started.

Default: `0`  
Range: 0-1000

##### StartDBSyncers

The number of pre-forked instances of [history syncers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).  
_Note_ : Be careful when changing this value, increasing it may do more harm than good. Roughly, the default value should be enough to handle up to 4000 NVPS.

Default: `4`  
Range: 1-100

##### StartDiscoverers

The number of pre-forked instances of [discovery workers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `5`  
Range: 0-1000

##### StartEscalators

The number of pre-forked instances of [escalators](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).

Default: `1`  
Range: 1-100

##### StartHistoryPollers

The number of pre-forked instances of [history pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).  
Only required for calculated checks.

Default: `5`  
Range: 0-1000

##### StartHTTPAgentPollers

The number of pre-forked instances of HTTP agent [pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads). See MaxConcurrentChecksPerPoller.

Default: `1`  
Range: 0-1000

##### StartHTTPPollers

The number of pre-forked instances of [HTTP pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `1`  
Range: 0-1000

##### StartIPMIPollers

The number of pre-forked instances of [IPMI pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).

Default: `0`  
Range: 0-1000

##### StartJavaPollers

The number of pre-forked instances of [Java pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `0`  
Range: 0-1000

##### StartLLDProcessors

The number of pre-forked instances of low-level discovery (LLD) [workers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.  
The LLD manager process is automatically started when an LLD worker is started.

Default: `2`  
Range: 0-100

##### StartODBCPollers

The number of pre-forked instances of [ODBC pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `1`  
Range: 0-1000

##### StartPingers

The number of pre-forked instances of [ICMP pingers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `1`  
Range: 0-1000

##### StartPollersUnreachable

The number of pre-forked instances of [pollers for unreachable hosts](/documentation/current/en/manual/concepts/server#server-process-types-and-threads) (including IPMI and Java)**[1](zabbix_server#footnotes)**.  
At least one poller for unreachable hosts must be running if regular, IPMI or Java pollers are started.

Default: `1`  
Range: 0-1000

##### StartPollers

The number of pre-forked instances of [pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `5`  
Range: 0-1000

##### StartPreprocessors

The number of pre-started instances of preprocessing [worker](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)** threads should be set to no less than the available CPU core count. More workers should be set if preprocessing is not CPU-bound and has lots of network requests.

Default: `16`  
Range: 1-1000

##### StartProxyPollers

The number of pre-forked instances of [pollers for passive proxies](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.

Default: `1`  
Range: 0-250

##### StartReportWriters

The number of pre-forked instances of [report writers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).  
If set to 0, scheduled report generation is disabled.  
The report manager process is automatically started when a report writer is started.

Default: `0`  
Range: 0-100

##### StartSNMPPollers

The number of pre-forked instances of SNMP [pollers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads). See MaxConcurrentChecksPerPoller.

Default: `1`  
Range: 0-1000

##### StartSNMPTrapper

If set to 1, an [SNMP trapper](/documentation/current/en/manual/concepts/server#server-process-types-and-threads) process will be started.

Default: `0`  
Range: 0-1

##### StartTimers

The number of pre-forked instances of [timers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads).  
Timers process maintenance periods.

Default: `1`  
Range: 1-1000

##### StartTrappers

The number of pre-forked instances of [trappers](/documentation/current/en/manual/concepts/server#server-process-types-and-threads)**[1](zabbix_server#footnotes)**.  
Trappers accept incoming connections from Zabbix sender, active agents and active proxies.

Default: `5`  
Range: 1-1000

##### StartVMwareCollectors

The number of pre-forked [VMware collector](/documentation/current/en/manual/concepts/server#server-process-types-and-threads) instances.

Default: `0`  
Range: 0-250

##### StatsAllowedIP

A list of comma delimited IP addresses, optionally in CIDR notation, or DNS names of external Zabbix instances. Stats request will be accepted only from the addresses listed here. If this parameter is not set no stats requests will be accepted.  
If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated equally and '::/0' will allow any IPv4 or IPv6 address. '0.0.0.0/0' can be used to allow any IPv4 address.

Example:
    
    
    StatsAllowedIP=127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.example.com

Copy

✔ Copied

##### Timeout

Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix proxy, agent, web service, legacy SNMP checks (single OID number or string), and `icmpping[*]` item.  

This parameter defines the duration for various communication operations:

  * remote command execution on Zabbix agent
  * SSH/Telnet command execution
  * requests to Zabbix web service
  * communication timeout for mediatype test request and the `history.push` method
  * rescheduling of items when an IPMI interface becomes unavailable
  * sending response to Zabbix proxy when failing to exchange data due to rights or encryption issues
  * ICMP pinger
  * deadline for IPC asynchronous sockets and runtime control options
  * JMX connections
  * fetching statistics from a remote Zabbix proxy or server
  * sending responses to Zabbix frontend
  * asynchronous poller DNS requests
  * response for active check heartbeat
  * retrieval of Zabbix agent data (values) from active agents
  * retrieval of data from Zabbix sender
  * response when trapper fails to process a request
  * sending active check list to Zabbix agent

This timeout will **not** be used for those checks that have [flexible timeout](/documentation/current/en/manual/config/items/item#item-timeout) settings configured in the frontend (on global, proxy, or per-item level). For example, SNMP `walk[OID]` and `get[OID]` items use the configured timeout from the frontend; legacy SNMP checks still use the server timeout value.

Default: `3`  
Range: 1-30

##### TLSCAFile

The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.

##### TLSCertFile

The full pathname of a file containing the server certificate or certificate chain, used for encrypted communications between Zabbix components.

##### TLSCipherAll

The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption.

Example:
    
    
    TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256

Copy

✔ Copied

##### TLSCipherAll13

The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption.

Example for GnuTLS:
    
    
    NONE:+VERS-TLS1.2:+ECDHE-RSA:+RSA:+ECDHE-PSK:+PSK:+AES-128-GCM:+AES-128-CBC:+AEAD:+SHA256:+SHA1:+CURVE-ALL:+COMP-NULL::+SIGN-ALL:+CTYPE-X.509

Copy

✔ Copied

Example for OpenSSL:
    
    
    EECDH+aRSA+AES128:RSA+aRSA+AES128:kECDHEPSK+AES128:kPSK+AES128

Copy

✔ Copied

##### TLSCipherCert

The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate-based encryption.

Example for GnuTLS:
    
    
    NONE:+VERS-TLS1.2:+ECDHE-RSA:+RSA:+AES-128-GCM:+AES-128-CBC:+AEAD:+SHA256:+SHA1:+CURVE-ALL:+COMP-NULL:+SIGN-ALL:+CTYPE-X.509

Copy

✔ Copied

Example for OpenSSL:
    
    
    EECDH+aRSA+AES128:RSA+aRSA+AES128

Copy

✔ Copied

##### TLSCipherCert13

The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate-based encryption.

##### TLSCipherPSK

The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for PSK-based encryption.

Example for GnuTLS:
    
    
    NONE:+VERS-TLS1.2:+ECDHE-PSK:+PSK:+AES-128-GCM:+AES-128-CBC:+AEAD:+SHA256:+SHA1:+CURVE-ALL:+COMP-NULL:+SIGN-ALL

Copy

✔ Copied

Example for OpenSSL:
    
    
    kECDHEPSK+AES128:kPSK+AES128

Copy

✔ Copied

##### TLSCipherPSK13

The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for PSK-based encryption.

Example:
    
    
    TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256

Copy

✔ Copied

##### TLSCRLFile

The full pathname of a file containing revoked certificates. This parameter is used for encrypted communications between Zabbix components.

##### TLSFrontendAccept

What incoming connections to accept from frontend.

Multiple values can be specified, separated by comma:

  * unencrypted - accept connections without encryption.
  * cert - accept connections secured with TLS and a certificate.

Default: `unencrypted`

##### TLSFrontendCertIssuer

Allowed frontend certificate issuer.

##### TLSFrontendCertSubject

Allowed frontend certificate subject.

##### TLSKeyFile

The full pathname of a file containing the server private key, used for encrypted communications between Zabbix components.

##### TLSListen

Controls TLS on the trapper socket.

Supported values:

  * required - accept only TLS connections

##### TmpDir

The temporary directory.

Default: `/tmp`

##### TrapperTimeout

Specifies timeout in seconds for:

  * retrieval of historical data from Zabbix proxy;
  * sending configuration data to Zabbix proxy;
  * global script execution or remote command execution on Zabbix server.

Default: `300`  
Range: 1-300

##### TrendCacheSize

The size of the trend cache, in bytes.  
The shared memory size for storing trends data.

Default: `4M`  
Range: 128K-16G

##### TrendFunctionCacheSize

The size of the trend function cache, in bytes.  
The shared memory size for caching calculated trend function data.

Default: `4M`  
Range: 128K-2G

##### UnavailableDelay

Determines how often host is checked for availability during the [unavailability](/documentation/current/en/manual/appendix/items/unreachability#unavailable-interface) period in seconds.

Default: `60`  
Range: 1-3600

##### UnreachableDelay

Determines how often host is checked for availability during the [unreachability](/documentation/current/en/manual/appendix/items/unreachability#unreachable-interface) period in seconds.

Default: `15`  
Range: 1-3600

##### UnreachablePeriod

Determines after how many seconds of [unreachability](/documentation/current/en/manual/appendix/items/unreachability#unreachable-interface) treats a host as unavailable.

Default: `45`  
Range: 1-3600

##### User

Drop privileges to a specific, existing user on the system.  
Only has effect if run as 'root' and AllowRoot is disabled.

Default: `zabbix`

##### ValueCacheSize

The size of the history value cache, in bytes.  
The shared memory size for caching item history data requests.  
Setting to 0 disables the value cache (not recommended).  
When the value cache runs out of the shared memory a warning message is written to the server log every 5 minutes.

Default: `8M`  
Range: 0,128K-64G

##### Vault

Specifies the vault provider:  
_HashiCorp_ \- HashiCorp KV Secrets Engine version 2  
 _CyberArk_ \- CyberArk Central Credential Provider  
Must match the vault provider set in the frontend.

Default: `HashiCorp`

##### VaultDBPath

Vault path or query, depending on the Vault, from where credentials for database will be retrieved by keys.

The keys used for [HashiCorp](/documentation/current/en/manual/config/secrets/hashicorp#retrieving-database-credentials) are 'password' and 'username'.

Example path with VaultPrefix=/v1/secret/data/zabbix/:
    
    
    database

Copy

✔ Copied

Example path without VaultPrefix:
    
    
    secret/zabbix/database

Copy

✔ Copied

The keys used for [CyberArk](/documentation/current/en/manual/config/secrets/cyberark#database-credentials) are 'Content' and 'UserName'.

Example:
    
    
    AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix_server_database

Copy

✔ Copied

This option can only be used if DBUser and DBPassword are not specified.

##### VaultPrefix

A custom prefix for Vault path or query, depending on the Vault. The most suitable defaults will be used if not specified.  
Note that 'data' is automatically appended after mountpoint for HashiCorp if VaultPrefix is not specified.

Example prefix for Hashicorp:
    
    
    v1/secret/data/zabbix/

Copy

✔ Copied

Example prefix for Cyberark:
    
    
    /AIMWebService/api/Accounts?

Copy

✔ Copied

##### VaultTLSCertFile

The name of the SSL certificate file used for client authentication  
The certificate file must be in PEM1 format.   
If the certificate file contains also the private key, leave the SSL key file field empty.   
The directory containing this file is specified by the configuration parameter SSLCertLocation.  
This option can be omitted but is recommended for CyberArkCCP vault.

##### VaultTLSKeyFile

The name of the SSL private key file used for client authentication.   
The private key file must be in PEM1 format.   
The directory containing this file is specified by the configuration parameter SSLKeyLocation.   
This option can be omitted but is recommended for CyberArkCCP vault.

##### VaultToken

The HashiCorp Vault authentication token that should have been generated exclusively for Zabbix server with read-only permission to the paths specified in [Vault macros](/documentation/current/en/manual/config/macros/user_macros#configuration) and read-only permission to the path specified in the optional VaultDBPath configuration parameter.  
It is an error if VaultToken and VAULT_TOKEN environment variable are defined at the same time.

Mandatory: Yes, if Vault is set to _HashiCorp_ ; otherwise no

##### VaultURL

The vault server HTTP[S] URL. The system-wide CA certificates directory will be used if SSLCALocation is not specified.

Default: `https://127.0.0.1:8200`

##### VMwareCacheSize

The shared memory size for storing VMware data.  
A VMware internal check zabbix[vmware,buffer,...] can be used to monitor the VMware cache usage (see [Internal checks](/documentation/current/en/manual/config/items/itemtypes/internal)).  
Note that shared memory is not allocated if there are no vmware collector instances configured to start.

Default: `8M`  
Range: 256K-2G

##### VMwareFrequency

The delay in seconds between data gathering from a single VMware service.  
This delay should be set to the least update interval of any VMware monitoring item.

Default: `60`  
Range: 10-86400

##### VMwarePerfFrequency

The delay in seconds between performance counter statistics retrieval from a single VMware service. This delay should be set to the least update interval of any VMware monitoring [item](/documentation/current/en/manual/vm_monitoring/vmware_keys#footnotes) that uses VMware performance counters.

Default: `60`  
Range: 10-86400

##### VMwareTimeout

The maximum number of seconds a vmware collector will wait for a response from VMware service (vCenter or ESX hypervisor).

Default: `10`  
Range: 1-300

##### WebServiceURL

The HTTP[S] URL to Zabbix web service in the format `http[s]://host:port/report`.

Example:
    
    
    WebServiceURL=http://localhost:10053/report

Copy

✔ Copied

Note: the scheme (`http://`) may be omitted only for non-TLS (HTTP) connections; if TLS is configured, `https://` must be used.

##### WebDriverURL

WebDriver interface HTTP[S] URL.

Example (used with Selenium WebDriver standalone server):
    
    
    WebDriverURL=http://localhost:4444

Copy

✔ Copied

#### Footnotes

**1** Note that too many data gathering processes (pollers, unreachable pollers, ODBC pollers, HTTP pollers, Java pollers, pingers, trappers, proxypollers) together with IPMI manager, SNMP trapper, preprocessing workers, and discovery workers can exhaust the per-process file descriptor limit for the preprocessing manager.

Exhausting the file descriptor limit will cause Zabbix server to stop, typically shortly after startup but sometimes taking longer. To avoid such issues, review the [Zabbix server configuration file](/documentation/current/en/manual/appendix/config/zabbix_server) to optimize the number of concurrent checks and processes. Additionally, if necessary, ensure that the file descriptor limit is set sufficiently high by checking and adjusting system limits.

**2** When a lot of items are deleted it increases the load to the database, because the housekeeper will need to remove all the history data that these items had. For example, if we only have to remove 1 item prototype from the template, but this template is linked to 50 hosts and for every host the prototype is expanded to 100 real items, 5000 items in total have to be removed (1*50*100). If 500 is set for MaxHousekeeperDelete (MaxHousekeeperDelete=500), the housekeeper process will have to remove up to 2500000 values (5000*500) for the deleted items from history and trends tables in one cycle.

**3** DBSocket and DBPort are mutually exclusive in server configuration. Specify only one, or leave both undefined.