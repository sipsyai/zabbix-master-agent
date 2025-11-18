---
title: Discovery of Windows services
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_services
downloaded: 2025-11-14 10:37:34
---

# 9 Discovery of Windows services

#### Overview

In a similar way as [file systems](/documentation/current/en/manual/discovery/low_level_discovery#configuring-low-level-discovery) are discovered, it is possible to also discover Windows services.

#### Item key

The item to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is
    
    
    service.discovery

Copy

✔ Copied

#### Supported macros

The following macros are supported for use in the discovery rule [filter](/documentation/current/en/manual/discovery/low_level_discovery#filter) and prototypes of items, triggers and graphs:

{#SERVICE.NAME} | Service name.  
---|---  
{#SERVICE.DISPLAYNAME} | Displayed service name.  
{#SERVICE.DESCRIPTION} | Service description.  
{#SERVICE.STATE} | Numerical value of the service state.  
See the [service.info](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys#service-info) item for details.  
{#SERVICE.STATENAME} | Name of the service state.  
See the [service.info](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys#service-info) item for details.  
{#SERVICE.PATH} | Service path.  
{#SERVICE.USER} | Service user.  
{#SERVICE.STARTUP} | Numerical value of the service startup type.  
See the [service.info](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys#service-info) item for details.  
{#SERVICE.STARTUPNAME} | Name of the service startup type.  
See the [service.info](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys#service-info) item for details.  
{#SERVICE.STARTUPTRIGGER} | Numerical value to indicate if the service startup type has:  
0 - no startup triggers  
1 - has startup triggers  
It is useful to discover such service startup types as _Automatic (trigger start)_ , _Automatic delayed (trigger start)_ and _Manual (trigger start)._  
  
  
Based on Windows service discovery you may create an [item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys) prototype like
    
    
    service.info[{#SERVICE.NAME},<param>]

Copy

✔ Copied

where `param` accepts the following values: _state_ , _displayname_ , _path_ , _user_ , _startup_ or _description_.

For example, to acquire the display name of a service you may use a "service.info[{#SERVICE.NAME},displayname]" item. If `param` value is not specified ("service.info[{#SERVICE.NAME}]"), the default _state_ parameter is used.