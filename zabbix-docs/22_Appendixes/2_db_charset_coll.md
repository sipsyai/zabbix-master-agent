---
title: Repairing Zabbix database character set and collation
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_charset_coll
downloaded: 2025-11-14 10:46:27
---

# 2 Repairing Zabbix database character set and collation

#### MySQL/MariaDB

Historically, MySQL and derivatives used 'utf8' as an alias for utf8mb3 - MySQL's own 3-byte implementation of the standard UTF8, which is 4-byte. Starting from MySQL 8.0.28 and MariaDB 10.6.1, 'utf8mb3' character set is deprecated and at some point its support will be dropped while 'utf8' will become a reference to 'utf8mb4'. Since Zabbix 6.0, 'utf8mb4' is supported. To avoid future problems, it is highly recommended to use 'utf8mb4'. Another advantage of switching to 'utf8mb4' is support of supplementary Unicode characters.

As versions before Zabbix 6.0 are not aware of utf8mb4, make sure to first upgrade Zabbix server and DB schema to 6.0.x or later before executing utf8mb4 conversion.

**1.** Check the database character set and collation.

For example:
    
    
    mysql> SELECT @@character_set_database, @@collation_database;
           +--------------------------+----------------------+
           | @@character_set_database | @@collation_database |
           +--------------------------+----------------------+
           | latin2                   | latin2 _general_ci   |
           +--------------------------+----------------------+

Copy

✔ Copied

Or:
    
    
    mysql> SELECT @@character_set_database, @@collation_database;
           +--------------------------+----------------------+
           | @@character_set_database | @@collation_database |
           +--------------------------+----------------------+
           | utf8                     | utf8_bin             |
           +--------------------------+----------------------+

Copy

✔ Copied

As we see, the character set here is not 'utf8mb4' and collation is not 'utf8mb4_bin', so we need to fix them.

**2.** Stop Zabbix.

**3.** Create a backup copy of the database!

**4.** Fix the character set and collation on database level:
    
    
    alter database <your DB name> character set utf8mb4 collate utf8mb4_bin;

Copy

✔ Copied

Fixed values:
    
    
    mysql> SELECT @@character_set_database, @@collation_database;
           +--------------------------+----------------------+
           | @@character_set_database | @@collation_database |
           +--------------------------+----------------------+
           | utf8mb4                  | utf8mb4_bin          |
           +--------------------------+----------------------+ 

Copy

✔ Copied

**5.** Load the [script](../../../../assets/en/manual/appendix/install/utf8mb4_convert.sql) to fix character set and collation on table and column level:
    
    
    mysql <your DB name> < utf8mb4_convert.sql

Copy

✔ Copied

**6.** Execute the script:
    
    
                   SET @ZABBIX_DATABASE = '<your DB name>';
           If MariaDB →  set innodb_strict_mode = OFF;        
                          CALL zbx_convert_utf8();
           If MariaDB →  set innodb_strict_mode = ON;   
                          drop procedure zbx_convert_utf8;

Copy

✔ Copied

Please note that 'utf8mb4' is expected to consume slightly more disk space.

**7.** If no errors - you may want to create a database backup copy with the fixed database.

**8.** Start Zabbix.