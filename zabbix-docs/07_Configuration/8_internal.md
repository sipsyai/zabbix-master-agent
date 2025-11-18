---
title: Internal checks
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/internal
downloaded: 2025-11-14 10:35:09
---

# 8 Internal checks

#### Overview

Internal checks allow to monitor the internal processes of Zabbix. In other words, you can monitor what goes on with Zabbix server or Zabbix proxy.

Internal checks are calculated:

  * on Zabbix server - if the host is monitored by server
  * on Zabbix proxy - if the host is monitored by proxy

Internal checks are processed by server or proxy regardless of the host maintenance status.

To use this item, choose the **Zabbix internal** item type.

Internal checks are processed by Zabbix pollers.

#### Performance

Using some internal items may negatively affect performance. These items are:

  * `zabbix[host,,items]`
  * `zabbix[host,,items_unsupported]`
  * `zabbix[hosts]`
  * `zabbix[items]`
  * `zabbix[items_unsupported]`
  * `zabbix[queue,,]`
  * `zabbix[requiredperformance]`
  * `zabbix[stats,,,queue,,]`
  * `zabbix[triggers]`

The [System information](/documentation/current/en/manual/web_interface/frontend_sections/reports/status_of_zabbix) and [Queue](/documentation/current/en/manual/web_interface/frontend_sections/administration/queue) frontend sections are also affected.

#### Supported checks

The item keys are listed without customizable parameters and additional information. Click on the item key to see the full details.

zabbix[boottime] | The startup time of Zabbix server or Zabbix proxy process in seconds.  
---|---  
zabbix[cluster,discovery,nodes] | Discovers the [high availability cluster](/documentation/current/en/manual/concepts/server/ha) nodes.  
zabbix[connector_queue] | The count of values enqueued in the connector queue.  
zabbix[discovery_queue] | The count of network checks enqueued in the discovery queue.  
zabbix[host,,items] | The number of enabled items (supported and not supported) on the host.  
zabbix[host,,items_unsupported] | The number of enabled unsupported items on the host.  
zabbix[host,,maintenance] | The current maintenance status of the host.  
zabbix[host,active_agent,available] | The availability of active agent checks on the host.  
zabbix[host,discovery,interfaces] | The details of all configured interfaces of the host in Zabbix frontend.  
zabbix[host,,available] | The availability of the main interface of a particular type of checks on the host.  
zabbix[hosts] | The number of monitored hosts.  
zabbix[items] | The number of enabled items (supported and not supported).  
zabbix[items_unsupported] | The number of unsupported items.  
zabbix[java,,] | The information about Zabbix Java gateway.  
zabbix[lld_queue] | The count of values enqueued in the low-level discovery processing queue.  
zabbix[preprocessing] | Statistics of the values received by the preprocessing manager.  
zabbix[preprocessing_queue] | The count of values enqueued in the preprocessing queue.  
zabbix[process,,,] | The percentage of time a particular Zabbix process or a group of processes (identified by <type> and <mode>) spent in <state>.  
zabbix[proxy,,] | The information about Zabbix proxy.  
zabbix[proxy,discovery] | The list of Zabbix proxies.  
zabbix[proxy group,,available] | The number of online proxies in a proxy group.  
zabbix[proxy group,,pavailable] | The percentage of online proxies in a proxy group.  
zabbix[proxy group,,proxies] | The list of Zabbix proxies in a proxy group.  
zabbix[proxy group,,state] | The state of a proxy group.  
zabbix[proxy group,discovery] | Returns a list of proxy groups with configuration data and real-time data.  
zabbix[proxy_buffer,buffer,] | Returns the proxy memory buffer usage statistics.  
zabbix[proxy_buffer,state,changes] | Returns the number of state changes between disk/memory buffer modes since start.  
zabbix[proxy_buffer,state,current] | Returns the current working state where the new data are being stored.  
zabbix[proxy_history] | The number of values in the proxy history table waiting to be sent to the server.  
zabbix[queue,,] | The number of monitored items in the queue which are delayed at least by <from> seconds, but less than <to> seconds.  
zabbix[rcache,,] | The availability statistics of the Zabbix configuration cache.  
zabbix[requiredperformance] | The required performance of Zabbix server or Zabbix proxy, in new values per second expected.  
zabbix[stats,,] | The internal metrics of a remote Zabbix server or proxy.  
zabbix[stats,,,queue,,] | The internal queue metrics of a remote Zabbix server or proxy.  
zabbix[tcache,,] | The effectiveness statistics of the Zabbix trend function cache.  
zabbix[triggers] | The number of enabled triggers in Zabbix database, with all items enabled on enabled hosts.  
zabbix[uptime] | The uptime of the Zabbix server or proxy process in seconds.  
zabbix[vcache,buffer,] | The availability statistics of the Zabbix value cache.  
zabbix[vcache,cache,] | The effectiveness statistics of the Zabbix value cache.  
zabbix[version] | The version of Zabbix server or proxy.  
zabbix[vmware,buffer,] | The availability statistics of the Zabbix vmware cache.  
zabbix[vps,written] | The total number of history values written to database.  
zabbix[wcache,,] | The statistics and availability of the Zabbix write cache.  
  
#### Item key details

  * Parameters without angle brackets are mandatory and must be used _as is_ (for example, "host" and "available" in `zabbix[host,<type>,available]`).
  * Parameters with angle brackets **<** **>** must be replaced with a valid value. If a parameter has a default value, it can be omitted.
  * Values for items and item parameters labeled "not supported on proxy" can only be retrieved if the host is monitored by server. Conversely, values "not supported on server" can only be retrieved if the host is monitored by proxy.

##### zabbix[boottime]

  
The startup time of Zabbix server or Zabbix proxy process in seconds.  
Return value: _Integer_.

##### zabbix[cluster,discovery,nodes]

  
Discovers the [high availability cluster](/documentation/current/en/manual/concepts/server/ha) nodes.  
Return value: _JSON object_.

Comments:

  * This item can be used in low-level discovery.

##### zabbix[connector_queue]

  
The count of values enqueued in the connector queue.  
Return value: _Integer_.

##### zabbix[discovery_queue]

  
The count of network checks enqueued in the discovery queue.  
Return value: _Integer_.

##### zabbix[host,,items]

  
The number of enabled items (supported and not supported) on the host.  
Return value: _Integer_.

##### zabbix[host,,items_unsupported]

  
The number of enabled unsupported items on the host.  
Return value: _Integer_.

##### zabbix[host,,maintenance]

  
The current maintenance status of the host.  
Return values: _0_ \- normal state; _1_ \- maintenance with data collection; _2_ \- maintenance without data collection.

Comments:

  * This item is always processed by Zabbix server regardless of the host location (on server or proxy). The proxy will not receive this item with configuration data.
  * The second parameter must be empty and is reserved for future use.

##### zabbix[host,active_agent,available]

  
The availability of active agent checks on the host.  
Return values: _0_ \- unknown; _1_ \- available; _2_ \- not available.

##### zabbix[host,discovery,interfaces]

  
The details of all configured interfaces of the host in Zabbix frontend.  
Return value: _JSON object_.

Comments:

  * This item can be used in [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/host_interfaces).
  * This item is not supported on Zabbix proxy.

##### zabbix[host,<type>,available]

  
The availability of the main interface of a particular type of checks on the host.  
Return values: _0_ \- not available; _1_ \- available; _2_ \- unknown.

Parameters:

  * **type** \- _agent_ , _snmp_ , _ipmi_ , or _jmx_.

Comments:

  * The item value is calculated according to the configuration parameters regarding host [unreachability/unavailability](/documentation/current/en/manual/appendix/items/unreachability).

##### zabbix[hosts]

  
The number of monitored hosts.  
Return value: _Integer_.

##### zabbix[items]

  
The number of enabled items (supported and not supported).  
Return value: _Integer_.

##### zabbix[items_unsupported]

  
The number of unsupported items.  
Return value: _Integer_.

##### zabbix[java,,<param>]

  
The information about Zabbix Java gateway.  
Return values: _1_ \- if <param> is _ping_ ; _Java gateway version_ \- if <param> is _version_ (for example: "7.4.0").

Parameters:

  * **param** \- _ping_ or _version_.

Comments:

  * This item can be used to check Java gateway availability using the `nodata()` trigger function.
  * The second parameter must be empty and is reserved for future use.

##### zabbix[lld_queue]

  
The count of values enqueued in the low-level discovery processing queue.  
Return value: _Integer_.

Comments:

  * This item can be used to monitor the low-level discovery processing queue length.

##### zabbix[preprocessing]

  
Statistics of the values received by the preprocessing manager:   
\- _queued_ \- the number and size of queued values that require preprocessing (counter)  
\- _direct_ \- the number and size of queued values that do not require preprocessing (counter)  
\- _queue_ \- the count of values enqueued in the preprocessing queue (same as `zabbix[preprocessing_queue]`)  
Return value: _JSON_.

Example of return values:
    
    
    {"data":
               {
               "queued": {
                   "count": 106,
                   "size": 58620
               },
               "direct": {
                   "count": 395,
                   "size": 33843
               },
               "queue": 0
               }
           }

Copy

✔ Copied

##### zabbix[preprocessing_queue]

  
The count of values enqueued in the preprocessing queue.  
Return value: _Integer_.

Comments:

  * This item can be used to monitor the preprocessing queue length.

##### zabbix[process,<type>,<mode>,<state>]

  
The percentage of time a particular Zabbix process or a group of processes (identified by <type> and <mode>) spent in <state>. It is calculated for the last minute only.  
Return value: _Float_.

Parameters:

  * **type** \- for [server processes](/documentation/current/en/manual/concepts/server#server-process-types-and-threads): _agent poller_ , _alert manager_ , _alert syncer_ , _alerter_ , _availability manager_ , _browser poller_ , _configuration syncer_ , _configuration syncer worker_ , _connector manager_ , _connector worker_ , _discovery manager_ , _discovery worker_ , _escalator_ , _ha manager_ , _history poller_ , _history syncer_ , _housekeeper_ , _http agent poller_ , _http poller_ , _icmp pinger_ , _internal poller_ _ipmi manager_ , _ipmi poller_ , _java poller_ , _lld manager_ , _lld worker_ , _odbc poller_ , _poller_ , _preprocessing manager_ , _preprocessing worker_ , _proxy group manager_ , _proxy poller_ , _self-monitoring_ , _service manager_ , _snmp poller_ , _snmp trapper_ , _task manager_ , _timer_ , _trapper_ , _trigger housekeeper_ , _unreachable poller_ , _vmware collector_ ;  
for [proxy processes](/documentation/current/en/manual/concepts/proxy#proxy-process-types-and-threads): _agent poller_ , _availability manager_ , _browser poller_ , _configuration syncer_ , _data sender_ , _discovery manager_ , _discovery worker_ , _history syncer_ , _housekeeper_ , _http agent poller_ , _http poller_ , _icmp pinger_ , _internal poller_ _ipmi manager_ , _ipmi poller_ , _java poller_ , _odbc poller_ , _poller_ , _preprocessing manager_ , _preprocessing worker_ , _self-monitoring_ , _snmp poller_ , _snmp trapper_ , _task manager_ , _trapper_ , _unreachable poller_ , _vmware collector_ ;
  * **mode** \- _avg_ \- average value for all processes of a given type (default);  
_count_ \- returns number of forks for a given process type, <state> should not be specified;  
_max_ \- maximum value;  
_min_ \- minimum value;  
_< process number>_ \- process number (between 1 and the number of pre-forked instances; for example, if 4 trappers are running, the value is between 1 and 4);
  * **state** \- _busy_ \- process is in busy state, for example, the processing request (default);  
_idle_ \- process is in idle state doing nothing.

Comments:

  * If <mode> is a Zabbix process number that is not running (for example, with 5 pollers running the <mode> is specified to be 6), such an item will turn unsupported.
  * Minimum and maximum refers to the usage percentage for a single process. So if in a group of 3 pollers usage percentages per process were 2, 18 and 66, min would return 2 and max would return 66.
  * Processes report what they are doing in shared memory and the self-monitoring process summarizes that data each second. State changes (busy/idle) are registered upon change - thus a process that becomes busy registers as such and doesn't change or update the state until it becomes idle. This ensures that even fully hung processes will be correctly registered as 100% busy.
  * Currently, "busy" means "not sleeping", but in the future additional states might be introduced - waiting for locks, performing database queries, etc. Note that asynchronous pollers are considered busy if they have reached the limit set by the MaxConcurrentChecksPerPoller [server](/documentation/current/en/manual/appendix/config/zabbix_server#maxconcurrentchecksperpoller)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#maxconcurrentchecksperpoller) configuration parameter.
  * On Linux and most other systems, resolution is 1/100 of a second.

Examples:
    
    
    zabbix[process,poller,avg,busy] #the average time of poller processes spent doing something during the last minute
           zabbix[process,"icmp pinger",max,busy] #the maximum time spent doing something by any ICMP pinger process during the last minute
           zabbix[process,"history syncer",2,busy] #the time spent doing something by history syncer number 2 during the last minute
           zabbix[process,trapper,count] #the amount of currently running trapper processes

Copy

✔ Copied

##### zabbix[proxy,<name>,<param>]

  
The information about Zabbix proxy.  
Return value: _Integer_.

Parameters:

  * **name** \- the proxy name;
  * **param** \- _lastaccess_ \- the timestamp of the last heartbeat message received from proxy;  
_delay_ \- how long the collected values are unsent; calculated as "proxy delay" + ("current server time" - "proxy lastaccess"), where "proxy delay" is the difference between the current proxy time and the timestamp of the oldest unsent value on proxy.

Comments:

  * This item is always processed by Zabbix server regardless of host location (on server or proxy).
  * The [`fuzzytime()`](/documentation/current/en/manual/appendix/functions/history#fuzzytime) function can be used to check the availability of proxy.

Example:
    
    
    zabbix[proxy,"Germany",lastaccess] #the timestamp of the last heartbeat message received from "Germany" proxy

Copy

✔ Copied

##### zabbix[proxy,discovery]

  
The list of Zabbix proxies with name, mode, encryption, compression, version, last seen, host count, item count, required values per second (vps), version status (current/outdated/unsupported), timeouts by item type, proxy group name (if proxy belongs to group), state (unknown/offline/online).  
Return value: _JSON object_.

##### zabbix[proxy group,<name>,available]

  
The number of online proxies in a proxy group.  
Return value: _Integer_.

Parameters:

  * **name** \- the proxy group name.

##### zabbix[proxy group,<name>,pavailable]

  
The percentage of online proxies in a proxy group.  
Return value: _Float_.

Parameters:

  * **name** \- the proxy group name.

##### zabbix[proxy group,<name>,proxies]

  
The list of Zabbix proxies in a proxy group with name, mode, encryption, compression, version, last seen, host count, item count, required values per second (vps), version status (current/outdated/unsupported), timeouts, proxy group name, state (unknown/offline/online).  
Return value: _JSON_.

Parameters:

  * **name** \- the proxy group name.

##### zabbix[proxy group,<name>,state]

  
The state of a proxy group.  
Return value: _0_ \- unknown; _1_ \- offline; _2_ \- recovering; _3_ \- online; _4_ \- degrading.

Parameters:

  * **name** \- the proxy group name.

##### zabbix[proxy group,discovery]

  
Returns a list of proxy groups with configuration data and real-time data. Configuration data include the proxy group name, failover delay, and the minimum number of online proxies required. Real-time data include the proxy group state (see comments for details), the number of online proxies, and the percentage of online proxies.  
Return value: _JSON_.

Comments:

  * This item does not return groupless proxies.
  * If there is an invalid value for "failover_delay" or "min_online", then a special value _-1_ is reported to indicate that. Invalid values might occur if macros are used for configuration and the macros cannot be expanded to a valid value.
  * The proxy group state is reported as an integer: _0_ \- unknown; _1_ \- offline; _2_ \- recovering; _3_ \- online; _4_ \- degrading.

Example of return values:
    
    
    {
               "groups": [
                  { "name": "Riga", "failover_delay": 60, "min_online": 1 },
                  { "name": "Tokyo", "failover_delay": 60, "min_online": 2 },
                  { "name": "Porto Alegre", "failover_delay": 60, "min_online": 3 }
               ],
               "details": {
                   "Riga": { "state": 3, "available": 10, "pavailable": 20 },
                   "Tokyo": { "state": 3, "available": 10, "pavailable": 20 },
                   "Porto Alegre": { "state": 1, "available": 0, "pavailable": 0 }
               }
           }

Copy

✔ Copied

##### zabbix[proxy_buffer,buffer,<mode>]

  
The proxy memory buffer usage statistics.  
Return values: _Integer_ (for size); _Float_ (for percentage).

Parameters:

  * **mode** : _total_ \- the total size of buffer (can be used to check if memory buffer is enabled);  
_free_ \- the size of free buffer;  
_pfree_ \- the percentage of free buffer;  
_used_ \- the size of used buffer;  
_pused_ \- the percentage of used buffer.

Comments:

  * Returns a 'Proxy memory buffer is disabled' error when the memory buffer is disabled;  

  * This item is not supported on Zabbix server.

##### zabbix[proxy_buffer,state,changes]

  
Returns the number of state changes between disk/memory buffer modes since start.  
Return values: _Integer_ ; _0_ \- the memory buffer is disabled.

Comments:

  * Frequent state changes indicate that either the memory buffer size or age must be increased.
  * If the memory buffer state is monitored infrequently (for example, once a minute) then the buffer might flip its state without it being registered.

##### zabbix[proxy_buffer,state,current]

  
Returns the current working state where the new data are being stored.  
Return values: _0_ \- disk; _1_ \- memory.

Comments:

  * "0" is also returned when the memory buffer is disabled.

##### zabbix[proxy_history]

  
The number of values in the proxy history table waiting to be sent to the server.  
Return values: _Integer_.

Comments:

  * This item is not supported on Zabbix server.

##### zabbix[queue,<from>,<to>]

  
The number of monitored items in the queue which are delayed at least by <from> seconds, but less than <to> seconds.  
Return value: _Integer_.

Parameters:

  * **from** \- delayed by at least (default is 6 seconds);
  * **to** \- delayed by at most (default is infinity).

Comments:

  * [Time suffixes](/documentation/current/en/manual/appendix/suffixes) (s,m,h,d,w) are supported in the parameters.

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.

##### zabbix[rcache,<cache>,<mode>]

  
The availability statistics of the Zabbix configuration cache.  
Return values: _Integer_ (for size); _Float_ (for percentage).

Parameters:

  * **cache** \- _buffer_ ;
  * **mode** \- _total_ \- the total size of buffer;  
_free_ \- the size of free buffer;  
_pfree_ \- the percentage of free buffer;  
_used_ \- the size of used buffer;  
_pused_ \- the percentage of used buffer.

##### zabbix[requiredperformance]

  
The required performance of Zabbix server or Zabbix proxy, in new values per second expected.  
Return value: _Float_.

Comments:

  * Approximately correlates with "Required server performance, new values per second" in _Reports →[System information](/documentation/current/en/manual/web_interface/frontend_sections/reports/status_of_zabbix)_.

##### zabbix[stats,<ip>,<port>]

  
The internal metrics of a remote Zabbix server or proxy.  
Return values: _JSON object_.

Parameters:

  * **ip** \- the IP/DNS/network mask list of servers/proxies to be remotely queried (default is 127.0.0.1);
  * **port** \- the port of server/proxy to be remotely queried (default is 10051).

Comments:

  * The stats request will only be accepted from the addresses listed in the 'StatsAllowedIP' [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) parameter on the target instance.
  * A selected set of internal metrics is returned by this item. For details, see [Remote monitoring of Zabbix stats](/documentation/current/en/manual/appendix/items/remote_stats#exposed-metrics).

##### zabbix[stats,<ip>,<port>,queue,<from>,<to>]

  
The internal queue metrics (see `zabbix[queue,<from>,<to>]`) of a remote Zabbix server or proxy.  
Return values: _JSON object_.

Parameters:

  * **ip** \- the IP/DNS/network mask list of servers/proxies to be remotely queried (default is 127.0.0.1);
  * **port** \- the port of server/proxy to be remotely queried (default is 10051);
  * **from** \- delayed by at least (default is 6 seconds);
  * **to** \- delayed by at most (default is infinity).

Comments:

  * The stats request will only be accepted from the addresses listed in the 'StatsAllowedIP' [server](/documentation/current/en/manual/appendix/config/zabbix_server)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) parameter on the target instance.
  * A selected set of internal metrics is returned by this item. For details, see [Remote monitoring of Zabbix stats](/documentation/current/en/manual/appendix/items/remote_stats#exposed-metrics).

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.

##### zabbix[tcache,<cache>,<parameter>]

  
The effectiveness statistics of the Zabbix trend function cache.  
Return values: _Integer_ (for size); _Float_ (for percentage).

Parameters:

  * **cache** \- _buffer_ ;
  * **parameter** \- _all_ \- total cache requests (default);  
_hits_ \- cache hits;  
_phits_ \- percentage of cache hits;  
_misses_ \- cache misses;  
_pmisses_ \- percentage of cache misses;  
_items_ \- the number of cached items;  
_requests_ \- the number of cached requests;  
_pitems_ \- percentage of cached items from cached items + requests. Low percentage most likely means that the cache size can be reduced.

Comments:

  * This item is not supported on Zabbix proxy.

##### zabbix[triggers]

  
The number of enabled triggers in Zabbix database, with all items enabled on enabled hosts.  
Return value: _Integer_.

Comments:

  * This item is not supported on Zabbix proxy.

##### zabbix[uptime]

  
The uptime of the Zabbix server or proxy process in seconds.  
Return value: _Integer_.

##### zabbix[vcache,buffer,<mode>]

  
The availability statistics of the Zabbix value cache.  
Return values: _Integer_ (for size); _Float_ (for percentage).

Parameters:

  * **mode** \- _total_ \- the total size of buffer;  
_free_ \- the size of free buffer;  
_pfree_ \- the percentage of free buffer;  
_used_ \- the size of used buffer;  
_pused_ \- the percentage of used buffer.

Comments:

  * This item is not supported on Zabbix proxy.

##### zabbix[vcache,cache,<parameter>]

  
The effectiveness statistics of the Zabbix value cache.  
Return values: _Integer_. With the _mode_ parameter returns: 0 - normal mode; 1 - low memory mode.

Parameters:

  * **parameter** \- _requests_ \- the total number of requests;  
_hits_ \- the number of cache hits (history values taken from the cache);  
_misses_ \- the number of cache misses (history values taken from the database);  
_mode_ \- the value cache operating mode.

Comments:

  * Once the low-memory mode has been switched on, the value cache will remain in this state for 24 hours, even if the problem that triggered this mode is resolved sooner.
  * You may use this key with the _Change per second_ preprocessing step in order to get values-per-second statistics.
  * This item is not supported on Zabbix proxy.

##### zabbix[version]

  
The version of Zabbix server or proxy.  
Return value: _String_. For example: `7.4.0`.

##### zabbix[vmware,buffer,<mode>]

  
The availability statistics of the Zabbix vmware cache.  
Return values: _Integer_ (for size); _Float_ (for percentage).

Parameters:

  * **mode** \- _total_ \- the total size of buffer;  
_free_ \- the size of free buffer;  
_pfree_ \- the percentage of free buffer;  
_used_ \- the size of used buffer;  
_pused_ \- the percentage of used buffer.

##### zabbix[vps,written]

  
The total number of history values written to database.  
Return value: _Integer_.

##### zabbix[wcache,<cache>,<mode>]

  
The statistics and availability of the Zabbix write cache.  
Return values: _Integer_ (for number/size); _Float_ (for percentage).

Parameters:

  * **cache** \- _values_ , _history_ , _index_ , or _trend_ ;
  * **mode** \- (with _values_) _all_ (default) - the total number of values processed by Zabbix server/proxy, except unsupported items (counter);  
_float_ \- the number of processed float values (counter);  
_uint_ \- the number of processed unsigned integer values (counter);  
_str_ \- the number of processed character/string values (counter);  
_log_ \- the number of processed log values (counter);  
_text_ \- the number of processed text values (counter);  
_not supported_ \- the number of times item processing resulted in item becoming unsupported or keeping that state (counter);  
(with _history_ , _index_ , _trend_ cache) _pfree_ (default) - the percentage of free buffer;  
_total_ \- the total size of buffer;  
_free_ \- the size of free buffer;  
_used_ \- the size of used buffer;  
_pused_ \- the percentage of used buffer.

Comments:

  * Specifying <cache> is mandatory. The `trend` cache parameter is not supported with Zabbix proxy.
  * The history cache is used to store item values. A low number indicates performance problems on the database side.
  * The history index cache is used to index the values stored in the history cache.
  * After the history cache is filled and then cleared, the history index cache will still keep some data. This behavior is expected and helps the system run more efficiently by avoiding the extra processing required to constantly resize the memory.
  * The trend cache stores the aggregate for the current hour for all items that receive data.
  * You may use the zabbix[wcache,values] key with the _Change per second_ preprocessing step in order to get values-per-second statistics.