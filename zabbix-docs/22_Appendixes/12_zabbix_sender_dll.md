---
title: Zabbix sender dynamic link library for Windows
source: https://www.zabbix.com/documentation/current/en/manual/appendix/zabbix_sender_dll
downloaded: 2025-11-14 10:47:56
---

# 12 Zabbix sender dynamic link library for Windows

#### Overview

In a Windows environment applications can send data to Zabbix server/proxy by using the Zabbix sender dynamic link library (zabbix_sender.dll) instead of having to launch an external process (zabbix_sender.exe).

zabbix_sender.h and zabbix_sender.lib are required for compiling user applications with zabbix_sender.dll.

#### Getting it

There are two ways of getting zabbix_sender.dll.

**1.** [Download](https://www.zabbix.com/download_agents) zabbix_sender.h, zabbix_sender.lib and zabbix_sender.dll files as a ZIP archive.

When choosing download options make sure to select "No encryption" under _Encryption_ and "Archive" under _Packaging_. Then download Zabbix agent (not Zabbix agent 2).

The zabbix_sender.h, zabbix_sender.lib and zabbix_sender.dll files will be inside the downloaded ZIP archive in the `bin\dev` directory. Unzip the files where you need it.

**2.** Build zabbix_sender.dll from source (see [instructions](/documentation/current/en/manual/installation/install/win_agent#overview)).

The dynamic link library with the development files will be located in the `bin\winXX\dev` directory. To use it, include the zabbix_sender.h header file and link with the zabbix_sender.lib library.

#### See also

  * [example](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/build/win32/examples/zabbix_sender/sender.c?at=refs%2Fheads%2Frelease%2F7.4) of a simple Zabbix sender utility implemented with Zabbix sender dynamic link library to illustrate the library usage;
  * [zabbix_sender.h](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/zabbix_sender/win32/zabbix_sender.h?at=refs%2Fheads%2Frelease%2F7.4) file for the interface functions of the Zabbix sender dynamic link library. This file contains documentation explaining the purpose of each interface function, its arguments, and return value.