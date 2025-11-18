---
title: httptest.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/httptest/delete
downloaded: 2025-11-14 10:46:11
---

# httptest.delete

### Description

`object httptest.delete(array webScenarioIds)`

This method allows to delete web scenarios.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the web scenarios to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted web scenarios under the `httptestids` property.

### Examples

#### Deleting multiple web scenarios

Delete two web scenarios.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "httptest.delete",
               "params": [
                   "2",
                   "3"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "httptestids": [
                       "2",
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CHttpTest::delete() in _ui/include/classes/api/services/CHttpTest.php_.