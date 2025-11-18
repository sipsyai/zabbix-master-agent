---
title: Items
source: https://www.zabbix.com/documentation/current/en/manual/config/items
downloaded: 2025-11-14 10:34:40
---

# 2 Items

#### Overview

An item is an individual metric.

Items are used for collecting data. Once you have configured a host, you must add items to get actual data. One way of quickly adding many items is to attach one of the predefined templates to a host. However, for optimized system performance, you may need to fine-tune the templates to have as many items and as frequent monitoring as necessary.

To specify what sort of data to collect from a host, use the [item key](/documentation/current/en/manual/config/items/item/key). For example, an item with the key name **system.cpu.load** will collect processor load data, while an item with the key name **net.if.in** will collect incoming traffic information.

Additional parameters can be specified in square brackets after the key name. For example, system.cpu.load**[avg5]** will return the processor load average for the last 5 minutes, while net.if.in**[eth0]** will show incoming traffic in the interface "eth0".

See individual sections of [item types](/documentation/current/en/manual/config/items/itemtypes) for all supported item types and item keys.

Proceed to [creating and configuring an item](/documentation/current/en/manual/config/items/item).