---
title: Agent vs agent 2 comparison
source: https://www.zabbix.com/documentation/current/en/manual/appendix/agent_comparison
downloaded: 2025-11-14 10:48:00
---

# 16 Agent vs agent 2 comparison

This section describes the differences between the Zabbix agent and the Zabbix agent 2.

Programming language | C | Go with some parts in C  
---|---|---  
Daemonization | yes | by systemd only (yes on Windows)  
Supported extensions | Custom [loadable modules](/documentation/current/en/manual/extensions/loadablemodules) in C. | Custom [plugins](/documentation/current/en/manual/extensions/plugins) in Go.  
_Requirements_  
Supported platforms | Linux, IBM AIX, FreeBSD, NetBSD, OpenBSD, HP-UX, Mac OS X, Solaris: 9, 10, 11, Windows: all desktop and server versions since XP | Linux, Windows: all desktop and server versions, on which a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) can be installed.  
Supported crypto libraries | GnuTLS 3.1.18 and newer  
OpenSSL 1.0.1, 1.0.2, 1.1.0, 1.1.1, 3.0.x  
LibreSSL - tested with versions 2.7.4, 2.8.2 (certain limitations apply, see the [Encryption](/documentation/current/en/manual/encryption#compiling-zabbix-with-encryption-support) page for details). | Linux: OpenSSL 1.0.1 and later.  
MS Windows: OpenSSL 1.1.1 or later.  
The OpenSSL library must have PSK support enabled. LibreSSL is not supported.  
_Monitoring processes_  
Processes | A separate active check process for each server/proxy record. | Single process with automatically created threads.  
The maximum number of threads is determined by the GOMAXPROCS environment variable.  
Metrics | **UNIX** : see a list of supported [items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
  
**Windows** : see a list of additional Windows-specific [items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys). | **UNIX** : All metrics supported by Zabbix agent.  
Additionally, the agent 2 provides Zabbix-native monitoring solution for: Docker, Memcached, MySQL, PostgreSQL, Redis, systemd, and other monitoring targets - see a full list of agent 2 specific [items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2).  
  
**Windows** : All metrics supported by Zabbix agent, and also net.tcp.service* checks of HTTPS, LDAP.  
Additionally, the agent 2 provides Zabbix-native monitoring solution for: PostgreSQL, Redis.  
Concurrency | Active checks for single server are executed sequentially. | Checks from different plugins or multiple checks within one plugin can be executed concurrently.  
Third-party traps | no | yes  
_Additional features_  
Persistent storage | no | yes  
Persistent files for log*[] metrics | yes (only on Unix) | no  
Log data upload | Can be performed during log gathering to free the buffer. | Log gathering is stopped when the buffer is full, therefore the [BufferSize](/documentation/current/en/manual/appendix/config/zabbix_agent2) parameter must be at least MaxLinesPerSecond x 2.  
Changes user at runtime | yes (Unix-like systems only) | no (controlled by systemd)  
User-configurable ciphersuites | yes | no  
  
**See also:**

  * _Zabbix processes description_ : [Zabbix agent](/documentation/current/en/manual/concepts/agent), [Zabbix agent 2](/documentation/current/en/manual/concepts/agent2)
  * _Configuration parameters_ : Zabbix agent [UNIX](/documentation/current/en/manual/appendix/config/zabbix_agentd) / [Windows](/documentation/current/en/manual/appendix/config/zabbix_agentd_win), Zabbix agent 2 [UNIX](/documentation/current/en/manual/appendix/config/zabbix_agent2) / [Windows](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)