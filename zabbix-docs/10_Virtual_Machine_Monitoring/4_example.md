---
title: VMware monitoring setup example
source: https://www.zabbix.com/documentation/current/en/manual/vm_monitoring/example
downloaded: 2025-11-14 10:37:00
---

# 4 VMware monitoring setup example

#### Overview

The following example describes how to set up Zabbix for monitoring VMware virtual machines. This involves:

  * creating a host that represents your VMware environment;
  * creating a low-level discovery rule that discovers virtual machines in your VMware environment;
  * creating a host prototype, based on which Zabbix will generate real hosts for virtual machines discovered by the low-level discovery rule.

#### Prerequisites

This example does not cover the configuration of VMware. It is assumed that VMware is already configured.

Before proceeding, set the [`StartVMwareCollectors`](/documentation/current/en/manual/appendix/config/zabbix_server#startvmwarecollectors) parameter in Zabbix server configuration file to `2` [or more](/documentation/current/en/manual/vm_monitoring#configuration) (the default value is `0`).

#### Create a host

1\. Go to _Data collection_ → [_Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts).

2\. [Create](/documentation/current/en/manual/config/hosts/host) a host:

  * In the _Host name_ field, enter a host name (for example, "VMware VMs").
  * In the _Host groups_ field, type or select a host group (for example, "Virtual machines").

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_host.png)

  * In the _Macros_ tab, set the following host macros: 
    * {$VMWARE.URL} - VMware service (ESXi hypervisor) SDK URL (https://servername/sdk)
    * {$VMWARE.USERNAME} - VMware service user name
    * {$VMWARE.PASSWORD} - VMware service {$VMWARE.USERNAME} user password

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_host_macros.png)

3\. Click the _Add_ button to create the host. This host will represent your VMware environment.

#### Create a low-level discovery rule

1\. Click _Discovery_ for the created host to go to the list of low-level discovery rules for that host.

2\. [Create](/documentation/current/en/manual/discovery/low_level_discovery#configuring-low-level-discovery) a low-level discovery rule:

  * In the _Name_ field, enter a low-level discovery rule name (for example, "Discover VMware VMs").
  * In the _Type_ field, select "[Simple check](/documentation/current/en/manual/config/items/itemtypes/simple_checks)".
  * In the _Key_ field, enter the built-in item key for discovering VMware virtual machines: [`vmware.vm.discovery[{$VMWARE.URL}]`](/documentation/current/en/manual/vm_monitoring/vmware_keys#vmware.vm.discovery)
  * In the _User name_ and _Password_ fields, enter the corresponding macros previously configured on the host.

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_host_discovery.png)

3\. Click the _Add_ button to create the low-level discovery rule. This discovery rule will discover virtual machines in your VMware environment.

#### Create a host prototype

1\. In the list of low-level discovery rules, click _Host prototypes_ for the previously created low-level discovery rule.

2\. [Create](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes#configuration) a host prototype. Since host prototypes are blueprints for creating hosts through low-level discovery rules, most fields will contain [low-level discovery macros](/documentation/current/en/manual/config/macros/lld_macros). This ensures that the hosts are created with properties based on the [content retrieved](/documentation/current/en/manual/vm_monitoring/discovery_fields) by the previously created low-level discovery rule.

  * In the _Host name_ field, enter the macro {#VM.UUID}.
  * In the _Visible name_ field, enter the macro {#VM.NAME}.
  * In the _Templates_ field, enter or select the "VMware Guest" template. This template contains [VMware items](/documentation/current/en/manual/vm_monitoring/vmware_keys) and discovery rules for monitoring the power state of a virtual machine, CPU usage, memory usage, network devices, etc.
  * In the _Host groups_ field, enter or select a host group (for example, "Discovered hosts").
  * In the _Interfaces_ field, add a custom [host interface](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes#host-interfaces). Then, enter the macro {#VM.DNS} in the _DNS name_ field, or enter the macro {#VM.IP} in the _IP address_ field. Alternatively, if your VMware environment virtual machines have multiple interfaces, proceed to the _Advanced host interface configuration_ section. Configuring a custom host interface is necessary for the correct functioning of the _VMware Guest_ template.

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_host_prototype.png)

  * In the _Macros_ tab, set the {$VMWARE.VM.UUID} macro with the value {#VM.UUID}. This is necessary for the correct functioning of the _VMware Guest_ template that uses this macro as a host-level user macro in item parameters (for example, _vmware.vm.net.if.discovery[{$VMWARE.URL}, {$VMWARE.VM.UUID}]_).

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_host_prototype_macros.png)

3\. Click the _Add_ button to create the host prototype. This host prototype will be used to create hosts for virtual machines discovered by the previously created low-level discovery rule.

#### View hosts and metrics

After the host prototype has been created, the low-level discovery rule will create hosts for discovered VMware virtual machines, and Zabbix will start to monitor them. Note that the discovery and creation of hosts can also be [executed manually](/documentation/current/en/manual/config/items/check_now), if necessary.

To view the created hosts, navigate to the [_Data collection_ → _Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts) menu section.

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_discovered_hosts.png)

To view collected metrics, navigate to the [_Monitoring_ → _Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) menu section and click _Latest data_ for one of the hosts.

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_monitored_hosts.png)

#### Advanced host interface configuration

The `vmware.vm.discovery[{$VMWARE.URL}]` item key, configured in the _Create a low-level discovery rule_ section, returns network interfaces data in the ["net_if" field](/documentation/current/en/manual/vm_monitoring/discovery_fields):
    
    
    "net_if": [
                 {
                   "ifname": "5000",
                   "ifdesc": "Network adapter 1",
                   "ifmac": "00:11:22:33:44:55",
                   "ifconnected": true,
                   "iftype": "VirtualVmxnet3",
                   "ifbackingdevice": "VLAN(myLab)",
                   "ifdvswitch_uuid": "",
                   "ifdvswitch_portgroup": "",
                   "ifdvswitch_port": "",
                   "ifip": [
                     "127.0.0.1",
                     "::1"
                   ]
                 },
                 {
                   "ifname": "5001",
                   "ifdesc": "Network adapter 2",
                   "ifmac": "00:11:22:33:44:55",
                   "ifconnected": false,
                   "iftype": "VirtualVmxnet3",
                   "ifbackingdevice": "VLAN(myLab2)",
                   "ifdvswitch_uuid": "",
                   "ifdvswitch_portgroup": "",
                   "ifdvswitch_port": "",
                   "ifip": []
                 }
               ]

Copy

✔ Copied

This data can be used to configure a custom host interface.

1\. When creating a low-level discovery rule, additionally configure a [low-level discovery macro](/documentation/current/en/manual/config/macros/lld_macros). In the _LLD macros_ tab, create a custom LLD macro with a [JSONPath](/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality) value. For example:

  * {#MYLAB.NET.IF} - `$.net_if[?(@.ifbackingdevice=="VLAN(myLab)")].ifip[0].first()`

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_lld_macro.png)

2\. When creating a host prototype, add a custom host interface and enter the LLD macro in the _DNS name_ or _IP address_ field.

![](/documentation/current/assets/en/manual/vm_monitoring/vmware_lld_macro_host_prototype.png)