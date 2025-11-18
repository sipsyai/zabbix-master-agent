---
title: SAML setup with Okta
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/okta
downloaded: 2025-11-14 10:46:40
---

# 13 SAML setup with Okta

This section provides guidelines for configuring [Okta](https://okta.com) to enable SAML 2.0 authentication and user provisioning for Zabbix.

#### Okta configuration

1\. Go to <https://developer.okta.com/signup/> and register/sign into your account.

2\. In the Okta web interface navigate to _Applications → Applications_.

3\. Click on _Create App Integration_.

![](/documentation/current/assets/en/manual/appendix/install/okta_app_create.png)

Select "SAML 2.0" as the sign-in method and click on _Next_.

4\. In general settings, fill in the app name and click on _Next_.

5\. In SAML configuration, enter the values provided below, then click on _Next_.

![](/documentation/current/assets/en/manual/appendix/install/okta_app_conf.png)

  * In **General** add: 
    * _Single sign-on URL_ : `http://<your-zabbix-url>/zabbix/index_sso.php?acs`  
Note the use of "http", and not "https", so that the `acs` parameter is not cut out in the request. The _Use this for Recipient URL and Destination URL_ checkbox should also be marked.
    * _Audience URI (SP Entity ID)_ : `zabbix`  
Note that this value will be used within the SAML assertion as a unique service provider identifier (if not matching, the operation will be rejected). It is possible to specify a URL or any string of data in this field.
    * _Default RelayState_ :  
Leave this field blank; if a custom redirect is required, it can be added in Zabbix in the _Users → Users_ settings.
    * Fill in other fields according to your preferences.
  * In **Attribute Statements/Group Attribute Statements** add:

![](/documentation/current/assets/en/manual/appendix/install/okta_app_conf2.png)

These attribute statements are inserted into the SAML assertions shared with Zabbix.

The attribute names used here are arbitrary examples. You may use different attribute names, however, it is required that they match the respective field value in Zabbix SAML settings.

If you want to configure SAML sign-in into Zabbix _without_ JIT user provisioning, then only the email attribute is required.

If planning to use an encrypted connection, generate the private and public encryption certificates, then upload the public certificate to Okta. The certificate upload form appears when _Assertion Encryption_ is set to "Encrypted" (click _Show Advanced Settings_ to find this parameter).

6\. In the next tab, select "I'm a software vendor. I'd like to integrate my app with Okta" and press "Finish".

7\. Navigate to the "Assignments" tab of the newly-created application and click on the _Assign_ button, then select "Assign to People" from the drop-down.

![](/documentation/current/assets/en/manual/appendix/install/okta_app_assign.png)

8\. In a popup that appears, assign the app to people that will use SAML 2.0 to authenticate with Zabbix, then click on _Save and go back_.

9\. Navigate to the "Sign On" tab and click on the _View Setup Instructions_ button.

Setup **instructions** will be opened in a new tab; keep this tab open while configuring Zabbix.

#### Zabbix configuration

1\. In Zabbix, go to the [SAML settings](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/saml#setting-up-zabbix) and fill the configuration options based on setup instructions from Okta:

![](/documentation/current/assets/en/manual/appendix/install/okta_zabbix_saml.png)

_IdP entity ID_ | Identity Provider Issuer |   
---|---|---  
_SSO service URL_ | Identity Provider Single Sign-On URL |   
_Username attribute_ | Attribute name | `usrEmail`  
_SP entity ID_ | Audience URI | `zabbix`  
_Group name attribute_ | Attribute name | `groups`  
_User name attribute_ | Attribute name | `user_name`  
_User last name attribute_ | Attribute name | `user_lastname`  
  
It is also required to configure user group and media mapping.

2\. Download the certificate provided in the Okta SAML setup instructions into _ui/conf/certs_ folder as idp.crt.

Set 644 permissions to it by running:
    
    
    chmod 644 idp.crt

Copy

✔ Copied

3\. If _Assertion Encryption_ has been set to "Encrypted" in Okta, the "Assertions" checkbox of the _Encrypt_ parameter should be marked in Zabbix as well.

4\. Press the "Update" button to save these settings.

#### SCIM provisioning

1\. To turn on SCIM provisioning, go to "General" -> "App Settings" of the application in Okta.

Mark the _Enable SCIM provisioning_ checkbox. As a result, a new _Provisioning_ tab appears.

2\. Go to the "Provisioning" tab to set up a SCIM connection:

  * In _SCIM connector base URL_ specify the path to the Zabbix frontend and append `api_scim.php` to it, i.e.:  
`https://<your-zabbix-url>/zabbix/api_scim.php`
  * _Unique identifier field for users_ : `email`
  * _Authentication mode_ : `HTTP header`
  * In _Authorization_ enter a valid API token with Super admin rights

![](/documentation/current/assets/en/manual/appendix/install/okta_scim_conn.png)

If you are experiencing authentication issues, see [Authorization header forwarding](/documentation/current/en/manual/installation/known_issues#authorization-header-forwarding).

3\. Click on _Test Connector Configuration_ to test the connection. If all is correct a success message will be displayed.

4\. In "Provisioning" -> "To App", make sure to mark the following checkboxes:

  * Create Users
  * Update User Attributes
  * Deactivate Users

This will make sure that these request types will be sent to Zabbix.

5\. Make sure that all attributes defined in SAML are defined in SCIM. You can access the profile editor for your app in "Provisioning" -> "To App", by clicking on _Go to Profile Editor_.

Click on _Add Attribute_. Fill the values for _Display name_ , _Variable name_ , _External name_ with the SAML attribute name, for example, `user_name`.

![](/documentation/current/assets/en/manual/appendix/install/okta_add_attr.png)

_External namespace_ should be the same as user schema: `urn:ietf:params:scim:schemas:core:2.0:User`

6\. Go to "Provisioning" -> "To App" -> "Attribute Mappings" of your application. Click on _Show Unmapped Attributes_ at the bottom. Newly added attributes appear.

7\. Map each added attribute.

![](/documentation/current/assets/en/manual/appendix/install/okta_map_attr.png)

8\. Add users in the "Assignments" tab. The users previously need to be added in _Directory_ -> _People_. All these assignments will be sent as requests to Zabbix.

9\. Add groups in the "Push Groups" tab. The user group mapping pattern in Zabbix SAML settings must match a group specified here. If there is no match, the user cannot be created in Zabbix.

Information about group members is sent every time when some change is made.