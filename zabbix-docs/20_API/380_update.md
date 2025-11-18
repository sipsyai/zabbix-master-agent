---
title: httptest.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/httptest/update
downloaded: 2025-11-14 10:46:13
---

# httptest.update

### Description

`object httptest.update(object/array webScenarios)`

This method allows to update existing web scenarios.

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Web scenario properties to be updated.

The `httptestid` property must be defined for each web scenario, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

Additionally to the [standard web scenario properties](object#web-scenario), the method accepts the following parameters.

steps | array | [Scenario steps](/documentation/current/en/manual/api/reference/httptest/object#scenario-step) to replace existing steps.  
---|---|---  
tags | array | [Web scenario tags](/documentation/current/en/manual/api/reference/httptest/object#web-scenario-tag).  
  
### Return values

`(object)` Returns an object containing the IDs of the updated web scenarios under the `httptestid` property.

### Examples

#### Enabling a web scenario

Enable a web scenario, that is, set its status to "0".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "httptest.update",
               "params": {
                   "httptestid": "5",
                   "status": 0
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "httptestids": [
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Scenario step](object#scenario-step)

### Source

CHttpTest::update() in _ui/include/classes/api/services/CHttpTest.php_.