---
title: Zabbix agent (Windows)
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agentd_win
downloaded: 2025-11-14 10:46:49
---

# 5 Zabbix agent (Windows)

### Overview

The parameters supported by the Windows Zabbix agent configuration file (zabbix_agentd.conf) are listed in this section.

The parameters are listed without additional information. Click on the parameter to see the full details.

Alias | Sets an alias for an item key.  
---|---  
AllowKey | Allow the execution of those item keys that match a pattern.  
BufferSend | Do not keep data longer than N seconds in buffer.  
BufferSize | The maximum number of values in the memory buffer.  
DebugLevel | The debug level.  
DenyKey | Deny the execution of those item keys that match a pattern.  
EnableRemoteCommands | Whether remote commands from Zabbix server are allowed.  
HeartbeatFrequency | The frequency of heartbeat messages in seconds.  
HostInterface | An optional parameter that defines the host interface.  
HostInterfaceItem | An optional parameter that defines an item used for getting the host interface.  
HostMetadata | An optional parameter that defines the host metadata.  
HostMetadataItem | An optional parameter that defines a Zabbix agent item used for getting the host metadata.  
Hostname | An optional parameter that defines the hostname.  
HostnameItem | An optional parameter that defines a Zabbix agent item used for getting the hostname.  
Include | You may include individual files or all files in a directory in the configuration file.  
ListenBacklog | The maximum number of pending connections in the TCP queue.  
ListenIP | A list of comma-delimited IP addresses that the agent should listen on.  
ListenPort | The agent will listen on this port for connections from the server.  
LogFile | The name of the log file.  
LogFileSize | The maximum size of the log file.  
LogRemoteCommands | Enable logging of executed shell commands as warnings.  
LogType | The type of the log output.  
MaxLinesPerSecond | The maximum number of new lines the agent will send per second to Zabbix server or proxy when processing 'log' and 'logrt' active checks.  
PerfCounter | Defines a new parameter <parameter_name> which is the average value for system performance counter <perf_counter_path> for the specified time period <period> (in seconds).  
PerfCounterEn | Defines a new parameter <parameter_name> which is the average value for system performance counter <perf_counter_path> for the specified time period <period> (in seconds). Compared to PerfCounter, the perfcounter paths must be in English.  
RefreshActiveChecks | How often the list of active checks is refreshed.  
Server | A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix servers and Zabbix proxies.  
ServerActive | The Zabbix server/proxy address or cluster configuration to get active checks from.  
SourceIP | The source IP address.  
StartAgents | The number of pre-forked instances of zabbix_agentd that process passive checks.  
Timeout | Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix proxy or server.  
TLSAccept | What incoming connections to accept.  
TLSCAFile | The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.  
TLSCertFile | The full pathname of a file containing the agent certificate or certificate chain, used for encrypted communications between Zabbix components.  
TLSConnect | How the agent should connect to Zabbix server or proxy.  
TLSCRLFile | The full pathname of a file containing revoked certificates. This parameter is used for encrypted communications between Zabbix components.  
TLSKeyFile | The full pathname of a file containing the agent private key, used for encrypted communications between Zabbix components.  
TLSPSKFile | The full pathname of a file containing the agent pre-shared key, used for encrypted communications with Zabbix server.  
TLSPSKIdentity | The pre-shared key identity string, used for encrypted communications with Zabbix server.  
TLSServerCertIssuer | The allowed server (proxy) certificate issuer.  
TLSServerCertSubject | The allowed server (proxy) certificate subject.  
UnsafeUserParameters | Allow all characters to be passed in arguments to user-defined parameters.  
UserParameter | A user-defined parameter to monitor.  
UserParameterDir | The default search path for UserParameter commands.  
  
All parameters are non-mandatory unless explicitly stated that the parameter is mandatory.

Note that:

  * The default values reflect daemon defaults, not the values in the shipped configuration files.
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables).
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark).
  * Comments starting with "#" are only supported in the beginning of the line.

### Parameter details

##### Alias

Sets an alias for an item key. It can be used to substitute a long and complex item key with a shorter and simpler one.  
Multiple _Alias_ parameters may be present. Multiple parameters with the same _Alias_ key are not allowed.  
Different _Alias_ keys may reference the same item key.  
Aliases can be used in _HostMetadataItem_ but not in _HostnameItem_ or _PerfCounter_ parameter.

Example 1: Retrieving the paging file usage in percentage from the server.
    
    
    Alias=pg_usage:perf_counter[\Paging File(_Total)\% Usage]

Copy

✔ Copied

Now the shorthand key **pg_usage** may be used to retrieve data.

Example 2: Getting the CPU load with default and custom parameters.
    
    
    Alias=cpu.load:system.cpu.load
           Alias=cpu.load[*]:system.cpu.load[*]

Copy

✔ Copied

This allows use **cpu.load** key to get the CPU load with default parameters as well as use **cpu.load[percpu,avg15]** to get specific data about the CPU load.

Example 3: Running multiple [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) rules processing the same discovery items.
    
    
    Alias=vfs.fs.discovery[*]:vfs.fs.discovery

Copy

✔ Copied

Now it is possible to set up several discovery rules using **vfs.fs.discovery** with different parameters for each rule, e.g., **vfs.fs.discovery[foo]** , **vfs.fs.discovery[bar]** , etc.

##### AllowKey

Allow the execution of those item keys that match a pattern. The key pattern is a wildcard expression that supports the "*" character to match any number of any characters.  
Multiple key matching rules may be defined in combination with DenyKey. The parameters are processed one by one according to their appearance order. See also: [Restricting agent checks](/documentation/current/en/manual/config/items/restrict_checks).

##### BufferSend

Do not keep data longer than N seconds in buffer.

Default: `5`  
Range: 1-3600

##### BufferSize

The maximum number of values in the memory buffer. The agent will send all collected data to the Zabbix server or proxy if the buffer is full.

Default: `100`  
Range: 2-65535

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

##### DenyKey

Deny the execution of those item keys that match a pattern. The key pattern is a wildcard expression that supports the "*" character to match any number of any characters.  
Multiple key matching rules may be defined in combination with AllowKey. The parameters are processed one by one according to their appearance order. See also: [Restricting agent checks](/documentation/current/en/manual/config/items/restrict_checks).

##### EnableRemoteCommands

Whether remote commands from Zabbix server are allowed. This parameter is **deprecated** , use AllowKey=system.run[*] or DenyKey=system.run[*] instead.  
It is an internal alias for AllowKey/DenyKey parameters depending on value:  
0 - DenyKey=system.run[*]  
1 - AllowKey=system.run[*]

Default: `0`  
Values: 0 - do not allow, 1 - allow

##### HeartbeatFrequency

The frequency of heartbeat messages in seconds. Used for monitoring the availability of active checks.  
0 - heartbeat messages disabled.

Default: `60`  
Range: 0-3600

##### HostInterface

An optional parameter that defines the host interface (IP address or DNS name) used during the host [autoregistration](/documentation/current/en/manual/discovery/auto_registration) process. This value will be used to populate the interface in the newly created host, and allows configuring either IP or DNS address explicitly. For more details, see [Using DNS as default interface](/documentation/current/en/manual/discovery/auto_registration#using-dns-as-default-interface).

If not defined, the value will be acquired from HostInterfaceItem.

The agent will issue an error and not start if the value is over the limit of 255 characters.

Range: 0-255 characters

##### HostInterfaceItem

An optional parameter that defines an item used to determine the host interface (IP address or DNS name) during the host [autoregistration](/documentation/current/en/manual/discovery/auto_registration) process. This value is used only if HostInterface is not defined. For more details, see [Using DNS as default interface](/documentation/current/en/manual/discovery/auto_registration#using-dns-as-default-interface).

During an autoregistration request the agent will log a warning message if the value returned by the specified item is over the limit of 255 characters.

The [system.run[]](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.run) item is supported regardless of AllowKey/DenyKey settings.

##### HostMetadata

An optional parameter that defines the [metadata](/documentation/current/en/manual/discovery/auto_registration#using-host-metadata) used to identify or distinguish the host during the host [autoregistration](/documentation/current/en/manual/discovery/auto_registration) process (active agent). HostMetadata allows distinguishing between hosts beyond the hostname.

If not defined, the value will be acquired from HostMetadataItem.

The agent will issue an error and not start if the specified value is over the limit of 2034 bytes or a non-UTF-8 string. When a parameter expects an IP address or DNS name, values that are valid UTF-8 but are not valid IPs or DNS names will also be rejected and reported as invalid.

Multi-line metadata is not supported — the output will be truncated at the first line break.

Range: 0-2034 bytes

##### HostMetadataItem

An optional parameter that defines a Zabbix agent item used to obtain [host metadata](/documentation/current/en/manual/discovery/auto_registration#using-host-metadata). This option is only used when HostMetadata is not defined.

The HostMetadataItem value is retrieved on each [autoregistration](/documentation/current/en/manual/discovery/auto_registration) attempt and is used only at host autoregistration process (active agent). HostMetadataItem allows distinguishing between hosts beyond the hostname.

User parameters, performance counters and aliases are supported. The [system.run[]](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.run) item is supported regardless of AllowKey/DenyKey settings.

During an autoregistration request the agent will log a warning message if the value returned by the specified item is over the limit of 65535 UTF-8 code points. The value returned by the item must be a UTF-8 string otherwise it will be ignored. When a parameter expects an IP address or DNS name, values that are valid UTF-8 but are not valid IPs or DNS names will also be rejected and reported as invalid.

Multi-line metadata is not supported — the output will be truncated at the first line break.

##### Hostname

A list of comma-delimited, unique, case-sensitive hostnames. Required for active checks and must match hostnames as configured on the server. The value is acquired from HostnameItem if undefined.  
Allowed characters: alphanumeric, '.', ' ', '_' and '-'. Maximum length: 128 characters per hostname, 2048 characters for the entire line.

Default: Set by HostnameItem

##### HostnameItem

An optional parameter that defines a Zabbix agent item used for getting the host name. This option is only used when Hostname is not defined. User parameters, performance counters or aliases are not supported, but the [system.run[]](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.run) item is supported regardless of AllowKey/DenyKey values.  
See also a [more detailed description](/documentation/current/en/manual/appendix/install/windows_agent#configuration).

Default: `system.hostname`

##### Include

You may include individual files or all files in a directory in the configuration file (located in `C:\Program Files\Zabbix Agent` by default if Zabbix agent is installed using Windows MSI installer packages; located in the folder specified during installation if Zabbix agent is installed as a zip archive). All included files must have correct syntax, otherwise agent will not start.  
To only include relevant files in the specified directory, the asterisk wildcard character is supported for pattern matching.  
See [special notes](special_notes_include) about limitations.

Example:
    
    
    Include=C:\Program Files\Zabbix Agent\zabbix_agentd.d\*.conf

Copy

✔ Copied

##### ListenBacklog

The maximum number of pending connections in the TCP queue.  
The default value is a hard-coded constant, which depends on the system.  
The maximum supported value depends on the system, too high values may be silently truncated to the 'implementation-specified maximum'.

Default: `SOMAXCONN`  
Range: 0 - INT_MAX

##### ListenIP

A list of comma-delimited IP addresses that the agent should listen on.

Default: `0.0.0.0`

##### ListenPort

The agent will listen on this port for connections from the server.

Default: `10050`  
Range: 1024-32767

##### LogFile

The name of the agent log file.

Default: `c:\zabbix_agentd.log`  
Mandatory: Yes, if LogType is set to _file_ ; otherwise no

##### LogFileSize

The maximum size of a log file in MB.  
0 - disable automatic log rotation.  
_Note_ : If the log file size limit is reached and file rotation fails, for whatever reason, the existing log file is truncated and started anew.

Default: `1`  
Range: 0-1024

##### LogRemoteCommands

Enable the logging of the executed shell commands as warnings. Commands will be logged only if executed remotely. Log entries will not be created if system.run[] is launched locally by HostMetadataItem, HostInterfaceItem or HostnameItem parameters.

Default: `0`  
Values: 0 - disabled, 1 - enabled

##### LogType

The type of the log output:  
_file_ \- write log to the file specified by LogFile parameter;  
_system_ \- write log to Windows Event Log;  
_console_ \- write log to standard output.

Default: `file`

##### MaxLinesPerSecond

The maximum number of new lines the agent will send per second to Zabbix server or proxy when processing 'log', 'logrt', and 'eventlog' active checks. The provided value will be overridden by the 'maxlines' parameter, provided in the 'log', 'logrt', or 'eventlog' item key.  
_Note_ : Zabbix will process 10 times more new lines than set in _MaxLinesPerSecond_ to seek the required string in log items.

Default: `20`  
Range: 1-1000

##### PerfCounter

Defines a new parameter <parameter_name> which is the average value for system performance counter <perf_counter_path> for the specified time period <period> (in seconds).  
Syntax: <parameter_name>,"<perf_counter_path>",<period>

For example, if you wish to receive the average number of processor interrupts per second for the last minute, you can define a new parameter "interrupts" as the following:  

    
    
    PerfCounter = interrupts,"\Processor(0)\Interrupts/sec",60

Copy

✔ Copied

Please note the double quotes around the performance counter path. The parameter name (interrupts) is to be used as the item key when creating an item. Samples for calculating the average value will be taken every second.  
You may run "typeperf -qx" to get the list of all performance counters available in Windows.

##### PerfCounterEn

Defines a new parameter <parameter_name> which is the average value for system performance counter <perf_counter_path> for the specified time period <period> (in seconds). Compared to PerfCounter, the perfcounter paths must be in English. Supported only on **Windows Server 2008/Vista** and later.  
Syntax: <parameter_name>,"<perf_counter_path>",<period>

For example, if you wish to receive the average number of processor interrupts per second for the last minute, you can define a new parameter "interrupts" as the following:  

    
    
    PerfCounterEn = interrupts,"\Processor(0)\Interrupts/sec",60

Copy

✔ Copied

Please note the double quotes around the performance counter path. The parameter name (interrupts) is to be used as the item key when creating an item. Samples for calculating the average value will be taken every second.  
You can find the list of English strings by viewing the following registry key: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\009`.

##### RefreshActiveChecks

How often the list of active checks is refreshed, in seconds. Note that after failing to refresh active checks the next refresh will be attempted in 60 seconds.

Default: `5`  
Range: 1-86400

##### Server

A list of comma-delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix servers or Zabbix proxies. Incoming connections will be accepted only from the hosts listed here. If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated equally and '::/0' will allow any IPv4 or IPv6 address. '0.0.0.0/0' can be used to allow any IPv4 address. Note that "IPv4-compatible IPv6 addresses" (0000::/96 prefix) are supported but deprecated by [RFC4291](https://tools.ietf.org/html/rfc4291#section-2.5.5). Spaces are allowed.

Example:
    
    
    Server=127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.example.com

Copy

✔ Copied

Mandatory: yes, if StartAgents is not explicitly set to 0

##### ServerActive

The Zabbix server/proxy address or cluster configuration to get active checks from. The server/proxy address is an IP address or DNS name and optional port separated by colon.  
The cluster configuration is one or more server addresses separated by semicolon. Multiple Zabbix servers/clusters and Zabbix proxies can be specified, separated by comma. More than one Zabbix proxy should not be specified from each Zabbix server/cluster. If Zabbix proxy is specified then Zabbix server/cluster for that proxy should not be specified.  
Multiple comma-delimited addresses can be provided to use several independent Zabbix servers in parallel. Spaces are allowed.  
If the port is not specified, default port is used.  
IPv6 addresses must be enclosed in square brackets if port for that host is specified. If port is not specified, square brackets for IPv6 addresses are optional.  
If this parameter is not specified, active checks are disabled.

Example for Zabbix proxy:
    
    
    ServerActive=127.0.0.1:10051

Copy

✔ Copied

Example for multiple servers:
    
    
    ServerActive=127.0.0.1:20051,zabbix.domain,[::1]:30051,::1,[12fc::1]

Copy

✔ Copied

Example for high availability:
    
    
    ServerActive=zabbix.cluster.node1;zabbix.cluster.node2:20051;zabbix.cluster.node3

Copy

✔ Copied

Example for high availability with two clusters and one server:
    
    
    ServerActive=zabbix.cluster.node1;zabbix.cluster.node2:20051,zabbix.cluster2.node1;zabbix.cluster2.node2,zabbix.domain

Copy

✔ Copied

Range: (*)

##### SourceIP

The source IP address for:

  * outgoing connections to Zabbix server or Zabbix proxy.
  * making connections while executing some items (web.page.get, net.tcp.port, etc.).

##### StartAgents

The number of pre-forked instances of zabbix_agentd that process passive checks. If set to 0, passive checks are disabled and the agent will not listen on any TCP port.

Default: `10`  
Range: 0-100 (*)

##### Timeout

Specifies how long to wait (in seconds) for establishing connection and exchanging data with Zabbix proxy or server.  

This parameter defines the duration of various communication operations, including:

  * awaiting a response from the Zabbix server;
  * sending requests to Zabbix server, including item configuration requests and item data in [active checks](/documentation/current/en/manual/appendix/items/activepassive#active-checks);
  * retrieving log data through logfile or Windows event log monitoring;
  * sending heartbeat messages;
  * maximum duration for `vfs.*` checks;
  * used by Zabbix agent modules;
  * serving as a fallback in scenarios where a server or proxy older than version 7.0 sends checks without timeouts.

This timeout will **not** be used for those agent checks that have configurable timeout settings in the frontend (on global, proxy, or per-item level).

Default: `3`  
Range: 1-30

##### TLSAccept

The incoming connections to accept. Used for passive checks. Multiple values can be specified, separated by comma:  
_unencrypted_ \- accept connections without encryption (default)  
_psk_ \- accept connections with TLS and a pre-shared key (PSK)  
_cert_ \- accept connections with TLS and a certificate

Mandatory: yes, if TLS certificate or PSK parameters are defined (even for _unencrypted_ connection); otherwise no

##### TLSCAFile

The full pathname of the file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.

##### TLSCertFile

The full pathname of the file containing the agent certificate or certificate chain, used for encrypted communications with Zabbix components.

##### TLSConnect

How the agent should connect to Zabbix server or proxy. Used for active checks. Only one value can be specified:  
_unencrypted_ \- connect without encryption (default)  
_psk_ \- connect using TLS and a pre-shared key (PSK)  
_cert_ \- connect using TLS and a certificate

Mandatory: yes, if TLS certificate or PSK parameters are defined (even for _unencrypted_ connection); otherwise no

##### TLSCRLFile

The full pathname of the file containing revoked certificates. This parameter is used for encrypted communications between Zabbix components.

##### TLSKeyFile

The full pathname of the file containing the agent private key, used for encrypted communications between Zabbix components.

##### TLSPSKFile

The full pathname of the file containing the agent pre-shared key, used for encrypted communications with Zabbix server.

##### TLSPSKIdentity

The pre-shared key identity string, used for encrypted communications with Zabbix server.

##### TLSServerCertIssuer

The allowed server (proxy) certificate issuer.

##### TLSServerCertSubject

The allowed server (proxy) certificate subject.

##### UnsafeUserParameters

Allow all characters to be passed in arguments to user-defined parameters. The following characters are not allowed: \ ' " ` * ? [ ] { } ~ $ ! & ; ( ) < > | # @  
Additionally, newline characters are not allowed.

Default: `0`  
Values: 0 - do not allow, 1 - allow

##### UserParameter

A user-defined parameter to monitor. There can be several user-defined parameters.  
Format: UserParameter=<key>,<shell command>  
Note that the shell command must not return empty string or EOL only. Shell commands may have relative paths, if the UserParameterDir parameter is specified.

Example:
    
    
    UserParameter=system.test,dir /b | find /c /v ""
           UserParameter=check_cpu,.\custom\_script.bat

Copy

✔ Copied

##### UserParameterDir

The default search path for UserParameter commands. If used, the agent will change its working directory to the one specified here before executing a command. Thereby, UserParameter commands can have a relative `./` prefix instead of a full path. Only one entry is allowed.

Example:
    
    
    UserParameterDir=C:\opt\myscripts

Copy

✔ Copied

(*) The number of active servers listed in ServerActive plus the number of pre-forked instances for passive checks specified in StartAgents must be less than 64.