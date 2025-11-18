---
title: Discovery of host interfaces in Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/host_interfaces
downloaded: 2025-11-14 10:37:39
---

# 15 Discovery of host interfaces in Zabbix

#### Overview

It is possible to [discover](/documentation/current/en/manual/discovery/low_level_discovery) all interfaces configured in Zabbix frontend for a host.

#### Item key

The item to use in the [discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#discovery-rule) is the
    
    
    zabbix[host,discovery,interfaces]

Copy

✔ Copied

internal item.

This item returns a JSON with the description of interfaces, including:

  * IP address/DNS hostname (depending on the “Connect to” host setting)
  * Port number
  * Interface type (Zabbix agent, SNMP, JMX, IPMI)
  * If it is the default interface or not
  * If the bulk request feature is enabled - for SNMP interfaces only.

For example:
    
    
    [{"{#IF.CONN}":"192.168.3.1","{#IF.IP}":"192.168.3.1","{#IF.DNS}":"","{#IF.PORT}":"10050","{#IF.TYPE}":"AGENT","{#IF.DEFAULT}":1}]  

Copy

✔ Copied

With multiple interfaces their records in JSON are ordered by:

  * Interface type,
  * Default - the default interface is put before non-default interfaces,
  * Interface ID (in ascending order).

#### Supported macros

The following macros are supported for use in the discovery rule [filter](/documentation/current/en/manual/discovery/low_level_discovery#filter) and prototypes of items, triggers and graphs:

{#IF.CONN} | Interface IP address or DNS host name.  
---|---  
{#IF.IP} | Interface IP address.  
{#IF.DNS} | Interface DNS host name.  
{#IF.PORT} | Interface port number.  
{#IF.TYPE} | Interface type ("AGENT", "SNMP", "JMX", or "IPMI").  
{#IF.DEFAULT} | Default status for the interface:  
0 - not default interface  
1 - default interface  
{#IF.SNMP.BULK} | SNMP bulk processing status for the interface:  
0 - disabled  
1 - enabled  
This macro is returned only if interface type is “SNMP”.