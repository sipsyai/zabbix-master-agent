---
title: built-in plugins
source: https://www.zabbix.com/documentation/current/en/manual/extensions/plugins#built-in
downloaded: 2025-11-14 10:46:23
---

# 2 Plugins

#### Overview

Plugins provide an option to extend the monitoring capabilities of Zabbix. Plugins are written in Go programming language and are supported by Zabbix agent 2 only. Plugins provide an alternative to [loadable modules](/documentation/current/en/manual/extensions/loadablemodules) (written in C), and [other methods](/documentation/current/en/manual/extensions) for extending Zabbix functionality.

The following features are specific to agent 2 and its plugins:

  * support of scheduled and flexible intervals for both passive and active checks
  * task queue management with respect to schedule and task concurrency
  * plugin-level timeouts
  * compatibility check of Zabbix agent 2 and its plugins on start up

Since Zabbix 6.0, plugins don't have to be integrated into the agent 2 directly and can be added as loadable plugins, thus making the creation process of additional plugins for gathering new monitoring metrics easier.

This page lists Zabbix native and loadable plugins, and describes plugin configuration principles from the user perspective.

For instructions on writing your own plugins, see [Developer center](/documentation/current/en/devel/plugins) and [Example plugin for Zabbix agent 2](https://git.zabbix.com/projects/AP/repos/example/browse).  
  
For details on the communication process between Zabbix agent 2 and a loadable plugin as well as the metric collection process, see [Connection diagram](/documentation/current/en/devel/plugins#connection-diagram).

#### Configuring plugins

This section provides common plugin configuration principles and best practices.

All plugins are configured using _Plugins.*_ parameter, which can either be part of the Zabbix agent 2 [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2) or a plugin's own [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins). If a plugin uses a separate configuration file, path to this file should be specified in the Include parameter of Zabbix agent 2 configuration file.

A typical plugin parameter has the following structure:

_Plugins. <PluginName>.<Parameter>=<Value>_

Additionally, there are two specific groups of parameters:

  * _Plugins. <PluginName>.Default.<Parameter>=<Value>_ used for defining default parameter values.

  * _Plugins. <PluginName>.<SessionName>.<Parameter>=<Value>_ used for defining separate sets of parameters for different monitoring targets via named sessions.

All parameter names should adhere to the following requirements:

  * it is recommended to capitalize the names of your plugins
  * the parameter should be capitalized
  * special characters are not allowed
  * nesting isn't limited by a maximum level
  * the number of parameters is not limited

For example, to perform [active checks](/documentation/current/en/manual/concepts/agent2#passive-and-active-checks) that do not have _Scheduling_ [update interval](/documentation/current/en/manual/config/items/item/custom_intervals#scheduling-intervals) immediately after the agent restart only for the Uptime plugin, set `Plugins.Uptime.System.ForceActiveChecksOnStart=1` in the [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2). Similarly, to set custom limit for [concurrent checks](/documentation/current/en/manual/concepts/agent2#check-concurrency) for the CPU plugin, set the `Plugins.CPU.System.Capacity=N` in the [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2).

##### Default values

You can set default values for the connection-related parameters (URI, username, password, etc.) in the configuration file in the format:
    
    
    Plugins.<PluginName>.Default.<Parameter>=<Value>

Copy

✔ Copied

For example, `Plugins.Mysql.Default.Username=zabbix`, `Plugins.MongoDB.Default.Uri=tcp://127.0.0.1:27017`, etc.

If a value for such parameter is not provided in an item key or in the named session parameters, the plugin will use the default value. If a default parameter is also undefined, hardcoded defaults will be used.

If an item key does not have any parameters, Zabbix agent 2 will attempt to collect the metric using values defined in the default parameters section.

##### Named sessions

Named sessions represent an additional level of plugin parameters and can be used to specify separate sets of authentication parameters for each of the instances being monitored. Each named session parameter should have the following structure:
    
    
    Plugins.<PluginName>.Sessions.<SessionName>.<Parameter>=<Value>

Copy

✔ Copied

A session name can be used as a connString item key parameter instead of specifying a URI, username, and/or password separately.

In item keys, the first parameter can be either a connString or a URI. If the first key parameter doesn't match any session name, it will be treated as a URI. Note that passing embedded URI credentials in the item key is not supported, use named session parameters instead.

The list of available [named session parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins) depends on the plugin.

It is possible to override session parameters by specifying new values in the item key parameters (see example).

If a parameter is not defined for the named session, Zabbix agent 2 will use the value defined in the default plugin parameter.

##### Parameter priority

Zabbix agent 2 plugins search for connection-related parameter values in the following order:

![](/documentation/current/assets/en/diagrams/agent2_parameters.png)

  1. The first item key parameter is compared to session names. If no match is found, it is treated as an actual value; in this case, step 3 will be skipped. If a match is found, the parameter value (usually, a URI) must be defined in the named session.
  2. Other parameters will be taken from the item key if defined.
  3. If an item key parameter (for example, password) is empty, plugin will look for the corresponding named session parameter.
  4. If the session parameter is also not specified, the value defined in the corresponding default parameter will be used.
  5. If all else fails, the plugin will use the hardcoded default value.

##### Example 1

Monitoring of two instances “MySQL1” and “MySQL2”.

Configuration parameters:
    
    
    Plugins.Mysql.Sessions.MySQL1.Uri=tcp://127.0.0.1:3306
           Plugins.Mysql.Sessions.MySQL1.User=mysql1_user
           Plugins.Mysql.Sessions.MySQL1.Password=unique_password
           Plugins.Mysql.Sessions.MySQL2.Uri=tcp://192.0.2.0:3306
           Plugins.Mysql.Sessions.MySQL2.User=mysql2_user
           Plugins.Mysql.Sessions.MySQL2.Password=different_password

Copy

✔ Copied

As a result of this configuration, each session name may be used as a connString in an [item key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2), e.g., `mysql.ping[MySQL1]` or `mysql.ping[MySQL2]`.

##### Example 2

Providing some of the parameters in the item key.

Configuration parameters:
    
    
    Plugins.PostgreSQL.Sessions.Session1.Uri=tcp://192.0.2.234:5432
           Plugins.PostgreSQL.Sessions.Session1.User=old_username
           Plugins.PostgreSQL.Sessions.Session1.Password=session_password

Copy

✔ Copied

[Item key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2): `pgsql.ping[session1,new_username,,postgres]`

As a result of this configuration, the agent will connect to PostgreSQL using the following parameters:

  * URI from session parameter: `192.0.2.234:5432`
  * Username from the item key: `new_username`
  * Password from session parameter (since it is omitted in the item key): `session_password`
  * Database name from the item key: `postgres`

##### Example 3

Collecting a metric using default configuration parameters.

Configuration parameters:
    
    
    Plugins.PostgreSQL.Default.Uri=tcp://192.0.2.234:5432
           Plugins.PostgreSQL.Default.User=zabbix
           Plugins.PostgreSQL.Default.Password=password

Copy

✔ Copied

[Item key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2): `pgsql.ping[,,,postgres]`

As a result of this configuration, the agent will connect to PostgreSQL using the parameters:

  * Default URI: `192.0.2.234:5432`
  * Default username: `zabbix`
  * Default password: `password`
  * Database name from the item key: `postgres`

##### Connections

Some plugins support gathering metrics from multiple instances simultaneously. Both local and remote instances can be monitored. TCP and Unix-socket connections are supported.

It is recommended to configure plugins to keep connections to instances in an open state. The benefits are reduced network congestion, latency, and CPU and memory usage due to the lower number of connections. The client library takes care of this.

Time period for which unused connections should remain open can be determined by _Plugins. <PluginName>.KeepAlive_ parameter. Example: _Plugins.Memcached.KeepAlive_

#### Plugins

All metrics supported by Zabbix agent 2 are collected by plugins.

##### Built-in

The following plugins for Zabbix agent 2 are available out-of-the-box. Click on the plugin name to go to the plugin repository with additional information.

Agent | Metrics of the Zabbix agent being used. | agent.hostname, agent.ping, agent.version | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
---|---|---|---  
[Ceph](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/ceph/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Ceph monitoring. | ceph.df.details, ceph.osd.stats, ceph.osd.discovery, ceph.osd.dump,  
ceph.ping, ceph.pool.discovery, ceph.status |   
[CPU](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/system/cpu?at=refs%2Fheads%2Frelease%2F7.4) | System CPU monitoring (number of CPUs/CPU cores, discovered CPUs, utilization percentage). | system.cpu.discovery, system.cpu.num, system.cpu.util | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Docker](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/docker?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of Docker containers. | docker.container_info, docker.container_stats, docker.containers, docker.containers.discovery,  
docker.data_usage, docker.images, docker.images.discovery, docker.info, docker.ping | See also:  
[Configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/d_plugin)  
File | File metrics collection. | vfs.file.cksum, vfs.file.contents, vfs.file.exists, vfs.file.md5sum,  
vfs.file.regexp, vfs.file.regmatch, vfs.file.size, vfs.file.time | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Kernel](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/kernel?at=refs%2Fheads%2Frelease%2F7.4) | Kernel monitoring. | kernel.maxfiles, kernel.maxproc | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Log](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/log?at=refs%2Fheads%2Frelease%2F7.4) | Log file monitoring. | log, log.count, logrt, logrt.count | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
  
See also:  
Plugin configuration parameters ([Unix](/documentation/current/en/manual/appendix/config/zabbix_agent2)/[Windows](/documentation/current/en/manual/appendix/config/zabbix_agent2_win))  
[Memcached](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/memcached/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Memcached server monitoring. | memcached.ping, memcached.stats |   
[Modbus](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/modbus/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Reads Modbus data. | modbus.get | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[MQTT](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/mqtt/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Receives published values of MQTT topics. | mqtt.get | To configure an encrypted connection to the MQTT broker, specify TLS parameters in the agent configuration file as a named session or default parameters. Currently TLS parameters cannot be passed as item key parameters.  
[MySQL](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/mysql/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of MySQL and its forks. | mysql.custom.query, mysql.db.discovery, mysql.db.size, mysql.get_status_variables,  
mysql.ping, mysql.replication.discovery, mysql.replication.get_slave_status, mysql.version | To configure an encrypted connection to the database, specify TLS parameters in the agent configuration file as a named session or default parameters. Currently TLS parameters cannot be passed as item key parameters.  
[NetIf](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/net/netif?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of network interfaces. | net.if.collisions, net.if.discovery, net.if.in, net.if.out, net.if.total | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Oracle](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/oracle/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Oracle Database monitoring. | oracle.diskgroups.stats, oracle.diskgroups.discovery, oracle.archive.info, oracle.archive.discovery,  
oracle.cdb.info, oracle.custom.query, oracle.datafiles.stats, oracle.db.discovery,  
oracle.fra.stats, oracle.instance.info, oracle.pdb.info, oracle.pdb.discovery,  
oracle.pga.stats, oracle.ping, oracle.proc.stats, oracle.redolog.info,  
oracle.sga.stats, oracle.sessions.stats, oracle.sys.metrics, oracle.sys.params,  
oracle.ts.stats, oracle.ts.discovery, oracle.user.info, oracle.version | Install the [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client/downloads.html) before using the plugin.  
[Proc](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/proc?at=refs%2Fheads%2Frelease%2F7.4) | Process CPU utilization percentage. | proc.cpu.util | Supported key has the same parameters as Zabbix agent [key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Redis](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/redis/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Redis server monitoring. | redis.config, redis.info, redis.ping, redis.slowlog.count | To configure an encrypted connection to Redis, specify TLS parameters in the agent configuration file as a named session or default parameters. TLS parameters cannot be passed as item key parameters. Note that an incorrect or otherwise invalid TLS configuration can prevent Zabbix agent 2 from starting, so verify certificate files, permissions and paths before enabling TLS.  
[Smart](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/smart?at=refs%2Fheads%2Frelease%2F7.4) | S.M.A.R.T. monitoring. | smart.attribute.discovery, smart.disk.discovery, smart.disk.get | The minimum required smartctl version is 7.1.   
Sudo/root access rights to smartctl are required for the user executing Zabbix agent 2. The plugin uses only the following commands:   
`/usr/sbin/smartctl -a *`  
`/usr/sbin/smartctl --scan *`   
`/usr/sbin/smartctl -j -V`   
  
Supported [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) can be used with Zabbix agent 2 only on Linux/Windows, both as a passive and active check.  
See also:  
[Configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/smart_plugin)  
[SW](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/system/sw?at=refs%2Fheads%2Frelease%2F7.4) | Listing of installed packages. | system.sw.packages, system.sw.packages.get | The supported keys have the same parameters as Zabbix agent [key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Swap](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/system/swap?at=refs%2Fheads%2Frelease%2F7.4) | Swap space size in bytes/percentage. | system.swap.size | Supported key has the same parameters as Zabbix agent [key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
SystemRun | Runs specified command. | system.run | Supported key has the same parameters as Zabbix agent [key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
  
See also:  
Plugin configuration parameters ([Unix](/documentation/current/en/manual/appendix/config/zabbix_agent2)/[Windows](/documentation/current/en/manual/appendix/config/zabbix_agent2_win))  
Systemd | Monitoring of systemd services. | systemd.unit.discovery, systemd.unit.get, systemd.unit.info |   
[TCP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/net/tcp?at=refs%2Fheads%2Frelease%2F7.4) | TCP connection availability check. | net.tcp.port | Supported key has the same parameters as Zabbix agent [key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[UDP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/net/udp?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of the UDP services availability and performance. | net.udp.service, net.udp.service.perf | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Uname](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/system/uname?at=refs%2Fheads%2Frelease%2F7.4) | Retrieval of information about the system. | system.hostname, system.sw.arch, system.uname | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[Uptime](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/system/uptime?at=refs%2Fheads%2Frelease%2F7.4) | System uptime metrics collection. | system.uptime | Supported key has the same parameters as Zabbix agent [key](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[VFSDev](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/vfs/dev?at=refs%2Fheads%2Frelease%2F7.4) | VFS metrics collection. | vfs.dev.discovery, vfs.dev.read, vfs.dev.write | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[WebCertificate](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/web/certificate?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of TLS/SSL website certificates. | web.certificate.get |   
[WebPage](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/web/page?at=refs%2Fheads%2Frelease%2F7.4) | Web page monitoring. | web.page.get, web.page.perf, web.page.regexp | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[ZabbixAsync](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/zabbix/async?at=refs%2Fheads%2Frelease%2F7.4) | Asynchronous metrics collection. | net.tcp.listen, net.udp.listen, sensor, system.boottime, system.cpu.intr, system.cpu.load,  
system.cpu.switches, system.hw.cpu, system.hw.macaddr, system.localtime, system.sw.os,  
system.swap.in, system.swap.out, vfs.fs.discovery | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[ZabbixStats](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/zabbix/stats?at=refs%2Fheads%2Frelease%2F7.4) | Zabbix server/proxy internal metrics or number of delayed items in a queue. | zabbix.stats | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
[ZabbixSync](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/zabbix/sync?at=refs%2Fheads%2Frelease%2F7.4) | Synchronous metrics collection. | net.dns, net.dns.record, net.tcp.service, net.tcp.service.perf, proc.mem,  
proc.num, system.hw.chassis, system.hw.devices, system.sw.packages,  
system.users.num, vfs.dir.count, vfs.dir.size, vfs.fs.get, vfs.fs.inode,  
vfs.fs.size, vm.memory.size. | Supported keys have the same parameters as Zabbix agent [keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent).  
  
##### Loadable

Loadable plugins for Zabbix agent 2 are not available out-of-the-box and need to be installed separately:

  * For Linux, you may use [packages](https://www.zabbix.com/download?zabbix=7.4&components=agent_2) or [build plugins](/documentation/current/en/manual/extensions/plugins/build).
  * For Windows, you may [install from MSI](/documentation/current/en/manual/installation/install_from_packages/win_msi#zabbix-agent-2-loadable-plugins) or [build plugins](/documentation/current/en/manual/installation/install/building_zabbix_agent_2_on_windows#compiling-zabbix-agent-2-loadable-plugins).

Click on the plugin name to go to the plugin repository with additional information.

[Ember+](https://git.zabbix.com/projects/AP/repos/ember-plus/browse?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of Ember+. | ember.get | Currently only available to be built from the source (for both Unix and Windows).  
  
See also [Ember+ plugin configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/ember_plus_plugin#parameters).  
---|---|---|---  
[MongoDB](https://git.zabbix.com/projects/AP/repos/mongodb/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of MongoDB servers and clusters (document-based, distributed database). | mongodb.collection.stats, mongodb.collections.discovery, mongodb.collections.usage, mongodb.connpool.stats,  
mongodb.db.stats, mongodb.db.discovery, mongodb.jumbo_chunks.count, mongodb.oplog.stats,  
mongodb.ping, mongodb.rs.config, mongodb.rs.status, mongodb.server.status,  
mongodb.sh.discovery, mongodb.version | To configure encrypted connections to the database, specify the TLS parameters in the agent configuration file as anamed session parameters.  
Currently, TLS parameters cannot be passed as item key parameters.  
  
See also [MongoDB plugin configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mongodb_plugin#parameters).  
[MSSQL](https://git.zabbix.com/projects/AP/repos/mssql/browse?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of MSSQL database. | mssql.availability.group.get, mssql.custom.query, mssql.db.get, mssql.job.status.get, mssql.last.backup.get, mssql.local.db.get, mssql.mirroring.get, mssql.nonlocal.db.get, mssql.perfcounter.get, mssql.ping, mssql.quorum.get, mssql.quorum.member.get, mssql.replica.get, mssql.version | To configure encrypted connection to the database, specify the TLS parameters in the agent configuration file as a named session or default parameters. Currently, TLS parameters cannot be passed as item key parameters.  
  
See also [MSSQL plugin configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mssql_plugin#parameters).  
[NVIDIA GPU](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of NVIDIA GPU. | nvml.device.count, nvml.device.decoder.utilization, nvml.device.ecc.mode, nvml.device.encoder.stats.get, nvml.device.encoder.utilization, nvml.device.energy.consumption, nvml.device.errors.memory, nvml.device.errors.register, nvml.device.fan.speed.avg, nvml.device.get, nvml.device.graphics.frequency, nvml.device.memory.bar1.get, nvml.device.memory.fb.get, nvml.device.memory.frequency, nvml.device.pci.utilization, nvml.device.performance.state, nvml.device.power.limit, nvml.device.power.usage, nvml.device.serial, nvml.device.sm.frequency, nvml.device.temperature, nvml.device.utilization, nvml.device.video.frequency, nvml.system.driver.version, nvml.version | See also [NVIDIA GPU plugin configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/nvidia_gpu#parameters).  
[PostgreSQL](https://git.zabbix.com/projects/AP/repos/postgresql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) | Monitoring of PostgreSQL and its forks. | pgsql.autovacuum.count, pgsql.archive, pgsql.bgwriter, pgsql.cache.hit, pgsql.connections,  
pgsql.custom.query, pgsql.dbstat, pgsql.dbstat.sum, pgsql.db.age, pgsql.db.bloating_tables,   
pgsql.db.discovery, pgsql.db.size, pgsql.locks, pgsql.oldest.xid, pgsql.ping, pgsql.queries,   
pgsql.replication.count, pgsql.replication.process, pgsql.replication.process.discovery, pgsql.replication.recovery_role, pgsql.replication.status,   
pgsql.replication_lag.b, pgsql.replication_lag.sec, pgsql.uptime, pgsql.version, pgsql.wal.stat | To configure encrypted connections to the database, specify the TLS parameters in the agent configuration file as a named session or default parameters.  
Currently, TLS parameters cannot be passed as item key parameters.  
  
See also [PostgreSQL plugin configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/postgresql_plugin#parameters).  
  
Loadable plugins, when launched with:  
\- `-V --version` \- print plugin version and license information;  
\- `-h --help` \- print help information.