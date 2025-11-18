---
title: SAML
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml
downloaded: 2025-11-14 10:39:23
---

# 3 SAML  
  
#### Overview

SAML 2.0 [authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication) can be used to sign in to Zabbix.

If only SAML sign-in is configured, then the user must also exist in Zabbix, however, its Zabbix password will not be used. If authentication is successful, then Zabbix will match a local username with the username attribute returned by SAML.

#### User provisioning

It is possible to configure JIT (just-in-time) **user provisioning** for SAML users. In this case, it is not required that a user already exists in Zabbix. The user account can be created when the user logs into Zabbix for the first time.

If JIT provisioning is enabled, a user group for deprovisioned users must be specified in the _Authentication_ tab.

On top of JIT provisioning it is also possible to enable and configure SCIM (System for Cross-domain Identity Management) provisioning - _continuous_ user account management for those users that have been created by user provisioning. SCIM provisioning requires a Zabbix [API token](/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens) (with Super admin permissions) for authentication into Zabbix.

For example, if a user is moved from one SAML group to another, the user will also be moved from one group to another in Zabbix; if a user is removed from a SAML group, the user will also be removed from the group in Zabbix and, if not belonging to any other group, added to the user group for deprovisioned users.

If SCIM is enabled and configured, a SAML user will be provisioned at the moment the user logs into Zabbix and continuously updated based on changes in SAML. Already existing SAML users will not be provisioned, and only provisioned users will be updated. Note that only valid media will be added to a user when the user is provisioned or updated.

If SCIM is not enabled, a SAML user will be provisioned (and later updated) at the moment the user logs into Zabbix.

If SAML authentication is enabled, users will be able to choose between logging in locally or via SAML single sign-on. If JIT provisioning is used, then only single sign-on is possible.

#### Setting up identity provider

In order to work with Zabbix, a SAML identity provider ([onelogin.com](https://onelogin.com), [auth0.com](https://auth0.com), [okta.com](https://okta.com), etc.) needs to be configured in the following way:

  * _Assertion Consumer URL_ should be set to `<path_to_zabbix_ui>/index_sso.php?acs`
  * _Single Logout URL_ should be set to `<path_to_zabbix_ui>/index_sso.php?sls`

`<path_to_zabbix_ui>` examples: `https://example.com/zabbix/ui`, `http://another.example.com/zabbix`, `http://<any_public_ip_address>/zabbix`

#### Setting up Zabbix

It is required to install php-openssl if you want to use SAML authentication in the frontend.

To use SAML authentication Zabbix should be configured in the following way:

1\. Private key and certificate should be stored in the _ui/conf/certs_ /, unless custom paths are provided in zabbix.conf.php.

By default, Zabbix will look in the following locations:

  * ui/conf/certs/sp.key - SP private key file
  * ui/conf/certs/sp.crt - SP cert file
  * ui/conf/certs/idp.crt - IDP cert file

2\. All of the most important settings can be configured in the Zabbix frontend. However, it is possible to specify additional settings in the configuration file.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/auth_saml.png)

Configuration parameters, available in the Zabbix frontend:

_Enable SAML authentication_ | Mark the checkbox to enable SAML authentication.  
---|---  
_Enable JIT provisioning_ | Mark the checkbox to enable JIT user provisioning.  
_IDP entity ID_ | The unique entity identifier within the SAML identity provider.  
_SSO service URL_ | The URL users will be redirected to when logging in.  
_SLO service URL_ | The URL users will be redirected to when logging out. If left empty, the SLO service will not be used.  
_Username attribute_ | SAML attribute to be used as a username when logging into Zabbix.  
The list of supported values is determined by the identity provider.  
  
Examples:  
uid  
userprincipalname  
samaccountname  
username  
userusername  
urn:oid:0.9.2342.19200300.100.1.1  
urn:oid:1.3.6.1.4.1.5923.1.1.1.13  
urn:oid:0.9.2342.19200300.100.1.44  
_SP entity ID_ | The unique service provider identifier (if not matching, the operation will be rejected).  
It is possible to specify a URL or any string of data.  
_SP name ID format_ | Request a particular name ID format in the response.  
  
Examples:  
urn:oasis:names:tc:SAML:2.0:nameid-format:persistent  
urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified  
urn:oasis:names:tc:SAML:2.0:nameid-format:transient  
_Sign_ | Mark the checkboxes to select entities for which SAML signature should be enabled:  
_Messages_  
 _Assertions_  
 _AuthN requests_  
 _Logout requests_  
 _Logout responses_  
_Encrypt_ | Mark the checkboxes to select entities for which SAML encryption should be enabled:  
_Name ID_  
 _Assertions_  
_Case-sensitive login_ | Unmark the checkbox to disable case-sensitive login for usernames (enabled by default).  
Disabling case-sensitive login allows, for example, to log in as "admin" even if the Zabbix user is "Admin" or "ADMIN".  
Please note that if case-sensitive login is disabled and there are multiple Zabbix users with similar usernames (e.g., Admin and admin), the login for those users will always be denied with the following error message: "Authentication failed: supplied credentials are not unique."  
_Configure JIT provisioning_ | Mark this checkbox to show options related to JIT user provisioning.  
_Group name attribute_ | Specify the group name attribute for JIT user provisioning.  
_User name attribute_ | Specify the user name attribute for JIT user provisioning.  
_User last name attribute_ | Specify the user last name attribute for JIT user provisioning.  
_User group mapping_ | Map a SAML user group pattern to Zabbix user group and user role.  
This is required to determine what user group/role the provisioned user will get in Zabbix.  
Click on _Add_ to add a mapping.  
The _SAML group pattern_ field supports wildcards. The group name must match an existing group.  
If a SAML user matches several Zabbix user groups, the user becomes a member of all of them.  
If a user matches several Zabbix user roles, the user will get the highest permission level among them.  
_Media type mapping_ | Map the user's SAML media attributes (e.g. email) to Zabbix user media for sending notifications.  
_Enable SCIM provisioning_ | Mark this checkbox to enable SCIM 2.0 provisioning.  
  
See examples of configuring SAML identity providers for sign-in and user provisioning into Zabbix with:

  * [Microsoft Azure AD](/documentation/current/en/manual/appendix/install/azure_ad)
  * [Okta](/documentation/current/en/manual/appendix/install/okta)
  * [Onelogin](/documentation/current/en/manual/appendix/install/onelogin)

#### Notes on SCIM provisioning

For SCIM provisioning specify the path to the Zabbix frontend and append api_scim.php to it, on the identity provider side, i.e.:
    
    
    https://<path-to-zabbix-ui>/api_scim.php

Copy

✔ Copied

User attributes that are used in Zabbix (username, user name, user lastname and media attributes) need to be added as custom attributes and, if necessary, external namespace should be the same as user schema: `urn:ietf:params:scim:schemas:core:2.0:User`.

#### Advanced settings

Additional SAML parameters can be configured in the Zabbix frontend configuration file (_zabbix.conf.php_):

  * $SSO['SP_KEY'] = '<path to the SP private key file>';
  * $SSO['SP_CERT'] = '<path to the SP cert file>';
  * $SSO['IDP_CERT'] = '<path to the IDP cert file>';
  * $SSO['SETTINGS']

Zabbix uses [OneLogin's SAML PHP Toolkit](https://github.com/onelogin/php-saml/tree/3.4.1) library (version 3.4.1). The structure of $SSO['SETTINGS'] section should be similar to the structure used by the library. For the description of configuration options, see official library [documentation](https://github.com/onelogin/php-saml/tree/3.4.1/#user-content-settings).

Only the following options can be set as part of $SSO['SETTINGS']:

  * _strict_
  * _baseurl_
  * _compress_
  * _contactPerson_
  * _organization_
  * _sp_ (only options specified in this list) 
    * _attributeConsumingService_
    * _x509certNew_
  * _idp_ (only options specified in this list) 
    * _singleLogoutService_ (only one option) 
      * _responseUrl_
    * _certFingerprint_
    * _certFingerprintAlgorithm_
    * _x509certMulti_
  * _security_ (only options specified in this list) 
    * _signMetadata_
    * _wantNameId_
    * _requestedAuthnContext_
    * _requestedAuthnContextComparison_
    * _wantXMLValidation_
    * _relaxDestinationValidation_
    * _destinationStrictlyMatches_
    * _rejectUnsolicitedResponsesWithInResponseTo_
    * _signatureAlgorithm_
    * _digestAlgorithm_
    * _lowercaseUrlencoding_

All other options will be taken from the database and cannot be overridden. The _debug_ option will be ignored.

In addition, if Zabbix UI is behind a proxy or a load balancer, the custom _use_proxy_headers_ option can be used:

  * _false_ (default) - ignore the option;
  * _true_ \- use X-Forwarded-* HTTP headers for building the base URL.

If using a load balancer to connect to Zabbix instance, where the load balancer uses TLS/SSL and Zabbix does not, you must indicate 'baseurl', 'strict' and 'use_proxy_headers' parameters as follows:
    
    
    $SSO['SETTINGS'] = [
               'strict' => false,
               'baseurl' => 'https://zabbix.example.com/zabbix/',
               'use_proxy_headers' => true
           ];

Copy

✔ Copied

**Configuration example:**
    
    
    $SSO['SETTINGS'] = [
               'security' => [
                   'signatureAlgorithm' => 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha384'
                   'digestAlgorithm' => 'http://www.w3.org/2001/04/xmldsig-more#sha384',
                   // ...
               ],
               // ...
           ];

Copy

✔ Copied

##### Frontend configuration with Kerberos/ADFS

The Zabbix frontend configuration file (_zabbix.conf.php_) can be used to configure SSO with Kerberos authentication and ADFS:
    
    
    $SSO['SETTINGS'] = [
               'security' => [
                   'requestedAuthnContext' => [
                       'urn:oasis:names:tc:SAML:2.0:ac:classes:Kerberos',
                   ],
                   'requestedAuthnContextComparison' => 'exact'
               ]
           ]; 

Copy

✔ Copied

In this case, in the SAML configuration _SP name ID_ field set:
    
    
    urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified

Copy

✔ Copied