---
title: token.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/token/delete
downloaded: 2025-11-14 10:45:09
---

# token.delete

### Description

`object token.delete(array tokenids)`

This method allows to delete tokens.

The _Manage API tokens_ [permission](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles#configuration) is required for the user role to manage tokens for other users.

### Parameters

`(array)` IDs of the tokens to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted tokens under the `tokenids` property.

### Examples

#### Delete multiple tokens

Delete two tokens.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "token.delete",
               "params": [
                   "188",
                   "192"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "tokenids": [
                       "188",
                       "192"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CToken::delete() in _ui/include/classes/api/services/CToken.php_.