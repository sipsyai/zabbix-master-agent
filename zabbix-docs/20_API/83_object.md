---
title: Discovered service object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dservice/object
downloaded: 2025-11-14 10:41:17
---

# Discovered service object

The following objects are directly related to the `dservice` API.

### Discovered service

Discovered services are created by the Zabbix server and cannot be modified via the API.

The discovered service object contains information about a service discovered by a network discovery rule on a host. It has the following properties.

dserviceid | ID | ID of the discovered service.  
---|---|---  
dcheckid | ID | ID of the discovery check used to detect the service.  
dhostid | ID | ID of the discovered host running the service.  
dns | string | DNS of the host running the service.  
ip | string | IP address of the host running the service.  
lastdown | timestamp | Time when the discovered service last went down.  
lastup | timestamp | Time when the discovered service last went up.  
port | integer | Service port number.  
status | integer | Status of the service.  
  
Possible values:  
0 - service up;  
1 - service down.  
value | string | Value returned by the service when performing a Zabbix agent, SNMPv1, SNMPv2 or SNMPv3 discovery check.