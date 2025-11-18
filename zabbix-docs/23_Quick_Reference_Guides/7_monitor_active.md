---
title: Monitor network traffic using active checks
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_active
downloaded: 2025-11-14 10:48:09
---

# 7 Monitor network traffic using active checks

### Introduction

This page walks you through the steps required to start basic monitoring of your network traffic with Zabbix using active checks.

**Who this guide is for**

This guide is designed for new Zabbix users and contains the minimum set of steps required to enable basic monitoring of your network traffic using active checks. If you are looking for deep customization options or require more advanced configuration, see the [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this guide, you need to [download and install](https://www.zabbix.com/download) Zabbix server, Zabbix frontend and Zabbix agent according to the instructions for your OS. Note that you should install Zabbix agent on the machine that requires traffic monitoring. This can be either the same host where Zabbix server is installed or a different host.

This guide will provide the instructions on configuring the network traffic monitoring of _eth0_ interface on a separate machine named _Remote host_.

### Configure Zabbix for monitoring

Zabbix agent can collect metrics in active or passive mode (simultaneously). See [Passive and active agent checks](/documentation/current/en/manual/appendix/items/activepassive) for more info. In this guide, monitoring by means of **active checks** will be described.

##### Configuring Zabbix agent

1\. Open the agent configuration file on the machine where the agent is installed.

If you're using Zabbix agent:
    
    
    sudo vi /etc/zabbix/zabbix_agentd.conf

Copy

✔ Copied

If you're using Zabbix agent 2:
    
    
    sudo vi /etc/zabbix/zabbix_agent2.conf

Copy

✔ Copied

2\. Add the IP address or DNS name (and optional port) of your Zabbix server to the ServerActive parameter. For example:
    
    
    ServerActive=192.0.2.0:10051

Copy

✔ Copied

Zabbix agent will use this address to connect to Zabbix server's trapper port (default: 10051) and request the configuration data for active checks.

3\. Define the Hostname parameter, which must match the host name that will be defined in Zabbix frontend. In our example, it is:
    
    
    Hostname=Remote host

Copy

✔ Copied

The Hostname value must match because, for active checks, Zabbix agent uses it to retrieve the correct host configuration from the server. Specifically, the agent initiates a connection to the server and identifies itself using the Hostname value. The server then provides the monitoring configuration for that host. If these values differ, the agent will not receive the appropriate configuration, resulting in missing metrics or monitoring issues.

4\. Restart Zabbix agent.

If you're using Zabbix agent:
    
    
    systemctl restart zabbix-agent

Copy

✔ Copied

If you're using Zabbix agent 2:
    
    
    systemctl restart zabbix-agent2

Copy

✔ Copied

##### Zabbix frontend

1\. Log into Zabbix frontend.

2\. [Create a host](/documentation/current/en/manual/config/hosts/host) in Zabbix web interface.

  * In the _Host name_ field, enter a host name (e.g., "Remote host") that matches the Hostname parameter value defined earlier in the agent configuration file.
  * In the _Host groups_ field, type or select a host group (e.g., "Zabbix servers").
  * Leave _Interfaces_ undefined; an interface is not necessary for active checks because the agent initiates the connection to the server instead of listening for a connection from the server.

![](/documentation/current/assets/en/manual/guides/traffic_host.png)

3\. Click on _Add_ to add the host. This host will represent the monitored Linux machine.

### Create items

Follow the instructions on [creating an item](/documentation/current/en/manual/config/items/item) to add the items for traffic monitoring, namely:

  * [Incoming traffic](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.in)
  * [Outgoing traffic](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.out)
  * [Total traffic](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.total)

A simple setup for the incoming traffic monitoring item with an active check would look as follows:

![](/documentation/current/assets/en/manual/guides/traffic_item_active.png)

To make the collected data suitable for practical use, you can set some [preprocessing](/documentation/current/en/manual/config/items/preprocessing) steps when creating the items. In the given case, those can be multiplication by 8 (to convert bytes to bits) and presentation as change per second.

![](/documentation/current/assets/en/manual/guides/traffic_item_prepr.png)

### View collected data

Congratulations! At this point, Zabbix is already monitoring your network traffic.

To view collected metrics, open the [_Monitoring → Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) menu section and click on the _Latest data_ in the row of the host.

![](/documentation/current/assets/en/manual/guides/traffic_latest.png)

You will see the traffic data.

![](/documentation/current/assets/en/manual/guides/traffic_graph_active.png)

**See also:**

  * [View graphs](/documentation/current/en/manual/guides/monitor_traffic#view-graphs) \- how to display the collected data as graphs.
  * [Configure triggers](/documentation/current/en/manual/guides/monitor_traffic#configure-triggers) \- how to set up triggers to detect abnormal network traffic.
  * [Set up problem alerts](/documentation/current/en/manual/guides/monitor_traffic#set-up-problem-alerts) \- how to set up notifications about problem situations.
  * [Problem escalations](/documentation/current/en/manual/config/notifications/action/escalations) \- how to create multi-step alert scenarios (e.g., first send message to the system administrator, then, if a problem is not resolved in 45 minutes, send message to the data center manager).
  * [Problem acknowledgment](/documentation/current/en/manual/acknowledgment) \- how to indicate that the problem is known, make comments on resolving it, suppress or close the problem.
  * [Monitor Linux with Zabbix agent](/documentation/current/en/manual/guides/monitor_linux) \- how to start basic monitoring of the most important items by linking a pre-configured template.
  * [Installation from packages](/documentation/current/en/manual/installation/install_from_packages) \- how to install Zabbix components using official RPM and DEB packages for various Linux distributions, ensuring access to the latest features and bug fixes.