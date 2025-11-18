---
title: TimescaleDB setup
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/timescaledb
downloaded: 2025-11-14 10:46:34
---

# 7 TimescaleDB setup

#### Overview

Zabbix supports TimescaleDB, a PostgreSQL-based database solution of automatically partitioning data into time-based chunks to support faster performance at scale.

Currently, TimescaleDB is not supported by Zabbix proxy.

Instructions on this page can be used for the following scenarios:

  * Creating a TimescaleDB database or migrating from existing PostgreSQL tables to TimescaleDB (see Configuration).
  * Upgrading an existing TimescaleDB database schema when upgrading Zabbix (see Upgrading TimescaleDB schema).

#### Configuration

**Pre-requisites** : TimescaleDB extension of a [supported version](/documentation/current/en/manual/installation/requirements#third-party-external-surrounding-software) installed on the database server. For installation instructions, see [TimescaleDB documentation](https://docs.tigerdata.com/self-hosted/latest/install/).

Before installing TimescaleDB, install a supported PostgreSQL release from the [official PostgreSQL](https://www.postgresql.org/download/) repository.

Enable TimescaleDB extension for the specific database by executing:
    
    
    echo "CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;" | sudo -u postgres psql zabbix

Copy

✔ Copied

Running this command requires database administrator privileges.

If you use a database schema other than 'public' you need to add a SCHEMA clause to the command above. E.g.:  
`echo "CREATE EXTENSION IF NOT EXISTS timescaledb SCHEMA yourschema CASCADE;" | sudo -u postgres psql zabbix`

Then run the `postgresql/timescaledb/schema.sql` script. For new installations, the script must be run after the regular PostgreSQL database has been created with initial schema/data (see [database creation](/documentation/current/en/manual/appendix/install/db_scripts)).
    
    
    cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/schema.sql | sudo -u zabbix psql zabbix

Copy

✔ Copied

Please ignore warning messages informing that the best practices are not followed while running `schema.sql` script on TimescaleDB version 2.9.0 and higher. Regardless of this warning, the configuration will be completed successfully.

The migration of existing history, trends and audit log data may take a lot of time. Zabbix server and frontend must be down for the period of migration.

The `schema.sql` script sets the following housekeeping parameters:

  * Override item history period
  * Override item trend period

In order to use partitioned housekeeping for history and trends, both these options must be enabled. It is also possible to enable override individually either for history only or trends only.

For PostgreSQL and TimescaleDB, the `postgresql/timescaledb/schema.sql` script sets two additional parameters:

  * Enable compression
  * Compress records older than 7 days

To successfully remove compressed data by housekeeper, both _Override item history period_ and _Override item trend period_ options must be enabled. If override is disabled and tables have compressed chunks, the housekeeper will not remove data from these tables, and warnings about incorrect configuration will be displayed in the [_Housekeeping_](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping) and [_System information_](/documentation/current/en/manual/web_interface/frontend_sections/reports/status_of_zabbix) sections.

All of these parameters can be changed in _Administration_ > [_Housekeeping_](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping) after the installation.

You may want to run the timescaledb-tune tool provided by TimescaleDB to optimize PostgreSQL configuration parameters in your `postgresql.conf`.

##### Upgrading TimescaleDB schema

When upgrading Zabbix to a version that contains new TimescaleDB hypertables, Zabbix server does not automatically configure those hypertables (for example, when upgrading from Zabbix 6.4 to 7.4, as versions 7.0.0 and 7.0.2 have introduced new hypertables).

To configure new TimescaleDB hypertables, follow these steps:

  1. Start Zabbix server; this upgrades the existing database.
  2. Check the server log file that the database upgrade is completed; when completed, stop Zabbix server. Note that the server logs a warning if it attempts to enable compression for a table that is not a hypertable.
  3. Run the `postgresql/timescaledb/schema.sql` script; this configures the new TimescaleDB hypertables. Note that, since Zabbix 7.0.0, the script's location and name have changed from `postgresql/timescaledb.sql` to `postgresql/timescaledb/schema.sql`.

Please ignore warning messages informing that the best practices are not followed while running `schema.sql` script on TimescaleDB version 2.9.0 and higher. Regardless of this warning, the configuration will be completed successfully.

#### TimescaleDB compression

Native TimescaleDB compression is supported for all Zabbix tables that are TimescaleDB hypertables. During the upgrade or migration to TimescaleDB, initial compression of the large tables may take a lot of time.

Note that compression is supported under the "timescale" Timescale Community license and it is not supported under "apache" Apache 2.0 license. If Zabbix detects that compression is not supported a warning message is written into the Zabbix server log and users cannot enable compression in the frontend.

Users are encouraged to get familiar with compression in [TimescaleDB documentation](https://docs.tigerdata.com/use-timescale/latest/compression/) before using compression.

Note that there are certain limitations imposed by compression, specifically:

  * Compressed chunk modifications (inserts, deletes, updates) are not allowed
  * Schema changes for compressed tables are not allowed.

Compression settings can be changed in the _History, trends and audit log compression_ block in _Administration_ > _Housekeeping_ section of Zabbix frontend.

_Enable compression_ | Enabled | Checking or unchecking the checkbox does not activate/deactivate compression immediately. Because compression is handled by the Housekeeper, the changes will take effect in up to 2 times `HousekeepingFrequency` hours (set in [zabbix_server.conf](/documentation/current/en/manual/appendix/config/zabbix_server))  
  
After disabling compression, new chunks that fall into the compression period will not be compressed. However, all previously compressed data will stay compressed. To uncompress previously compressed chunks, follow the instructions in [TimescaleDB documentation](https://docs.tigerdata.com/use-timescale/latest/compression/).  
  
When upgrading from older versions of Zabbix with TimescaleDB support, compression will not be enabled by default.  
---|---|---  
_Compress records older than_ | 7d | This parameter cannot be less than 7 days.  
  
Due to immutability of compressed chunks all late data (e.g. data delayed by a proxy) that is older than this value will be discarded.  
  
For better trend update performance, you may want to lower the "chunk_time_interval" for `trends` and `trends_uint` tables from 30 days to 7 days or less depending on how many items use trends. The purpose of this setting is to adhere to TimescaleDB's best practices and to ensure that the chunk size remains within the system's available resources.