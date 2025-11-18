---
title: Upgrade procedure
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade
downloaded: 2025-11-14 10:34:13
---

# 7 Upgrade procedure

#### Overview

This section provides upgrade information for Zabbix **7.4** :

  * Using packages for [Red Hat Enterprise Linux](/documentation/current/en/manual/installation/upgrade/packages/rhel) or [Debian/Ubuntu](/documentation/current/en/manual/installation/upgrade/packages/debian_ubuntu)
  * Using [sources](/documentation/current/en/manual/installation/upgrade/sources)

Related instructions:

  * For servers in a high-availability (HA) cluster, see [Upgrading HA cluster](/documentation/current/en/manual/concepts/server/ha#upgrading-ha-cluster)
  * For TimescaleDB database, see [Upgrading TimescaleDB schema](/documentation/current/en/manual/appendix/install/timescaledb#upgrading-timescaledb-schema)

Upgrading Zabbix agents is recommended but not mandatory.

Upgrading Zabbix proxies is highly recommended. Zabbix server fully supports proxies that are of the same major version as the server. Zabbix server also supports proxies that are **no older** than Zabbix server previous LTS release version, but with limited functionality (data collection, execution of [remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command), [immediate item value checks](/documentation/current/en/manual/config/items/check_now)). Configuration update is also disabled, and [outdated](/documentation/current/en/manual/appendix/compatibility#supported-zabbix-proxies) proxies will only work with old configuration.

Proxies that are older than Zabbix server previous LTS release version or newer than Zabbix server major version are not supported. Zabbix server will ignore data from unsupported proxies and all communication with Zabbix server will fail with a warning. For more information, see [Version compatibility](/documentation/current/en/manual/appendix/compatibility#supported-zabbix-proxies).

To minimize downtime and data loss during the upgrade, it is recommended to stop, upgrade, and start Zabbix server and then stop, upgrade, and start Zabbix proxies one after another. During server downtime, running proxies will continue data collection. Once the server is up and running, [outdated](/documentation/current/en/manual/appendix/compatibility#supported-zabbix-proxies) proxies will send the data to the newer server (proxy configuration will not be updated though) and will remain partly functional. Any notifications for problems during Zabbix server downtime will be generated only after the upgraded server is started.

If Zabbix proxy is started for the first time and the SQLite database file is missing, proxy creates it automatically.

**Note** that if Zabbix proxy uses SQLite3 and on startup detects that existing database file version is older than required, it will **delete the database file automatically** and create a new one. Therefore, history data stored in the SQLite database file will be lost. If Zabbix proxy's version is older than the database file version, Zabbix will log an error and exit.

Depending on the database size, the database upgrade to version 7.4 may take a long time.

Direct upgrade to Zabbix 7.4.x is possible from Zabbix **7.2**.x, **7.0**.x, **6.4**.x, **6.2**.x, **6.0**.x, **5.4**.x, **5.2**.x, **5.0**.x, **4.4**.x, **4.2**.x, **4.0**.x, **3.4**.x, **3.2**.x, **3.0**.x, **2.4**.x, **2.2**.x and **2.0**.x. For upgrading from earlier versions consult Zabbix documentation for 2.0 and earlier.

Please be aware that after upgrading some third-party software integrations in Zabbix might be affected, if the external software is not compatible with the upgraded Zabbix version.

The following upgrade notes are available:

7.2.x | For:  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Support of PCRE library dropped.  
---|---|---  
7.0.x LTS | For:  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Support of Oracle DB dropped.  
6.4.x | For:  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required PHP version upped from 7.4.0 to 8.0.0.  
Asynchronous pollers for agent, HTTP agent and SNMP walk[oid] checks.  
Separate database table for proxies.  
Default location for Windows agent configuration file changed.  
Oracle DB deprecated.  
Old numeric (float) value type dropped.  
6.2.x | For:  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required MySQL version raised from 8.0.0 to 8.0.30.  
'libevent_pthreads' library is required for Zabbix server/proxy.  
Upon the first launch after an upgrade, Zabbix proxy with SQLite3 automatically drops the old version of the database (with all the history) and creates a new one.  
6.0.x LTS | For:  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required PHP version upped from 7.2.5 to 7.4.0.  
Service monitoring reworked significantly.  
Deterministic triggers need to be created during the upgrade. If binary logging is enabled for MySQL/MariaDB, this requires superuser privileges or setting the variable/configuration parameter _log_bin_trust_function_creators = 1_. See [Database creation scripts](/documentation/current/en/manual/appendix/install/db_scripts#mysqlmariadb) for instructions how to set the variable.  
5.4.x | For:  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required database versions upped.  
Server/proxy will not start if outdated database.  
Audit log records lost because of database structure change.  
5.2.x | For:  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required database versions upped.  
Aggregate items removed as a separate type.  
5.0.x LTS | For:  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required PHP version upped from 7.2.0 to 7.2.5.  
Password hashing algorithm changed from MD5 to bcrypt.  
4.4.x | For:  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Support of IBM DB2 dropped.  
Minimum required PHP version upped from 5.4.0 to 7.2.0.  
Minimum required database versions upped.  
Changed Zabbix PHP file directory.  
4.2.x | For:  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Jabber, Ez Texting media types removed.  
4.0.x LTS | For:  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Older proxies no longer can report data to an upgraded server.  
Newer agents no longer will be able to work with an older Zabbix server.  
3.4.x | For:  
Zabbix [4.0](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade_notes_400)  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | 'libpthread' and 'zlib' libraries now mandatory.  
Support for plain text protocol dropped and header is mandatory.  
Pre-1.4 version Zabbix agents are no longer supported.  
The Server parameter in passive proxy configuration now mandatory.  
3.2.x | For:  
Zabbix [3.4](https://www.zabbix.com/documentation/3.4/manual/installation/upgrade_notes_340)  
Zabbix [4.0](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade_notes_400)  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | SQLite support as backend database dropped for Zabbix server/frontend.  
Perl Compatible Regular Expressions (PCRE) supported instead of POSIX extended.  
'libpcre' and 'libevent' libraries mandatory for Zabbix server.  
Exit code checks added for user parameters, remote commands and system.run[] items without the 'nowait' flag as well as Zabbix server executed scripts.  
Zabbix Java gateway has to be upgraded to support new functionality.  
3.0.x LTS | For:  
Zabbix [3.2](https://www.zabbix.com/documentation/3.2/manual/installation/upgrade_notes_320)  
Zabbix [3.4](https://www.zabbix.com/documentation/3.4/manual/installation/upgrade_notes_340)  
Zabbix [4.0](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade_notes_400)  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Database upgrade may be slow, depending on the history table size.  
2.4.x | For:  
Zabbix [3.0](https://www.zabbix.com/documentation/3.0/manual/installation/upgrade_notes_300)  
Zabbix [3.2](https://www.zabbix.com/documentation/3.2/manual/installation/upgrade_notes_320)  
Zabbix [3.4](https://www.zabbix.com/documentation/3.4/manual/installation/upgrade_notes_340)  
Zabbix [4.0](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade_notes_400)  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required PHP version upped from 5.3.0 to 5.4.0.  
LogFile agent parameter must be specified.  
2.2.x LTS | For:  
Zabbix [2.4](https://www.zabbix.com/documentation/2.4/manual/installation/upgrade_notes_240)  
Zabbix [3.0](https://www.zabbix.com/documentation/3.0/manual/installation/upgrade_notes_300)  
Zabbix [3.2](https://www.zabbix.com/documentation/3.2/manual/installation/upgrade_notes_320)  
Zabbix [3.4](https://www.zabbix.com/documentation/3.4/manual/installation/upgrade_notes_340)  
Zabbix [4.0](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade_notes_400)  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Node-based distributed monitoring removed.  
2.0.x | For:  
Zabbix [2.2](https://www.zabbix.com/documentation/2.2/manual/installation/upgrade_notes_220)  
Zabbix [2.4](https://www.zabbix.com/documentation/2.4/manual/installation/upgrade_notes_240)  
Zabbix [3.0](https://www.zabbix.com/documentation/3.0/manual/installation/upgrade_notes_300)  
Zabbix [3.2](https://www.zabbix.com/documentation/3.2/manual/installation/upgrade_notes_320)  
Zabbix [3.4](https://www.zabbix.com/documentation/3.4/manual/installation/upgrade_notes_340)  
Zabbix [4.0](https://www.zabbix.com/documentation/4.0/manual/installation/upgrade_notes_400)  
Zabbix [4.2](https://www.zabbix.com/documentation/4.2/manual/installation/upgrade_notes_420)  
Zabbix [4.4](https://www.zabbix.com/documentation/4.4/manual/installation/upgrade_notes_440)  
Zabbix [5.0](https://www.zabbix.com/documentation/5.0/manual/installation/upgrade_notes_500)  
Zabbix [5.2](https://www.zabbix.com/documentation/5.2/manual/installation/upgrade_notes_520)  
Zabbix [5.4](https://www.zabbix.com/documentation/5.4/manual/installation/upgrade_notes_540)  
Zabbix [6.0](https://www.zabbix.com/documentation/6.0/manual/installation/upgrade_notes_600)  
Zabbix [6.2](https://www.zabbix.com/documentation/6.2/manual/installation/upgrade_notes_620)  
Zabbix [6.4](https://www.zabbix.com/documentation/6.4/manual/installation/upgrade_notes_640)  
Zabbix [7.0](https://www.zabbix.com/documentation/7.0/manual/installation/upgrade_notes_700)  
Zabbix [7.2](https://www.zabbix.com/documentation/7.2/manual/installation/upgrade_notes_720)  
Zabbix [7.4](/documentation/current/en/manual/installation/upgrade_notes) | Minimum required PHP version upped from 5.1.6 to 5.3.0.  
Case-sensitive MySQL database required for proper server work; character set utf8 and utf8_bin collation is required for Zabbix server to work properly with MySQL database. See [database creation scripts](/documentation/current/en/manual/appendix/install/db_scripts#mysqlmariadb).  
'mysqli' PHP extension required instead of 'mysql'.