---
title: Discovery of IPMI sensors
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/ipmi_sensors
downloaded: 2025-11-14 10:37:32
---

# 7 Discovery of IPMI sensors

#### Overview

It is possible to automatically discover IPMI sensors.

To do that, you may use a combination of:

  * the `ipmi.get` IPMI item as the master item
  * dependent low-level discovery rule and item prototypes

#### Configuration

##### Master item

Create an IPMI item using the following key:
    
    
    ipmi.get

Copy

✔ Copied

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/ipmi_get_item.png)

Set the type of information to "Text" for possibly big JSON data.

##### Dependent LLD rule

Create a low-level discovery rule as "Dependent item" type:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/ipmi_get_lld.png)

As master item select the `ipmi.get` item we created.

In the "LLD macros" tab define a custom macro with the corresponding JSONPath:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/ipmi_get_lld_b.png)

##### Dependent item prototype

Create an item prototype with "Dependent item" type in this LLD rule. As master item for this prototype select the `ipmi.get` item we created.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/ipmi_get_prototype.png)

Note the use of the {#SENSOR_ID} macro in the item prototype name and key:

  * _Name_ : IPMI value for sensor {#SENSOR_ID}
  * _Key_ : ipmi_sensor[{#SENSOR_ID}]

As type of information, _Numeric (unsigned)_.

In the item prototype "Preprocessing" tab select JSONPath and use the following JSONPath expression as parameter:
    
    
    $.[?(@.id=='{#SENSOR_ID}')].value.first()

Copy

✔ Copied

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/ipmi_get_prototype_b.png)

When discovery starts, one item per each IPMI sensor will be created. This item will return the integer value of the given sensor.