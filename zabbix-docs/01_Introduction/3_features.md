---
title: Zabbix features
source: https://www.zabbix.com/documentation/current/en/manual/introduction/features
downloaded: 2025-11-14 10:33:42
---

# 3 Zabbix features

#### Overview

Zabbix is a highly integrated network monitoring solution, offering a multiplicity of features in a single package.

**[Data gathering](/documentation/current/en/manual/config/items)**

  * availability and performance checks
  * support for SNMP (both trapping and polling), IPMI, JMX, VMware monitoring
  * custom checks
  * gathering desired data at custom intervals
  * performed by server/proxy and by agents

**[Flexible threshold definitions](/documentation/current/en/manual/config/triggers)**

  * you can define very flexible problem thresholds, called triggers, referencing values from the backend database

**[Highly configurable alerting](/documentation/current/en/manual/config/notifications)**

  * sending notifications can be customized for the escalation schedule, recipient, media type
  * notifications can be made meaningful and helpful using macro variables
  * automatic actions include remote commands

**[Real-time graphing](/documentation/current/en/manual/config/visualization/graphs/simple)**

  * monitored items are immediately graphed using the built-in graphing functionality

**[Web monitoring capabilities](/documentation/current/en/manual/web_monitoring)**

  * Zabbix can follow a path of simulated mouse clicks on a web site and check for functionality and response time

**[Extensive visualization options](/documentation/current/en/manual/config/visualization)**

  * ability to create custom graphs that can combine multiple items into a single view
  * network maps
  * slideshows in a dashboard-style overview
  * reports
  * high-level (business) view of monitored resources

**[Historical data storage](/documentation/current/en/manual/installation/requirements#database-size)**

  * data stored in a database
  * configurable history
  * built-in housekeeping procedure

**[Easy configuration](/documentation/current/en/manual/config/hosts)**

  * add monitored devices as hosts
  * hosts are picked up for monitoring, once in the database
  * apply templates to monitored devices

**[Use of templates](/documentation/current/en/manual/config/templates)**

  * grouping checks in templates
  * templates can inherit other templates

**[Network discovery](/documentation/current/en/manual/discovery)**

  * automatic discovery of network devices
  * agent autoregistration
  * discovery of file systems, network interfaces and SNMP OIDs

**[Fast web interface](/documentation/current/en/manual/web_interface)**

  * a web-based frontend in PHP
  * accessible from anywhere
  * you can click your way through
  * audit log

**[Zabbix API](/documentation/current/en/manual/api)**

  * Zabbix API provides programmable interface to Zabbix for mass manipulations, third-party software integration and other purposes.

**[Permissions system](/documentation/current/en/manual/config/users_and_usergroups)**

  * secure user authentication
  * certain users can be limited to certain views

**[Full featured and easily extensible agent](/documentation/current/en/manual/concepts/agent)**

  * deployed on monitoring targets
  * can be deployed on both Linux and Windows

**[Binary daemons](/documentation/current/en/manual/concepts/server)**

  * written in C, for performance and small memory footprint
  * easily portable

**[Ready for complex environments](/documentation/current/en/manual/distributed_monitoring)**

  * remote monitoring made easy by using a Zabbix proxy