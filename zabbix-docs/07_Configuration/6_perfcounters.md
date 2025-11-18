---
title: Windows performance counters
source: https://www.zabbix.com/documentation/current/en/manual/config/items/perfcounters
downloaded: 2025-11-14 10:35:24
---

# 6 Windows performance counters

#### Overview

You can effectively monitor Windows performance counters using the _perf_counter[]_ key.

For example:
    
    
    perf_counter["\Processor(0)\Interrupts/sec"]

Copy

✔ Copied

or
    
    
    perf_counter["\Processor(0)\Interrupts/sec", 10]

Copy

✔ Copied

For more information on using this key or its English-only equivalent `perf_counter_en`, see [Windows-specific item keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys).

In order to get a full list of performance counters available for monitoring, you may run:
    
    
    typeperf -qx

Copy

✔ Copied

You may also use low-level discovery to discover multiple [object instances](/documentation/current/en/manual/discovery/low_level_discovery/examples/windows_perf_instances) of Windows performance counters and automate the creation of perf_counter items for multiple instance objects.

#### Numeric representation

Windows maintains numeric representations (indexes) for object and performance counter names. Zabbix supports these numeric representations as parameters to the `perf_counter`, `perf_counter_en` item keys and in `PerfCounter`, `PerfCounterEn` configuration parameters.

However, it's not recommended to use them unless you can guarantee your numeric indexes map to correct strings on specific hosts. If you need to create portable items that work across different hosts with various localized Windows versions, you can use the `perf_counter_en` key or `PerfCounterEn` configuration parameter which allow to use English names regardless of system locale.

To find out the numeric equivalents, run **regedit** , then locate the _Counter_ in _HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\009_.

The registry entry contains information like this:
    
    
    1
           1847
           2
           System
           4
           Memory
           6
           % Processor Time
           10
           File Read Operations/sec
           12
           File Write Operations/sec
           14
           File Control Operations/sec
           16
           File Read Bytes/sec
           18
           File Write Bytes/sec
           ....

Copy

✔ Copied

Here you can find the corresponding numbers for each string part of the performance counter, like in '\System\% Processor Time':
    
    
    System → 2
           % Processor Time → 6

Copy

✔ Copied

Then you can use these numbers to represent the path in numbers:
    
    
    \2\6

Copy

✔ Copied

#### Performance counter parameters

You can deploy some PerfCounter parameters for the monitoring of Windows performance counters.

For example, you can add these to the Zabbix agent configuration file:
    
    
       PerfCounter=UserPerfCounter1,"\Memory\Page Reads/sec",30
              or
              PerfCounter=UserPerfCounter2,"\4\24",30

Copy

✔ Copied

With such parameters in place, you can then simply use _UserPerfCounter1_ or _UserPerfCounter2_ as the keys for creating the respective items.

Remember to restart Zabbix agent after making changes to the configuration file.