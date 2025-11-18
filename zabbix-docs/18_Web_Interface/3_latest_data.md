---
title: Latest data
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data
downloaded: 2025-11-14 10:38:38
---

# 3 Latest data

#### Overview

The _Monitoring_ → _Latest data_ section displays the latest values gathered by items.

This section contains the following elements:

  * Filter
  * Subfilter
  * Item list

The subfilter and item list is displayed only if the filter is set and there are results to display.

![](/documentation/current/assets/en/manual/web_interface/latest_data.png)

_Host_ | Name of the host to which the item belongs.  
Clicking on the name brings up the [host context menu](/documentation/current/en/manual/web_interface/menu/host_menu).  
If a host is in maintenance, an orange wrench ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/configuration/maintenance_wrench_icon.png) icon is displayed after the host's name.  
If a host is disabled, the name of the host is displayed in red. Note that data of disabled hosts (including graphs and item value lists) is accessible in the _Latest data_ section.  
---|---  
_Name_ | Name of the item.  
Clicking on the name brings up the [item menu](/documentation/current/en/manual/web_interface/menu/item_menu).  
A question mark ![](/documentation/current/assets/en/manual/web_interface/item_description_icon.png) icon is displayed next to the item name for all items that have a description. Hover over the icon to display a tooltip with the item description.  
_Last check_ | Time since the last item check.  
_Last value_ | Most recent value for the item.  
Values are displayed with unit conversion and value mapping applied. Hover over the value to display raw data.  
By default, only values received in the last 24 hours are displayed. This limit improves initial loading times for large pages of latest data; to extend it, update the value of the _Max history display period_ parameter in _Administration_ → _General_ → [_GUI_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui).  
_Change_ | Difference between the previous value and the most recent value.  
For items with an update frequency of 1 day or more, the change amount will never be displayed (with the default setting). In this case, the last value will not be displayed at all if it was received more than 24 hours ago.  
_Tags_ | Tags associated with the item.  
Tags in the item list are clickable. Clicking a tag enables in the subfilter, making the item list display only items containing this tag (and any other tags previously selected in the subfilter). Note that once items have been filtered this way, tags in the item list are no longer clickable. Further modification based on tags (for example, to remove tags or specify other filters) must be done in the subfilter.  
_Graph/History_ | Link to simple graph/history of item values.  
_Info_ | Additional information about the item.  
If an item has errors (for example, has become unsupported), an information ![](/documentation/current/assets/en/manual/web_interface/info_icon.png) icon is displayed. Hover over the icon for details.  
  
##### Buttons

View mode buttons being common for all sections are described on the [Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons) page.

##### Mass actions

Buttons below the list offer mass actions with one or several selected items:

  * _Display stacked graph_ \- display a stacked [ad-hoc graph](/documentation/current/en/manual/config/visualization/graphs/adhoc).
  * _Display graph_ \- display a simple [ad-hoc graph](/documentation/current/en/manual/config/visualization/graphs/adhoc).
  * _Execute now_ \- execute a check for new item values immediately. Supported for **passive** checks only (see [more details](/documentation/current/en/manual/config/items/check_now)). This option is available only for hosts with read-write access. Accessing this option for hosts with read-only permissions depends on the [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) option called _Invoke "Execute now" on read-only hosts_.

To use these options, mark the checkboxes before the respective items, then click on the required button.

#### Using filter

You can use the filter to display only the items you are interested in. For better search performance, data is searched with macros unresolved.

The filter ![](/documentation/current/assets/en/manual/web_interface/icon_filter_collapsed.png) icon is located above the item list and the subfilter. Click it to expand the filter.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/latest_data_filter.png)

The filter allows to narrow the item list by host group, host, item name, tag, state and other settings. Specifying a parent host group in the filter implicitly selects all nested host groups. See _Monitoring_ → _[Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#using-filter)_ for details on filtering by tags.

The _Show details_ filter option allows to extend the information displayed for the items. Mark it to display such details as the item refresh interval, history and trends settings, item type, and item errors (fine/unsupported).

##### Saving filter

Favorite filter settings can be saved as tabs and then quickly accessed by clicking on the respective tab above the filter.

See more details about [saving filters](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#tabs-for-favorite-filters).

#### Using subfilter

The subfilter allows to further modify the filtering from the main filter.

It contains clickable links for a quick access to related items. Items are related by common entity - host, tag name or value, item state, or data status. When an entity is clicked, the entity is highlighted with a gray background, and items are immediately filtered (no need to click _Apply_ in the main filter). Clicking another entity adds it to the filtered results. Clicking the entity again removes the filtering.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/latest_data_subfilter.png)

Subfilters are generated based on the filtered data, which is limited to 1000 records. If there are 20 hosts each having 100 items (so 2000 records in total), only half of the hosts will be visible in the subfilter. If you want to see more records in the subfilter, you need to increase the value of _Limit for search and filter results_ parameter (in _Administration_ -> _General_ -> _[GUI](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_).

Unlike the main filter, the subfilter is updated with each table refresh request to always have up-to-date information of available filtering options and their counter numbers.

For each entity group (hosts, tags, tag values, etc.), up to 10 rows of entities are displayed. If there are more entities, this list can be expanded to display a maximum of 1000 entries (the value of SUBFILTER_VALUES_PER_GROUP in [frontend definitions](/documentation/current/en/manual/web_interface/definitions)) by clicking the three-dot ![](/documentation/current/assets/en/manual/web_interface/icon_subfilter_expand.png) icon at the end of the list. For _Tag values_ , the list can be expanded to display a maximum of 200 tag names with their corresponding values. Note that once fully expanded, the list cannot be collapsed.

A number next to each clickable entity indicates the number of items grouped in it (based on the results of the main filter). When an entity is clicked, the numbers with other available entities are displayed with a plus sign indicating how many items may be added to the current selection. Entities without items are not displayed unless selected in the subfilter before.

#### Graphs and history

The _Graph/History_ column in the item list offers the following links:

  * **History** \- for all textual items, leading to listings (_Values/500 latest values_) displaying the history of previous item values.
  * **Graph** \- for all numeric items, leading to a [simple graph](/documentation/current/en/manual/config/visualization/graphs/simple). Note that when the graph is displayed, a dropdown on the upper right offers a possibility to switch to _Values/500 latest values_ as well.

![](/documentation/current/assets/en/manual/web_interface/latest_values.png)

The values displayed in this list are raw, that is, no postprocessing is applied.

The total amount of values displayed is defined by the value of _Limit for search and filter results_ parameter, set in _Administration_ → _General_ → [_GUI_](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui).