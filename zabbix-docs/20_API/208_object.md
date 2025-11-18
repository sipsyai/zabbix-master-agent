---
title: Media type object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mediatype/object
downloaded: 2025-11-14 10:43:22
---

# Media type object

The following objects are directly related to the `mediatype` API.

### Media type

The media type object has the following properties.

mediatypeid | ID | ID of the media type.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the media type.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
type | integer | Transport used by the media type.  
  
Possible values:  
0 - Email;  
1 - Script;  
2 - SMS;  
4 - Webhook.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
exec_path | string | Name of the script file (e.g., notification.sh) that is located in the directory specified in the [AlertScriptsPath](/documentation/current/en/manual/appendix/config/zabbix_server#alertscriptspath) server configuration parameter.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Script"  
gsm_modem | string | Serial device name of the GSM modem.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "SMS"  
passwd | string | Authentication password.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_authentication` is set to "Normal password"  
provider | integer | Email provider.  
  
Possible values:  
0 - _(default)_ Generic SMTP;  
1 - Gmail;  
2 - Gmail relay;  
3 - Office365;  
4 - Office365 relay.  
smtp_email | string | Email address from which notifications will be sent.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Email"  
smtp_helo | string | SMTP HELO.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Email"  
smtp_server | string | SMTP server.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Email"  
smtp_port | integer | SMTP server port to connect to.  
  
Default: 25.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Email"  
smtp_security | integer | SMTP connection security level to use.  
  
Possible values:  
0 - _(default)_ None;  
1 - STARTTLS;  
2 - SSL/TLS.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Email"  
smtp_verify_host | integer | SSL verify host for SMTP.  
  
Possible values:  
0 - _(default)_ No;  
1 - Yes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_security` is set to "STARTTLS" or "SSL/TLS"  
smtp_verify_peer | integer | SSL verify peer for SMTP.  
  
Possible values:  
0 - _(default)_ No;  
1 - Yes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_security` is set to "STARTTLS" or "SSL/TLS"  
smtp_authentication | integer | SMTP authentication method to use.  
  
Possible values:  
0 - _(default)_ None;  
1 - Normal password;  
2 - OAuth token.  
OAuth authentication is not allowed for _Office365 relay_ email provider.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Email"  
redirection_url | string | Zabbix frontend URL to redirect back OAuth authorization.  
  
Default:  
Value of API settings property `url` with part `zabbix.php?action=oauth.authorize`  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
client_id | string | The client identifier registered within the OAuth authorization server.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
client_secret | string | The client secret registered within the OAuth authorization server. Accessible only for user of type Super Admin.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
authorization_url | string | OAuth URL, with parameters, to get access and refresh tokens.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
token_url | string | OAuth URL to exchange authorization token to access and refresh tokens.  
This URL also is used by server to refresh invalid access token.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
tokens_status | integer | Bit mask on tokens' status.  
  
Possible values:  
0 - (default) Both tokens contain invalid value  
1 - Access token contains valid value  
2 - Refresh token contains valid value  
3 - Both tokens contain valid value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_authentication` is set to "OAuth token"  
access_token | string | OAuth access token value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
access_token_updated | timestamp | Timestamp of last modification of `access_token` done by server when refreshing with `refresh_token` or API on token changes.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_authentication` is set to "OAuth token"  
access_expires_in | integer | Time in seconds when `access_token` will become outdated and will require to make request to `refresh_url`.  
Is set by Zabbix server on `access_token` refresh or by API on token changes.  
  
Timestamp is calculated by adding value of `access_token_updated`.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_authentication` is set to "OAuth token"  
refresh_token | string | OAuth refresh token value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `smtp_authentication` is set to "OAuth token"  
status | integer | Whether the media type is enabled.  
  
Possible values:  
0 - _(default)_ Enabled;  
1 - Disabled.  
username | string | User name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `smtp_authentication` is set to "Normal password"  
maxsessions | integer | The maximum number of alerts that can be processed in parallel.  
  
Possible values if `type` is set to "SMS": 1.  
  
Possible values if `type` is set to "Email", "Script", or "Webhook": 0-100.  
  
Default: 1.  
maxattempts | integer | The maximum number of attempts to send an alert.  
  
Possible values: 1-100.  
  
Default: 3.  
attempt_interval | string | The interval between retry attempts.  
Accepts seconds and time unit with suffix.  
  
Possible values: 0-1h.  
  
Default: 10s.  
message_format | integer | Message format.  
  
Possible values:  
0 - Plain text;  
1 - _(default)_ HTML.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Email"  
script | text | Webhook script body (JavaScript).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Webhook"  
timeout | string | Webhook script timeout.  
Accepts seconds and time unit with suffix.  
  
Possible values: 1-60s.  
  
Default: 30s.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Webhook"  
process_tags | integer | Process JSON property values in Webhook script response as tags. These tags are added to any existing problem tags.  
  
Possible values:  
0 - _(default)_ Ignore webhook script response;  
1 - Process webhook script response as tags.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Webhook"  
show_event_menu | integer | Include an entry in the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu) that links to a custom URL. Also adds the `urls` property to the output of [problem.get](/documentation/current/en/manual/api/reference/problem/get) and [event.get](/documentation/current/en/manual/api/reference/event/get).  
  
Possible values:  
0 - _(default)_ Do not include event menu entry or `urls` property;  
1 - Include event menu entry and `urls` property.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Webhook"  
event_menu_url | string | URL used in the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu) entry and in the `urls` property returned by [problem.get](/documentation/current/en/manual/api/reference/problem/get) and [event.get](/documentation/current/en/manual/api/reference/event/get).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `show_event_menu` is set to "Include event menu entry and `urls` property"  
event_menu_name | string | Name used for the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu) entry and in the `urls` property returned by [problem.get](/documentation/current/en/manual/api/reference/problem/get) and [event.get](/documentation/current/en/manual/api/reference/event/get).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `show_event_menu` is set to "Include event menu entry and `urls` property"  
parameters | array | Webhook or script parameters.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `type` is set to "Webhook" or "Script"  
description | text | Media type description.  
  
#### Webhook parameters

Webhook parameters have the following properties.

name | string | Parameter name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Parameter value, supports macros.  
Supported macros are described on the [Supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) page.  
  
#### Script parameters

Script parameters have the following properties.

sortorder | integer | The order in which parameter values will be passed to the script as command-line arguments, starting with 0 as the first one.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Parameter value, supports macros.  
Supported macros are described on the [Supported macros](/documentation/current/en/manual/appendix/macros/supported_by_location) page.  
  
### Message template

The message template object defines a template that will be used as a default message for action operations to send a notification. It has the following properties.

eventsource | integer | Event source.  
  
Possible values:  
0 - Triggers;  
1 - Discovery;  
2 - Autoregistration;  
3 - Internal;  
4 - Services.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
recovery | integer | Operation mode.  
  
Possible values:  
0 - Operations;  
1 - Recovery operations;  
2 - Update operations.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
subject | string | Message subject.  
message | string | Message text.