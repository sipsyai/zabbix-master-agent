---
title: MQTT plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mqtt_plugin
downloaded: 2025-11-14 10:46:58
---

# 7 MQTT plugin

#### Overview

This section lists parameters supported in the MQTT Zabbix agent 2 plugin configuration file (mqtt.conf).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.MQTT.Default.Password | no |  |  | Default password for connecting to MQTT; used if no value is specified in an item key or named session.  
---|---|---|---|---  
Plugins.MQTT.Default.TLSCAFile | no |  |  | Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification for encrypted communications between Zabbix agent 2 and MQTT broker; used if no value is specified in a named session.  
Plugins.MQTT.Default.TLSCertFile | no |  |  | Full pathname of a file containing the agent certificate or certificate chain for encrypted communications between Zabbix agent 2 and MQTT broker; used if no value is specified in a named session.  
Plugins.MQTT.Default.TLSKeyFile | no |  |  | Full pathname of a file containing the MQTT private key for encrypted communications between Zabbix agent 2 and MQTT broker; used if no value is specified in a named session.  
Plugins.MQTT.Default.Topic | no |  |  | Default topic for MQTT subscription; used if no value is specified in an item key or named session.  
  
The topic may contain wildcards ("+","#")  
Examples: `path/to/file`  
`path/to/#`  
`path/+/topic`  
Plugins.MQTT.Default.Url | no |  | tcp://localhost:1883 | Default MQTT broker connection string; used if no value is specified in an item key or named session.  
  
Should not include query parameters.  
Must match the URL format.  
Supported schemes: `tcp` (default), `ws`, `tls`; a scheme can be omitted.  
A port can be omitted (default=1883).  
Examples: `tcp://host:1883`  
`localhost`  
`ws://host:8080`  
Plugins.MQTT.Default.User | no |  |  | Default username for connecting to MQTT; used if no value is specified in an item key or named session.  
Plugins.MQTT.Sessions.<SessionName>.Password | no |  |  | Named session password.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MQTT.Sessions.<SessionName>.TLSCAFile | no |  |  | Full pathname of a file containing the top-level CA(s) certificates for peer certificate verification, used for encrypted communications between Zabbix agent 2 and MQTT broker.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MQTT.Sessions.<SessionName>.TLSCertFile | no |  |  | Full pathname of a file containing the agent certificate or certificate chain, used for encrypted communications between Zabbix agent 2 and MQTT broker.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MQTT.Sessions.<SessionName>.TLSKeyFile | no |  |  | Full pathname of a file containing the MQTT private key used for encrypted communications between Zabbix agent 2 and MQTT broker.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.MQTT.Sessions.<SessionName>.Topic | no |  |  | Named session topic for MQTT subscription.  
**< SessionName>** \- define name of a session for using in item keys.  
  
The topic may contain wildcards ("+","#")  
Examples: `path/to/file`  
`path/to/#`  
`path/+/topic`  
Plugins.MQTT.Sessions.<SessionName>.Url | no |  |  | Connection string of a named session.  
**< SessionName>** \- define name of a session for using in item keys.  
  
Should not include query parameters.  
Must match the URL format.  
Supported schemes: `tcp` (default), `ws`, `tls`; a scheme can be omitted.  
A port can be omitted (default=1883).  
Examples: `tcp://host:1883`  
`localhost`  
`ws://host:8080`  
Plugins.MQTT.Sessions.<SessionName>.User | no |  |  | Named session username.  
**< SessionName>** \- define name of a session for using in item keys.  
  
If you need to set the request execution timeout (how long to wait for a request to complete before shutting it down), use the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form.

See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)