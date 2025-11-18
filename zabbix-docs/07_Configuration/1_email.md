---
title: Email
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/email
downloaded: 2025-11-14 10:36:11
---

# 1 Email  
  
#### Overview

To configure email as the delivery channel for messages, you need to configure email as the media type and assign specific addresses to users.

Multiple notifications for single event will be grouped together on the same email thread.

#### Configuration

To configure email as the media type:

  1. Go to _Alerts > Media types_.
  2. Click on _Create media type_ (or click on _Email_ in the list of pre-defined media types).

The **Media type** tab contains general media type attributes:

![](/documentation/current/assets/en/manual/config/notifications/media/media_email.png)

All mandatory input fields are marked with a red asterisk.

Password is exported in clear text when exporting email media type configuration.

The following parameters are specific for the email media type:

_Email provider_ | Select the email provider: _Generic SMTP_ , _Gmail_ , _Gmail relay_ , _Office365_ , or _Office365 relay_.  
If you select the Gmail/Office365-related options, you will only need to supply the sender email address and password; such options as _SMTP server_ , _SMTP server port_ , _SMTP helo_ , and _Connection security_ will be automatically filled by Zabbix. See also: [Automated Gmail/Office365 media types](/documentation/current/en/manual/config/notifications/media/email/gmail_office).  
---|---  
_SMTP server_ | Set an SMTP server to handle outgoing messages.  
This field is available if _Generic SMTP_ is selected as the email provider.  
_SMTP server port_ | Set the SMTP server port to handle outgoing messages.  
This field is available if _Generic SMTP_ is selected as the email provider.  
_Email_ | The address entered here will be used as the **From** address for the messages sent.  
Adding a sender display name (like "Zabbix_info" in _Zabbix_info <zabbix@company.com>_ in the screenshot above) with the actual email address is supported.  
There are some restrictions on display names in Zabbix emails in comparison to what is allowed by RFC 5322, as illustrated by examples:  
Valid examples:  
_zabbix@company.com_ (only email address, no need to use angle brackets)  
_Zabbix_info <zabbix@company.com>_ (display name and email address in angle brackets)  
_∑Ω-monitoring <zabbix@company.com>_ (UTF-8 characters in display name)  
Invalid examples:  
_Zabbix HQ zabbix@company.com_ (display name present but no angle brackets around email address)  
_"Zabbix\@\ <H(comment)Q\>" <zabbix@company.com>_ (although valid by RFC 5322, quoted pairs and comments are not supported in Zabbix emails)  
_SMTP helo_ | Set a correct SMTP helo value, normally a domain name.  
If empty, the domain name of the email will be sent (i.e., what comes after `@` in the _Email_ field). If it is impossible to fetch the domain name, a debug-level warning will be logged and the server hostname will be sent as the domain for HELO command.  
This field is available if _Generic SMTP_ is selected as the email provider.  
_Connection security_ | Select the level of connection security:  
**None** \- do not use the [CURLOPT_USE_SSL](http://curl.haxx.se/libcurl/c/CURLOPT_USE_SSL.html) option  
**STARTTLS** \- use the CURLOPT_USE_SSL option with CURLUSESSL_ALL value  
**SSL/TLS** \- use of CURLOPT_USE_SSL is optional  
_SSL verify peer_ | Mark the checkbox to verify the SSL certificate of the SMTP server.  
The value of "SSLCALocation" server configuration directive should be put into [CURLOPT_CAPATH](http://curl.haxx.se/libcurl/c/CURLOPT_CAPATH.html) for certificate validation.  
This sets cURL option [CURLOPT_SSL_VERIFYPEER](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYPEER.html).  
_SSL verify host_ | Mark the checkbox to verify that the _Common Name_ field or the _Subject Alternate Name_ field of the SMTP server certificate matches.  
This sets cURL option [CURLOPT_SSL_VERIFYHOST](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYHOST.html).  
_Authentication_ | Select the level of authentication:  
**None** \- no cURL options are set  
**Username and password** \- implies "AUTH=*" leaving the choice of authentication mechanism to cURL  
**OAuth** \- OAuth authentication  
OAuth authentication is not supported for the _Office365 relay_ email provider.  
_Username_ | User name to use in authentication.  
This sets the value of [CURLOPT_USERNAME](http://curl.haxx.se/libcurl/c/CURLOPT_USERNAME.html).  
[User macros](/documentation/current/en/manual/appendix/macros/supported_by_location_user#other-locations) supported.  
_Password_ | Password to use in authentication.  
This sets the value of [CURLOPT_PASSWORD](http://curl.haxx.se/libcurl/c/CURLOPT_PASSWORD.html).  
[User macros](/documentation/current/en/manual/appendix/macros/supported_by_location_user#other-locations) supported.  
The value entered here is exported as is when media type configuration is exported. To avoid exposing sensitive credentials in exported files, use a user macro (for example `{$EMAIL_SMTP_PASSWORD}`) instead of a literal password — the macro reference will be exported while the secret value should be (re)configured on the destination system.  
_OAuth tokens_ | Click on _Configure_ to set up parameters for retrievieng OAuth tokens in a new window.  
This field is only available if "OAuth" is selected in the _Authentication_ field.  
_Message format_ | Select message format:  
**HTML** \- send as HTML  
**Plain text** \- send as plain text  
  
To enable SMTP authentication, Zabbix server must be compiled with the `--with-libcurl` [compilation](/documentation/current/en/manual/installation/install#configure-the-sources) option, which requires libcurl (see [server](/documentation/current/en/manual/installation/requirements#serverproxy) requirements for version details).

See also [common media type parameters](/documentation/current/en/manual/config/notifications/media#common-parameters) for details on how to configure default messages and alert processing options.

#### OAuth tokens

The following parameters are required for retrieving OAuth tokens:

![](/documentation/current/assets/en/manual/config/notifications/media/media_email_oauth.png)

_Redirection endpoint_ | Enter Zabbix frontend URL where the OAuth service will redirect back the OAuth authorization (using format `https://<zabbix-frontend-url>/zabbix.php?action=oauth.authorize`).  
It is set automatically for a new email media type when the [frontend URL](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) is defined.  
---|---  
_Client ID_ | Enter unique identifier of the client app registered within the OAuth authorization server.  
_Client secret_ | Enter private secret of the client app registered within the OAuth authorization server.  
_Authorization endpoint_ | Enter the OAuth authorization server URL for requesting user authorization.  
_Authorization parameters_ | Enter parameters for the authorization endpoint.  
_Authorization code_ | Enter the authorization code:  
**Automatic** \- the code will be retrieved automatically through a redirection page  
**Manual** \- enter the code manually if automatic retrieval fails  
_Token endpoint_ | Enter the OAuth authorization server URL to exchange the authorization code for access and refresh tokens.  
_Token parameters_ | Enter parameters for the access token.  
  
The retrieval of OAuth tokens has [automated features](/documentation/current/en/manual/config/notifications/media/email/gmail_office#oauth-tokens) for **Gmail** , **Gmail relay** and **Office365** email providers. It is only required to supply _Redirection endpoint_ , _Client ID_ and _Client secret_ parameter values. Zabbix will automatically fill the other required values (see [OAuth URL defaults by provider](/documentation/current/en/manual/config/notifications/media/email/gmail_office#oauth-url-defaults-by-provider)).

##### OAuth access and refresh token retrieval

After submitting OAuth parameters:

  1. A browser popup is opened navigating user to the _Authorization endpoint_.

  2. User authorizes Zabbix in the OAuth service.

  3. The OAuth service redirects user to the Zabbix frontend action `oauth.authorize` with the authorization code and scope value.

  4. In response, Zabbix will make a request to _Token endpoint_ to exchange the authorization code for access and refresh tokens.

#### Testing

To test whether a configured email media type works correctly:

  1. Locate the relevant email in the [list](/documentation/current/en/manual/config/notifications/media#overview) of media types.
  2. Click on _Test_ in the last column of the list (a testing window will open).
  3. Enter a _Send to_ recipient address, message body and, optionally, subject.
  4. Click on _Test_ to send a test message.

Test success or failure message will be displayed in the same window:

![](/documentation/current/assets/en/manual/config/notifications/media/test_email0.png)

#### User media

Once the email media type is configured, go to the _Users > Users_ section and edit user profile to assign email media to the user. Steps for setting up user media, being common for all media types, are described on the [Media types](/documentation/current/en/manual/config/notifications/media#user-media) page.