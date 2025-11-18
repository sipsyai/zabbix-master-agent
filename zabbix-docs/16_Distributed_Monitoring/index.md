---
title: Distributed monitoring
source: https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring
downloaded: 2025-11-14 10:37:41
---

# 16 Distributed monitoring

#### Overview

Zabbix provides an effective and reliable way of monitoring a distributed IT infrastructure using Zabbix [proxies](/documentation/current/en/manual/distributed_monitoring/proxies).

Proxies can be used to collect data locally on behalf of a centralized Zabbix server and then report the data to the server.

##### Proxy features

When making a choice of using/not using a proxy, several considerations must be taken into account.

_Lightweight_ | **Yes**  
---|---  
_GUI_ | No  
_Works independently_ | **Yes**  
_Easy maintenance_ | **Yes**  
_Automatic DB creation_ | **Yes** 1  
_Local administration_ | No  
_Ready for embedded hardware_ | **Yes**  
_One way TCP connections_ | **Yes**  
_Centralized configuration_ | **Yes**  
_Generates notifications_ | No  
  
1 Automatic DB creation feature works only with SQLite. Other supported databases require [manual setup](/documentation/current/en/manual/appendix/install/db_scripts).

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.