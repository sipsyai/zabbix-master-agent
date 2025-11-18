---
title: Zabbix proxy
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_proxy
downloaded: 2025-11-14 10:46:46
---

# 2 Zabbix proxy

### Overview

The parameters supported by the Zabbix proxy configuration file (zabbix_proxy.conf) are listed in this section.

The parameters are listed without additional information. Click on the parameter to see the full details.

AllowRoot | Allow the proxy to run as 'root'.  
---|---  
AllowUnsupportedDBVersions | Allow the proxy to work with unsupported database versions.  
CacheSize | The size of the configuration cache.  
ConfigFrequency | This parameter is **deprecated** (use ProxyConfigFrequency instead).  
How often the proxy retrieves configuration data from Zabbix server in seconds.  
DataSenderFrequency | The proxy will send collected data to the server every N seconds.  
DBHost | The database host name.  
DBName | The database name or path to the database file for SQLite3.  
DBPassword | The database password.  
DBPort | The database port when not using local socket.  
DBSchema | The database schema name. Used for PostgreSQL.  
DBSocket | The path to the MySQL socket file.  
DBUser | The database user.  
DBTLSConnect | Setting this option to the specified value enforces to use a TLS connection to the database.  
DBTLSCAFile | The full pathname of a file containing the top-level CA(s) certificates for database certificate verification.  
DBTLSCertFile | The full pathname of a file containing the Zabbix proxy certificate for authenticating to database.  
DBTLSKeyFile | The full pathname of a file containing the private key for authenticating to database.  
DBTLSCipher | The list of encryption ciphers that Zabbix proxy permits for TLS protocols up through TLS v1.2. Supported only for MySQL.  
DBTLSCipher13 | The list of encryption ciphersuites that Zabbix proxy permits for the TLS v1.3 protocol. Supported only for MySQL, starting from version 8.0.16.  
DebugLevel | The debug level.  
EnableRemoteCommands | Whether remote commands from Zabbix server are allowed.  
ExternalScripts | The location of external scripts.  
Fping6Location | The location of fping6.  
FpingLocation | The location of fping.  
HistoryCacheSize | The size of the history cache.  
HistoryIndexCacheSize | The size of the history index cache.  
Hostname | A unique, case sensitive proxy name.  
HostnameItem | The item used for setting Hostname if it is undefined.  
HousekeepingFrequency | How often Zabbix will perform the housekeeping procedure in hours.  
Include | You may include individual files or all files in a directory in the configuration file.  
JavaGateway | The IP address (or hostname) of Zabbix Java gateway.  
JavaGatewayPort | The port that Zabbix Java gateway listens on.  
ListenBacklog | The maximum number of pending connections in the TCP queue.  
ListenIP | A list of comma-delimited IP addresses that the trapper should listen on.  
ListenPort | The listen port for trapper.  
LoadModule | The module to load at proxy startup.  
LoadModulePath | The full path to the location of proxy modules.  
LogFile | The name of the log file.  
LogFileSize | The maximum size of the log file.  
LogRemoteCommands | Enable logging of executed shell commands as warnings.  
LogSlowQueries | How long a database query may take before being logged.  
LogType | The type of the log output.  
MaxConcurrentChecksPerPoller | The maximum number of asynchronous checks that can be executed at once by each HTTP agent poller, agent poller or SNMP poller.  
PidFile | The name of the PID file.  
ProxyBufferMode | Specifies history, discovery and autoregistration data storage mechanism (disk/memory/hybrid).  
ProxyConfigFrequency | How often the proxy retrieves configuration data from Zabbix server in seconds.  
ProxyLocalBuffer | The proxy will keep data locally for N hours, even if the data have already been synced with the server.  
ProxyMemoryBufferAge | The maximum age of data in proxy memory buffer in seconds.  
ProxyMemoryBufferSize | The size of shared memory cache for collected history, discovery and auto registration data.  
ProxyMode | The proxy operating mode (active/passive).  
ProxyOfflineBuffer | The proxy will keep data for N hours in case of no connectivity with Zabbix server.  
Server | If ProxyMode is set to active mode: Zabbix server IP address or DNS name (address:port) or cluster (address:port;address2:port) to get configuration data from and send data to.  
If ProxyMode is set to passive mode: List of comma delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix server.  
SNMPTrapperFile | The temporary file used for passing data from the SNMP trap daemon to the proxy.  
SocketDir | The directory to store the IPC sockets used by internal Zabbix services.  
SourceIP | The source IP address.  
SSHKeyLocation | The location of public and private keys for SSH checks and actions.  
SSLCertLocation | The location of SSL client certificate files for client authentication.  
SSLKeyLocation | The location of SSL private key files for client authentication.  
SSLCALocation | Override the location of certificate authority (CA) files for SSL server certificate verification.  
StartAgentPollers | The number of pre-forked instances of asynchronous Zabbix agent pollers.  
StartBrowserPollers | The number of pre-forked instances of browser item pollers.  
StartDBSyncers | The number of pre-forked instances of history syncers.  
StartDiscoverers | The number of pre-forked instances of discovery workers.  
StartHTTPAgentPollers | The number of pre-forked instances of asynchronous HTTP agent pollers.  
StartHTTPPollers | The number of pre-forked instances of HTTP pollers.  
StartIPMIPollers | The number of pre-forked instances of IPMI pollers.  
StartJavaPollers | The number of pre-forked instances of Java pollers.  
StartODBCPollers | The number of pre-forked instances of ODBC pollers.  
StartPingers | The number of pre-forked instances of ICMP pingers.  
StartPollersUnreachable | The number of pre-forked instances of pollers for unreachable hosts (including IPMI and Java).  
StartPollers | The number of pre-forked instances of pollers.  
StartPreprocessors | The number of pre-started instances of preprocessing workers.  
StartSNMPPollers | The number of pre-forked instances of asynchronous SNMP pollers.  
StartSNMPTrapper | If set to 1, an SNMP trapper process will be started.  
StartTrappers | The number of pre-forked instances of trappers.  
StartVMwareCollectors | The number of pre-forked VMware collector instances.  
StatsAllowedIP | A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of external Zabbix instances. The stats request will be accepted only from the addresses listed here.  
Timeout | Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix proxy, agent, web service, and for SNMP checks (except SNMP `walk[OID]` and `get[OID]` items) and `icmpping[*]` item.  
TLSAccept | What incoming connections to accept from Zabbix server.  
TLSCAFile | The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.  
TLSCertFile | The full pathname of a file containing the server certificate or certificate chain, used for encrypted communications between Zabbix components.  
TLSCipherAll | The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption.  
TLSCipherAll13 | The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate- and PSK-based encryption.  
TLSCipherCert | The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for certificate-based encryption.  
TLSCipherCert13 | The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for certificate-based encryption.  
TLSCipherPSK | The GnuTLS priority string or OpenSSL (TLS 1.2) cipher string. Override the default ciphersuite selection criteria for PSK-based encryption.  
TLSCipherPSK13 | The cipher string for OpenSSL 1.1.1 or newer in TLS 1.3. Override the default ciphersuite selection criteria for PSK-based encryption.  
TLSConnect | How the proxy should connect to Zabbix server.  
TLSCRLFile | The full pathname of a file containing revoked certificates. This parameter is used for encrypted communications between Zabbix components.  
TLSKeyFile | The full pathname of a file containing the proxy private key, used for encrypted communications between Zabbix components.  
TLSListen | Controls TLS on the trapper socket.  
TLSPSKFile | The full pathname of a file containing the proxy pre-shared key, used for encrypted communications with Zabbix server.  
TLSPSKIdentity | The pre-shared key identity string, used for encrypted communications with Zabbix server.  
TLSServerCertIssuer | The allowed server certificate issuer.  
TLSServerCertSubject | The allowed server certificate subject.  
TmpDir | The temporary directory.  
TrapperTimeout | Specifies timeout in seconds for:   
\- retrieval of configuration data from the Zabbix server;  
\- global script execution or remote command execution.  
UnavailableDelay | How often a host is checked for availability during the unavailability period.  
UnreachableDelay | How often a host is checked for availability during the unreachability period.  
UnreachablePeriod | After how many seconds of unreachability treat the host as unavailable.  
User | Drop privileges to a specific, existing user on the system.  
Vault | The vault provider.  
VaultDBPath | The location, from where database credentials should be retrieved by keys.  
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
  
All parameters are non-mandatory unless explicitly stated that the parameter is mandatory.

Note that:

  * The default values reflect daemon defaults, not the values in the shipped configuration files.
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables).
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark).
  * Comments starting with "#" are only supported in the beginning of the line.

### Parameter details

##### AllowRoot

Allow the proxy to run as 'root'. If disabled and the proxy is started by 'root', the proxy will try to switch to the 'zabbix' user instead. Has no effect if started under a regular user.

Default: `0`  
Values: 0 - do not allow; 1 - allow

##### AllowUnsupportedDBVersions

Allow the proxy to work with unsupported database versions.

Default: `0`  
Values: 0 - do not allow; 1 - allow

##### CacheSize

The size of the configuration cache, in bytes. The shared memory size for storing host and item data.

Default: `32M`  
Range: 128K-64G

##### ConfigFrequency

This parameter is **deprecated** (use ProxyConfigFrequency instead).  
How often the proxy retrieves configuration data from Zabbix server in seconds.  
Active proxy parameter. Ignored for passive proxies (see ProxyMode parameter).

Default: `3600`  
Range: 1-604800

##### DataSenderFrequency

The proxy will send collected data to the server every N seconds. Note that an active proxy will still poll Zabbix server every second for remote command tasks.  
Active proxy parameter. Ignored for passive proxies (see ProxyMode parameter).

Default: `1`  
Range: 1-3600

##### DBHost

The database host name.  
With MySQL `localhost` or empty string results in using a socket. With PostgreSQL only empty string results in attempt to use socket.

Default: `localhost`

##### DBName

The database name or path to the database file for SQLite3 (the multi-process architecture of Zabbix does not allow to use [in-memory database](https://www.sqlite.org/inmemorydb.html), e.g. `:memory:`, `file::memory:?cache=shared` or `file:memdb1?mode=memory&cache=shared`).  
_Warning_ : Do not attempt to use the same database the Zabbix server is using.

Mandatory: Yes

##### DBPassword

The database password. Comment this line if no password is used. Ignored for SQLite.

##### DBPort

The database port when not using local socket.**[1](zabbix_proxy#footnotes)** Ignored for SQLite.

Default for MySQL: `3306`

Default for PostgreSQL: `5432`

Range: 1024-65535

##### DBSchema

The database schema name. Used for PostgreSQL.

##### DBSocket

The path to the MySQL socket file.**[1](zabbix_proxy#footnotes)**  
The database port when not using local socket. Ignored for SQLite.

Default: `3306`

##### DBUser

The database user. Ignored for SQLite.

##### DBTLSConnect

Setting this option enforces to use TLS connection to the database:  
_required_ \- connect using TLS  
 _verify_ca_ \- connect using TLS and verify certificate  
 _verify_full_ \- connect using TLS, verify certificate and verify that database identity specified by DBHost matches its certificate  
On MySQL starting from 5.7.11 and PostgreSQL the following values are supported: "required", "verify", "verify_full".  
On MariaDB starting from version 10.2.6 "required" and "verify_full" values are supported.  
By default not set to any option and the behavior depends on database configuration.

##### DBTLSCAFile

The full pathname of a file containing the top-level CA(s) certificates for database certificate verification.

Mandatory: no (yes, if DBTLSConnect set to _verify_ca_ or _verify_full_)

##### DBTLSCertFile

The full pathname of a file containing the Zabbix proxy certificate for authenticating to database.

##### DBTLSKeyFile

The full pathname of a file containing the private key for authenticating to the database.

##### DBTLSCipher

The list of encryption ciphers that Zabbix proxy permits for TLS protocols up through TLS v1.2. Supported only for MySQL.

##### DBTLSCipher13

The list of encryption ciphersuites that Zabbix proxy permits for the TLS v1.3 protocol. Supported only for MySQL, starting from version 8.0.16.

##### DebugLevel

Specify the debug level:  
_0_ \- basic information about starting and stopping of Zabbix processes  
 _1_ \- critical information;  
_2_ \- error information;  
_3_ \- warnings;  
_4_ \- for debugging (produces lots of information);  
_5_ \- extended debugging (produces even more information).

Default: `3`  
Range: 0-5

##### EnableRemoteCommands

Whether remote commands from Zabbix server are allowed.

Default: `0`  
Values: 0 - not allowed; 1 - allowed

##### ExternalScripts

The location of external scripts (depends on the `datadir` compile-time installation variable).

Default: `/usr/local/share/zabbix/externalscripts`

##### Fping6Location

The location of fping6. Make sure that the fping6 binary has root ownership and the SUID flag set. Make empty ("Fping6Location=") if your fping utility is capable to process IPv6 addresses.

Default: `/usr/sbin/fping6`

##### FpingLocation

The location of fping. Make sure that the fping binary has root ownership and the SUID flag set.

Default: `/usr/sbin/fping`

##### HistoryCacheSize

The size of the history cache, in bytes. The shared memory size for storing history data.

Default: `16M`  
Range: 128K-16G

##### HistoryIndexCacheSize

The size of the history index cache, in bytes. The shared memory size for indexing the history data stored in history cache. The index cache size needs roughly 100 bytes to cache one item.

Default: `4M`  
Range: 128K-16G

##### Hostname

A unique, case sensitive proxy name. Make sure the proxy name is known to the server.  
Allowed characters: alphanumeric, '.', ' ', '_' and '-'. Maximum length: 128

Default: Set by HostnameItem

##### HostnameItem

The item used for setting Hostname if it is undefined (this will be run on the proxy similarly as on an agent). Ignored if Hostname is set.  
Does not support UserParameters, performance counters or aliases, but does support system.run[].

Default: system.hostname

##### HousekeepingFrequency

How often Zabbix will perform housekeeping procedure (in hours). Housekeeping is removing outdated information from the database.  
_Note_ : To lower load on proxy startup housekeeping is postponed for 30 minutes after proxy start. Thus, if HousekeepingFrequency is 1, the very first housekeeping procedure after proxy start will run after 30 minutes, and will repeat every hour thereafter.  
It is possible to disable automatic housekeeping by setting HousekeepingFrequency to 0. In this case the housekeeping procedure can only be started by _housekeeper_execute_ runtime control option.

Default: `1`  
Range: 0-24

##### Include

You may include individual files or all files in a directory in the configuration file.  
To only include relevant files in the specified directory, the asterisk wildcard character is supported for pattern matching.  
See [special notes](special_notes_include) about limitations.

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

The module to load at proxy startup. Modules are used to extend the functionality of the proxy. The module must be located in the directory specified by LoadModulePath or the path must precede the module name. If the preceding path is absolute (starts with '/') then LoadModulePath is ignored.  
Formats:  
LoadModule=<module.so>  
LoadModule=<path/module.so>  
LoadModule=</abs_path/module.so>  
It is allowed to include multiple LoadModule parameters.

##### LoadModulePath

The full path to the location of proxy modules. The default depends on compilation options.

##### LogFile

The name of the log file.

Mandatory: Yes, if LogType is set to _file_ ; otherwise no

##### LogFileSize

The maximum size of a log file in MB.  
0 - disable automatic log rotation.  
_Note_ : If the log file size limit is reached and file rotation fails, for whatever reason, the existing log file is truncated and started anew.

Default: `1`  
Range: 0-1024

##### LogRemoteCommands

Enable the logging of executed shell commands as warnings.

Default: `0`  
Values: 0 - disabled, 1 - enabled

##### LogType

The type of the log output:  
_file_ \- write log to the file specified by LogFile parameter;  
_system_ \- write log to syslog;  
_console_ \- write log to standard output.

Default: `file`

##### LogSlowQueries

How long a database query may take before being logged (in milliseconds).  
0 - don't log slow queries.  
This option becomes enabled starting with DebugLevel=3.

Default: `0`  
Range: 0-3600000

##### MaxConcurrentChecksPerPoller

The maximum number of asynchronous checks that can be executed at once by each HTTP agent poller, agent poller or SNMP poller. See StartHTTPAgentPollers, StartAgentPollers, and StartSNMPPollers.

Default: `1000`  
Range: 1-1000

##### PidFile

The name of the PID file.

Default: `/tmp/zabbix_proxy.pid`

##### ProxyBufferMode

Specifies history, network discovery and autoregistration data storage mechanism: _disk_ \- data are stored in database and uploaded from database; _memory_ \- data are stored in memory and uploaded from memory. If buffer runs out of memory the old data will be discarded. On shutdown the buffer is discarded. _hybrid_ \- the proxy buffer normally works like in the memory mode until it runs out of memory or the oldest record exceeds the configured age. If that happens the buffer is flushed to database and it works like in disk mode until all data have been uploaded and it starts working with memory again. On shutdown the memory buffer is flushed to database.

See also: [Proxy memory buffer](/documentation/current/en/manual/concepts/proxy#memory-buffer).

Default: `disk`  
Values: disk; memory; hybrid

##### ProxyConfigFrequency

How often the proxy retrieves configuration data from Zabbix server in seconds.  
Active proxy parameter. Ignored for passive proxies (see ProxyMode parameter).

Default: `10`  
Range: 1-604800

##### ProxyLocalBuffer

The proxy will keep data locally for N hours, even if the data have already been synced with the server.  
This parameter may be used if local data will be used by third-party applications.

Default: `0`  
Range: 0-720

##### ProxyMemoryBufferAge

The maximum age of data in proxy memory buffer, in seconds. When enabled (not zero) and records in proxy memory buffer are older, then it forces proxy buffer to switch to database mode until all records are uploaded to server. This parameter must be less or equal to ProxyOfflineBuffer parameter.

Default: `0`  
Range: 0;600-864000

##### ProxyMemoryBufferSize

The size of shared memory cache for collected history, discovery, and autoregistration data, in bytes. If enabled (not zero) proxy will keep history discovery and autoregistration data in memory unless cache is full or stored records are older than defined ProxyMemoryBufferAge. This parameter cannot be used together with ProxyLocalBuffer parameter.

Default: `0`  
Range: 0;128K-2G

##### ProxyMode

The proxy operating mode.  
0 - proxy in the active mode  
1 - proxy in the passive mode  
 _Note_ that (sensitive) proxy configuration data may become available to parties having access to the Zabbix server trapper port when using an active proxy. This is possible because anyone may pretend to be an active proxy and request configuration data; authentication does not take place.

Default: `0`  
Range: 0-1

##### ProxyOfflineBuffer

The proxy will keep data for N hours in case of no connectivity with Zabbix server.  
Older data will be lost.

Default: `1`  
Range: 1-720

##### Server

If ProxyMode is set to _active mode_ :  
Zabbix server IP address or DNS name (address:port) or [cluster](/documentation/current/en/manual/concepts/server/ha) (address:port;address2:port) to get configuration data from and send data to.  
If port is not specified, the default port is used.  
Cluster nodes must be separated by a semicolon.  
  
If ProxyMode is set to _passive mode_ :  
List of comma delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix server. Incoming connections will be accepted only from the addresses listed here. If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated equally.  
'::/0' will allow any IPv4 or IPv6 address. '0.0.0.0/0' can be used to allow any IPv4 address.

Example:
    
    
    Server=127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.example.com

Copy

✔ Copied

Mandatory: yes

##### SNMPTrapperFile

A temporary file used for passing data from the SNMP trap daemon to the proxy.  
Must be the same as in zabbix_trap_receiver.pl or SNMPTT configuration file.

Default: `/tmp/zabbix_traps.tmp`

##### SocketDir

The directory to store IPC sockets used by internal Zabbix services.

Default: `/tmp`

##### SourceIP

The source IP address for:

  * outgoing connections to Zabbix server
  * agentless connections (VMware, SSH, JMX, SNMP, Telnet and simple checks)
  * HTTP agent connections
  * script item JavaScript HTTP requests
  * preprocessing JavaScript HTTP requests
  * connections to the Vault

##### SSHKeyLocation

The location of public and private keys for SSH checks and actions.

##### SSLCertLocation

The location of SSL client certificate files for client authentication.  
This parameter is used in web monitoring only.

##### SSLKeyLocation

The location of SSL private key files for client authentication.  
This parameter is used in web monitoring only.

##### SSLCALocation

The location of certificate authority (CA) files for SSL server certificate verification.  
Note that the value of this parameter will be set as the CURLOPT_CAPATH libcurl option. For libcurl versions before 7.42.0, this only has effect if libcurl was compiled to use OpenSSL. For more information see the [cURL web page](http://curl.haxx.se/libcurl/c/CURLOPT_CAPATH.html).  
This parameter is used in web monitoring and in SMTP authentication.

##### StartAgentPollers

The number of pre-forked instances of Zabbix agent [pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads). See MaxConcurrentChecksPerPoller.

Default: `1`  
Range: 0-1000

##### StartBrowserPollers

The number of pre-forked instances of browser item [pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `1`  
Range: 0-1000

##### StartDBSyncers

The number of pre-forked instances of [history syncers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).  
_Note_ : Be careful when changing this value, increasing it may do more harm than good.

Default: `4`  
Range: 1-100

##### StartDiscoverers

The number of pre-forked instances of [discovery workers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `5`  
Range: 0-1000

##### StartHTTPAgentPollers

The number of pre-forked instances of HTTP agent [pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads). See MaxConcurrentChecksPerPoller.

Default: `1`  
Range: 0-1000

##### StartHTTPPollers

The number of pre-forked instances of [HTTP pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `1`  
Range: 0-1000

##### StartIPMIPollers

The number of pre-forked instances of [IPMI pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `0`  
Range: 0-1000

##### StartJavaPollers

The number of pre-forked instances of [Java pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `0`  
Range: 0-1000

##### StartODBCPollers

The number of pre-forked instances of [ODBC pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `1`  
Range: 0-1000

##### StartPingers

The number of pre-forked instances of [ICMP pingers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `1`  
Range: 0-1000

##### StartPollersUnreachable

The number of pre-forked instances of [pollers for unreachable hosts](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads) (including IPMI and Java). At least one poller for unreachable hosts must be running if regular, IPMI or Java pollers are started.

Default: `1`  
Range: 0-1000

##### StartPollers

The number of pre-forked instances of [pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).

Default: `5`  
Range: 0-1000

##### StartPreprocessors

The number of pre-started instances of preprocessing [worker](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads) threads should be set to no less than the available CPU core count. More workers should be set if preprocessing is not CPU-bound and has lots of network requests.

Default: `16`  
Range: 1-1000

##### StartSNMPPollers

The number of pre-forked instances of SNMP [pollers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads). See MaxConcurrentChecksPerPoller.

Default: `1`  
Range: 0-1000

##### StartSNMPTrapper

If set to 1, an [SNMP trapper](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads) process will be started.

Default: `0`  
Range: 0-1

##### StartTrappers

The number of pre-forked instances of [trappers](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads).  
Trappers accept incoming connections from Zabbix sender and active agents.

Default: `5`  
Range: 0-1000

##### StartVMwareCollectors

The number of pre-forked [VMware collector](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads) instances.

Default: `0`  
Range: 0-250

##### StatsAllowedIP

A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of external Zabbix instances. The stats request will be accepted only from the addresses listed here. If this parameter is not set no stats requests will be accepted.  
If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated equally and '::/0' will allow any IPv4 or IPv6 address. '0.0.0.0/0' can be used to allow any IPv4 address.

Example:
    
    
    StatsAllowedIP=127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.example.com

Copy

✔ Copied

##### Timeout

Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix server, agent, web service, legacy SNMP checks (single OID number or string), and `icmpping[*]` item.

This parameter defines the duration for various communication operations:

  * Remote command execution on Zabbix agent
  * SSH / Telnet command execution
  * Rescheduling of items when IPMI interface becomes unavailable
  * ICMP pinger
  * Sending response to Zabbix server when failing to exchange data due to rights or encryption issues
  * Deadline for IPC asynchronous sockets and runtime control options
  * Asynchronous poller DNS requests
  * Response for active check heartbeat
  * Retrieval of Zabbix agent data (values) from active agents
  * Retrieval of data from Zabbix sender
  * Sending active check list to Zabbix agent

This timeout will **not** be used for those checks that have [flexible timeout](/documentation/current/en/manual/config/items/item#item-timeout) settings configured in the frontend (on global, proxy, or per-item level). For example, SNMP `walk[OID]` and `get[OID]` items use the configured timeout from the frontend; legacy SNMP checks still use the server timeout value.

Default: `3`  
Range: 1-30

##### TLSAccept

What incoming connections to accept from Zabbix server. Used for a passive proxy, ignored on an active proxy. Multiple values can be specified, separated by comma:  
_unencrypted_ \- accept connections without encryption (default)  
_psk_ \- accept connections with TLS and a pre-shared key (PSK)  
_cert_ \- accept connections with TLS and a certificate

Mandatory: yes for passive proxy, if TLS certificate or PSK parameters are defined (even for _unencrypted_ connection); otherwise no

##### TLSCAFile

The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.

##### TLSCertFile

The full pathname of a file containing the proxy certificate or certificate chain, used for encrypted communications between Zabbix components.

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

##### TLSConnect

How the proxy should connect to Zabbix server. Used for an active proxy, ignored on a passive proxy. Only one value can be specified:  
_unencrypted_ \- connect without encryption (default)  
_psk_ \- connect using TLS and a pre-shared key (PSK)  
_cert_ \- connect using TLS and a certificate

Mandatory: yes for active proxy, if TLS certificate or PSK parameters are defined (even for _unencrypted_ connection); otherwise no

##### TLSCRLFile

The full pathname of a file containing revoked certificates. This parameter is used for encrypted communications between Zabbix components.

##### TLSKeyFile

The full pathname of a file containing the proxy private key, used for encrypted communications between Zabbix components.

##### TLSListen

Controls TLS on the trapper socket.

Supported values:

  * required - accept only TLS connections

##### TLSPSKFile

The full pathname of a file containing the proxy pre-shared key, used for encrypted communications with Zabbix server.

##### TLSPSKIdentity

The pre-shared key identity string, used for encrypted communications with Zabbix server.

##### TLSServerCertIssuer

The allowed server certificate issuer.

##### TLSServerCertSubject

The allowed server certificate subject.

##### TmpDir

The temporary directory.

Default: `/tmp`

##### TrapperTimeout

Specifies timeout in seconds for:   
\- retrieval of configuration data from the Zabbix server;  
\- global script execution or remote command execution.

Default: `300`  
Range: 1-300

##### UnavailableDelay

How often a host is checked for availability during the [unavailability](/documentation/current/en/manual/appendix/items/unreachability#unavailable-interface) period in seconds.

Default: `60`  
Range: 1-3600

##### UnreachableDelay

How often a host is checked for availability during the [unreachability](/documentation/current/en/manual/appendix/items/unreachability#unreachable-interface) period in seconds.

Default: `15`  
Range: 1-3600

##### UnreachablePeriod

After how many seconds of [unreachability](/documentation/current/en/manual/appendix/items/unreachability#unreachable-interface) treat a host as unavailable.

Default: `45`  
Range: 1-3600

##### User

Drop privileges to a specific, existing user on the system.  
Only has effect if run as 'root' and AllowRoot is disabled.

Default: `zabbix`

##### Vault

The vault provider:  
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
    
    
    AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix_proxy_database

Copy

✔ Copied

This option can only be used if DBUser and DBPassword are not specified.

##### VaultPrefix

A custom prefix for Vault path or query, depending on the Vault. The most suitable defaults will be used if not specified.  
Note that 'data' is automatically appended after mountpoint for HashiCorp if VaultPrefix is not specified.   
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

The name of the SSL certificate file used for client authentication. The certificate file must be in PEM1 format.  
If the certificate file contains also the private key, leave the SSL key file field empty.  
The directory containing this file is specified by the SSLCertLocation configuration parameter.  
This option can be omitted, but is recommended for CyberArkCCP vault.

##### VaultTLSKeyFile

The name of the SSL private key file used for client authentication. The private key file must be in PEM1 format.  
The directory containing this file is specified by the SSLKeyLocation configuration parameter.  
This option can be omitted, but is recommended for CyberArkCCP vault.

##### VaultToken

The HashiCorp vault authentication token that should have been generated exclusively for Zabbix proxy with read-only permission to the path specified in the optional VaultDBPath configuration parameter.  
It is an error if VaultToken and the VAULT_TOKEN environment variable are defined at the same time.

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

The delay in seconds between performance counter statistics retrieval from a single VMware service.  
This delay should be set to the least update interval of any VMware monitoring [item](/documentation/current/en/manual/vm_monitoring/vmware_keys#footnotes) that uses VMware performance counters.

Default: `60`  
Range: 10-86400

##### VMwareTimeout

The maximum number of seconds a vmware collector will wait for a response from VMware service (vCenter or ESX hypervisor).

Default: `10`  
Range: 1-300

##### WebDriverURL

WebDriver interface HTTP[S] URL.

Example (used with Selenium WebDriver standalone server):
    
    
    WebDriverURL=http://localhost:4444

Copy

✔ Copied

#### Footnotes

**1** DBSocket and DBPort are mutually exclusive in proxy configuration. Specify only one, or leave both undefined.