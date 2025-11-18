---
title: Automated Gmail/Office365 media types
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/email/gmail_office
downloaded: 2025-11-14 10:36:12
---

# 1 Automated Gmail/Office365 media types

#### Overview

Gmail or Office365 users may benefit from automated features in media type configuration.

#### Configuration

The _Email provider_ field in the email media type configuration allows to select pre-configured options for Gmail and Office 365.

When selecting the Gmail/Office365 related options, it is only required to supply the sender email address/password to create a working media type.

![](/documentation/current/assets/en/manual/config/notifications/media_type_gmail.png)

As soon as the email address/password is supplied, Zabbix will be able to automatically fill all required settings for Gmail/Office365 media types with the actual/recommended values, i.e., _SMTP server_ , _SMTP server port_ , _SMTP helo_ , and _Connection security_. Because of this automation, these fields are not even shown, however, it is possible to see the SMTP server and email details in the media type list (see the _Details_ column).

Note also that:

  * The password is not required for the relay options.
  * For Office365 relay, the domain name of the provided email address will be used to dynamically fill the SMTP server (i.e., replace "example.com" in `example-com.mail.protection.outlook.com` with the real value).

#### OAuth tokens

The retrieval of [OAuth tokens](/documentation/current/en/manual/config/notifications/media/email#oauth-tokens) has automated features for _Gmail_ , _Gmail relay_ and _Office365_ email providers.

![](/documentation/current/assets/en/manual/config/notifications/media/media_email_oauth2.png)

It is only necessary to supply a limited set of parameters for OAuth access and refresh token retrieval - _Redirection endpoint_ , _Client ID_ and _Client secret_. Zabbix will automatically fill the other required values (see OAuth URL defaults by provider).

Note that it is also possible to use the [Generic SMTP](/documentation/current/en/manual/config/notifications/media/email#oauth-tokens) form for setting up OAuth authorization for these providers.

SmtpClientAuthentication must be enabled either per user/shared mailbox or per whole tenant in Office365 (not enabled by default settings).

#### OAuth URL defaults by provider

The following table lists default OAuth URL values and parameters per provider that are used by Zabbix.

_Authorization endpoint_ | `https://accounts.google.com/o/oauth2/v2/auth` | `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` | No default  
---|---|---|---  
| _scope_ | `https://mail.google.com` | `https://outlook.office.com/SMTP.Send, offline_access` | No default  
_access_type_ | `offline` | Not used | No default  
_prompt_ | `consent` | Not used | No default  
_redirect_uri_ | Value of _Redirection endpoint_ field is added by code automatically. Not listed in _Authorization endpoint_ parameters.  
_state_ | Unique hash to identify media being updated with OAuth token is added by code automatically. Not listed in _Authorization endpoint_ parameters.  
_Token endpoint_ | `https://oauth2.googleapis.com/token` | `https://login.microsoftonline.com/common/oauth2/v2.0/token` | No default  
| _grant_type_ | `authorization_code` | `authorization_code` | No default  
_redirect_uri_ | Value of _Redirection endpoint_ field is added by code automatically. Not listed in _Token endpoint_ parameters.  
_state_ | Unique hash to identify media being updated with OAuth token is added by code automatically. Not listed in _Token endpoint_ parameters.  
  
#### Office365 workaround for personal accounts

Office365 personal accounts do not support query strings in the redirect URL.

To work around this issues the Apache web server administrator can add the following rewrite rule to the `.htaccess` file:
    
    
    RewriteEngine On
           RewriteRule ^/oauth\.authorize$ /zabbix.php?action=oauth.authorize [QSA,L,PT]

Copy

✔ Copied

This enables the use of a simplified redirect URL like:
    
    
    http://server-name/zabbix/oauth.authorize

Copy

✔ Copied

instead of a URL with query parameters, ensuring compatibility with Office365 personal accounts.