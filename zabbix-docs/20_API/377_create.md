---
title: httptest.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/httptest/create
downloaded: 2025-11-14 10:46:10
---

# httptest.create  
  
### Description

`object httptest.create(object/array webScenarios)`

This method allows to create new web scenarios.

Creating a web scenario will automatically create a set of [web monitoring items](/documentation/current/en/manual/web_monitoring/items).

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Web scenarios to create.

Additionally to the [standard web scenario properties](object#web-scenario), the method accepts the following parameters.

steps | array | [Scenario steps](/documentation/current/en/manual/api/reference/httptest/object#scenario-step).  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
tags | array | [Web scenario tags](/documentation/current/en/manual/api/reference/httptest/object#web-scenario-tag).  
  
### Return values

`(object)` Returns an object containing the IDs of the created web scenarios under the `httptestids` property. The order of the returned IDs matches the order of the passed web scenarios.

### Examples

#### Creating a web scenario

Create a web scenario to monitor the company home page. The scenario will have two steps, to check the home page and the "About" page and make sure they return the HTTP status code 200.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "httptest.create",
               "params": {
                   "name": "Homepage check",
                   "hostid": "10085",
                   "steps": [
                       {
                           "name": "Homepage",
                           "url": "http://example.com",
                           "status_codes": "200",
                           "no": 1
                       },
                       {
                           "name": "Homepage / About",
                           "url": "http://example.com/about",
                           "status_codes": "200",
                           "no": 2
                       }
                   ]
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

CHttpTest::create() in _ui/include/classes/api/services/CHttpTest.php_.