---
title: Securing MySQL/MariaDB
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/security/access_control/mysql
downloaded: 2025-11-14 10:39:49
---

# 1 Securing MySQL/MariaDB

#### Overview

This section contains best practices for securing a MySQL/MariaDB database.

For a basic setup, see the default [MySQL/MariaDB database creation](/documentation/current/en/manual/appendix/install/db_scripts#mysqlmariadb) instructions, which include creating the 'zabbix' user with full privileges on the Zabbix database. This user is the database owner that also has the necessary privileges for modifying the database structure when [upgrading](/documentation/current/en/manual/installation/upgrade) Zabbix.

To improve security, creating additional database roles and users with minimal privileges is recommended. These roles and users should be configured based on the [principle of least privilege](/documentation/current/en/manual/best_practices/security/access_control#principle-of-least-privilege), that is, they should only have privileges that are essential for performing the intended functions.

#### Creating user roles

Create the following roles with the corresponding privileges:

  * **zbx_srv** \- role for running Zabbix server and proxy:

    
    
    CREATE ROLE 'zbx_srv';
           GRANT DELETE, INSERT, SELECT, UPDATE ON zabbix.* TO 'zbx_srv';
           FLUSH PRIVILEGES;

Copy

✔ Copied

  * **zbx_web** \- role for running Zabbix frontend and API:

    
    
    CREATE ROLE 'zbx_web';
           GRANT DELETE, INSERT, SELECT, UPDATE ON zabbix.* TO 'zbx_web';
           FLUSH PRIVILEGES;

Copy

✔ Copied

  * **zbx_bckp** \- role for table backup:

    
    
    CREATE ROLE 'zbx_bckp';
           GRANT LOCK TABLES, TRIGGER, SELECT ON zabbix.* TO 'zbx_bckp';
           GRANT process ON *.* TO 'zbx_bckp';
           FLUSH PRIVILEGES;

Copy

✔ Copied

Table restoration and upgrade should be performed by the database owner.

  * **zbx_part** \- role with a reduced set of privileges for database partitioning; note that this role can be created only after the database has been created, as it grants privileges on specific database tables:

    
    
    CREATE ROLE 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.history TO 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.history_uint TO 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.history_str TO 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.history_text TO 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.history_log TO 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.trends TO 'zbx_part';
           GRANT SELECT, ALTER, DROP ON zabbix.trends_uint TO 'zbx_part';
           -- For MariaDB: skip the next line (GRANT session_variables_admin ON *.* TO 'zbx_part';)
           GRANT session_variables_admin ON *.* TO 'zbx_part';
           GRANT SELECT ON zabbix.dbversion TO 'zbx_part';
           GRANT SELECT, DELETE ON zabbix.housekeeper TO 'zbx_part';
           FLUSH PRIVILEGES;

Copy

✔ Copied

After creating roles, they can be assigned to users.

#### Assigning user roles

To assign the created user roles, create users and assign the relevant roles to them. Replace `<user>`, `<host>`, `<role>`, and `<password>` as necessary.
    
    
    CREATE USER '<user>'@'<host>' IDENTIFIED BY '<password>';
           GRANT '<role>' TO '<user>'@'<host>';
           SET DEFAULT ROLE '<role>' TO '<user>'@'<host>';
           -- For MariaDB: SET DEFAULT ROLE '<role>' FOR '<user>'@'<host>'
           FLUSH PRIVILEGES;

Copy

✔ Copied

For example, to create and assign the role for running Zabbix server and proxy:
    
    
    CREATE USER 'usr_srv'@'localhost' IDENTIFIED BY 'password';
           GRANT 'zbx_srv' TO 'usr_srv'@'localhost';
           SET DEFAULT ROLE ALL TO 'usr_srv'@'localhost';
           FLUSH PRIVILEGES;

Copy

✔ Copied