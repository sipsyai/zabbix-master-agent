---
title: Redis plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/redis_plugin
downloaded: 2025-11-14 10:47:04
---

# 13 Redis plugin

#### Overview

This section lists parameters supported in the Redis Zabbix agent 2 plugin configuration file (redis.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files.
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables).
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark).
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.Redis.Default.Password | no |  |  | Default password for connecting to Redis; used if no value is specified in an item key or named session.  
---|---|---|---|---  
Plugins.Redis.Default.TLSConnect | no |  |  | Client (Zabbix agent 2) TLS verification requirement.  
  
Supported values:  
`required` \- encrypted, unverified (only for testing)  
`verify_ca` \- encrypted, server certificate  
`verify_full` \- encrypted, server certificate and server name verified with SAN  
An empty or unset value is treated as no tls.  
Plugins.Redis.Default.TLSCAFile | no |  |  | Default full pathname of a file containing the top-level CA(s) certificates.  
Plugins.Redis.Default.TLSCertFile | no |  |  | Default full pathname of a file containing the agent's certificate.  
Plugins.Redis.Default.TLSKeyFile | no |  |  | Default full pathname of a file containing the agent's private key.  
Plugins.Redis.Default.Uri | no |  | tcp://localhost:6379 | Default URI for connecting to Redis; used if no value is specified in an item key or named session.   
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`; a scheme can be omitted.  
A port can be omitted (default=6379).  
Examples: `tcp://localhost:6379`  
`localhost`  
`unix:/var/run/redis.sock`  
Plugins.Redis.Default.User | no |  | default | Default user to send to the protected Redis server; used if no value is specified in an item key or named session.  
Plugins.Redis.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.Redis.Sessions.<SessionName>.Password | no |  |  | Named session password.  
**< SessionName>** \- define the session name to be used in item keys.  
Plugins.Redis.Sessions.<SessionName>.TLSConnect | no |  |  | Client (Zabbix agent 2) TLS verification requirement.  
**< SessionName>** \- define the session name to be used in item keys.  
  
Supported values:  
`required` \- encrypted, unverified (only for testing)  
`verify_ca` \- encrypted, server certificate  
`verify_full` \- encrypted, server certificate and server name verified with SAN  
An empty or unset value is treated as no tls.  
Plugins.Redis.Sessions.<SessionName>.TLSCAFile | no  
(yes, if TLSConnect is `verify_ca` or `verify_full`) |  |  | Full pathname of a file containing the top-level CA(s) certificates for Redis server certificate verification.  
**< SessionName>** \- define the session name to be used in item keys.  
Plugins.Redis.Sessions.<SessionName>.TLSCertFile | no |  |  | Full pathname of a file containing the agent's certificate for client authentication.  
**< SessionName>** \- define the session name to be used in item keys.  
Plugins.Redis.Sessions.<SessionName>.TLSKeyFile | no |  |  | Full pathname of a file containing the agent's private key for client authentication.  
**< SessionName>** \- define the session name to be used in item keys.  
Plugins.Redis.Sessions.<SessionName>.Uri | no |  | localhost:6379 | Connection string of a named session.  
**< SessionName>** \- define the session name to be used in item keys.  
  
Should not include embedded credentials (they will be ignored).  
Must match the URI format.  
Supported schemes: `tcp`, `unix`; a scheme can be omitted.  
A port can be omitted (default=6379).  
Examples: `tcp://localhost:6379`  
`localhost`  
`unix:/var/run/redis.sock`  
Plugins.Redis.Sessions.<SessionName>.User | no |  | default | User to send to the protected Redis server.  
**< SessionName>** \- define the session name to be used in item keys.  
Plugins.Redis.Timeout | no | 1-30 | global timeout | Request execution timeout (the duration, in seconds, to wait for a request to complete before shutting it down).  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)