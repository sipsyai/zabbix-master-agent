---
title: Item types
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes
downloaded: 2025-11-14 10:34:54
---

# 3 Item types

#### Overview

Item types cover various methods of acquiring data from your system. Each item type comes with its own set of supported item keys and required parameters.

The following items types are currently offered by Zabbix:

  * [Zabbix agent checks](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent)
  * [SNMP agent checks](/documentation/current/en/manual/config/items/itemtypes/snmp)
  * [SNMP traps](/documentation/current/en/manual/config/items/itemtypes/snmptrap)
  * [IPMI checks](/documentation/current/en/manual/config/items/itemtypes/ipmi)
  * [Simple checks](/documentation/current/en/manual/config/items/itemtypes/simple_checks)
    * [VMware monitoring](/documentation/current/en/manual/vm_monitoring/vmware_keys)
  * [Log file monitoring](/documentation/current/en/manual/config/items/itemtypes/log_items)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
    * [Aggregate calculations](/documentation/current/en/manual/config/items/itemtypes/calculated/aggregate)
  * [Zabbix internal checks](/documentation/current/en/manual/config/items/itemtypes/internal)
  * [SSH checks](/documentation/current/en/manual/config/items/itemtypes/ssh_checks)
  * [Telnet checks](/documentation/current/en/manual/config/items/itemtypes/telnet_checks)
  * [External checks](/documentation/current/en/manual/config/items/itemtypes/external)
  * [Trapper items](/documentation/current/en/manual/config/items/itemtypes/trapper)
  * [JMX monitoring](/documentation/current/en/manual/config/items/itemtypes/jmx_monitoring)
  * [ODBC checks](/documentation/current/en/manual/config/items/itemtypes/odbc_checks)
  * [Dependent items](/documentation/current/en/manual/config/items/itemtypes/dependent_items)
  * [HTTP checks](/documentation/current/en/manual/config/items/itemtypes/http)
  * [Prometheus checks](/documentation/current/en/manual/config/items/itemtypes/prometheus)
  * [Script items](/documentation/current/en/manual/config/items/itemtypes/script)
  * [Browser items](/documentation/current/en/manual/config/items/itemtypes/browser)

Details for all item types are included in the subpages of this section. Even though item types offer a lot of options for data gathering, there are further options through [user parameters](/documentation/current/en/manual/config/items/userparameters) or [loadable modules](/documentation/current/en/manual/extensions/loadablemodules).

Some checks are performed by Zabbix server alone (as agent-less monitoring) while others require Zabbix agent or even Zabbix Java gateway (with JMX monitoring).

If a particular item type requires a particular [interface](/documentation/current/en/manual/config/hosts/host#configuration) (like an IPMI check needs an IPMI interface on the host) that interface must exist in the host definition.

Multiple interfaces can be set in the host definition: Zabbix agent, SNMP agent, JMX and IPMI. If an item can use more than one interface, it will search the available host interfaces (in the order: Agent→SNMP→JMX→IPMI) for the first appropriate one to be linked with.

All [items](/documentation/current/en/manual/config/items/item#configuration) that return text (character, log, text types of information) can return whitespace only as well (where applicable) setting the return value to an empty string (supported since 2.0).