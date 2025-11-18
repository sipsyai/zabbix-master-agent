---
title: Passive and active agent checks
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/activepassive
downloaded: 2025-11-14 10:47:20
---

# 2 Passive and active agent checks

#### Overview

This section provides details on passive and active checks performed by [Zabbix agent](/documentation/current/en/manual/concepts/agent) and [Zabbix agent 2](/documentation/current/en/manual/concepts/agent2).

Zabbix uses a JSON-based communication protocol for communicating with the agents.

Zabbix agent and Zabbix agent 2 protocols have been unified since Zabbix 7.0. The difference between Zabbix agent and Zabbix agent 2 requests/responses is expressed by the "variant" tag value.

#### Passive checks

A passive check is a simple data request. Zabbix server or proxy asks for some data (for example, CPU load) and Zabbix agent sends back the result to the server.

Passive checks are executed asynchronously - it is not required to receive the response to one request before other checks are started. DNS resolving is asynchronous as well.

The agent poller will attempt to connect to all addresses returned by the DNS lookup. This ensures that if one IP address is unreachable, the poller will try the next available address, increasing the likelihood of a successful connection. This enhancement applies to both Zabbix server and proxy.

The maximum concurrency of asynchronous checks is 1000 (defined by [MaxConcurrentChecksPerPoller](/documentation/current/en/manual/appendix/config/zabbix_server#maxconcurrentchecksperpoller)).

The number of asynchronous agent pollers is defined by the [StartAgentPollers](/documentation/current/en/manual/appendix/config/zabbix_server#startagentpollers) parameter.

**Server request**

For definition of header and data length please refer to [protocol details](/documentation/current/en/manual/appendix/protocols/header_datalen).
    
    
    {
             "request": "passive checks",
             "data": [
               {
                 "key": "agent.version",
                 "timeout": 3
               }
             ]
           }

Copy

✔ Copied

request | _string_ | yes | `"passive checks"`  
---|---|---|---  
data | _array of object_ | yes | Passive check item.  
| key | _string_ | yes | Item key with expanded macros.  
timeout | _string_ | yes | Item timeout.  
  
**Agent response**
    
    
    {
             "version": "7.4.0",
             "variant": 2,
             "data": [
               {
                 "value": "7.4.0"
               }
             ]
           }

Copy

✔ Copied

version | _string_ | yes | The agent version number.  
---|---|---|---  
variant | _number_ | yes | The agent variant (_1_ \- Zabbix agent, _2_ \- Zabbix agent 2).  
data | _array of object_ | yes | Contains the result of the check.  
| value | _string_ | no | The item value if the check was successful.  
| error | _string_ | no | The error message if the check was not successful.  
  
For example, for supported items:

  1. Server opens a TCP connection
  2. Server sends **< HEADER><DATALEN>{"request":"passive checks","data":[{"key":"agent.ping","timeout":3}]}**
  3. Agent reads the request and responds with **< HEADER><DATALEN>{"version":"7.4.0","variant":2,"data":[{"value":1}]}**
  4. Server processes data to get the value, '1' in our case
  5. TCP connection is closed

For not supported items:

  1. Server opens a TCP connection
  2. Server sends **< HEADER><DATALEN>{"request":"passive checks","data":[{"key":"vfs.fs.size[/nono]","timeout":3}]}**
  3. Agent reads the request and responds with **< HEADER><DATALEN>{"version":"7.4.0","variant":2,"data":[{"error":"Unsupported item key."}]}**
  4. Server processes data, changes item state to not supported with the specified error message
  5. TCP connection is closed

##### Failover to old protocol

To make sure that Zabbix server or proxy can work with agents from pre-7.2 versions, which have plaintext protocol, a failover to the old protocol is implemented.

Passive checks are performed using the JSON protocol (7.0 and later) after restart or when the interface configuration is changed. If no valid JSON is received in response (agent sent "ZBX_NOTSUPPORTED"), Zabbix will cache the interface as old protocol and **retry** the check by sending only the item key.

Note that every hour Zabbix server/proxy will again try working with the new protocol with all interfaces, falling back to the old protocol if required.

#### Active checks

Active checks require more complex processing. The agent must first retrieve from the server/proxy a list of items and/or [remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command) for independent processing.

The servers/proxies to get the active checks from are listed in the 'ServerActive' parameter of the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agent2). The frequency of asking for these checks is set by the 'RefreshActiveChecks' parameter in the same configuration file. However, if refreshing active checks fails, it is retried after hardcoded 60 seconds.

Since Zabbix 6.4 the agent (in active mode) no longer receives from the server/proxy a full copy of the configuration once every two minutes (default). Instead, in order to decrease network traffic and resources usage, an incremental configuration sync is performed every 5 seconds (default) upon which the server/proxy provides a full copy of the configuration **only** if the agent has not yet received it, or something has changed in host configuration, global macros or global regular expressions.

The agent then periodically sends the new values to the server(s). If the agent received any [remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command) to execute, the execution result will also be sent. Note that remote command execution on an active agent is supported since Zabbix agent 7.0.

If an agent is behind the firewall you might consider using only Active checks because in this case you wouldn't need to modify the firewall to allow initial incoming connections.

##### Getting the list of items

**Agent request**

The active checks request is used to obtain the active checks to be processed by agent. This request is sent by the agent upon start and then with [RefreshActiveChecks](/documentation/current/en/manual/appendix/config/zabbix_agent2) intervals.
    
    
    {
             "request": "active checks",
             "host": "Zabbix server",
             "host_metadata": "mysql,nginx",
             "interface": "zabbix.server.lan",
             "ip": "159.168.1.1",
             "port": 12050,
             "version": "7.4.0",
             "variant": 2,
             "config_revision": 1,
             "session": "e3dcbd9ace2c9694e1d7bbd030eeef6e"
           }

Copy

✔ Copied

request | _string_ | yes | `active checks`  
---|---|---|---  
host | _string_ | yes | Host name.  
host_metadata | _string_ | no | The configuration parameter HostMetadata or HostMetadataItem metric value.  
interface | _string_ | no | The configuration parameter HostInterface or HostInterfaceItem metric value.  
ip | _string_ | no | The configuration parameter ListenIP first IP if set.  
port | _number_ | no | The configuration parameter ListenPort value if set and not default agent listening port.  
version | _string_ | yes | The agent version number.  
variant | _number_ | yes | The agent variant (_1_ \- Zabbix agent, _2_ \- Zabbix agent 2).  
config_revision | _number_ | no | Configuration identifier for incremental configuration sync.  
session | _string_ | no | Session identifier for incremental configuration sync.  
  
**Server response**

The active checks response is sent by the server back to agent after processing the active checks request.
    
    
    {
             "response": "success",
             "config_revision": 2,
             "data": [
               {
                 "key": "system.uptime",
                 "itemid": 1234,
                 "delay": "10s",
                 "lastlogsize": 0,
                 "mtime": 0
               },
               {
                 "key": "agent.version",
                 "itemid": 5678,
                 "delay": "10m",
                 "lastlogsize": 0,
                 "mtime": 0,
                 "timeout": "30s"
               }
             ],
             "commands": [
               {
                 "command": "df -h --output=source,size / | awk 'NR>1 {print $2}'",
                 "id": 1324,
                 "wait": 1
               }
             ]
           }

Copy

✔ Copied

response | _string_ | yes | `success` | `failed`  
---|---|---|---  
info | _string_ | no | Error information in case of failure.  
data | _array of objects_ | no | Active check items. Omitted if host configuration is unchanged.  
| key | _string_ | no | Item key with expanded macros.  
itemid | _number_ | no | Item identifier.  
delay | _string_ | no | Item update interval.  
Flexible/scheduling intervals are supported by both Zabbix agent and Zabbix agent 2 since Zabbix 7.0.  
lastlogsize | _number_ | no | Item lastlogsize.  
mtime | _number_ | no | Item mtime.  
timeout | _string_ | no | Item timeout.  
refresh_unsupported | _number_ | no | Unsupported item refresh interval.  
regexp | _array of objects_ | no | Global regular expressions.  
| name | _string_ | no | Global regular expression name.  
expression | _string_ | no | Global regular expression.  
expression_type | _number_ | no | Global regular expression type.  
exp_delimiter | _string_ | no | Global regular expression delimiter.  
case_sensitive | _number_ | no | Global regular expression case sensitivity setting.  
commands | _array of objects_ | no | Remote commands to execute. Included if remote command execution has been triggered by an action [operation](/documentation/current/en/manual/config/notifications/action/operation#operations) or manual [script](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) execution. Note that remote command execution on an active agent is supported since Zabbix agent 7.0. Older active agents will ignore any remote commands included in the active checks server response.  
| command | _string_ | no | Remote command.  
id | _number_ | no | Remote command identifier.  
wait | _number_ | no | Remote command mode of execution ("0" (nowait) for commands from action [operations](/documentation/current/en/manual/config/notifications/action/operation#operations); "1" (wait) for commands from manual [script](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) execution).  
config_revision | _number_ | no | Configuration identifier for incremental configuration sync. Omitted if host configuration is unchanged. Incremented if host configuration is changed.  
  
The server must respond with success.

For example:

  1. Agent opens a TCP connection
  2. Agent asks for the list of checks
  3. Server responds with a list of items and remote commands to execute
  4. Agent parses the response
  5. TCP connection is closed
  6. Agent starts periodical collection of data and executes remote commands (supported since Zabbix agent 7.0)

Note that (sensitive) configuration data may become available to parties having access to the Zabbix server trapper port when using an active check. This is possible because anyone may pretend to be an active agent and request item configuration data; authentication does not take place unless you use [encryption](/documentation/current/en/manual/encryption) options.

##### Sending in collected data

**Agent sends**

The agent data request contains the gathered item values and the values for executed remote commands (if any).
    
    
    {
             "request": "agent data",
             "data": [
               {
                 "id": 1,
                 "itemid": 5678,
                 "value": "7.0.0",
                 "clock": 1712830783,
                 "ns": 76808644
               },
               {
                 "id": 2,
                 "itemid": 1234,
                 "value": "69672",
                 "clock": 1712830783,
                 "ns": 77053975
               }
             ],
             "commands": [
               {
                 "id": 1324,
                 "value": "16G"
               }
             ],
             "session": "1234456akdsjhfoui",
             "host": "Zabbix server",
             "version": "7.4.0",
             "variant": 2
           }

Copy

✔ Copied

request | _string_ | yes | `agent data`  
---|---|---|---  
data | _array of objects_ | yes | Item values.  
| id | _number_ | yes | The value identifier (incremental counter used for checking duplicated values in the case of network problems).  
itemid | _string_ | yes | The item identifier.  
value | _string_ | no | The item value.  
lastlogsize | _number_ | no | The item lastlogsize.  
mtime | _number_ | no | The item mtime.  
state | _number_ | no | The item state.  
source | _string_ | no | The value event log source.  
eventid | _number_ | no | The value event log eventid.  
severity | _number_ | no | The value event log severity.  
timestamp | _number_ | no | The value event log timestamp.  
clock | _number_ | yes | The value timestamp (seconds since Epoch).  
ns | _number_ | yes | The value timestamp nanoseconds.  
commands | _array of objects_ | no | Remote commands execution result. Note that remote command execution on an active agent is supported since Zabbix agent 7.0. Older active agents will ignore any remote commands included in the active checks server response.  
| id | _number_ | no | Remote command identifier.  
value | _string_ | no | Remote command execution result if the execution was successful.  
error | _string_ | no | Remote command execution error message if the execution failed.  
session | _string_ | yes | Unique session identifier generated each time when agent is started.  
host | _string_ | yes | Host name.  
version | _string_ | yes | The agent version number.  
variant | _number_ | yes | The agent variant (_1_ \- Zabbix agent, _2_ \- Zabbix agent 2).  
  
A virtual ID is assigned to each value. Value ID is a simple ascending counter, unique within one data session (identified by the session token). This ID is used to discard duplicate values that might be sent in poor connectivity environments.

**Server response**

The agent data response is sent by the server back to the agent after processing the agent data request.
    
    
    {
             "response": "success",
             "info": "processed: 2; failed: 0; total: 2; seconds spent: 0.003534"
           }

Copy

✔ Copied

response | _string_ | yes | `success` | `failed`  
---|---|---|---  
info | _string_ | yes | Item processing results.  
  
If sending of some values fails on the server (for example, because host or item has been disabled or deleted), agent will not retry sending of those values.

For example:

  1. Agent opens a TCP connection
  2. Agent sends a list of values
  3. Server processes the data and sends the status back
  4. TCP connection is closed

Note how in the example above the not supported status for vfs.fs.size[/nono] is indicated by the "state" value of 1 and the error message in "value" property.

Error message will be trimmed to 2048 symbols on server side.

##### Heartbeat message

**Agent sends**

The heartbeat message is sent by an active agent to Zabbix server/proxy every HeartbeatFrequency seconds (configured in the [Zabbix agent](/documentation/current/en/manual/appendix/config/zabbix_agentd)/ [agent 2](/documentation/current/en/manual/appendix/config/zabbix_agent2) configuration file).

It is used to monitor the availability of active checks.
    
    
    {
             "request": "active check heartbeat",
             "host": "Zabbix server",
             "heartbeat_freq": 60,
             "version": "7.4.0",
             "variant": 2
           }

Copy

✔ Copied

request | _string_ | yes | `active check heartbeat`  
---|---|---|---  
host | _string_ | yes | The host name.  
heartbeat_freq | _number_ | yes | The agent heartbeat frequency (HeartbeatFrequency configuration parameter).  
version | _string_ | yes | The agent version number.  
variant | _number_ | yes | The agent variant (_1_ \- Zabbix agent, _2_ \- Zabbix agent 2).  
  
**Redirect response**

When a host has been reassigned, the server may instruct the agent to redirect its heartbeat (and subsequent active checks) to another proxy or server instance.
    
    
      {
               "response": "failed",
               "redirect": {
                 "revision": 2,
                 "address": "192.0.2.0:10055"
               }
             }

Copy

✔ Copied

response | _string_ | yes | `success` | `failed`  
---|---|---|---  
redirect | _object_ | yes | Redirect instructions.  
| revision | _number_ | yes | Configuration revision identifier.  
address | _string_ | yes | Target server/proxy address.  
  
#### Older XML protocol

Zabbix will take up to 16 MB of XML Base64-encoded data, but a single decoded value should be no longer than 64 KB otherwise it will be truncated to 64 KB while decoding.