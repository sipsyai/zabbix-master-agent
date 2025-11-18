---
title: ODBC template operation
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box/odbc_checks
downloaded: 2025-11-14 10:36:06
---

# 6 ODBC template operation

Steps to ensure correct operation of templates that collect metrics via [ODBC monitoring](/documentation/current/en/manual/config/items/itemtypes/odbc_checks):

1\. Make sure that required ODBC driver is installed on Zabbix server or proxy.  
2\. [Link](/documentation/current/en/manual/config/templates/linking#linking-a-template) the template to a target host (if the template is not available in your Zabbix installation, you may need to [import](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade) the template first).  
3\. If necessary, adjust the values of template macros.  
4\. Configure the instance being monitored to allow data sharing with Zabbix.

A detailed description of a template, including the full list of macros, items, and triggers, is available in the template's README file (accessible by clicking on a template name).

The following templates are available:

  * [MSSQL by ODBC](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mssql_odbc/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MySQL by ODBC](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_odbc/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Oracle by ODBC](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/oracle_odbc/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [PostgreSQL by ODBC](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/postgresql_odbc/README.md?at=refs%2Fheads%2Frelease%2F7.4)