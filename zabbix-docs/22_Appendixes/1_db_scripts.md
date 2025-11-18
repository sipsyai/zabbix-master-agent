---
title: Database creation
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_scripts
downloaded: 2025-11-14 10:46:26
---

# 1 Database creation

#### Overview

A Zabbix database must be created during the installation of Zabbix server or proxy.

This section provides instructions for creating a Zabbix database. A separate set of instructions is available for each supported database.

To improve database security by creating database roles/users with minimal privileges, see database creation best practices for each supported database:   
  

  * [MySQL/MariaDB](/documentation/current/en/manual/best_practices/security/access_control/mysql)
  * [PostgreSQL/TimescaleDB](/documentation/current/en/manual/best_practices/security/access_control/postgresql)

For configuring secure TLS connections, see [Secure connection to the database](/documentation/current/en/manual/appendix/install/db_encrypt).

UTF-8 is the only encoding supported by Zabbix. It is known to work without any security flaws. Users should be aware that there are known security issues if using some of the other encodings. For switching to UTF-8, see [Repairing Zabbix database character set and collation](/documentation/current/en/manual/appendix/install/db_charset_coll). See also [Limits of filtering with utf8mb4 collations](/documentation/current/en/manual/installation/known_issues#limits-of-filtering-with-utf8mb4-collations).

If installing from [Zabbix Git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse?at=refs%2Fheads%2Frelease%2F7.4), you need to run the following command prior to proceeding to the next steps:   
  
`make dbschema`

#### MySQL/MariaDB

Character sets utf8 (aka utf8mb3) and utf8mb4 are supported (with utf8_bin and utf8mb4_bin collation respectively) for Zabbix server/proxy to work properly with MySQL database. It is recommended to use utf8mb4 for new installations.

Deterministic triggers need to be created during the import of schema. On MySQL and MariaDB, this requires `GLOBAL log_bin_trust_function_creators = 1` to be set if binary logging is enabled and there is no superuser privileges and log_bin_trust_function_creators = 1 is not set in MySQL configuration file.

If you are installing from Zabbix **packages** , proceed to the [instructions](https://www.zabbix.com/download) for your platform.

If you are installing Zabbix from sources:

  * Create and configure a database and a user.

    
    
    mysql -uroot -p<password>
           
           mysql> create database zabbix character set utf8mb4 collate utf8mb4_bin;
           mysql> create user 'zabbix'@'localhost' identified by '<password>';
           mysql> grant all privileges on zabbix.* to 'zabbix'@'localhost';
           mysql> SET GLOBAL log_bin_trust_function_creators = 1;
           mysql> quit;

Copy

✔ Copied

  * Import the data into the database and set utf8mb4 character set as default. For a Zabbix proxy database, only `schema.sql` should be imported (no images.sql nor data.sql).

    
    
    cd database/mysql
           mysql -uzabbix -p<password> zabbix < schema.sql
           # stop here if you are creating database for Zabbix proxy
           mysql -uzabbix -p<password> zabbix < images.sql
           mysql -uzabbix -p<password> --default-character-set=utf8mb4 zabbix < data.sql

Copy

✔ Copied

`log_bin_trust_function_creators` can be disabled after the schema has been successfully imported:
    
    
    mysql -uroot -p<password>
           
           mysql> SET GLOBAL log_bin_trust_function_creators = 0;
           mysql> quit;

Copy

✔ Copied

#### PostgreSQL

You need to have database user with permissions to create database objects.

If you are installing from Zabbix **packages** , proceed to the [instructions](https://www.zabbix.com/download) for your platform.

If you are installing Zabbix from sources:

  * Create a database user.

The following shell command will create user `zabbix`. Specify a password when prompted and repeat the password (note, you may first be asked for `sudo` password):
    
    
    sudo -u postgres createuser --pwprompt zabbix

Copy

✔ Copied

  * Create a database.

The following shell command will create the database `zabbix` (last parameter) with the previously created user as the owner (`-O zabbix`).
    
    
    sudo -u postgres createdb -O zabbix -E Unicode -T template0 zabbix

Copy

✔ Copied

  * Import the initial schema and data (assuming you are in the root directory of Zabbix sources). For a Zabbix proxy database, only `schema.sql` should be imported (no images.sql nor data.sql).

    
    
    cd database/postgresql
           cat schema.sql | sudo -u zabbix psql zabbix
           # stop here if you are creating database for Zabbix proxy
           cat images.sql | sudo -u zabbix psql zabbix
           cat data.sql | sudo -u zabbix psql zabbix

Copy

✔ Copied

The above commands are provided as an example that will work in most of GNU/Linux installations. You can use different commands depending on how your system/database is configured, for example:   
  
`psql -U <username>`   
  
If you have any trouble setting up the database, please consult your Database administrator.

#### TimescaleDB

Instructions for creating and configuring TimescaleDB are provided in a separate [section](/documentation/current/en/manual/appendix/install/timescaledb).

#### SQLite

Using SQLite is supported for **Zabbix proxy** only!

The database will be automatically created if it does not exist.

Return to the [installation section](/documentation/current/en/manual/installation/install).