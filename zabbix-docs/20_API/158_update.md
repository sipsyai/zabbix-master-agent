---
title: housekeeping.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/housekeeping/update
downloaded: 2025-11-14 10:42:31
---

# housekeeping.update

### Description

`object housekeeping.update(object housekeeping)`

This method allows to update existing housekeeping settings.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` [Housekeeping properties](object#housekeeping) to be updated.

### Return values

`(array)` Returns an array with the names of updated parameters.

### Examples

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "housekeeping.update",
               "params": {
                   "hk_events_mode": "1",
                   "hk_events_trigger": "200d",
                   "hk_events_internal": "2d",
                   "hk_events_discovery": "2d"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": [
                   "hk_events_mode",
                   "hk_events_trigger",
                   "hk_events_internal",
                   "hk_events_discovery"
               ],
               "id": 1
           }

Copy

✔ Copied

### Source

CHousekeeping::update() in _ui/include/classes/api/services/CHousekeeping.php_.