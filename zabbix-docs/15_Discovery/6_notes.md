---
title: Notes on low-level discovery
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/notes
downloaded: 2025-11-14 10:37:24
---

# 6 Notes on low-level discovery  
  
#### Using LLD macros in user macro contexts

LLD macros may be used inside user macro context, for example, [in trigger prototypes](/documentation/current/en/manual/config/macros/user_macros_context#use-cases).

#### Multiple LLD rules for the same item

It is possible to define several low-level discovery rules with the same discovery item.

To do that you need to define the Alias agent [parameter](/documentation/current/en/manual/appendix/config/zabbix_agentd), allowing to use altered discovery item keys in different discovery rules, for example `vfs.fs.discovery[foo]`, `vfs.fs.discovery[bar]`, etc.

#### Data limits for return values

There is no limit for low-level discovery rule JSON data if it is received directly by Zabbix server. This is because the return values are processed without being stored in a database.

There is also no limit for custom low-level discovery rules. However, if custom low-level discovery rule data is retrieved using a user parameter, the user parameter [return value limit](/documentation/current/en/manual/config/items/userparameters#command-result) applies.

If data has to go through Zabbix proxy, it has to store this data in the database. In such a case, [database limits](/documentation/current/en/manual/config/items/item#text-data-limits) apply.