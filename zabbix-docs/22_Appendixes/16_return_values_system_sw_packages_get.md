---
title: Return values for system.sw.packages.get
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/return_values_system_sw_packages_get
downloaded: 2025-11-14 10:47:34
---

# 16 Return values for system.sw.packages.get

#### Overview

This section provides return value details for the [`system.sw.packages.get`](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.sw.packages.get) Zabbix agent item.

#### Details

The output of this item is an array of objects each containing the following keys:

  * **name** \- package name
  * **manager** \- package manager that reported this data (`rpm`, `dpkg`, `pacman`, `pkgtool`, or `portage`)
  * **version** \- package version
  * **size** \- uncompressed package size in bytes (if not available, set to 0)
  * **arch** \- package architecture
  * **buildtime** \- an object with 2 entries: 
    * **timestamp** \- UNIX timestamp when the package was built (if not available, set to 0)
    * **value** \- human readable date and time when the package was built (if not available, set to empty string)
  * **installtime** \- an object with 2 entries: 
    * **timestamp** \- UNIX timestamp when the package was installed (if not available, set to 0)
    * **value** \- human readable date and time when the package was installed (if not available, set to empty string)

Example:
    
    
    [
               {
                   "name": "util-linux-core",
                   "manager": "rpm",
                   "version": "2.37.4-3.el9",
                   "size": 1296335,
                   "arch": "x86_64",
                   "buildtime": {
                       "timestamp" : 1653552239,
                       "value" : "Sep 20 01:39:40 2021 UTC"
                   },
                   "installtime": {
                       "timestamp" : 1660780885,
                       "value" : "Aug 18 00:01:25 2022 UTC"
                   }
               },
               {
                   "name": "xfonts-base",
                   "manager": "dpkg",
                   "version": "1:1.0.5",
                   "size": 7337984,
                   "arch": "all",
                   "buildtime": {
                       "timestamp": 0,
                       "value": ""
                   },
                   "installtime": {
                       "timestamp": 0,
                       "value": ""
                   }
               }
           ]

Copy

✔ Copied