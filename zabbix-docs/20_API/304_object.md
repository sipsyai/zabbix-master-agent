---
title: Template group object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/templategroup/object
downloaded: 2025-11-14 10:44:57
---

# Template group object

The following objects are directly related to the `templategroup` API.

### Template group

The template group object has the following properties.

groupid | ID | ID of the template group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the template group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
uuid | string | Universal unique identifier, used for linking imported template groups to already existing ones. Auto-generated, if not given.