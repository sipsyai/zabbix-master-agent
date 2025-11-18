---
title: Connector object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/connector/object
downloaded: 2025-11-14 10:40:22
---

# Connector object

The following objects are directly related to the `connector` API.

### Connector

The connector object has the following properties.

connectorid | ID | ID of the connector.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the connector.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
url | string | Endpoint URL, that is, URL of the receiver.  
User macros are supported.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
protocol | integer | Communication protocol.  
  
Possible values:  
0 - _(default)_ Zabbix Streaming Protocol v1.0.  
data_type | integer | Data type.  
  
Possible values:  
0 - _(default)_ Item values;  
1 - Events.  
item_value_type | integer | A sum of item value types to be sent.  
  
Possible values:  
1 - Numeric (float);  
2 - Character;  
4 - Log;  
8 - Numeric (unsigned);  
10 - Text;  
20 - Binary.  
  
Default: 31 - All item types (except binary).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `data_type` is set to "Item values".  
max_records | integer | Maximum number of events or items that can be sent within one message.  
  
Possible values: 0-2147483647 (max value of 32-bit signed integer).  
  
Default: 0 - Unlimited.  
max_senders | integer | Number of sender processes to run for this connector.  
  
Possible values: 1-100.  
  
Default: 1.  
max_attempts | integer | Number of attempts.  
  
Possible values: 1-5.  
  
Default: 1.  
attempt_interval | string | The interval between retry attempts.  
Accepts seconds.  
  
Possible values: 0s-10s.  
  
Default: 5s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `max_attempts` is greater than 1.  
timeout | string | Timeout.  
Time suffixes are supported (e.g., 30s, 1m).  
User macros are supported.  
  
Possible values: 1s-60s.  
  
Default: 5s.  
http_proxy | string | HTTP(S) proxy connection string given as   
_[protocol]://[username[:password]@]proxy.example.com[:port]_.  
  
User macros are supported.  
authtype | integer | HTTP authentication method.  
  
Possible values:  
0 - _(default)_ None;  
1 - Basic;  
2 - NTLM;  
3 - Kerberos;  
4 - Digest;  
5 - Bearer.  
username | string | User name.  
User macros are supported.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `authtype` is set to "Basic", "NTLM", "Kerberos", or "Digest"  
password | string | Password.  
User macros are supported.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `authtype` is set to "Basic", "NTLM", "Kerberos", or "Digest"  
token | string | Bearer token.  
User macros are supported.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `authtype` is set to "Bearer"  
verify_peer | integer | Whether to validate that the host's certificate is authentic.  
  
Possible values:  
0 - Do not validate;  
1 - _(default)_ Validate.  
verify_host | integer | Whether to validate that the host name for the connection matches the one in the host's certificate.  
  
Possible values:  
0 - Do not validate;  
1 - _(default)_ Validate.  
ssl_cert_file | string | Public SSL Key file path.  
User macros are supported.  
ssl_key_file | string | Private SSL Key file path.  
User macros are supported.  
ssl_key_password | string | Password for SSL Key file.  
User macros are supported.  
description | text | Description of the connector.  
status | integer | Whether the connector is enabled.  
  
Possible values:  
0 - Disabled;  
1 - _(default)_ Enabled.  
tags_evaltype | integer | Tag [evaluation method](/documentation/current/en/manual/config/export/streaming#configuration).  
  
Possible values:  
0 - _(default)_ And/Or;  
2 - Or.  
  
### Tag filter

Tag filter allows to export only matching item values or events. If not set then everything will be exported. The tag filter object has the following properties.

tag | string | Tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
operator | integer | Condition [operator](/documentation/current/en/manual/config/export/streaming#configuration).  
  
Possible values:  
0 - _(default)_ Equals;  
1 - Does not equal;  
2 - Contains;  
3 - Does not contain;  
12 - Exists;  
13 - Does not exist.  
value | string | Tag value.