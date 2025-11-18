---
title: New host
source: https://www.zabbix.com/documentation/current/en/manual/quickstart/host
downloaded: 2025-11-14 10:34:27
---

# 2 New host

#### Overview

In this section you will learn how to set up a new host.

A host in Zabbix is a networked entity (physical, virtual) that you wish to monitor. The definition of what can be a "host" in Zabbix is quite flexible. It can be a physical server, a network switch, a virtual machine or some application.

#### Adding host

Information about configured hosts in Zabbix is available in _Data collection > Hosts_ as well as _Monitoring_ > _Hosts_ menu sections. There is already one pre-defined host, called "Zabbix server", but we want to learn adding another.

To add a new host, click on _Create host_. This will present us with a host configuration form.  
![](/documentation/current/assets/en/manual/quickstart/new_host.png)

All mandatory input fields are marked with a red asterisk.

The bare minimum to enter here is:

**_Host name_**

  * Enter a host name. Alphanumerics, spaces, dots, dashes and underscores are allowed.

**_Host groups_**

  * Select one or several existing groups by clicking _Select_ button or enter a non-existing group name to create a new group.

All access permissions are assigned to host groups, not individual hosts. That is why a host must belong to at least one group.

**_Interfaces: IP address_**

  * Although not a required field technically, a host interface is necessary for collecting certain metrics. To use Zabbix agent passive checks, specify the agent's IP or DNS in this field. Note that you should also specify Zabbix server's IP or DNS in the Zabbix agent configuration file 'Server' directive. If Zabbix agent and Zabbix server are installed on the same machine, you need to specify the same IP/DNS in both places.

[Other options](/documentation/current/en/manual/config/hosts/host#configuration) will suit us with their defaults for now.

When done, click _Add_. Your new host should be visible in the host list.

![](/documentation/current/assets/en/manual/quickstart/host_list.png)

The Availability column contains indicators of host availability per each interface. We have defined a Zabbix agent interface, so we can use the agent availability icon (with 'ZBX' on it) to understand host availability:

  * ![icon_zbx_gray.png](/documentation/current/assets/en/manual/quickstart/icon_zbx_gray.png) \- host status has not been established; no metric check has happened yet
  * ![icon_zbx_green.png](/documentation/current/assets/en/manual/quickstart/icon_zbx_green.png) \- host is available, a metric check has been successful
  * ![icon_zbx_red.png](/documentation/current/assets/en/manual/quickstart/icon_zbx_red.png) \- host is unavailable, a metric check has failed (move your mouse cursor over the icon to see the error message). There might be some error with communication, possibly caused by incorrect interface credentials. Check that Zabbix server is running, and try refreshing the page later as well.