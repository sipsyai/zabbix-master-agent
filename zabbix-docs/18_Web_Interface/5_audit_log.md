---
title: Audit log
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/audit_log
downloaded: 2025-11-14 10:38:51
---

# 5 Audit log

#### Overview

In the _Reports_ → _Audit log_ section, the records of user and system activity can be viewed.

For audit records to be collected and displayed, the _Enable audit logging_ checkbox has to be marked in the _Administration_ → [_Audit log_](/documentation/current/en/manual/web_interface/frontend_sections/administration/audit_log) section. Without this setting enabled, the history of activities will not be recorded in the database and will not be shown in the audit log.

![](/documentation/current/assets/en/manual/web_interface/audit_log.png)

Audit log displays the following data:

_Time_ | Timestamp of the audit record.  
---|---  
_User_ | User who performed the activity.  
_IP_ | IP from which the activity was initiated.  
Clicking on the hyperlink will result in filtering audit log records by this IP.  
_Resource_ | Type of the affected resource (_API token_ , _Action_ , _Authentication_ , _Autoregistration_ , etc.).  
_ID_ | ID of the affected resource.  
Clicking on the hyperlink will result in filtering audit log records by this resource ID.  
_Action_ | Type of the activity (_Add_ , [_Configuration refresh_](/documentation/current/en/manual/web_interface/frontend_sections/administration/proxies#mass-editing-options), _Delete_ , _Execute_ , _Failed login_ , _History clear_ , _Login_ , _Logout_ , [_Push_](/documentation/current/en/manual/api/reference/history/push), _Update_).  
_Recordset ID_ | Shared ID for all audit log records created as a result of the same operation.  
For example, when linking a template to a host, a separate audit log record is created for each inherited template entity (item, trigger, etc.) - all these records will have the same _Recordset ID_.  
Clicking on the hyperlink will result in filtering audit log records by this _Recordset ID_.  
_Details_ | Description of the resource and detailed information about the performed activity.  
If a record contains more than two rows, an additional _Details_ link will be displayed. Click on this link to view the full list of changes.  
  
When a [trapper item](/documentation/current/en/manual/config/items/itemtypes/trapper) or an [HTTP agent item](/documentation/current/en/manual/config/items/itemtypes/http) (with trapping enabled) has received some data, an entry in the audit log will be added only if the data was sent using the [`history.push`](/documentation/current/en/manual/api/reference/history/push) API method, and not the [Zabbix sender](/documentation/current/en/manual/concepts/sender) utility.

#### Using filter

The filter is located below the _Audit log_ bar. It can be opened and collapsed by clicking the _Filter_ tab in the upper-right corner.

![](/documentation/current/assets/en/manual/web_interface/audit_log_filter.png)

You may use the filter to narrow the records by user, affected resource, resource ID, performed operation (_Recordset ID_), and IP. Depending on the resource, one or more specific actions can be selected in the filter.

For better search performance, all data is searched with macros unresolved.

#### Time period selector

The [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) allows to select often required periods with one mouse click. The _Time period_ selector can be expanded and collapsed by clicking the _Time period_ tab in the upper-right corner.