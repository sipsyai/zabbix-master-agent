---
title: Proxy
source: https://www.zabbix.com/documentation/current/en/manual/concepts/proxy
downloaded: 2025-11-14 10:33:52
---

# 4 Proxy

#### Overview

Zabbix proxy is a process that may collect monitoring data from one or more monitored devices and send the information to the Zabbix server, essentially working on behalf of the server. All collected data is buffered locally and then transferred to the Zabbix server the proxy belongs to.

Deploying a proxy is optional, but may be very beneficial to distribute the load of a single Zabbix server. If only proxies collect data, processing on the server becomes less CPU and disk I/O hungry.

A Zabbix proxy is the ideal solution for centralized monitoring of remote locations, branches and networks with no local administrators.

Zabbix proxy requires a separate database.

Note that databases supported with Zabbix proxy are SQLite, MySQL and PostgreSQL.

See also: [Using proxies in a distributed environment](/documentation/current/en/manual/distributed_monitoring/proxies)

#### Running proxy

##### If installed as package

Zabbix proxy runs as a daemon process. The proxy can be started by executing:
    
    
    systemctl start zabbix-proxy

Copy

✔ Copied

This will work on most of GNU/Linux systems. On other systems you may need to run:
    
    
    /etc/init.d/zabbix-proxy start

Copy

✔ Copied

Similarly, for stopping/restarting/viewing status of Zabbix proxy, use the following commands:
    
    
    systemctl stop zabbix-proxy
           systemctl restart zabbix-proxy
           systemctl status zabbix-proxy

Copy

✔ Copied

##### Start up manually

If the above does not work you have to start it manually. Find the path to the zabbix_proxy binary and execute:
    
    
    zabbix_proxy

Copy

✔ Copied

You can use the following command-line parameters with Zabbix proxy:
    
    
    -c --config <file>              path to the configuration file
           -f --foreground                 run Zabbix proxy in foreground
           -R --runtime-control <option>   perform administrative functions
           -T --test-config                validate configuration file and exit
           -h --help                       give this help
           -V --version                    display version number

Copy

✔ Copied

Examples of running Zabbix proxy with command-line parameters:
    
    
    zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf
           zabbix_proxy --help
           zabbix_proxy -V

Copy

✔ Copied

##### Runtime control

Runtime control options:

config_cache_reload | Reload configuration cache. Ignored if cache is being currently loaded.  
Active Zabbix proxy will connect to the Zabbix server and request configuration data.  
Passive Zabbix proxy will request configuration data from Zabbix server the next time when the server connects to the proxy. |   
---|---|---  
history_cache_clear=target | Clear history cache for the item specified by its ID.  
Affects all values of the item, except the first and last value. | **target** \- ID of the item  
diaginfo[=<**section** >] | Gather diagnostic information in the proxy log file. | **historycache** \- history cache statistics  
**preprocessing** \- preprocessing manager statistics  
**locks** \- list of mutexes (is empty on _BSD_ systems)  
snmp_cache_reload | Reload SNMP cache — clear SNMP engine properties (engine time, engine boots, engine id, credentials) for all hosts. Use to force a global cache clear when troubleshooting SNMP issues. |   
housekeeper_execute | Start the housekeeping procedure. Ignored if the housekeeping procedure is currently in progress. |   
log_level_increase[=<**target** >] | Increase log level, affects all processes if target is not specified.   
Not supported on _BSD_ systems. | **process type** \- All processes of specified type (e.g., poller)  
See all proxy process types.  
**process type,N** \- Process type and number (e.g., poller,3)  
**pid** \- Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  
log_level_decrease[=<**target** >] | Decrease log level, affects all processes if target is not specified.  
Not supported on _BSD_ systems.  
prof_enable[=<**target** >] | Enable profiling.  
Affects all processes if target is not specified.  
Enabled profiling provides details of all rwlocks/mutexes by function name. | **process type** \- All processes of specified type (e.g., history syncer)  
See all proxy process types.  
**process type,N** \- Process type and number (e.g., history syncer,1)  
**pid** \- Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  
**scope** \- `rwlock`, `mutex`, `processing` can be used with the process type and number (e.g., history syncer,1,processing) or all processes of type (e.g., history syncer,rwlock)  
prof_disable[=<**target** >] | Disable profiling.  
Affects all processes if target is not specified. | **process type** \- All processes of specified type (e.g., history syncer)  
See all proxy process types.  
**process type,N** \- Process type and number (e.g., history syncer,1)  
**pid** \- Process identifier (1 to 65535). For larger values specify target as 'process type,N'.  
  
Example of using runtime control to reload the proxy configuration cache:
    
    
    zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R config_cache_reload

Copy

✔ Copied

Example of using runtime control to clear the history cache for an item:
    
    
    zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R history_cache_clear=42243

Copy

✔ Copied

Examples of using runtime control to gather diagnostic information:
    
    
    # Gather all available diagnostic information in the proxy log file:
           zabbix_proxy -R diaginfo
           
           # Gather history cache statistics in the proxy log file:
           zabbix_proxy -R diaginfo=historycache

Copy

✔ Copied

Example of using runtime control to reload the SNMP cache:
    
    
    zabbix_proxy -R snmp_cache_reload

Copy

✔ Copied

When an SNMPv3 interface is updated via the Zabbix UI, Zabbix will automatically reload the new SNMPv3 credentials for that interface in most cases; use `-R snmp_cache_reload` only if polling still fails after credential changes (for example, due to engineBoots/engineID inconsistencies or non-RFC devices), or when you need to force a global SNMP cache clear for troubleshooting.

Example of using runtime control to trigger execution of housekeeper:
    
    
    zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R housekeeper_execute

Copy

✔ Copied

Examples of using runtime control to change log level:
    
    
    # Increase log level of all processes:
           zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_increase
           
           # Increase log level of second poller process:
           zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_increase=poller,2
           
           # Increase log level of process with PID 1234:
           zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_increase=1234
           
           # Decrease log level of all http poller processes:
           zabbix_proxy -c /usr/local/etc/zabbix_proxy.conf -R log_level_decrease="http poller"

Copy

✔ Copied

##### Process user

Zabbix proxy is designed to run as a non-root user. It will run as whatever non-root user it is started as. So you can run proxy as any non-root user without any issues.

If you will try to run it as 'root', it will switch to a hardcoded 'zabbix' user, which must be present on your system. You can only run proxy as 'root' if you modify the 'AllowRoot' parameter in the proxy configuration file accordingly.

##### Configuration file

See the [configuration file](/documentation/current/en/manual/appendix/config/zabbix_proxy) options for details on configuring zabbix_proxy.

#### Proxy process types and threads

  * `agent poller` \- asynchronous poller process for passive checks with a worker thread
  * `availability manager` \- process for host availability updates
  * `browser poller` \- poller for browser item checks
  * `configuration syncer` \- process for managing in-memory cache of configuration data
  * `data sender` \- proxy data sender
  * `discovery manager` \- manager process for discovery of devices
  * `discovery worker` \- process for handling discovery tasks from the discovery manager
  * `history syncer` \- history DB writer
  * `housekeeper` \- process for removal of old historical data
  * `http agent poller` \- asynchronous poller process for HTTP checks with a worker thread
  * `http poller` \- web monitoring poller
  * `icmp pinger` \- poller for icmpping checks
  * `internal poller` \- poller for internal checks
  * `ipmi manager` \- IPMI poller manager
  * `ipmi poller` \- poller for IPMI checks
  * `java poller` \- poller for Java checks
  * `odbc poller` \- poller for ODBC checks
  * `poller` \- normal poller for passive checks
  * `preprocessing manager` \- manager of preprocessing tasks with preprocessing worker threads
  * `preprocessing worker` \- thread for data preprocessing
  * `self-monitoring` \- process for collecting internal server statistics
  * `snmp poller` \- asynchronous poller process for SNMP checks with a worker thread (`walk[OID]` and `get[OID]` items only)
  * `snmp trapper` \- trapper for SNMP traps
  * `task manager` \- process for remote execution of tasks requested by other components (e.g. close problem, acknowledge problem, check item value now, remote command functionality)
  * `trapper` \- trapper for active checks, traps, proxy communication
  * `unreachable poller` \- poller for unreachable devices
  * `vmware collector` \- VMware data collector responsible for data gathering from VMware services

The proxy log file can be used to observe these process types.

Various types of Zabbix proxy processes can be monitored using the **zabbix[process, <type>,<mode>,<state>]** internal [item](/documentation/current/en/manual/config/items/itemtypes/internal).

##### History syncer transaction statistics

The history syncer process title displays detailed statistics about history syncer transactions.
    
    
    205276 ?        S      0:00  zabbix_proxy: history syncer #1 [processed 1 values in 0.001179 (0.001167,0.000000) sec, idle 1 sec]
           205277 ?        S      0:00  zabbix_proxy: history syncer #2 [processed 0 values in 0.000022 (0.000000,0.000000) sec, idle 1 sec]

Copy

✔ Copied

The timings, in "processed...in N (<timings>) sec", are:

  * Time spent writing item values into database;
  * Time spent updating item data (state, errors).

#### Supported platforms

Zabbix proxy runs on the same list of [supported platforms](/documentation/current/en/manual/concepts/server#supported-platforms) as Zabbix server.

#### Memory buffer

The memory buffer allows to store new data (item values, network discovery, host autoregistration) in the buffer and upload to Zabbix server without accessing the database. The memory buffer has been introduced for the proxy since Zabbix 7.0.

In installations before Zabbix 7.0 the collected data was stored in the database before uploading to Zabbix server. For these installations this remains the default behavior after upgrading to Zabbix 7.0.

For optimized performance, it is recommended to configure the use of memory buffer on the proxy. This is possible by modifying the value of [ProxyBufferMode](/documentation/current/en/manual/appendix/config/zabbix_proxy#proxybuffermode) from "disk" (hardcoded default for existing installations) to "hybrid" (recommended) or "memory". It is also required to set the memory buffer size ([ProxyMemoryBufferSize](/documentation/current/en/manual/appendix/config/zabbix_proxy#proxymemorybuffersize) parameter).

In hybrid mode the buffer is protected from data loss by flushing unsent data to the database if the proxy is stopped, the buffer is full or data too old. When all values have been flushed into database, the proxy goes back to using memory buffer.

In memory mode, the memory buffer will be used, however, there is no protection against data loss. If the proxy is stopped, or the memory gets overfilled, the unsent data will be dropped.

The hybrid mode (ProxyBufferMode=hybrid) is applied to all new installations since Zabbix 7.0.

Additional parameters such as [ProxyMemoryBufferSize](/documentation/current/en/manual/appendix/config/zabbix_proxy#proxymemorybuffersize) and [ProxyMemoryBufferAge](/documentation/current/en/manual/appendix/config/zabbix_proxy#proxymemorybufferage) define the memory buffer size and the maximum age of data in the buffer, respectively.

_Note_ that with conflicting configuration the proxy will print an error and fail to start, for example, if:

  * ProxyBufferMode is set to "hybrid" or "memory" and ProxyMemoryBufferSize is "0";
  * ProxyBufferMode is set to "hybrid" or "memory" and ProxyLocalBuffer is not "0".

#### Locale

Note that the proxy requires a UTF-8 locale so that some textual items can be interpreted correctly. Most modern Unix-like systems have a UTF-8 locale as default, however, there are some systems where that may need to be set specifically.

#### Calculation of queues during maintenance

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.