---
title: Discovered host object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dhost/object
downloaded: 2025-11-14 10:41:14
---

# Discovered host object

The following objects are directly related to the `dhost` API.

### Discovered host

Discovered host are created by the Zabbix server and cannot be modified via the API.

The discovered host object contains information about a host discovered by a network discovery rule. It has the following properties.

dhostid | ID | ID of the discovered host.  
---|---|---  
druleid | ID | ID of the discovery rule that detected the host.  
lastdown | timestamp | Time when the discovered host last went down.  
lastup | timestamp | Time when the discovered host last went up.  
status | integer | Whether the discovered host is up or down. A host is up if it has at least one active discovered service.  
  
Possible values:  
0 - host up;  
1 - host down.