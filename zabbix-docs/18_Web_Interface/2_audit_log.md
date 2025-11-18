---
title: Audit log
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/audit_log
downloaded: 2025-11-14 10:39:27
---

# 2 Audit log  
  
#### Overview

This section allows configuring audit log settings.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/audit_log.png)

The following parameters are available:

_Enable audit logging_ | Enable (default) or disable audit logging.  
---|---  
_Log system actions_ | Enable (default) or disable audit logging of low-level discovery, network discovery and autoregistration activities performed by the server (System user).  
_Enable internal housekeeping_ | Enable (default) or disable internal housekeeping for audit log records.  
_Data storage period_ | Amount of days audit log records should be kept before being removed by the housekeeper.  
Mandatory if housekeeping is enabled.  
Default: 31 days.  
  
The audit log compression parameters are available in the _Administration > Housekeeping_ section, within the _History, trends and audit log compression_ block, which becomes visible when [TimescaleDB](/documentation/current/en/manual/appendix/install/timescaledb) is used.