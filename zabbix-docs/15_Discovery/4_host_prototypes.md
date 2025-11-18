---
title: Host prototypes
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes
downloaded: 2025-11-14 10:37:22
---

# 4 Host prototypes

Host prototypes are blueprints for creating hosts through [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) rules. Before being discovered as hosts, these prototypes cannot have items and triggers, except those linked from templates.

#### Configuration

Host prototypes are configured under [low-level discovery rules](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule).

To create a host prototype:

1\. Go to [_Data collection_ → _Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts).

2\. Click _Discovery_ for the required host to navigate to the list of low-level discovery rules configured for that host.

3\. Click _Host prototypes_ for the required discovery rule.

4\. Click the _Create host prototype_ button in the upper-right corner.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/host_prototype.png)

Host prototypes have the same parameters as regular [hosts](/documentation/current/en/manual/config/hosts/host); however, the following parameters support different or additional configuration:

_Host name_ | This parameter must contain at least one [low-level discovery macro](/documentation/current/en/manual/config/macros/lld_macros) to ensure unique host names for created hosts.  
---|---  
_Visible name_ | [Low-level discovery macros](/documentation/current/en/manual/config/macros/lld_macros) are supported.  
_Group prototypes_ | Allows specifying host group prototypes by using [low-level discovery macros](/documentation/current/en/manual/config/macros/lld_macros).  
Based on the specified group prototypes, [host groups](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hostgroups) will be discovered, created and linked to the created hosts; discovered groups that have already been created by other low-level discovery rules will also be linked to the created hosts. However, discovered host groups that match [manually](/documentation/current/en/manual/config/hosts/host_groups) created host groups will not be linked to the created hosts.  
_Interfaces_ | Set whether discovered hosts inherit the IP from the host that the discovery rule belongs to (default), or get custom interfaces.  
[Low-level discovery macros](/documentation/current/en/manual/config/macros/lld_macros) and [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Create enabled_ | Set the status of discovered hosts; if unchecked, hosts will be created as disabled.  
_Discover_ | Set whether hosts will be created from the host prototype; if unchecked, hosts will not be created from the host prototype (unless this setting is [overridden](/documentation/current/en/manual/discovery/low_level_discovery#override) in the low-level discovery rule).  
  
[Low-level discovery macros](/documentation/current/en/manual/config/macros/lld_macros) are also supported for tag values and host prototype user macro values.  
_Value maps_ are not supported for host prototypes.

For an example of how to configure a host prototype, see [_Virtual machine monitoring_](/documentation/current/en/manual/vm_monitoring#configuration-examples).

##### Host interfaces

To add custom interfaces, switch the _Interfaces_ selector from "Inherit" to "Custom". Click ![add_link.png](/documentation/current/assets/en/manual/config/add_link.png) and select the interface type - Zabbix agent, SNMP, JMX, IPMI.

If _Custom_ is selected, but no interfaces have been set, the hosts will be created without interfaces.  
If _Inherit_ is selected and the host prototype belongs to a template, all discovered hosts will inherit the host interface from the host to which the template is linked.

If multiple custom interfaces are specified, the primary interface can be set in the _Default_ column.

For an example of how to configure a custom host interface, see [_VMware monitoring setup example_](/documentation/current/en/manual/vm_monitoring/example#advanced-host-interface-configuration).

A host will only be created if a host interface contains correct data.

##### Discovered hosts

In the host list, discovered hosts are prefixed with the name of the discovery rule that created them.

Discovered hosts inherit most parameters from host prototypes as _read-only_. Only the following discovered host parameters can be configured:

  * _Templates_ \- link new templates or unlink manually added ones. Templates inherited from a host prototype cannot be unlinked.
  * _Description_ \- add or edit the host description.
  * _Status_ \- enable or disable the host.
  * _Tags_ \- add new tags or remove manually added ones. Tags inherited from a host prototype cannot be removed. Note that tags cannot have duplicates (tags with the same name and value). If a new tag is added to the host prototype and it matches a manually added tag on a discovered host, the manually added tag will be replaced with the inherited tag during discovery.
  * _Macros_ \- add new host macros or remove manually added ones, as well as those inherited from a host prototype; change macro values and [types](/documentation/current/en/manual/config/macros/user_macros#configuration).

Discovered hosts also inherit [user macros](/documentation/current/en/manual/config/macros/user_macros) from the host where the discovery rule is configured. These inherited macros can be removed, and their values and types can be changed.

Discovered hosts can also discover other hosts. For example, if a host prototype (used to discover hypervisors) has a template linked to it that includes a low-level discovery rule with its own host prototype (used to discover virtual machines), Zabbix will discover both hypervisors and their virtual machines. To additionally discover containers on those VMs, you can create low-level discovery rules or link a new template with host prototypes to the discovered VMs or pre-configure the VM host prototype by linking a template that itself includes host prototypes.

Discovered hosts can be deleted manually. Note, however, that they will be discovered again if discovery is enabled for them.

Hosts that are no longer discovered may be:

  * automatically disabled (based on the _Disable lost resources_ value of the discovery rule)
  * automatically deleted (based on the _Delete lost resources_ value of the discovery rule).