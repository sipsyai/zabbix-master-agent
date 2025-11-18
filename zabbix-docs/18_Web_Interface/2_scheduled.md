---
title: Scheduled reports
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/scheduled
downloaded: 2025-11-14 10:38:48
---

# 2 Scheduled reports  
  
#### Overview

In _Reports → Scheduled reports_ , users with sufficient permissions can configure scheduled generation of PDF versions of the dashboards, which will be sent by email to specified recipients.

![](/documentation/current/assets/en/manual/web_interface/scheduled_overview.png)

The opening screen displays information about scheduled reports, which can be filtered out for easy navigation - see Using filter section below.

Displayed data:

_Name_ | Name of the report. Clicking it opens the report [configuration form](/documentation/current/en/manual/config/reports#configuration).  
---|---  
_Owner_ | User who created the report.  
_Repeats_ | Report generation frequency (daily/weekly/monthly/yearly).  
_Period_ | Period for which the report is prepared.  
_Last sent_ | The date and time when the latest report has been sent.  
_Status_ | Current status of the report (enabled/disabled/expired). Users with sufficient permissions can change the status by clicking it - from "Enabled" to "Disabled" (and back); from "Expired" to "Disabled" (and back). For users with insufficient rights, the status is not clickable.  
_Info_ | Displays informative icons:  
A red icon indicates that report generation has failed; hovering over it will display a tooltip with the error information.  
A yellow icon indicates that a report was generated, but sending to some (or all) recipients has failed or that a report is expired; hovering over it will display a tooltip with additional information.  
  
##### Using filter

You may use the filter to narrow down the list of reports. For better search performance, data is searched with macros unresolved.

The following filtering options are available:

  * _Name_ \- partial name match is allowed
  * _Show_ \- created by current user or all reports
  * _Status_ \- select between "Any" (show all reports), "Enabled", "Disabled", or "Expired"

The filter is located below the _Scheduled reports_ section name. It can be opened and collapsed by clicking the _Filter_ tab in the upper-right corner.

##### Mass update

Sometimes you may want to delete or change the status of a number of reports at once. Instead of opening each individual report for editing, you may use the mass update function for that.

To mass-update some reports, do the following:

  * Mark the checkboxes of the reports to update in the list
  * Click the required button below the list to make the changes (_Enable_ , _Disable_ , or _Delete_)