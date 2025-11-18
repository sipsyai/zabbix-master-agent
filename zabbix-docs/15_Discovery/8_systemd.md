---
title: Discovery of systemd services
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/systemd
downloaded: 2025-11-14 10:37:33
---

# 8 Discovery of systemd services

### Overview

It is possible to [discover](/documentation/current/en/manual/discovery/low_level_discovery) systemd units (services, by default) with Zabbix.

### Item key

The item to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is the
    
    
    systemd.unit.discovery

Copy

✔ Copied

This [item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) key is only supported in Zabbix agent 2.

This item returns a JSON with information about systemd units, for example:
    
    
    [{
               "{#UNIT.NAME}": "mysqld.service",
               "{#UNIT.DESCRIPTION}": "MySQL Server",
               "{#UNIT.LOADSTATE}": "loaded",
               "{#UNIT.ACTIVESTATE}": "active",
               "{#UNIT.SUBSTATE}": "running",
               "{#UNIT.FOLLOWED}": "",
               "{#UNIT.PATH}": "/org/freedesktop/systemd1/unit/mysqld_2eservice",
               "{#UNIT.JOBID}": 0,
               "{#UNIT.JOBTYPE}": "",
               "{#UNIT.JOBPATH}": "/",
               "{#UNIT.UNITFILESTATE}": "enabled"
               "{#UNIT.SERVICETYPE}": "simple"
           }, {
               "{#UNIT.NAME}": "systemd-journald.socket",
               "{#UNIT.DESCRIPTION}": "Journal Socket",
               "{#UNIT.LOADSTATE}": "loaded",
               "{#UNIT.ACTIVESTATE}": "active",
               "{#UNIT.SUBSTATE}": "running",
               "{#UNIT.FOLLOWED}": "",
               "{#UNIT.PATH}": "/org/freedesktop/systemd1/unit/systemd_2djournald_2esocket",
               "{#UNIT.JOBID}": 0,
               "{#UNIT.JOBTYPE}": "",
               "{#UNIT.JOBPATH}": "/",
               "{#UNIT.UNITFILESTATE}": "enabled"
           }]

Copy

✔ Copied

##### Discovery of disabled systemd units

It is also possible to discover **disabled** systemd units. In this case three macros are returned in the resulting JSON:

  * {#UNIT.PATH}
  * {#UNIT.ACTIVESTATE}
  * {#UNIT.UNITFILESTATE}.

To have items and triggers created from prototypes for disabled systemd units, make sure to adjust (or remove) prohibiting LLD filters for {#UNIT.ACTIVESTATE} and {#UNIT.UNITFILESTATE}.

### Supported macros

The following macros are supported for use in the discovery rule [filter](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule-filter) and prototypes of items, triggers and graphs:

{#UNIT.NAME} | Primary unit name.  
---|---  
{#UNIT.DESCRIPTION} | Human readable description.  
{#UNIT.LOADSTATE} | Load state (i.e. whether the unit file has been loaded successfully)  
{#UNIT.ACTIVESTATE} | Active state (i.e. whether the unit is currently started or not)  
{#UNIT.SUBSTATE} | Sub state (a more fine-grained version of the active state that is specific to the unit type, which the active state is not)  
{#UNIT.FOLLOWED} | Unit that is being followed in its state by this unit, if there is any; otherwise an empty string.  
{#UNIT.PATH} | Unit object path.  
{#UNIT.JOBID} | Numeric job ID if there is a job queued for the job unit; `0` otherwise.  
{#UNIT.JOBTYPE} | Job type.  
{#UNIT.JOBPATH} | Job object path.  
{#UNIT.UNITFILESTATE} | The install state of the unit file.  
{#UNIT.SERVICETYPE} | Type of the service unit (e.g., `simple`, `forking`, `oneshot`, `idle`, etc.). This macro is returned only if the unit is a service.  
  
### Item prototypes

Item prototypes that can be created based on systemd service discovery include, for example:

  * Item name: `{#UNIT.DESCRIPTION} active state info`; item key: `systemd.unit.info["{#UNIT.NAME}"]`
  * Item name: `{#UNIT.DESCRIPTION} load state info`; item key: `systemd.unit.info["{#UNIT.NAME}",LoadState]`