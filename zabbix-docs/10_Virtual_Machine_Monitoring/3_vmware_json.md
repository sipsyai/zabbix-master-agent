---
title: JSON examples for VMware items
source: https://www.zabbix.com/documentation/current/en/manual/vm_monitoring/vmware_json
downloaded: 2025-11-14 10:36:59
---

# 3 JSON examples for VMware items  
  
## Overview

This section provides additional information about JSON objects returned by various VMware [items](/documentation/current/en/manual/vm_monitoring/vmware_keys).

## vmware.*.alarms.get

The items **vmware.alarms.get[]** , **vmware.cluster.alarms.get[]** , **vmware.datastore.alarms.get[]** , **vmware.dc.alarms.get[]** , **vmware.hv.alarms.get[]** , **vmware.vm.alarms.get[]** return JSON objects with the following structure (values are provided as an example):
    
    
    {
               "alarms": [ 
                   { 
                       "name": "Host connection and power state", 
                       "system_name": "alarm.HostConnectionStateAlarm", 
                       "description": "Default alarm to monitor host connection and power state", 
                       "enabled": true, 
                       "key": "alarm-1.host-2013", 
                       "time": "2022-06-27T05:27:38.759976Z", 
                       "overall_status": "red", 
                       "acknowledged": false 
                   }, 
                   { 
                       "name": "Host memory usage", 
                       "system_name": "alarm.HostMemoryUsageAlarm", 
                       "description": "Default alarm to monitor host memory usage", 
                       "enabled": true, 
                       "key": "alarm-4.host-1004", 
                       "time": "2022-05-16T13:32:42.47863Z", 
                       "overall_status": "yellow", 
                       "acknowledged": false 
                   }, 
                   { 
                       // other alarms 
                   } 
               ]
           } 

Copy

✔ Copied

## vmware.*.tags.get

The items **vmware.cluster.tags.get[]** , **vmware.datastore.tags.get[]** , **vmware.dc.tags.get[]** , **vmware.hv.tags.get[]** , **vmware.vm.tags.get[]** return JSON objects with the following structure (values are provided as an example):
    
    
    {
               "tags": [ 
                   { 
                       "name": "Windows", 
                       "description": "tag for cat OS type", 
                       "category": "OS type" 
                   }, 
                   { 
                       "name": "SQL Server", 
                       "description": "tag for cat application name", 
                       "category": "application name" 
                   }, 
                   { 
                       // other tags 
                   } 
               ] 
           }

Copy

✔ Copied

## vmware.hv.diskinfo.get

The item **vmware.hv.diskinfo.get[]** returns JSON objects with the following structure (values are provided as an example):
    
    
    [
             {
               "instance": "mpx.vmhba32:C0:T0:L0",
               "hv_uuid": "8002299e-d7b9-8728-d224-76004bbb6100",
               "datastore_uuid": "",
               "operational_state": [
                 "ok"
               ],
               "lun_type": "disk",
               "queue_depth": 1,
               "model": "USB DISK",
               "vendor": "SMI Corp",
               "revision": "1100",
               "serial_number": "CCYYMMDDHHmmSS9S62CK",
               "vsan": {}
             },
             {
               // other instances
             }
           ]

Copy

✔ Copied

## vmware.dvswitch.fetchports.get

The item **vmware.dvswitch.fetchports.get[]** returns JSON objects with the following structure (values are provided as an example):
    
    
    { 
               "FetchDVPortsResponse": 
               { 
                   "returnval": [ 
                       { 
                           "key": "0", 
                           "dvsUuid": "50 36 6a 24 25 c0 10 9e-05 4a f6 ea 4e 3d 09 88", 
                           "portgroupKey": "dvportgroup-2023", 
                           "proxyHost": 
                           { 
                               "@type": "HostSystem", 
                               "#text": "host-2021" 
                           }, 
                           "connectee": 
                           { 
                               "connectedEntity": 
                               { 
                                   "@type": "HostSystem", 
                                   "#text": "host-2021" 
                               }, 
                               "nicKey": "vmnic0", 
                               "type": "pnic" 
                           }, 
                           "conflict": "false", 
                           "state": 
                           { 
                               "runtimeInfo": 
                               { 
                                   "linkUp": "true", 
                                   "blocked": "false", 
                                   "vlanIds": 
                                   { 
                                       "start": "0", 
                                       "end": "4094" 
                                   }, 
                                   "trunkingMode": "true", 
                                   "linkPeer": "vmnic0", 
                                   "macAddress": "00:00:00:00:00:00", 
                                   "statusDetail": null, 
                                   "vmDirectPathGen2Active": "false", 
                                   "vmDirectPathGen2InactiveReasonOther": "portNptIncompatibleConnectee" 
                               }, 
                               "stats": 
                               { 
                                   "packetsInMulticast": "2385470", 
                                   "packetsOutMulticast": "45", 
                                   "bytesInMulticast": "309250248", 
                                   "bytesOutMulticast": "5890", 
                                   "packetsInUnicast": "155601537", 
                                   "packetsOutUnicast": "113008658", 
                                   "bytesInUnicast": "121609489384", 
                                   "bytesOutUnicast": "47240279759", 
                                   "packetsInBroadcast": "1040420", 
                                   "packetsOutBroadcast": "7051",
                                   "bytesInBroadcast": "77339771", 
                                   "bytesOutBroadcast": "430392", 
                                   "packetsInDropped": "0", 
                                   "packetsOutDropped": "0", 
                                   "packetsInException": "0", 
                                   "packetsOutException": "0" 
                               } 
                           }, 
                           "connectionCookie": "1702765133", 
                           "lastStatusChange": "2022-03-25T14:01:11Z", 
                           "hostLocalPort": "false" 
                       }, 
                       { 
                           //other keys
                       } 
                   ] 
               } 
           }

Copy

✔ Copied

## vmware.hv.hw.sensors.get

The item **vmware.hv.hw.sensors.get[]** returns JSON objects with the following structure (values are provided as an example):
    
    
    {
               "val": 
                   { 
                       "@type": "HostHardwareStatusInfo", 
                       "storageStatusInfo": [ 
                           { 
                               "name": "Intel Corporation HD Graphics 630 #2", 
                               "status": 
                                   { 
                                       "label": "Unknown", 
                                       "summary": "Cannot report on the current status of the physical element",
                                       "key": "Unknown" 
                                   } 
                           }, 
                           { 
                               "name": "Intel Corporation 200 Series/Z370 Chipset Family USB 3.0 xHCI Controller #20",
                               "status": 
                                   { 
                                       "label": "Unknown", 
                                       "summary": "Cannot report on the current status of the physical element", 
                                       "key": "Unknown" 
                                   } 
                           }, 
                           { 
                               // other hv hw sensors 
                           } 
                       ] 
                   }
           } 

Copy

✔ Copied

## vmware.hv.sensors.get

The item **vmware.hv.sensors.get[]** returns JSON objects with the following structure (values are provided as an example):
    
    
    { 
               "val": 
                   { 
                       "@type": "ArrayOfHostNumericSensorInfo", "HostNumericSensorInfo": [ 
                           { 
                               "@type": "HostNumericSensorInfo", 
                               "name": "System Board 1 PwrMeter Output --- Normal", 
                               "healthState": 
                                   { 
                                       "label": "Green", 
                                       "summary": "Sensor is operating under normal conditions", 
                                       "key": "green" 
                                   }, 
                               "currentReading": "10500", 
                               "unitModifier": "-2", 
                               "baseUnits": "Watts", 
                               "sensorType": "other" 
                           }, 
                           { 
                               "@type": "HostNumericSensorInfo", 
                               "name": "Power Supply 1 PS 1 Output --- Normal", 
                               "healthState":
                                   { 
                                       "label": "Green", 
                                       "summary": "Sensor is operating under normal conditions", 
                                       "key": "green" 
                                   }, 
                               "currentReading": "10000", 
                               "unitModifier": "-2", 
                               "baseUnits": "Watts", 
                               "sensorType": "power" 
                           }, 
                           { 
                               // other hv sensors 
                           } 
                       ] 
                   } 
           } 

Copy

✔ Copied

## vmware.vm.snapshot.get

If any snapshots exist, the item **vmware.snapshot.get[]** returns a JSON object with the following structure (values are provided as an example):
    
    
    {
             "snapshot": [
               {
                 "name": "VM Snapshot 4%2f1%2f2022, 9:16:39 AM",
                 "description": "Descr 1",
                 "createtime": "2022-04-01T06:16:51.761Z",
                 "size": 5755795171,
                 "uniquesize": 5755795171
               },
               {
                 "name": "VM Snapshot 4%2f1%2f2022, 9:18:21 AM",
                 "description": "Descr 2",
                 "createtime": "2022-04-01T06:18:29.164999Z",
                 "size": 118650595,
                 "uniquesize": 118650595
               },
               {
                 "name": "VM Snapshot 4%2f1%2f2022, 9:37:29 AM",
                 "description": "Descr 3",
                 "createtime": "2022-04-01T06:37:53.534999Z",
                 "size": 62935016,
                 "uniquesize": 62935016
               }
             ],
             "count": 3,
             "latestdate": "2022-04-01T06:37:53.534999Z",
             "latestage": 22729203,
             "oldestdate": "2022-04-01T06:16:51.761Z",
             "oldestage": 22730465,
             "size": 5937380782,
             "uniquesize": 5937380782
           }

Copy

✔ Copied

If no snapshot exists, the item **vmware.snapshot.get[]** returns a JSON object with empty values:
    
    
    {
             "snapshot": [],
             "count": 0,
             "latestdate": null,
             "latestage": 0,
             "oldestdate": null,
             "oldestage": 0,
             "size": 0,
             "uniquesize": 0
           } 

Copy

✔ Copied