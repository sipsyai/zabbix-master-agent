---
title: History object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/history/object
downloaded: 2025-11-14 10:41:51
---

# History object

The following objects are directly related to the `history` API.

History objects differ depending on the item's type of information. They are created by Zabbix server and cannot be modified via the API.

### Float history

The float history object has the following properties.

clock | timestamp | Time when that value was received.  
---|---|---  
itemid | ID | ID of the related item.  
ns | integer | Nanoseconds when the value was received.  
value | float | Received value.  
  
### Integer history

The integer history object has the following properties.

clock | timestamp | Time when that value was received.  
---|---|---  
itemid | ID | ID of the related item.  
ns | integer | Nanoseconds when the value was received.  
value | integer | Received value.  
  
### String history

The string history object has the following properties.

clock | timestamp | Time when that value was received.  
---|---|---  
itemid | ID | ID of the related item.  
ns | integer | Nanoseconds when the value was received.  
value | string | Received value.  
  
### Text history

The text history object has the following properties.

id | ID | ID of the history entry.  
---|---|---  
clock | timestamp | Time when that value was received.  
itemid | ID | ID of the related item.  
ns | integer | Nanoseconds when the value was received.  
value | text | Received value.  
  
### Log history

The log history object has the following properties.

id | ID | ID of the history entry.  
---|---|---  
clock | timestamp | Time when that value was received.  
itemid | ID | ID of the related item.  
logeventid | integer | Windows event log entry ID.  
ns | integer | Nanoseconds when the value was received.  
severity | integer | Windows event log entry level.  
source | string | Windows event log entry source.  
timestamp | timestamp | Windows event log entry time.  
value | text | Received value.