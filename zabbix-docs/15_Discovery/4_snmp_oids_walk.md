---
title: Discovery of SNMP OIDs
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk
downloaded: 2025-11-14 10:37:29
---

# 4 Discovery of SNMP OIDs

#### Overview

In this section we will perform a [low-level discovery](/documentation/current/en/manual/discovery/low_level_discovery) on an SNMP device.

This discovery method of SNMP OIDs has been supported since Zabbix server/proxy 6.4.

#### Sample Configuration

1\. Create an SNMP agent item with a key such as:
    
    
    walk[.1.3.6.1.4.1.9999.1.1.1.1]

Copy

✔ Copied

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/snmp_walk_item.png)

This item performs a single SNMP table walk and returns all table entries in one request, in a format that corresponds to the output of the `snmpwalk` utility with the formatting options `-Oe -Ot -On`.

It will return the following multiline text value:
    
    
    .1.3.6.1.4.1.9999.1.1.1.1.1.1 = STRING: "Temperature Sensor"
           .1.3.6.1.4.1.9999.1.1.1.1.2.1 = STRING: "temp"
           .1.3.6.1.4.1.9999.1.1.1.1.3.1 = 100
           .1.3.6.1.4.1.9999.1.1.1.1.1.2 = STRING: "Humidity Sensor"
           .1.3.6.1.4.1.9999.1.1.1.1.2.2 = STRING: "humidity"
           .1.3.6.1.4.1.9999.1.1.1.1.3.2 = 200

Copy

✔ Copied

2\. Create a discovery rule:

  * In the _Name_ field, enter a descriptive discovery rule name (e.g., "Discover sensors").
  * In the _Type_ field, select "Dependent item".
  * In the _Key_ field, enter a descriptive key (e.g., "net.if.discovery").
  * In the _Master item_ field, select "SNMP walk item".

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/snmp_discovery_dep_item.png)

3\. In the _Preprocessing_ tab, add a preprocessing step with the "SNMP walk to JSON" in the _Name_ dropdown with 3 parameters:

  * _Field name_ : "{#SENSORNAME}"; _OID prefix_ : ".1.3.6.1.4.1.9999.1.1.1.1.1": _Format_ : "Unchanged".
  * _Field name_ : "{#SENSORTYPE}"; _OID prefix_ : ".1.3.6.1.4.1.9999.1.1.1.1.2": _Format_ : "Unchanged".
  * _Field name_ : "{#SENSORVALUE}"; _OID prefix_ : ".1.3.6.1.4.1.9999.1.1.1.1.3": _Format_ : "Unchanged".

After preprocessing, the discovery rule returns a JSON array of macro sets.

For example:
    
    
    [
               {
                   "{#SNMPINDEX}": "1",
                   "{#SENSORNAME}": "Temperature Sensor",
                   "{#SENSORTYPE}": "temp",
                   "{#SENSORVALUE}": "100"
               },
               {
                   "{#SNMPINDEX}": "2",
                   "{#SENSORNAME}": "Humidity Sensor",
                   "{#SENSORTYPE}": "humidity",
                   "{#SENSORVALUE}": "200"
               }
           ]

Copy

✔ Copied

Each object represents one discovered sensor and provides macros such as `{#SNMPINDEX}`, `{#SENSORNAME}`, `{#SENSORTYPE}`, and `{#SENSORVALUE}`.

They are grouped by the SNMP index, which is the numeric suffix at the end of each OID (e.g., .1, .2) — this index uniquely identifies each row in the SNMP table and is automatically extracted as `{#SNMPINDEX}`.

4\. Under the discovery rule, create one or more item prototypes (with discovery rule as a master item).

For example, sensor value dependent item:

  * In the _Name_ field, enter "Sensor {#SNMPINDEX}: {#SENSORNAME}".
  * In the _Type_ field, select "Dependent item".
  * In the _Key_ field, enter "sensor.value[{#SNMPINDEX}]".
  * In the _Master item_ field, select "SNMP walk item".

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/snmp_item_prototype.png)

In the _Preprocessing_ tab, add a preprocessing step with the "SNMP walk value" name with ".1.3.6.1.4.1.9999.1.1.1.1.3.{#SNMPINDEX}" OID in the _Parameter_ field. _Format_ : "Unchanged".

Following items will be discovered:

Sensor 1: Temperature Sensor | sensor.value[1] | .1.3.6.1.4.1.9999.1.1.1.1.3.1 | 100  
---|---|---|---  
Sensor 2: Humidity Sensor | sensor.value[2] | .1.3.6.1.4.1.9999.1.1.1.1.3.2 | 200  
  
When the discovery rule runs, items such as `sensor.value[1]`, `sensor.value[2]` are created.

Each dependent item extracts its value from the master item's SNMP walk result using preprocessing, without performing separate SNMP requests themselves.

5\. Reference dependent item prototypes in trigger prototypes using the same macros from the discovery rule. Example:
    
    
    {Template_Sensor:sensor.value[{#SNMPINDEX}].last()} > 75

Copy

✔ Copied

This produces a trigger for each discovered sensor (for example, sensor.value[1], sensor.value[2]) and fires if the latest value (temperature or humidity) exceeds 75.

6\. Include dependent items for each discovered entity. Example graph item key:
    
    
    sensor.value[{#SNMPINDEX}]

Copy

✔ Copied

One graph is created per `{#SNMPINDEX}`, plotting temperature and humidity over time.

This configuration performs only a single SNMP walk request per polling cycle, regardless of the number of discovered items. All dependent items extract their values from the master SNMP walk result using preprocessing, significantly reducing SNMP traffic and load.

#### Dynamic indexes with walk[]

Dynamic indexes (for example, interface indexes) can shift when hardware is reconfigured. To accommodate this behavior, a master SNMP walk discovery rule is created with a key such as:
    
    
    walk[1.3.6.1.2.1.2.2.1.10]

Copy

✔ Copied

After SNMP walk to JSON preprocessing, the result might resemble:
    
    
    [
               {
                   "{#SNMPINDEX}": "2",
                   "{#VALUE}": "123456"
               },
               {
                   "{#SNMPINDEX}": "3",
                   "{#VALUE}": "654321"
               }
           ]

Copy

✔ Copied

A dependent item prototype uses the `{#SNMPINDEX}` macro to construct the key:
    
    
    net.if.in[{#SNMPINDEX}]

Copy

✔ Copied

Preprocessing for this prototype includes "SNMP walk value" name with "1.3.6.1.2.1.2.2.1.10.{#SNMPINDEX}" OID in the _Parameter_ field. _Format_ : "Unchanged".

At runtime, actual items such as `net.if.in[2]` and `net.if.in[3]` are created. If a given interface index changes (for example, if the index `2` is replaced by `5` in the SNMP table), then on the next run of the discovery rule:

  * The old dependent item net.if.in[2] is marked as "lost" or removed, and no new data is gathered for that item.
  * A new dependent item net.if.in[5] is created, starting with an empty history.
  * Historical data from net.if.in[2] is not automatically moved to net.if.in[5].

Trigger prototype example:
    
    
    {Template_Interface:net.if.in[{#SNMPINDEX}].last()} > 1000000000

Copy

✔ Copied

Graph prototype example includes items:
    
    
    net.if.in[{#SNMPINDEX}]
           net.if.out[{#SNMPINDEX}]

Copy

✔ Copied

This configuration ensures reliable monitoring of tables with dynamic indexes while minimizing SNMP traffic—only a single SNMP walk per poll cycle is required, with dependent item prototypes extracting the necessary values.

#### Discovered entities

When the server runs, it will create real dependent items, triggers and graphs based on the values the SNMP discovery rule returns.