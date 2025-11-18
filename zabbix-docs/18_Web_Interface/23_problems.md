---
title: Problems
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems
downloaded: 2025-11-14 10:38:21
---

# 23 Problems  
  
#### Overview

In this widget you can display current problems. The information in this widget is similar to _Monitoring_ > _Problems_.

Up to 1000 records can be displayed.

#### Configuration

To configure, select _Problems_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/problems_widget.png)

You can limit how many problems are displayed in the widget in various ways - by problem status, problem name, severity, host group, host, event tag, acknowledgment status, etc.

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Show_ | Filter by problem status:  
**Recent problems** \- unresolved and recently resolved problems are displayed (default);  
**Problems** \- unresolved problems are displayed;  
**History** \- history of all events is displayed.  
---|---  
_Host groups_ | Select host groups to display problems of in the widget.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Problems from these host groups will be displayed in the widget; if no host groups are entered, problems from all host groups will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Exclude host groups_ | Select host groups to hide problems of from the widget.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Specifying a parent host group implicitly selects all nested host groups.  
Problems from these host groups will not be displayed in the widget. For example, hosts 001, 002, 003 may be in Group A and hosts 002, 003 in Group B as well. If we select to _show_ Group A and _exclude_ Group B at the same time, only problems from host 001 will be displayed in the widget.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Hosts_ | Select hosts to display problems of in the widget.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
If no hosts are entered, problems of all hosts will be displayed.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Problem_ | You can limit the number of problems displayed by their name.  
If you enter a string here, only those problems whose name contains the entered string will be displayed.  
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
  
When filtered, the tags specified here will be displayed first with the problem, unless overridden by the _Tag display priority_ (see below) list.  
_Show tags_ | Select the number of displayed tags:  
**None** \- no _Tags_ column;  
**1** \- _Tags_ column contains one tag;  
**2** \- _Tags_ column contains two tags;  
**3** \- _Tags_ column contains three tags.  
To see all tags for the problem roll your mouse over the three dots icon.  
_Tag name_ | Select tag name display mode:  
**Full** \- tag names and values are displayed in full;  
**Shortened** \- tag names are shortened to 3 symbols, but tag values are displayed in full;  
**None** \- only tag values are displayed; no names.  
_Tag display priority_ | Enter tag display priority for a problem, as a comma-separated list of tags.  
Only tag names should be used, no values.  
Example: `Services,Applications,Application`  
The tags of this list will always be displayed first, overriding the natural ordering by alphabet.  
_Show operational data_ | Select the mode for displaying [operational data](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#operational-data-of-problems):  
**None** \- no operational data is displayed;  
**Separately** \- operational data is displayed in a separate column;  
**With problem name** \- append operational data to the problem name, using parentheses for the operational data.  
_Show symptoms_ | Mark the checkbox to display in its own line problems classified as symptoms.  
_Show suppressed problems_ | Mark the checkbox to display problems that would otherwise be suppressed (not shown) because of host maintenance or single [problem suppression](/documentation/current/en/manual/acknowledgment/suppression).  
_Acknowledgement status_ | Filter to display all problems, unacknowledged problems only, or acknowledged problems only. Mark the additional checkbox to filter out those problems ever acknowledged by you.  
_Sort entries by_ | Sort entries by:  
**Time** (descending or ascending);  
**Severity** (descending or ascending);  
**Problem name** (descending or ascending);  
**Host** (descending or ascending).  
  
Sorting entries by **Host** (descending or ascending) is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Show timeline_ | Mark the checkbox to display a visual timeline.  
_Highlight whole row_ | Mark the checkbox to highlight the full line for unresolved problems. The problem severity color is used for highlighting.  
_Highlight whole row_ is not available in the high-contrast themes.  
This option is supported since Zabbix 7.4.3.  
_Show lines_ | Specify the number of problem lines to display.  
  
#### Using the widget

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/problems_widget_view.png)

Problems widget offers quick access to additional information:

  * Click on the problem date (in the Time column) or the recovery date (in the Recovery Time column) to view [event details](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#viewing-details).
  * If the Info field is not empty, hover over the displayed icon to view additional details.
  * Click on the host name to open the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu).
  * Click on the problem name to open the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu).
  * Hover over or click on the problem duration to view problem event popup.
  * Pressing Update opens an [Update problem](/documentation/current/en/manual/acknowledgment#updating-problems) window.
  * Hover over or press on the gray arrow icon in Actions column to view list of executed actions.

##### Problem event popup

The problem event popup includes the list of problem events for this trigger and, if defined, the trigger description and a clickable URL.

![](/documentation/current/assets/en/manual/web_interface/problem_event_popup.png)

To bring up the problem event popup:

  * Roll a mouse over the problem duration in the _Duration_ column of the _Problems_ widget. The popup disappears once you remove the mouse from the duration.
  * Click on the duration in the _Duration_ column of the _Problems_ widget. The popup disappears only if you click on the duration again.