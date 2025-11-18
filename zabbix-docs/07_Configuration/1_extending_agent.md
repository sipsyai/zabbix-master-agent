---
title: Extending Zabbix agents
source: https://www.zabbix.com/documentation/current/en/manual/config/items/userparameters/extending_agent
downloaded: 2025-11-14 10:35:23
---

# 1 Extending Zabbix agents

This tutorial provides step-by-step instructions on how to extend the functionality of Zabbix agent with the use of a [user parameter](/documentation/current/en/manual/config/items/userparameters).

##### Step 1

Write a script or command line to retrieve required parameter.

For example, we may write the following command in order to get total number of queries executed by a MySQL server:
    
    
    mysqladmin -uroot status | cut -f4 -d":" | cut -f1 -d"S"

Copy

✔ Copied

When executed, the command returns total number of SQL queries.

##### Step 2

Add the command to zabbix_agentd.conf:
    
    
    UserParameter=mysql.questions,mysqladmin -uroot status | cut -f4 -d":" | cut -f1 -d"S"

Copy

✔ Copied

**mysql.questions** is a unique identifier. It can be any valid key identifier, for example, _queries_.

Test this parameter by using Zabbix agent with "-t" flag (if running under root, however, note that the agent may have different permissions when launched as a daemon):
    
    
    zabbix_agentd -t mysql.questions

Copy

✔ Copied

##### Step 3

Reload user parameters from the configuration file by running:
    
    
    zabbix_agentd -R userparameter_reload

Copy

✔ Copied

You may also restart the agent instead of the runtime control command.

Test the parameter by using [zabbix_get](/documentation/current/en/manual/concepts/get) utility.

##### Step 4

Add new item with Key=mysql.questions to the monitored host. Type of the item must be either Zabbix Agent or Zabbix Agent (active).

Be aware that type of returned values must be set correctly on Zabbix server. Otherwise Zabbix won't accept them.