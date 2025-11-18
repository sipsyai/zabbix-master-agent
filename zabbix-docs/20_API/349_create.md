---
title: userdirectory.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/userdirectory/create
downloaded: 2025-11-14 10:45:42
---

# userdirectory.create  
  
### Description

`object userdirectory.create(object/array userDirectory)`

This method allows to create new user directories.

This method is only available to _Super admin_ user type.

### Parameters

`(object/array)` User directories to create.

The method accepts user directories with the [standard user directory properties](object#userdirectory).

### Return values

`(object)` Returns an object containing the IDs of the created user directories under the `userdirectoryids` property. The order of the returned IDs matches the order of the passed user directories.

### Examples

##### Creating a user directory

Create a user directory to authenticate users with StartTLS over LDAP. Note that to authenticate users over LDAP, [LDAP authentication](/documentation/current/en/manual/api/reference/authentication/object#authentication-object) must be enabled.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.create",
               "params": {
                   "idp_type": "1",
                   "name": "LDAP API server #1",
                   "host": "ldap://local.ldap",
                   "port": "389",
                   "base_dn": "ou=Users,dc=example,dc=org",
                   "bind_dn": "cn=ldap_search,dc=example,dc=org",
                   "bind_password": "ldapsecretpassword",
                   "search_attribute": "uid",
                   "start_tls": "1"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userdirectoryids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

##### Creating a user directory (JIT provisioning enabled)

Create a user directory to authenticate users over LDAP (with JIT provisioning enabled). Note that to authenticate users over LDAP, [LDAP authentication](/documentation/current/en/manual/api/reference/authentication/object#authentication-object) must be enabled.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "userdirectory.create",
               "params": {
                       "idp_type": "1",
                       "name": "AD server",
                       "provision_status": "1",
                       "description": "",
                       "host": "host.example.com",
                       "port": "389",
                       "base_dn": "DC=zbx,DC=local",
                       "search_attribute": "sAMAccountName",
                       "bind_dn": "CN=Admin,OU=Users,OU=Zabbix,DC=zbx,DC=local",
                       "start_tls": "0",
                       "search_filter": "",
                       "group_basedn": "OU=Zabbix,DC=zbx,DC=local",
                       "group_name": "CN",
                       "group_member": "member",
                       "group_filter": "(%{groupattr}=CN=%{ref},OU=Users,OU=Zabbix,DC=zbx,DC=local)",
                       "group_membership": "",
                       "user_username": "givenName",
                       "user_lastname": "sn",
                       "user_ref_attr": "CN",
                       "provision_media": [
                           {
                               "name": "example.com",
                               "mediatypeid": "1",
                               "attribute": "user@example.com"
                           }
                       ],
                       "provision_groups": [
                           {
                               "name": "*",
                               "roleid": "4",
                               "user_groups": [
                                   {
                                       "usrgrpid": "8"
                                   }
                               ]
                           },
                           {
                               "name": "Zabbix administrators",
                               "roleid": "2",
                               "user_groups": [
                                   {
                                       "usrgrpid": "7"
                                   },
                                   {
                                       "usrgrpid": "8"
                                   }
                               ]
                           }
                       ]
                   },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "userdirectoryids": [
                       "2"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CUserDirectory::create() in _ui/include/classes/api/services/CUserDirectory.php_.