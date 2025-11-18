---
title: Unreachable/unavailable host interface settings
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/unreachability
downloaded: 2025-11-14 10:47:29
---

# 11 Unreachable/unavailable host interface settings  
  
#### Overview

Several configuration [parameters](/documentation/current/en/manual/appendix/config/zabbix_server) define how Zabbix server should behave when an agent check (Zabbix, SNMP, IPMI, JMX) fails and a host interface becomes unreachable.

#### Unreachable interface

A host interface is treated as unreachable after a failed check (network error, timeout) by Zabbix, SNMP, IPMI or JMX agents. Since Zabbix 6.2.0, active Zabbix agent checks also affect interface availability. When active checks become unavailable, they contribute to the overall availability status of the agent interface.

From the moment an interface becomes unreachable, [**UnreachableDelay**](/documentation/current/en/manual/appendix/config/zabbix_server#unreachabledelay) defines how often it is rechecked using one of the items (including LLD rules). These rechecks are performed by unreachable pollers (or IPMI pollers for IPMI checks). By default, the interval between consecutive reachability checks is 15 seconds.

Checks performed by asynchronous pollers are not moved to unreachable pollers.

In the Zabbix server log unreachability is indicated by messages like:
    
    
    Zabbix agent item "system.cpu.load[percpu,avg1]" on host "New host" failed: first network error, wait for 15 seconds
           Zabbix agent item "system.cpu.load[percpu,avg15]" on host "New host" failed: another network error, wait for 15 seconds

Copy

✔ Copied

The log messages specify the exact item that failed and its type (Zabbix agent).

The _Timeout_ parameter will also affect how early an interface is rechecked during unreachability. If Timeout is set to 20 seconds and UnreachableDelay to 30 seconds, the next check will be in 50 seconds after the first attempt.

The **UnreachablePeriod** parameter defines the total duration of the unreachability period. By default UnreachablePeriod is 45 seconds. This value should be several times larger than UnreachableDelay to ensure that an interface is rechecked multiple times before being marked as unavailable.

An internal item, [zabbix[host,active_agent,available]](/documentation/current/en/manual/config/items/itemtypes/internal#active.available), allows monitoring the availability of active checks in unreachable scenarios.

##### Switching interface back to available

When the unreachability period is over, the interface is polled again, decreasing priority for item that turned the interface into unreachable state. If the unreachable interface reappears, the monitoring returns to normal automatically:
    
    
    resuming Zabbix agent checks on host "New host": connection restored

Copy

✔ Copied

Once interface becomes available, the host does not poll all its items immediately for two reasons:

  * It might overload the host.
  * The interface restore time is not always matching planned item polling schedule time.

So, after the interface becomes available, items are not polled immediately, but they are getting rescheduled to their next polling round.

#### Unavailable interface

After the UnreachablePeriod ends and the interface has not reappeared, the interface is treated as unavailable.

In the server log it is indicated by messages like these:
    
    
    temporarily disabling Zabbix agent checks on host "New host": interface unavailable

Copy

✔ Copied

and in the [frontend](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts) the host availability icon goes from green/gray to yellow/red (the unavailable interface details can be seen in the hint box that is displayed when a mouse is positioned on the host availability icon):

![](/documentation/current/assets/en/manual/config/unavailable.png)

The **UnavailableDelay** parameter defines how often an interface is checked during interface unavailability.

By default it is 60 seconds (so in this case "temporarily disabling", from the log message above, will mean disabling checks for one minute).

When the connection to the interface is restored, the monitoring returns to normal automatically, too:
    
    
    enabling Zabbix agent checks on host "New host": interface became available

Copy

✔ Copied