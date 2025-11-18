---
title: Upgrade from sources
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade/sources
downloaded: 2025-11-14 10:34:14
---

# 1 Upgrade from sources  
  
#### Overview

This section provides the steps required for a successful [upgrade](/documentation/current/en/manual/installation/upgrade) from Zabbix **7.2**.x to Zabbix **7.4**.x using official Zabbix sources.

Before the upgrade make sure to read the relevant [**upgrade notes**](/documentation/current/en/manual/installation/upgrade)!

You may also want to review the [requirements](/documentation/current/en/manual/installation/requirements) for 7.4.

It may be handy to run two parallel SSH sessions during the upgrade, executing the upgrade steps in one and monitoring the server/proxy logs in another. For example, run `tail -f zabbix_server.log` or `tail -f zabbix_proxy.log` in the second SSH session showing you the latest log file entries and possible errors in real time. This can be critical for production instances.

#### Server upgrade process

##### 1 Stop server

Stop Zabbix server to make sure that no new data is inserted into database.

##### 2 Back up the existing Zabbix database

This is a very important step. Make sure that you have a backup of your database. It will help if the upgrade procedure fails (lack of disk space, power off, any unexpected problem).

##### 3 Back up configuration files, PHP files and Zabbix binaries

Make a backup copy of Zabbix binaries, configuration files and the PHP file directory.

##### 4 Install new server binaries

Use these [instructions](/documentation/current/en/manual/installation/install#installing-zabbix-daemons) to compile Zabbix server from sources.

##### 5 Review server configuration parameters

Make sure to review [Upgrade notes](/documentation/current/en/manual/installation/upgrade_notes) to check if any changes in the configuration parameters are required.

For new optional parameters, see the [What's new](/documentation/current/en/manual/introduction/whatsnew) page.

##### 6 Start new Zabbix binaries

Start new binaries. Check log files to see if the binaries have started successfully.

Zabbix server will automatically upgrade the database. When starting up, Zabbix server reports the current (mandatory and optional) and required database versions. If the current mandatory version is older than the required version, Zabbix server automatically executes the required database upgrade patches. The start and progress level (percentage) of the database upgrade is written to the Zabbix server log file. When the upgrade is completed, a "database upgrade fully completed" message is written to the log file. If any of the upgrade patches fail, Zabbix server will not start. Zabbix server will also not start if the current mandatory database version is newer than the required one. Zabbix server will only start if the current mandatory database version corresponds to the required mandatory version.
    
    
    8673:20161117:104750.259 current database version (mandatory/optional): 03040000/03040000
           8673:20161117:104750.259 required mandatory version: 03040000

Copy

✔ Copied

Before you start the server:

  * Make sure the database user has enough permissions (create table, drop table, create index, drop index)
  * Make sure you have enough free disk space.

##### 7 Install new Zabbix web interface

The minimum required PHP version is 8.0.0. Update if needed and follow [installation instructions](/documentation/current/en/manual/installation/frontend).

##### 8 Clear web browser cookies and cache

After the upgrade you may need to clear web browser cookies and web browser cache for the Zabbix web interface to work properly.

#### Proxy upgrade process

##### 1 Stop proxy

Stop Zabbix proxy.

##### 2 Back up configuration files and Zabbix proxy binaries

Make a backup copy of the Zabbix proxy binary and configuration file.

##### 3 Install new proxy binaries

Use these [instructions](/documentation/current/en/manual/installation/install#installing-zabbix-daemons) to compile Zabbix proxy from sources.

##### 4 Review proxy configuration parameters

There are no mandatory changes in this version to proxy [parameters](/documentation/current/en/manual/appendix/config/zabbix_proxy).

##### 5 Start new Zabbix proxy

Start the new Zabbix proxy. Check log files to see if the proxy has started successfully.

Zabbix proxy will automatically upgrade the database. Database upgrade takes place similarly as when starting [Zabbix server](/documentation/current/en/manual/installation/upgrade/sources#start-new-zabbix-binaries).

#### Agent upgrade process

Upgrading agents is not mandatory. You only need to upgrade agents if it is required to access the new functionality.

The upgrade procedure described in this section may be used for upgrading both the Zabbix agent and the Zabbix agent 2.

##### 1 Stop agent

Stop Zabbix agent.

##### 2 Back up configuration files and Zabbix agent binaries

Make a backup copy of the Zabbix agent binary and configuration file.

##### 3 Install new agent binaries

Use these [instructions](/documentation/current/en/manual/installation/install#installing-zabbix-daemons) to compile Zabbix agent from sources.

Alternatively, you may download pre-compiled Zabbix agents from the [Zabbix download page](http://www.zabbix.com/download.php).

##### 4 Review agent configuration parameters

There are no mandatory changes in this version neither to [agent](/documentation/current/en/manual/appendix/config/zabbix_agentd) nor to [agent 2](/documentation/current/en/manual/appendix/config/zabbix_agent2) parameters.

##### 5 Start new Zabbix agent

Start the new Zabbix agent. Check log files to see if the agent has started successfully.

#### Upgrade between minor versions

When upgrading between minor versions of 7.4.x (for example from 7.4.1 to 7.4.3) it is required to execute the same actions for server/proxy/agent as during the upgrade between major versions. The only difference is that when upgrading between minor versions no changes to the database are made.