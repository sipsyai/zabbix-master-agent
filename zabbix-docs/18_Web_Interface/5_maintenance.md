---
title: Maintenance
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/data_collection/maintenance
downloaded: 2025-11-14 10:39:09
---

# 5 Maintenance

#### Overview

In the _Data collection → Maintenance_ section users can configure and maintain maintenance periods for hosts.

A listing of existing maintenance periods with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/maintenance_periods1.png)

Displayed data:

_Name_ | Name of the maintenance period. Clicking on the maintenance period name opens the maintenance period [configuration form](/documentation/current/en/manual/maintenance#configuration).  
---|---  
_Type_ | The type of maintenance is displayed: _With data collection_ or _No data collection_  
_Active since_ | The date and time when executing maintenance periods becomes active.  
Note: This time does not activate a maintenance period; maintenance periods need to be set separately.  
_Active till_ | The date and time when executing maintenance periods stops being active.  
_State_ | The state of the maintenance period:  
**Approaching** \- will become active soon  
**Active** \- is active  
**Expired** \- is not active any more  
_Description_ | Description of the maintenance period is displayed.  
  
To configure a new maintenance period, click on the _Create maintenance period_ button in the upper-right corner.

##### Mass editing options

A button below the list offers one mass-editing option:

  * _Delete_ \- delete the maintenance periods

To use this option, mark the checkboxes before the respective maintenance periods and click on _Delete_.

##### Using filter

You can use the filter to display only the maintenance periods you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of maintenance periods. If you click on it, a filter becomes available where you can filter maintenance periods by host group, name and state.

![](/documentation/current/assets/en/manual/web_interface/maintenance_filter1.png)

#### Calculation of queues during maintenance

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.