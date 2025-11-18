---
title: Ember+ plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/ember_plus_plugin
downloaded: 2025-11-14 10:46:54
---

# 3 Ember+ plugin

#### Overview

This section lists parameters supported in the Ember+ Zabbix agent 2 plugin configuration file (ember.conf).

The Ember+ plugin is a loadable plugin and is available and fully described in the [Ember+ plugin repository](https://git.zabbix.com/projects/AP/repos/ember-plus/browse).

This plugin is currently only available to be built from the source (for both Unix and Windows).

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

Plugins.EmberPlus.Default.Uri | no |  | tcp://localhost:9998 | The default URI to connect. The only supported schema is `tcp://`. A schema can be omitted. Embedded credentials will be ignored.  
---|---|---|---|---  
Plugins.EmberPlus.KeepAlive | no | 60-900 | 300 | The maximum time of waiting (in seconds) before unused plugin connections are closed.  
Plugins.EmberPlus.Sessions.<SessionName>.Uri | no |  | tcp://localhost:9998 | The URI to connect, for the named session. The only supported schema is `tcp://`. A schema can be omitted. Embedded credentials will be ignored.  
**< SessionName>** \- define name of a session for using in item keys.  
Plugins.EmberPlus.System.Path | no |  |  | Path to the Ember+ plugin executable.  
Example usage: `Plugins.EmberPlus.System.Path=/usr/libexec/zabbix/zabbix-agent2-plugin-ember-plus`  
Plugins.EmberPlus.Timeout | no | 1-30 | global timeout | The duration, in seconds, to wait for a server to respond when first connecting and on follow-up operations in the session.  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)