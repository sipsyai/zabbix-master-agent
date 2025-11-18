---
title: Server-proxy data exchange protocol
source: https://www.zabbix.com/documentation/current/en/manual/appendix/protocols/server_proxy
downloaded: 2025-11-14 10:47:12
---

# 1 Server-proxy data exchange protocol

#### Overview

Server - proxy data exchange is based on JSON format.

Request and response messages must begin with [header and data length](/documentation/current/en/manual/appendix/protocols/header_datalen).

#### Passive proxy

##### Configuration request

The server will first send an empty `proxy config` request. This request is sent every `ProxyConfigFrequency` (server configuration parameter) seconds.

The proxy responds with the current proxy version, session token and configuration revision. The server responds with the configuration data that need to be updated.

server→proxy:  
---  
**request** | _string_ | 'proxy config'  
proxy→server:  
**version** | _string_ | Proxy version (<major>.<minor>.<build>).  
**session** | _string_ | Proxy configuration session token.  
**config_revision** | _number_ | Proxy configuration revision.  
server→proxy:  
**full_sync** | _number_ | 1 - if full configuration data is sent; absent - otherwise (optional).  
**data** | _array_ | Object of table data. Absent if configuration has not been changed (optional).  
| **< table>** | _object_ | One or more objects with <table> data (optional, depending on changes).  
| **fields** | _array_ | Array of field names.  
| - | _string_ | Field name.  
**data** | _array_ | Array of rows.  
| - | _array_ | Array of columns.  
| - | _string_ ,_number_ | Column value with type depending on column type in database schema.  
**macro.secrets** | _object_ | Secret macro information, absent if there are no changes in vault macros (optional).  
**config_revision** | _number_ | Configuration cache revision - sent with configuration data (optional).  
**del_hostids** | _array_ | Array of removed hostids (optional).  
| - | _number_ | Host identifier.  
**del_macro_hostids** | _array_ | Array of hostids with all macros removed (optional).  
| - | _number_ | Host identifier.  
proxy→server:  
**response** | _string_ | Request success information ('success' or 'failed').  
**version** | _string_ | Proxy version (<major>.<minor>.<build>).  
  
Example:

server→proxy:
    
    
    {
             "request":"proxy config"
           } 

Copy

✔ Copied

proxy→server:
    
    
    {
             "version": "7.4.0",
             "session": "0033124949800811e5686dbfd9bcea98",
             "config_revision": 0
           }

Copy

✔ Copied

server→proxy:
    
    
    {
               "full_sync": 1,
               "data": {
                   "hosts": {
                       "fields": ["hostid", "host", "status", "ipmi_authtype", "ipmi_privilege", "ipmi_username", "ipmi_password", "name", "tls_connect", "tls_accept", "tls_issuer", "tls_subject", "tls_psk_identity", "tls_psk"],
                       "data": [
                           [10084, "Zabbix server", 0, -1, 2, "", "", "Zabbix server", 1, 1, "", "", "", ""]
                       ]
                   },
                   "interface": {
                       "fields": ["interfaceid", "hostid", "main", "type", "useip", "ip", "dns", "port", "available"],
                       "data": [
                           [1, 10084, 1, 1, 1, "127.0.0.1", "", "10053", 1]
                       ]
                   },
                   "interface_snmp": {
                       "fields": ["interfaceid", "version", "bulk", "community", "securityname", "securitylevel", "authpassphrase", "privpassphrase", "authprotocol", "privprotocol", "contextname"],
                       "data": []
                   },
                   "host_inventory": {
                       "fields": ["hostid", "type", "type_full", "name", "alias", "os", "os_full", "os_short", "serialno_a", "serialno_b", "tag", "asset_tag", "macaddress_a", "macaddress_b", "hardware", "hardware_full", "software", "software_full", "software_app_a", "software_app_b", "software_app_c", "software_app_d", "software_app_e", "contact", "location", "location_lat", "location_lon", "notes", "chassis", "model", "hw_arch", "vendor", "contract_number", "installer_name", "deployment_status", "url_a", "url_b", "url_c", "host_networks", "host_netmask", "host_router", "oob_ip", "oob_netmask", "oob_router", "date_hw_purchase", "date_hw_install", "date_hw_expiry", "date_hw_decomm", "site_address_a", "site_address_b", "site_address_c", "site_city", "site_state", "site_country", "site_zip", "site_rack", "site_notes", "poc_1_name", "poc_1_email", "poc_1_phone_a", "poc_1_phone_b", "poc_1_cell", "poc_1_screen", "poc_1_notes", "poc_2_name", "poc_2_email", "poc_2_phone_a", "poc_2_phone_b", "poc_2_cell", "poc_2_screen", "poc_2_notes"],
                       "data": [
                           [10084, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "56.95387", "24.22067", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                       ]
                   },
                   "items": {
                       "fields": ["itemid", "type", "snmp_oid", "hostid", "key_", "delay", "history", "status", "value_type", "trapper_hosts", "logtimefmt", "params", "ipmi_sensor", "authtype", "username", "password", "publickey", "privatekey", "flags", "interfaceid", "inventory_link", "jmx_endpoint", "master_itemid", "timeout", "url", "query_fields", "posts", "status_codes", "follow_redirects", "post_type", "http_proxy", "headers", "retrieve_mode", "request_method", "output_format", "ssl_cert_file", "ssl_key_file", "ssl_key_password", "verify_peer", "verify_host", "allow_traps"],
                       "data": [
                           [44161, 7, "", 10084, "agent.hostmetadata", "10s", "90d", 0, 1, "", "", "", "", 0, "", "", "", "", 0, null, 0, "", null, "3s", "", "", "", "200", 1, 0, "", "", 0, 0, 0, "", "", "", 0, 0, 0],
                           [44162, 0, "", 10084, "agent.ping", "10s", "90d", 0, 3, "", "", "", "", 0, "", "", "", "", 0, 1, 0, "", null, "3s", "", "", "", "200", 1, 0, "", "", 0, 0, 0, "", "", "", 0, 0, 0]
                       ]
                   },
                   "item_rtdata": {
                       "fields": ["itemid", "lastlogsize", "mtime"],
                       "data": [
                           [44161, 0, 0],
                           [44162, 0, 0]
                       ]
                   },
                   "item_preproc": {
                       "fields": ["item_preprocid", "itemid", "step", "type", "params", "error_handler", "error_handler_params"],
                       "data": []
                   },
                   "item_parameter": {
                       "fields": ["item_parameterid", "itemid", "name", "value"],
                       "data": []
                   },
                   "globalmacro": {
                       "fields": ["globalmacroid", "macro", "value", "type"],
                       "data": [
                           [2, "{$SNMP_COMMUNITY}", "public", 0]
                       ]
                   },
                   "hosts_templates": {
                       "fields": ["hosttemplateid", "hostid", "templateid", "link_type"],
                       "data": []
                   },
                   "hostmacro": {
                       "fields": ["hostmacroid", "hostid", "macro", "value", "type", "automatic"],
                       "data": [
                           [5676, 10084, "{$M}", "AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix:Content", 2, 0]
                       ]
                   },
                   "drules": {
                       "fields": ["druleid", "name", "iprange", "delay"],
                       "data": [
                           [2, "Local network", "127.0.0.1", "10s"]
                       ]
                   },
                   "dchecks": {
                       "fields": ["dcheckid", "druleid", "type", "key_", "snmp_community", "ports", "snmpv3_securityname", "snmpv3_securitylevel", "snmpv3_authpassphrase", "snmpv3_privpassphrase", "uniq", "snmpv3_authprotocol", "snmpv3_privprotocol", "snmpv3_contextname", "host_source", "name_source"],
                       "data": [
                           [2, 2, 9, "system.uname", "", "10052", "", 0, "", "", 0, 0, 0, "", 1, 0]
                       ]
                   },
                   "regexps": {
                       "fields": ["regexpid", "name"],
                       "data": [
                           [1, "File systems for discovery"],
                           [2, "Network interfaces for discovery"],
                           [3, "Storage devices for SNMP discovery"],
                           [4, "Windows service names for discovery"],
                           [5, "Windows service startup states for discovery"]
                       ]
                   },
                   "expressions": {
                       "fields": ["expressionid", "regexpid", "expression", "expression_type", "exp_delimiter", "case_sensitive"],
                       "data": [
                           [1, 1, "^(btrfs|ext2|ext3|ext4|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|apfs|refs|ntfs|fat32|zfs)$", 3, ",", 0],
                           [3, 3, "^(Physical memory|Virtual memory|Memory buffers|Cached memory|Swap space)$", 4, ",", 1],
                           [5, 4, "^(MMCSS|gupdate|SysmonLog|clr_optimization_v2.0.50727_32|clr_optimization_v4.0.30319_32)$", 4, ",", 1],
                           [6, 5, "^(automatic|automatic delayed)$", 3, ",", 1],
                           [7, 2, "^Software Loopback Interface", 4, ",", 1],
                           [8, 2, "^(In)?[Ll]oop[Bb]ack[0-9._]*$", 4, ",", 1],
                           [9, 2, "^NULL[0-9.]*$", 4, ",", 1],
                           [10, 2, "^[Ll]o[0-9.]*$", 4, ",", 1],
                           [11, 2, "^[Ss]ystem$", 4, ",", 1],
                           [12, 2, "^Nu[0-9.]*$", 4, ",", 1]
                       ]
                   },
                   "settings": {
                       "fields": ["name", "type", "value_str", "value_int"],
                       "data": [
                           ["autoreg_tls_accept", 2, "", 1],
                           ["hk_history_global", 2, "", 0],
                           ["snmptrap_logging", 2, "", 1],
                           ["proxy_secrets_provider", 2, "", 0],
                           ["hk_history", 1, "31d", 0],
                           ["timeout_db_monitor", 1, "3s", 0],
                           ["timeout_external_check", 1, "3s", 0],
                           ["timeout_http_agent", 1, "3s", 0],
                           ["timeout_simple_check", 1, "3s", 0],
                           ["timeout_snmp_agent", 1, "3s", 0],
                           ["timeout_ssh_agent", 1, "3s", 0],
                           ["timeout_telnet_agent", 1, "3s", 0],
                           ["timeout_zabbix_agent", 1, "3s", 0],
                           ["timeout_browser", 1, "30s", 0]
                       ]
                   },
                   "httptest": {
                       "fields": ["httptestid", "name", "delay", "agent", "authentication", "http_user", "http_password", "hostid", "http_proxy", "retries", "ssl_cert_file", "ssl_key_file", "ssl_key_password", "verify_peer", "verify_host"],
                       "data": []
                   },
                   "httptestitem": {
                       "fields": ["httptestitemid", "httptestid", "itemid", "type"],
                       "data": []
                   },
                   "httptest_field": {
                       "fields": ["httptest_fieldid", "httptestid", "type", "name", "value"],
                       "data": []
                   },
                   "httpstep": {
                       "fields": ["httpstepid", "httptestid", "name", "no", "url", "timeout", "posts", "required", "status_codes", "follow_redirects", "retrieve_mode", "post_type"],
                       "data": []
                   },
                   "httpstepitem": {
                       "fields": ["httpstepitemid", "httpstepid", "itemid", "type"],
                       "data": []
                   },
                   "httpstep_field": {
                       "fields": ["httpstep_fieldid", "httpstepid", "type", "name", "value"],
                       "data": []
                   },
                   "config_autoreg_tls": {
                       "fields": ["autoreg_tlsid", "tls_psk_identity", "tls_psk"],
                       "data": [
                           [1, "", ""]
                       ]
                   }
               },
               "macro.secrets": {
                   "AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix": {
                       "Content": "738"
                   }
               },
               "config_revision": 2
           }

Copy

✔ Copied

proxy→server:
    
    
    {
             "response": "success",
             "version": "7.4.0"
           }

Copy

✔ Copied

##### Data request

The `proxy data` request is used to obtain host interface availability, historical, discovery and autoregistration data from proxy. This request is sent every `ProxyDataFrequency` (server configuration parameter) seconds.

server→proxy:  
---  
**request** | _string_ | 'proxy data'  
proxy→server:  
**session** | _string_ | Data session token.  
**interface availability** | _array_ | _(optional)_ Array of interface availability data objects.  
| **interfaceid** | _number_ | Interface identifier.  
**available** | _number_ | Interface availability:  
  
**0** , _INTERFACE_AVAILABLE_UNKNOWN_ \- unknown  
**1** , _INTERFACE_AVAILABLE_TRUE_ \- available  
**2** , _INTERFACE_AVAILABLE_FALSE_ \- unavailable  
**error** | _string_ | Interface error message or empty string.  
**history data** | _array_ | _(optional)_ Array of history data objects.  
| **itemid** | _number_ | Item identifier.  
**clock** | _number_ | Item value timestamp (seconds).  
**ns** | _number_ | Item value timestamp (nanoseconds).  
**value** | _string_ | _(optional)_ Item value.  
**id** | _number_ | Value identifier (ascending counter, unique within one data session).  
**timestamp** | _number_ | _(optional)_ Timestamp of log type items.  
**source** | _string_ | _(optional)_ Eventlog item source value.  
**severity** | _number_ | _(optional)_ Eventlog item severity value.  
**eventid** | _number_ | _(optional)_ Eventlog item eventid value.  
**state** | _string_ | _(optional)_ Item state:  
**0** , _ITEM_STATE_NORMAL_  
**1** , _ITEM_STATE_NOTSUPPORTED_  
**lastlogsize** | _number_ | _(optional)_ Last log size of log type items.  
**mtime** | _number_ | _(optional)_ Modification time of log type items.  
**discovery data** | _array_ | _(optional)_ Array of discovery data objects.  
| **clock** | _number_ | Discovery data timestamp.  
**druleid** | _number_ | Discovery rule identifier.  
**dcheckid** | _number_ | Discovery check identifier or null for discovery rule data.  
**type** | _number_ | Discovery check type:  
  
**-1** discovery rule data  
**0** , _SVC_SSH_ \- SSH service check  
**1** , _SVC_LDAP_ \- LDAP service check  
**2** , _SVC_SMTP_ \- SMTP service check  
**3** , _SVC_FTP_ \- FTP service check  
**4** , _SVC_HTTP_ \- HTTP service check  
**5** , _SVC_POP_ \- POP service check  
**6** , _SVC_NNTP_ \- NNTP service check  
**7** , _SVC_IMAP_ \- IMAP service check  
**8** , _SVC_TCP_ \- TCP port availability check  
**9** , _SVC_AGENT_ \- Zabbix agent  
**10** , _SVC_SNMPv1_ \- SNMPv1 agent  
**11** , _SVC_SNMPv2_ \- SNMPv2 agent  
**12** , _SVC_ICMPPING_ \- ICMP ping  
**13** , _SVC_SNMPv3_ \- SNMPv3 agent  
**14** , _SVC_HTTPS_ \- HTTPS service check  
**15** , _SVC_TELNET_ \- Telnet availability check  
**ip** | _string_ | Host IP address.  
**dns** | _string_ | Host DNS name.  
**port** | _number_ | _(optional)_ Service port number.  
**key_** | _string_ | _(optional)_ Item key for discovery check of type **9** _SVC_AGENT_  
**value** | _string_ | _(optional)_ Value received from the service, can be empty for most of services.  
**status** | _number_ | _(optional)_ Service status:  
  
**0** , _DOBJECT_STATUS_UP_ \- Service UP  
**1** , _DOBJECT_STATUS_DOWN_ \- Service DOWN  
**auto registration** | _array_ | _(optional)_ Array of autoregistration data objects.  
| **clock** | _number_ | Autoregistration data timestamp.  
**host** | _string_ | Host name.  
**ip** | _string_ | _(optional)_ Host IP address.  
**dns** | _string_ | _(optional)_ Resolved DNS name from IP address.  
**port** | _string_ | _(optional)_ Host port.  
**host_metadata** | _string_ | _(optional)_ Host metadata sent by agent (based on HostMetadata or HostMetadataItem agent configuration parameter).  
**tasks** | _array_ | _(optional)_ Array of tasks.  
| **type** | _number_ | Task type:  
  
**0** , _ZBX_TM_TASK_PROCESS_REMOTE_COMMAND_RESULT_ \- remote command result  
**status** | _number_ | Remote-command execution status:  
  
**0** , _ZBX_TM_REMOTE_COMMAND_COMPLETED_ \- remote command completed successfully  
**1** , _ZBX_TM_REMOTE_COMMAND_FAILED_ \- remote command failed  
**error** | _string_ | _(optional)_ Error message.  
**parent_taskid** | _number_ | Parent task ID.  
**more** | _number_ | _(optional)_ 1 - there are more history data to send.  
**clock** | _number_ | _(optional)_ Data transfer timestamp (seconds).  
**ns** | _number_ | _(optional)_ Data transfer timestamp (nanoseconds).  
**version** | _string_ | Proxy version (<major>.<minor>.<build>).  
server→proxy:  
**response** | _string_ | Request success information ('success' or 'failed').  
**tasks** | _array_ | _(optional)_ Array of tasks.  
| **type** | _number_ | Task type:  
  
**1** , _ZBX_TM_TASK_PROCESS_REMOTE_COMMAND_ \- remote command  
**clock** | _number_ | Task creation time.  
**ttl** | _number_ | Time in seconds after which the task expires.  
**commandtype** | _number_ | Remote-command type:  
  
**0** , _ZBX_SCRIPT_TYPE_CUSTOM_SCRIPT_ \- use custom script  
**1** , _ZBX_SCRIPT_TYPE_IPMI_ \- use IPMI  
**2** , _ZBX_SCRIPT_TYPE_SSH_ \- use SSH  
**3** , _ZBX_SCRIPT_TYPE_TELNET_ \- use Telnet  
**4** , _ZBX_SCRIPT_TYPE_GLOBAL_SCRIPT_ \- use global script (currently functionally equivalent to custom script)  
**command** | _string_ | Remote command to execute.  
**execute_on** | _number_ | Execution target for custom scripts:  
  
**0** , _ZBX_SCRIPT_EXECUTE_ON_AGENT_ \- execute script on agent  
**1** , _ZBX_SCRIPT_EXECUTE_ON_SERVER_ \- execute script on server  
**2** , _ZBX_SCRIPT_EXECUTE_ON_PROXY_ \- execute script on proxy  
**port** | _number_ | _(optional)_ Port for Telnet and SSH commands.  
**authtype** | _number_ | _(optional)_ Authentication type for SSH commands.  
**username** | _string_ | _(optional)_ User name for Telnet and SSH commands.  
**password** | _string_ | _(optional)_ Password for Telnet and SSH commands.  
**publickey** | _string_ | _(optional)_ Public key for SSH commands.  
**privatekey** | _string_ | _(optional)_ Private key for SSH commands.  
**parent_taskid** | _number_ | Parent task ID.  
**hostid** | _number_ | Target host ID.  
  
Example:

server→proxy:
    
    
    {
             "request": "proxy data"
           }

Copy

✔ Copied

proxy→server:
    
    
    {
               "session": "12345678901234567890123456789012"
               "interface availability": [
                   {
                       "interfaceid": 1,
                       "available": 1,
                       "error": ""
               },
                   {
                       "interfaceid": 2,
                       "available": 2,
                       "error": "Get value from agent failed: cannot connect to [[127.0.0.1]:10049]: [111] Connection refused"
               },
                   {
                       "interfaceid": 3,
                       "available": 1,
                       "error": ""
               },
                   {
                       "interfaceid": 4,
                       "available": 1,
                       "error": ""
               }
               ],
               "history data":[
                   {
                       "itemid":"12345",
                       "clock":1478609647,
                       "ns":332510044,
                       "value":"52956612",
                       "id": 1
                   },
                   {
                       "itemid":"12346",
                       "clock":1478609647,
                       "ns":330690279,
                       "state":1,
                       "value":"Cannot find information for this network interface in /proc/net/dev.",
                       "id": 2
                   }
               ],
               "discovery data":[
                   {
                       "clock":1478608764,
                       "drule":2,
                       "dcheck":3,
                       "type":12,
                       "ip":"10.3.0.10",
                       "dns":"vdebian",
                       "status":1
                   },
                   {
                       "clock":1478608764,
                       "drule":2,
                       "dcheck":null,
                       "type":-1,
                       "ip":"10.3.0.10",
                       "dns":"vdebian",
                       "status":1
                   }
               ],
               "auto registration":[
                   {
                       "clock":1478608371,
                       "host":"Logger1",
                       "ip":"10.3.0.1",
                       "dns":"localhost",
                       "port":"10050"
                   },
                   {
                       "clock":1478608381,
                       "host":"Logger2",
                       "ip":"10.3.0.2",
                       "dns":"localhost",
                       "port":"10050"
                   }
               ],
               "tasks":[
                   {
                       "type": 0,
                       "status": 0,
                       "parent_taskid": 10
                   },
                   {
                       "type": 0,
                       "status": 1,
                       "error": "No permissions to execute task.",
                       "parent_taskid": 20
                   }
               ],
               "version":"7.4.0"
           }

Copy

✔ Copied

server→proxy:
    
    
    {
             "response": "success",
             "tasks":[
                 {
                    "type": 1,
                    "clock": 1478608371,
                    "ttl": 600,
                    "commandtype": 2,
                    "command": "restart_service1.sh",
                    "execute_on": 2,
                    "port": 80,
                    "authtype": 0,
                    "username": "userA",
                    "password": "password1",
                    "publickey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe",
                    "privatekey": "lsuusFncCzWBQ7RKNUSesmQRMSGkVb1/3j+skZ6UtW+5u09lHNsj6tQ5QCqGKukO1De7zhd",
                    "parent_taskid": 10,
                    "hostid": 10070
                 },
                 {
                    "type": 1,
                    "clock": 1478608381,
                    "ttl": 600,
                    "commandtype": 1,
                    "command": "restart_service2.sh",
                    "execute_on": 0,
                    "authtype": 0,
                    "username": "",
                    "password": "",
                    "publickey": "",
                    "privatekey": "",
                    "parent_taskid": 20,
                    "hostid": 10084
                 }
             ]
           }

Copy

✔ Copied

#### Active proxy

##### Configuration request

The `proxy config` request is sent by active proxy to obtain proxy configuration data. This request is sent every `ProxyConfigFrequency` (proxy configuration parameter) seconds.

proxy→server:  
---  
**request** | _string_ | 'proxy config'  
**host** | _string  
_ | Proxy name.  
**version** | _string_ | Proxy version (<major>.<minor>.<build>).  
**session** | _string_ | Proxy configuration session token.  
**config_revision** | _number_ | Proxy configuration revision.  
server→proxy:  
**fullsync** | _number_ | 1 - if full configuration data is sent, absent otherwise (optional).  
**data** | _array_ | Object of table data. Absent if configuration has not been changed (optional).  
| **< table>** | _object_ | One or more objects with <table> data (optional, depending on changes).  
| **fields** | _array_ | Array of field names.  
| - | _string_ | Field name.  
**data** | _array_ | Array of rows.  
| - | _array_ | Array of columns.  
| - | _string_ ,_number_ | Column value with type depending on column type in database schema.  
**macro.secrets** | _object_ | Secret macro information, absent if there are no changes in vault macros (optional).  
**config_revision** | _number_ | Configuration cache revision - sent with configuration data (optional).  
**del_hostids** | _array_ | Array of removed hostids (optional).  
| - | _number_ | Host identifier.  
**del_macro_hostids** | _array_ | Array of hostids with all macros removed (optional).  
| - | _number_ | Host identifier.  
  
Example:

proxy→server:
    
    
    {
             "request": "proxy config",
             "host": "Zabbix proxy",
             "version":"7.4.0",
             "session": "fd59a09ff4e9d1fb447de1f04599bcf6",
             "config_revision": 0
           }

Copy

✔ Copied

server→proxy:
    
    
    {
               "full_sync": 1,
               "data": {
                   "hosts": {
                       "fields": ["hostid", "host", "status", "ipmi_authtype", "ipmi_privilege", "ipmi_username", "ipmi_password", "name", "tls_connect", "tls_accept", "tls_issuer", "tls_subject", "tls_psk_identity", "tls_psk"],
                       "data": [
                           [10084, "Zabbix server", 0, -1, 2, "", "", "Zabbix server", 1, 1, "", "", "", ""]
                       ]
                   },
                   "interface": {
                       "fields": ["interfaceid", "hostid", "main", "type", "useip", "ip", "dns", "port", "available"],
                       "data": [
                           [1, 10084, 1, 1, 1, "127.0.0.1", "", "10053", 1]
                       ]
                   },
                   "interface_snmp": {
                       "fields": ["interfaceid", "version", "bulk", "community", "securityname", "securitylevel", "authpassphrase", "privpassphrase", "authprotocol", "privprotocol", "contextname"],
                       "data": []
                   },
                   "host_inventory": {
                       "fields": ["hostid", "type", "type_full", "name", "alias", "os", "os_full", "os_short", "serialno_a", "serialno_b", "tag", "asset_tag", "macaddress_a", "macaddress_b", "hardware", "hardware_full", "software", "software_full", "software_app_a", "software_app_b", "software_app_c", "software_app_d", "software_app_e", "contact", "location", "location_lat", "location_lon", "notes", "chassis", "model", "hw_arch", "vendor", "contract_number", "installer_name", "deployment_status", "url_a", "url_b", "url_c", "host_networks", "host_netmask", "host_router", "oob_ip", "oob_netmask", "oob_router", "date_hw_purchase", "date_hw_install", "date_hw_expiry", "date_hw_decomm", "site_address_a", "site_address_b", "site_address_c", "site_city", "site_state", "site_country", "site_zip", "site_rack", "site_notes", "poc_1_name", "poc_1_email", "poc_1_phone_a", "poc_1_phone_b", "poc_1_cell", "poc_1_screen", "poc_1_notes", "poc_2_name", "poc_2_email", "poc_2_phone_a", "poc_2_phone_b", "poc_2_cell", "poc_2_screen", "poc_2_notes"],
                       "data": [
                           [10084, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "56.95387", "24.22067", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
                       ]
                   },
                   "items": {
                       "fields": ["itemid", "type", "snmp_oid", "hostid", "key_", "delay", "history", "status", "value_type", "trapper_hosts", "logtimefmt", "params", "ipmi_sensor", "authtype", "username", "password", "publickey", "privatekey", "flags", "interfaceid", "inventory_link", "jmx_endpoint", "master_itemid", "timeout", "url", "query_fields", "posts", "status_codes", "follow_redirects", "post_type", "http_proxy", "headers", "retrieve_mode", "request_method", "output_format", "ssl_cert_file", "ssl_key_file", "ssl_key_password", "verify_peer", "verify_host", "allow_traps"],
                       "data": [
                           [44161, 7, "", 10084, "agent.hostmetadata", "10s", "90d", 0, 1, "", "", "", "", 0, "", "", "", "", 0, null, 0, "", null, "3s", "", "", "", "200", 1, 0, "", "", 0, 0, 0, "", "", "", 0, 0, 0],
                           [44162, 0, "", 10084, "agent.ping", "10s", "90d", 0, 3, "", "", "", "", 0, "", "", "", "", 0, 1, 0, "", null, "3s", "", "", "", "200", 1, 0, "", "", 0, 0, 0, "", "", "", 0, 0, 0]
                       ]
                   },
                   "item_rtdata": {
                       "fields": ["itemid", "lastlogsize", "mtime"],
                       "data": [
                           [44161, 0, 0],
                           [44162, 0, 0]
                       ]
                   },
                   "item_preproc": {
                       "fields": ["item_preprocid", "itemid", "step", "type", "params", "error_handler", "error_handler_params"],
                       "data": []
                   },
                   "item_parameter": {
                       "fields": ["item_parameterid", "itemid", "name", "value"],
                       "data": []
                   },
                   "globalmacro": {
                       "fields": ["globalmacroid", "macro", "value", "type"],
                       "data": [
                           [2, "{$SNMP_COMMUNITY}", "public", 0]
                       ]
                   },
                   "hosts_templates": {
                       "fields": ["hosttemplateid", "hostid", "templateid", "link_type"],
                       "data": []
                   },
                   "hostmacro": {
                       "fields": ["hostmacroid", "hostid", "macro", "value", "type", "automatic"],
                       "data": [
                           [5676, 10084, "{$M}", "AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix:Content", 2, 0]
                       ]
                   },
                   "drules": {
                       "fields": ["druleid", "name", "iprange", "delay"],
                       "data": [
                           [2, "Local network", "127.0.0.1", "10s"]
                       ]
                   },
                   "dchecks": {
                       "fields": ["dcheckid", "druleid", "type", "key_", "snmp_community", "ports", "snmpv3_securityname", "snmpv3_securitylevel", "snmpv3_authpassphrase", "snmpv3_privpassphrase", "uniq", "snmpv3_authprotocol", "snmpv3_privprotocol", "snmpv3_contextname", "host_source", "name_source"],
                       "data": [
                           [2, 2, 9, "system.uname", "", "10052", "", 0, "", "", 0, 0, 0, "", 1, 0]
                       ]
                   },
                   "regexps": {
                       "fields": ["regexpid", "name"],
                       "data": [
                           [1, "File systems for discovery"],
                           [2, "Network interfaces for discovery"],
                           [3, "Storage devices for SNMP discovery"],
                           [4, "Windows service names for discovery"],
                           [5, "Windows service startup states for discovery"]
                       ]
                   },
                   "expressions": {
                       "fields": ["expressionid", "regexpid", "expression", "expression_type", "exp_delimiter", "case_sensitive"],
                       "data": [
                           [1, 1, "^(btrfs|ext2|ext3|ext4|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|apfs|refs|ntfs|fat32|zfs)$", 3, ",", 0],
                           [3, 3, "^(Physical memory|Virtual memory|Memory buffers|Cached memory|Swap space)$", 4, ",", 1],
                           [5, 4, "^(MMCSS|gupdate|SysmonLog|clr_optimization_v2.0.50727_32|clr_optimization_v4.0.30319_32)$", 4, ",", 1],
                           [6, 5, "^(automatic|automatic delayed)$", 3, ",", 1],
                           [7, 2, "^Software Loopback Interface", 4, ",", 1],
                           [8, 2, "^(In)?[Ll]oop[Bb]ack[0-9._]*$", 4, ",", 1],
                           [9, 2, "^NULL[0-9.]*$", 4, ",", 1],
                           [10, 2, "^[Ll]o[0-9.]*$", 4, ",", 1],
                           [11, 2, "^[Ss]ystem$", 4, ",", 1],
                           [12, 2, "^Nu[0-9.]*$", 4, ",", 1]
                       ]
                   },
                   "settings": {
                       "fields": ["name", "type", "value_str", "value_int"],
                       "data": [
                           ["autoreg_tls_accept", 2, "", 1],
                           ["hk_history_global", 2, "", 0],
                           ["snmptrap_logging", 2, "", 1],
                           ["proxy_secrets_provider", 2, "", 0],
                           ["hk_history", 1, "31d", 0],
                           ["timeout_db_monitor", 1, "3s", 0],
                           ["timeout_external_check", 1, "3s", 0],
                           ["timeout_http_agent", 1, "3s", 0],
                           ["timeout_simple_check", 1, "3s", 0],
                           ["timeout_snmp_agent", 1, "3s", 0],
                           ["timeout_ssh_agent", 1, "3s", 0],
                           ["timeout_telnet_agent", 1, "3s", 0],
                           ["timeout_zabbix_agent", 1, "3s", 0],
                           ["timeout_browser", 1, "30s", 0]
                       ]
                   },
                   "httptest": {
                       "fields": ["httptestid", "name", "delay", "agent", "authentication", "http_user", "http_password", "hostid", "http_proxy", "retries", "ssl_cert_file", "ssl_key_file", "ssl_key_password", "verify_peer", "verify_host"],
                       "data": []
                   },
                   "httptestitem": {
                       "fields": ["httptestitemid", "httptestid", "itemid", "type"],
                       "data": []
                   },
                   "httptest_field": {
                       "fields": ["httptest_fieldid", "httptestid", "type", "name", "value"],
                       "data": []
                   },
                   "httpstep": {
                       "fields": ["httpstepid", "httptestid", "name", "no", "url", "timeout", "posts", "required", "status_codes", "follow_redirects", "retrieve_mode", "post_type"],
                       "data": []
                   },
                   "httpstepitem": {
                       "fields": ["httpstepitemid", "httpstepid", "itemid", "type"],
                       "data": []
                   },
                   "httpstep_field": {
                       "fields": ["httpstep_fieldid", "httpstepid", "type", "name", "value"],
                       "data": []
                   },
                   "config_autoreg_tls": {
                       "fields": ["autoreg_tlsid", "tls_psk_identity", "tls_psk"],
                       "data": [
                           [1, "", ""]
                       ]
                   }
               },
               "macro.secrets": {
                   "AppID=zabbix_server&Query=Safe=passwordSafe;Object=zabbix": {
                       "Content": "738"
                   }
               },
               "config_revision": 2
           }

Copy

✔ Copied

##### Data request

The `proxy data` request is sent by proxy to provide host interface availability, history, discovery and autoregistration data. This request is sent every `DataSenderFrequency` (proxy configuration parameter) seconds. Note that active proxy will still poll Zabbix server every second for remote command tasks (with an empty `proxy data` request).

proxy→server:  
---  
**request** | _string_ | 'proxy data'  
**host** | _string_ | Proxy name.  
**session** | _string_ | Data session token.  
**interface availability** | _array_ | _(optional)_ Array of interface availability data objects.  
| **interfaceid** | _number_ | Interface identifier.  
**available** | _number_ | Interface availability:  
  
**0** , _INTERFACE_AVAILABLE_UNKNOWN_ \- unknown  
**1** , _INTERFACE_AVAILABLE_TRUE_ \- available  
**2** , _INTERFACE_AVAILABLE_FALSE_ \- unavailable  
**error** | _string_ | Interface error message or empty string.  
**history data** | _array_ | _(optional)_ Array of history data objects.  
| **itemid** | _number_ | Item identifier.  
**clock** | _number_ | Item value timestamp (seconds).  
**ns** | _number_ | Item value timestamp (nanoseconds).  
**value** | _string_ | _(optional)_ Item value.  
**id** | _number_ | Value identifier (ascending counter, unique within one data session).  
**timestamp** | _number_ | _(optional)_ Timestamp of log type items.  
**source** | _string_ | _(optional)_ Eventlog item source value.  
**severity** | _number_ | _(optional)_ Eventlog item severity value.  
**eventid** | _number_ | _(optional)_ Eventlog item eventid value.  
**state** | _string_ | _(optional)_ Item state:  
**0** , _ITEM_STATE_NORMAL_  
**1** , _ITEM_STATE_NOTSUPPORTED_  
**lastlogsize** | _number_ | _(optional)_ Last log size of log type items.  
**mtime** | _number_ | _(optional)_ Modification time of log type items.  
**discovery data** | _array_ | _(optional)_ Array of discovery data objects.  
| **clock** | _number_ | Discovery data timestamp.  
**druleid** | _number_ | Discovery rule identifier.  
**dcheckid** | _number_ | Discovery check identifier or null for discovery rule data.  
**type** | _number_ | Discovery check type:  
  
**-1** discovery rule data  
**0** , _SVC_SSH_ \- SSH service check  
**1** , _SVC_LDAP_ \- LDAP service check  
**2** , _SVC_SMTP_ \- SMTP service check  
**3** , _SVC_FTP_ \- FTP service check  
**4** , _SVC_HTTP_ \- HTTP service check  
**5** , _SVC_POP_ \- POP service check  
**6** , _SVC_NNTP_ \- NNTP service check  
**7** , _SVC_IMAP_ \- IMAP service check  
**8** , _SVC_TCP_ \- TCP port availability check  
**9** , _SVC_AGENT_ \- Zabbix agent  
**10** , _SVC_SNMPv1_ \- SNMPv1 agent  
**11** , _SVC_SNMPv2_ \- SNMPv2 agent  
**12** , _SVC_ICMPPING_ \- ICMP ping  
**13** , _SVC_SNMPv3_ \- SNMPv3 agent  
**14** , _SVC_HTTPS_ \- HTTPS service check  
**15** , _SVC_TELNET_ \- Telnet availability check  
**ip** | _string_ | Host IP address.  
**dns** | _string_ | Host DNS name.  
**port** | _number_ | _(optional)_ Service port number.  
**key_** | _string_ | _(optional)_ Item key for discovery check of type **9** _SVC_AGENT_  
**value** | _string_ | _(optional)_ Value received from the service, can be empty for most services.  
**status** | _number_ | _(optional)_ Service status:  
  
**0** , _DOBJECT_STATUS_UP_ \- Service UP  
**1** , _DOBJECT_STATUS_DOWN_ \- Service DOWN  
**autoregistration** | _array_ | _(optional)_ Array of autoregistration data objects.  
| **clock** | _number_ | Autoregistration data timestamp.  
**host** | _string_ | Host name.  
**ip** | _string_ | _(optional)_ Host IP address.  
**dns** | _string_ | _(optional)_ Resolved DNS name from IP address.  
**port** | _string_ | _(optional)_ Host port.  
**host_metadata** | _string_ | _(optional)_ Host metadata sent by agent (based on HostMetadata or HostMetadataItem agent configuration parameter).  
**tasks** | _array_ | _(optional)_ Array of tasks.  
| **type** | _number_ | Task type:  
  
**0** , _ZBX_TM_TASK_PROCESS_REMOTE_COMMAND_RESULT_ \- remote command result  
**status** | _number_ | Remote-command execution status:  
  
**0** , _ZBX_TM_REMOTE_COMMAND_COMPLETED_ \- remote command completed successfully  
**1** , _ZBX_TM_REMOTE_COMMAND_FAILED_ \- remote command failed  
**error** | _string_ | _(optional)_ Error message.  
**parent_taskid** | _number_ | Parent task ID.  
**more** | _number_ | _(optional)_ 1 - there are more history data to send  
**clock** | _number_ | _(optional)_ Data transfer timestamp (seconds).  
**ns** | _number_ | _(optional)_ Data transfer timestamp (nanoseconds).  
**version** | _string_ | Proxy version (<major>.<minor>.<build>).  
server→proxy:  
**response** | _string_ | Request success information ('success' or 'failed').  
**upload** | _string_ | Upload control for historical data (history, autoregistration, host availability, network discovery).  
  
Possible values:  
**enabled** \- normal operation  
**disabled** \- server is not accepting data (possibly due to internal cache over limit)  
**tasks** | _array_ | _(optional)_ Array of tasks.  
| **type** | _number_ | Task type:  
  
**1** , _ZBX_TM_TASK_PROCESS_REMOTE_COMMAND_ \- remote command  
**clock** | _number_ | Task creation time.  
**ttl** | _number_ | Time in seconds after which the task expires.  
**commandtype** | _number_ | Remote-command type:  
  
**0** , _ZBX_SCRIPT_TYPE_CUSTOM_SCRIPT_ \- use custom script  
**1** , _ZBX_SCRIPT_TYPE_IPMI_ \- use IPMI  
**2** , _ZBX_SCRIPT_TYPE_SSH_ \- use SSH  
**3** , _ZBX_SCRIPT_TYPE_TELNET_ \- use Telnet  
**4** , _ZBX_SCRIPT_TYPE_GLOBAL_SCRIPT_ \- use global script (currently functionally equivalent to custom script)  
**command** | _string_ | Remote command to execute.  
**execute_on** | _number_ | Execution target for custom scripts:  
  
**0** , _ZBX_SCRIPT_EXECUTE_ON_AGENT_ \- execute script on agent  
**1** , _ZBX_SCRIPT_EXECUTE_ON_SERVER_ \- execute script on server  
**2** , _ZBX_SCRIPT_EXECUTE_ON_PROXY_ \- execute script on proxy  
**port** | _number_ | _(optional)_ Port for Telnet and SSH commands.  
**authtype** | _number_ | _(optional)_ Authentication type for SSH commands.  
**username** | _string_ | _(optional)_ User name for Telnet and SSH commands.  
**password** | _string_ | _(optional)_ Password for Telnet and SSH commands.  
**publickey** | _string_ | _(optional)_ Public key for SSH commands.  
**privatekey** | _string_ | _(optional)_ Private key for SSH commands.  
**parent_taskid** | _number_ | Parent task ID.  
**hostid** | _number_ | Target host ID.  
  
Example:

proxy→server:
    
    
    {
               "request": "proxy data",
               "host": "Zabbix proxy",
               "session": "818cdd1b537bdc5e50c09ed4969235b6",
               "interface availability": [{
                   "interfaceid": 1,
                   "available": 1,
                   "error": ""
               }],
               "history data": [{
                   "id": 1114,
                   "itemid": 44162,
                   "clock": 1665730632,
                   "ns": 798953105,
                   "value": "1"
               }, {
                   "id": 1115,
                   "itemid": 44161,
                   "clock": 1665730633,
                   "ns": 811684663,
                   "value": "58"
               }],
               "auto registration": [{
                   "clock": 1665730633,
                   "host": "Zabbix server",
                   "ip": "127.0.0.1",
                   "dns": "localhost",
                   "port": "10053",
                   "host_metadata": "58",
                   "tls_accepted": 1
               }],
               "discovery data": [{
                   "clock": 1665732232,
                   "drule": 2,
                   "dcheck": 2,
                   "ip": "127.0.0.1",
                   "dns": "localhost",
                   "port": 10052,
                   "status": 1
               }, {
                   "clock": 1665732232,
                   "drule": 2,
                   "dcheck": null,
                   "ip": "127.0.0.1",
                   "dns": "localhost",
                   "status": 1
               }],
               "host data": [{
                   "hostid": 10084,
                   "active_status": 1
               }],
               "tasks": [{
                   "type": 3,
                   "clock": 1665730985,
                   "ttl": 0,
                   "status": -1,
                   "info": "Remote commands are not enabled",
                   "parent_taskid": 3
               }],
               "version": "7.4.0",
               "clock": 1665730643,
               "ns": 65389964
           }

Copy

✔ Copied

server→proxy:
    
    
    {
               "upload": "enabled",
               "response": "success",
               "tasks": [{
                   "type": 2,
                   "clock": 1665730986,
                   "ttl": 600,
                   "commandtype": 0,
                   "command": "ping -c 3 127.0.0.1; case $? in [01]) true;; *) false;; esac",
                   "execute_on": 2,
                   "port": 0,
                   "authtype": 0,
                   "username": "",
                   "password": "",
                   "publickey": "",
                   "privatekey": "",
                   "alertid": 0,
                   "parent_taskid": 4,
                   "hostid": 10084
               }]
           }

Copy

✔ Copied