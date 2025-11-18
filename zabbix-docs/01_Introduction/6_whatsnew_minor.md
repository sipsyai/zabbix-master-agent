---
title: What's new in Zabbix 7.4.x
source: https://www.zabbix.com/documentation/current/en/manual/introduction/whatsnew_minor
downloaded: 2025-11-14 10:33:45
---

# 6 What's new in Zabbix 7.4.x

This page provides collective information on new features included in minor releases of the major Zabbix version.

See also [What's new](/documentation/current/en/manual/introduction/whatsnew) of the major version.

For changes to existing templates and information on new templates covering various devices, services, and partner solutions, see [Template changes](/documentation/current/en/manual/installation/template_changes).

## What's new in Zabbix 7.4.4

**Warning!** Upgrading to this version is not recommended due to [errors](/documentation/current/en/manual/installation/known_issues#known-issues-in-7.4.4) related to graphs and the Zabbix agent 2 MySQL plugin.

#### PostgreSQL 18 support

The maximum [supported version](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) for PostgreSQL is now 18.X.

#### TimescaleDB 2.22 support

The maximum [supported version](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) for TimescaleDB is now 2.22.X.

#### Redis plugin — TLS support and startup-time validation

TLS support has been added to the [Redis plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/redis_plugin) for Zabbix agent 2.

Startup-time validation of the plugin TLS configuration was implemented and validation/error messages improved. An invalid configuration logic (for example: using connection type `verify_full` without specifying `TLSCAFile`) can prevent Zabbix agent 2 from starting.

## What's new in Zabbix 7.4.3

#### TNS name support for Oracle plugin

Oracle-native TNS name support has been added to the Oracle plugin in Zabbix agent 2. The TNS key or TNS value can be specified on the level of item key [parameters](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2#oracleping) or the plugin [configuration](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/oracle_plugin) (for named session or default parameters).

TNS name support allows connection description in a clustered DB environment with a single Zabbix host. For more information, see the Oracle plugin [README](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/oracle/README.md?at=release%2F7.0).

#### Increased maximum timeout for the zabbix_get and zabbix_js

The maximum value for the `timeout` parameter of the [zabbix_get](/documentation/current/en/manual/concepts/get) and [zabbix_js](/documentation/current/en/manual/concepts/js) command-line utilities has been increased to 600 seconds.

#### MariaDB 12.0 support

The maximum [supported version](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) for MariaDB is now 12.0.X.

#### Highlight whole row in Problems view and Problems widget

The _Highlight whole row_ option is now available in the non-compact [Monitoring > Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#overview) view and in the [Problems](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems) dashboard widget.

## What's new in Zabbix 7.4.2

#### Additional role support for Oracle plugin

Oracle plugin [items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2#oracle.diskgroups.stats) for Zabbix agent 2 now support additional roles such as SysBACKUP, SysDG, SysKM, or SysRAC in the login options.

#### Automatic reload of SNMPv3 credentials

SNMP agent walk[] and get[] item checks now automatically reload updated SNMPv3 authentication and privacy settings when the corresponding SNMPv3 interface is modified. The manual cache reload command [-R snmp_cache_reload](/documentation/current/en/manual/concepts/server#runtime-control) remains available for troubleshooting and for devices that do not fully comply with SNMPv3 specifications.

#### smart.disk.discovery — new **type** parameter

The [smart.disk.discovery](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2#smart.disk.discovery) item (Zabbix agent 2 S.M.A.R.T. plugin) now accepts an optional **type** parameter to specify a value to scan for the disks.

## What's new in Zabbix 7.4.1

#### TimescaleDB 2.21 support

The maximum [supported version](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) for TimescaleDB is now 2.21.X.

#### Server/proxy preprocessing diagnostic information

Top items sections sorted by the received value number and size have been added to the preprocessing section of server/proxy runtime diagnostic information. Top item IDs with the longest processing times are being highlighted.

This information is accessible by running Zabbix server or proxy with the diaginfo runtime option, for example `zabbix_server -R diaginfo=preprocessing`.

#### Bypass preprocessing manager for items without preprocessing

To reduce processing load, item values from items that have neither preprocessing nor dependent items are added directly to the history cache or sent to the LLD manager (see [Preprocessing details](/documentation/current/en/manual/config/items/preprocessing/preprocessing_details)). Previously, all item values passed through the preprocessing manager regardless of preprocessing configuration.

#### GLPi webhook integration updated

The [GLPi media type](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/glpi/README.md?at=refs%2Fheads%2Frelease%2F7.4) now supports authentication using application tokens.