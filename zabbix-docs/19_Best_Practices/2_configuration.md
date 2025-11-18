---
title: Configuration best practices
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/configuration
downloaded: 2025-11-14 10:39:53
---

# 2 Configuration best practices

#### Overview

This section outlines best practices for configuring Zabbix to achieve optimal performance and ease of use. The recommendations are based on the advice of Zabbix developers and practical experience of Zabbix trainers and support engineers.

Every Zabbix installation is unique and some of these guidelines might not be suitable for your specific configuration. However, it is recommended to try to adhere to these guidelines as much as possible to avoid common potential issues.

If you believe this page could be improved, we'd love to hear from you! Please highlight the text in question and press **ctrl+Enter** to report a mistake or share your feedback.

### Hosts and items

##### Defining a host

A host in Zabbix is not a physical machine or device, but a logical entity. For monitoring purposes, you can create separate hosts for a database or, for example, a virtual machine. Alternatively, you can create a generic host _John's laptop_ and monitor all metrics under that host.

The best practice is to create a separate host for each independent instance such as a virtual machine, a database, a container, or a network switch. By utilizing this approach, you will:

  1. Avoid clutter in the monitoring data by having separate items, triggers, and alert notifications for each host.

  2. Fine-tune user-access levels. You can configure [user-roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) to grant access to viewing and/or configuring only specific hosts. See also [the principle of least privilege](/documentation/current/en/manual/best_practices/security/access_control#principle-of-least-privilege).

##### Hosts with duplicated items

If you have several similar hosts, such as _Network switch 1_ and _Network switch 2_ , Zabbix provides multiple ways to quickly recreate the host. You can simply clone a host with all of its metrics by pressing the Clone button, but in this case, to update an item later, you will need to do it manually on each host.

The best practice is to create a template with all of the required metrics, for example, _Network switch template_. Then group the similar hosts into a host group, for the example above it could be _Network switches_. Now, in the _Data Collection - > Hosts_ section you can filter all hosts by host group and use the _Mass update_ button to link the template to all of your network switches.

##### Dependent items

To minimize the number of requests to the target entity, Zabbix allows the creation of master and dependent items. In this case, the master item collects a large set of information in a single request. Then dependent items can be configured to extract specific pieces of data from that collection via preprocessing and store them as individual metrics.

For example, the master item might collect a JSON or XML response containing multiple metrics or execute a database query that returns multiple columns of data (e.g., number of open connections, aborted connections, maximum allowed simultaneous connections, and total cumulative connections since startup), and dependent items will parse and store each required value separately.

The best practice for this configuration is to discard master item's history right after collection and only keep the dependent items data.

#### Servers and proxies

If all hosts are in the same local network as the Zabbix server and there are no scalability or performance concerns, you may not need a proxy. In larger or more complex environments, directly monitoring hosts with the Zabbix server may not be sufficient. Adding a proxy and assigning part of the hosts to that proxy allows for a more even load distribution.

The best practice is to add a Zabbix proxy when:

  1. You are monitoring multiple hosts using various metric collection methods behind a firewall. The proxy will gather data from the hosts and forward it to the Zabbix server, reducing the need for opening multiple firewall ports.

  2. You are monitoring remote locations, branches, and/or networks. In case of a network interruption between the Zabbix server and your remote locations, the Zabbix proxies deployed in the remote locations will continue data collection and send the collected data back to the Zabbix server whenever the network connection is restored.

  3. You have a large-scale deployment and want to reduce the load on Zabbix server and improve performance. The definition of a large-scale deployment is very broad and depends not only on the number of hosts, but also on the number of values collected per second.

#### Secret macros

You may want to use [secret](/documentation/current/en/manual/config/macros/secret_macros) user macros as either secret text or secret vault macros.

For enhanced security when using secret vault macros it is recommended to [configure](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) macro values to be retrieved by Zabbix server and Zabbix proxies independently. By default secret macro values are retrieved by Zabbix server and propagated to Zabbix proxies.