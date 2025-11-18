---
title: Setup example
source: https://www.zabbix.com/documentation/current/en/manual/it_services/example
downloaded: 2025-11-14 10:36:50
---

# 3 Setup example

### Overview

This section describes a simple setup for monitoring Zabbix high availability cluster as a service.

### Pre-requisites

Prior to configuring service monitoring, you need to have the hosts configured:

  * _HA node 1_ with at least one trigger and a tag (preferably set on a trigger level) `component:ha-node-1`
  * _HA node 2_ with at least one trigger and a tag (preferably set on a trigger level) `component:ha-node-2`

### Service tree

The next step is to build the service tree. In this example, the infrastructure is very basic and consists of three services: _Zabbix cluster_ (parent) and two child services _Zabbix server node 1_ and _Zabbix server node 2_.
    
    
    Zabbix cluster
           |
           |- Zabbix server node 1
           |- Zabbix server node 2

Copy

✔ Copied

At the Services page, turn on _Edit_ mode and press Create service:

![](/documentation/current/assets/en/manual/config/service_mode.png)

In the service configuration window, enter name _Zabbix cluster_ and click on the _Advanced configuration_ label to display advanced configuration options.

![](/documentation/current/assets/en/manual/config/service_cluster.png)

Configure additional rule:

![](/documentation/current/assets/en/manual/config/service_add_rule.png)

Zabbix cluster will have two child services - one for each of the HA nodes. If both HA nodes have problems of at least _Warning_ status, parent service status should be set to _Disaster_. To achieve this, additional rule should be configured as:

  * Set status to: Disaster
  * Condition: If at least `N` child services have `Status` status or above
  * N: 2
  * Status: Warning

Switch to the _Tags_ tab and add a tag `application:zabbix-server`. This tag will be used later for service actions and SLA reports.

![](/documentation/current/assets/en/manual/config/service_cluster1.png)

Save the new service.

To add a child service, press on the plus icon next to the Zabbix cluster service (the icon is visible only in _Edit_ mode).

![](/documentation/current/assets/en/manual/config/service_cluster2.png)

In the service configuration window, enter name _Zabbix server node 1_. Note that the Parent services parameter is already pre-filled with _Zabbix cluster_.

Availability of this service is affected by problems on the host _HA node 1_ , marked with `component:ha-node-1` problem tag. In the Problem tags parameter, enter:

  * Name: component
  * Operation: Equals
  * Value: ha-node-1

![](/documentation/current/assets/en/manual/config/service_cluster3.png)

Switch to the _Tags_ tab and add a service tag: `zabbix-server:node-1`. This tag will be used later for service actions and SLA reports.

![](/documentation/current/assets/en/manual/config/service_cluster4.png)

Save the new service.

Create another child service of Zabbix cluster with name "Zabbix server node 2".

Set the Problem tags as:

  * Name: component
  * Operation: Equals
  * Value: ha-node-2

Switch to the _Tags_ tab and add a service tag: `zabbix-server:node-2`.

Save the new service.

### SLA

In this example, expected Zabbix cluster performance is 100% excluding semi-annual one hour maintenance period.

First, you need to add a new service level agreement.

Go to the _Services- >SLA_ menu section and press Create SLA. Enter name _Zabbix cluster performance_ and set the SLO to 100%.

The service Zabbix cluster has a service tag `application:zabbix-server`. To use this SLA for measuring performance of Zabbix cluster, in the _Service tags_ parameter, specify:

  * Name: application
  * Operation: Equals
  * Value: zabbix-server

![](/documentation/current/assets/en/manual/config/service_sla.png)

In a real-life setup, you can also update desired reporting period, time zone and start date or change the schedule from 24/7 to custom. For this example, the default settings are sufficient.

Switch to the _Excluded downtimes_ tab and add downtimes for scheduled maintenance periods to exclude these periods from SLA calculation. In the Excluded downtimes section press the Add link, enter downtime name, planned start time and duration.

![](/documentation/current/assets/en/manual/config/service_sla1.png)

Press Add to save the new SLA.

Switch to the SLA reports section to view the SLA report for Zabbix cluster.

![](/documentation/current/assets/en/manual/config/service_sla2.png)

The SLA info can also be checked in the _Services_ section.

![](/documentation/current/assets/en/manual/config/service_sla3.png)