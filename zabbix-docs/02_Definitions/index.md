---
title: Definitions
source: https://www.zabbix.com/documentation/current/en/manual/definitions
downloaded: 2025-11-14 10:33:46
---

# 2 Definitions

#### Overview

In this section you can learn the meaning of some terms commonly used in Zabbix.

#### Definitions

**_[host](/documentation/current/en/manual/config/hosts)_**

\- _any physical or virtual device, application, service, or any other logically-related collection of monitored parameters._

**_[host group](/documentation/current/en/manual/config/hosts)_**

\- _a logical grouping of hosts. Host groups are used when assigning access rights to hosts for different user groups._

**_[item](/documentation/current/en/manual/config/items)_**

\- _a particular piece of data that you want to receive from a host, a metric of data._

**_[value preprocessing](/documentation/current/en/manual/config/items/item#item-value-preprocessing)_**

\- _a transformation of received metric value_ before saving it to the database.

**_[trigger](/documentation/current/en/manual/config/triggers)_**

\- _a logical expression that defines a problem threshold and is used to "evaluate" data received in items._

When received data are above the threshold, triggers go from 'Ok' into a 'Problem' state. When received data are below the threshold, triggers stay in/return to an 'Ok' state.

**_[template](/documentation/current/en/manual/config/templates)_**

\- _a set of entities (items, triggers, graphs, low-level discovery rules, web scenarios) ready to be applied to one or several hosts._

The job of templates is to speed up the deployment of monitoring tasks on a host; also to make it easier to apply mass changes to monitoring tasks. Templates are linked directly to individual hosts.

**_[template group](/documentation/current/en/manual/config/templates)_**

\- _a logical grouping of templates. Template groups are used when assigning access rights to templates for different user groups._

**_[event](/documentation/current/en/manual/config/events)_**

\- _a single occurrence of something that deserves attention such as a trigger changing state or a discovery/agent autoregistration taking place._

**_[event tag](/documentation/current/en/manual/config/tagging)_**

\- _a pre-defined marker for the event._ It may be used in event correlation, permission granulation, etc.

**_[event correlation](/documentation/current/en/manual/config/event_correlation)_**

\- _a method of correlating problems to their resolution flexibly and precisely._

For example, you may define that a problem reported by one trigger may be resolved by another trigger, which may even use a different data collection method.

**_[problem](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems)_**

\- _a trigger that is in "Problem" state._

**_[problem update](/documentation/current/en/manual/acknowledgment#updating-problems)_**

\- _problem management options provided by Zabbix, such as adding comment, acknowledging, changing severity or closing manually._

**_[action](/documentation/current/en/manual/config/notifications/action)_**

\- _a predefined means of reacting to an event._

An action consists of operations (e.g. sending a notification) and conditions (_when_ the operation is carried out)

**_[escalation](/documentation/current/en/manual/config/notifications/action/escalations)_**

\- _a custom scenario for executing operations within an action; a sequence of sending notifications/executing remote commands._

**_[media](/documentation/current/en/manual/config/notifications/media)_**

\- _a means of delivering notifications; delivery channel._

**_[notification](/documentation/current/en/manual/config/notifications/action/operation/message)_**

\- _a message about some event sent to a user via the chosen media channel._

**_[remote command](/documentation/current/en/manual/config/notifications/action/operation/remote_command)_**

\- _a pre-defined command that is automatically executed on a monitored host upon some condition._

**_[web scenario](/documentation/current/en/manual/web_monitoring)_**

\- _one or several HTTP requests to check the availability of a web site._

**_[frontend](/documentation/current/en/manual/introduction/overview#architecture)_**

\- _the web interface provided with Zabbix._

**_[dashboard](/documentation/current/en/manual/web_interface/frontend_sections/dashboards)_**

\- _customizable section of the web interface displaying summaries and visualizations_ of important information in visual units called widgets.

**_[widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets)_**

\- _visual unit displaying information of a certain kind and source_ (a summary, a map, a graph, the clock, etc.), used in the dashboard.

**_[Zabbix API](/documentation/current/en/manual/api)_**

\- _Zabbix API allows you to use the JSON RPC protocol to create, update and fetch Zabbix objects (like hosts, items, graphs and others) or perform any other custom tasks._

**_[Zabbix server](/documentation/current/en/manual/concepts/server)_**

\- _a central process of Zabbix software that performs monitoring, interacts with Zabbix proxies and agents, calculates triggers, sends notifications; a central repository of data._

**_[Zabbix proxy](/documentation/current/en/manual/concepts/proxy)_**

\- _a process that may collect data on behalf of Zabbix server, taking some processing load from the server._

**_[Zabbix agent](/documentation/current/en/manual/concepts/agent)_**

\- _a process deployed on monitoring targets to actively monitor local resources and applications._

**_[Zabbix agent 2](/documentation/current/en/manual/concepts/agent2)_**

\- _a new generation of Zabbix agent to actively monitor local resources and applications, allowing to use custom plugins for monitoring._

Because Zabbix agent 2 shares much functionality with Zabbix agent, the term "Zabbix agent" in documentation stands for both - Zabbix agent and Zabbix agent 2, if the functional behavior is the same. Zabbix agent 2 is only specifically named where its functionality differs.

**_[encryption](/documentation/current/en/manual/encryption)_**

\- _support of encrypted communications between Zabbix components (server, proxy, agent, zabbix_sender and zabbix_get utilities)_ using Transport Layer Security (TLS) protocol.

**_[agent autoregistration](/documentation/current/en/manual/discovery/auto_registration)_**

\- _automated process whereby a Zabbix agent itself is registered_ as a host and started to monitor.

**_[network discovery](/documentation/current/en/manual/discovery/network_discovery)_**

\- _automated discovery of network devices_.

**_[low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery)_**

\- _automated discovery of low-level entities on a particular device_ (e.g. file systems, network interfaces, etc).

**_[low-level discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule)_**

\- _set of definitions for automated discovery of low-level entities_ on a device.

**_[item prototype](/documentation/current/en/manual/discovery/low_level_discovery#item-prototypes)_**

\- _a metric with certain parameters as variables, ready for low-level discovery_. After low-level discovery the variables are automatically substituted with the real discovered parameters and the metric automatically starts gathering data.

**_[trigger prototype](/documentation/current/en/manual/discovery/low_level_discovery#trigger-prototypes)_**

\- _a trigger with certain parameters as variables, ready for low-level discovery_. After low-level discovery the variables are automatically substituted with the real discovered parameters and the trigger automatically starts evaluating data.

_Prototypes_ of some other Zabbix entities are also in use in low-level discovery - graph prototypes, host prototypes, host group prototypes.