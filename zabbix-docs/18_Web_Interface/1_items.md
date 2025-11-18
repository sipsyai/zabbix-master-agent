---
title: Items
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/items
downloaded: 2025-11-14 10:38:58
---

# 1 Items

#### Overview

The item list for a template can be accessed from _Data collection → Templates_ by clicking on _Items_ for the respective template.

A list of existing items is displayed.

![](/documentation/current/assets/en/manual/web_interface/template_items.png)

Displayed data:

_Item menu_ | Click on the three-dot icon to open the [item menu](/documentation/current/en/manual/web_interface/menu/item_menu).  
---|---  
_Template_ | Template the item belongs to.  
Clicking on the template name opens the template [configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template).  
This column is displayed only if multiple templates or no templates are selected in the filter.  
_Name_ | Name of the item displayed as a blue link to item details.  
Clicking on the item name link opens the item [configuration form](/documentation/current/en/manual/config/items/item#configuration).  
If the item is inherited from another template, the template name is displayed before the item name as a gray link. Clicking on the template link opens the item list on that template level.  
_Triggers_ | Moving the mouse over Triggers will display an infobox displaying the triggers associated with the item.  
The number of the triggers is displayed in gray.  
_Key_ | Item key is displayed.  
_Interval_ | Frequency of the check is displayed.  
_History_ | How many days item data history will be kept is displayed.  
_Trends_ | How many days item trends history will be kept is displayed.  
_Type_ | Item type is displayed (Zabbix agent, SNMP agent, simple check, etc).  
_Status_ | Item status is displayed - _Enabled_ or _Disabled_. By clicking on the status you can change it - from Enabled to Disabled (and back).  
_Tags_ | Item tags are displayed.  
Up to three tags (name:value pairs) can be displayed. If there are more tags, a "..." link is displayed that allows to see all tags on mouseover.  
  
To configure a new item, click on the _Create item_ button at the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change item status to _Enabled_.
  * _Disable_ \- change item status to _Disabled_.
  * _Copy_ \- copy the items to other hosts or templates.
  * _Mass update_ \- [update several properties](/documentation/current/en/manual/config/items/itemupdate) for a number of items at once.
  * _Delete_ \- delete the items.

To use these options, mark the checkboxes before the respective items, then click on the required button.

##### Using filter

The item list may contain a lot of items. By using the filter, you can filter out some of them to quickly locate the items you'ŗe looking for. For better search performance, data is searched with macros unresolved.

The _Filter_ icon is available at the upper-right corner. Clicking on it will open a filter where you can specify the desired filtering criteria.

![](/documentation/current/assets/en/manual/web_interface/template_item_filter.png)

_Template groups_ | Filter by one or more template groups.  
Specifying a parent template group implicitly selects all nested groups.  
---|---  
_Templates_ | Filter by one or more templates.  
_Name_ | Filter by item name.  
_Key_ | Filter by item key.  
_Value mapping_ | Filter by the value map used.  
This parameter is not displayed if the _Templates_ option is empty.  
_Type_ | Filter by item type (Zabbix agent, SNMP agent, etc.).  
_Type of information_ | Filter by type of information (Numeric unsigned, float, etc.).  
_History_ | Filter by how long item history is kept.  
_Trends_ | Filter by how long item trends are kept.  
_Update interval_ | Filter by item update interval.  
_Tags_ | Specify tags to limit the number of items displayed. It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
There are several operators available for each condition:  
**Exists** \- include the specified tag names  
**Equals** \- include the specified tag names and values (case-sensitive)  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
**Does not exist** \- exclude the specified tag names  
**Does not equal** \- exclude the specified tag names and values (case-sensitive)  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive)  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition  
**Or** \- enough if one condition is met  
_Status_ | Filter by item status - _Enabled_ or _Disabled_.  
_Triggers_ | Filter items with (or without) triggers.  
_Inherited_ | Filter items inherited (or not inherited) from linked templates.  
  
##### Using subfilter

The subfilter allows to further modify the filtering from the main filter.

It contains clickable links for a quick access to related items. Items are related by common entity - tag, item type, item update interval, etc. When an entity is clicked, the entity is highlighted with a gray background, and items are immediately filtered (no need to click _Apply_ in the main filter). Clicking another entity adds it to the filtered results. Clicking the entity again removes the filtering.

![](/documentation/current/assets/en/manual/web_interface/template_item_subfilter.png)

Subfilters are generated based on the filtered data, which is limited to 1000 records. If you want to see more records in the subfilter, you need to increase the value of _Limit for search and filter results_ parameter (in _Administration_ -> _General_ -> _[GUI](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_).

Unlike the main filter, the subfilter is updated with each table refresh request to always have up-to-date information of available filtering options and their counter numbers.

The number of entities displayed is limited to 100 horizontally. If there are more, a three-dot icon is displayed at the end; it is not clickable.

A number next to each clickable entity indicates the number of items grouped in it (based on the results of the main filter). When an entity is clicked, the numbers with other available entities are displayed with a plus sign indicating how many items may be added to the current selection. Entities without items are not displayed unless selected in the subfilter before.