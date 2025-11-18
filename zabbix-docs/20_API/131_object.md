---
title: Host group object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hostgroup/object
downloaded: 2025-11-14 10:42:05
---

# Host group object

The following objects are directly related to the `hostgroup` API.

### Host group

The host group object has the following properties.

groupid | ID | ID of the host group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the host group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
flags | integer | Origin of the host group.  
  
Possible values:  
0 - a plain host group;  
4 - a discovered host group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
uuid | string | Universal unique identifier, used for linking imported host groups to already existing ones. Auto-generated, if not given.