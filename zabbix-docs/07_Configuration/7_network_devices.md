---
title: Standardized templates for network devices
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box/network_devices
downloaded: 2025-11-14 10:36:07
---

# 7 Standardized templates for network devices

#### Overview

In order to provide monitoring for network devices such as switches and routers, we have created two so-called models: for the network device itself (its chassis basically) and for network interface.

Templates for many families of network devices are provided. All templates cover (where possible to get these items from the device):

  * Chassis fault monitoring (power supplies, fans and temperature, overall status)
  * Chassis performance monitoring (CPU and memory items)
  * Chassis inventory collection (serial numbers, model name, firmware version)
  * Network interface monitoring with IF-MIB and EtherLike-MIB (interface status, interface traffic load, duplex status for Ethernet)

If the template is not available in your Zabbix installation, you may need to [import](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade) the template first.

If you are importing the new out-of-the-box templates, you may want to also update the `@Network interfaces for discovery` global regular expression to:
    
    
    Result is FALSE: ^Software Loopback Interface
           Result is FALSE: ^(In)?[lL]oop[bB]ack[0-9._]*$
           Result is FALSE: ^NULL[0-9.]*$
           Result is FALSE: ^[lL]o[0-9.]*$
           Result is FALSE: ^[sS]ystem$
           Result is FALSE: ^Nu[0-9.]*$

Copy

✔ Copied

to filter out loopbacks and null interfaces on most systems.

#### Devices

List of device families for which templates are available:

_Alcatel Timetra TiMOS SNMP_ | Alcatel | Alcatel Timetra | ALCATEL SR 7750 | TiMOS | TIMETRA-SYSTEM-MIB,TIMETRA-CHASSIS-MIB | Certified  
---|---|---|---|---|---|---  
_Aruba CX 8300s by SNMP_ | HPE Aruba Networking | Aruba CX Switch Series | Aruba JL636A 8325, Aruba JL717A 8360 | Aruba AOS-CX | ARUBAWIRED-FAN-MIB, ARUBAWIRED-POWERSUPPLY-MIB, ARUBAWIRED-SYSTEMINFO-MIB, ARUBAWIRED-TEMPSENSOR-MIB, OSPF-MIB | Certified  
_Brocade FC SNMP_ | Brocade | Brocade FC switches | Brocade 300 SAN Switch- | - | SW-MIB,ENTITY-MIB | Performance  
Fault  
_Brocade_Foundry Stackable SNMP_ | Brocade | Brocade ICX | Brocade ICX6610, Brocade ICX7250-48, Brocade ICX7450-48F |  | FOUNDRY-SN-AGENT-MIB, FOUNDRY-SN-STACKING-MIB | Certified  
_Brocade_Foundry Nonstackable SNMP_ | Brocade, Foundry | Brocade MLX, Foundry | Brocade MLXe, Foundry FLS648, Foundry FWSX424 |  | FOUNDRY-SN-AGENT-MIB | Performance  
Fault  
_Check Point Next Generation Firewall by SNMP_ | Check Point | Next Generation Firewall | - | Gaia | HOST-RESOURCES-MIB, CHECKPOINT-MIB, UCD-SNMP-MIB, SNMPv2-MIB, IF-MIB | Certified  
_Ciena 3906 by SNMP_ | Ciena | Ciena CPE | Ciena 3906 | SAOS | WWP-LEOS-BLADE-MIB, WWP-LEOS-CHASSIS-MIB, WWP-LEOS-SYSTEM-CONFIG-MIB | Certified  
_Cisco Catalyst 3750 <device model> SNMP_ | Cisco | Cisco Catalyst 3750 | Cisco Catalyst 3750V2-24FS, Cisco Catalyst 3750V2-24PS, Cisco Catalyst 3750V2-24TS, Cisco Catalyst SNMP, Cisco Catalyst SNMP |  | CISCO-MEMORY-POOL-MIB, IF-MIB, EtherLike-MIB, SNMPv2-MIB, CISCO-PROCESS-MIB, CISCO-ENVMON-MIB, ENTITY-MIB | Certified  
_Cisco IOS SNMP_ | Cisco | Cisco IOS ver > 12.2 3.5 | Cisco C2950 | IOS | CISCO-PROCESS-MIB,CISCO-MEMORY-POOL-MIB,CISCO-ENVMON-MIB | Certified  
_Cisco IOS versions 12.0_3_T-12.2_3.5 SNMP_ | Cisco | Cisco IOS > 12.0 3 T and < 12.2 3.5 | - | IOS | CISCO-PROCESS-MIB,CISCO-MEMORY-POOL-MIB,CISCO-ENVMON-MIB | Certified  
_Cisco IOS prior to 12.0_3_T SNMP_ | Cisco | Cisco IOS < 12.0 3 T | - | IOS | OLD-CISCO-CPU-MIB,CISCO-MEMORY-POOL-MIB | Certified  
_D-Link DES_DGS Switch SNMP_ | D-Link | DES/DGX switches | D-Link DES-xxxx/DGS-xxxx,DLINK DGS-3420-26SC | - | DLINK-AGENT-MIB,EQUIPMENT-MIB,ENTITY-MIB | Certified  
_D-Link DES 7200 SNMP_ | D-Link | DES-7xxx | D-Link DES 7206 | - | ENTITY-MIB,MY-SYSTEM-MIB,MY-PROCESS-MIB,MY-MEMORY-MIB | Performance  
Fault  
Interfaces  
_Dell Force S-Series SNMP_ | Dell | Dell Force S-Series | S4810 |  | F10-S-SERIES-CHASSIS-MIB | Certified  
_Extreme Exos SNMP_ | Extreme | Extreme EXOS | X670V-48x | EXOS | EXTREME-SYSTEM-MIB,EXTREME-SOFTWARE-MONITOR-MIB | Certified  
_FortiGate by SNMP_ | Fortinet | FortiGate (NGFW) | - | FortiOS | HOST-RESOURCES-MIB  
FORTINET-FORTIGATE-MIB  
FORTINET-CORE-MIB  
SNMPv2-MIB  
IF-MIB  
ENTITY-MIB | Performance  
Inventory  
_HP Comware HH3C SNMP_ | HP | HP (H3C) Comware | HP A5500-24G-4SFP HI Switch |  | HH3C-ENTITY-EXT-MIB,ENTITY-MIB | Certified  
_HP Enterprise Switch SNMP_ | HP | HP Enterprise Switch | HP ProCurve J4900B Switch 2626, HP J9728A 2920-48G Switch |  | STATISTICS-MIB,NETSWITCH-MIB,HP-ICF-CHASSIS,ENTITY-MIB,SEMI-MIB | Certified  
_Huawei OceanStor 5300 V5 by SNMP_ | Huawei | Huawei OceanStor Dorado | Huawei OceanStor Dorado with V5 software |  | HUAWEI-STORAGE-HARDWARE-MIB, HUAWEI-STORAGE-SPACE-MIB, ISM-PERFORMANCE-MIB, HOST-RESOURCES-MIB, SNMPv2-MIB | Certified  
_Huawei OceanStor Dorado by SNMP_ | Huawei | Huawei OceanStor, Huawei OceanStor Dorado | Huawei OceanStor Dorado 3000/5000/6000/8000/18000/5300/5500/5600/6800/18500/18800 with V6/V700 software |  | HUAWEI-STORAGE-HARDWARE-MIB, HUAWEI-STORAGE-SPACE-MIB, ISM-PERFORMANCE-MIB, HOST-RESOURCES-MIB, SNMPv2-MIB | Certified  
_Huawei VRP by SNMP_ | Huawei | Huawei VRP | S2352P-EI |  | ENTITY-MIB,HUAWEI-ENTITY-EXTENT-MIB | Certified  
_Intel_Qlogic Infiniband SNMP_ | Intel/QLogic | Intel/QLogic Infiniband devices | Infiniband 12300 |  | ICS-CHASSIS-MIB | Fault  
Inventory  
_Juniper SNMP_ | Juniper | MX,SRX,EX models | Juniper MX240, Juniper EX4200-24F | JunOS | JUNIPER-MIB | Certified  
_Juniper MX NETCONF_ | Juniper | MX models | Juniper MX204 Edge Router | JunOS 24.2R1-S1.10 | _Not applicable (uses NETCONF over SSH)_ | Certified  
_Juniper MX SNMP_ | Juniper | MX models | Juniper MX204 Edge Router | JunOS 24.2R1-S1.10 | OSPF-MIB, JUNIPER-DOM-MIB, JUNIPER-MIB, BGP4-V2-MIB-JUNIPER, OSPFV3-MIB-JUNIPER | Certified  
_Mellanox SNMP_ | Mellanox | Mellanox Infiniband devices | SX1036 | MLNX-OS | HOST-RESOURCES-MIB,ENTITY-MIB,ENTITY-SENSOR-MIB,MELLANOX-MIB | Certified  
_MikroTik CCR <device model> SNMP_ | MikroTik | MikroTik Cloud Core Routers (CCR series) | Separate dedicated templates are available for MikroTik CCR1009-7G-1C-1S+, MikroTik CCR1009-7G-1C-1S+PC, MikroTik CCR1009-7G-1C-PC, MikroTik CCR1016-12G, MikroTik CCR1016-12S-1S+, MikroTik CCR1036-12G-4S-EM, MikroTik CCR1036-12G-4S, MikroTik CCR1036-8G-2S+, MikroTik CCR1036-8G-2S+EM, MikroTik CCR1072-1G-8S+, MikroTik CCR2004-16G-2S+, MikroTik CCR2004-1G-12S+2XS | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik CRS <device model> SNMP_ | MikroTik | MikroTik Cloud Router Switches (CRS series) | Separate dedicated templates are available for MikroTik CRS106-1C-5S, MikroTik CRS109-8G-1S-2HnD-IN, MikroTik CRS112-8G-4S-IN, MikroTik CRS112-8P-4S-IN, MikroTik CRS125-24G-1S-2HnD-IN, MikroTik CRS212-1G-10S-1S+IN, MikroTik CRS305-1G-4S+IN, MikroTik CRS309-1G-8S+IN, MikroTik CRS312-4C+8XG-RM, MikroTik CRS317-1G-16S+RM, MikroTik CRS326-24G-2S+IN, MikroTik CRS326-24G-2S+RM, MikroTik CRS326-24S+2Q+RM, MikroTik CRS328-24P-4S+RM, MikroTik CRS328-4C-20S-4S+RM, MikroTik CRS354-48G-4S+2Q+RM, MikroTik CRS354-48P-4S+2Q+RM | RouterOS/SwitchOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik CSS <device model> SNMP_ | MikroTik | MikroTik Cloud Smart Switches (CSS series) | Separate dedicated templates are available for MikroTik CSS326-24G-2S+RM, MikroTik CSS610-8G-2S+IN | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik FiberBox SNMP_ | MikroTik | MikroTik FiberBox | MikroTik FiberBox | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik hEX <device model> SNMP_ | MikroTik | MikroTik hEX | Separate dedicated templates are available for MikroTik hEX, MikroTik hEX lite, MikroTik hEX PoE, MikroTik hEX PoE lite, MikroTik hEX S | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik netPower <device model> SNMP_ | MikroTik | MikroTik netPower | Separate dedicated templates are available for MikroTik netPower 15FR, MikroTik netPower 16P SNMP, MikroTik netPower Lite 7R | RouterOS/SwitchOS, SwitchOS Lite | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik PowerBox <device model> SNMP_ | MikroTik | MikroTik PowerBox | Separate dedicated templates are available for MikroTik PowerBox, MikroTik PowerBox Pro | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik RB <device model> SNMP_ | MikroTik | MikroTik RB series routers | Separate dedicated templates are available for MikroTik RB1100AHx4, MikroTik RB1100AHx4 Dude Edition, MikroTik RB2011iL-IN, MikroTik RB2011iL-RM, MikroTik RB2011iLS-IN, MikroTik RB2011UiAS-IN, MikroTik RB2011UiAS-RM, MikroTik RB260GS, MikroTik RB3011UiAS-RM, MikroTik RB4011iGS+RM, MikroTik RB5009UG+S+IN | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_MikroTik SNMP_ | MikroTik | MikroTik RouterOS devices | MikroTik CCR1016-12G, MikroTik RB2011UAS-2HnD, MikroTik 912UAG-5HPnD, MikroTik 941-2nD, MikroTik 951G-2HnD, MikroTik 1100AHx2 | RouterOS | MIKROTIK-MIB,HOST-RESOURCES-MIB | Certified  
_Netgear Fastpath SNMP_ | Netgear | Netgear Fastpath | M5300-28G |  | FASTPATH-SWITCHING-MIB,FASTPATH-BOXSERVICES-PRIVATE-MIB | Fault  
Inventory  
_QTech QSW SNMP_ | QTech | Qtech devices | Qtech QSW-2800-28T | - | QTECH-MIB,ENTITY-MIB | Performance  
Inventory  
_Stormshield SNS by SNMP_ | Stormshield | Stormshield Network Security (SNS) firewalls | SN3100 | Stormshield SNS | HOST-RESOURCES-MIB, UCD-SNMP-MIB, STORMSHIELD-ASQ-STATS-MIB, STORMSHIELD-AUTOUPDATE-MIB, STORMSHIELD-HA-MIB, STORMSHIELD-PROPERTY-MIB, STORMSHIELD-HEALTH-MONITOR-MIB, STORMSHIELD-IF-MIB, STORMSHIELD-SYSTEM-MONITOR-MIB, STORMSHIELD-IPSEC-STATS-MIB | Certified  
_TP-LINK SNMP_ | TP-LINK | TP-LINK | T2600G-28TS v2.0 |  | TPLINK-SYSMONITOR-MIB,TPLINK-SYSINFO-MIB | Performance  
Inventory  
_Ubiquiti AirOS SNMP_ | Ubiquiti | Ubiquiti AirOS wireless devices | NanoBridge,NanoStation,Unifi | AirOS | FROGFOOT-RESOURCES-MIB,IEEE802dot11-MIB | Performance  
_Vyatta Virtual Router by SNMP_ | Ciena | Vyatta | Vyatta Virtual Router 1908e | Vyatta 1908e | SNMPv2-MIB, HOST-RESOURCES-MIB, UCD-SNMP-MIB, IF-MIB, DISMAN-EVENT-MIB | Performance  
Inventory  
  
#### Template design

Templates were designed with the following in mind:

  * User macros are used as much as possible so triggers can be tuned by the user;
  * Low-level discovery is used as much as possible to minimize the number of unsupported items;
  * All templates depend on Template ICMP Ping so all devices are also checked by ICMP;
  * Items don't use any MIBs - SNMP OIDs are used in items and low-level discoveries. So it's not necessary to load any MIBs into Zabbix for templates to work;
  * Loopback network interfaces are filtered when discovering as well as interfaces with ifAdminStatus = down(2)
  * 64bit counters are used from IF-MIB::ifXTable where possible. If it is not supported, default 32bit counters are used instead.

All discovered network interfaces have a trigger that monitors its operational status (link), for example:
    
    
     {$IFCONTROL:"{#IFNAME}"}=1 and last(/Alcatel Timetra TiMOS SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}])=2 and (last(/Alcatel Timetra TiMOS SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}],#1)<>last(/Alcatel Timetra TiMOS SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}],#2))

  * If you do no want to monitor this condition for a specific interface create a user macro with context with the value 0. For example:

![](/documentation/current/assets/en/manual/config/template_ifcontrol.png)

where Gi0/0 is {#IFNAME}. That way the trigger is not used any more for this specific interface.

  * You can also change the default behavior for all triggers not to fire and activate this trigger only to limited number of interfaces like uplinks:

![](/documentation/current/assets/en/manual/config/template_ifcontrol2.png)

#### Tags

  * Performance – device family MIBs provide a way to monitor CPU and memory items;
  * Fault - device family MIBs provide a way to monitor at least one temperature sensor;
  * Inventory – device family MIBs provide a way to collect at least the device serial number and model name;
  * Certified – all three main categories above are covered.