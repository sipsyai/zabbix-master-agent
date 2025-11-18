---
title: Trigger overview
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/trigger_overview
downloaded: 2025-11-14 10:38:28
---

# 30 Trigger overview  
  
#### Overview

In the trigger overview widget, you can display the trigger states for a group of hosts.

  * The trigger states are displayed as colored blocks (the color of the blocks for PROBLEM triggers depends on the problem severity color, which can be adjusted in the [problem update](/documentation/current/en/manual/acknowledgment#updating-problems) screen). Note that recent trigger state changes (within the last 2 minutes) will be displayed as blinking blocks.
  * Gray up and down arrows indicate triggers that have dependencies. On mouseover, dependency details are revealed.
  * A checkbox icon indicates acknowledged problems. All problems or resolved problems of the trigger must be acknowledged for this icon to be displayed.

Clicking on a trigger block provides context-dependent links to problem events of the trigger, the problem acknowledgment screen, trigger configuration, trigger URL or a simple graph/latest values list.

Note that 50 records are displayed by default (configurable in _Administration_ → _General_ → _[GUI](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_ , using the _Max number of columns and rows in overview tables_ option). If more records exist than are configured to display, a message is displayed at the bottom of the table, asking to provide more specific filtering criteria. There is no pagination. Note that this limit is applied first, before any further filtering of data, for example, by tags.

#### Configuration

To configure, select _Trigger overview_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/trigger_overview.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Show_ | Filter triggers by trigger state:  
**Recent problems** \- _(default)_ show triggers that recently have been or still are in a PROBLEM state (resolved and unresolved);  
**Problems** \- show triggers that are in a PROBLEM state (unresolved);  
**Any** \- show all triggers.  
---|---  
_Host groups_ | Select host groups.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Hosts_ | Select hosts.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Problem tags_ | Specify tags to filter the triggers displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
**Note:** If the parameter _Show_ is set to 'Any', all triggers will be displayed even if tags are specified. However, while recent trigger state changes (displayed as blinking blocks) will update for all triggers, the trigger state details (problem severity color and whether the problem is acknowledged) will only update for triggers that match the specified tags.  
  
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
_Show suppressed problems_ | Mark the checkbox to display problems that would otherwise be suppressed (not shown) because of host maintenance.  
_Layout_ | Select the layout option:  
**Horizontal** \- host names will be displayed on the left;  
**Vertical** \- host names will be displayed at the top.