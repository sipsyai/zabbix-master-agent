---
title: Streaming to external systems
source: https://www.zabbix.com/documentation/current/en/manual/config/export/streaming
downloaded: 2025-11-14 10:36:45
---

# 2 Streaming to external systems

#### Overview

It is possible to stream item values and events from Zabbix to external systems over HTTP (see protocol details).

The tag filter can be used to stream subsets of item values or events.

Two Zabbix server processes are responsible for data streaming: `connector manager` and `connector worker`. A Zabbix internal item `zabbix[connector_queue]` allows to monitor the count of values enqueued in the connector queue.

#### Configuration

The following steps are required to configure data streaming to an external system:

1\. Have a remote system set up for receiving data from Zabbix. For this purpose, the following tools are available:

  * An example of a simple [receiver](https://git.zabbix.com/projects/ZT/repos/receiver/browse) that logs the received information in `events.ndjson` and `history.ndjson` files.
  * [Kafka connector for Zabbix server](https://git.zabbix.com/projects/ZT/repos/kafka-connector/browse) \- a lightweight server written in Go, designed to forward item values and events from a Zabbix server to a Kafka broker.

2\. Set the required number of connector workers in Zabbix by adjusting the [`StartConnectors`](/documentation/current/en/manual/appendix/config/zabbix_server#startconnectors) parameter in `zabbix_server.conf`. The number of connector workers should match (or exceed if concurrent sessions are more than 1) the configured connector count in Zabbix frontend. Then, restart Zabbix server.

3\. Configure a new connector in Zabbix frontend (_Administration_ → _General_ → _Connectors_) and reload the server cache with the `zabbix_server -R config_cache_reload` command.

![](/documentation/current/assets/en/manual/config/connector.png)

Mandatory fields are marked by an asterisk.

_Name_ | Enter the connector name.  
---|---  
_Data type_ | Select the data type to stream:  
**Item values** \- stream item values from Zabbix to external systems;  
**Events** \- stream events from Zabbix to external systems.  
_URL_ | Enter the receiver URL. User macros are supported.  
_Tag filter_ | Export only item values or events matching the tag filter. If not set, then export everything.  
It is possible to include as well as exclude specific tags and tag values. Several conditions can be set. Tag name matching is always case-sensitive.  
  
There are several operators available for each condition:  
**Exists** \- include the specified tag names;  
**Equals** \- include the specified tag names and values (case-sensitive);  
**Contains** \- include the specified tag names where the tag values contain the entered string (substring match, case-insensitive);  
**Does not exist** \- exclude the specified tag names;  
**Does not equal** \- exclude the specified tag names and values (case-sensitive);  
**Does not contain** \- exclude the specified tag names where the tag values contain the entered string (substring match, case-insensitive).  
  
There are two calculation types for conditions:  
**And/Or** \- all conditions must be met, conditions having the same tag name will be grouped by the Or condition;  
**Or** \- enough if one condition is met.  
_Type of information_ | Select the type of information (numeric (unsigned), numeric (float), character, etc.), by which to filter the item values that the connector should stream.  
This field is available if _Data type_ is set to "Item values".  
_HTTP authentication_ | Select the authentication option:  
**None** \- no authentication used;  
**Basic** \- basic authentication is used;  
**NTLM** \- NTLM ([Windows NT LAN Manager](http://en.wikipedia.org/wiki/NTLM)) authentication is used;  
**Kerberos** \- Kerberos authentication is used (see also: [Configuring Kerberos with Zabbix](/documentation/current/en/manual/appendix/items/kerberos));  
**Digest** \- Digest authentication is used;  
**Bearer** \- Bearer authentication is used.  
_Username_ | Enter the user name (up to 255 characters). User macros are supported.  
This field is available if _HTTP authentication_ is set to "Basic", "NTLM", "Kerberos", or "Digest".  
_Password_ | Enter the user password (up to 255 characters). User macros are supported.  
This field is available if _HTTP authentication_ is set to "Basic", "NTLM", "Kerberos", or "Digest".  
_Bearer token_ | Enter the Bearer token. User macros are supported.  
This field is available and required if _HTTP authentication_ is set to "Bearer".  
_Advanced configuration_ | Click the _Advanced configuration_ label to display advanced configuration options (see below).  
_Max records per message_ | Specify the maximum number of values or events that can be streamed within one message.  
_Concurrent sessions_ | Select the number of sender processes to run for this connector. Up to 100 sessions can be specified; the default value is "1".  
_Attempts_ | Number of attempts for streaming data. Up to 5 attempts can be specified; the default value is "1".  
_Attempt interval_ | Specify how long the connector should wait after an unsuccessful attempt to stream data. Up to 10s can be specified; the default value is "5s".  
This field is available if _Attempts_ is set to "2" or more.  
Unsuccessful attempts are those where establishing a connection has failed, or where the HTTP response code is not 200, 201, 202, 203, 204. Retries are **triggered** in case of communication errors or when the HTTP response code is not 200, 201, 202, 203, 204, 400, 401, 403, 404, 405, 415, 422. Redirects are followed, so 302 -> 200 is a positive response; whereas 302 -> 503 will trigger a retry.  
_Timeout_ | Specify the message timeout (1-60 seconds, default - 5 seconds).  
Time suffixes are supported, e.g., 30s, 1m. User macros are supported.  
_HTTP proxy_ | You can specify an HTTP proxy to use in the following format:  
`[protocol://][username[:password]@]proxy.example.com[:port]`  
User macros are supported.  
  
The optional `protocol://` prefix may be used to specify alternative proxy protocols (the protocol prefix support was added in cURL 7.21.7). With no protocol specified, the proxy will be treated as an HTTP proxy. By default, 1080 port will be used.  
  
If _HTTP proxy_ is specified, the proxy will overwrite proxy related environment variables like `http_proxy`, `HTTPS_PROXY`. If not specified, the proxy will not overwrite proxy-related environment variables. The entered value is passed on as is, no sanity checking takes place.  
You may also enter a SOCKS proxy address. If you specify the wrong protocol, the connection will fail and the item will become unsupported.  
  
Note that only simple authentication is supported with HTTP proxy.  
_SSL verify peer_ | Mark the checkbox to verify the SSL certificate of the web server.  
The server certificate will be automatically taken from system-wide certificate authority (CA) location. You can override the location of CA files using Zabbix server or proxy configuration parameter [`SSLCALocation`](/documentation/current/en/manual/appendix/config/zabbix_server#sslcalocation).  
_SSL verify host_ | Mark the checkbox to verify that the _Common Name_ field or the _Subject Alternate Name_ field of the web server certificate matches.  
This sets the [`CURLOPT_SSL_VERIFYHOST`](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYHOST.html) cURL option.  
_SSL certificate file_ | Name of the SSL certificate file used for client authentication. The certificate file must be in PEM1 format. User macros are supported.  
If the certificate file also contains the private key, leave the _SSL key file_ field empty. If the key is encrypted, specify the password in the _SSL key password_ field. The directory containing this file is specified by Zabbix server or proxy configuration parameter [`SSLCertLocation`](/documentation/current/en/manual/appendix/config/zabbix_server#sslcertlocation).  
_SSL key file_ | Name of the SSL private key file used for client authentication. The private key file must be in PEM1 format. User macros are supported.  
The directory containing this file is specified by Zabbix server or proxy configuration parameter [`SSLKeyLocation`](/documentation/current/en/manual/appendix/config/zabbix_server#sslkeylocation).  
_SSL key password_ | SSL private key file password. User macros are supported.  
_Description_ | Enter the connector description.  
_Enabled_ | Mark the checkbox to enable the connector.  
  
#### Protocol

Communication between the server and the receiver is done over HTTP using REST API, NDJSON, "Content-Type: application/x-ndjson".

For more details, see [Newline-delimited JSON export protocol](/documentation/current/en/manual/appendix/protocols/real_time_export).

##### Server request

Example of streaming item values:
    
    
    POST /v1/history HTTP/1.1
           Host: localhost:8080
           Accept: */*
           Accept-Encoding: deflate, gzip, br, zstd
           Content-Length: 628
           Content-Type: application/x-ndjson
            
           {"host":{"host":"Zabbix server","name":"Zabbix server"},"groups":["Zabbix servers"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":44457,"name":"foo","clock":1673454303,"ns":800155804,"value":0,"type":3}
           {"host":{"host":"Zabbix server","name":"Zabbix server"},"groups":["Zabbix servers"],"item_tags":[{"tag":"foo","value":"test"}],"itemid":44457,"name":"foo","clock":1673454303,"ns":832290669,"value":1,"type":3}
           {"host":{"host":"Zabbix server","name":"Zabbix server"},"groups":["Zabbix servers"],"item_tags":[{"tag":"bar","value":"test"}],"itemid":44458,"name":"bar","clock":1673454303,"ns":867770366,"value":123,"type":3}

Copy

✔ Copied

Example of streaming events:
    
    
    POST /v1/events HTTP/1.1
           Host: localhost:8080
           Accept: */*
           Accept-Encoding: deflate, gzip, br, zstd
           Content-Length: 333
           Content-Type: application/x-ndjson
            
           {"clock":1673454303,"ns":800155804,"value":1,"eventid":5,"name":"trigger for foo being 0","severity":0,"hosts":[{"host":"Zabbix server","name":"Zabbix server"}],"groups":["Zabbix servers"],"tags":[{"tag":"foo_trig","value":"test"},{"tag":"foo","value":"test"}]}
           {"clock":1673454303,"ns":832290669,"value":0,"eventid":6,"p_eventid":5}

Copy

✔ Copied

##### Receiver response

The response consists of the HTTP response status code and the JSON payload. The HTTP response status code must be "200", "201", "202", "203", or "204" for requests that were handled successfully, other for failed requests.

Example of success:
    
    
    localhost:8080/v1/history": HTTP/1.1 200 OK
           Date: Wed, 11 Jan 2023 16:40:30 GMT
           Content-Length: 0

Copy

✔ Copied

Example with errors:
    
    
    localhost:8080/v1/history": HTTP/1.1 422 Unprocessable Entity
           Content-Type: application/json
           Date: Wed, 11 Jan 2023 17:07:36 GMT
           Content-Length: 55
            
           {"error":"invalid character '{' after top-level value"}

Copy

✔ Copied