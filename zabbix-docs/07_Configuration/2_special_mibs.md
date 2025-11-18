---
title: Special OIDs
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmp/special_mibs
downloaded: 2025-11-14 10:35:00
---

# 2 Special OIDs

Some of the most used SNMP OIDs are translated automatically to a numeric representation by Zabbix. For example, **ifIndex** is translated to **1.3.6.1.2.1.2.2.1.1** , **ifIndex.0** is translated to **1.3.6.1.2.1.2.2.1.1.0**.

The table contains list of the special OIDs.

ifIndex | 1.3.6.1.2.1.2.2.1.1 | A unique value for each interface.  
---|---|---  
ifDescr | 1.3.6.1.2.1.2.2.1.2 | A textual string containing information about the interface.This string should include the name of the manufacturer, the product name and the version of the hardware interface.  
ifType | 1.3.6.1.2.1.2.2.1.3 | The type of interface, distinguished according to the physical/link protocol(s) immediately 'below' the network layer in the protocol stack.  
ifMtu | 1.3.6.1.2.1.2.2.1.4 | The size of the largest datagram which can be sent / received on the interface, specified in octets.  
ifSpeed | 1.3.6.1.2.1.2.2.1.5 | An estimate of the interface's current bandwidth in bits per second.  
ifPhysAddress | 1.3.6.1.2.1.2.2.1.6 | The interface's address at the protocol layer immediately `below' the network layer in the protocol stack.  
ifAdminStatus | 1.3.6.1.2.1.2.2.1.7 | The current administrative state of the interface.  
ifOperStatus | 1.3.6.1.2.1.2.2.1.8 | The current operational state of the interface.  
ifInOctets | 1.3.6.1.2.1.2.2.1.10 | The total number of octets received on the interface, including framing characters.  
ifInUcastPkts | 1.3.6.1.2.1.2.2.1.11 | The number of subnetwork-unicast packets delivered to a higher-layer protocol.  
ifInNUcastPkts | 1.3.6.1.2.1.2.2.1.12 | The number of non-unicast (i.e., subnetwork- broadcast or subnetwork-multicast) packets delivered to a higher-layer protocol.  
ifInDiscards | 1.3.6.1.2.1.2.2.1.13 | The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space.  
ifInErrors | 1.3.6.1.2.1.2.2.1.14 | The number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  
ifInUnknownProtos | 1.3.6.1.2.1.2.2.1.15 | The number of packets received via the interface which were discarded because of an unknown or unsupported protocol.  
ifOutOctets | 1.3.6.1.2.1.2.2.1.16 | The total number of octets transmitted out of the interface, including framing characters.  
ifOutUcastPkts | 1.3.6.1.2.1.2.2.1.17 | The total number of packets that higher-level protocols requested be transmitted, and which were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent.  
ifOutNUcastPkts | 1.3.6.1.2.1.2.2.1.18 | The total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent.  
ifOutDiscards | 1.3.6.1.2.1.2.2.1.19 | The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space.  
ifOutErrors | 1.3.6.1.2.1.2.2.1.20 | The number of outbound packets that could not be transmitted because of errors.  
ifOutQLen | 1.3.6.1.2.1.2.2.1.21 | The length of the output packet queue (in packets).