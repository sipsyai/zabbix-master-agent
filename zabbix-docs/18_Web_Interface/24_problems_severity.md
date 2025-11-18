---
title: Problems by severity
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems_severity
downloaded: 2025-11-14 10:38:22
---

# 24 Problems by severity

#### Overview

In this widget, you can display the problem count by severity. You can limit what hosts and triggers are displayed in the widget and define how the problem count is displayed.

The problem count is displayed only for cause problems.

#### Configuration

To configure, select _Problems by severity_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/problems_by_severity.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups to display in the widget.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Host data from these host groups will be displayed in the widget; if no host groups are entered, all host groups will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Exclude host groups_ | Select host groups to hide from the widget.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Host data from these host groups will not be displayed in the widget. For example, hosts 001, 002, 003 may be in Group A and hosts 002, 003 in Group B as well. If we select to _show_ Group A and _exclude_ Group B at the same time, only data from host 001 will be displayed in the dashboard.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Hosts_ | Select hosts to display in the widget.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
If no hosts are entered, all hosts will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Problem_ | You can limit the number of problem hosts displayed by the problem name.  
If you enter a string here, only those hosts with problems whose name contains the entered string will be displayed.  
Macros are not expanded.  
_Severity_ | Mark problem severities to filter problems to be displayed in the widget.  
If no severities are marked, all problems will be displayed.  
_Problem tags_ | Specify problem tags to limit the number of problems displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the _Or_ condition;  
**Or** \- enough if one condition is met.  
_Show_ | Select the show option:  
**Host groups** \- display problems per host group;  
**Totals** \- display a problem total for all selected host groups in colored blocks corresponding to the problem severity.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), and only a problem total will be displayed.  
_Layout_ | Select the layout option:  
**Horizontal** \- colored blocks of totals will be displayed horizontally;  
**Vertical** \- colored blocks of totals will be displayed vertically.  
This parameter is available if _Show_ is set to "Totals".  
_Show operational data_ | Display operational data (see description of _[Operational data](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#operational-data-of-problems)_ in _Monitoring_ > _Problems_) as:  
**None** \- operational data will not be displayed  
**Separately** \- operational data will be displayed as a separate line  
**With problem name** \- operational data will be displayed together with the problem name.  
_Show suppressed problems_ | Mark the checkbox to display problems that would otherwise be suppressed (not shown) because of host maintenance.  
_Hide groups without problems_ | Mark the _Hide groups without problems_ option to hide data from host groups without problems in the widget.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Problem display_ | Display problem count as:  
**All** \- full problem count will be displayed;  
**Separated** \- unacknowledged problem count will be displayed separated as a number of the total problem count;  
**Unacknowledged only** \- only the unacknowledged problem count will be displayed.  
_Show timeline_ | Mark the checkbox to display a visual timeline.