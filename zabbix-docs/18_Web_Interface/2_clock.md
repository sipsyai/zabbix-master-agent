---
title: Clock
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/clock
downloaded: 2025-11-14 10:38:01
---

# 2 Clock  
  
#### Overview

In the clock widget, you may display local, server, or specified host time.

Both analog and digital clocks can be displayed:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/clock_analog.png)

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/clock_digital.png)

#### Configuration

To configure, select _Clock_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/clock.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_Time type_ | Select local, server, or specified host time.  
Server time will be identical to the time zone set globally or for the Zabbix user.  
---|---  
_Item_ | Select the item for displaying time. To display host time, use the `system.localtime[local]` [item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent). This item must exist on the host.  
This field is available only when _Host time_ is selected.  
_Clock type_ | Select clock type:  
**Analog** \- analog clock  
**Digital** \- digital clock  
_Show_ | Select information units (date, time, time zone) to display in the digital clock.  
Unit size is dynamic, filling all available widget space based on displayed units, widget size, and display scaling.  
This field is available only if "Digital" is selected in the _Clock type_ field; at least one information unit type must be selected.  
_Advanced configuration_ | Click on the _Advanced configuration_ label to display advanced configuration options for the digital clock.  
This section is available only if "Digital" is selected in the _Clock type_ field.  
  
#### Advanced configuration

Advanced configuration options are available in the collapsible _Advanced configuration_ section, and only for those elements that are selected in the _Show_ field (see above).

Additionally, advanced configuration allows to change the background color for the whole widget.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/clock_advanced.png)

_Background color_ | Select the background color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
---|---  
_**Date**_ |   
_Bold_ | Mark the checkbox to display date in bold type.  
_Color_ | Select the date color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
_**Time**_ |   
_Bold_ | Mark the checkbox to display time in bold type.  
_Color_ | Select the time color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
_Seconds_ | Mark the checkbox to display seconds. Otherwise only hours and minutes will be displayed.  
_Format_ | Select to display a 24-hour or 12-hour time.  
_**Time zone**_ |   
_Bold_ | Mark the checkbox to display time zone in bold type.  
_Color_ | Select the time zone color from the color picker.  
`D` stands for default color (depends on the frontend theme). To return to the default value, click the _Use default_ button in the color picker.  
_Time zone_ | Select the time zone.  
_Format_ | Select to display time zone in short format (e.g. `New York`) or full format (e.g.`(UTC-04:00) America/New York`).