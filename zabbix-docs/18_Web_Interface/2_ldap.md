---
title: LDAP
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/ldap
downloaded: 2025-11-14 10:39:22
---

# 2 LDAP

#### Overview

External LDAP [authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication) can be used to check user names and passwords.

Zabbix LDAP authentication works at least with Microsoft Active Directory and OpenLDAP.

If only LDAP sign-in is configured, then the user must also exist in Zabbix, however, its Zabbix password will not be used. If authentication is successful, then Zabbix will match a local username with the username attribute returned by LDAP.

#### User provisioning

It is possible to configure JIT (just-in-time) **user provisioning** for LDAP users. In this case, it is not required that a user already exists in Zabbix. The user account can be created when the user logs into Zabbix for the first time.

When an LDAP user enters their LDAP login and password, Zabbix checks the _default_ LDAP server if this user exists. If the user exists and does not have an account in Zabbix yet, a new user is created in Zabbix and the user is able to log in.

If JIT provisioning is enabled, a user group for deprovisioned users must be specified in the _Authentication_ tab.

JIT provisioning also allows to update provisioned user accounts based on changes in LDAP. For example, if a user is moved from one LDAP group to another, the user will also be moved from one group to another in Zabbix; if a user is removed from an LDAP group, the user will also be removed from the group in Zabbix and, if not belonging to any other group, added to the user group for deprovisioned users. Provisioned user accounts are updated based on the configured provisioning period or when the user logs into Zabbix.

Note that background provisioning is done by Zabbix frontend when the user is interacting with it or at least has an open frontend page in the browser. There are no dedicated background processes to provision users.

LDAP JIT provisioning is available only when LDAP is configured to use "anonymous" or "special user" for binding. For direct user binding, provisioning will be made only for user login action, because logging in user password is used for such type of binding.

#### Multiple servers

Several LDAP servers can be defined, if necessary. For example, a different server can be used to authenticate a different user group. Once LDAP servers are configured, in [user group](/documentation/current/en/manual/config/users_and_usergroups/usergroup#configuration) configuration it becomes possible to select the required LDAP server for the respective user group.

If a user is in multiple user groups and multiple LDAP servers, the first server in the list of LDAP servers sorted by name in ascending order will be used for authentication.

#### Configuration

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/auth_ldap.png)

Configuration parameters:

_Enable LDAP authentication_ | Mark the checkbox to enable LDAP authentication.  
---|---  
_Enable JIT provisioning_ | Mark the checkbox to enable JIT provisioning.  
_Servers_ | Click on _Add_ to configure an LDAP server (see LDAP server configuration below).  
_Case-sensitive login_ | Unmark the checkbox to disable case-sensitive login for usernames (enabled by default).  
Disabling case-sensitive login allows, for example, to log in as "admin" even if the Zabbix user is "Admin" or "ADMIN".  
Please note that if case-sensitive login is disabled and there are multiple Zabbix users with similar usernames (e.g., Admin and admin), the login for those users will always be denied with the following error message: "Authentication failed: supplied credentials are not unique."  
_Provisioning period_ | Set the provisioning period, i.e. how often the logged in user will be provisioned while working with the frontend.  
  
#### LDAP server configuration

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/auth_ldap_server.png)

LDAP server configuration parameters:

_Name_ | Name of the LDAP server in Zabbix configuration.  
---|---  
_Host_ | Hostname, IP or URI of the LDAP server. Examples: ldap.example.com, 127.0.0.1, ldap://ldap.example.com  
For secure LDAP server, use _ldaps_ protocol and hostname. Example: ldaps://ldap.example.com  
With OpenLDAP 2.x.x and later, a full LDAP URI of the form ldap://hostname:port or ldaps://hostname:port may be used.  
_Port_ | Port of the LDAP server. Default is 389.  
For secure LDAP connection port number is normally 636.  
Not used when using full LDAP URIs.  
_Base DN_ | Base path to user accounts in LDAP server:  
ou=Users,ou=system (for OpenLDAP),  
DC=company,DC=com (for Microsoft Active Directory)  
uid=%{user},dc=example,dc=com (for direct user binding, see a note below)  
_Search attribute_ | LDAP account attribute used for search:  
uid (for OpenLDAP),  
sAMAccountName (for Microsoft Active Directory)  
_Bind DN_ | LDAP account for binding and searching over the LDAP server, examples:  
uid=ldap_search,ou=system (for OpenLDAP),  
CN=ldap_search,OU=user_group,DC=company,DC=com (for Microsoft Active Directory)  
Anonymous binding is also supported. Note that anonymous binding potentially opens up domain configuration to unauthorized users (information about users, computers, servers, groups, services, etc.). For security reasons, disable anonymous binds on LDAP hosts and use authenticated access instead.  
_Bind password_ | LDAP password of the account for binding and searching over the LDAP server.  
_Description_ | Description of the LDAP server.  
_Configure JIT provisioning_ | Mark this checkbox to show options related to JIT provisioning.  
_Group configuration_ | Select the group configuration method:  
**memberOf** \- by searching users and their group membership attribute  
**groupOfNames** \- by searching groups through the member attribute  
Note that memberOf is preferable as it is faster; use groupOfNames if your LDAP server does not support `memberOf` or group filtering is required.  
_Group name attribute_ | Specify the attribute to get the group name from all objects in the `memberOf` attribute (see the _User group membership attribute_ field)  
The group name is necessary for user group mapping.  
_User group membership attribute_ | Specify the attribute that contains information about the groups that the user belongs to (e.g. `memberOf`).  
For example, the memberOf attribute may hold information like this: `memberOf=cn=zabbix-admin,ou=Groups,dc=example,dc=com`  
This field is available only for the memberOf method.  
_User name attribute_ | Specify the attribute that contains the user's first name.  
_User last name attribute_ | Specify the attribute that contains the user's last name.  
_User group mapping_ | Map an LDAP user group pattern to Zabbix user group and user role.  
This is required to determine what user group/role the provisioned user will get in Zabbix.  
Click on _Add_ to add a mapping.  
The _LDAP group pattern_ field supports wildcards. The group name must match an existing group.  
If an LDAP user matches several Zabbix user groups, the user becomes a member of all of them.  
If a user matches several Zabbix user roles, the user will get the one with the highest permission level among them.  
_Media type mapping_ | Map the user's LDAP media attributes (e.g. email) to Zabbix user media for sending notifications.  
_Advanced configuration_ | Click on the _Advanced configuration_ label to display advanced configuration options (see below).  
_StartTLS_ | Mark the checkbox to use the StartTLS operation when connecting to LDAP server. The connection will fall if the server doesn't support StartTLS.  
StartTLS cannot be used with servers that use the _ldaps_ protocol.  
_Search filter_ | Define a custom string when authenticating a user in LDAP. The following placeholders are supported:  
`%{attr}` \- search attribute name (uid, sAMAccountName)  
`%{user}` \- user username value to authenticate  
For example, to carry out a case-sensitive search within the case-insensitive LDAP or Microsoft Active Directory environment, the string can be defined as follows:  
`(%{attr}:caseExactMatch:=%{user})`.  
If the filter is not customized, LDAP will use the default: `(%{attr}=%{user})`.  
  
To configure an LDAP server for **direct user binding** , append an attribute uid=%{user} to the _Base DN_ parameter (for example,_uid=%{user},dc=example,dc=com_) and leave _BindDN_ and _Bind password_ parameters empty. When authenticating, a placeholder %{user} will be replaced by the username entered during login.

The following fields are specific to "groupOfNames" as the _Group configuration_ method:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/auth_ldap_server2.png)

_Group base DN_ | Base path to the groups in LDAP server.  
---|---  
_Group name attribute_ | Specify the attribute to get the group name in the specified base path to groups.  
The group name is necessary for user group mapping.  
_Group member attribute_ | Specify the attribute that contains information about the members of the group in LDAP (e.g. `member`).  
_Reference attribute_ | Specify the reference attribute for the group filter (see the _Group filter_ field).  
Then use `%{ref}` in the group filter to get values for the attribute specified here.  
_Group filter_ | Specify the filter to retrieve the group that the user is member of.  
For example, `(member=uid=%{ref},ou=Users,dc=example,dc=com)` will match "User1" if the member attribute of the group is `uid=User1,ou=Users,dc=example,dc=com` and will return the group that "User1" is a member of.  
  
In case of trouble with certificates, to make a secure LDAP connection (ldaps) work you may need to add a `TLS_REQCERT allow` line to the /etc/openldap/ldap.conf configuration file. It may decrease the security of connection to the LDAP catalog.

It is recommended to create a separate LDAP account (_Bind DN_) to perform binding and searching over the LDAP server with minimal privileges in the LDAP instead of using real user accounts (used for logging in the Zabbix frontend).  
Such an approach provides more security and does not require changing the _Bind password_ when the user changes his own password in the LDAP server.  
In the table above it's the _ldap_search_ account name.

##### Testing access

The _Test_ button allows to test user access:

_Login_ | LDAP user name to test (prefilled with the current user name from Zabbix frontend). This user name must exist in the LDAP server.  
Zabbix will not activate LDAP authentication if it is unable to authenticate the test user.  
---|---  
_User password_ | LDAP user password to test.