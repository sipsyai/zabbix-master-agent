---
title: Large file support
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/large_file_support
downloaded: 2025-11-14 10:47:23
---

# 5 Large file support

Large file support, often abbreviated to LFS, is the term applied to the ability to work with files larger than 2 GB on 32-bit operating systems. Support for large files affects at least [log file monitoring](/documentation/current/en/manual/config/items/itemtypes/log_items) and all [vfs.file.* items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#supported-item-keys). Large file support depends on the capabilities of a system at Zabbix compilation time, but is completely disabled on a 32-bit Solaris due to its incompatibility with procfs and swapctl.