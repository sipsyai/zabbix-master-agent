---
title: VMware template operation
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box/vmware
downloaded: 2025-11-14 10:36:08
---

# 8 VMware template operation

#### Overview

Zabbix includes a range of ready-to-use templates for [virtual machine monitoring](/documentation/current/en/manual/vm_monitoring), designed for VMware vCenter and ESXi hypervisors. The available templates are contained in two separate template sets:

  * [VMware](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vmware/README.md?at=refs%2Fheads%2Frelease%2F7.4) \- uses UUID data for corresponding macros
  * [VMware FQDN](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vmware_fqdn/README.md?at=refs%2Fheads%2Frelease%2F7.4) \- uses FQDN data for corresponding macros

The templates designed for monitoring VMware vCenter or ESXi hypervisors contain pre-configured low-level discovery rules along with various built-in checks for monitoring virtual installations.

For the correct functioning of the _VMware FQDN_ template, each monitored virtual machine should have a unique OS name adhering to FQDN rules. Additionally, VMware Tools/Open Virtual Machine tools must be installed on every machine. If these prerequisites are met, using the _VMware FQDN_ template is recommended. The _VMware FQDN_ template has been available since Zabbix 5.2 with the introduction of the ability to create hosts with custom interfaces.   
  
A classic _VMware_ template is also available and can be used if FQDN requirements are unmet. However, the _VMware_ template has a known issue. Hosts for discovered virtual machines are created with names that are saved in vCenter (for example, "VM1", "VM2", etc.). If Zabbix agent is installed on these hosts, and active Zabbix agent autoregistration is enabled, the autoregistration process will read host names as they were registered during launch (for example, "vm1.example.com", "vm2.example.com", etc.). This can lead to the creation of new hosts for existing virtual machines (since no name matches have been found), resulting in duplicate hosts with different names.

Please note:

  * The template _VMware Hypervisor_ can be manually linked to a host as well as used in discovery;
  * The template _VMware Guest_ should not be manually linked to a host and can only be used in discovery.

#### Host macro configuration

To use VMware simple checks, the host must have the following user macros defined:

  * {$VMWARE.URL} - VMware service (vCenter or ESXi hypervisor) SDK URL (https://servername/sdk)
  * {$VMWARE.USERNAME} - VMware service user name
  * {$VMWARE.PASSWORD} - VMware service {$VMWARE.USERNAME} user password