---
title: Zabbix agent 2 plugin protocol
source: https://www.zabbix.com/documentation/current/en/manual/appendix/protocols/zabbix_agent2_plugin
downloaded: 2025-11-14 10:47:14
---

# 4 Zabbix agent 2 plugin protocol

Zabbix agent 2 protocol is based on code, size and data model.

### Code

Byte | 4 | Payload type, currently only JSON is supported.  
---|---|---  
  
### Size

Byte | 4 | Size of the current payload in bytes.  
---|---|---  
  
### Payload data

Byte | Defined by the _Size_ field | JSON formatted data.  
---|---|---  
  
##### Payload data definition

###### Common data

These parameters are present in all requests/responses:

id | uint32 | For requests - the incrementing identifier used to link requests with responses. Unique within a request direction (i.e. from agent to plugin or from plugin to agent).  
For responses - ID of the corresponding request.  
---|---|---  
type | uint32 | The request type.  
  
###### Log request

A request sent by a plugin to write a log message into the agent log file.

direction | plugin → agent  
---|---  
response | no  
  
Parameters specific to log requests:

severity | uint32 | The message severity (log level).  
---|---|---  
message | string | The message to log.  
  
_Example:_
    
    
    {"id":0,"type":1,"severity":3,"message":"message"}

Copy

✔ Copied

###### Register request

A request sent by the agent during the agent startup phase to obtain provided metrics to register a plugin.

direction | agent → plugin  
---|---  
response | yes  
  
Parameters specific to register requests:

version | string | The protocol version <major>.<minor>  
---|---|---  
  
_Example:_
    
    
    {"id":1,"type":2,"version":"1.0"}

Copy

✔ Copied

###### Register response

Plugin's response to the register request.

direction | plugin → agent  
---|---  
response | n/a  
  
Parameters specific to register responses:

name | string | The plugin name.  
---|---|---  
metrics | array of strings (optional) | The metrics with descriptions as used in the plugin. Returns RegisterMetrics(). Absent if error is returned.  
interfaces | uint32 (optional) | The bit mask of plugin's supported interfaces. Absent if error is returned.  
error | string (optional) | An error message returned if a plugin cannot be started. Absent, if metrics are returned.  
  
_Examples:_
    
    
    {"id":2,"type":3,"metrics":["external.test", "External exporter Test."], "interfaces": 4}

Copy

✔ Copied

or
    
    
    {"id":2,"type":3,"error":"error message"}

Copy

✔ Copied

###### Start request

A request to execute the Start function of the Runner interface.

direction | agent → plugin  
---|---  
response | no  
  
The request doesn't have specific parameters, it only contains common data parameters.

_Example:_
    
    
    {"id":3,"type":4}

Copy

✔ Copied

###### Terminate request

A request sent by the agent to shutdown a plugin.

direction | agent → plugin  
---|---  
response | no  
  
The request doesn't have specific parameters, it only contains common data parameters.

_Example:_
    
    
    {"id":3,"type":5}

Copy

✔ Copied

###### Export request

A request to execute the Export function of the Exporter interface.

direction | agent → plugin  
---|---  
response | no  
  
Parameters specific to export requests:

key | string | The plugin key.  
---|---|---  
parameters | array of strings (optional) | The parameters for Export function.  
  
_Example:_
    
    
    {"id":4,"type":6,"key":"test.key","parameters":["foo","bar"]}

Copy

✔ Copied

###### Export response

Response from the Export function of the Exporter interface.

direction | plugin → agent  
---|---  
response | n/a  
  
Parameters specific to export responses:

value | string (optional) | Response value from the Export function. Absent, if error is returned.  
---|---|---  
error | string (optional) | Error message if the Export function has not been executed successfully. Absent, if value is returned.  
  
_Examples:_
    
    
    {"id":5,"type":7,"value":"response"}

Copy

✔ Copied

or
    
    
    {"id":5,"type":7,"error":"error message"}

Copy

✔ Copied

###### Configure request

A request to execute the _Configure_ function of the _Configurator_ interface.

direction | agent → plugin  
---|---  
response | n/a  
  
Parameters specific to _Configure_ requests:

global_options | JSON object | JSON object containing global agent configuration options.  
---|---|---  
private_options | JSON object (optional) | JSON object containing private plugin configuration options, if provided.  
  
_Example:_
    
    
    {"id":6,"type":8,"global_options":{...},"private_options":{...}}

Copy

✔ Copied

###### Validate request

A request to execute _Validate_ function of the _Configurator_ interface.

direction | agent → plugin  
---|---  
response | yes  
  
Parameters specific to _Validate_ requests:

private_options | JSON object (optional) | JSON object containing private plugin configuration options, if provided.  
---|---|---  
  
_Example:_
    
    
    {"id":7,"type":9,"private_options":{...}}

Copy

✔ Copied

###### Validate response

Response from _Validate_ function of _Configurator_ interface.

direction | plugin → agent  
---|---  
response | n/a  
  
Parameters specific to _Validate_ responses:

error | string (optional) | An error message returned if the Validate function is not executed successfully. Absent if executed successfully.  
---|---|---  
  
_Example:_
    
    
    {"id":8,"type":10}

Copy

✔ Copied

or
    
    
    {"id":8,"type":10,"error":"error message"}

Copy

✔ Copied