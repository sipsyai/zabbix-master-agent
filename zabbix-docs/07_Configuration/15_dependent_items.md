---
title: Dependent items
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/dependent_items
downloaded: 2025-11-14 10:35:16
---

# 15 Dependent items

#### Overview

There are situations when one item gathers multiple metrics at a time or it even makes more sense to collect related metrics simultaneously, for example:

  * CPU utilization of individual cores
  * Incoming/outgoing/total network traffic

To allow for bulk metric collection and simultaneous use in several related items, Zabbix supports dependent items. Dependent items depend on the master item that collects their data simultaneously, in one query. A new value for the master item automatically populates the values of the dependent items. Dependent items cannot have a different update interval than the master item.

Zabbix preprocessing options can be used to extract the part that is needed for the dependent item from the master item data.

Preprocessing is managed by a `preprocessing manager` process, along with worker threads that perform the preprocessing steps. All values with preprocessing (before Zabbix 7.4.1, all values), received from different data gatherers, pass through the preprocessing manager before being added to the history cache. Socket-based IPC communication is used between data gatherers (pollers, trappers, etc) and the preprocessing process.

Zabbix server or Zabbix proxy (if host is monitored by proxy) are performing preprocessing steps and processing dependent items.

Items of any type, even dependent items, can be set as master items. Additional levels of dependent items can be used to extract smaller parts from the value of an existing dependent item.

##### Limitations

  * Only same host (template) dependencies are allowed
  * An item prototype can depend on another item prototype or regular item from the same host
  * Dependent item on a host with master item from template will not be exported to XML

#### Item configuration

A dependent item depends on its master item for data. That is why the **master item** must be configured (or exist) first:

  * Go to: _Data collection_ → _Hosts_
  * Click on _Items_ in the row of the host
  * Click on _Create item_
  * Enter parameters of the item in the form

![](/documentation/current/assets/en/manual/config/items/itemtypes/master_item.png)

All mandatory input fields are marked with a red asterisk.

Click on _Add_ to save the master item.

Then you can configure a **dependent item**.

![](/documentation/current/assets/en/manual/config/items/itemtypes/dependent_item.png)

All mandatory input fields are marked with a red asterisk.

The fields that require specific information for dependent items are:

_Type_ | Select **Dependent item** here.  
---|---  
_Key_ | Enter a key that will be used to recognize the item.  
_Master item_ | Select the master item. Master item value will be used to populate dependent item value.  
_Type of information_ | Select the type of information that will correspond the format of data that will be stored.  
  
You may use item value [preprocessing](/documentation/current/en/manual/config/items/item#item-value-preprocessing) to extract the required part of the master item value.

![](/documentation/current/assets/en/manual/config/items/itemtypes/dependent_item_preprocessing.png)

Without preprocessing, the dependent item value will be exactly the same as the master item value.

Click on _Add_ to save the dependent item.

A shortcut to creating a dependent item quicker can be accessed by clicking on the ![](/documentation/current/assets/en/manual/config/items/itemtypes/dependent_item_button.png) button in the item list and selecting _Create dependent item_.

![](/documentation/current/assets/en/manual/config/items/itemtypes/dependent_item_menu.png)

##### Display

In the item list dependent items are displayed with their master item name as prefix.

![](/documentation/current/assets/en/manual/config/items/itemtypes/dependent_items.png)

If a master item is deleted, so are all its dependent items.