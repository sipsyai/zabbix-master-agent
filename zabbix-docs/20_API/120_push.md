---
title: history.push
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/history/push
downloaded: 2025-11-14 10:41:53
---

# history.push

#### Description

`object history.push(object/array itemHistoryData)`

This method allows sending item history data to Zabbix server.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

#### Parameters

`(object/array)` Item history data to send.

The method supports the following parameters.

itemid | ID | ID of the related item.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `host` and `key` are not set  
---|---|---  
host | string | Technical name of the host.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `itemid` is not set  
key | string | Item key.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `itemid` is not set  
value | mixed | Item value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
clock | timestamp | Time when the value was received.  
ns | integer | Nanoseconds when the value was received.  
  
#### Return values

`(object)` Returns the result of the data sending operation.

#### Examples

##### Send item history data

Send item history data to Zabbix server for items "10600", "10601", and "999999".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "history.push",
               "params": [
                   {
                       "itemid": 10600,
                       "value": 0.5,
                       "clock": 1690891294,
                       "ns": 45440940
                   },
                   {
                       "itemid": 10600,
                       "value": 0.6,
                       "clock": 1690891295,
                       "ns": 312431
                   },
                   {
                       "itemid": 10601,
                       "value": "[Tue Aug 01 15:01:35 2023] [error] [client 1.2.3.4] File does not exist: /var/www/html/robots.txt"
                   },
                   {
                       "itemid": 999999,
                       "value": 123
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "response": "success",
                   "data": [
                       {
                           "itemid": "10600"
                       },
                       {
                           "itemid": "10600"
                       },
                       {
                           "itemid": "10601",
                           "error": "Item is disabled."
                       },
                       {
                           "error": "No permissions to referred object or it does not exist."
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### See also

  * [Trapper items](/documentation/current/en/manual/config/items/itemtypes/trapper#sending-data)
  * [HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http) items
  * [Host](/documentation/current/en/manual/api/reference/host/object#host)
  * [Item](/documentation/current/en/manual/api/reference/item/object#item)

#### Source

CHistory::push() in _ui/include/classes/api/services/CHistory.php_.