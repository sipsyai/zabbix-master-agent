---
title: Discovery using ODBC SQL queries
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/sql_queries
downloaded: 2025-11-14 10:37:36
---

# 12 Discovery using ODBC SQL queries

#### Overview

This type of low-level [discovery](/documentation/current/en/manual/discovery/low_level_discovery) is done using SQL queries, whose results get automatically transformed into a JSON object suitable for low-level discovery.

#### Item key

SQL queries are performed using a "Database monitor" item type. Therefore, most of the instructions on [ODBC monitoring](/documentation/current/en/manual/config/items/itemtypes/odbc_checks) page apply in order to get a working "Database monitor" discovery rule.

Two item keys may be used in "Database monitor" discovery rules:

  * **db.odbc.discovery**[<unique short description>,<dsn>,<connection string>] - this item transforms the SQL query result into a JSON array, turning the column names from the query result into low-level discovery macro names paired with the discovered field values. These macros can be used in creating item, trigger, etc prototypes. See also: Using db.odbc.discovery.

  * **db.odbc.get**[<unique short description>,<dsn>,<connection string>] - this item transforms the SQL query result into a JSON array, keeping the original column names from the query result as a field name in JSON paired with the discovered values. Compared to `db.odbc.discovery[]`, this item does not create low-level discovery macros in the returned JSON, therefore there is no need to check if the column names can be valid macro names. The low-level discovery macros can be defined as an additional step as required, using the [custom LLD macro](/documentation/current/en/manual/discovery/low_level_discovery#custom-macros) functionality with JSONPath pointing to the discovered values in the returned JSON. See also: Using db.odbc.get.

#### Using db.odbc.discovery

As a practical example to illustrate how the SQL query is transformed into JSON, let us consider low-level discovery of Zabbix proxies by performing an ODBC query on Zabbix database. This is useful for automatic creation of "zabbix[proxy,<name>,lastaccess]" [internal items](/documentation/current/en/manual/config/items/itemtypes/internal) to monitor which proxies are alive.

Let us start with discovery rule configuration:

![lld_rule_odbc.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_odbc.png)

All mandatory input fields are marked with a red asterisk.

Here, the following direct query on Zabbix database is used to select all Zabbix proxies, together with the number of hosts they are monitoring. The number of hosts can be used, for instance, to filter out empty proxies:
    
    
    mysql> SELECT h1.host, COUNT(h2.host) AS count FROM hosts h1 LEFT JOIN hosts h2 ON h1.hostid = h2.proxyid WHERE h1.status IN (5, 6) GROUP BY h1.host;
           +---------+-------+
           | host    | count |
           +---------+-------+
           | Japan 1 |     5 |
           | Japan 2 |    12 |
           | Latvia  |     3 |
           +---------+-------+
           3 rows in set (0.01 sec)

Copy

✔ Copied

By the internal workings of "db.odbc.discovery[,{$DSN}]" item, the result of this query gets automatically transformed into the following JSON:
    
    
    [
               {
                   "{#HOST}": "Japan 1",
                   "{#COUNT}": "5"
               },
               {
                   "{#HOST}": "Japan 2",
                   "{#COUNT}": "12"
               },
               {
                   "{#HOST}": "Latvia",
                   "{#COUNT}": "3"
               }
           ]

Copy

✔ Copied

It can be seen that column names become macro names and selected rows become the values of these macros.

If it is not obvious how a column name would be transformed into a macro name, it is recommended to use column aliases like "COUNT(h2.host) AS count" in the example above.

In case a column name cannot be converted into a valid macro name, the discovery rule becomes not supported, with the error message detailing the offending column number. If additional help is desired, the obtained column names are provided under DebugLevel=4 in Zabbix server log file:
    
    
    $ grep db.odbc.discovery /tmp/zabbix_server.log
            ...
            23876:20150114:153410.856 In db_odbc_discovery() query:'SELECT h1.host, COUNT(h2.host) FROM hosts h1 LEFT JOIN hosts h2 ON h1.hostid = h2.proxy_hostid WHERE h1.status IN (5, 6) GROUP BY h1.host;'
            23876:20150114:153410.860 db_odbc_discovery() column[1]:'host'
            23876:20150114:153410.860 db_odbc_discovery() column[2]:'COUNT(h2.host)'
            23876:20150114:153410.860 End of db_odbc_discovery():NOTSUPPORTED
            23876:20150114:153410.860 Item [Zabbix server:db.odbc.discovery[proxies,{$DSN}]] error: Cannot convert column #2 name to macro.

Copy

✔ Copied

Now that we understand how a SQL query is transformed into a JSON object, we can use {#HOST} macro in item prototypes:

![item_prototype_odbc.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/item_prototype_odbc.png)

Once discovery is performed, an item will be created for each proxy:

![discovered_items_odbc1.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_items_odbc1.png)

#### Using db.odbc.get

Using `db.odbc.get[,{$DSN}]` and the following SQL example:
    
    
    mysql> SELECT h1.host, COUNT(h2.host) AS count FROM hosts h1 LEFT JOIN hosts h2 ON h1.hostid = h2.proxyid WHERE h1.status IN (5, 6) GROUP BY h1.host;
           +---------+-------+
           | host    | count |
           +---------+-------+
           | Japan 1 |     5 |
           | Japan 2 |    12 |
           | Latvia  |     3 |
           +---------+-------+
           3 rows in set (0.01 sec)

Copy

✔ Copied

this JSON will be returned:
    
    
    [
               {
                   "host": "Japan 1",
                   "count": "5"
               },
               {
                   "host": "Japan 2",
                   "count": "12"
               },
               {
                   "host": "Latvia",
                   "count": "3"
               }
           ]

Copy

✔ Copied

As you can see, there are no low-level discovery macros there. However, custom low-level discovery macros can be created in the [LLD macros](/documentation/current/en/manual/discovery/low_level_discovery#custom-macros) tab of a discovery rule using JSONPath, for example:
    
    
    {#HOST} → $.host

Copy

✔ Copied

Now this {#HOST} macro may be used in item prototypes:

![item_prototype_odbc.png](/documentation/current/assets/en/manual/discovery/low_level_discovery/item_prototype_odbc.png)