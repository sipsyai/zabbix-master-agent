---
title: Discovery of CPUs and CPU cores
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/cpu
downloaded: 2025-11-14 10:37:28
---

# 3 Discovery of CPUs and CPU cores

In a similar way as [file systems](/documentation/current/en/manual/discovery/low_level_discovery#configuring-low-level-discovery) are discovered, it is possible to also discover CPUs and CPU cores.

#### Item key

The item key to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is
    
    
    system.cpu.discovery

Copy

✔ Copied

#### Supported macros

This discovery key returns two macros - {#CPU.NUMBER} and {#CPU.STATUS} identifying the CPU order number and status respectively. It enumerates processors from 0 to N - 1, where N is total processor count.
    
    
    [
               {
                   "{#CPU.NUMBER}": 0,
                   "{#CPU.STATUS}": "online"
               },
               {
                   "{#CPU.NUMBER}": 1,
                   "{#CPU.STATUS}": "offline"
               },
               {
                   "{#CPU.NUMBER}": 2,
                   "{#CPU.STATUS}": "unknown" /* "unknown" is only on Windows */
               },
               {
                   "{#CPU.NUMBER}": 3,
                   "{#CPU.STATUS}": "online"
               }
           ]

Copy

✔ Copied

Note that a clear distinction cannot be made between actual, physical processors, cores and hyperthreads. {#CPU.STATUS} on Linux, UNIX and BSD systems returns the status of the processor, which can be either "online" or "offline". On Windows systems, this same macro may represent a third value - "unknown" - which indicates that a processor has been detected, but no information has been collected for it yet.

CPU discovery relies on the agent's collector process to remain consistent with the data provided by the collector and save resources on obtaining the data. This has the effect of this item key not working with the test (-t) command line flag of the agent binary, which will return a NOT_SUPPORTED status and an accompanying message indicating that the collector process has not been started.

Item prototypes that can be created based on CPU discovery include, for example:

  * `system.cpu.util[{#CPU.NUMBER},<type>,<mode>]`
  * `system.hw.cpu[{#CPU.NUMBER},<info>]`

For detailed item key description, see [Zabbix agent item keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#supported-item-keys).

#### Notes on discovered performance counter items on NUMA systems

Some [Windows performance counters](/documentation/current/en/manual/config/items/perfcounters) might be not available for some of the logical processors at NUMA systems.

For example, items discovered with an item prototype with the key below might work only for the first NUMA node. Items for the other NUMA nodes might be in unsupported state.
    
    
    perf_counter[\Processor({#CPU.NUMBER})\% Processor Time,60]

Also, a discovery rule with key "system.cpu.discovery" does not provide any low-level discovery macro values to substitute into such performance counters as:
    
    
    perf_counter["\Processor Information(<NUMA node index>,<CPU index in NUMA node>)\% Processor Time",60]

While [system.cpu.util](/documentation/current/en/manual/appendix/items/system_cpu_util) items rely on different performance counters to monitor CPU utilization percentage depending on the processor group count and processor count. Also, there is a rare bug related to [processor groups on Windows](/documentation/current/en/manual/installation/known_issues#win-proc-groups).