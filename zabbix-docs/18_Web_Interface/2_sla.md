---
title: SLA
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/services/sla
downloaded: 2025-11-14 10:38:43
---

# 2 SLA

### Overview

This section allows to view and [configure](/documentation/current/en/manual/it_services/sla) SLAs.

### SLAs

![](/documentation/current/assets/en/manual/web_interface/sla_list.png)

A list of the configured SLAs is displayed. _Note_ that only the SLAs related to services accessible to the user will be displayed (as read-only, unless _Manage SLA_ is enabled for the user role).

Displayed data:

_Name_ | The SLA name is displayed.  
The name is a link to [SLA configuration](/documentation/current/en/manual/it_services/sla#configuration).  
---|---  
_SLO_ | The service level objective (SLO) is displayed.  
_Effective date_ | The date of starting SLA calculation is displayed.  
_Reporting period_ | The period used in the SLA report is displayed - _daily_ , _weekly_ , _monthly_ , _quarterly_ , or _annually_.  
_Time zone_ | The SLA time zone is displayed.  
_Schedule_ | The SLA schedule is displayed - 24x7 or custom.  
_SLA report_ | Click on the link to see the SLA report for this SLA.  
_Status_ | The SLA status is displayed - enabled or disabled.