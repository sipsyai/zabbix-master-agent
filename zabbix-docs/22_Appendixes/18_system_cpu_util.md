---
title: Notes on system.cpu.util items on Windows
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/system_cpu_util
downloaded: 2025-11-14 10:47:36
---

# 18 Notes on system.cpu.util items on Windows

[system.cpu.util](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.cpu.util) item provides the CPU utilization percentage.

When a collector process is started on Zabbix agent for Windows, a buffer for N items for N logical processors (threads) is initialized. Values are periodically updated in the buffer using Windows performance counters. These values are reported when `system.cpu.util[n]` is requested, where 0 <= n < N.

One more item in the buffer is used for `system.cpu.util[total]`.

Zabbix automatically selects different performance counters to support both NUMA systems and older Windows versions with no processor group support.

If logical processor (thread) count is less or equal than 64 and number of processor groups is equal to 1, then:
    
    
    N is logical processor (thread) count.
           
           \Processor(_Total)\% Processor Time
           \Processor(0)\% Processor Time
           \Processor(1)\% Processor Time
           \Processor(2)\% Processor Time
           ...
           \Processor(N-1)\% Processor Time

Copy

✔ Copied

Else:
    
    
    G is processor group count and N is logical processor (thread) count in group.
           
           \Processor Information(_Total)\% Processor Time
           \Processor Information(0,0)\% Processor Time
           \Processor Information(0,1)\% Processor Time
           \Processor Information(0,2)\% Processor Time
           ...
           \Processor Information(0,N-1)\% Processor Time
           ...
           \Processor Information(G-1,0)\% Processor Time
           \Processor Information(G-1,1)\% Processor Time
           \Processor Information(G-1,2)\% Processor Time
           ...
           \Processor Information(G-1,N-1)\% Processor Time

Copy

✔ Copied