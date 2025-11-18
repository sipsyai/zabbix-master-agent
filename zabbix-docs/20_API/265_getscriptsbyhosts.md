---
title: script.getscriptsbyhosts
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/script/getscriptsbyhosts
downloaded: 2025-11-14 10:44:18
---

# script.getscriptsbyhosts

### Description

`object script.getscriptsbyhosts(object parameters)`

This method allows to retrieve all available scripts on the given host or specific script if script ID is provided. When manualinput is provided, it substitutes the {MANUALINPUT} macro with the specified value.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` The method accepts object or array of objects with the following parameters.

hostid | ID | ID of host to return scripts for.  
Must be unique.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
scriptid | ID | ID of script to return.  
manualinput | string | Value of the user-provided {MANUALINPUT} macro value.  
  
### Return values

`(object)` Returns an object with host IDs as properties and arrays of available scripts as values. If script ID is provided, the associated value is an array containing the specific script.

The method will automatically expand macros in the `confirmation` text, `manualinput prompt` text and `url`.

If the manualinput parameter is provided, the {MANUALINPUT} macro will be resolved to the specified value.

### Examples

#### Retrieve scripts by host IDs

Retrieve all scripts available on hosts "30079" and "30073".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.getscriptsbyhosts",
               "params": [
                  {
                     "hostid":  "30079"
                  },
                  {
                     "hostid":  "30073"
                  }
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "30079": [
                       {
                           "scriptid": "3",
                           "name": "Detect operating system",
                           "command": "sudo /usr/bin/nmap -O {HOST.CONN} 2>&1",
                           "host_access": "2",
                           "usrgrpid": "7",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "",
                           "type": "0",
                           "execute_on": "1",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "",
                           "manualinput_default_value": "",
                           "parameters": []
                       },
                       {
                           "scriptid": "1",
                           "name": "Ping",
                           "command": "/bin/ping -c 3 {HOST.CONN} 2>&1",
                           "host_access": "2",
                           "usrgrpid": "0",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "",
                           "type": "0",
                           "execute_on": "1",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "",
                           "manualinput_default_value": "",
                           "parameters": []
                       },
                       {
                           "scriptid": "4",
                           "name": "Open Zabbix page",
                           "command": "",
                           "host_access": "2",
                           "usrgrpid": "0",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "Are you sure you want to open page *UNKNOWN*?",
                           "type": "6",
                           "execute_on": "2",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "http://localhost/ui/zabbix.php?action=*UNKNOWN*",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "Zabbix page to open:",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "dashboard.view,discovery.view",
                           "manualinput_default_value": "",
                           "parameters": []
                       },
                       {
                           "scriptid": "2",
                           "name": "Traceroute",
                           "command": "/usr/bin/traceroute {HOST.CONN} 2>&1",
                           "host_access": "2",
                           "usrgrpid": "0",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "",
                           "type": "0",
                           "execute_on": "1",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "",
                           "manualinput_default_value": "",
                           "parameters": []
                       }
                   ],
                   "30073": [
                       {
                           "scriptid": "3",
                           "name": "Detect operating system",
                           "command": "sudo /usr/bin/nmap -O {HOST.CONN} 2>&1",
                           "host_access": "2",
                           "usrgrpid": "7",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "",
                           "type": "0",
                           "execute_on": "1",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "",
                           "manualinput_default_value": "",
                           "parameters": []
                       },
                       {
                           "scriptid": "1",
                           "name": "Ping",
                           "command": "/bin/ping -c 3 {HOST.CONN} 2>&1",
                           "host_access": "2",
                           "usrgrpid": "0",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "",
                           "type": "0",
                           "execute_on": "1",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "",
                           "manualinput_default_value": "",
                           "parameters": []
                       },
                       {
                           "scriptid": "4",
                           "name": "Open Zabbix page",
                           "command": "",
                           "host_access": "2",
                           "usrgrpid": "0",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "Are you sure you want to open page *UNKNOWN*?",
                           "type": "6",
                           "execute_on": "2",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "http://localhost/ui/zabbix.php?action=*UNKNOWN*",
                           "new_window": "1",
                           "manualinput": "1",
                           "manualinput_prompt": "Zabbix page to open:",
                           "manualinput_validator_type": "1",
                           "manualinput_validator": "dashboard.view,discovery.view",
                           "manualinput_default_value": "",
                           "parameters": []
                       },
                       {
                           "scriptid": "2",
                           "name": "Traceroute",
                           "command": "/usr/bin/traceroute {HOST.CONN} 2>&1",
                           "host_access": "2",
                           "usrgrpid": "0",
                           "groupid": "0",
                           "description": "",
                           "confirmation": "",
                           "type": "0",
                           "execute_on": "1",
                           "timeout": "30s",
                           "scope": "2",
                           "port": "",
                           "authtype": "0",
                           "username": "",
                           "password": "",
                           "publickey": "",
                           "privatekey": "",
                           "menu_path": "",
                           "url": "",
                           "new_window": "1",
                           "manualinput": "0",
                           "manualinput_prompt": "",
                           "manualinput_validator_type": "0",
                           "manualinput_validator": "",
                           "manualinput_default_value": "",
                           "parameters": []
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Retrieve specific script with manualinput value.

Retrieve script with ID "4" on host "30079" with manualinput value "dashboard.view".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.getscriptsbyhosts",
               "params": [
                 {
                   "hostid":  "30079",
                   "scriptid": "4",
                   "manualinput": "dashboard.view"
                 }
             ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                 "30079": [
                   {
                     "scriptid": "4",
                     "name": "Open Zabbix page",
                     "command": "",
                     "host_access": "2",
                     "usrgrpid": "0",
                     "groupid": "0",
                     "description": "",
                     "confirmation": "Are you sure you want to open page dashboard.view?",
                     "type": "6",
                     "execute_on": "2",
                     "timeout": "30s",
                     "scope": "2",
                     "port": "",
                     "authtype": "0",
                     "username": "",
                     "password": "",
                     "publickey": "",
                     "privatekey": "",
                     "menu_path": "",
                     "url": "http://localhost/ui/zabbix.php?action=dashboard.view",
                     "new_window": "1",
                     "manualinput": "1",
                     "manualinput_prompt": "Zabbix page to open:",
                     "manualinput_validator_type": "1",
                     "manualinput_validator": "dashboard.view,discovery.view",
                     "manualinput_default_value": "",
                     "parameters": []
                   }
                 ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CScript::getScriptsByHosts() in _ui/include/classes/api/services/CScript.php_.