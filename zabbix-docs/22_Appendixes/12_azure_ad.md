---
title: SAML setup with Microsoft Entra ID
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/azure_ad
downloaded: 2025-11-14 10:46:39
---

# 12 SAML setup with Microsoft Entra ID

#### Overview

This section provides guidelines for configuring single sign-on and user provisioning into Zabbix from Microsoft Entra ID (formerly Microsoft Azure Active Directory) using SAML 2.0 authentication.

#### Microsoft Entra ID configuration

##### Creating application

1\. Log into Microsoft Entra admin center at [Microsoft Entra ID](https://entra.microsoft.com). For testing purposes, you may create a free trial account in Microsoft Entra ID.

2\. In Microsoft Entra admin center select _Applications_ -> _Enterprise applications_ -> _New application_ -> _Create your own application_.

3\. Add the name of your app and select the _Integrate any other application..._ option. After that, click on _Create_.

![](/documentation/current/assets/en/manual/appendix/install/entra_create_app.png)

##### Setting up single sign-on

1\. In your application page, go to _Set up single sign on_ and click on _Get started_. Then select _SAML_.

2\. Edit _Basic SAML Configuration_ :

  * In _Identifier (Entity ID)_ set a unique name to identify your app to Microsoft Entra ID, for example, `zabbix`;
  * In _Reply URL (Assertion Consumer Service URL)_ set the Zabbix single sign-on endpoint: `https://<path-to-zabbix-ui>/index_sso.php?acs`:

![](/documentation/current/assets/en/manual/appendix/install/entra_basic_saml.png)

Note that "https" is required. To make that work with Zabbix, it is necessary to add to `conf/zabbix.conf.php` the following line:
    
    
    $SSO['SETTINGS'] = ['use_proxy_headers' => true];

3\. Edit _Attributes & Claims_. You must add all attributes that you want to pass to Zabbix (user_name, user_lastname, user_email, user_mobile, groups).

The attribute names are arbitrary. Different attribute names may be used, however, it is required that they match the respective field value in Zabbix SAML settings.

  * Click on _Add new claim_ to add an attribute:

![](/documentation/current/assets/en/manual/appendix/install/azure_claim.png)

  * Click on _Add a group claim_ to add an attribute for passing groups to Zabbix:

![](/documentation/current/assets/en/manual/appendix/install/entra_claim_group.png)

It is important in this claim that the group names (rather than group IDs) are passed to Zabbix by the selected _Source attribute_. Otherwise JIT user provisioning will not work properly.

4\. In _SAML Certificates_ download the Base64 certificate provided by Entra ID and place it into `conf/certs` of the Zabbix frontend installation.

Set 644 permissions to it by running:
    
    
    chmod 644 entra.cer

Copy

✔ Copied

Make sure that `conf/zabbix.conf.php` contains the line:
    
    
    $SSO['IDP_CERT'] = 'conf/certs/entra.cer';

5\. Use the values from _Set up <your app name>_ in Entra ID to configure Zabbix SAML authentication (see next section):

![](/documentation/current/assets/en/manual/appendix/install/entra_sso_settings.png)

#### Zabbix configuration

1\. In Zabbix, go to the [SAML settings](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml#setting-up-zabbix) and fill the configuration options based on the Entra ID configuration:

![](/documentation/current/assets/en/manual/appendix/install/entra_zabbix_conf.png)

_IdP entity ID_ | Microsoft Entra identifier |   
---|---|---  
_SSO service URL_ | Login URL |   
_SLO service URL_ | Logout URL |   
_SP entity ID_ | Identifier (Entity ID) |   
_Username attribute_ | Custom attribute (claim) | `user_email`  
_Group name attribute_ | Custom attribute (claim) | `groups`  
_User name attribute_ | Custom attribute (claim) | `user_name`  
_User last name attribute_ | Custom attribute (claim) | `user_lastname`  
  
It is also required to configure user group mapping. Media mapping is optional.

Click on _Update_ to save these settings.

#### SCIM user provisioning

1\. In your Entra ID application page, from the main menu open the Provisioning page. Click on _Get started_ and then select Automatic provisioning mode:

  * In _Tenant URL_ , set the following value: `https://<path-to-zabbix-ui>/api_scim.php`
  * In _Secret token_ , enter a Zabbix API token with Super admin permissions.
  * Click on _Test connection_ to see if the connection is established.

![](/documentation/current/assets/en/manual/appendix/install/entra_api_connection.png)

2\. Now you can add all the attributes that will be passed with SCIM to Zabbix. To do that, click on _Mappings_ and then on _Provision Microsoft Entra ID Users_.

![](/documentation/current/assets/en/manual/appendix/install/entra_scim_mappings_add.png)

At the bottom of the Attribute Mapping list, enable _Show advanced options_ , and then click on _Edit attribute list for customappsso_.

At the bottom of the attribute list, add your own attributes with type 'String':

![](/documentation/current/assets/en/manual/appendix/install/azure_scim_attrib.png)

Save the list.

3\. Now you can add mappings for the added attributes. At the bottom of the Attribute Mapping list, click on _Add New Mapping_ and create mappings as shown below:

![](/documentation/current/assets/en/manual/appendix/install/azure_scim_mapping.png)

When all mappings are added, save the list of mappings.

![](/documentation/current/assets/en/manual/appendix/install/azure_scim_mappings.png)

4\. As a prerequisite of user provisioning into Zabbix, you must have users and groups configured in Entra ID.

To do that, go to _Microsoft Entra admin center_ and then add users/groups in the respective Users and Groups pages.

5\. When users and groups have been created in Entra ID, you can go to the _Users and groups_ menu of your application and add them to the app.

6\. Go to the _Provisioning_ menu of your app, and click on _Start provisioning_ to have users provisioned to Zabbix.

Note that the Users PATCH request in Entra ID does not support changes in media.

#### Authentication request signing

It is possible to configure Entra ID to [validate the signature](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/howto-enforce-signed-saml-authentication) of signed authentication requests.

To make this work, create public/private keys:
    
    
    openssl req -x509 -newkey rsa:4096 -keyout /usr/share/zabbix/conf/certs/request-sign.key -out /usr/share/zabbix/conf/certs/request-sign.pem -sha256 -days 1825 -nodes

Copy

✔ Copied

Assign permissions:
    
    
    chown apache /usr/share/zabbix/conf/certs/request-sign.key 
           chmod 400 /usr/share/zabbix/conf/certs/request-sign.key

Copy

✔ Copied

Update Zabbix frontend configuration by adding:
    
    
    $SSO['SP_KEY'] = 'conf/certs/request-sign.key';
           $SSO['SP_CERT'] = 'conf/certs/request-sign.crt';

Copy

✔ Copied

#### Troubleshooting

Authentication issues may occur with MicroSoft Edge browsers when a user, trying to login to Zabbix via SAML, is already logged in with the MicroSoft Edge profile. As a sign of such issue the user may be able to log in to Zabbix using MicroSoft Edge in private mode.

To avoid authentication issues in this case it may be necessary to set `requestedAuthnContext` to "false" in the Zabbix frontend configuration file (_zabbix.conf.php_).
    
    
    $SSO['SETTINGS'] = [
               'security' => [
                   'requestedAuthnContext' => false
               ]
           ]; 

Copy

✔ Copied