---
title: Service monitoring upgrade
source: https://www.zabbix.com/documentation/current/en/manual/appendix/services_upgrade
downloaded: 2025-11-14 10:47:58
---

# 14 Service monitoring upgrade

### Overview

In Zabbix 6.0, [service monitoring](/documentation/current/en/manual/it_services) functionality has been reworked significantly (see [What's new in Zabbix 6.0.0](https://www.zabbix.com/documentation/6.0/en/manual/introduction/whatsnew600#services) for the list of changes).

This page describes how services and SLAs, defined in earlier Zabbix versions, are changed during an upgrade to Zabbix 6.0 or newer.

### Services

In older Zabbix versions, services had two types of dependencies: soft and hard. After an upgrade, all dependencies will become equal.

If a service "Child service" has been previously linked to "Parent service 1" via hard dependency and additionally "Parent service 2" via soft dependency, after an upgrade the "Child service" will have two parent services "Parent service 1" and "Parent service 2".

Trigger-based mapping between problems and services has been replaced by tag-based mapping. In Zabbix 6.0 and newer, service configuration form has a new parameter _Problem tags_ , which allows specifying one or multiple tag name and value pairs for problem matching. Triggers that have been linked to a service will get a new tag `ServiceLink` : `<trigger ID>:<trigger name>` (tag value will be truncated to 32 characters). Linked services will get `ServiceLink` [problem tag](/documentation/current/en/manual/it_services/service_tree#problem-tags) with the same value.

#### Status calculation rules

The 'Status calculation algorithm' will be upgraded using the following rules:

  * Do not calculate → Set status to OK
  * Problem, if at least one child has a problem → Most critical of child services
  * Problem, if all children have problems → Most critical if all children have problems

### SLAs

Previously, SLA targets had to be defined for each service separately. Since Zabbix 6.0, SLA has become a separate entity, which contains information about service schedule, expected service level objective (SLO) and downtime periods to exclude from the calculation. Once configured, an SLA can be assigned to multiple services through [service tags](/documentation/current/en/manual/it_services/service_tree#tags).

During an upgrade:

  * Identical SLAs defined for each service will be grouped and one SLA per each group will be created.
  * Each affected service will get a special tag `SLA`:`<ID>` and the same tag will be specified in the _Service tags_ parameter of the corresponding SLA.
  * Service creation time, a new metric in SLA reports, will be set to 01/01/2000 00:00 for existing services.