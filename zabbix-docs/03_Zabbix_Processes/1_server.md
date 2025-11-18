---
title: Server
source: https://www.zabbix.com/documentation/current/en/manual/concepts/server
downloaded: 2025-11-14 10:33:48
---

# 1 Server

#### Overview

Zabbix server is the central process of Zabbix software.

The server performs the polling and trapping of data, it calculates triggers, sends notifications to users. It is the central component to which Zabbix agents and proxies report data on availability and integrity of systems. The server can itself remotely check networked services (such as web servers and mail servers) using simple service checks.

The server is the central repository in which all configuration, statistical and operational data is stored, and it is the entity in Zabbix that will actively alert administrators when problems arise in any of the monitored systems.

The functioning of a basic Zabbix server is broken into three distinct components; they are: Zabbix server, web frontend and database storage.

All of the configuration information for Zabbix is stored in the database, which both the server and the web frontend interact with. For example, when you create a new item using the web frontend (or API) it is added to the items table in the database. Then, about once a minute Zabbix server will query the items table for a list of the items which are active that is then stored in a cache within the Zabbix server. This is why it can take up to two minutes for any changes made in Zabbix frontend to show up in the latest data section.

#### Running server

##### If installed as package

Zabbix server runs as a daemon process. The server can be started by executing:
    
    
    systemctl start zabbix-server

Copy

✔ Copied

This will work on most of GNU/Linux systems. On other systems you may need to run:
    
    
    /etc/init.d/zabbix-server start

Copy

✔ Copied

Similarly, for stopping/restarting/viewing status, use the following commands:
    
    
    systemctl stop zabbix-server
           systemctl restart zabbix-server
           systemctl status zabbix-server

Copy

✔ Copied

##### Start up manually

If the above does not work you have to start it manually. Find the path to the zabbix_server binary and execute:
    
    
    zabbix_server

Copy

✔ Copied

You can use the following command-line parameters with Zabbix server:
    
    
    -c --config <file>              path to the configuration file (default is /usr/local/etc/zabbix_server.conf)
           -f --foreground                 run Zabbix server in foreground
           -R --runtime-control <option>   perform administrative functions
           -T --test-config                validate configuration file and exit
           -h --help                       give this help
           -V --version                    display version number

Copy

✔ Copied

Examples of running Zabbix server with command-line parameters:
    
    
    zabbix_server -c /usr/local/etc/zabbix_server.conf
           zabbix_server --help
           zabbix_server -V

Copy

✔ Copied

##### Runtime control

Runtime control options:

config_cache_reload | Reload configuration cache. Ignored if cache is being currently loaded. |   
---|---|---  
history_cache_clear=target | Clear history cache for the item specified by its ID.  
Affects all values of the item, except the first and last value. | **target** \- ID of the item  
diaginfo[=<**section** >] | Gather diagnostic information in the server log file. | **historycache** \- history cache statistics  
**valuecache** \- value cache statistics  
**preprocessing** \- preprocessing manager statistics  
**alerting** \- alert manager statistics  
**lld** \- LLD manager statistics  
**locks** \- list of mutexes (is empty on _BSD_ systems)  
**connector** \- statistics for connectors with the largest queue  
ha_status | Log high availability (HA) cluster status. |   
ha_remove_node=target | Remove the high availability (HA) node specified by its name or ID.  
Note that active/standby nodes cannot be removed. | **target** \- name or ID of the node (can be obtained by running ha_status)  
ha_set_failover_delay=delay | Set high availability (HA) failover delay.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 10s, 1m. |   
proxy_config_cache_reload[=<**target** >] | Reload proxy configuration cache. | **target** \- comma-delimited list of proxy names  
If no target is specified, reload configuration for all proxies  
secrets_reload | Reload secrets from Vault. |   
service_cache_reload | Reload the service manager cache. |   
snmp_cache_reload | Reload SNMP cache — clear SNMP engine properties (engine time, engine boots, engine id, credentials) for all hosts. Use to force a global cache clear when troubleshooting SNMP issues. |   
housekeeper_execute | Start the [housekeeping](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping) procedure.  
Ignored if the housekeeping procedure is currently in progress. |   
trigger_housekeeper_execute | Start the trigger housekeeping procedure for [services](/documentation/current/en/manual/it_services) to remove problems caused by triggers that have since been deleted, including service problems generated by such problems (considered as resolved at the time of housekeeping).  
Note that, until the housekeeping procedure is started, problems caused by now-deleted triggers might still generate service problems and assign them to services.  
  
If your setup involves many service [status calculation rules](/documentation/current/en/manual/it_services/service_tree#service-configuration) based on frequently discovered/undiscovered triggers, consider increasing the frequency of the trigger housekeeping procedure by adjusting the [ProblemHousekeepingFrequency](/documentation/current/en/manual/appendix/config/zabbix_server#problemhousekeepingfrequency) server configuration parameter.  
  
Ignored if the trigger housekeeping procedure is currently in progress. |   
log_level_increase[=<**target** >] | Increase log level, affects all processes if target is not specified.  
Not supported on _BSD_ systems. | **process type** \- All processes of specified type (e.g., poller)  
See all server process types.  
**process type,N** \- Process type and number (e.g., poller,3)  
**pid** \- Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  
log_level_decrease[=<**target** >] | Decrease log level, affects all processes if target is not specified.  
Not supported on _BSD_ systems.  
prof_enable[=<**target** >] | Enable profiling.  
Affects all processes if target is not specified.  
Enabled profiling provides details of all rwlocks/mutexes by function name. | **process type** \- All processes of specified type (e.g. history syncer)  
Supported process types as profiling targets: alerter, alert manager, availability manager, configuration syncer, discovery manager, escalator, history poller, history syncer, housekeeper, http poller, icmp pinger, ipmi manager, ipmi poller, java poller, lld manager, lld worker, odbc poller, poller, preprocessing manager, preprocessing worker, proxy poller, self-monitoring, service manager, snmp trapper, task manager, timer, trapper, unreachable poller, vmware collector  
**process type,N** \- Process type and number (e.g., history syncer,1)  
**pid** \- Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  
**scope** \- `rwlock`, `mutex`, `processing` can be used with the process type and number (e.g., history syncer,1,processing) or all processes of type (e.g., history syncer,rwlock)  
prof_disable[=<**target** >] | Disable profiling.  
Affects all processes if target is not specified. | **process type** \- All processes of specified type (e.g. history syncer)  
Supported process types as profiling targets: see `prof_enable`  
**process type,N** \- Process type and number (e.g., history syncer,1)  
**pid** \- Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  
  
Example of using runtime control to reload the server configuration cache:
    
    
    zabbix_server -c /usr/local/etc/zabbix_server.conf -R config_cache_reload

Copy

✔ Copied

Examples of using runtime control to reload the proxy configuration:
    
    
    # Reload configuration of all proxies:
           zabbix_server -R proxy_config_cache_reload
               
           # Reload configuration of Proxy1 and Proxy2:
           zabbix_server -R proxy_config_cache_reload=Proxy1,Proxy2

Copy

✔ Copied

Example of using runtime control to clear the history cache for an item:
    
    
    zabbix_server -c /usr/local/etc/zabbix_server.conf -R history_cache_clear=42243

Copy

✔ Copied

Examples of using runtime control to gather diagnostic information:
    
    
    # Gather all available diagnostic information in the server log file:
           zabbix_server -R diaginfo
           
           # Gather history cache statistics in the server log file:
           zabbix_server -R diaginfo=historycache

Copy

✔ Copied

Example of using runtime control to reload the SNMP cache:
    
    
    zabbix_server -R snmp_cache_reload

Copy

✔ Copied

When an SNMPv3 interface is updated via the Zabbix UI, Zabbix will automatically reload the new SNMPv3 credentials for that interface in most cases; use `-R snmp_cache_reload` only if polling still fails after credential changes (for example, due to engineBoots/engineID inconsistencies or non-RFC devices), or when you need to force a global SNMP cache clear for troubleshooting.

Example of using runtime control to trigger execution of housekeeper:
    
    
    zabbix_server -c /usr/local/etc/zabbix_server.conf -R housekeeper_execute

Copy

✔ Copied

Examples of using runtime control to change log level:
    
    
    # Increase log level of all processes:
           zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_increase
           
           # Increase log level of second poller process:
           zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_increase=poller,2
           
           # Increase log level of process with PID 1234:
           zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_increase=1234
           
           # Decrease log level of all http poller processes:
           zabbix_server -c /usr/local/etc/zabbix_server.conf -R log_level_decrease="http poller"

Copy

✔ Copied

Example of setting the HA failover delay to the minimum of 10 seconds:
    
    
    zabbix_server -R ha_set_failover_delay=10s

Copy

✔ Copied

##### Process user

Zabbix server is designed to run as a non-root user. It will run as whatever non-root user it is started as. So you can run server as any non-root user without any issues.

If you will try to run it as 'root', it will switch to a hardcoded 'zabbix' user, which must be [present](/documentation/current/en/manual/installation/install) on your system. You can only run server as 'root' if you modify the 'AllowRoot' parameter in the server configuration file accordingly.

If Zabbix server and [agent](agent) are run on the same machine it is recommended to use a different user for running the server than for running the agent. Otherwise, if both are run as the same user, the agent can access the server configuration file and any Admin level user in Zabbix can quite easily retrieve, for example, the database password.

##### Configuration file

See the [configuration file](/documentation/current/en/manual/appendix/config/zabbix_server) options for details on configuring zabbix_server.

##### Start-up scripts

The scripts are used to automatically start/stop Zabbix processes during system's start-up/shutdown. The scripts are located under directory misc/init.d.

#### Server process types and threads

  * `agent poller` \- asynchronous poller process for passive checks with a worker thread
  * `alert manager` \- alert queue manager
  * `alert syncer` \- alert DB writer
  * `alerter` \- process for sending notifications
  * `availability manager` \- process for host availability updates
  * `browser poller` \- poller for browser item checks
  * `configuration syncer` \- process for managing in-memory cache of configuration data
  * `configuration syncer worker` \- process for resolving and synchronizing user macro values in item names
  * `connector manager` \- manager process for connectors
  * `connector worker` \- process for handling requests from the connector manager
  * `discovery manager` \- manager process for discovery of devices
  * `discovery worker` \- process for handling discovery tasks from the discovery manager
  * `escalator` \- process for escalation of actions
  * `ha manager` \- process for managing high availability
  * `history poller` \- process for handling calculated checks requiring a database connection
  * `history syncer` \- history DB writer
  * `housekeeper` \- process for removal of old historical data
  * `http agent poller` \- asynchronous poller process for HTTP checks with a worker thread
  * `http poller` \- web monitoring poller
  * `icmp pinger` \- poller for icmpping checks
  * `internal poller` \- poller for internal checks
  * `ipmi manager` \- IPMI poller manager
  * `ipmi poller` \- poller for IPMI checks
  * `java poller` \- poller for Java checks
  * `lld manager` \- manager process of low-level discovery tasks
  * `lld worker` \- worker process of low-level discovery tasks
  * `odbc poller` \- poller for ODBC checks
  * `poller` \- normal poller for passive checks
  * `preprocessing manager` \- manager of preprocessing tasks with preprocessing worker threads
  * `preprocessing worker` \- thread for data preprocessing
  * `proxy poller` \- poller for passive proxies
  * `proxy group manager` \- manager of proxy load balancing and high availability
  * `report manager`\- manager of scheduled report generation tasks
  * `report writer` \- process for generating scheduled reports
  * `self-monitoring` \- process for collecting internal server statistics
  * `service manager` \- process for managing services by receiving information about problems, problem tags, and problem recovery from history syncer, task manager, and alert manager
  * `snmp poller` \- asynchronous poller process for SNMP checks with a worker thread (`walk[OID]` and `get[OID]` items only)
  * `snmp trapper` \- trapper for SNMP traps
  * `task manager` \- process for remote execution of tasks requested by other components (e.g., close problem, acknowledge problem, check item value now, remote command functionality)
  * `timer` \- timer for processing maintenances
  * `trapper` \- trapper for active checks, traps, proxy communication
  * `trigger housekeeper` \- process for removing problems generated by triggers that have been deleted
  * `unreachable poller` \- poller for unreachable devices
  * `vmware collector` \- VMware data collector responsible for data gathering from VMware services

The server log file can be used to observe these process types.

Various types of Zabbix server processes can be monitored using the **zabbix[process, <type>,<mode>,<state>]** internal [item](/documentation/current/en/manual/config/items/itemtypes/internal).

##### History syncer transaction statistics

The history syncer process title displays detailed statistics about history syncer transactions:
    
    
    205182 ?        S      0:00  zabbix_server: history syncer #2 [processed 0 values, 0+0 triggers in 0.000021 (0.000000,0.000000,0.000000,0.000000,0.000000) sec, idle 1 sec]
           205183 ?        S      0:00  zabbix_server: history syncer #3 [processed 18 values, 7+0 triggers in 0.002612 (0.001108,0.000000,0.000000,0.001208,0.000014) sec, idle 1 sec]
           205184 ?        S      0:00  zabbix_server: history syncer #4 [processed 0 values, 0+0 triggers in 0.000027 (0.000000,0.000000,0.000000,0.000000,0.000000) sec, idle 1 sec]

Copy

✔ Copied

In "A+B triggers":

  * A - triggers processed because of history values;
  * B - triggers processed because of timers.

The timings, in "processed...in N (<timings>) sec", are:

  * Time spent writing item values into database;
  * Time spent updating item data (state, errors, host inventory, etc);
  * Time spent flushing trends to database;
  * Time spent calculating triggers;
  * Time spent processing events and actions.

#### Supported platforms

Due to the security requirements and mission-critical nature of server operation, UNIX is the only operating system that can consistently deliver the necessary performance, fault tolerance and resilience. Zabbix operates on market leading versions.

Zabbix server is tested on the following platforms:

  * Linux
  * Solaris
  * AIX
  * HP-UX
  * Mac OS X
  * FreeBSD
  * OpenBSD
  * NetBSD
  * SCO Open Server

Zabbix may work on other Unix-like operating systems as well.

#### Locale

Note that the server requires a UTF-8 locale so that some textual items can be interpreted correctly. Most modern Unix-like systems have a UTF-8 locale as default, however, there are some systems where that may need to be set specifically.