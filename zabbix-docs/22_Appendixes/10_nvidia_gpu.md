---
title: NVIDIA GPU plugin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/nvidia_gpu
downloaded: 2025-11-14 10:47:01
---

# 10 NVIDIA GPU plugin

#### Overview

This section lists parameters supported in the NVIDIA GPU Zabbix agent 2 plugin configuration file (nvidia.conf).

The NVIDIA GPU plugin is a loadable plugin and is available and fully described in the [NVIDIA GPU plugin repository](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse).

Note that:

  * The default values reflect process defaults, not the values in the shipped configuration files;
  * Values support [environment variables](/documentation/current/en/manual/appendix/config/environment_variables);
  * Zabbix supports configuration files only in UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark);
  * Comments starting with "#" are only supported at the beginning of the line.

#### Parameters

Plugins.NVIDIA.System.Path | no |  |  | Path to the NVIDIA GPU plugin executable.  
Example usage: `Plugins.NVIDIA.System.Path=/path/to/executable/nvidia`  
---|---|---|---|---  
Plugins.NVIDIA.Timeout | no | 1-30 | global timeout | Specifies the maximum time (in seconds) to wait for a server response during connection attempts and subsequent operations in the session. The global item-type timeout or individual item timeout will override this value if greater.  
  
See also:

  * Description of general Zabbix agent 2 configuration parameters: [Zabbix agent 2 (UNIX)](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Zabbix agent 2 (Windows)](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)
  * Instructions for configuring [plugins](/documentation/current/en/manual/extensions/plugins)