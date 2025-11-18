---
title: Gauge
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge
downloaded: 2025-11-14 10:38:05
---

# 6 Gauge

#### Overview

The gauge widget displays the value of a single item as a gauge.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge.png)

When configured, the widget can consist of the following elements:

  * Item description (for example, "CPU utilization", "Speed")
  * Item value (for example, "30.70", "19.80")
  * Item value units (for example, "%", "km/h")
  * Gauge scale (for example, "0%/100%", "0/100/180/200")
  * Gauge arc (gauge value arc and gauge thresholds arc)
  * Gauge needle

The widget can be visually fine-tuned using the advanced configuration options to create a wide variety of visual styles:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge_styles.png)

The gauge widget can display only numeric values. Displaying binary values is not supported.

Clicking on the gauge widget leads to a graph for the item.

#### Configuration

To configure, select _Gauge_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge_configuration.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Item_ | Select the item.  
Alternatively, select a compatible widget as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for items.  
This field is auto-complete, so starting to type the name of an item will offer a dropdown of matching items.  
Note that you can select only items that return [numeric](/documentation/current/en/manual/config/items/item#configuration) data.  
---|---  
_Min_ | Enter the minimum value of the gauge.  
[Suffixes](/documentation/current/en/manual/appendix/suffixes) (for example, "1d", "2w", "4K", "8G") are supported. [Value mappings](/documentation/current/en/manual/config/items/mapping) are supported.  
_Max_ | Enter the maximum value of the gauge.  
[Suffixes](/documentation/current/en/manual/appendix/suffixes) (for example, "1d", "2w", "4K", "8G") are supported. [Value mappings](/documentation/current/en/manual/config/items/mapping) are supported.  
_Colors_ | Select the color from the color picker:  
**Value arc** \- select the gauge value arc color;  
**Arc background** \- select the gauge value arc and gauge thresholds arc background color;  
**Background** \- select the widget background color.  
  
"D" stands for the default color, which depends on the frontend theme. If _Thresholds_ are set, the default color for **Value arc** depends on the threshold color. To return to the default color, click the _Use default_ button in the color picker.  
_Show_ | Mark the checkbox to display the respective gauge element - description, value, value arc, needle, scale (the minimum and maximum value of the gauge at the beginning and end of the gauge arc). Unmark to hide. At least one element must be selected.  
  
Note that the gauge needle and scale can be displayed if the gauge value arc or gauge thresholds arc (see advanced configuration options) is displayed. Also note that if the gauge needle is displayed, the value is placed under the needle; if the needle is hidden, the value is aligned with the bottom of the gauge arc.  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
_Advanced configuration_ | Click the _Advanced configuration_ label to display advanced configuration options. This is also where you'll be able to adjust the gauge elements selected in the _Show_ field.  
  
##### Advanced configuration

Advanced configuration options are available in the collapsible _Advanced configuration_ section:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge_advanced_configuration.png)

_Angle_ | Select the gauge angle (180° or 270°).  
---|---  
**_Description_**  
_Description_ | Enter the item description. This description may override the default item name.  
Multiline descriptions are supported. A combination of text and supported macros is possible.  
{HOST.*}, {ITEM.*}, {INVENTORY.*} and user macros are supported.  
_Size_ | Enter the font size height for the item description (in percent, relative to the total widget height).  
_Vertical position_ | Select the vertical position of the item description (top or bottom, relative to the gauge arc).  
_Bold_ | Mark the checkbox to display the item description in bold.  
_Color_ | Select the item description color from the color picker.  
"D" stands for the default color, which depends on the frontend theme. To return to the default color, click the _Use default_ button in the color picker.  
**_Value_**  
_Decimal places_ | Enter the number of decimal places to display with the value.  
This option affects only items that return [numeric (float)](/documentation/current/en/manual/config/items/item#configuration) data.  
_Size_ | Enter the font size height for the value (in percent, relative to the gauge arc height).  
_Bold_ | Mark the checkbox to display the value in bold.  
_Color_ | Select the value color from the color picker.  
"D" stands for the default color, which depends on the frontend theme. To return to the default color, click the _Use default_ button in the color picker.  
**_Units_**  
_Units_ | Mark the checkbox to display units with the item value.  
If you enter a unit name, it will override the units set in the [item configuration](/documentation/current/en/manual/config/items/item#configuration).  
_Size_ | Enter the font size height for the item units (in percent, relative to the gauge arc height).  
_Bold_ | Mark the checkbox to display item units in bold.  
_Position_ | Select the position of the item units (above, below, before or after, relative to the item value).  
This option is ignored for the following [time-related units](/documentation/current/en/manual/config/items/item#configuration): unixtime, uptime, s.  
_Color_ | Select the item units color from the color picker.  
"D" stands for the default color, which depends on the frontend theme. To return to the default color, click the _Use default_ button in the color picker.  
**_Value arc_**  
_Arc size_ | Enter the size height of the gauge value arc (in percent, relative to the gauge arc radius).  
**_Needle_**  
_Color_ | Select the gauge needle color from the color picker.  
"D" stands for the default color, which depends on the frontend theme. If _Thresholds_ are set, the default color for the needle depends on the threshold color. To return to the default color, click the _Use default_ button in the color picker.  
**_Scale_**  
_Show units_ | Mark the checkbox to display units with the minimum and maximum value of the gauge.  
_Size_ | Enter the font size height for the minimum and maximum value of the gauge (in percent, relative to the gauge arc height).  
_Decimal places_ | Enter the number of decimal places to display with the minimum and maximum value of the gauge.  
This option affects only items that return [numeric (float)](/documentation/current/en/manual/config/items/item#configuration) data.  
**_Thresholds_**  
_Thresholds_ | Click _Add_ to add a threshold, select a threshold color from the color picker, and specify a numeric value.  
The thresholds list will be sorted in ascending order when saved.  
Note that the colors configured as thresholds will be displayed correctly only for numeric items.  
[Suffixes](/documentation/current/en/manual/appendix/suffixes) (for example, "1d", "2w", "4K", "8G") are supported. [Value mappings](/documentation/current/en/manual/config/items/mapping) are supported.  
_Show labels_ | Mark the checkbox to display threshold values as labels on the gauge scale.  
_Show arc_ | Mark the checkbox to display the gauge thresholds arc.  
_Arc size_ | Enter the size height of the gauge thresholds arc (in percent, relative to the gauge arc radius).  
  
The information displayed by the gauge widget can be downloaded as a _.png_ image using the [widget menu](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#widget-menu):

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/gauge_download.png)

A screenshot of the widget will be saved to the _Downloads_ folder.