---
title: correlation.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/correlation/delete
downloaded: 2025-11-14 10:40:30
---

# correlation.delete

### Description

`object correlation.delete(array correlationids)`

This method allows to delete correlations.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the correlations to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted correlations under the `correlationids` property.

### Example

#### Delete multiple correlations

Delete two correlations.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "correlation.delete",
               "params": [
                   "1",
                   "2"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "correlationids": [
                       "1",
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CCorrelation::delete() in _ui/include/classes/api/services/CCorrelation.php_.