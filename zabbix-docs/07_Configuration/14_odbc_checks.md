---
title: ODBC monitoring
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/odbc_checks
downloaded: 2025-11-14 10:35:15
---

# 14 ODBC monitoring

#### Overview

ODBC monitoring corresponds to the **Database monitor** item type in the Zabbix frontend.

ODBC is a C programming language middle-ware API for accessing database management systems (DBMS). The ODBC concept was developed by Microsoft and later ported to other platforms.

Zabbix may query any database, which is supported by ODBC. To do that, Zabbix does not directly connect to the databases, but uses the ODBC interface and drivers set up in ODBC. This allows for more efficient monitoring of different databases for multiple purposes (for example, checking specific database queues, usage statistics, etc.).

Zabbix supports unixODBC, which is one of the most commonly used open source ODBC API implementations.

See also: [known issues](/documentation/current/en/manual/installation/known_issues#odbc-checks) for ODBC checks.

#### Installing unixODBC

The recommended way of installing unixODBC is to use the Linux operating system default package repositories. In the most popular Linux distributions, unixODBC is included in the package repository by default. If packages are not available, the source files can be obtained at the unixODBC homepage: <http://www.unixodbc.org/download.html>.

To install unixODBC, use the package manager for the system of your choice:
    
    
    # For Ubuntu/Debian systems:
           apt install unixodbc unixodbc-dev
           
           # For RedHat/Fedora-based systems:
           dnf install unixODBC unixODBC-devel
           
           # For SUSE-based systems:
           zypper in unixODBC-devel

Copy

✔ Copied

The `unixodbc-dev` or `unixODBC-devel` package is necessary to compile Zabbix with unixODBC support. To enable ODBC support, Zabbix should be compiled with the following [configuration option](/documentation/current/en/manual/installation/install#configure-the-sources):   
  

    
    
    --with-unixodbc[=ARG] # Use ODBC driver against unixODBC package.

Copy

✔ Copied

#### Installing unixODBC drivers

The unixODBC database driver should be installed for the database that will be monitored. For a list of supported databases and drivers, see the unixODBC homepage: <http://www.unixodbc.org/drivers.html>.

In some Linux distributions, database drivers are included in package repositories.

##### MySQL

To install the MySQL unixODBC database driver, use the package manager for the system of your choice:
    
    
    # For Ubuntu/Debian systems:
           apt install odbc-mariadb
           
           # For RedHat/Fedora-based systems:
           dnf install mariadb-connector-odbc
           
           # For SUSE-based systems:
           zypper install mariadb-connector-odbc

Copy

✔ Copied

To install the database driver without a package manager, please refer to [MySQL documentation](https://dev.mysql.com/downloads/connector/odbc/) for `mysql-connector-odbc`, or [MariaDB documentation](https://mariadb.com/kb/en/mariadb-connector-odbc/) for `mariadb-connector-odbc`.

##### PostgreSQL

To install the PostgreSQL unixODBC database driver, use the package manager for the system of your choice:
    
    
    # For Ubuntu/Debian systems:
           apt install odbc-postgresql
           
           # For RedHat/Fedora-based systems:
           dnf install postgresql-odbc
           
           # For SUSE-based systems:
           zypper install psqlODBC

Copy

✔ Copied

To install the database driver without a package manager, please refer to [PostgreSQL documentation](https://www.postgresql.org/download/linux/).

##### Oracle

To install the unixODBC database driver, please refer to [Oracle documentation](https://www.oracle.com/database/technologies/releasenote-odbc-ic.html).

##### MSSQL

To install the MSSQL unixODBC database driver for Ubuntu/Debian systems, use the package manager for the system of your choice:
    
    
    # For Ubuntu/Debian systems:
           apt install tdsodbc
           
           # For RedHat/Fedora-based systems (EPEL packages: https://docs.fedoraproject.org/en-US/epel/):
           dnf install epel-release
           dnf install freetds
           
           # For SUSE-based systems:
           zypper install libtdsodbc0

Copy

✔ Copied

To install the database driver without a package manager, please refer to [FreeTDS user guide](http://www.freetds.org/userguide/).

#### Configuring unixODBC

To configure unixODBC, you must edit the `odbcinst.ini` and `odbc.ini` files. You can verify the location of these files by executing the following command:
    
    
    odbcinst -j

Copy

✔ Copied

The command result should contain information that is similar to the following:
    
    
    unixODBC 2.3.9
           DRIVERS............: /etc/odbcinst.ini
           SYSTEM DATA SOURCES: /etc/odbc.ini
           FILE DATA SOURCES..: /etc/ODBCDataSources

Copy

✔ Copied

##### odbcinst.ini

The `odbcinst.ini` file lists the installed ODBC database drivers. If `odbcinst.ini` is missing, it is necessary to create it manually.
    
    
    [TEST_MYSQL]
           Description=ODBC for MySQL
           Driver=/usr/lib/libmyodbc5.so
           FileUsage=1

Copy

✔ Copied

TEST_MYSQL | Database driver name.  
---|---  
Description | Database driver description.  
Driver | Database driver library location.  
FileUsage | Determines whether the database driver supports connecting to a database server without the support for accessing local files (0); supports reading data from files (1); supports writing data to files (2).  
Threading | Thread serialization level. Supported for PostgreSQL.  
Since 1.6, if the driver manager is built with thread support, you may add another driver entry.  
  
##### odbc.ini

The `odbc.ini` file is used to configure data sources. Note that the list of supported parameters depends on the database driver (for example, Oracle databases may use ServerName instead of Server, etc.).
    
    
    [TEST_MYSQL]
           Description=MySQL Test Database
           Driver=mysql
           Server=127.0.0.1
           User=root
           Password=
           Port=3306
           Socket=
           Database=zabbix

Copy

✔ Copied

TEST_MYSQL | Data source name (DSN).  
---|---  
Description | Data source description.  
Driver | Database driver name (as specified in `odbcinst.ini`).  
Server | Database server IP/DNS.  
User | Database user for connection.  
Password | Database user password.  
Port | Database connection port.  
Socket | Database connection socket.  
Database | Database name.  
  
For other possible configuration parameter options, see [MySQL documentation](https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-configuration-connection-parameters.html).

The `odbc.ini` file for PostgreSQL may contain additional parameters:
    
    
    [TEST_PSQL]
           Description=PostgreSQL Test Database
           Driver=postgresql
           Username=zbx_test
           Password=zabbix
           Servername=127.0.0.1
           Database=zabbix
           Port=5432
           ReadOnly=No
           Protocol=7.4+
           ShowOidColumn=No
           FakeOidIndex=No
           RowVersioning=No
           ShowSystemTables=No
           Fetch=Yes
           BoolsAsChar=Yes
           SSLmode=Require
           ConnSettings=

Copy

✔ Copied

ReadOnly | Specifies whether the database connection allows only read operations (`SELECT` queries) and restricts modifications (`INSERT`, `UPDATE`, and `DELETE` statements); useful for scenarios where data should remain unchanged.  
---|---  
Protocol | PostgreSQL backend protocol version (ignored when using SSL connections).  
ShowOidColumn | Specifies whether to include Object ID (OID) in SQLColumns.  
FakeOidIndex | Specifies whether to create a fake unique index on OID.  
RowVersioning | Specifies whether to enable applications to detect if data has been modified by other users while you are attempting to update a row. Note that this parameter can speed up the update process, since, to update a row, every single column does not need to be specified in the `WHERE` clause.  
ShowSystemTables | Specifies whether the database driver should treat system tables as regular tables in SQLTables; useful for accessibility, allowing visibility into system tables.  
Fetch | Specifies whether the driver should automatically use declare cursor/fetch to handle `SELECT` statements and maintain a cache of 100 rows.  
BoolsAsChar | Controls the mapping of Boolean types.  
If set to "Yes", Bools are mapped to `SQL_CHAR`; otherwise, they are mapped to `SQL_BIT`.  
SSLmode | Specifies the SSL mode for the connection.  
ConnSettings | Additional settings sent to the backend on connection.  
  
##### Testing ODBC connection

To test if the ODBC connection is working successfully, you can use the `isql` utility (included in the `unixODBC` package):
    
    
    isql test
           +---------------------------------------+
           | Connected!                            |
           |                                       |
           | sql-statement                         |
           | help [tablename]                      |
           | quit                                  |
           |                                       |
           +---------------------------------------+

Copy

✔ Copied

#### Item configuration in Zabbix frontend

Configure a **Database monitoring** [item](/documentation/current/en/manual/config/items/item#overview).

![](/documentation/current/assets/en/manual/config/items/itemtypes/db_monitor.png)

All mandatory input fields are marked with a red asterisk.

For database monitoring items, you must specify:

_Type_ | Select "Database monitor" here.  
---|---  
_Key_ | Enter one of the supported item keys:  
**db.odbc.select[]** \- this item returns one value (the first column of the first row of the SQL query result);  
**db.odbc.get[]** \- this item returns multiple rows/columns in JSON format;  
**db.odbc.discovery[]** \- this item returns low-level discovery data.  
_User name_ | Enter the database user name (up to 255 characters).  
This parameter is optional if the database user name is specified in the `odbc.ini` file.  
If a connection string is used, and the _User name_ field is not empty, then it is appended to the connection string as `UID=<user>`.  
_Password_ | Enter the database user password (up to 255 characters).  
This parameter is optional if the password is specified in the `odbc.ini` file.  
If a connection string is used, and the _Password_ field is not empty, then it is appended to the connection string as `PWD=<password>`.  
Special characters are supported in this field.  
The password will be appended to connection string after the username as, for example `UID=<username>;PWD=P?;)*word`.  
To test the resulting string, you can run the following command:  
`isql -v -k 'Driver=libmaodbc.so;Database=zabbix;UID=zabbix;PWD=P?;)*word'`  
_SQL query_ | Enter the SQL query.  
Note that with `db.odbc.select[]`, the query must return one value only.  
_Type of information_ | Select the type of information that will be returned by the query here.  
If the type of information is selected incorrectly, the item will become unsupported.  
  
**Important notes**

  * Database monitoring items will become unsupported if no _odbc poller_ processes are started in the server or proxy configuration. To activate ODBC pollers, set the `StartODBCPollers` parameter in Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server) configuration file or, for checks performed by proxy, in Zabbix [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy) configuration file.
  * The _Timeout_ parameter value in the [item configuration](/documentation/current/en/manual/config/items/item#configuration) form is used as the ODBC login timeout and the query execution timeout. Note that these timeout settings might be ignored if the installed ODBC driver does not support them.
  * The SQL command must return a result set like any query using the `select` statement. The query syntax will depend on the RDBMS which will process them. The syntax of request to a storage procedure must be started with the `call` keyword.

#### Item key details

Parameters without angle brackets are mandatory. Parameters marked with angle brackets **<** **>** are optional.

##### db.odbc.select[<unique short description>,<dsn>,<connection string>]

  
Returns one value, that is, the first column of the first row of the SQL query result.  
Return value: Depending on the SQL query.

Parameters:

  * **unique short description** \- a unique short description to identify the item (for use in triggers, etc.);
  * **dsn** \- the data source name (as specified in `odbc.ini`);
  * **connection string** \- the connection string (may contain driver-specific arguments).

Comments:

  * Although `dsn` and `connection string` are optional parameters, at least one of them is required; if both are defined, `dsn` will be ignored.
  * If a query returns more than one column, only the first column is read. If a query returns more than one line, only the first line is read.

##### db.odbc.get[<unique short description>,<dsn>,<connection string>]

  
Transforms the SQL query result into a JSON array.  
Return value: _JSON object_.

Parameters:

  * **unique short description** \- a unique short description to identify the item (for use in triggers, etc.);
  * **dsn** \- the data source name (as specified in `odbc.ini`);
  * **connection string** \- the connection string (may contain driver-specific arguments).

Comments:

  * Although `dsn` and `connection string` are optional parameters, at least one of them is required; if both are defined, `dsn` will be ignored.
  * Multiple rows/columns in JSON format may be returned. This item may be used as a master item that collects all data in one system call, while JSONPath preprocessing may be used in dependent items to extract individual values. For more information, see an [example](/documentation/current/en/manual/discovery/low_level_discovery/examples/sql_queries#using-db.odbc.get) of the returned format, used in low-level discovery.

Example:
    
    
    # Connection for MySQL ODBC driver 5:
           db.odbc.get[MySQL example,,"Driver=/usr/local/lib/libmyodbc5a.so;Database=master;Server=127.0.0.1;Port=3306"]

Copy

✔ Copied

##### db.odbc.discovery[<unique short description>,<dsn>,<connection string>]

  
Transforms the SQL query result into a JSON array, used for [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery/examples/sql_queries). The column names from the query result are turned into low-level discovery macro names paired with the discovered field values. These macros can be used in creating item, trigger, etc. prototypes.  
Return value: _JSON object_.

Parameters:

  * **unique short description** \- a unique short description to identify the item (for use in triggers, etc.);
  * **dsn** \- the data source name (as specified in `odbc.ini`);
  * **connection string** \- the connection string (may contain driver-specific arguments).

Comments:

  * Although `dsn` and `connection string` are optional parameters, at least one of them is required; if both are defined, `dsn` will be ignored.

#### Error messages

ODBC error messages are structured into fields to provide detailed information. For example, an error message might look like this:
    
    
    Cannot execute ODBC query: [SQL_ERROR]:[42601][7][ERROR: syntax error at or near ";"; Error while executing the query]

Copy

✔ Copied

  * "`Cannot execute ODBC query`" - Zabbix message
  * "`[SQL_ERROR]`" - ODBC return code
  * "`[42601]`" - SQLState
  * "`[7]`" - Native error code
  * "`[ERROR: syntax error at or near ";"; Error while executing the query]`" - Native error message

Note that the error message length is limited to 2048 bytes, so the message can be truncated. If there is more than one ODBC diagnostic record, Zabbix tries to concatenate them (separated with `|`) as far as the length limit allows.