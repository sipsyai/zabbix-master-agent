---
title: Item navigator
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_navigator
downloaded: 2025-11-14 10:38:15
---

# 17 Item navigator  
  
#### Overview

The item navigator widget displays items based on various filtering and grouping options.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_navigator.png)

The widget also allows to control the information displayed in other widgets based on the selected item.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_navigator_control.png)

Groups by which items are organized can be expanded or collapsed.

For groups and problems, additional details are accessible by mouseover hints.

#### Configuration

To configure, select _Item navigator_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/item_navigator_configuration.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Host groups_ | Select host groups.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for host groups.  
This field is auto-complete, so starting to type the name of a group will offer a dropdown of matching groups.  
Selecting a parent host group implicitly selects all nested host groups; if no host groups are selected, the widget will display items belonging to all hosts from all host groups.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
---|---  
_Hosts_ | Select hosts.  
Alternatively, select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This field is auto-complete, so starting to type the name of a host will offer a dropdown of matching hosts.  
If no hosts are selected, the widget will display items belonging to all hosts.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Host tags_ | Specify tags to filter the items displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set.  
Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Item patterns_ | Enter item patterns or select existing items as item patterns. Items that match the specified patterns will be displayed on the item navigator.  
  
Wildcard patterns may be used for selection (for example, `*` will return items that match zero or more characters; `Zabbix*` will return items that start with "Zabbix").  
To specify a wildcard pattern, enter the string manually and press _Enter_. When you start typing, a dropdown list will show matching items limited to those belonging to selected _Hosts_ or hosts within selected _Host groups_ , if any. The wildcard symbol is always interpreted, therefore, it is not possible to add, for example, an item named _item*_ individually, if there are other matching items (e.g., item2, item3).  
  
When configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), this parameter allows selecting only [items configured on the template](/documentation/current/en/manual/config/templates/template#adding-items-triggers-graphs).  
_Item tags_ | Specify tags to filter the items displayed in the widget.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set.  
Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
_State_ | Filter which items to display based on their state (all, normal, not supported).  
_Show problems_ | Filter which problems to display with items based on their status (all, unsuppressed, none).  
_Group by_ | Add a grouping attribute by which to group items:  
**Host group** \- group items by host groups of their hosts;  
**Host name** \- group items by their hosts;  
**Host tag value** \- enter a tag name to group items by the values of this host tag (for example, enter "city" to group items by values "Riga", "Tokyo", etc.);  
**Item tag value** \- enter a tag name to group items by the values of this item tag (for example, enter "component" to group items by values "cpu", "memory", etc.).  
  
Grouping attributes can be reordered by dragging up or down by the handle before the group name. Note that grouping attribute order determines group nesting order. For example, specifying multiple host tag names (1: color, 2: city) will result in items being grouped by color (red, blue, etc.) and then by city (Riga, Tokyo, etc.).  
  
An item may be displayed in multiple groups depending on the configured grouping attributes (for example, when grouping by host group and the item's host belongs to multiple host groups). Clicking such items selects and highlights them in all groups.  
Items that do not match the configured grouping attributes are displayed in the _Uncategorized_ group.  
  
If _Show problems_ is configured to display problems, they are displayed as follows:  
\- for each group, all subordinate item problem count is displayed;  
\- for each item, only its problem count is displayed.  
  
Up to 10 grouping attributes can be specified, and all must be unique.  
If no grouping attributes are specified, items will not be grouped.  
_Item limit_ | Enter the maximum number of items to be displayed. Possible values range from 1-9999.  
  
When more items are available for displaying than the set limit, a corresponding message is shown below the displayed items (for example, "100 of 100+ items are shown").  
Note that the configured item limit also affects the display of configured groups; for example, if item limit is set to 100 and items are grouped by their hosts (each containing 200 items), only the first host with its 100 items will be displayed in the widget.  
  
This parameter is not affected by the _Limit for search and filter results_ parameter in _Administration_ → _General_ → [_GUI_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui).