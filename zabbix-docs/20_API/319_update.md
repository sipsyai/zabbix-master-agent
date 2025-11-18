---
title: token.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/token/update
downloaded: 2025-11-14 10:45:12
---

# token.update

### Description

`object token.update(object/array tokens)`

This method allows to update existing tokens.

The _Manage API tokens_ [permission](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles#configuration) is required for the user role to manage tokens for other users.

### Parameters

`(object/array)` Token properties to be updated.

The `tokenid` property must be defined for each token, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged.

The method accepts tokens with the [standard token properties](object).

### Return values

`(object)` Returns an object containing the IDs of the updated tokens under the `tokenids` property.

### Examples

#### Remove token expiry

Remove expiry date from token.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "token.update",
               "params": {
                   "tokenid": "2",
                   "expires_at": "0"
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
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CToken::update() in _ui/include/classes/api/services/CToken.php_.