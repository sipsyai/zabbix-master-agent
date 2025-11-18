---
title: Inventory
source: https://www.zabbix.com/documentation/current/en/manual/config/hosts/inventory
downloaded: 2025-11-14 10:34:38
---

# 4 Inventory

#### Overview

You can keep the inventory of networked devices in Zabbix.

There is a special _Inventory_ menu in the Zabbix frontend. However, you will not see any data there initially and it is not where you enter data. Building inventory data is done manually when configuring a host or automatically by using some automatic population options.

#### Building inventory

##### Manual mode

When [configuring a host](host), in the _Inventory_ tab you can enter such [details](/documentation/current/en/manual/api/reference/host/object#host-inventory) as the type of device, serial number, location, responsible person, URLs, etc. - data that will populate inventory information.

If a URL is included in host inventory information and it starts with 'http' or 'https', it will result in a clickable link in the _Inventory_ section.

##### Automatic mode

Host inventory can also be populated automatically. For that to work, when configuring a host the inventory mode in the _Inventory_ tab must be set to _Automatic_.

Then you can [configure host items](/documentation/current/en/manual/config/items/item) to populate any host inventory field with their value, indicating the destination field with the respective attribute (called _Item will populate host inventory field_) in item configuration.

Items that are especially useful for automated inventory data collection:

  * system.hw.chassis[full|type|vendor|model|serial] - default is [full], root permissions needed
  * system.hw.cpu[all|cpunum,full|maxfreq|vendor|model|curfreq] - default is [all,full]
  * system.hw.devices[pci|usb] - default is [pci]
  * system.hw.macaddr[interface,short|full] - default is [all,full], interface is regexp
  * system.sw.arch
  * system.sw.os[name|short|full] - default is [name]
  * system.sw.packages[regexp,manager,short|full] - default is [all,all,full]

##### Inventory mode selection

Inventory mode can be selected in the host configuration form.

Inventory mode by default for new hosts is selected based on the _Default host inventory mode_ setting in _Administration_ → _General_ → _[Other](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other-parameters)_.

For hosts added by network discovery or autoregistration actions, it is possible to define a _Set host inventory mode_ operation selecting manual or automatic mode. This operation overrides the _Default host inventory mode_ setting.

#### Inventory overview

The details of all existing inventory data are available in the _Inventory_ menu.

In _Inventory → Overview_ you can get a host count by various fields of the inventory.

In _Inventory → Hosts_ you can see all hosts that have inventory information. Clicking on the host name will reveal the inventory details in a form.

![](/documentation/current/assets/en/manual/web_interface/inventory_host.png)

The **Overview** tab shows:

_Host name_ | Name of the host.  
Clicking on the name opens a menu with the scripts defined for the host.  
Host name is displayed with an orange icon, if the host is in maintenance.  
---|---  
_Visible name_ | Visible name of the host (if defined).  
_Host (Agent, SNMP, JMX, IPMI)  
interfaces_ | This block provides details of the interfaces configured for the host.  
_OS_ | Operating system inventory field of the host (if defined).  
_Hardware_ | Host hardware inventory field (if defined).  
_Software_ | Host software inventory field (if defined).  
_Description_ | Host description.  
_Monitoring_ | Links to monitoring sections with data for this host: _Web_ , _Latest data_ , _Problems_ , _Graphs_ , _Dashboards_.  
_Configuration_ | Links to configuration sections for this host: _Host_ , _Items_ , _Triggers_ , _Graphs_ , _Discovery_ , _Web_.  
The amount of configured entities is listed after each link.  
  
The **Details** tab shows all inventory fields that are populated (are not empty).

#### Inventory macros

There are host inventory macros {INVENTORY.*} available for use in notifications, for example:

"Server in {INVENTORY.LOCATION1} has a problem, responsible person is {INVENTORY.CONTACT1}, phone number {INVENTORY.POC.PRIMARY.PHONE.A1}."

For more details, see the [Supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) page.