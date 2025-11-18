---
title: script.execute
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/script/execute
downloaded: 2025-11-14 10:44:15
---

# script.execute

### Description

`object script.execute(object parameters)`

This method allows to run a script on a host or event. Except for URL type scripts. Those are not executable.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the ID of the script to run, either the ID of the host or the ID of the event and manualinput value.

scriptid | ID | ID of the [script](/documentation/current/en/manual/api/reference/script/object#script) to run.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
hostid | ID | ID of the [host](/documentation/current/en/manual/api/reference/host/object#host) to run the script on.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `eventid` is not set  
eventid | ID | ID of the [event](/documentation/current/en/manual/api/reference/event/object#event) to run the script on.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if `hostid` is not set  
manualinput | string | User-provided value to run the script with, substituting   
the {MANUALINPUT} macro.  
  
### Return values

`(object)` Returns the result of script execution.

response | string | Whether the script was run successfully.  
  
Possible value - `success`.  
---|---|---  
value | string | Script output.  
debug | object | Contains a [debug](/documentation/current/en/manual/api/reference/script/object#debug) object if a webhook script is executed. For other script types, it contains empty object.  
  
### Examples

#### Run a webhook script

Run a webhook script that sends HTTP request to external service.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.execute",
               "params": {
                   "scriptid": "4",
                   "hostid": "30079"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "response": "success",
                   "value": "{\"status\":\"sent\",\"timestamp\":\"1611235391\"}",
                   "debug": {
                       "logs": [
                            {
                                "level": 3,
                                "ms": 480,
                                "message": "[Webhook Script] HTTP status: 200."
                            }
                        ],
                        "ms": 495
                   }
               },
               "id": 1
           }

Copy

✔ Copied

#### Run a custom script

Run a "ping" script on a host.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.execute",
               "params": {
                   "scriptid": "1",
                   "hostid": "30079"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "response": "success",
                   "value": "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_req=1 ttl=64 time=0.074 ms\n64 bytes from 127.0.0.1: icmp_req=2 ttl=64 time=0.030 ms\n64 bytes from 127.0.0.1: icmp_req=3 ttl=64 time=0.030 ms\n\n--- 127.0.0.1 ping statistics ---\n3 packets transmitted, 3 received, 0% packet loss, time 1998ms\nrtt min/avg/max/mdev = 0.030/0.044/0.074/0.022 ms\n",
                   "debug": []
               },
               "id": 1
           }

Copy

✔ Copied

#### Run a custom script with manual input

Run a "ping" script with command "ping -c {MANUALINPUT} {HOST.CONN}; case $? in [01]) true;; *) false;; esac" on a host.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "script.execute",
               "params": {
                   "scriptid": "7",
                   "hostid": "30079",
                   "manualinput": "2"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "response": "success",
                   "value": "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.051 ms\n64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.025 ms\n\n--- 127.0.0.1 ping statistics ---\n2 packets transmitted, 2 received, 0% packet loss, time 1021ms\nrtt min/avg/max/mdev = 0.025/0.038/0.051/0.013 ms",
                   "debug": []
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CScript::execute() in _ui/include/classes/api/services/CScript.php_.