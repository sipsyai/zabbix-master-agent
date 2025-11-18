---
title: User directory object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/userdirectory/object
downloaded: 2025-11-14 10:45:41
---

# User directory object

The following objects are directly related to the `userdirectory` API.

### User directory

The user directory object has the following properties.

userdirectoryid | ID | ID of the user directory.  
  
If a user directory is deleted, the value of the [User object](/documentation/current/en/manual/api/reference/user/object#user) property `userdirectoryid` is set to "0" for all users that are linked to the deleted user directory.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
idp_type | integer | Type of the authentication protocol used by the identity provider for the user directory.  
Note that only one user directory of type SAML can exist.  
  
Possible values:  
1 - User directory of type LDAP;  
2 - User directory of type SAML.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
group_name | string | LDAP/SAML user directory attribute that contains the group name used to map groups between the LDAP/SAML user directory and Zabbix.  
  
Example: _cn_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `provision_status` is set to "Enabled" and `saml_jit_status` of [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication) is set to "Enabled for configured SAML IdPs"  
user_username | string | LDAP/SAML user directory attribute (also SCIM attribute if `scim_status` is set to "SCIM provisioning is enabled") that contains the user's name which is used as the value for the [User object](/documentation/current/en/manual/api/reference/user/object#user) property `name` when the user is provisioned.  
  
Examples: _cn_ , _commonName_ , _displayName_ , _name_  
user_lastname | string | LDAP/SAML user directory attribute (also SCIM attribute if `scim_status` is set to "SCIM provisioning is enabled") that contains the user's last name which is used as the value for the [User object](/documentation/current/en/manual/api/reference/user/object#user) property `surname` when the user is provisioned.  
  
Examples: _sn_ , _surname_ , _lastName_  
provision_status | integer | Provisioning status of the user directory.  
  
Possible values:  
0 - _(default)_ Disabled (provisioning of users created by this user directory is disabled);  
1 - Enabled (provisioning of users created by this user directory is enabled; additionally, the status of LDAP or SAML provisioning (`ldap_jit_status` or `saml_jit_status` of [Authentication object](/documentation/current/en/manual/api/reference/authentication/object#authentication)) must be enabled).  
provision_groups | array | Array of [provisioning groups mappings](object#provisioning-groups-mappings) objects for mapping LDAP/SAML user group pattern to Zabbix user group and user role.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `provision_status` is set to "Enabled"  
provision_media | array | Array of [media type mappings](object#media-type-mappings) objects for mapping user's LDAP/SAML media attributes (e.g., email) to Zabbix user media for sending notifications.  
**[LDAP](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap)-specific properties:**  
name | string | Unique name of the user directory.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type LDAP"  
host | string | Host name, IP or URI of the LDAP server.  
URI must contain schema (`ldap://` or `ldaps://`), host, and port (optional).  
  
Examples:  
_host.example.com_  
 _127.0.0.1_  
 _ldap://ldap.example.com:389_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type LDAP"  
port | integer | Port of the LDAP server.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type LDAP"  
base_dn | string | LDAP user directory base path to user accounts.  
  
Examples:  
_ou=Users,dc=example,dc=org_  
 _ou=Users,ou=system_ (for OpenLDAP)  
_DC=company,DC=com_ (for Microsoft Active Directory)  
_uid=%{user},dc=example,dc=com_ (for direct user binding; placeholder "_%{user}_ " is mandatory)  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type LDAP"  
search_attribute | string | LDAP user directory attribute by which to identify the user account from the information provided in the login request.  
  
Examples:  
_uid_ (for OpenLDAP)  
_sAMAccountName_ (for Microsoft Active Directory)  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type LDAP"  
bind_dn | string | LDAP server account for binding and searching over the LDAP server.  
  
For direct user binding and anonymous binding, `bind_dn` must be empty.  
  
Examples:  
_uid=ldap_search,ou=system_ (for OpenLDAP)  
_CN=ldap_search,OU=user_group,DC=company,DC=com_ (for Microsoft Active Directory)  
_CN=Admin,OU=Users,OU=Zabbix,DC=zbx,DC=local_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
bind_password | string | LDAP password of the account for binding and searching over the LDAP server.  
  
For direct user binding and anonymous binding, `bind_password` must be empty.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
description | string | Description of the user directory.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
group_basedn | string | LDAP user directory base path to groups; used to configure a user membership check in the LDAP user directory.  
  
Ignored when provisioning a user if `group_membership` is set.  
  
Example: _ou=Groups,dc=example,dc=com_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
group_filter | string | Filter string for retrieving LDAP user directory groups that the user is a member of; used to configure a user membership check in the LDAP user directory.  
  
Ignored when provisioning a user if `group_membership` is set.  
  
Supported `group_filter` placeholders:  
_%{attr}_ \- search attribute (replaced by the `search_attribute` property value);  
_%{groupattr}_ \- group attribute (replaced by the `group_member` property value);  
_%{host}_ \- host name, IP or URI of the LDAP server (replaced by the `host` property value);  
_%{user}_ \- Zabbix user username.  
  
Default: _(%{groupattr}=%{user})_  
  
Examples:  
\- _(member=uid=%{ref},ou=Users,dc=example,dc=com)_ will match "User1" if an LDAP group object contains the "_member_ " attribute with the value "_uid=User1,ou=Users,dc=example,dc=com_ ", and will return the group that "User1" is a member of;  
\- _(%{groupattr}=cn=%{ref},ou=Users,ou=Zabbix,DC=example,DC=com)_ will match "User1" if an LDAP group object contains the attribute specified in the `group_member` property with the value "_cn=User1,ou=Users,ou=Zabbix,DC=example,DC=com_ ", and will return the group that "User1" is a member of.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
group_member | string | LDAP user directory attribute that contains information about the group members; used to configure a user membership check in the LDAP user directory.  
  
Ignored when provisioning a user if `group_membership` is set.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
group_membership | string | LDAP user directory attribute that contains information about the groups that a user belongs to.  
  
Example: _memberOf_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
search_filter | string | Custom filter string used to locate and authenticate a user in an LDAP user directory based on the information provided in the login request.  
  
Supported `search_filter` placeholders:  
_%{attr}_ \- search attribute name (e.g., _uid_ , _sAMAccountName_);  
_%{user}_ \- Zabbix user username.  
  
Default: _(%{attr}=%{user})_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
start_tls | integer | LDAP server configuration option that allows the communication with the LDAP server to be secured using Transport Layer Security (TLS).  
  
Note that `start_tls` must be set to "Disabled" for hosts using the `ldaps://` protocol.  
  
Possible values:  
0 - _(default)_ Disabled;  
1 - Enabled.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
user_ref_attr | string | LDAP user directory attribute used to reference a user object. The value of `user_ref_attr` is used to get values from the specified attribute in the user directory and place them instead of the _%{ref}_ placeholder in the `group_filter` string.  
  
Examples: _cn_ , _uid_ , _member_ , _uniqueMember_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type LDAP"  
**[SAML](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml)-specific properties:**  
idp_entityid | string | URI that identifies the identity provider and is used to communicate with the identity provider in SAML messages.  
  
Example: _https://idp.example.com/idp_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type SAML"  
sp_entityid | string | URL or any string that identifies the identity provider's service provider.  
  
Examples:  
_https://idp.example.com/sp_  
 _zabbix_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type SAML"  
username_attribute | string | SAML user directory attribute (also SCIM attribute if `scim_status` is set to "SCIM provisioning is enabled") that contains the user's username which is compared with the value of the [User object](/documentation/current/en/manual/api/reference/user/object#user) property `username` when authenticating.  
  
Examples: _uid_ , _userprincipalname_ , _samaccountname_ , _username_ , _userusername_ , _urn:oid:0.9.2342.19200300.100.1.1_ , _urn:oid:1.3.6.1.4.1.5923.1.1.1.13_ , _urn:oid:0.9.2342.19200300.100.1.44_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type SAML"  
sso_url | string | URL of the identity provider's SAML single sign-on service, to which Zabbix will send the SAML authentication requests.  
  
Example: _http://idp.example.com/idp/sso/saml_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `idp_type` is set to "User directory of type SAML"  
slo_url | string | URL of the identity provider's SAML single log-out service, to which Zabbix will send the SAML logout requests.  
  
Example: _https://idp.example.com/idp/slo/saml_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
encrypt_nameid | integer | Whether the SAML name ID should be encrypted.  
  
Possible values:  
0 -  _(default)_ Do not encrypt name ID;  
1 - Encrypt name ID.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
encrypt_assertions | integer | Whether the SAML assertions should be encrypted.  
  
Possible values:  
0 -  _(default)_ Do not encrypt assertions;  
1 - Encrypt assertions.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
nameid_format | string | Name ID format of the SAML identity provider's service provider.  
  
Examples:  
_urn:oasis:names:tc:SAML:2.0:nameid-format:persistent_  
 _urn:oasis:names:tc:SAML:2.0:nameid-format:transient_  
 _urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos_  
 _urn:oasis:names:tc:SAML:2.0:nameid-format:entity_  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
scim_status | integer | Whether SCIM provisioning for SAML is enabled or disabled.  
  
Possible values:  
0 -  _(default)_ SCIM provisioning is disabled;  
1 - SCIM provisioning is enabled.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
sign_assertions | integer | Whether the SAML assertions should be signed with a SAML signature.  
  
Possible values:  
0 -  _(default)_ Do not sign assertions;  
1 - Sign assertions.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
sign_authn_requests | integer | Whether the SAML AuthN requests should be signed with a SAML signature.  
  
Possible values:  
0 -  _(default)_ Do not sign AuthN requests;  
1 - Sign AuthN requests.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
sign_messages | integer | Whether the SAML messages should be signed with a SAML signature.  
  
Possible values:  
0 -  _(default)_ Do not sign messages;  
1 - Sign messages.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
sign_logout_requests | integer | Whether the SAML logout requests should be signed with a SAML signature.  
  
Possible values:  
0 -  _(default)_ Do not sign logout requests;  
1 - Sign logout requests.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
sign_logout_responses | integer | Whether the SAML logout responses should be signed with a SAML signature.  
  
Possible values:  
0 -  _(default)_ Do not sign logout responses;  
1 - Sign logout responses.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `idp_type` is set to "User directory of type SAML"  
  
#### Media type mappings

The media type mappings object has the following properties.

userdirectory_mediaid | ID | Media type mapping ID.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
---|---|---  
name | string | Visible name in the list of media type mappings.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
mediatypeid | ID | ID of the media type to be created; used as the value for the [Media object](/documentation/current/en/manual/api/reference/user/object#media) property `mediatypeid`.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
attribute | string | LDAP/SAML user directory attribute (also SCIM attribute if `scim_status` is set to "SCIM provisioning is enabled") that contains the user's media (e.g., _user@example.com_) which is used as the value for the [Media object](/documentation/current/en/manual/api/reference/user/object#media) property `sendto`.  
  
If present in data received from the LDAP/SAML identity provider, and the value is not empty, this will trigger media creation for the provisioned user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
active | integer | User media `active` property value when media is created for the provisioned user.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
severity | integer | User media `severity` property value when media is created for the provisioned user.  
  
Default: 63.  
period | string | User media `period` property value when media is created for the provisioned user.  
  
Default: 1-7,00:00-24:00.  
  
#### Provisioning groups mappings

The provisioning groups mappings has the following properties.

name | string | Full name of a group (e.g., _Zabbix administrators_) in LDAP/SAML user directory (also SCIM if `scim_status` is set to "SCIM provisioning is enabled").  
Supports the wildcard character "*".  
Unique across all provisioning groups mappings.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
roleid | ID | ID of the user role to assign to the user.  
  
If multiple provisioning groups mappings are matched, the role of the highest user type (_User_ , _Admin_ , or _Super admin_) is assigned to the user. If there are multiple roles with the same user type, the first role (sorted in alphabetical order) is assigned to the user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
user_groups | array | Array of Zabbix user group ID objects. Each object has the following properties:  
`usrgrpid` \- `(ID)` ID of Zabbix user group to assign to the user.  
  
If multiple provisioning groups mappings are matched, Zabbix user groups of all matched mappings is assigned to the user.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_