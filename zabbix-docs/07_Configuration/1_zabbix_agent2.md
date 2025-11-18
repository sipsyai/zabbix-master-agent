---
title: Zabbix agent 2
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2
downloaded: 2025-11-14 10:34:56
---

# 1 Zabbix agent 2

Zabbix agent 2 supports all item keys supported for Zabbix agent on [Unix](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) and [Windows](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/win_keys). This page provides details on the additional item keys, which you can use with Zabbix agent 2 only, grouped by the plugin they belong to.

The item keys are listed without parameters and additional information. Click on the item key to see the full details.

ceph.df.details | The cluster's data usage and distribution among pools. | Ceph  
---|---|---  
ceph.osd.stats | Aggregated and per OSD statistics.  
ceph.osd.discovery | The list of discovered OSDs.  
ceph.osd.dump | The usage thresholds and statuses of OSDs.  
ceph.ping | Tests whether a connection to Ceph can be established.  
ceph.pool.discovery | The list of discovered pools.  
ceph.status | The overall cluster's status.  
docker.container_info | Low-level information about a container. | Docker  
docker.container_stats | The container resource usage statistics.  
docker.containers | Returns the list of containers.  
docker.containers.discovery | Returns the list of containers. Used for low-level discovery.  
docker.data.usage | Information about the current data usage.  
docker.images | Returns the list of images.  
docker.images.discovery | Returns the list of images. Used for low-level discovery.  
docker.info | The system information.  
docker.ping | Test if the Docker daemon is alive or not.  
ember.get | Returns the result of the required device. | Ember+  
memcached.ping | Test if a connection is alive or not. | Memcached  
memcached.stats | Gets the output of the STATS command.  
mongodb.collection.stats | Returns a variety of storage statistics for a given collection. | MongoDB  
mongodb.collections.discovery | Returns a list of discovered collections.  
mongodb.collections.usage | Returns the usage statistics for collections.  
mongodb.connpool.stats | Returns information regarding the open outgoing connections from the current database instance to other members of the sharded cluster or replica set.  
mongodb.db.stats | Returns the statistics reflecting a given database system state.  
mongodb.db.discovery | Returns a list of discovered databases.  
mongodb.jumbo_chunks.count | Returns the count of jumbo chunks.  
mongodb.oplog.stats | Returns the status of the replica set, using data polled from the oplog.  
mongodb.ping | Test if a connection is alive or not.  
mongodb.rs.config | Returns the current configuration of the replica set.  
mongodb.rs.status | Returns the replica set status from the point of view of the member where the method is run.  
mongodb.server.status | Returns the database state.  
mongodb.sh.discovery | Returns the list of discovered shards present in the cluster.  
mongodb.version | Returns the database server version.  
mqtt.get | Subscribes to a specific topic or topics (with wildcards) of the provided broker and waits for publications. | MQTT  
mssql.availability.group.get | Returns availability groups. | MSSQL  
mssql.custom.query | Returns the result of a custom query.  
mssql.db.get | Returns all available MSSQL databases.  
mssql.job.status.get | Returns the status of jobs.  
mssql.last.backup.get | Returns the last backup time for all databases.  
mssql.local.db.get | Returns databases that are participating in an Always On availability group and replica (primary or secondary) and are located on the server that the connection was established to.  
mssql.mirroring.get | Returns mirroring info.  
mssql.nonlocal.db.get | Returns databases that are participating in an Always On availability group and replica (primary or secondary) located on other servers (the database is not local to the SQL Server instance that the connection was established to).  
mssql.perfcounter.get | Returns the performance counters.  
mssql.ping | Test if a connection is alive or not.  
mssql.quorum.get | Returns the quorum info.  
mssql.quorum.member.get | Returns the quorum members.  
mssql.replica.get | Returns the replicas.  
mssql.version | Returns the MSSQL version.  
mysql.custom.query | Returns the result of a custom query. | MySQL  
mysql.db.discovery | Returns the list of MySQL databases.  
mysql.db.size | The database size in bytes.  
mysql.get_status_variables | Values of the global status variables.  
mysql.ping | Test if a connection is alive or not.  
mysql.replication.discovery | Returns the list of MySQL replications.  
mysql.replication.get_slave_status | The replication status.  
mysql.version | The MySQL version.  
net.dns.get | Performs a DNS query and returns detailed DNS record information. | Network  
nvml.device.count | The number of GPU devices. | NVIDIA GPU  
nvml.device.decoder.utilization | GPU device decoder utilization.  
nvml.device.ecc.mode | GPU device ECC mode.  
nvml.device.encoder.stats.get | GPU device encoder statistics.  
nvml.device.encoder.utilization | GPU device encoder utilization.  
nvml.device.energy.consumption | GPU device energy consumption.  
nvml.device.errors.memory | GPU device ECC memory error information.  
nvml.device.errors.register | GPU device ECC register error information.  
nvml.device.fan.speed.avg | GPU device fan speed average.  
nvml.device.get | Discovered GPUs with UUID and name.  
nvml.device.graphics.frequency | GPU device graphics clock speed.  
nvml.device.memory.bar1.get | GPU device BAR1 memory information.  
nvml.device.memory.fb.get | GPU device framebuffer memory information.  
nvml.device.memory.frequency | GPU device memory clock speed.  
nvml.device.pci.utilization | GPU device PCI utilization.  
nvml.device.performance.state | GPU device performance state.  
nvml.device.power.limit | GPU device power limit.  
nvml.device.power.usage | GPU device power usage.  
nvml.device.serial | GPU device serial number.  
nvml.device.sm.frequency | GPU device streaming multiprocessor clock speed.  
nvml.device.temperature | GPU device temperature.  
nvml.device.utilization | GPU device utilization statistics.  
nvml.device.video.frequency | GPU device video clock speed.  
nvml.system.driver.version | The NVIDIA driver version.  
nvml.version | The NVML library version.  
oracle.diskgroups.stats | Returns the Automatic Storage Management (ASM) disk groups statistics. | Oracle  
oracle.diskgroups.discovery | Returns the list of ASM disk groups.  
oracle.archive.info | The archive logs statistics.  
oracle.cdb.info | The Container Databases (CDBs) information.  
oracle.custom.query | The result of a custom query.  
oracle.datafiles.stats | Returns the data files statistics.  
oracle.db.discovery | Returns the list of databases.  
oracle.fra.stats | Returns the Fast Recovery Area (FRA) statistics.  
oracle.instance.info | The instance statistics.  
oracle.pdb.info | The Pluggable Databases (PDBs) information.  
oracle.pdb.discovery | Returns the list of PDBs.  
oracle.pga.stats | Returns the Program Global Area (PGA) statistics.  
oracle.ping | Test whether a connection to Oracle can be established.  
oracle.proc.stats | Returns the processes statistics.  
oracle.redolog.info | The log file information from the control file.  
oracle.sga.stats | Returns the System Global Area (SGA) statistics.  
oracle.sessions.stats | Returns the sessions statistics.  
oracle.sys.metrics | Returns a set of system metric values.  
oracle.sys.params | Returns a set of system parameter values.  
oracle.ts.stats | Returns the tablespaces statistics.  
oracle.ts.discovery | Returns a list of tablespaces.  
oracle.user.info | Returns Oracle user information.  
oracle.version | Returns the database server version.  
pgsql.autovacuum.count | The number of autovacuum workers. | PostgreSQL  
pgsql.archive | The information about archived files.  
pgsql.bgwriter | The combined number of checkpoints for the database cluster, broken down by checkpoint type.  
pgsql.cache.hit | The PostgreSQL buffer cache hit rate.  
pgsql.connections | Returns connections by type.  
pgsql.custom.query | Returns the result of a custom query.  
pgsql.db.age | The age of the oldest FrozenXID of the database.  
pgsql.db.bloating_tables | The number of bloating tables per database.  
pgsql.db.discovery | The list of PostgreSQL databases.  
pgsql.db.size | The database size in bytes.  
pgsql.dbstat | Collects the statistics per database.  
pgsql.dbstat.sum | The summarized data for all databases in a cluster.  
pgsql.locks | The information about granted locks per database.  
pgsql.oldest.xid | The age of the oldest XID.  
pgsql.ping | Test if a connection is alive or not.  
pgsql.queries | Query metrics by execution time.  
pgsql.replication.count | The number of standby servers.  
pgsql.replication.process | The flush lag, write lag and replay lag per each sender process.  
pgsql.replication.process.discovery | The replication process name discovery.  
pgsql.replication.recovery_role | The recovery status.  
pgsql.replication.status | The status of replication.  
pgsql.replication_lag.b | The replication lag in bytes.  
pgsql.replication_lag.sec | The replication lag in seconds.  
pgsql.uptime | The PostgreSQL uptime in milliseconds.  
pgsql.version | Returns PostgreSQL version.  
pgsql.wal.stat | The WAL statistics.  
redis.config | Gets the configuration parameters of a Redis instance that match the pattern. | Redis  
redis.info | Gets the output of the INFO command.  
redis.ping | Test if a connection is alive or not.  
redis.slowlog.count | The number of slow log entries since Redis was started.  
smart.attribute.discovery | Returns a list of S.M.A.R.T. device attributes. | S.M.A.R.T.  
smart.disk.discovery | Returns a list of S.M.A.R.T. devices.  
smart.disk.get | Returns all available properties of S.M.A.R.T. devices.  
systemd.unit.get | Returns all properties of a systemd unit. | Systemd  
systemd.unit.info | Systemd unit information.  
systemd.unit.discovery | The list of systemd units and their details.  
web.certificate.get | Validates the certificates and returns certificate details. | Web certificates  
  
See also:

  * [Built-in plugins](/documentation/current/en/manual/extensions/plugins#built-in)
  * [Loadable plugins](/documentation/current/en/manual/extensions/plugins#loadable)

### Item key details

Parameters without angle brackets are mandatory. Parameters marked with angle brackets **<** **>** are optional.

##### ceph.df.details[connString,<user>,<apikey>]

  
The cluster’s data usage and distribution among pools.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### ceph.osd.stats[connString,<user>,<apikey>]

  
Aggregated and per OSD statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### ceph.osd.discovery[connString,<user>,<apikey>]

  
The list of discovered OSDs. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### ceph.osd.dump[connString,<user>,<apikey>]

  
The usage thresholds and statuses of OSDs.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### ceph.ping[connString,<user>,<apikey>]

  
Tests whether a connection to Ceph can be established.  
Return value: _0_ \- connection is broken (if there is any error presented including AUTH and configuration issues); _1_ \- connection is successful.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### ceph.pool.discovery[connString,<user>,<apikey>]

  
The list of discovered pools. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### ceph.status[connString,<user>,<apikey>]

  
The overall cluster's status.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Ceph login credentials.  

##### docker.container_info[<ID>,<info>]

  
Low-level information about a container.  
Return value: The output of the [ContainerInspect](https://docs.docker.com/engine/api/v1.28/#operation/ContainerInspect) API call serialized as JSON.

Parameters:

  * **ID** \- the ID or name of the container;  

  * **info** \- the amount of information returned. Supported values: _short_ (default) or _full_.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.container_stats[<ID>]

  
The container resource usage statistics.  
Return value: The output of the [ContainerStats](https://docs.docker.com/engine/api/v1.28/#operation/ContainerStats) API call and CPU usage percentage serialized as JSON.

Parameter:

  * **ID** \- the ID or name of the container.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.containers

  
The list of containers.  
Return value: The output of the [ContainerList](https://docs.docker.com/engine/api/v1.28/#operation/ContainerList) API call serialized as JSON.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.containers.discovery[<options>]

  
Returns the list of containers. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/).  
Return value: _JSON object_.

Parameter:

  * **options** \- specify whether all or only running containers should be discovered. Supported values: _true_ \- return all containers; _false_ \- return only running containers (default).

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.data.usage

  
Information about the current data usage.  
Return value: The output of the [SystemDataUsage](https://docs.docker.com/engine/api/v1.28/#operation/SystemDataUsage) API call serialized as JSON.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.images

  
Returns the list of images.  
Return value: The output of the [ImageList](https://docs.docker.com/engine/api/v1.28/#operation/ImageList) API call serialized as JSON.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.images.discovery

  
Returns the list of images. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/).  
Return value: _JSON object_.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.info

  
The system information.  
Return value: The output of the [SystemInfo](https://docs.docker.com/engine/api/v1.28/#operation/SystemInfo) API call serialized as JSON.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### docker.ping

  
Test if the Docker daemon is alive or not.  
Return value: _1_ \- the connection is alive; _0_ \- the connection is broken.

The Agent 2 user ('zabbix') must be added to the 'docker' [group](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) for sufficient privileges. Otherwise the check will fail.

##### ember.get[<uri>,<path>]

  
Returns the result of the required device.  
Return value: _JSON object_.

Parameters:

  * **uri** \- Ember+ device URI. Default: 127.0.0.1:9998;  

  * **path** \- OID path to device. Empty by default, returns root collection data.  

##### memcached.ping[connString,<user>,<password>]

  
Test if a connection is alive or not.  
Return value: _1_ \- the connection is alive; _0_ \- the connection is broken (if there is any error presented including AUTH and configuration issues).

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Memcached login credentials.  

##### memcached.stats[connString,<user>,<password>,<type>]

  
Gets the output of the STATS command.  
Return value: _JSON_ \- the output is serialized as JSON.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the Memcached login credentials;  

  * **type** \- stat type to be returned: _items_ , _sizes_ , _slabs_ or _settings_ (empty by default, returns general statistics).

##### mongodb.collection.stats[connString,<user>,<password>,<database>,collection]

  
Returns a variety of storage statistics for a given collection.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials;  

  * **database** \- the database name (default: admin);  

  * **collection** \- the collection name.

##### mongodb.collections.discovery[connString,<user>,<password>]

  
Returns a list of discovered collections. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.collections.usage[connString,<user>,<password>]

  
Returns the usage statistics for collections.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.connpool.stats[connString,<user>,<password>]

  
Returns information regarding the open outgoing connections from the current database instance to other members of the sharded cluster or replica set.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials;  

  * **database** \- the database name (default: admin);  

  * **collection** \- the collection name.

##### mongodb.db.stats[connString,<user>,<password>,<database>]

  
Returns the statistics reflecting a given database system state.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials;  

  * **database** \- the database name (default: admin).  

##### mongodb.db.discovery[connString,<user>,<password>]

  
Returns a list of discovered databases. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.jumbo_chunks.count[connString,<user>,<password>]

  
Returns the count of jumbo chunks.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.oplog.stats[connString,<user>,<password>]

  
Returns the status of the replica set, using data polled from the oplog.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.ping[connString,<user>,<password>]

  
Test if a connection is alive or not.  
Return value: _1_ \- the connection is alive; _0_ \- the connection is broken (if there is any error presented including AUTH and configuration issues).

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.rs.config[connString,<user>,<password>]

  
Returns the current configuration of the replica set.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.rs.status[connString,<user>,<password>]

  
Returns the replica set status from the point of view of the member where the method is run.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.server.status[connString,<user>,<password>]

  
Returns the database state.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.sh.discovery[connString,<user>,<password>]

  
Returns the list of discovered shards present in the cluster.  
Return value: _JSON object_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mongodb.version[connString,<user>,<password>]

  
Returns the database server version.  
Return value: _String_.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MongoDB login credentials.  

##### mqtt.get[<broker url>,topic,<user>,<password>]

  
Subscribes to a specific topic or topics (with wildcards) of the provided broker and waits for publications.  
Return value: Depending on topic content. If wildcards are used, returns topic content as JSON.

Parameters:

  * **broker url** \- the MQTT broker URL in the format `protocol://host:port` without query parameters (supported protocols: `tcp`, `ssl`, `ws`). If no value is specified, the agent will use `tcp://localhost:1883`. If a protocol or port are omitted, default protocol (`tcp`) or port (`1883`) will be used;   

  * **topic** \- the MQTT topic (mandatory). Wildcards (+,#) are supported;  

  * **user, password** \- the authentication credentials (if required).  

Comments:

  * The item must be configured as an [active check](/documentation/current/en/manual/appendix/items/activepassive#active-checks) ('Zabbix agent (active)' item type);
  * TLS encryption certificates can be used by saving them into a default location (e.g. `/etc/ssl/certs/` directory for Ubuntu). For TLS, use the `tls://` scheme.

##### mssql.availability.group.get[URI,<user>,<password>]

  
Returns availability groups.  
Return value: _JSON object_.

Parameters:

  * **URI** \- MSSQL server URI (the only supported schema is `sqlserver://`). Embedded credentials will be ignored. It is possible to specify an instance name as part of the URI, i.e.: `sqlserver://localhost/InstanceName` (no port). If port is specified, the instance name is ignored;  

  * **user, password** \- username, password to send to protected MSSQL server.  

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.custom.query[URI,<user>,<password>,queryName,<args...>]

  
Returns the result of a custom query.  
Return value: _JSON object_.

Parameters:

  * **URI** \- MSSQL server URI (the only supported schema is `sqlserver://`). Embedded credentials will be ignored. It is possible to specify an instance name as part of the URI, i.e.: `sqlserver://localhost/InstanceName` (no port). If port is specified, the instance name is ignored;  

  * **user, password** \- username, password to send to protected MSSQL server;  

  * **queryName** \- name of a custom query configured in `Plugins.MSSQL.CustomQueriesDir` without the .sql extension;  

  * **args** \- one or several comma-separated arguments to pass to a query.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.db.get

  
Returns all available MSSQL databases.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.job.status.get

  
Returns the status of jobs.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.last.backup.get

  
Returns the last backup time for all databases.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.local.db.get

  
Returns databases that are participating in an Always On availability group and replica (primary or secondary) and are located on the server that the connection was established to.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.mirroring.get

  
Returns mirroring info.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.nonlocal.db.get

  
Returns databases that are participating in an Always On availability group and replica (primary or secondary) located on other servers (the database is not local to the SQL Server instance that the connection was established to).  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.perfcounter.get

  
Returns the performance counters.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.ping

  
Ping the database. Test if connection is correctly configured.  
Return value: _1_ \- alive, _0_ \- not alive.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.quorum.get

  
Returns the quorum info.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.quorum.member.get

  
Returns the quorum members.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.replica.get

  
Returns the replicas.  
Return value: _JSON object_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mssql.version

  
Returns the MSSQL version.  
Return value: _String_.

For more information see the [MSSQL plugin](https://git.zabbix.com/projects/AP/repos/mssql/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mysql.custom.query[connString,<user>,<password>,queryName,<args...>]

  
Returns the result of a custom query.  
Return value: _JSON object_.

Parameters:

  * **connString** \- URI or session name;  

  * **user, password** \- MySQL login credentials;  

  * **queryName** \- name of a custom query, must match SQL file name without an extension;  

  * **args** \- one or several comma-separated arguments to pass to a query.

For more information see the [MySQL plugin](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/src/go/plugins/mysql/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### mysql.db.discovery[connString,<user>,<password>]

  
Returns the list of MySQL databases. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: The result of the "show databases" SQL query in LLD JSON format.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials.  

##### mysql.db.size[connString,<user>,<password>,<database name>]

  
The database size in bytes.  
Return value: Result of the "select coalesce(sum(data_length + index_length),0) as size from information_schema.tables where table_schema=?" SQL query for specific database in bytes.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials;  

  * **database name** \- the database name.

##### mysql.get_status_variables[connString,<user>,<password>]

  
Values of the global status variables.  
Return value: Result of the "show global status" SQL query in JSON format.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials.  

##### mysql.ping[connString,<user>,<password>]

  
Test if a connection is alive or not.  
Return value: _1_ \- the connection is alive; _0_ \- the connection is broken (if there is any error presented including AUTH and configuration issues).

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials.  

##### mysql.replication.discovery[connString,<user>,<password>]

  
Returns the list of MySQL replications. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: The result of the "show slave status" SQL query in LLD JSON format.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials.  

##### mysql.replication.get_slave_status[connString,<user>,<password>,<master host>]

  
The replication status.  
Return value: Result of the "show slave status" SQL query in JSON format.

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials;  

  * **master host** \- the replication master host name. If none found, an error is returned. If this parameter is not specified, all hosts are returned.  

##### mysql.version[connString,<user>,<password>]

  
The MySQL version.  
Return value: _String_ (with the MySQL instance version).

Parameters:

  * **connString** \- the URI or session name;  

  * **user, password** \- the MySQL login credentials.  

##### net.dns.get[<ip>,name,<type>,<timeout>,<count>,<protocol>,"<flags>"]

Performs a DNS query and returns detailed DNS record information.  
This item is an extended version of the [`net.dns.record`](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#net.dns.record) Zabbix agent item with more record types and customizable flags supported.  
Return values: _JSON object_

Parameters:

  * **ip** \- the IP address of DNS server (leave empty for the default DNS server);
  * **name** \- the DNS name to query;
  * **type** \- the record type to be queried (default is _SOA_);
  * **timeout** \- the timeout for the request in seconds (default is 1 second);
  * **count** \- the number of tries for the request (default is 2);
  * **protocol** \- the protocol used to perform DNS queries: _udp_ (default) or _tcp_ ;
  * **flags** \- one or more comma-separated arguments to pass to a query.

Comments:

  * The possible values for `type` are: _A_ , _NS_ , _MD_ , _MF_ , _CNAME_ , _SOA_ , _MB_ , _MG_ , _MR_ , _NULL_ , _PTR_ , _HINFO_ , _MINFO_ , _MX_ , _TXT_ , _RP_ , _AFSDB_ , _X25_ , _ISDN_ , _RT_ , _NSAPPTR_ , _SIG_ , _KEY_ , _PX_ , _GPOS_ , _AAAA_ , _LOC_ , _NXT_ , _EID_ , _NIMLOC_ , _SRV_ , _ATMA_ , _NAPTR_ , _KX_ , _CERT_ , _DNAME_ , _OPT_ , _APL_ , _DS_ , _SSHFP_ , _IPSECKEY_ , _RRSIG_ , _NSEC_ , _DNSKEY_ , _DHCID_ , _NSEC3_ , _NSEC3PARAM_ , _TLSA_ , _SMIMEA_ , _HIP_ , _NINFO_ , _RKEY_ , _TALINK_ , _CDS_ , _CDNSKEY_ , _OPENPGPKEY_ , _CSYNC_ , _ZONEMD_ , _SVCB_ , _HTTPS_ , _SPF_ , _UINFO_ , _UID_ , _GID_ , _UNSPEC_ , _NID_ , _L32_ , _L64_ , _LP_ , _EUI48_ , _EUI64_ , _URI_ , _CAA_ , _AVC_ , _AMTRELAY_. Note that values must be in uppercase only; lowercase or mixed case values are not supported.
  * For reverse DNS lookups (when `type` is set to _PTR_), you can provide the DNS name in both reversed and non-reversed format (see examples below). Note that when PTR record is requested, the DNS name is actually an IP address.
  * The possible values for `flags` are: _cdflag_ or _nocdflag_ (default), _rdflag_ (default) or _nordflag_ , _dnssec_ or _nodnssec_ (default), _nsid_ or _nonsid_ (default), _edns0_ (default) or _noedns0_ , _aaflag_ or _noaaflag_ (default), _adflag_ or _noadflag_ (default). The `flags` _dnssec_ and _nsid_ cannot be used together with _noedns0_ , as both require _edns0_. Note that values must be in lowercase only; uppercase case or mixed case values are not supported.
  * Internationalized domain names are not supported, please use IDNA encoded names instead.
  * The output is an object containing DNS record information based on the parameters provided (see [more details](/documentation/current/en/manual/appendix/items/return_values_net_dns_get)).

Examples:
    
    
    net.dns.get[192.0.2.0,example.com,DNSKEY,3,3,tcp,"cdflag,rdflag,nsid"]
           
           net.dns.get[,198.51.100.1,PTR,,,,"cdflag,rdflag,nsid"]
           net.dns.get[,1.100.51.198.in-addr.arpa,PTR,,,,"cdflag,rdflag,nsid"]
           
           net.dns.get[,2a00:1450:400f:800::200e,PTR,,,,"cdflag,rdflag,nsid"]
           net.dns.get[,e.0.0.2.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.0.f.0.0.4.0.5.4.1.0.0.a.2.ip6.arpa,PTR,,,,"cdflag,rdflag,nsid"]

Copy

✔ Copied

##### nvml.device.count

  
The number of GPU devices.  
Return value: _Integer_.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.decoder.utilization[<deviceUUID>]

  
GPU device decoder utilization as a percentage.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.ecc.mode[<deviceUUID>]

  
GPU device ECC mode information (current, pending).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.encoder.stats.get[<deviceUUID>]

  
GPU device encoder statistics.  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.encoder.utilization[<deviceUUID>]

  
GPU device encoder utilization as a percentage.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.energy.consumption[<deviceUUID>]

  
GPU device total energy consumption in millijoules (mJ) since the driver was last reloaded.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.errors.memory[<deviceUUID>]

  
GPU device ECC memory error information (corrected, uncorrected).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.errors.register[<deviceUUID>]

  
GPU device ECC register error information (corrected, uncorrected).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.fan.speed.avg[<deviceUUID>]

  
GPU device average fan speed as a percentage of maximum speed.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.get

  
Discovered GPUs with UUID and name.  
Return value: _JSON_.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.graphics.frequency[<deviceUUID>]

  
GPU device graphics clock speed in MHz.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.memory.fb.get[<deviceUUID>]

  
GPU device framebuffer memory statistics (total, reserved, free, used).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.memory.bar1.get[<deviceUUID>]

  
GPU device BAR1 memory statistics (total, free, used).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.memory.frequency[<deviceUUID>]

  
GPU device memory clock speed in MHz.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.pci.utilization[<deviceUUID>]

  
GPU device PCI utilization (transmit/receive throughput in KBps).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.performance.state[<deviceUUID>]

  
GPU device performance state.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.power.limit[<deviceUUID>]

  
GPU device power limit in milliwatts.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.power.usage[<deviceUUID>]

  
GPU device current power usage in milliwatts.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.serial[<deviceUUID>]

  
GPU device serial number.  
Return value: _String_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.sm.frequency[<deviceUUID>]

  
GPU device streaming multiprocessor clock speed in MHz.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.temperature[<deviceUUID>]

  
GPU device temperature in Celsius.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.utilization[<deviceUUID>]

  
GPU device utilization statistics (GPU/memory utilization as a percentage).  
Return value: _JSON_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.device.video.frequency[<deviceUUID>]

  
GPU device video clock speed in MHz.  
Return value: _Integer_.

Parameter:

  * **deviceUUID** \- GPU device UUID.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.system.driver.version

  
The NVIDIA driver version.  
Return value: _String_.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### nvml.version

  
The NVML library version.  
Return value: _String_.

For more information see the [NVIDIA GPU plugin](https://git.zabbix.com/projects/AP/repos/nvidia-gpu/browse/README.md?at=refs%2Fheads%2Frelease%2F7.4) readme.

##### oracle.diskgroups.stats[connString,<user>,<password>,<service>,<diskgroup>]

  
Returns the Automatic Storage Management (ASM) disk groups statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **diskgroup** \- the name of the ASM disk group to query.

##### oracle.diskgroups.discovery[connString,<user>,<password>,<service>]

  
Returns the list of ASM disk groups. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.archive.info[connString,<user>,<password>,<service>,<destination>]

  
The archive logs statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **destination** \- the name of the destination to query.

##### oracle.cdb.info[connString,<user>,<password>,<service>,<database>]

  
The Container Databases (CDBs) information.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **destination** \- the name of the database to query.

##### oracle.custom.query[connString,<user>,<password>,<service>,queryName,<args...>]

  
The result of a custom query.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **queryName** \- the name of a custom query, must match SQL file name without an extension;  

  * **args** \- one or several comma-separated arguments to pass to the query.

Comments: - Returned data is automatically converted into JSON. - Avoid returning JSON directly from queries, as it will become corrupted when the plugin attempts to convert it into JSON again.

##### oracle.datafiles.stats[connString,<user>,<password>,<service>]

  
Returns the data files statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **diskgroup** \- the name of the ASM disk group to query.

##### oracle.db.discovery[connString,<user>,<password>,<service>]

  
Returns the list of databases. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.fra.stats[connString,<user>,<password>,<service>]

  
Returns the Fast Recovery Area (FRA) statistics.  
Return value: _JSON object_.

Parameters: - **connString** \- it can be:  
\- the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  
\- session name - if such a name is found in the plugin configuration file;  
\- TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  
\- TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  
\- **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  
\- **password** \- the Oracle password;  
\- **service** \- the Oracle service name.  

##### oracle.instance.info[connString,<user>,<password>,<service>]

  
The instance statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.pdb.info[connString,<user>,<password>,<service>,<database>]

  
The Pluggable Databases (PDBs) information.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **destination** \- the name of the database to query.

##### oracle.pdb.discovery[connString,<user>,<password>,<service>]

  
Returns the list of PDBs. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.pga.stats[connString,<user>,<password>,<service>]

  
Returns the Program Global Area (PGA) statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.ping[connString,<user>,<password>,<service>]

  
Test whether a connection to Oracle can be established.  
Return value: _1_ \- the connection is successful; _0_ \- the connection is broken (if there is any error presented including AUTH and configuration issues).

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

Examples:
    
    
    oracle.ping[tcp://127.0.0.1:1521,ZABBIX_MON,zabbix,xe]
           oracle.ping[localhost,ZABBIX_MON,zabbix,xe]
           oracle.ping[zbx_tns_example,ZABBIX_MON,zabbix,xe]
           oracle.ping["(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=xe)))",ZABBIX_MON,zabbix]

##### oracle.proc.stats[connString,<user>,<password>,<service>]

  
Returns the processes statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.redolog.info[connString,<user>,<password>,<service>]

  
The log file information from the control file.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.sga.stats[connString,<user>,<password>,<service>]

  
Returns the System Global Area (SGA) statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.sessions.stats[connString,<user>,<password>,<service>,<lockMaxTime>]

  
Returns the sessions statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **lockMaxTime** \- the maximum session lock duration in seconds to count the session as a prolongedly locked. Default: 600 seconds.

##### oracle.sys.metrics[connString,<user>,<password>,<service>,<duration>]

  
Returns a set of system metric values.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **duration** \- the capturing interval (in seconds) of system metric values. Possible values: _60_ — long duration (default), _15_ — short duration.

##### oracle.sys.params[connString,<user>,<password>,<service>]

  
Returns a set of system parameter values.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.  

##### oracle.ts.stats[connString,<user>,<password>,<service>,<tablespace>,<type>,<conname>]

  
Returns the tablespaces statistics.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **tablespace** \- name of the tablespace to query. Default (if left empty and `type` is set): 
    * "TEMP" (if `type` is set to "TEMPORARY");
    * "USERS" (if `type` is set to "PERMANENT").
  * **type** \- the type of the tablespace to query. Default (if `tablespace` is set): "PERMANENT".
  * **conname** \- name of the container for which the information is required.

If `tablespace`, `type`, or `conname` is omitted, the item will return tablespace statistics for all matching containers (including PDBs and CDB).

##### oracle.ts.discovery[connString,<user>,<password>,<service>]

  
Returns a list of tablespaces. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.

##### oracle.user.info[connString,<user>,<password>,<service>,<username>]

  
Returns Oracle user information.  
Return value: _JSON object_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name;  

  * **username** \- the username for which the information is needed. Lowercase usernames are not supported. Default: current user.

##### oracle.version[connString,<user>,<password>,<service>]

  
Returns the database server version.  
Return value: _String_.

Parameters:

  * **connString** \- it can be:  

    * the URI - if no session with the given name is found, and `Plugins.Oracle.ResolveTNS` is set to false. If it contains a schema (e.g., "tcp://"), port (e.g., 1521) or both, the ResolveTNS option will not be taken into account, and it anyway will be treated as URI;  

    * session name - if such a name is found in the plugin configuration file;  

    * TNS key (supported since Zabbix 7.4.3) - if the ResolveTNS option is set to true, and none of the above conditions apply;  

    * TNS value (supported since Zabbix 7.4.3) - if it starts with the open bracket “(“ (leading spaces ignored). In this case, the ResolveTNS option is not taken into account.  

  * **user** \- the Oracle username, supports appending one of the login options `as sysdba`, `as sysoper`, `as sysasm`, `as sysbackup`, `as sysdg`, `as syskm`, or `as sysrac` in the format `user as sysdba` (a login option is case-insensitive, must not contain a trailing space). Note that only `as sysdba`, `as sysoper`, or `as sysasm` login options are supported before Zabbix 7.4.2;  

  * **password** \- the Oracle password;  

  * **service** \- the Oracle service name.

##### pgsql.autovacuum.count[uri,<username>,<password>,<database name>]

  
The number of autovacuum workers.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.archive[uri,<username>,<password>,<database name>]

  
The information about archived files.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.bgwriter[uri,<username>,<password>,<database name>]

  
The combined number of checkpoints for the database cluster, broken down by checkpoint type.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.cache.hit[uri,<username>,<password>,<database name>]

  
The PostgreSQL buffer cache hit rate.  
Return value: _Float_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.connections[uri,<username>,<password>,<database name>]

  
Returns connections by type.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.custom.query[uri,<username>,<password>,queryName,<args...>]

  
Returns the result of a custom query.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **queryName** \- the name of a custom query, must match the SQL file name without an extension;  

  * **args** \- one or several comma-separated arguments to pass to a query.

##### pgsql.db.age[uri,<username>,<password>,<database name>]

  
The age of the oldest FrozenXID of the database.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.db.bloating_tables[uri,<username>,<password>,<database name>]

  
The number of bloating tables per database.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.db.discovery[uri,<username>,<password>,<database name>]

  
The list of PostgreSQL databases. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.db.size[uri,<username>,<password>,<database name>]

  
The database size in bytes.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.dbstat[uri,<username>,<password>,<database name>]

  
Collects the statistics per database. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.dbstat.sum[uri,<username>,<password>,<database name>]

  
The summarized data for all databases in a cluster.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.locks[uri,<username>,<password>,<database name>]

  
The information about granted locks per database. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery).  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.oldest.xid[uri,<username>,<password>,<database name>]

  
The age of the oldest XID.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.ping[uri,<username>,<password>,<database name>]

  
Tests whether a connection is alive or not.  
Return value: _1_ \- the connection is alive; _0_ \- the connection is broken (if there is any error presented including AUTH and configuration issues).

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.queries[uri,<username>,<password>,<database name>,<time period>]

  
Queries metrics by execution time.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name;  

  * **timePeriod** \- the execution time limit for the count of slow queries (must be a positive integer).

##### pgsql.replication.count[uri,<username>,<password>]

  
The number of standby servers.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.replication.process[uri,<username>,<password>]

  
The flush lag, write lag and replay lag per each sender process.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.replication.process.discovery[uri,<username>,<password>]

  
The replication process name discovery.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.replication.recovery_role[uri,<username>,<password>]

  
The recovery status.  
Return value: _0_ \- master mode; _1_ \- recovery is still in progress (standby mode).

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.replication.status[uri,<username>,<password>]

  
The status of replication.  
Return value: _0_ \- streaming is down; _1_ \- streaming is up; _2_ \- master mode.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.replication_lag.b[uri,<username>,<password>]

  
The replication lag in bytes.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.replication_lag.sec[uri,<username>,<password>]

  
The replication lag in seconds.  
Return value: _Integer_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials.

##### pgsql.uptime[uri,<username>,<password>,<database name>]

  
The PostgreSQL uptime in milliseconds.  
Return value: _Float_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.version[uri,<username>,<password>,<database name>]

  
Returns PostgreSQL version.  
Return value: _String_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### pgsql.wal.stat[uri,<username>,<password>,<database name>]

  
The WAL statistics.  
Return value: _JSON object_.

Parameters:

  * **uri** \- the URI or session name;  

  * **username, password** \- the PostgreSQL credentials;  

  * **database name** \- the database name.  

##### redis.config[connString,<password>,<pattern>]

  
Gets the configuration parameters of a Redis instance that match the pattern.  
Return value: _JSON_ \- if a glob-style pattern was used; single value - if a pattern did not contain any wildcard character.

Parameters:

  * **connString** \- the URI or session name;  

  * **password** \- the Redis password;  

  * **pattern** \- a glob-style pattern (_*_ by default).

##### redis.info[connString,<password>,<section>]

  
Gets the output of the INFO command.  
Return value: _JSON_ \- the output is serialized as JSON.

Parameters:

  * **connString** \- the URI or session name;  

  * **password** \- the Redis password;  

  * **section** \- the [section](https://redis.io/commands/info) of information (_default_ by default).  

##### redis.ping[connString,<password>]

  
Test if a connection is alive or not.  
Return value: _1_ \- the connection is alive; _0_ \- the connection is broken (if there is any error presented including AUTH and configuration issues).

Parameters:

  * **connString** \- the URI or session name;  

  * **password** \- the Redis password.  

##### redis.slowlog.count[connString,<password>]

  
The number of slow log entries since Redis was started.  
Return value: _Integer_.

Parameters:

  * **connString** \- the URI or session name;  

  * **password** \- the Redis password.  

##### smart.attribute.discovery

  
Returns a list of S.M.A.R.T. device attributes.  
Return value: _JSON object_.

Comments:

  * The following macros and their values are returned: {#NAME}, {#DISKTYPE}, {#ID}, {#ATTRNAME}, {#THRESH};
  * HDD, SSD and NVME drive types are supported. Drives can be alone or combined in a RAID. {#NAME} will have an add-on in case of RAID, e.g: {"{#NAME}": "/dev/sda cciss,2"}.

##### smart.disk.discovery[<type>]

  
Returns a list of S.M.A.R.T. devices.  
Return value: _JSON object_.

Parameter:

  * **type** \- specifies a value to scan for the disks. Possible values: _id_ , _name_ (default). _id_ is not supported on Windows, and will return an error if selected

Comments:

  * The following macros and their values are returned: {#NAME}, {#DISKTYPE}, {#MODEL}, {#SN}, {#PATH}, {#ATTRIBUTES}, {#RAIDTYPE};
  * HDD, SSD and NVME drive types are supported. If a drive does not belong to a RAID, the {#RAIDTYPE} will be empty. {#NAME} will have an add-on in case of RAID, e.g: {"{#NAME}": "/dev/sda cciss,2"}.

##### smart.disk.get[<path>,<raid type>]

  
Returns all available properties of S.M.A.R.T. devices.  
Return value: _JSON object_.

Parameters:

  * **path** \- the disk path, the {#PATH} macro may be used as a value;  

  * **raid_type** \- the RAID type, the {#RAID} macro may be used as a value

Comments:

  * HDD, SSD and NVME drive types are supported. Drives can be alone or combined in a RAID;  

  * The data includes smartctl version and call arguments, and additional fields:  
_disk_name_ \- holds the name with the required add-ons for RAID discovery, e.g: {"disk_name": "/dev/sda cciss,2"}  
_disk_type_ \- holds the disk type HDD, SSD, or NVME, e.g: {"disk_type": "ssd"};  

  * If no parameters are specified, the item will return information about all disks.

##### systemd.unit.get[unit name,<interface>]

  
Returns all properties of a systemd unit.  
Return value: _JSON object_.

Parameters:

  * **unit name** \- the unit name (you may want to use the {#UNIT.NAME} macro in item prototype to discover the name);  

  * **interface** \- the unit interface type, possible values: _Unit_ (default), _Service_ , _Socket_ , _Device_ , _Mount_ , _Automount_ , _Swap_ , _Target_ , _Path_.

Comments:

  * This item is supported on Linux platform only;
  * LoadState, ActiveState and UnitFileState for Unit interface are returned as text and integer: `"ActiveState":{"state":1,"text":"active"}`.

##### systemd.unit.info[unit name,<property>,<interface>]

  
A systemd unit information.  
Return value: _String_.

Parameters:

  * **unit name** \- the unit name (you may want to use the {#UNIT.NAME} macro in item prototype to discover the name);  

  * **property** \- unit property (e.g. ActiveState (default), LoadState, Description);
  * **interface** \- the unit interface type (e.g. Unit (default), Socket, Service).

Comments:

  * This item is supported on Linux platform only;
  * This item allows to retrieve a specific property from specific type of interface as described in [dbus API](https://www.freedesktop.org/wiki/Software/systemd/dbus/).

Examples:
    
    
    systemd.unit.info["{#UNIT.NAME}"] #collect active state (active, reloading, inactive, failed, activating, deactivating) info on discovered systemd units
           systemd.unit.info["{#UNIT.NAME}",LoadState] #collect load state info on discovered systemd units
           systemd.unit.info[mysqld.service,Id] #retrieve the service technical name (mysqld.service)
           systemd.unit.info[mysqld.service,Description] #retrieve the service description (MySQL Server)
           systemd.unit.info[mysqld.service,ActiveEnterTimestamp] #retrieve the last time the service entered the active state (1562565036283903)
           systemd.unit.info[dbus.socket,NConnections,Socket] #collect the number of connections from this socket unit

Copy

✔ Copied

##### systemd.unit.discovery[<type>]

  
List of systemd units and their details. Used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/systemd).  
Return value: _JSON object_.

Parameter:

  * **type** \- possible values: _all_ , _automount_ , _device_ , _mount_ , _path_ , _service_ (default), _socket_ , _swap_ , _target_.

This item is supported on Linux platform only.

##### web.certificate.get[hostname,<port>,<address>]

  
Validates the certificates and returns certificate details.  
Return value: _JSON object_.

Parameter:

  * **hostname** \- can be either IP or DNS.  
May contain the URL scheme (_https_ only), path (it will be ignored), and port.  
If a port is provided in both the first and the second parameters, their values must match.  
If address (the 3rd parameter) is specified, the hostname is only used for SNI and hostname verification;  

  * **port** \- the port number (default is 443 for HTTPS);  

  * **address** \- can be either IP or DNS. If specified, it will be used for connection, and hostname (the 1st parameter) will be used for SNI, and host verification. In case, the 1st parameter is an IP and the 3rd parameter is DNS, the 1st parameter will be used for connection, and the 3rd parameter will be used for SNI and host verification.

Comments:

  * This item turns unsupported if the destination specified in the host configuration does not exist, is unavailable, or if the TLS handshake fails with any error except an invalid certificate;  

  * Currently, AIA (Authority Information Access) X.509 extension, CRLs and OCSP (including OCSP stapling), and Certificate Transparency are not supported;
  * JSON response fields: 
    * _x509_ : contains the details of the X.509 certificate. 
      * _version_ : the X.509 version (e.g., `3`).
      * _serial_number_ : the serial number of the certificate.
      * _signature_algorithm_ : the algorithm used to sign the certificate (e.g., `SHA256-RSA`).
      * _issuer_ : the issuer of the certificate.
      * _not_before_ : the start date of the certificate's validity.
      * _not_after_ : the expiration date of the certificate.
      * _subject_ : the subject of the certificate.
      * _public_key_algorithm_ : the algorithm used for the public key (e.g., `RSA`).
      * _alternative_names_ : subject alternative names (if present), otherwise `null`.
    * result: contains the validation result. 
      * _value_ : the validation status (see possible values below).
      * _message_ : detailed validation message (e.g., `"certificate verified successfully"`).
    * _sha1_fingerprint_ : the SHA-1 fingerprint of the certificate.
    * _sha256_fingerprint_ : the SHA-256 fingerprint of the certificate.
  * The `$.result.value` field indicates the certificate validation result. Possible values include: 
    * _valid_ – the certificate is valid and trusted.
    * _valid-but-self-signed_ – the certificate is valid but self-signed, meaning its subject matches its issuer.
    * _invalid_ – the certificate is invalid due to an issue such as expiration, incorrect hostname, or an unknown signing authority.

Example:
    
    
    web.certificate.get[example.com,443]

Copy

✔ Copied

JSON Response:
    
    
    {
             "x509": {
               "version": 3,
               "serial_number": "0ad893bafa68b0b7fb7a404f06ecaf9a",
               "signature_algorithm": "ECDSA-SHA384",
               "issuer": "CN=DigiCert Global G3 TLS ECC SHA384 2020 CA1,O=DigiCert Inc,C=US",
               "not_before": {
                 "value": "Jan 15 00:00:00 2025 GMT",
                 "timestamp": 1736899200
               },
               "not_after": {
                 "value": "Jan 15 23:59:59 2026 GMT",
                 "timestamp": 1768521599
               },
               "subject": "CN=*.example.com,O=Internet Corporation for Assigned Names and Numbers,L=Los Angeles,ST=California,C=US",
               "public_key_algorithm": "ECDSA",
               "alternative_names": [
                 "*.example.com",
                 "example.com"
               ]
             },
             "result": {
               "value": "valid",
               "message": "certificate verified successfully"
             },
             "sha1_fingerprint": "310db7af4b2bc9040c8344701aca08d0c69381e3",
             "sha256_fingerprint": "455943cf819425761d1f950263ebf54755d8d684c25535943976f488bc79d23b"
           }

Copy

✔ Copied