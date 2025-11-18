---
title: vm.memory.size parameters
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/vm.memory.size_params
downloaded: 2025-11-14 10:47:19
---

# 1 vm.memory.size parameters

#### Overview

This section provides some parameter details for the [vm.memory.size[<mode>]](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#vm.memory.size) agent item.

#### Parameters

The following parameters are available for this item:

  * **active** \- memory currently in use or very recently used, and so it is in RAM
  * **anon** \- memory not associated with a file (cannot be re-read from it)
  * **available** \- available memory, calculated differently depending on the platform (see the table below)
  * **buffers** \- cache for things like file system metadata
  * **cached** \- cache for various things
  * **exec** \- executable code, typically from a (program) file
  * **file** \- cache for contents of recently accessed files
  * **free** \- memory that is readily available to any entity requesting memory
  * **inactive** \- memory that is marked as not used
  * **pavailable** \- 'available' memory as percentage of 'total' (calculated as `available`/`total`*100)
  * **pinned** \- same as 'wired'
  * **pused** \- 'used' memory as percentage of 'total' (calculated as `used`/`total`*100)
  * **shared** \- memory that may be simultaneously accessed by multiple processes
  * **slab** \- total amount of memory used by the kernel to cache data structures for its own use
  * **total** \- total physical memory available
  * **used** \- used memory, calculated differently depending on the platform (see the table below)
  * **wired** \- memory that is marked to always stay in RAM. It is never moved to disk.

Some of these parameters are platform-specific and might not be available on your platform. See [Zabbix agent items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) for details.

Platform-specific calculation of **available** and **used** :

_AIX_ | free + cached | real memory in use  
---|---|---  
_FreeBSD_ | inactive + cached + free | active + wired + cached  
_HP UX_ | free | total - free  
_Linux <3.14_ | free + buffers + cached | total - free  
_Linux 3.14+_  
(also backported to 3.10 on RHEL 7) | /proc/meminfo, see "MemAvailable" in Linux kernel [documentation](https://www.kernel.org/doc/Documentation/filesystems/proc.txt) for details.  
Note that free + buffers + cached is no longer equal to 'available' due to not all the page cache can be freed and low watermark being used in calculation. | total - free  
_NetBSD_ | inactive + execpages + file + free | total - free  
_OpenBSD_ | inactive + free + cached | active + wired  
_OSX_ | inactive + free | active + wired  
_Solaris_ | free | total - free  
_Win32_ | free | total - free  
  
The sum of _vm.memory.size[used]_ and _vm.memory.size[available]_ does not necessarily equal total. For instance, on FreeBSD:  
* Active, inactive, wired, cached memories are considered used, because they store some useful information.  
* At the same time inactive, cached, free memories are considered available, because these kinds of memories can be given instantly to processes that request more memory.  
  
So inactive memory is both used and available simultaneously. Because of this, the _vm.memory.size[used]_ item is designed for informational purposes only, while _vm.memory.size[available]_ is designed to be used in triggers.

### See also

  1. [Additional details about memory calculation in different OS](http://blog.zabbix.com/when-alexei-isnt-looking#vm.memory.size)