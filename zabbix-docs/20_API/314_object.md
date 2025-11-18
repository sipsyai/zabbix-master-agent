---
title: Token object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/token/object
downloaded: 2025-11-14 10:45:07
---

# Token object

The following objects are directly related to the `token` API.

### Token

The token object has the following properties.

tokenid | ID | ID of the token.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the token.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
description | text | Description of the token.  
userid | ID | ID of the user that the token has been assigned to.  
  
Default: _current user_.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _constant_  
lastaccess | timestamp | Most recent date and time the token was authenticated.  
  
"0" if the token has never been authenticated.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
status | integer | Token status.  
  
Possible values:  
0 - _(default)_ enabled token;  
1 - disabled token.  
expires_at | timestamp | Token expiration date and time.  
  
"0" for never-expiring tokens.  
created_at | timestamp | Token creation date and time.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
creator_userid | ID | ID of the user that created the token.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_