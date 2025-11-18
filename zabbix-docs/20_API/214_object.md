---
title: MFA object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mfa/object
downloaded: 2025-11-14 10:43:28
---

# MFA object

The following objects are directly related to the `mfa` API.

### MFA

The MFA (Multi-Factor Authentication) object has the following properties.

mfaid | ID | ID of the MFA method.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\-  _required_ for update operations  
---|---|---  
type | integer | Type of the MFA method.  
  
Possible values:  
1 - TOTP (Time-based One-Time Passwords);  
2 - Duo Universal Prompt.  
name | string | Unique name of the MFA method.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
hash_function | integer | Type of the hash function for generating TOTP codes.  
  
Possible values:  
1 - SHA-1;  
2 - SHA-256;  
3 - SHA-512.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "TOTP"  
code_length | integer | Verification code length.  
  
Possible values:  
6 - 6-digit long;  
8 - 8-digit long.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "TOTP"  
api_hostname | string | API hostname provided by the Duo authentication service.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Duo Universal Prompt"  
clientid | string | Client ID provided by the Duo authentication service.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "Duo Universal Prompt"  
client_secret | string | Client secret provided by the Duo authentication service.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
\- _required_ if `type` is set to "Duo Universal Prompt"