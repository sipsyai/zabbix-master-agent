---
title: Action log
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/action_log
downloaded: 2025-11-14 10:38:00
---

# 1 Action log  
  
#### Overview

In the action log widget, you can display details of action operations (notifications, remote commands). It replicates information from _Reports →[Action log](/documentation/current/en/manual/web_interface/frontend_sections/reports/action_log)_.

Up to 1000 records can be displayed.

#### Configuration

To configure, select _Action log_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/action_log.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Recipients_ | Filter entries by recipients. This field is auto-complete, so starting to type the name of a recipient will offer a dropdown of matching recipients. If no recipients are selected, details of action operations for all recipients will be displayed.  
---|---  
_Actions_ | Filter entries by actions. This field is auto-complete, so starting to type the name of an action will offer a dropdown of matching actions. If no actions are selected, details of action operations for all actions will be displayed.  
_Media types_ | Filter entries by media types. This field is auto-complete, so starting to type the name of a media type will offer a dropdown of matching media types. If no media types are selected, details of action operations for all media types will be displayed.  
_Status_ | Mark the checkbox to filter entries by the respective status:  
**In progress** \- action operations that are in progress are displayed;  
**Sent/Executed** \- action operations that have sent a notification or have been executed are displayed;  
**Failed** \- action operations that have failed are displayed.  
_Search string_ | Filter entries by the content of the message/remote command. If you enter a string here, only those action operations whose message/remote command contains the entered string will be displayed. Macros are not resolved.  
_Time period_ | Filter entries by time period. Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for the time period:  
**Dashboard** \- set the _Time period_ selector as the data source;  
**Widget** \- set a compatible widget specified in the _Widget_ parameter as the data source;  
**Custom** \- set the time period specified in the _From_ and _To_ parameters as the data source; if set, a clock icon will be displayed in the upper-right corner of the widget, indicating the set time on mouseover.  
_Widget_ | Enter or select a compatible widget as the data source for the time period.  
This parameter is available if _Time period_ is set to "Widget".  
_From_ | Enter or select the start of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_To_ | Enter or select the end of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_Sort entries by_ | Sort entries by:  
**Time** (descending or ascending);  
**Type** (descending or ascending);  
**Status** (descending or ascending);  
**Recipient** (descending or ascending).  
_Show lines_ | Set how many action log lines will be displayed in the widget.