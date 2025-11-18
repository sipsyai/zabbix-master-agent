---
title: Discovery of block devices
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/devices
downloaded: 2025-11-14 10:37:38
---

# 14 Discovery of block devices

In a similar way as [file systems](/documentation/current/en/manual/discovery/low_level_discovery#configuring-low-level-discovery) are discovered, it is possible to also discover block devices and their type.

#### Item key

The item key to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is
    
    
    vfs.dev.discovery

Copy

✔ Copied

This item is supported on Linux platforms only.

You may create discovery rules using this discovery item and:

  * filter: **{#DEVNAME} matches`sd[\D]$`** \- to discover devices named "sd0", "sd1", "sd2", ...
  * filter: **{#DEVTYPE} matches`disk` AND {#DEVNAME} does not match `^loop.*`** \- to discover disk type devices whose name does not start with "loop"

#### Supported macros

This discovery key returns two macros - {#DEVNAME} and {#DEVTYPE} identifying the block device name and type respectively, e.g.:
    
    
    [ 
              { 
                 "{#DEVNAME}":"loop1",
                 "{#DEVTYPE}":"disk"
              },
              { 
                 "{#DEVNAME}":"dm-0",
                 "{#DEVTYPE}":"disk"
              },
              { 
                 "{#DEVNAME}":"sda",
                 "{#DEVTYPE}":"disk"
              },
              { 
                 "{#DEVNAME}":"sda1",
                 "{#DEVTYPE}":"partition"
              }
           ]

Copy

✔ Copied

Block device discovery allows to use `vfs.dev.read[]` and `vfs.dev.write[]` items to create item prototypes using the {#DEVNAME} macro, for example:

  * "vfs.dev.read[{#DEVNAME},sps]"
  * "vfs.dev.write[{#DEVNAME},sps]"

{#DEVTYPE} is intended for device filtering.