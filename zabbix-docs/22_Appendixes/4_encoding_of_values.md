---
title: Encoding of returned values
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/encoding_of_values
downloaded: 2025-11-14 10:47:22
---

# 4 Encoding of returned values  
  
Zabbix server expects every returned text value in the UTF8 encoding. This is related to any type of checks: Zabbix agent, SSH, Telnet, etc.

Different monitored systems/devices and checks can return non-ASCII characters in the value. For such cases, almost all possible **zabbix** keys contain an additional item key parameter - **< encoding>**. This key parameter is optional but it should be specified if the returned value is not in the UTF8 encoding and it contains non-ASCII characters. Otherwise the result can be unexpected and unpredictable.

A description of behavior with different database backends in such cases follows.

#### MySQL

If a value contains a non-ASCII character in non UTF8 encoding - this character and the following will be discarded when the database stores this value. No warning messages will be written to the _zabbix_server.log_.  
Relevant for at least MySQL version 5.1.61

#### PostgreSQL

If a value contains a non-ASCII character in non UTF8 encoding - this will lead to a failed SQL query (PGRES_FATAL_ERROR:ERROR invalid byte sequence for encoding) and data will not be stored. An appropriate warning message will be written to the _zabbix_server.log_.  
Relevant for at least PostgreSQL version 9.1.3