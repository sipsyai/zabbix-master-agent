---
title: High availability node object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/hanode/object
downloaded: 2025-11-14 10:41:48
---

# High availability node object

The following object is related to operating a High availability cluster of Zabbix servers.

### High availability node

Nodes are created by the Zabbix server and cannot be modified via the API.

The High availability node object has the following properties.

ha_nodeid | ID | ID of the node.  
---|---|---  
name | string | Name assigned to the node, using the HANodeName configuration entry of zabbix_server.conf. Empty for a server running in standalone mode.  
address | string | IP or DNS name where the node connects from.  
port | integer | Port on which the node is running.  
lastaccess | integer | Heartbeat time, that is, time of last update from the node. UTC timestamp.  
status | integer | State of the node.  
  
Possible values:  
0 - standby;  
1 - stopped manually;  
2 - unavailable;  
3 - active.