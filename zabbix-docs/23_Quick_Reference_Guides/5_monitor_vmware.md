---
title: Monitor VMware with Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_vmware
downloaded: 2025-11-14 10:48:07
---

# 5 Monitor VMware with Zabbix

#### Introduction

This page walks you through the steps required to start basic monitoring of VMware.

**Who this guide is for**

This guide is designed for new Zabbix users and contains the minimum set of steps required to enable basic monitoring of VMware. If you are looking for deep customization options or require more advanced configuration, see the [Virtual machine monitoring](/documentation/current/en/manual/vm_monitoring) section or the [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this guide, you need to [download and install](https://www.zabbix.com/download) Zabbix server and Zabbix frontend according to the instructions for your OS.

This guide is based on the following setup:

  * Zabbix version: 7.2 PRE-RELEASE (installed from packages)
  * OS distribution: Ubuntu
  * OS version: 22.04 (Jammy)
  * Zabbix components: Server, Frontend, Agent
  * Database: MySQL
  * Web server: Apache

It is assumed that VMware is already configured. This guide does not cover the configuration of VMware.

#### Configure Zabbix server

To monitor VMware, the _vmware collector_ Zabbix processes need to be enabled. For more information on how VMware monitoring is performed, see [Virtual machine monitoring](/documentation/current/en/manual/vm_monitoring#data-collection).

1\. Open the Zabbix server configuration file.
    
    
    vi /etc/zabbix/zabbix_server.conf

Copy

✔ Copied

2\. Locate and set the [`StartVMwareCollectors`](/documentation/current/en/manual/appendix/config/zabbix_server#startvmwarecollectors) parameter in Zabbix server configuration file to `2` [or more](/documentation/current/en/manual/vm_monitoring#configuration) (the default value is `0`).
    
    
    ### Option: StartVMwareCollectors
           #       Number of pre-forked vmware collector instances.
           #
           # Mandatory: no
           # Range: 0-250
           # Default:
           # StartVMwareCollectors=0
           
           StartVMwareCollectors=2

Copy

✔ Copied

3\. Restart Zabbix server.
    
    
    systemctl restart zabbix-server

Copy

✔ Copied

Once the _vmware collector_ processes have been started, move on to the next step.

#### Configure Zabbix frontend

1\. Log into Zabbix frontend.

2\. [Create a host](/documentation/current/en/manual/config/hosts/host) in Zabbix web interface:

  * In the _Host name_ field, enter a host name (for example, "VMware environment").
  * In the _Templates_ field, type or select the "VMware FQDN" (or "VMware") template. For more information on these templates, see [Virtual machine monitoring](/documentation/current/en/manual/vm_monitoring#ready-to-use-templates).
  * In the _Host groups_ field, type or select a host group (for example, a new host group "VMware").

![](/documentation/current/assets/en/manual/guides/vmware_host.png)

  * In the _Macros_ tab, set the following host macros: 
    * {$VMWARE.URL} - VMware service (vCenter or ESXi hypervisor) SDK URL (https://servername/sdk)
    * {$VMWARE.USERNAME} - VMware service user name
    * {$VMWARE.PASSWORD} - VMware service {$VMWARE.USERNAME} user password

![](/documentation/current/assets/en/manual/guides/vmware_macros.png)

3\. Click the _Add_ button to create the host. This host will represent your VMware environment.

#### View collected metrics

Congratulations! At this point, Zabbix is already monitoring your VMware environment.

Depending on the configuration of your VMware environment, Zabbix may [discover](/documentation/current/en/manual/vm_monitoring#discovery) and then create hosts for the discovered entities. Note that the discovery and creation of hosts can also be [executed manually](/documentation/current/en/manual/config/items/check_now), if necessary.

To view created hosts, navigate to the [_Data collection → Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts) menu section.

![](/documentation/current/assets/en/manual/guides/vmware_discovered_hosts.png)

To view collected metrics, navigate to the [_Monitoring → Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) menu section and click _Latest data_ next to the created "VMware environment" host or one of the hosts that were created for the discovered entities.

![](/documentation/current/assets/en/manual/guides/vmware_monitored_hosts.png)

This action will open a list of all the latest metrics collected from the selected host.

![](/documentation/current/assets/en/manual/guides/vmware_latest_data.png)

Note that some items have no data and the _Not supported_ state. This is because Zabbix cannot find valid [performance counters](/documentation/current/en/manual/vm_monitoring/vmware_keys#footnotes) on the specific datastore, as it is not enabled in the VMware environment being monitored.

#### Set up problem alerts

Zabbix can notify you about a problem with your infrastructure using a variety of methods. This guide provides basic configuration steps for sending email alerts.

1\. Navigate to [_User settings → Profile_](/documentation/current/en/manual/web_interface/user_profile), switch to the _Media_ tab and [add your email](/documentation/current/en/manual/quickstart/login#adding-user).

![](/documentation/current/assets/en/manual/quickstart/new_media.png)

2\. Follow the guide for [Receiving a problem notification](/documentation/current/en/manual/quickstart/notification).

Next time, when Zabbix detects a problem, you should receive an alert via email.

#### See also

  * [Creating an item](/documentation/current/en/manual/config/items/item) \- how to start monitoring additional metrics.
  * [Problem escalations](/documentation/current/en/manual/config/notifications/action/escalations) \- how to create multi-step alert scenarios (e.g., first send message to the system administrator, then, if a problem is not resolved in 45 minutes, send message to the data center manager).
  * [Virtual machine monitoring](/documentation/current/en/manual/vm_monitoring#ready-to-use-templates) \- additional information about VMware monitoring (data collection process, server configuration options, troubleshooting guidance, etc.).
  * [VMware monitoring item keys](/documentation/current/en/manual/vm_monitoring/vmware_keys) \- a full list of VMware metrics that can be monitored using Zabbix.
  * Template [_VMware_](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vmware?at=refs%2Fheads%2Frelease%2F7.4) \- additional information about the _VMware_ template.
  * Template [_VMware FQDN_](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vmware_fqdn?at=refs%2Fheads%2Frelease%2F7.4) \- additional information about the _VMware FQDN_ template.