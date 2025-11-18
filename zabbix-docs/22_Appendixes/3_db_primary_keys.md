---
title: Database upgrade to primary keys
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_primary_keys
downloaded: 2025-11-14 10:46:28
---

# 3 Database upgrade to primary keys

### Overview

This section provides instructions for manually upgrading tables in existing installations to primary keys.

Upgrading to primary keys optimizes how data is indexed and accessed, which may speed up queries and save space. It also improves data management and synchronization in clustered setups, helping with scaling and ensuring the system remains reliable even if some servers fail.

The instructions provided on this page are designed for advanced users and may need to be adjusted for your specific configuration. Upgrading to primary keys can be time-consuming and resource-intensive. Ensure that enough free disk space is available; depending on your database size and stored data, the process may require up to 2.5 times the space currently used by history tables.

Primary keys are used for all tables in new installations since Zabbix 6.0.

There is no automatic database upgrade to primary keys; however, existing installations may be upgraded manually **after** upgrading Zabbix server to 6.0 or newer.

Since Zabbix 7.0, upgrading tables to primary keys also upgrades tables to use double precision data types.   
  
If you have Zabbix 7.0 (or later), tables already use double precision. However, the instructions on this page can still be followed to upgrade tables to primary keys without affecting tables that already use double precision.   
  
If you have Zabbix 6.4 (or earlier), consider upgrading tables to double precision first. For more information, see [Upgrading to numeric values of extended range](https://www.zabbix.com/documentation/7.0/en/manual/appendix/install/db_float_range) in Zabbix 7.0 documentation.

Instructions are available for:

  * MySQL
  * PostgreSQL
  * TimescaleDB

### Important notes

To perform the database upgrade:

  1. Stop Zabbix server.

Stopping Zabbix server for the time of the upgrade is strongly recommended. However, if absolutely necessary, you can perform the upgrade while the server is running (only for MySQL, MariaDB, and PostgreSQL without TimescaleDB).

  2. Back up your database.
  3. Install the latest zabbix-sql-scripts package compatible with your Zabbix version (e.g., for RHEL: `dnf install zabbix-sql-scripts`).
  4. Run the scripts for your database.
  5. Start Zabbix server.

Run the scripts for the server database only. The proxy will not benefit from this upgrade.

If the database uses partitions, contact the DB administrator or Zabbix Support for help.

CSV files can be removed after a successful upgrade to primary keys.

Optionally, Zabbix frontend may be switched to [maintenance mode](/documentation/current/en/manual/web_interface/maintenance_mode).

### MySQL

Export and import must be performed in tmux/screen to ensure that the session isn't dropped.

See also: Important notes

#### MySQL 8.0+ with mysqlsh

This method can be used with a running Zabbix server, but it is recommended to stop the server for the time of the upgrade. The MySQL Shell (_mysqlsh_) must be [installed](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html) and able to connect to the DB.

  * Log in to MySQL console as root (recommended) or as any user with FILE privileges.

  * Start MySQL with the [local_infile](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_local_infile) variable enabled.

  * Rename old tables and create new tables by running `history_upgrade_prepare.sql`.

    
    
    mysql -uzabbix -p<password> zabbix < /usr/share/zabbix/sql-scripts/mysql/option-patches/history_upgrade_prepare.sql

Copy

✔ Copied

  * Export and import data.

Connect via mysqlsh. If using a socket connection, specifying the path might be required.
    
    
    sudo mysqlsh -uroot -S /run/mysqld/mysqld.sock --no-password -Dzabbix

Copy

✔ Copied

Switch into JavaScript mode using:
    
    
    \js

Copy

✔ Copied

Then run the code below (CSVPATH can be changed as needed):
    
    
    CSVPATH="/var/lib/mysql-files";
           
           util.exportTable("history_old", CSVPATH + "/history.csv", { dialect: "csv" });
           util.importTable(CSVPATH + "/history.csv", {"dialect": "csv", "table": "history" });
           
           util.exportTable("history_uint_old", CSVPATH + "/history_uint.csv", { dialect: "csv" });
           util.importTable(CSVPATH + "/history_uint.csv", {"dialect": "csv", "table": "history_uint" });
           
           util.exportTable("history_str_old", CSVPATH + "/history_str.csv", { dialect: "csv" });
           util.importTable(CSVPATH + "/history_str.csv", {"dialect": "csv", "table": "history_str" });
           
           util.exportTable("history_log_old", CSVPATH + "/history_log.csv", { dialect: "csv" });
           util.importTable(CSVPATH + "/history_log.csv", {"dialect": "csv", "table": "history_log" });
           
           util.exportTable("history_text_old", CSVPATH + "/history_text.csv", { dialect: "csv" });
           util.importTable(CSVPATH + "/history_text.csv", {"dialect": "csv", "table": "history_text" });

Copy

✔ Copied

If you receive the message "JavaScript is not supported", your MySQL Shell installation lacks JS support. In that case, install the official [MySQL Shell package](https://dev.mysql.com/downloads/shell/) from Oracle (or build it from source) so that JavaScript mode is enabled.

  * Follow post-migration instructions to drop the old tables.

#### MariaDB/MySQL 8.0+ without mysqlsh

This upgrade method takes more time and should be used only if an upgrade with _mysqlsh_ is not possible.

##### Table upgrade

  * Log in to MySQL console as root (recommended) or any user with FILE privileges.

  * If performing migration with a running Zabbix server, start MySQL with the [local_infile](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_local_infile) variable enabled.

  * Rename old tables and create new tables by running `history_upgrade_prepare.sql`:

    
    
    mysql -uzabbix -p<password> zabbix < /usr/share/zabbix/sql-scripts/mysql/option-patches/history_upgrade_prepare.sql

Copy

✔ Copied

##### Migration with stopped server

`max_execution_time` (in MySQL) or `max_statement_time` (in MariaDB) must be disabled before migrating data to avoid timeout during migration.

For MySQL:
    
    
    SET @@max_execution_time=0;

Copy

✔ Copied

For MariaDB:
    
    
    SET @@max_statement_time=0;

Copy

✔ Copied
    
    
    INSERT IGNORE INTO history SELECT * FROM history_old;
           INSERT IGNORE INTO history_uint SELECT * FROM history_uint_old;
           INSERT IGNORE INTO history_str SELECT * FROM history_str_old;
           INSERT IGNORE INTO history_log SELECT * FROM history_log_old;
           INSERT IGNORE INTO history_text SELECT * FROM history_text_old;

Copy

✔ Copied

Follow post-migration instructions to drop the old tables.

##### Migration with running server

Check for which paths import/export is enabled:
    
    
    mysql> SELECT @@secure_file_priv;
           +-----------------------+
           | @@secure_file_priv    |
           +-----------------------+
           | /var/lib/mysql-files/ |
           +-----------------------+

Copy

✔ Copied

If _secure_file_priv_ value is a path to a directory, export/import will be performed for files in that directory. In this case, edit paths to files in queries accordingly or set the _secure_file_priv_ value to an empty string for the upgrade time.

If _secure_file_priv_ value is empty, export/import can be performed from any location.

If _secure_file_priv_ value is NULL, set it to the path that contains exported table data ('/var/lib/mysql-files/' in the example above).

For more information, see [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/server-system-variables.html#sysvar_secure_file_priv) or [MariaDB documentation](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#secure_file_priv).

`max_execution_time` (in MySQL) or `max_statement_time` (in MariaDB) must be disabled before exporting data to avoid timeout during export.

For MySQL:
    
    
    SET @@max_execution_time=0;

Copy

✔ Copied

For MariaDB:
    
    
    SET @@max_statement_time=0;

Copy

✔ Copied
    
    
    SELECT * INTO OUTFILE '/var/lib/mysql-files/history.csv' FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n' FROM history_old;
           LOAD DATA INFILE '/var/lib/mysql-files/history.csv' IGNORE INTO TABLE history FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n';
           
           SELECT * INTO OUTFILE '/var/lib/mysql-files/history_uint.csv' FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n' FROM history_uint_old;
           LOAD DATA INFILE '/var/lib/mysql-files/history_uint.csv' IGNORE INTO TABLE history_uint FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n';
           
           SELECT * INTO OUTFILE '/var/lib/mysql-files/history_str.csv' FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n' FROM history_str_old;
           LOAD DATA INFILE '/var/lib/mysql-files/history_str.csv' IGNORE INTO TABLE history_str FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n';
           
           SELECT * INTO OUTFILE '/var/lib/mysql-files/history_log.csv' FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n' FROM history_log_old;
           LOAD DATA INFILE '/var/lib/mysql-files/history_log.csv' IGNORE INTO TABLE history_log FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n';
           
           SELECT * INTO OUTFILE '/var/lib/mysql-files/history_text.csv' FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n' FROM history_text_old;
           LOAD DATA INFILE '/var/lib/mysql-files/history_text.csv' IGNORE INTO TABLE history_text FIELDS TERMINATED BY ',' ESCAPED BY '"' LINES TERMINATED BY '\n';

Copy

✔ Copied

Follow post-migration instructions to drop the old tables.

### PostgreSQL

Export and import must be performed in tmux/screen to ensure that the session isn't dropped. For installations with TimescaleDB, skip this section and proceed to PostgreSQL + TimescaleDB.

See also: Important notes

#### Table upgrade

  * Rename tables using `history_upgrade_prepare.sql`:

    
    
    sudo -u zabbix psql zabbix < /usr/share/zabbix/sql-scripts/postgresql/option-patches/history_upgrade_prepare.sql

Copy

✔ Copied

#### Migration with stopped server

  * Export current history, import it to the temp table, then insert the data into new tables while ignoring duplicates:

    
    
    INSERT INTO history SELECT * FROM history_old ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           INSERT INTO history_uint SELECT * FROM history_uint_old ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           INSERT INTO history_str SELECT * FROM history_str_old ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           INSERT INTO history_log SELECT * FROM history_log_old ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           INSERT INTO history_text SELECT * FROM history_text_old ON CONFLICT (itemid,clock,ns) DO NOTHING;

Copy

✔ Copied

See tips for improving INSERT performance: [PostgreSQL: Bulk Loading Huge Amounts of Data](https://www.cybertec-postgresql.com/en/postgresql-bulk-loading-huge-amounts-of-data), [Checkpoint Distance and Amount of WAL](https://www.cybertec-postgresql.com/en/checkpoint-distance-and-amount-of-wal).

  * Follow post-migration instructions to drop the old tables.

#### Migration with running server

  * Export current history, import it to the temp table, then insert the data into new tables while ignoring duplicates:

    
    
    \copy history_old TO '/tmp/history.csv' DELIMITER ',' CSV
           CREATE TEMP TABLE temp_history (
               itemid                   bigint                                    NOT NULL,
               clock                    integer         DEFAULT '0'               NOT NULL,
               value                    DOUBLE PRECISION DEFAULT '0.0000'          NOT NULL,
               ns                       integer         DEFAULT '0'               NOT NULL
           );
           \copy temp_history FROM '/tmp/history.csv' DELIMITER ',' CSV
           INSERT INTO history SELECT * FROM temp_history ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           \copy history_uint_old TO '/tmp/history_uint.csv' DELIMITER ',' CSV
           CREATE TEMP TABLE temp_history_uint (
               itemid                   bigint                                    NOT NULL,
               clock                    integer         DEFAULT '0'               NOT NULL,
               value                    numeric(20)     DEFAULT '0'               NOT NULL,
               ns                       integer         DEFAULT '0'               NOT NULL
           );
           \copy temp_history_uint FROM '/tmp/history_uint.csv' DELIMITER ',' CSV
           INSERT INTO history_uint SELECT * FROM temp_history_uint ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           \copy history_str_old TO '/tmp/history_str.csv' DELIMITER ',' CSV
           CREATE TEMP TABLE temp_history_str (
               itemid                   bigint                                    NOT NULL,
               clock                    integer         DEFAULT '0'               NOT NULL,
               value                    varchar(255)    DEFAULT ''                NOT NULL,
               ns                       integer         DEFAULT '0'               NOT NULL
           );
           \copy temp_history_str FROM '/tmp/history_str.csv' DELIMITER ',' CSV
           INSERT INTO history_str (itemid,clock,value,ns) SELECT * FROM temp_history_str ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           \copy history_log_old TO '/tmp/history_log.csv' DELIMITER ',' CSV
           CREATE TEMP TABLE temp_history_log (
               itemid                   bigint                                    NOT NULL,
               clock                    integer         DEFAULT '0'               NOT NULL,
               timestamp                integer         DEFAULT '0'               NOT NULL,
               source                   varchar(64)     DEFAULT ''                NOT NULL,
               severity                 integer         DEFAULT '0'               NOT NULL,
               value                    text            DEFAULT ''                NOT NULL,
               logeventid               integer         DEFAULT '0'               NOT NULL,
               ns                       integer         DEFAULT '0'               NOT NULL
           );
           \copy temp_history_log FROM '/tmp/history_log.csv' DELIMITER ',' CSV
           INSERT INTO history_log SELECT * FROM temp_history_log ON CONFLICT (itemid,clock,ns) DO NOTHING;
           
           \copy history_text_old TO '/tmp/history_text.csv' DELIMITER ',' CSV
           CREATE TEMP TABLE temp_history_text (
               itemid                   bigint                                    NOT NULL,
               clock                    integer         DEFAULT '0'               NOT NULL,
               value                    text            DEFAULT ''                NOT NULL,
               ns                       integer         DEFAULT '0'               NOT NULL
           );
           \copy temp_history_text FROM '/tmp/history_text.csv' DELIMITER ',' CSV
           INSERT INTO history_text SELECT * FROM temp_history_text ON CONFLICT (itemid,clock,ns) DO NOTHING;

Copy

✔ Copied

  * Follow post-migration instructions to drop the old tables.

### PostgreSQL + TimescaleDB

Export and import must be performed in tmux/screen to ensure that the session isn't dropped. Zabbix server should be down during the upgrade.

See also: Important notes

  * Rename tables using `history_upgrade_prepare.sql`. 
    * If compression is enabled (on default installation), run the script from `/usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression`:
          
          cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/history_upgrade_prepare.sql | sudo -u zabbix psql zabbix

Copy

✔ Copied

    * If compression is disabled, run the script from `/usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression`:
          
          cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/history_upgrade_prepare.sql | sudo -u zabbix psql zabbix

Copy

✔ Copied

  * Run TimescaleDB hypertable migration scripts based on compression settings: 
    * If compression is enabled (on default installation), run scripts from `/usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression`:
          
          cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/history_upgrade.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/history_upgrade_uint.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/history_upgrade_log.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/history_upgrade_str.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/history_upgrade_text.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/with-compression/trends_upgrade.sql | sudo -u zabbix psql zabbix

Copy

✔ Copied

    * If compression is disabled, run scripts from `/usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression`:
          
          cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/history_upgrade.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/history_upgrade_uint.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/history_upgrade_log.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/history_upgrade_str.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/history_upgrade_text.sql | sudo -u zabbix psql zabbix
                 cat /usr/share/zabbix/sql-scripts/postgresql/timescaledb/option-patches/without-compression/trends_upgrade.sql | sudo -u zabbix psql zabbix

Copy

✔ Copied

See also: [Tips](https://www.tigerdata.com/blog/13-tips-to-improve-postgresql-insert-performance) for improving INSERT performance.

  * Follow post-migration instructions to drop the old tables.

### Post-migration

For all databases, once the migration is completed, do the following:

  * Verify that everything works as expected.

  * Drop old tables:

    
    
    DROP TABLE history_old;
           DROP TABLE history_uint_old;
           DROP TABLE history_str_old;
           DROP TABLE history_log_old;
           DROP TABLE history_text_old;

Copy

✔ Copied

  * For TimescaleDB, also drop the following old table:

    
    
    DROP TABLE trends_old;

Copy

✔ Copied

#### See also

  * [Preparing auditlog table for partitioning](/documentation/current/en/manual/appendix/install/auditlog_primary_keys)