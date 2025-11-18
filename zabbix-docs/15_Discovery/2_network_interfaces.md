---
title: Discovery of network interfaces
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/network_interfaces
downloaded: 2025-11-14 10:37:27
---

# 2 Discovery of network interfaces

In a similar way as [file systems](/documentation/current/en/manual/discovery/low_level_discovery#configuring-low-level-discovery) are discovered, it is possible to also discover network interfaces.

#### Item key

The item key to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is
    
    
    net.if.discovery

Copy

✔ Copied

#### Supported macros

You may use the {#IFNAME} macro in the discovery rule [filter](/documentation/current/en/manual/discovery/low_level_discovery#filter) and prototypes of items, triggers and graphs.

Examples of item prototypes that you might wish to create based on "net.if.discovery":

  * "net.if.in[{#IFNAME},bytes]",
  * "net.if.out[{#IFNAME},bytes]".

Note that on Windows {#IFGUID} is also returned.