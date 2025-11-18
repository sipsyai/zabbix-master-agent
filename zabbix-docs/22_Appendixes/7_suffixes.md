---
title: Unit symbols
source: https://www.zabbix.com/documentation/current/en/manual/appendix/suffixes
downloaded: 2025-11-14 10:47:52
---

# 7 Unit symbols

#### Overview

Working with large values such as 86400, 104857600, or 1000000 can be challenging and can lead to errors. To simplify configuration and improve readability, Zabbix supports unit symbols (suffixes) that function as value multipliers.

Trigger expressions without suffixes:
    
    
    last(/host/system.uptime)<86400
           avg(/host/system.cpu.load,600s)<10
           last(/host/vm.memory.size[available])<20971520

Copy

✔ Copied

Trigger expressions with suffixes:
    
    
    last(/host/system.uptime)<1d
           avg(/host/system.cpu.load,10m)<10
           last(/host/vm.memory.size[available])<20M

Copy

✔ Copied

Suffixes can also simplify the configuration of other entities, such as items, widgets, etc., and help display item values in a human-readable format.

To see if an entity configuration field supports suffixes, always see the relevant page for the entity being configured.

#### Time suffixes

Zabbix frontend supports the following time suffixes in entity configuration:

  * **s** \- seconds _(when used, works the same as the raw value)_
  * **m** \- minutes
  * **h** \- hours
  * **d** \- days
  * **w** \- weeks
  * **M** \- months _([trend functions](/documentation/current/en/manual/appendix/functions/trends) only)_
  * **y** \- years _([trend functions](/documentation/current/en/manual/appendix/functions/trends) only)_

Time suffixes are supported only with integer numbers. For example, 1h is supported, but 1,5h or 1.5h is not supported; use 90m instead.

#### Memory size suffixes

Zabbix supports the following memory size suffixes:

  * **K** \- kilobytes
  * **M** \- megabytes
  * **G** \- gigabytes
  * **T** \- terabytes

#### Item value suffixes

Suffixes can also be used to display numeric item values in a human-readable format.

To enable this, use one of the following suffixes in the _Units_ field when [configuring an item](/documentation/current/en/manual/config/items/item#configuration):

  * **B** \- bytes
  * **Bps** \- bytes per second
  * **s** \- seconds, displayed using up to three largest non-zero time units
  * **uptime** \- elapsed time in hh:mm:ss or N days, hh:mm:ss
  * **unixtime** \- Unix timestamp, formatted as yyyy.mm.dd hh:mm:ss

The following additional rules apply to how these suffixes are interpreted and displayed:

  * For B and Bps, Zabbix uses base-2 conversion (1K = 1024B), following the [JEDEC](https://en.wikipedia.org/wiki/JEDEC_memory_standards) standard.
  * For other units (such as Hz, W, etc.), Zabbix uses base-10 conversion (1K = 1000).
  * For s (seconds): 
    * The format includes yyy mmm ddd hhh mmm sss ms; only up to three largest non-zero time units are displayed (e.g., 1M 10d 4h).
    * If a unit is zero and between two non-zero units, it is omitted (e.g., 10d 56m instead of 10d 0h 56m).

When _Units_ are used, the following multiplier suffixes are automatically applied to item values:

  * **K** , **M** , **G** , **T** \- kilo, mega, giga, tera
  * **P** , **E** , **Z** , **Y** \- peta, exa, zetta, yotta _(these are applied in frontend only)_

To prevent unit conversion, use the `!` prefix (e.g., !B or !s).

The following examples show how received item values are converted based on the specified units:
    
    
    1 B → 1 B
           1024 B → 1 KB
           1536 B → 1.5 KB
           881764 B → 881.76 KB
           881764 !B → 881764 B
           
           0.0000155 s → 0.016ms
           3470400 s → 1M 10d 4h
           2606400 s → 1M 4h
           2592000 s → 1M
           2592001 s → 1M
           2592001 !s → 2592001 s
           
           17764 uptime → 04:56:04
           86400 uptime → 1 day, 00:00:00
           881764 uptime → 10 days, 04:56:04
           32417764 uptime → 375 days, 04:56:04
           32417764 !uptime → 32417764 uptime
           
           881764 unixtime → 1970-01-11 04:56:04 AM
           
           17764 Hz → 17.76 KHz
           86400 Hz → 86.4 KHz
           881764 Hz → 881.76 KHz
           32417764 Hz → 32.42 MHz
           
           0 ! → 0
           0 !! → 0 !

Copy

✔ Copied

Before Zabbix 4.0, there was a hardcoded unit stoplist consisting of `ms`, `rpm`, `RPM`, `%`. This stoplist has been deprecated, thus the correct way to prevent converting such units is `!ms`, `!rpm`, `!RPM`, `!%`.