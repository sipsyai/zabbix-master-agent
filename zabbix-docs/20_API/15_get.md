---
title: auditlog.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/auditlog/get
downloaded: 2025-11-14 10:40:08
---

# auditlog.get  
  
### Description

`integer/array auditlog.get(object parameters)`

The method allows to retrieve audit log records according to the given parameters.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports the following parameters.

auditids | ID/array | Return only audit log with the given IDs.  
---|---|---  
userids | ID/array | Return only audit log that were created by the given users.  
time_from | timestamp | Returns only audit log entries that have been created after or at the given time.  
time_till | timestamp | Returns only audit log entries that have been created before or at the given time.  
sortfield | string/array | Sort the result by the given properties.  
  
Possible values: `auditid`, `userid`, `clock`.  
countOutput | boolean | These parameters are described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
excludeSearch | boolean  
filter | object  
limit | integer  
output | query  
preservekeys | boolean  
search | object  
searchByAny | boolean  
searchWildcardsEnabled | boolean  
sortorder | string/array  
startSearch | boolean  
  
### Return values

`(integer/array)` Returns either:

  * an array of objects;
  * the count of retrieved objects, if the `countOutput` parameter has been used.

### Examples

#### Retrieve audit log

Retrieve two latest audit log records.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "auditlog.get",
               "params": {
                   "output": "extend",
                   "sortfield": "clock",
                   "sortorder": "DESC",
                   "limit": 2
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   {
                       "auditid": "cksstgfam0001yhdcc41y20q2",
                       "userid": "1",
                       "username": "Admin",
                       "clock": "1629975715",
                       "ip": "127.0.0.1",
                       "action": "1",
                       "resourcetype": "0",
                       "resourceid": "0",
                       "resourcename": "Jim",
                       "recordsetid": "cksstgfal0000yhdcso67ondl",
                       "details": "{\"user.name\":[\"update\",\"Jim\",\"\"],\"user.medias[37]\":[\"add\"],\"user.medias[37].\":[\"add\"],\"user.medias[37].mediatypeid\":[\"add\",\"1\"],\"user.medias[37].sendto\":[\"add\",\"support123@company.com\"]}"
                   },
                   {
                       "auditid": "ckssofl0p0001yhdcqxclsg8r",
                       "userid": "1",
                       "username": "Admin",
                       "clock": "1629967278",
                       "ip": "127.0.0.1",
                       "action": "0",
                       "resourcetype": "0",
                       "resourceid": "20",
                       "resourcename": "John",
                       "recordsetid": "ckssofl0p0000yhdcpxyo1jgo",
                       "details": "{\"user.username\":[\"add\",\"John\"], \"user.userid:\":[\"add\",\"20\"],\"user.usrgrps[28]\":[\"add\"],\"user.usrgrps[28].usrgrpid\":[\"add\", \"7\"]}"
                   }
               ],
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Audit log object](/documentation/current/en/manual/api/reference/auditlog/object)

### Source

CAuditLog::get() in _ui/include/classes/api/services/CAuditLog.php_.