---
title: Preparing auditlog table for partitioning
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/auditlog_primary_keys
downloaded: 2025-11-14 10:46:29
---

# 4 Preparing auditlog table for partitioning

#### Overview

Some databases (for example, MySQL) require the partitioning column to be part of the table's unique constraint. Therefore, to partition the `auditlog` table by time, the primary key must be changed from `auditid` to a composite key `auditid` \+ `clock`.

This section provides instructions for altering the primary key of the `auditlog` table.

The instructions provided on this page are designed for advanced users. Note that these instructions might need to be adjusted for your specific configuration. Altering the primary key can also be incompatible with future upgrade patches, so manually handling future upgrades may be necessary.   
  
Altering the primary key can be a resource-intensive operation that takes a lot of time depending on the `auditlog` table size. Stopping Zabbix server and switching Zabbix frontend to [maintenance mode](/documentation/current/en/manual/web_interface/maintenance_mode) for the time of the alteration is recommended. However, if absolutely necessary, there is a way to alter the primary key without downtime (see below).

Partitioning the `auditlog` table can improve, for example, housekeeping in large setups. Although Zabbix [housekeeping](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping) currently cannot take advantage of partitioned tables (except for TimescaleDB), you can disable Zabbix housekeeping and delete partitions using scripts.

Since Zabbix 7.0, the `auditlog` table for TimescaleDB has been converted to a hypertable, which allows the housekeeper to drop data by chunks. To upgrade the existing `auditlog` table to a hypertable, see [Upgrading TimescaleDB schema](/documentation/current/en/manual/appendix/install/timescaledb#upgrading-timescaledb-schema).

#### MySQL

##### Important notes on rebuilding indexes

MySQL automatically rebuilds indexes for the primary key during the `ALTER TABLE` operation. However, it is highly recommended to also manually rebuild indexes with the `OPTIMIZE TABLE` statement to ensure optimal database performance.

Rebuilding indexes may temporarily require as much additional disk space as the table itself uses. To obtain the current size of data and indexes, you can execute the following statements:
    
    
    ANALYZE TABLE auditlog;
           SHOW TABLE STATUS LIKE 'auditlog';

Copy

✔ Copied

If the available disk space is a concern, follow the Altering primary key without downtime instructions. Other options are also available:

  * Increasing the [`sort_buffer_size`](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html) MySQL parameter may help to reduce disk space usage when manually rebuilding indexes. However, modifying this variable may impact overall memory usage of the database.
  * Consider freeing up space by deleting potentially unnecessary data.
  * Consider decreasing the _Data storage period_ [housekeeper](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping#overview) parameter before executing the housekeeper.

##### Altering primary key with downtime

1\. Drop the current `auditlog` table primary key and add the new primary key.
    
    
    ALTER TABLE auditlog DROP PRIMARY KEY, ADD PRIMARY KEY (auditid, clock);

Copy

✔ Copied

2\. Rebuild indexes (optional but highly recommended, see Important notes on rebuilding indexes).
    
    
    OPTIMIZE TABLE auditlog;

Copy

✔ Copied

##### Altering primary key without downtime

Manual method of altering the primary key is described here. Alternatively, you can use the [pt-online-schema-change](https://docs.percona.com/percona-toolkit/pt-online-schema-change.html) toolkit from Percona. This toolkit performs the following actions automatically, while also minimizing the space used for altering the `auditlog` table.

1\. Create a new table with the new primary key and create indexes.
    
    
    CREATE TABLE `auditlog_new` (
             `auditid`            varchar(25)                               NOT NULL,
             `userid`             bigint unsigned                           NULL,
             `username`           varchar(100)    DEFAULT ''                NOT NULL,
             `clock`              integer         DEFAULT '0'               NOT NULL,
             `ip`                 varchar(39)     DEFAULT ''                NOT NULL,
             `action`             integer         DEFAULT '0'               NOT NULL,
             `resourcetype`       integer         DEFAULT '0'               NOT NULL,
             `resourceid`         bigint unsigned                           NULL,
             `resource_cuid`      varchar(25)                               NULL,
             `resourcename`       varchar(255)    DEFAULT ''                NOT NULL,
             `recordsetid`        varchar(25)                               NOT NULL,
             `details`            longtext                                  NOT NULL,
             PRIMARY KEY (auditid,clock)
           ) ENGINE=InnoDB;
           CREATE INDEX `auditlog_1` ON `auditlog_new` (`userid`,`clock`);
           CREATE INDEX `auditlog_2` ON `auditlog_new` (`clock`);
           CREATE INDEX `auditlog_3` ON `auditlog_new` (`resourcetype`,`resourceid`);

Copy

✔ Copied

2\. Swap tables.
    
    
    RENAME TABLE auditlog TO auditlog_old, auditlog_new TO auditlog;

Copy

✔ Copied

3\. Copy data from the old table to the new table.
    
    
    INSERT INTO auditlog SELECT * FROM auditlog_old;

Copy

✔ Copied

This can be done in chunks (multiple `INSERT INTO` statements with `WHERE clock` clauses as needed) to avoid excessive resource usage.

4\. Drop the old table.
    
    
    DROP TABLE auditlog_old;

Copy

✔ Copied

#### PostgreSQL

##### Important notes on rebuilding indexes

PostgreSQL automatically rebuilds indexes for the primary key during the `ALTER TABLE` operation. However, it is highly recommended to also manually rebuild indexes with the `REINDEX TABLE CONCURRENTLY` statement to ensure optimal database performance.

Rebuilding indexes may temporarily require up to three times of disk space currently used by indexes. To obtain the current size of indexes, you can execute the following query:
    
    
    SELECT pg_size_pretty(pg_indexes_size('auditlog'));

Copy

✔ Copied

If the available disk space is a concern, follow the Altering primary key without downtime instructions. Other options are also available:

  * Increasing the [`maintenance_work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM) PostgreSQL parameter may help to reduce disk space usage when manually rebuilding indexes. However, modifying this variable may impact overall memory usage of the database.
  * If you have another disk or tablespace with more available space, you might consider changing the temporary storage location for the index rebuild. You can set the [`temp_tablespaces`](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TEMP-TABLESPACES) PostgreSQL parameter to specify a different tablespace for temporary objects.
  * Consider freeing up space by deleting potentially unnecessary data.
  * Consider decreasing the _Data storage period_ [housekeeper](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping#overview) parameter before executing the housekeeper.

##### Altering primary key with downtime

1\. Drop the current `auditlog` table primary key and add the new primary key.
    
    
    ALTER TABLE auditlog DROP CONSTRAINT auditlog_pkey;
           ALTER TABLE auditlog ADD PRIMARY KEY (auditid,clock);

Copy

✔ Copied

2\. Rebuild indexes (optional but highly recommended, see Important notes on rebuilding indexes).
    
    
    REINDEX TABLE CONCURRENTLY auditlog;

Copy

✔ Copied

##### Altering primary key without downtime

Manual method of altering the primary key is described here. Alternatively, the `pg_repack` extension can be considered for creating a new table, copying data, and swapping tables.

1\. Create a new table with the new primary key and create indexes.
    
    
    CREATE TABLE auditlog_new (
             auditid              varchar(25)                               NOT NULL,
             userid               bigint                                    NULL,
             username             varchar(100)    DEFAULT ''                NOT NULL,
             clock                integer         DEFAULT '0'               NOT NULL,
             ip                   varchar(39)     DEFAULT ''                NOT NULL,
             action               integer         DEFAULT '0'               NOT NULL,
             resourcetype         integer         DEFAULT '0'               NOT NULL,
             resourceid           bigint                                    NULL,
             resource_cuid        varchar(25)                               NULL,
             resourcename         varchar(255)    DEFAULT ''                NOT NULL,
             recordsetid          varchar(25)                               NOT NULL,
             details              text            DEFAULT ''                NOT NULL,
             PRIMARY KEY (auditid,clock)
           );
           CREATE INDEX auditlog_new_1 ON auditlog_new (userid,clock);
           CREATE INDEX auditlog_new_2 ON auditlog_new (clock);
           CREATE INDEX auditlog_new_3 ON auditlog_new (resourcetype,resourceid);

Copy

✔ Copied

2\. Swap tables.
    
    
    ALTER TABLE auditlog RENAME TO auditlog_old;
           ALTER TABLE auditlog_new RENAME TO auditlog;

Copy

✔ Copied

3\. Copy data from the old table to the new table.
    
    
    INSERT INTO auditlog SELECT * FROM auditlog_old;

Copy

✔ Copied

This can be done in chunks (multiple `INSERT INTO` statements with `WHERE clock` clauses as needed) to avoid excessive resource usage.

4\. Drop the old table.
    
    
    DROP TABLE auditlog_old;

Copy

✔ Copied

#### See also

  * [Database upgrade to primary keys](/documentation/current/en/manual/appendix/install/db_primary_keys)