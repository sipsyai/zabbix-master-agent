---
title: Zabbix web service
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_web_service
downloaded: 2025-11-14 10:47:07
---

# 9 Zabbix web service

### Overview

The Zabbix web service is a process that is used for communication with external web services.

The parameters supported by the Zabbix web service configuration file (zabbix_web_service.conf) are listed in this section.

The parameters are listed without additional information. Click on the parameter to see the full details.

AllowedIP | A list of comma delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix servers and Zabbix proxies.  
---|---  
DebugLevel | The debug level.  
IgnoreURLCertErrors | Specifies TLS certificate validation error handling when accessing the frontend URL.  
ListenPort | The service will listen on this port for connections from the server.  
LogFile | The name of the log file.  
LogFileSize | The maximum size of the log file.  
LogType | The type of the log output.  
Timeout | The maximum time (in seconds) spent formatting the PDF [report](/documentation/current/en/manual/config/reports) of a dashboard.  
TLSAccept | What incoming connections to accept.  
TLSCAFile | The full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.  
TLSCertFile | The full pathname of a file containing the service certificate or certificate chain, used for encrypted communications between Zabbix components.  
TLSKeyFile | The full pathname of a file containing the service private key, used for encrypted communications between Zabbix components.  
  
All parameters are non-mandatory unless explicitly stated that the parameter is mandatory.

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

### Parameter details

##### AllowedIP

A list of comma delimited IP addresses, optionally in CIDR notation, or DNS names of Zabbix servers and Zabbix proxies. Incoming connections will be accepted only from the hosts listed here.  
If IPv6 support is enabled then `127.0.0.1`, `::127.0.0.1`, `::ffff:127.0.0.1` are treated equally and `::/0` will allow any IPv4 or IPv6 address. `0.0.0.0/0` can be used to allow any IPv4 address.

Example:
    
    
    127.0.0.1,192.168.1.0/24,::1,2001:db8::/32,zabbix.example.com

Copy

✔ Copied

Mandatory: yes

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

##### IgnoreURLCertErrors

Specifies TLS certificate validation error handling when accessing the frontend URL:  
0 - do not ignore certificate errors;  
1 - ignore certificate errors.  

Default: `0`  
Range: 0-1

##### ListenPort

The service will listen on this port for connections from the server.

Default: `10053`  
Range: 1024-32767

##### LogFile

The name of the log file.

Example:
    
    
    /tmp/zabbix_web_service.log

Copy

✔ Copied

Mandatory: Yes, if LogType is set to _file_ ; otherwise no

##### LogFileSize

The maximum size of a log file in MB.  
0 - disable automatic log rotation.  
_Note_ : If the log file size limit is reached and file rotation fails, for whatever reason, the existing log file is truncated and started anew.

Default: `1`  
Range: 0-1024

##### LogType

The type of the log output:  
_file_ \- write log to the file specified by LogFile parameter;  
_system_ \- write log to syslog;  
_console_ \- write log to standard output.

Default: `file`

##### Timeout

The maximum time (in seconds) spent formatting the PDF [report](/documentation/current/en/manual/config/reports) of a dashboard.

Default: `10`  
Range: 1-30

##### TLSAccept

What incoming connections to accept:  
_unencrypted_ \- accept connections without encryption (default)  
_cert_ \- accept connections with TLS and a certificate

Default: `unencrypted`

##### TLSCAFile

The full pathname of the file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix components.

##### TLSCertFile

The full pathname of the file containing the service certificate or certificate chain, used for encrypted communications with Zabbix components.

##### TLSKeyFile

The full pathname of the file containing the service private key, used for encrypted communications between Zabbix components.