---
title: Web scenario object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/httptest/object
downloaded: 2025-11-14 10:46:09
---

# Web scenario object

The following objects are directly related to the `webcheck` API.

### Web scenario

The web scenario object has the following properties.

httptestid | ID | ID of the web scenario.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
hostid | ID | ID of the host that the web scenario belongs to.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
\- _required_ for create operations  
name | string | Name of the web scenario.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
agent | string | User agent string that will be used by the web scenario.  
  
Default: Zabbix  
authentication | integer | Authentication method that will be used by the web scenario.  
  
Possible values:  
0 - _(default)_ none;  
1 - basic HTTP authentication;  
2 - NTLM authentication.  
delay | string | Execution interval of the web scenario.  
  
Accepts seconds or time unit with suffix (e.g., 30s, 1m, 2h, 1d), or a user macro.  
  
Default: 1m.  
headers | array | [HTTP headers](/documentation/current/en/manual/api/reference/httptest/object#http-field) that will be sent when performing a request.  
http_password | string | Password used for basic HTTP or NTLM authentication.  
http_proxy | string | Proxy that will be used by the web scenario given as _http://[username[:password]@]proxy.example.com[:port]_.  
http_user | string | User name used for basic HTTP or NTLM authentication.  
retries | integer | Number of times a web scenario will try to execute each step before failing.  
  
Default: 1.  
ssl_cert_file | string | Name of the SSL certificate file used for client authentication (must be in PEM format).  
ssl_key_file | string | Name of the SSL private key file used for client authentication (must be in PEM format).  
ssl_key_password | string | SSL private key password.  
status | integer | Whether the web scenario is enabled.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
templateid | ID | ID of the parent template web scenario.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
variables | array | Web scenario [variables](/documentation/current/en/manual/api/reference/httptest/object#http-field).  
verify_host | integer | Whether to validate that the host name for the connection matches the one in the host's certificate.  
  
Possible values:  
0 - _(default)_ skip host verification;  
1 - verify host.  
verify_peer | integer | Whether to validate that the host's certificate is authentic.  
  
Possible values:  
0 - _(default)_ skip peer verification;  
1 - verify peer.  
uuid | string | Global unique identifier, used for linking imported web scenarios to already existing ones. Auto-generated, if not given.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if the web scenario belongs to a template  
  
### Scenario step

The scenario step object defines a specific web scenario check. It has the following properties.

name | string | Name of the scenario step.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
no | integer | Sequence number of the step in a web scenario.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
url | string | URL to be checked.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
follow_redirects | integer | Whether to follow HTTP redirects.  
  
Possible values:  
0 - don't follow redirects;  
1 - _(default)_ follow redirects.  
headers | array | [HTTP headers](/documentation/current/en/manual/api/reference/httptest/object#http-field) that will be sent when performing a request. Scenario step headers will overwrite headers specified for the web scenario.  
posts | string/array | HTTP POST variables as a string (raw post data) or as an array of [HTTP fields](/documentation/current/en/manual/api/reference/httptest/object#http-field) (form field data).  
required | string | Text that must be present in the response.  
retrieve_mode | integer | Part of the HTTP response that the scenario step must retrieve.  
  
Possible values:  
0 - _(default)_ only body;  
1 - only headers;  
2 - headers and body.  
status_codes | string | Ranges of required HTTP status codes, separated by commas.  
timeout | string | Request timeout in seconds. Accepts seconds, time unit with suffix, or a user macro.  
  
Default: 15s. Maximum: 1h. Minimum: 1s.  
variables | array | Scenario step [variables](/documentation/current/en/manual/api/reference/httptest/object#http-field).  
query_fields | array | Query fields - array of [HTTP fields](/documentation/current/en/manual/api/reference/httptest/object#http-field) that will be added to URL when performing a request.  
  
#### HTTP field

The HTTP field object defines the name and value that is used to specify the web scenario variables, HTTP headers, and POST fields or query fields. It has the following properties.

name | string | Name of header/variable/POST or GET field.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Value of header/variable/POST or GET field.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
  
### Web scenario tag

The web scenario tag object has the following properties.

tag | string | Web scenario tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Web scenario tag value.