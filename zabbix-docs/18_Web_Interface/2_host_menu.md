---
title: Host menu
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/menu/host_menu
downloaded: 2025-11-14 10:37:55
---

# 2 Host menu

#### Overview

The host menu contains shortcuts to actions or frontend sections that are frequently required for a host.

The host menu can be opened by clicking on the host name or the three dots icon, depending on the frontend section, for example:

_Monitoring_ → [_Latest data_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data)  
  
![](/documentation/current/assets/en/manual/web_interface/host_context_menu.png) | _Data collection_ → [_Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts)  
  
![](/documentation/current/assets/en/manual/web_interface/host_context_menu_02.png)  
---|---  
  
#### Content

The host context menu has four sections: _View_ , _Configuration_ , _Links_ , and _Scripts_. For the entities that are not configured, links are disabled and displayed in gray color. The sections _Scripts_ and _Links_ are displayed if their entities are configured.

_View_ section contains links to:

  * **Dashboards** \- opens widgets and graphs.
  * **Problems** \- opens the _Problems_ section with the list of unresolved problems of the underlying trigger.
  * **Latest data** \- opens the _Latest data_ section with the list of all the latest data of the current host.
  * **Graphs** \- opens simple graphs of the current host.
  * **Web** \- opens the link to the configured web scenarios.
  * **Inventory** \- opens the link to the inventory of the current host.

_Configuration_ section contains links to:

  * **Host Wizard** \- opens [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard) for the current host (disabled for discovered hosts).
  * **Host** \- configuration form of the current host.
  * **Items** \- the list of the current host items.
  * **Triggers** \- the list of the current host triggers.
  * **Graphs** \- simple graphs of the current host.
  * **Discovery** \- the list of low-level discovery rules of the current host.
  * **Web** \- the list of web scenarios of the current host.

Note that configuration section is available only for Admin and Super admin users.

_Links_ section contains links to:

  * access a configured [trigger URL](/documentation/current/en/manual/config/triggers/trigger#configuration).
  * access custom links configured in [Global scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) (with scope _Manual host action_ and type 'URL').

_Scripts_ section allows to execute [global scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) configured for the current host. These scripts need to have their scope defined as _Manual host action_ to be available in the host menu.

#### Supported locations

The host menu is accessible by clicking on a host name in various frontend sections, for example:

  * Dashboards [widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets), such as Problems, Top items, Trigger overview, etc.
  * Monitoring → [Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems)
  * Monitoring → [Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems) → Event details
  * Monitoring → [Hosts](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts)
  * Monitoring → Hosts → [Web Monitoring](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts/web)
  * Monitoring → [Latest data](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data)
  * Monitoring → [Maps](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/maps)
  * Inventory → [Hosts](/documentation/current/en/manual/web_interface/frontend_sections/inventory/hosts)
  * Reports → [Top 100 triggers](/documentation/current/en/manual/web_interface/frontend_sections/reports/triggers_top)

The host menu is accessible by clicking on the three dots icon in Data collection → [Hosts](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts).