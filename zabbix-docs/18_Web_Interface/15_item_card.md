---
title: Item card
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card
downloaded: 2025-11-14 10:38:13
---

# 15 Item card  
  
#### Overview

The Item card widget provides comprehensive and customizable information about a single item.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card.png)

The item can be set directly in the widget configuration or selected from a compatible widget on the dashboard.

The widget can display multiple sections, each showing different type of information (item description, latest data, etc.). Section layout automatically adjusts based on widget width. When expanded horizontally, sections are rearranged into multiple columns, ordered left to right across each row.

#### Configuration

To configure, select _Item card_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card_configuration.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Item_ | Select the item.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for items.  
Matching suggestions appear as you type.  
  
The top section of the widget always displays the **item name** (clicking it opens the [item menu](/documentation/current/en/manual/web_interface/menu/item_menu)):  
\- If the item is disabled, a red _Disabled_ label is displayed next to the item name.  
\- In case of errors, a square icon with the letter "i" is displayed. In case of problems, a square icon with the problem count is displayed for each problem severity. Hovering over an icon opens a pop-up with details.  
\- On a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), the technical name (instead of visible name) of the item is displayed.  
  
The top section of the widget also displays the **item path** —its host and, if applicable, template, low-level discovery (LLD) rule, or master item (clicking an entity opens its configuration).  
Item path is displayed only to users with permissions to the respective entities.  
---|---  
_Show_ | Add sections to display in the widget. Sections can be rearranged by dragging and dropping.  
| _Description_ | Displays item description. Macros are resolved.  
_Error text_ | Displays item error (if any).  
_Metrics_ | Displays the following information:  
\- Item update interval (except for [trapper items](/documentation/current/en/manual/config/items/itemtypes/trapper));  
\- Item history configuration (if any);  
\- Item trends configuration (if any).  
Macros are resolved.  
  
If the item uses [custom intervals](/documentation/current/en/manual/config/items/item/custom_intervals), a help icon is displayed next to item update interval. Hovering over the icon opens a pop-up with custom interval details.  
_Latest data_ | Displays the following information:  
\- Time since last item check;  
\- Item last value;  
\- Link to [simple graph/history](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data#graphs-and-history) of item values (if history or trends are stored);  
\- Configurable sparkline chart (if item is numeric).  
  
For binary type items, a thumbnail or the _Show_ option is displayed instead of last value. Hovering over the thumbnail opens a pop-up with the image. Hovering over _Show_ opens a pop-up with the item value (Base64 string).  
  
On a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), _No data_ is displayed instead of item last value.  
_Type of information_ | Displays item type of information.  
_Triggers_ | Displays the following information:  
\- _Triggers_ label with trigger count (hovering over _Triggers_ opens a pop-up with trigger details);  
\- List of trigger names (macros are resolved).  
_Host interface_ | Displays host interface used by the item, or _No data_ if the item does not have a host interface (e.g., dependent items, simple checks).  
  
On a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards), _No data_ is displayed.  
_Type_ | Displays item type.  
_Host inventory_ | Displays host inventory field that item value populates.  
_Tags_ | Displays item tags.  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
  
##### Sparkline

Sparkline chart configuration options are available only if the _Latest data_ section is added to the widget.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card_sparkline.png)

_Width_ | Set the graph line thickness by using the slider or manually entering a value in the range from 0 to 10.  
---|---  
_Color_ | Select line and fill color.  
_Fill_ | Set fill color transparency level by using the slider or manually entering a value in the range from 0 to 10.  
_Time period_ | Select the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#dynamic-parameters) for the time period:  
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
_History data_ | Take data from history or trends:  
**Auto** \- automatic selection;  
**History** \- take history data;  
**Trends** \- take trend data.  
This parameter applies only to numeric data. Non-numeric data will always be taken from history.