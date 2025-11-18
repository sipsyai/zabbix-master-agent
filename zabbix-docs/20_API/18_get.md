---
title: authentication.get
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/authentication/get
downloaded: 2025-11-14 10:40:11
---

# authentication.get  
  
### Description

`object authentication.get(object parameters)`

The method allows to retrieve authentication object according to the given parameters.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the desired output.

The method supports only one parameter.

output | query | This parameter is described in the [reference commentary](/documentation/current/en/manual/api/reference_commentary#common-get-method-parameters).  
---|---|---  
  
### Return values

`(object)` Returns authentication object.

### Examples

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "authentication.get",
               "params": {
                   "output": "extend"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "authentication_type": "0",
                   "http_auth_enabled": "0",
                   "http_login_form": "0",
                   "http_strip_domains": "",
                   "http_case_sensitive": "1",
                   "ldap_auth_enabled": "0",
                   "ldap_case_sensitive": "1",
                   "ldap_userdirectoryid": "0",
                   "saml_auth_enabled": "0",
                   "saml_case_sensitive": "0",
                   "passwd_min_length": "8",
                   "passwd_check_rules": "15",
                   "jit_provision_interval": "1h",
                   "saml_jit_status": "0",
                   "ldap_jit_status": "0",
                   "disabled_usrgrpid": "9",
                   "mfa_status": "0",
                   "mfaid": "0"
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CAuthentication::get() in _ui/include/classes/api/services/CAuthentication.php_.