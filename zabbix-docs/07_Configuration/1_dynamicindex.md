---
title: Dynamic indexes
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmp/dynamicindex
downloaded: 2025-11-14 10:34:59
---

# 1 Dynamic indexes

#### Overview

While you may find the required index number (for example, of a network interface) among the SNMP OIDs, sometimes you may not completely rely on the index number always staying the same.

Index numbers may be dynamic - they may change over time and your item may stop working as a consequence.

To avoid this scenario, it is possible to define an OID which takes into account the possibility of an index number changing.

For example, if you need to retrieve the index value to append to **ifInOctets** that corresponds to the **GigabitEthernet0/1** interface on a Cisco device, use the following OID:
    
    
    ifInOctets["index","ifDescr","GigabitEthernet0/1"]

Copy

✔ Copied

##### The syntax

A special syntax for OID is used:

**< OID of data>["index","<base OID of index>","<string to search for>"]**

OID of data | Main OID to use for data retrieval on the item.  
---|---  
index | Method of processing. Currently one method is supported:  
**index** – search for index and append it to the data OID  
base OID of index | This OID will be looked up to get the index value corresponding to the string.  
string to search for | The string to use for an exact match with a value when doing lookup. Case sensitive.  
  
#### Example

Getting memory usage of _apache_ process.

If using this OID syntax:
    
    
    HOST-RESOURCES-MIB::hrSWRunPerfMem["index","HOST-RESOURCES-MIB::hrSWRunPath", "/usr/sbin/apache2"]

Copy

✔ Copied

the index number will be looked up here:
    
    
    ...
           HOST-RESOURCES-MIB::hrSWRunPath.5376 = STRING: "/sbin/getty"
           HOST-RESOURCES-MIB::hrSWRunPath.5377 = STRING: "/sbin/getty"
           HOST-RESOURCES-MIB::hrSWRunPath.5388 = STRING: "/usr/sbin/apache2"
           HOST-RESOURCES-MIB::hrSWRunPath.5389 = STRING: "/sbin/sshd"
           ...

Copy

✔ Copied

Now we have the index, 5388. The index will be appended to the data OID in order to receive the value we are interested in:
    
    
    HOST-RESOURCES-MIB::hrSWRunPerfMem.5388 = INTEGER: 31468 KBytes

Copy

✔ Copied

#### Index lookup caching

When a dynamic index item is requested, Zabbix retrieves and caches whole SNMP table under base OID for index, even if a match would be found sooner. This is done in case another item would refer to the same base OID later - Zabbix would look up index in the cache, instead of querying the monitored host again. Note that each poller process uses separate cache.

In all subsequent value retrieval operations only the found index is verified. If it has not changed, value is requested. If it has changed, cache is rebuilt - each poller that encounters a changed index walks the index SNMP table again.