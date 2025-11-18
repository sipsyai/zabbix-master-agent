---
title: Discovery of Windows performance counter instances
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_perf_instances
downloaded: 2025-11-14 10:37:34
---

# 10 Discovery of Windows performance counter instances

#### Overview

It is possible to discover object instances of Windows performance counters. This is useful for multi-instance performance counters.

#### Item key

To configure the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule), use the following item:

  * `perf_instance.discovery[object]`

Note that the object name may be localized. For example:
    
    
    perf_instance.discovery[Processor] # The object name is in English.
           perf_instance.discovery[Processador] # The object name is in Portuguese.

Copy

✔ Copied

Alternatively, to ensure that the object name is provided in English, independent of OS localization, use the following item:

  * `perf_instance_en.discovery[object]`

For example:
    
    
    perf_instance_en.discovery[Processor]
           perf_instance_en.discovery[Memory]

Copy

✔ Copied

#### Supported macros

The discovery process will return all instances of the specified object in the `{#INSTANCE}` macro:
    
    
    [
               {"{#INSTANCE}":"0"},
               {"{#INSTANCE}":"1"},
               {"{#INSTANCE}":"_Total"}
           ]

Copy

✔ Copied

This macro may be used in the prototypes of `perf_counter[]` and `perf_counter_en[]` items.

For example, if the item key used in the discovery rule is `perf_instance.discovery[Processor]`, you may create the following item prototype:
    
    
    perf_counter["\Processor({#INSTANCE})\% Processor Time"]

Copy

✔ Copied

Note:

  * If the specified object is not found or does not support variable instances, the discovery item will become NOTSUPPORTED.
  * If the specified object supports variable instances but currently does not have any instances, an empty JSON array will be returned.
  * Duplicate instances will be skipped.