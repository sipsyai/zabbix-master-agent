---
title: Discovery using WMI queries
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/wmi
downloaded: 2025-11-14 10:37:35
---

# 11 Discovery using WMI queries

#### Overview

[WMI](https://en.wikipedia.org/wiki/Windows_Management_Instrumentation) is a powerful interface in Windows that can be used for retrieving various information about Windows components, services, state and software installed.

It can be used for physical disk discovery and their performance data collection, network interface discovery, Hyper-V guest discovery, monitoring Windows services and many other things in Windows OS.

This type of low-level [discovery](/documentation/current/en/manual/discovery/low_level_discovery) is done using WQL queries whose results get automatically transformed into a JSON object suitable for low-level discovery.

#### Item key

The item to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is
    
    
    wmi.getall[<namespace>,<query>]

Copy

✔ Copied

This [item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys) transforms the query result into a JSON array. For example:
    
    
    select * from Win32_DiskDrive where Name like '%PHYSICALDRIVE%'

Copy

✔ Copied

may return something like this:
    
    
    [
               {
                   "DeviceID" : "\\.\PHYSICALDRIVE0",
                   "BytesPerSector" : 512,
                   "Capabilities" : [
                       3,
                       4
                   ],
                   "CapabilityDescriptions" : [
                       "Random Access",
                       "Supports Writing"
                   ],
                   "Caption" : "VBOX HARDDISK ATA Device",
                   "ConfigManagerErrorCode" : 0,
                   "ConfigManagerUserConfig" : "False",
                   "CreationClassName" : "Win32_DiskDrive",
                   "Description" : "Disk drive",
                   "FirmwareRevision" : "1.0",
                   "Index" : 0,
                   "InterfaceType" : "IDE"
               },
               {
                   "DeviceID" : "\\.\PHYSICALDRIVE1",
                   "BytesPerSector" : 512,
                   "Capabilities" : [
                       3,
                       4
                   ],
                   "CapabilityDescriptions" : [
                       "Random Access",
                       "Supports Writing"
                   ],
                   "Caption" : "VBOX HARDDISK ATA Device",
                   "ConfigManagerErrorCode" : 0,
                   "ConfigManagerUserConfig" : "False",
                   "CreationClassName" : "Win32_DiskDrive",
                   "Description" : "Disk drive",
                   "FirmwareRevision" : "1.0",
                   "Index" : 1,
                   "InterfaceType" : "IDE"
               }
           ]

Copy

✔ Copied

#### Low-level discovery macros

Even though no low-level discovery macros are created in the returned JSON, these macros can be defined by the user as an additional step, using the [custom LLD macro](/documentation/current/en/manual/discovery/low_level_discovery#custom-macros) functionality with JSONPath pointing to the discovered values in the returned JSON.

The macros then can be used to create item, trigger, etc prototypes.