---
title: Service monitoring
source: https://www.zabbix.com/documentation/current/en/manual/it_services
downloaded: 2025-11-14 10:36:47
---

# 8 Service monitoring

#### Overview

Service monitoring is a business-level monitoring that can be used to get an overview of the entire IT infrastructure service tree, identify weak places of the infrastructure, calculate SLA of various IT services, and check out other information at a higher level. Service monitoring focuses on the overall availability of a service instead of low-level details, such as the lack of disk space, high processor load, etc. Service monitoring also provides functionality to find the root cause of a problem if a service is not performing as expected.

Service monitoring allows to create a hierarchy representation of monitored data.

A very simple service structure may look like:
    
    
    Service
           |
           |-Workstations
           | |
           | |-Workstation1
           | |
           | |-Workstation2
           |
           |-Servers

Copy

✔ Copied

Each node of the structure has attribute status. The status is calculated and propagated to upper levels according to the selected algorithm. The status of individual nodes is affected by the status of the mapped problems. Problem mapping is accomplished with [tagging](/documentation/current/en/manual/it_services/service_tree#problem-tags).

Zabbix can send notifications or automatically execute a script on the Zabbix server in case service status change is detected. It is possible to define flexible rules whether a parent service should go into a 'Problem state' based on the statuses of child services. Services problem data can then be used to calculate SLA and send SLA reports based on the flexible set of conditions.

Service monitoring is configured in the Services menu, which consists of the following sections:

  * [Services](/documentation/current/en/manual/it_services/service_tree)

Services section allows to build a hierarchy of your monitored infrastructure by adding parent services, and then - child services to the parent services.

In addition to configuring service tree, this section provides an overview of the whole infrastructure and allows to quickly identify the problems that led to a service status change.

  * [SLA](/documentation/current/en/manual/it_services/sla)

In this section you can define service level agreements and set service level objectives for specific services.

  * [SLA report](/documentation/current/en/manual/it_services/sla#sla-reports)

In this section you can view SLA reports.

**Service actions**

You may also configure service [actions](/documentation/current/en/manual/config/notifications/action).

Service actions are optional and allow to:

  * send a notification that a service is down
  * execute a remote command on a Zabbix server upon a service status change
  * send a recovery notification when a service is up again.

**See also:**

  * SLA monitoring configuration [example](/documentation/current/en/manual/it_services/example)
  * Notes about [upgrading services](/documentation/current/en/manual/appendix/services_upgrade) from Zabbix versions below 6.0