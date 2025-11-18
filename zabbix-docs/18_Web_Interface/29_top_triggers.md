---
title: Top triggers
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers
downloaded: 2025-11-14 10:38:27
---

# 29 Top triggers  
  
#### Overview

In the _Top triggers_ widget, you can see the triggers with the highest number of problems.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers.png)

The maximum number of triggers that can be shown is 1000. When viewing the widget on a dashboard, it is possible to select the time period for displaying the data.

The information on top triggers is also available in the _Reports_ → [_Top 100 triggers_](/documentation/current/en/manual/web_interface/frontend_sections/reports/triggers_top) menu section.

#### Configuration

To configure, select _Top triggers_ as widget type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/top_triggers_configuration.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups to display problems of in the widget.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Problems from these host groups will be displayed in the widget; if no host groups are entered, problems from all host groups will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Hosts_ | Select hosts to display problems of in the widget.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
If no hosts are entered, problems of all hosts will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Problem_ | You can view the triggers for particular problems only. For this, enter the string to be matched in the problem name.  
Macros are not expanded.  
_Severity_ | Mark trigger severities to filter triggers to be displayed in the widget.  
If no severities are marked, all triggers will be displayed.  
_Problem tags_ | Specify the tags of the problems to be displayed in the widget.  
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
_Time period_ | Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for the time period:  
**Dashboard** \- set the _Time period_ selector as the data source;  
**Widget** \- set a compatible widget specified in the _Widget_ parameter as the data source;  
**Custom** \- set the time period specified in the _From_ and _To_ parameters as the data source; if set, a clock icon will be displayed in the upper-right corner of the widget, indicating the set time on mouseover.  
_Widget_ | Enter or select a compatible widget (_Graph_ , _Graph (classic)_ , _Graph prototype_) as the data source for the time period.  
This parameter is available if _Time period_ is set to "Widget".  
_From_ | Enter or select the start of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_To_ | Enter or select the end of the time period.  
[Relative time syntax](/documentation/current/en/manual/web_interface/time_period_selector) (`now`, `now/d`, `now/w-1w`, etc.) is supported.  
This parameter is available if _Time period_ is set to "Custom".  
_Trigger limit_ | Set the number of triggers to be displayed. Possible value range: 1-1000.