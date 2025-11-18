---
title: Icon map object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/iconmap/object
downloaded: 2025-11-14 10:42:33
---

# Icon map object

The following objects are directly related to the `iconmap` API.

### Icon map

The icon map object has the following properties.

iconmapid | ID | ID of the icon map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
default_iconid | ID | ID of the default icon.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
name | string | Name of the icon map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
  
### Icon mapping

The icon mapping object defines a specific icon to be used for hosts with a certain inventory field value. It has the following properties.

iconid | ID | ID of the icon used by the icon mapping.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
expression | string | Expression to match the inventory field against.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
inventory_link | integer | ID of the host inventory field.  
  
Refer to the [host inventory object](/documentation/current/en/manual/api/reference/host/object#host-inventory) for a list of supported inventory fields.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
sortorder | integer | Position of the icon mapping in the icon map.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_