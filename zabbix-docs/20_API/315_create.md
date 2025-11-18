---
title: token.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/token/create
downloaded: 2025-11-14 10:45:08
---

# token.create  
  
### Description

`object token.create(object/array tokens)`

This method allows to create new tokens.

The _Manage API tokens_ [permission](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles#configuration) is required for the user role to manage tokens for other users.

A token created by this method also has to be [generated](generate) before it is usable.

### Parameters

`(object/array)` Tokens to create.

The method accepts tokens with the [standard token properties](object).

### Return values

`(object)` Returns an object containing the IDs of the created tokens under the `tokenids` property. The order of the returned IDs matches the order of the passed tokens.

### Examples

#### Create a token

Create an enabled token that never expires and authenticates user of ID 2.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "token.create",
               "params": {
                   "name": "Your token",
                   "userid": "2"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "tokenids": [
                       "188"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Create a disabled token that expires at January 21st, 2021. This token will authenticate current user.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "token.create",
               "params": {
                   "name": "Your token",
                   "status": "1",
                   "expires_at": "1611238072"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "tokenids": [
                       "189"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CToken::create() in _ui/include/classes/api/services/CToken.php_.