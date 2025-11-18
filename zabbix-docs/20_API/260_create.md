---
title: script.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/script/create
downloaded: 2025-11-14 10:44:13
---

# script.create  
  
### Description

`object script.create(object/array scripts)`

This method allows to create new scripts.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Scripts to create.

The method accepts scripts with the [standard script properties](/documentation/current/en/manual/api/reference/script/object#script).

### Return values

`(object)` Returns an object containing the IDs of the created scripts under the `scriptids` property. The order of the returned IDs matches the order of the passed scripts.

### Examples

#### Create a webhook script

Create a webhook script that sends HTTP request to external service.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.create",
               "params": {
                   "name": "Webhook script",
                   "command": "try {\n var request = new HttpRequest(),\n response,\n data;\n\n request.addHeader('Content-Type: application/json');\n\n response = request.post('https://localhost/post', value);\n\n try {\n response = JSON.parse(response);\n }\n catch (error) {\n response = null;\n }\n\n if (request.getStatus() !== 200 || !('data' in response)) {\n throw 'Unexpected response.';\n }\n\n data = JSON.stringify(response.data);\n\n Zabbix.log(3, '[Webhook Script] response data: ' + data);\n\n return data;\n}\ncatch (error) {\n Zabbix.log(3, '[Webhook Script] script execution failed: ' + error);\n throw 'Execution failed: ' + error + '.';\n}",
                   "type": 5,
                   "timeout": "40s",
                   "parameters": [
                       {
                           "name": "token",
                           "value": "{$WEBHOOK.TOKEN}"
                       },
                       {
                           "name": "host",
                           "value": "{HOST.HOST}"
                       },
                       {
                           "name": "v",
                           "value": "2.2"
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
                   "scriptids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create an SSH script

Create an SSH script with public key authentication that can be executed on a host and has a context menu.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.create",
               "params": {
                   "name": "SSH script",
                   "command": "my script command",
                   "type": 2,
                   "authtype": 1,
                   "username": "John",
                   "publickey": "pub.key",
                   "privatekey": "priv.key",
                   "password": "secret",
                   "port": "12345",
                   "scope": 2,
                   "menu_path": "All scripts/SSH",
                   "usrgrpid": "7",
                   "groupid": "4"
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
                       "5"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create a custom script

Create a custom script that will reboot a server. The script will require write access to the host and will prompt the user for manual input. Upon successful input submission, script will display confirmation message in the frontend.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.create",
               "params": {
                   "name": "Reboot server",
                   "command": "reboot server {MANUALINPUT}",
                   "type": 0,
                   "scope": 2,
                   "confirmation": "Are you sure you would like to reboot the server {MANUALINPUT}?",
                   "manualinput": 1,
                   "manualinput_prompt": "Which server you want to reboot?",
                   "manualinput_validator": "[1-9]",
                   "manualinput_validator_type": 0,
                   "manualinput_default_value": "1"
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
                       "4"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create a URL type script

Create a URL type script for host scope that remains in the same window and has confirmation text.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.create",
               "params": {
                   "name": "URL script",
                   "type": 6,
                   "scope": 2,
                   "url": "http://zabbix/ui/zabbix.php?action=host.edit&hostid={HOST.ID}",
                   "confirmation": "Edit host {HOST.NAME}?",
                   "new_window": 0
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
                       "56"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Create a URL type script with manual input

Create a URL type script for event scope that opens in a new window and has manual input.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.create",
               "params": {
                   "name": "URL script with manual input",
                   "type": 6,
                   "scope": 4,
                   "url": "http://zabbix/ui/zabbix.php?action={MANUALINPUT}",
                   "new_window": 1,
                   "manualinput": 1,
                   "manualinput_prompt": "Select a page to open:",
                   "manualinput_validator": "dashboard.view,script.list,actionlog.list",
                   "manualinput_validator_type": 1
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
                       "57"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CScript::create() in _ui/include/classes/api/services/CScript.php_.