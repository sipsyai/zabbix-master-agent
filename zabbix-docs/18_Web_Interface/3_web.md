---
title: Web scenarios
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts/web
downloaded: 2025-11-14 10:38:37
---

# 3 Web scenarios

#### Overview

Host [web scenario](/documentation/current/en/manual/web_monitoring) information can be accessed from _Monitoring → Hosts_ by clicking on Web for the respective host.

![](/documentation/current/assets/en/manual/web_interface/web_monitoring.png)

Clicking on the host name brings up the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu). Data of disabled hosts is also accessible. The name of a disabled host is listed in red.

The maximum number of scenarios displayed per page depends on the _Rows per page_ user profile [setting](/documentation/current/en/manual/web_interface/user_profile#user-profile).

By default, only values that fall within the last 24 hours are displayed. This limit has been introduced with the aim of improving initial loading times for large pages of latest data. You can extend this time period by changing the value of _Max history display period_ parameter in the _[Administration → General → GUI](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#gui)_ menu section.

The scenario name is link to more detailed statistics about it:

![](/documentation/current/assets/en/manual/web_monitoring/scenario_details2.png)

##### Using filter

The page shows a list of all web scenarios of the selected host. To view web scenarios for another host or host group without returning to the _Monitoring → Hosts_ page, select that host or group in the filter. You may also filter scenarios based on tags.

##### Buttons

View mode buttons being common for all sections are described on the [Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring#view-mode-buttons) page.