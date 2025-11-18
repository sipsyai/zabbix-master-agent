---
title: SAML setup with OneLogin
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/onelogin
downloaded: 2025-11-14 10:46:41
---

# 14 SAML setup with OneLogin

#### Overview

This section provides guidelines for configuring single sign-on and user provisioning into Zabbix from [OneLogin](https://onelogin.com) using SAML 2.0 authentication.

#### OneLogin configuration

##### Creating application

1\. Log into your account at OneLogin. For testing purposes, you may create a free developer account in OneLogin.

2\. In the OneLogin web interface navigate to _Applications → Applications_.

3\. Click on "Add App" and search for the appropriate app. The guidelines in this page are based on the _SCIM Provisioner with SAML (SCIM v2 Enterprise, full SAML)_ app example.

4\. To begin with, you may want to customize the display name of your app. You may also want to add the icon and app details. After that, click on _Save_.

##### Setting up SSO/SCIM provisioning

1\. In _Configuration_ -> _Application details_ , set the Zabbix single sign-on endpoint `http://<zabbix-instance-url>/zabbix/index_sso.php?acs` as the value of these fields:

  * _ACS (Consumer) URL Validator_
  * _ACS (Consumer) URL_

Note the use of "http", and not "https", so that the `acs` parameter is not cut out in the request.

![](/documentation/current/assets/en/manual/appendix/install/onelogin_endpoints.png)

It is also possible to use "https". To make that work with Zabbix, it is necessary to add to `conf/zabbix.conf.php` the following line:
    
    
    $SSO['SETTINGS'] = ['use_proxy_headers' => true];

Leave other options with their default values.

2\. In _Configuration_ -> _API connection_ , set the following values:

  * _SCIM Base URL_ : `https://<zabbix-instance-url>/zabbix/api_scim.php`
  * _SCIM JSON Template_ : should contain all custom attributes that you would like to pass to Zabbix via SCIM such as `user_name`, `user_lastname`, `user_email`, and `user_mobile`:

    
    
    {
             "schemas": [
               "urn:ietf:params:scim:schemas:core:2.0:User"
             ],
             "userName": "{$parameters.scimusername}",
             "name": {
               "familyName": "{$user.lastname}",
               "givenName": "{$user.firstname}"
             },
              "user_name": "{$user.firstname}",
              "user_lastname": "{$user.lastname}",
              "user_mobile": "{$user.phone}",
              "user_email": "{$user.email}"
           }

The attribute names are arbitrary. Different attribute names may be used, however, it is required that they match the respective field value in Zabbix SAML settings.

Note that for user provisioning to work, OneLogin needs to receive in response a 'name' attribute with 'givenName' and 'familyName', even if it was not required by the service provider. Thus it is necessary to specify this in the schema in the application configuration part.

  * _SCIM Bearer Token_ : enter a Zabbix API token with Super admin permissions.

Click on _Enable_ to activate the connection.

![](/documentation/current/assets/en/manual/appendix/install/onelogin_api_connection.png)

3\. In the _Provisioning_ page, enable the Provisioning option:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_provisioning.png)

4\. The _Parameters_ page contains a list of default parameters:

  * Make sure that the 'scimusername' matches the user login value in OneLogin (e.g. email);
  * Mark the _Include in User Provisioning_ option for the 'Groups' parameter;
  * Click on "+" to create the custom parameters that are required for SAML assertions and user provisioning such as `user_name`, `user_lastname`, `user_email`, and `user_mobile`:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_param_add.png)

When adding a parameter, make sure to mark both the _Include in SAML assertion_ and _Include in User Provisioning_ options.

  * Add a 'group' parameter that matches user roles in OneLogin. User roles will be passed as a string, separated by a semicolon `;`. The OneLogin user roles will be the used for creating user groups in Zabbix:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_param_group.png)

Verify the list of parameters:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_params.png)

5\. In the _Rules_ page, create user role mappings to the default Groups parameter.

![](/documentation/current/assets/en/manual/appendix/install/onelogin_rule_edit.png)

You may use a regular expression to pass specific roles as groups. The role names should not contain `;` as OneLogin uses it as a separator when sending an attribute with several roles.

#### Zabbix configuration

1\. In Zabbix, go to the [SAML settings](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml#setting-up-zabbix) and fill the configuration options based on the OneLogin configuration:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_zabbix_conf.png)

_IdP entity ID_ | Issuer URL  
(see SSO tab of your application in OneLogin) |   
---|---|---  
_SSO service URL_ | SAML 2.0 Endpoint (HTTP)  
(see SSO tab of your application in OneLogin) |   
_SLO service URL_ | SLO Endpoint (HTTP)  
(see SSO tab of your application in OneLogin) |   
_Username attribute_ | Custom parameter | `user_email`  
_Group name attribute_ | Custom parameter | `group`  
_User name attribute_ | Custom parameter | `user_name`  
_User last name attribute_ | Custom parameter | `user_lastname`  
  
It is also required to configure user group mapping. Media mapping is optional. Click on _Update_ to save these settings.

2\. Download the certificate provided by OneLogin and place it into `conf/certs` of the Zabbix frontend installation, as idp.crt.

Set 644 permissions to it by running:
    
    
    chmod 644 idp.crt

Copy

✔ Copied

You can access the certificate download in OneLogin in _Applications_ -> _SSO_ -> click on _View details_ under the current certificate.

It is possible to use a different certificate name and location. In that case, make sure to add to `conf/zabbix.conf.php` the following line:
    
    
    $SSO['IDP_CERT'] = 'path/to/certname.crt';

#### SCIM user provisioning

With user provisioning enabled, it is now possible to add/update users and their roles in OneLogin and have them immediately provisioned to Zabbix.

For example, you may create a new user:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_user.png)

Add it to a user role and the application that will provision the user:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_add_to_role.png)

When saving the user, it will be provisioned to Zabbix. In Application -> Users you can check the provisioning status of current application users:

![](/documentation/current/assets/en/manual/appendix/install/onelogin_provisioned.png)

If successfully provisioned, the user can be seen in the Zabbix user list.

![](/documentation/current/assets/en/manual/appendix/install/onelogin_users_zbx.png)