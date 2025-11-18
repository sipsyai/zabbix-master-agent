---
title: Securing PostgreSQL/TimescaleDB
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/security/access_control/postgresql
downloaded: 2025-11-14 10:39:50
---

# 2 Securing PostgreSQL/TimescaleDB

#### Overview

This section contains best practices for securing a PostgreSQL database.

For a basic setup, see the default [PostgreSQL database creation](/documentation/current/en/manual/appendix/install/db_scripts#postgresql) instructions, which include creating the 'zabbix' user with full privileges on the Zabbix database. This user is the database owner that also has the necessary privileges for modifying the database structure when [upgrading](/documentation/current/en/manual/installation/upgrade) Zabbix.

To improve security, configuring a secure schema usage pattern, as well as creating additional database roles and users with minimal privileges is recommended. These roles and users should be configured based on the [principle of least privilege](/documentation/current/en/manual/best_practices/security/access_control#principle-of-least-privilege), that is, they should only have privileges that are essential for performing the intended functions.

#### Database setup

Create the user that will be the database owner, and create the Zabbix database; the database owner is the user that is specified on database creation:
    
    
    createuser -U postgres -h localhost --pwprompt usr_owner
           createdb -U postgres -h localhost -O usr_owner -E Unicode -T template0 zabbix

Copy

✔ Copied

A clean install or upgrade of the database has to be performed by the database owner. This is because the right to drop a database object or alter its definition is a privilege that is inherent to the database owner and cannot be granted or revoked.

The following commands on this page must be executed while the connection to PostgreSQL is made specifically to the `zabbix` database.

Create the `zabbix` schema and set the database owner (`usr_owner`) to be the owner of this schema:
    
    
    CREATE SCHEMA zabbix AUTHORIZATION usr_owner;

Copy

✔ Copied

Configure a secure schema [usage pattern](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATTERNS):
    
    
    REVOKE CREATE ON SCHEMA public FROM PUBLIC;
           REVOKE ALL ON DATABASE zabbix FROM PUBLIC;
           -- Note: search_path should point to the "zabbix" schema:
           ALTER ROLE ALL IN DATABASE zabbix SET search_path = "zabbix";

Copy

✔ Copied

After setting up the database, proceed to creating user roles.

#### Creating user roles

Create the following roles with the corresponding privileges:

  * **zbx_srv** \- role for running Zabbix server and proxy:

    
    
    CREATE ROLE zbx_srv;
           GRANT CONNECT ON DATABASE zabbix TO zbx_srv;
           GRANT USAGE ON SCHEMA zabbix TO zbx_srv;
           ALTER DEFAULT PRIVILEGES FOR ROLE usr_owner IN SCHEMA zabbix GRANT DELETE, INSERT, SELECT, UPDATE ON TABLES TO zbx_srv;
           ALTER DEFAULT PRIVILEGES FOR ROLE usr_owner IN SCHEMA zabbix GRANT SELECT, UPDATE, USAGE ON sequences TO zbx_srv;

Copy

✔ Copied

  * **zbx_web** \- role for running Zabbix frontend and API:

    
    
    CREATE ROLE zbx_web;
           GRANT CONNECT ON DATABASE zabbix TO zbx_web;
           GRANT USAGE ON SCHEMA zabbix TO zbx_web;
           ALTER DEFAULT PRIVILEGES FOR ROLE usr_owner IN SCHEMA zabbix GRANT DELETE, INSERT, SELECT, UPDATE ON TABLES TO zbx_web;
           ALTER DEFAULT PRIVILEGES FOR ROLE usr_owner IN SCHEMA zabbix GRANT SELECT, UPDATE, USAGE ON sequences TO zbx_web;

Copy

✔ Copied

  * **zbx_bckp** \- role for table backup:

    
    
    CREATE ROLE zbx_bckp;
           GRANT CONNECT ON DATABASE zabbix TO zbx_bckp;
           GRANT USAGE ON SCHEMA zabbix TO zbx_bckp;
           ALTER DEFAULT PRIVILEGES FOR ROLE usr_owner IN SCHEMA zabbix GRANT SELECT ON TABLES TO zbx_bckp;
           ALTER DEFAULT PRIVILEGES FOR ROLE usr_owner IN SCHEMA zabbix GRANT SELECT, UPDATE, USAGE ON sequences TO zbx_bckp;

Copy

✔ Copied

Table restoration is possible only by the database owner.

After creating roles, they can be assigned to users.

#### Assigning user roles

To assign the created user roles, create users and assign the relevant roles to them. Replace `<user>`, `<role>`, and `<password>` as necessary.
    
    
    CREATE USER <user> WITH ENCRYPTED password '<password>';
           GRANT <role> TO <user>;

Copy

✔ Copied

For example, to create and assign the role for running Zabbix server and proxy:
    
    
    CREATE USER usr_srv WITH ENCRYPTED password 'password';
           GRANT zbx_srv TO usr_srv;

Copy

✔ Copied

#### Database partitioning with TimescaleDB

Database partitioning is facilitated by TimescaleDB. To utilize TimescaleDB, Zabbix server requires database owner privileges.

If the PostgreSQL `zabbix` schema has already been created in the `zabbix` database, you can enable TimescaleDB with the following command:
    
    
    echo "CREATE EXTENSION IF NOT EXISTS timescaledb WITH SCHEMA zabbix CASCADE;" | sudo -u postgres psql zabbix

Copy

✔ Copied