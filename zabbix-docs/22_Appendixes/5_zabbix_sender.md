---
title: Zabbix sender protocol
source: https://www.zabbix.com/documentation/current/en/manual/appendix/protocols/zabbix_sender
downloaded: 2025-11-14 10:47:15
---

# 5 Zabbix sender protocol

#### Overview

Zabbix server and Zabbix proxy use a JSON-based communication protocol for receiving data from Zabbix sender. Data can be received with the help of a [trapper item](/documentation/current/en/manual/config/items/itemtypes/trapper), or an [HTTP agent item](/documentation/current/en/manual/config/items/itemtypes/http) with trapping enabled.

Request and response messages must begin with [header and data length](/documentation/current/en/manual/appendix/protocols/header_datalen).

#### Zabbix sender request
    
    
    {
               "request": "sender data",
               "data": [
                   {
                       "host": "<hostname>",
                       "key": "trap",
                       "value": "test value"
                   }
               ]
           }

Copy

✔ Copied

#### Zabbix server response
    
    
    {
               "response": "success",
               "info": "processed: 1; failed: 0; total: 1; seconds spent: 0.060753"
           }

Copy

✔ Copied

#### Zabbix sender request with a timestamp

Alternatively, Zabbix sender can send a request with a timestamp and nanoseconds.
    
    
    {
               "request": "sender data",
               "data": [
                   {
                       "host": "<hostname>",
                       "key": "trap",
                       "value": "test value",
                       "clock": 1516710794,
                       "ns": 592397170
                   },
                   {
                       "host": "<hostname>",
                       "key": "trap",
                       "value": "test value",
                       "clock": 1516710795,
                       "ns": 192399456
                   }
               ],
               "clock": 1516712029,
               "ns": 873386094
           }

Copy

✔ Copied

#### Zabbix server response
    
    
    {
               "response": "success",
               "info": "processed: 2; failed: 0; total: 2; seconds spent: 0.060904"
           }

Copy

✔ Copied