---
title: script.update
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/script/update
downloaded: 2025-11-14 10:44:19
---

# script.update

### Description

`object script.update(object/array scripts)`

This method allows to update existing scripts.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` [Script properties](object#script) to be updated.

The `scriptid` property must be defined for each script, all other properties are optional. Only the passed properties will be updated, all others will remain unchanged. An exception is `type` property change from 5 (Webhook) to other: the `parameters` property will be cleaned.

### Return values

`(object)` Returns an object containing the IDs of the updated scripts under the `scriptids` property.

### Examples

#### Change script command

Change the command of the script to "/bin/ping -c 10 {HOST.CONN} 2>&1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.update",
               "params": {
                   "scriptid": "1",
                   "command": "/bin/ping -c 10 {HOST.CONN} 2>&1"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "scriptids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Change script command and add manual input

Change the command of the script to "/bin/ping -c {MANUALINPUT} {HOST.CONN} 2>&1".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.update",
               "params": {
                 "scriptid": "1",
                 "command": "/bin/ping -c {MANUALINPUT} {HOST.CONN} 2>&1",
                 "manualinput": "1",
                 "manualinput_prompt": "Specify the number of ICMP packets to send with the ping command",
                 "manualinput_validator": "^(?:[1-9]|10)$",
                 "manualinput_validator_type": "0",
                 "manualinput_default_value": "10"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "scriptids": [
                       "1"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CScript::update() in _ui/include/classes/api/services/CScript.php_.