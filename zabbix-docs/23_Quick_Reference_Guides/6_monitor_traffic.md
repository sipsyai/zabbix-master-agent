---
title: Monitor network traffic with Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_traffic
downloaded: 2025-11-14 10:48:08
---

# 6 Monitor network traffic with Zabbix

### Introduction

This page walks you through the steps required to start basic monitoring of your network traffic with Zabbix.

**Who this guide is for**

This guide is designed for new Zabbix users and contains the minimum set of steps required to enable basic monitoring of your network traffic. If you are looking for deep customization options or require more advanced configuration, see the [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this guide, you need to [download and install](https://www.zabbix.com/download) Zabbix server, Zabbix frontend and Zabbix agent according to the instructions for your OS. Note that you should install Zabbix agent on the machine that requires traffic monitoring. This can be either the same host where Zabbix server is installed or a different host.

This guide will provide the instructions on configuring the network traffic monitoring of _eth0_ interface on a separate machine named _Remote host_.

### Configure Zabbix for monitoring

Zabbix agent can collect metrics in active or passive mode (simultaneously). See [Passive and active agent checks](/documentation/current/en/manual/appendix/items/activepassive) for more info. In this guide, monitoring by means of passive checks will be described.

##### Configuring Zabbix agent

1\. Open the agent configuration file on the machine where the agent is installed (by default, the path is _/usr/local/etc/zabbix_agentd.conf_):
    
    
    sudo vi /usr/local/etc/zabbix_agentd.conf

Copy

✔ Copied

2\. Add the IP address or DNS name of your Zabbix server to the _Server_ parameter. For example:
    
    
    Server=192.0.2.22

Copy

✔ Copied

3\. Restart Zabbix agent:
    
    
    systemctl restart zabbix-agent

Copy

✔ Copied

##### Zabbix frontend

1\. Log into Zabbix frontend.

2\. [Create a host](/documentation/current/en/manual/config/hosts/host) in Zabbix web interface, specifying the IP address or DNS name of the machine on which the agent is installed.

![](/documentation/current/assets/en/manual/guides/traffic_host.png)

### Create items

Follow the instructions on [creating an item](/documentation/current/en/manual/config/items/item) to add the items for traffic monitoring, namely:

  * [Incoming traffic](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.in)
  * [Outgoing traffic](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.out)
  * [Total traffic](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.if.total)

A simple setup for the incoming traffic monitoring item would look as follows:

![](/documentation/current/assets/en/manual/guides/traffic_item.png)

To make the collected data suitable for practical use, you can set some [preprocessing](/documentation/current/en/manual/config/items/preprocessing) steps when creating the items. In the given case, those can be multiplication by 8 (to convert bytes to bits) and presentation as change per second.

![](/documentation/current/assets/en/manual/guides/traffic_item_prepr.png)

### View collected data

Congratulations! At this point, Zabbix is already monitoring your network traffic.

To view collected metrics, open the [_Monitoring → Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) menu section and click on the _Latest data_ in the row of the host.

![](/documentation/current/assets/en/manual/guides/traffic_latest.png)

You will see the traffic data.

![](/documentation/current/assets/en/manual/guides/traffic_graph.png)

### View graphs

The data collected can be displayed as [graphs](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts/graphs). To view those, in the _Latest data_ section click on _Graph_ in the row of the item or select required items and click on _Display graph_ below.

![](/documentation/current/assets/en/manual/guides/traffic_graph2.png)

### Configure triggers

You can set [triggers](/documentation/current/en/manual/config/triggers) to detect abnormal network traffic. See the instructions on [configuring a trigger](/documentation/current/en/manual/config/triggers/trigger) and add the trigger signalling that the total traffic is too high, for example:

![](/documentation/current/assets/en/manual/guides/traffic_trigger.png)

Now make the traffic exceed the threshold you have set in the trigger expression and navigate to the _Monitoring → Problems_ to check that the problem is listed there.

![](/documentation/current/assets/en/manual/guides/traffic_problem.png)

### Set up problem alerts

There are several ways of getting notifications about the problem. Email being the most popular one, follow the instructions on setting up a [problem notification](/documentation/current/en/manual/quickstart/notification) via email. You can also choose other [media types](/documentation/current/en/manual/config/notifications/media) to be used for the notification delivery.

**See also:**

  * [Problem escalations](/documentation/current/en/manual/config/notifications/action/escalations) \- how to create multi-step alert scenarios (e.g., first send message to the system administrator, then, if a problem is not resolved in 45 minutes, send message to the data center manager).
  * [Problem acknowledgment](/documentation/current/en/manual/acknowledgment) \- how to indicate that the problem is known, make comments on resolving it, suppress or close the problem.
  * [Monitor Linux with Zabbix agent](/documentation/current/en/manual/guides/monitor_linux) \- how to start basic monitoring of the most important items by linking a pre-configured template.