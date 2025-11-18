---
title: Execute now
source: https://www.zabbix.com/documentation/current/en/manual/config/items/check_now
downloaded: 2025-11-14 10:35:29
---

# 11 Execute now

#### Overview

The _Execute now_ option allows executing passive checks immediately.

Item value collection in Zabbix follows configured update intervals. Some items (e.g., low-level discovery rules) have long intervals, and you may need to fetch a new value immediately—for example, to detect changes in discoverable resources.

The _Execute now_ option is supported for the following item types:

  * Zabbix agent (passive)
  * Simple check
  * SNMP agent (v1/v2/v3)
  * Zabbix internal
  * External check
  * Database monitor
  * HTTP agent
  * IPMI agent
  * SSH agent
  * TELNET agent
  * JMX agent
  * Calculated
  * Dependent item
  * Script
  * Browser

If the item is of type "Dependent item", then its master item must also be one of the above types.

#### Configuration

You can execute passive checks from:

  * _Monitoring_ > [_Latest data_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data)
  * _Data collection_ > _Hosts_ > [_Items_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/items) or [_Discovery_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery)
  * The [item menu](/documentation/current/en/manual/web_interface/menu/item_menu)
  * When editing items or low-level discovery rules (in their configuration forms)

The check must exist in the configuration cache in order to get executed; see also [CacheUpdateFrequency](/documentation/current/en/manual/appendix/config/zabbix_server#cacheupdatefrequency). The cache is **not updated** before check execution, so recent changes to item or low-level discovery rule configuration will not be picked up. To test items or LLD rules that are being created or newly created, you can use the [Test](/documentation/current/en/manual/config/items/item#testing) option instead.

For example, to execute a passive check in _Monitoring_ > [_Latest data_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data):

  1. Select items; you can execute the check for multiple items at once.
  2. Click _Execute now_.

![](/documentation/current/assets/en/manual/config/items/execute_now_latest_data.png)

In _Latest data_ , users may _Execute now_ items on hosts for which they have _read-write_ [permission](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration), or _read_ permission and _Invoke "Execute now" on read-only hosts_ [action](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles#default-permissions) enabled for their role.