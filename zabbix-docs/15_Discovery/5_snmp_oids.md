---
title: Discovery of SNMP OIDs (legacy)
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids
downloaded: 2025-11-14 10:37:30
---

# 5 Discovery of SNMP OIDs (legacy)

#### Overview

In this section we will perform an SNMP [discovery](/documentation/current/en/manual/discovery/low_level_discovery) on a switch.

#### Item key

Unlike with file system and network interface discovery, the item does not necessarily has to have an "snmp.discovery" key - item type of SNMP agent is sufficient.

To configure the discovery rule, do the following:

  * Go to: _Data collection_ → _Templates_
  * Click on _Discovery_ in the row of an appropriate template

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/templates_snmp.png)

  * Click on _Create discovery rule_ in the upper-right corner of the screen
  * Fill in the discovery rule form with the required details as in the screenshot below

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_snmp.png)

All mandatory input fields are marked with a red asterisk.

The OIDs to discover are defined in SNMP OID field in the following format: `discovery[{#MACRO1}, oid1, {#MACRO2}, oid2, …,]`

where _{#MACRO1}_ , _{#MACRO2}_ … are valid lld macro names and _oid1_ , _oid2_... are OIDs capable of generating meaningful values for these macros. A built-in macro _{#SNMPINDEX}_ containing index of the discovered OID is applied to discovered entities. The discovered entities are grouped by _{#SNMPINDEX}_ macro value.

To understand what we mean, let us perform few snmpwalks on our switch:
    
    
    $ snmpwalk -v 2c -c public 192.168.1.1 IF-MIB::ifDescr
           IF-MIB::ifDescr.1 = STRING: WAN
           IF-MIB::ifDescr.2 = STRING: LAN1
           IF-MIB::ifDescr.3 = STRING: LAN2
           
           $ snmpwalk -v 2c -c public 192.168.1.1 IF-MIB::ifPhysAddress
           IF-MIB::ifPhysAddress.1 = STRING: 8:0:27:90:7a:75
           IF-MIB::ifPhysAddress.2 = STRING: 8:0:27:90:7a:76
           IF-MIB::ifPhysAddress.3 = STRING: 8:0:27:2b:af:9e

Copy

✔ Copied

And set SNMP OID to: `discovery[{#IFDESCR}, ifDescr, {#IFPHYSADDRESS}, ifPhysAddress]`

Now this rule will discover entities with {#IFDESCR} macros set to **WAN** , **LAN1** and **LAN2** , {#IFPHYSADDRESS} macros set to **8:0:27:90:7a:75** , **8:0:27:90:7a:76** , and **8:0:27:2b:af:9e** , {#SNMPINDEX} macros set to the discovered OIDs indexes **1** , **2** and **3** :
    
    
    [
               {
                   "{#SNMPINDEX}": "1",
                   "{#IFDESCR}": "WAN",
                   "{#IFPHYSADDRESS}": "8:0:27:90:7a:75"
               },
               {
                   "{#SNMPINDEX}": "2",
                   "{#IFDESCR}": "LAN1",
                   "{#IFPHYSADDRESS}": "8:0:27:90:7a:76"
               },
               {
                   "{#SNMPINDEX}": "3",
                   "{#IFDESCR}": "LAN2",
                   "{#IFPHYSADDRESS}": "8:0:27:2b:af:9e"
               }
           ]

Copy

✔ Copied

If an entity does not have the specified OID, then the corresponding macro will be omitted for this entity. For example if we have the following data:
    
    
    ifDescr.1 "Interface #1"
           ifDescr.2 "Interface #2"
           ifDescr.4 "Interface #4"
           
           ifAlias.1 "eth0"
           ifAlias.2 "eth1"
           ifAlias.3 "eth2"
           ifAlias.5 "eth4"

Copy

✔ Copied

Then in this case SNMP discovery `discovery[{#IFDESCR}, ifDescr, {#IFALIAS}, ifAlias]` will return the following structure:
    
    
    [
               {
                   "{#SNMPINDEX}": 1,
                   "{#IFDESCR}": "Interface #1",
                   "{#IFALIAS}": "eth0"
               },
               {
                   "{#SNMPINDEX}": 2,
                   "{#IFDESCR}": "Interface #2",
                   "{#IFALIAS}": "eth1"
               },
               {
                   "{#SNMPINDEX}": 3,
                   "{#IFALIAS}": "eth2"
               },
               {
                   "{#SNMPINDEX}": 4,
                   "{#IFDESCR}": "Interface #4"
               },
               {
                   "{#SNMPINDEX}": 5,
                   "{#IFALIAS}": "eth4"
               }
           ]

Copy

✔ Copied

#### Item prototypes

The following screenshot illustrates how we can use these macros in item prototypes:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/item_prototype_snmp.png)

You can create as many item prototypes as needed:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/item_prototypes_snmp.png)

#### Trigger prototypes

The following screenshot illustrates how we can use these macros in trigger prototypes:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/trigger_prototype_snmp.png)

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/trigger_prototypes_snmp.png)

#### Graph prototypes

The following screenshot illustrates how we can use these macros in graph prototypes:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/graph_prototype_snmp.png)

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/graph_prototypes_snmp.png)

A summary of our discovery rule:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rules_snmp.png)

#### Discovered entities

When server runs, it will create real items, triggers and graphs based on the values the SNMP discovery rule returns. In the host configuration they are prefixed with an orange link to a discovery rule they come from.

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_items_snmp.png)

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_triggers_snmp.png)

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/discovered_graphs_snmp.png)