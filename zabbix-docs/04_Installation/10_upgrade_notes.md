---
title: Upgrade notes for 7.4.0
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade_notes
downloaded: 2025-11-14 10:34:23
---

# 10 Upgrade notes for 7.4.0

These notes are for upgrading from Zabbix 7.2.x to Zabbix 7.4.0.

All notes are grouped into:

  * **Breaking changes** \- changes that may break existing installations and other critical information related to the upgrade process
  * **Other** \- all remaining information describing the changes in Zabbix functionality

See also:

  * [Upgrade procedure](/documentation/current/en/manual/installation/upgrade) for all relevant information about upgrading from versions before Zabbix 7.4.0;
  * [Upgrading HA cluster](/documentation/current/en/manual/concepts/server/ha#upgrading-ha-cluster) for instructions on upgrading servers in a **high-availability** (HA) cluster.

#### Upgrade process

To complete a successful Zabbix server upgrade on MySQL/MariaDB, you may require to set `GLOBAL log_bin_trust_function_creators = 1` in MySQL if binary logging is enabled, there are no superuser privileges and `log_bin_trust_function_creators = 1` is not set in MySQL configuration file.

To set the variable using the MySQL console, run:
    
    
    mysql> SET GLOBAL log_bin_trust_function_creators = 1;

Copy

✔ Copied

Once the upgrade has been successfully completed, this option can be disabled:
    
    
    mysql> SET GLOBAL log_bin_trust_function_creators = 0;

Copy

✔ Copied

## Breaking changes

#### PCRE library dropped

The [PCRE](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) (or PCRE1) library has been dropped. Zabbix is now compiled with PCRE2.

#### Managing own user media

All users are now allowed to manage their own media by default.

User permissions to change media details for themselves can be granted (or revoked) based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit own media_ option).

Additionally, Super admin user permissions to change media details for others can also be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit user media_ option).

If upgrading from older versions, both options will be enabled for all roles having the _Default access to new actions_ enabled. Note that if _Default access to new actions_ is not enabled, administrators and super administrators **may lose** the ability to edit media after the upgrade.

#### Escaping of backslashes in history function parameters

Proper escaping of backslashes has been added in history function string parameters since Zabbix 7.0.0.

As additional backslashes are added during the upgrade from pre-7.0 Zabbix versions, this leads to longer parameters which may result in broken trigger functions if the parameter length exceeds the maximum data size of 255 characters.

To avoid this problem it is recommended to manually move long parameters into user macros before the upgrade.

Additional checks for the resulting parameter length have been added for upgrades from pre-7.0 Zabbix versions. If the resulting length exceeds the maximum size, such parameters are **not upgraded** while printing a warning in the logs asking users to fix the listed parameters manually.

See also [escaping-related upgrade issues](/documentation/current/en/manual/installation/known_issues/db_upgrade_escaping).

#### MSSQL Zabbix agent 2 plugin update

The template [MSSQL by Zabbix agent 2](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mssql_agent2) has been updated with filters to include or exclude discovered quorum members by name as well as a service filter that allows filtering by cluster name to exclude empty clusters. To have the template work without errors, the [MSSQL Zabbix agent 2 plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mssql_plugin) must be updated to a version equal to or above 7.4.0.

#### Minimum required libssh2 version

The minimum required libssh2 version has been raised from 1.0.0 to 1.8.0.

#### Host prototypes on discovered hosts

If your current configuration includes [host prototypes](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes) that use templates containing other host prototypes, upgrading to Zabbix 7.4 will cause all discovered hosts to have the host prototypes defined in those templates. If this behavior is not intended, please manually delete the host prototypes from the relevant templates before upgrading.

To identify discovered hosts that will receive host prototypes during the upgrade, you can run the following SQL query in your Zabbix database:
    
    
    SELECT h.hostid,ht.templateid
           FROM hosts_templates ht
           JOIN hosts h ON ht.hostid=h.hostid
           WHERE h.flags=4
             AND EXISTS (
               SELECT NULL
               FROM items i,host_discovery hd
               WHERE i.hostid=ht.templateid
               AND hd.parent_itemid=i.itemid
               )
           ORDER BY hostid;

Copy

✔ Copied

#### Database connection parameters

[DBPort](/documentation/current/en/manual/appendix/config/zabbix_server#dbport) and [DBSocket](/documentation/current/en/manual/appendix/config/zabbix_server#dbsocket) are now mutually exclusive. When specifying database connection parameters, you may define either DBPort or DBSocket, or leave both undefined to use defaults.

## Other

#### Unsupported SNMP walk/discovery items with no valid OIDs

SNMP [walk](/documentation/current/en/manual/config/items/itemtypes/snmp#step-3) items, in case none of the OIDs or OID instances exist, now return an error and the item becomes unsupported. The non-existing OID/instance details are logged with DebugLevel=5. Previously they would return an empty string in such cases.

Similarly, SNMP [discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids) items, in case none of the OIDs or OID instances exist, now return an error and the item becomes unsupported. Previously they would return an empty array in such cases.

Note that empty string/array is now returned only if the OID/instance exists, but there is no data for it.

#### Managing history cache

In some data collection scenarios, specific items can temporarily block the server/proxy history cache. This may delay writing history data to the database and slow down the system. To help manage the history cache, the following improvements have been introduced:

  * **Manual cache clearing:** The new history_cache_clear=target runtime command for Zabbix [server](/documentation/current/en/manual/concepts/server#runtime-control)/[proxy](/documentation/current/en/manual/concepts/proxy#runtime-control) allows you to manually clear the history cache for a specific item by its ID.
  * **Automatic cache clearing:** When you disable an item, it is immediately removed from the history cache (except for its last value, which is kept for logs). Similarly, when you disable a host, all its items are removed from the history cache (except for their last values).
  * **Cache diagnostics logging:** When the history cache is full, Zabbix server/proxy now logs history cache diagnostic information starting from [DebugLevel=3](/documentation/current/en/manual/appendix/config/zabbix_server#debuglevel) (previously DebugLevel=4). The log contains items with the most values in the history cache.

For long-term system stability, make sure that data collection is balanced with available resources (database performance, cache size, collection intervals, log item parameters, etc.). You can monitor Zabbix history cache using the [zabbix[wcache]](/documentation/current/en/manual/config/items/itemtypes/internal#wcache) internal item. You can also consider increasing the size of the history cache for Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#historycachesize)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#historycachesize).

#### Separate menu section for user notifications

For better visibility of user media, user notifications now have their own [menu section](/documentation/current/en/manual/web_interface/user_profile) under _User settings_.

The new Notifications section contains two tabs - _Media_ and _Frontend notifications_ , which previously were part of the user profile section.

#### Correct information from nested host groups in maps

Information from nested host groups is now correctly displayed in maps, for example:

  * Host group label now displays the problem summary from all hosts in nested host groups;
  * "Host group elements" view now displays a separate map element for each host in the nested host groups;
  * Map label now displays summary of all problems contained in nested host groups.

#### Database table for settings converted

The `settings` table now replaces the `config` table for storing [global configuration](/documentation/current/en/manual/web_interface/frontend_sections/administration/general) parameters. The new table uses a key-value format instead of storing parameters in a single row with a column per parameter. For an example of how this affects data exchange, see [Server-proxy data exchange protocol](/documentation/current/en/manual/appendix/protocols/server_proxy) (`"settings"` object).

#### Increased maximum cache sizes for server and proxy

The maximum cache sizes have been raised from 2 GB to 16 GB to delay cache exhaustion and sustain operation during temporary issues (e.g. configuration, database, or network problems):

  * server: the maximum value for [HistoryCacheSize](/documentation/current/en/manual/appendix/config/zabbix_server#historycachesize), [HistoryIndexCacheSize](/documentation/current/en/manual/appendix/config/zabbix_server#historyindexcachesize), and [TrendCacheSize](/documentation/current/en/manual/appendix/config/zabbix_server#trendcachesize) have been increased;
  * proxy: the maximum values for [HistoryCacheSize](/documentation/current/en/manual/appendix/config/zabbix_proxy#historycachesize) and [HistoryIndexCacheSize](/documentation/current/en/manual/appendix/config/zabbix_proxy#historyindexcachesize) have been increased.

#### Reduced default user sessions storage period

The default [storage period](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping#configuration) for user session data has been reduced from 365 days to 31 days. This change affects the [hk_sessions](/documentation/current/en/manual/api/reference/housekeeping/object) parameter, which now defaults to 31d instead of 365d.

#### Minimum supported Go version

The minimum supported Go version has been raised from 1.21 to 1.23.

If you previously built Zabbix [agent 2](/documentation/current/en/manual/concepts/agent2), agent 2 [loadable plugins](/documentation/current/en/manual/extensions/plugins#loadable), or [web service](/documentation/current/en/manual/concepts/web_service) from source using a Go version older than 1.23, it is recommended to rebuild these components using a [supported Go version](/documentation/current/en/manual/installation/requirements#agent-2) to receive the latest security updates and bug fixes. Components built with an older Go version will continue to work, but [upgrading](/documentation/current/en/manual/installation/upgrade/sources#agent-upgrade-process) them will require a newer Go environment.

#### Template upgrade for Host Wizard

The new [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard) introduces a guided, step-by-step interface for setting up your monitoring target (device, application, service, etc.) in Zabbix. It simplifies the configuration of new or existing hosts by walking users through key steps such as selecting a template, installing Zabbix agent, adding host interfaces, and more.

After upgrading from an earlier Zabbix version, templates must be upgraded to work with the Host Wizard. For instructions, see [Template upgrade](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade).