---
title: Host dashboards
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts/dashboards
downloaded: 2025-11-14 10:38:36
---

# 2 Host dashboards

#### Overview

Host dashboards look similar to [global dashboards](/documentation/current/en/manual/web_interface/frontend_sections/dashboards); however, host dashboards lack an [owner](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#creating-a-dashboard) and display data only for the selected host.

![](/documentation/current/assets/en/manual/config/visualization/host_dashboards.png)

When viewing host dashboards, you can switch between the configured dashboards by clicking:

  * the dashboard tabs;
  * the ![](/documentation/current/assets/en/manual/config/visualization/arrow_left.png) ![](/documentation/current/assets/en/manual/config/visualization/arrow_right.png) arrow buttons under the header;
  * the ![](/documentation/current/assets/en/manual/config/visualization/arrow_down.png) arrow button under the header, which will display the full list of host dashboards available.

To switch to the _Monitoring → Hosts_ section, click the _All hosts_ navigation link under the header in the upper-left corner.

#### Configuration

Host dashboards are configured at the [template](/documentation/current/en/manual/config/templates/template#adding-dashboards) level. Once a template is linked to a host, host dashboards are generated for that host. Note that host dashboards _cannot_ be configured in the [_Dashboards_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards) section, which is reserved for global dashboards.

Widgets of host dashboards can also be configured only at the [template](/documentation/current/en/manual/config/templates/template#adding-dashboards) level, except for changing the [refresh interval](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters). Moreover, widgets of host dashboards can only be copied to other host dashboards within the same template. Note that widgets from global dashboards _cannot_ be copied to host dashboards.

Host dashboards used to be host screens before Zabbix 5.2. When importing an older template that contains screens, the screen import will be ignored.

#### Access

Host dashboards can be accessed:

  * after searching for a host name in [global search](/documentation/current/en/manual/web_interface/global_search) (click the _Dashboards_ link provided in the search results);
  * after clicking a host name in _Inventory →[Hosts](/documentation/current/en/manual/web_interface/frontend_sections/inventory/hosts)_ (click the _Dashboards_ link provided in the host overview);
  * from the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu) by clicking _Dashboards_.

![](/documentation/current/assets/en/manual/config/visualization/host_menu_dashboards.png)

Note that host dashboards _cannot_ be directly accessed in the _[Dashboards](/documentation/current/en/manual/web_interface/frontend_sections/dashboards)_ section, which is reserved for global dashboards.