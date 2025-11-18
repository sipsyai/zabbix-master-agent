---
title: Item menu
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/menu/item_menu
downloaded: 2025-11-14 10:37:56
---

# 3 Item menu

#### Overview

The item menu contains shortcuts to actions or frontend sections that are frequently required for an item.

The item menu can be opened by clicking on the item name or the three-dot icon, depending on the frontend section, for example:

_Monitoring_ → [_Latest data_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data)  
  
![](/documentation/current/assets/en/manual/web_interface/item_context_menu_2.png) | _Data Collection_ → _Templates_ → [_Items_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/items)  
  
![](/documentation/current/assets/en/manual/web_interface/item_context_menu_3.png)  
---|---  
  
#### Content

The item menu has three sections: _View_ , _Configuration_ , and _Actions_.

The _View_ section contains the following options:

  * **Latest data** \- opens the [_Latest data_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data) section filtered by the current host and item;
  * **Graph** \- opens a [simple graph](/documentation/current/en/manual/config/visualization/graphs/simple) of the current item;
  * **Values** \- opens the list of all [values](/documentation/current/en/manual/config/visualization/graphs/simple#switching-to-raw-values) received for the current item within the past 60 minutes;
  * **500 latest values** \- opens the list of [500 latest values](/documentation/current/en/manual/config/visualization/graphs/simple#switching-to-raw-values) for the current item.

The _Configuration_ section (available only for _Admin_ and _Super admin_ type users) contains the following options:

  * **Item** \- opens the [item configuration form](/documentation/current/en/manual/config/items/item#configuration) of the current item;
  * **Template** \- opens the [template configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template) of the template that the item belongs to (available only when the item menu is accessed from _Data collection_ → _Templates_ → [_Items_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates/items));
  * **Host** \- opens the [host configuration form](/documentation/current/en/manual/config/hosts/host#configuring-a-host) of the host that the item belongs to;
  * **Triggers** \- on mouseover, opens a list of item's triggers, if any; clicking on a trigger opens its [trigger configuration form](/documentation/current/en/manual/config/triggers/trigger#configuration);
  * **Create trigger** \- opens the [trigger configuration form](/documentation/current/en/manual/config/triggers/trigger#configuration) to create a trigger for this item;
  * **Create dependent item** \- opens the [item configuration form](/documentation/current/en/manual/config/items/item#configuration) to create a dependent item, with the current item as the master item;
  * **Create dependent discovery rule** \- opens the [discovery rule configuration form](/documentation/current/en/manual/discovery/network_discovery/rule) to create a dependent discovery rule, with the current item as the master item.

The _Actions_ section contains the following option:

  * **Execute now** \- [executes a check](/documentation/current/en/manual/config/items/check_now) for a new item value immediately.

#### Supported locations

The item menu is accessible by clicking on an item name in various frontend sections, for example:

  * Monitoring → [Latest data](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data)
  * Data collection → Hosts → [Items](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/items)
  * Data collection → Hosts → Discovery rules → [Item prototypes](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts/discovery/item_prototypes)

The item menu is accessible by clicking on an item value in the [Top items](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/top_items) dashboard widget.