---
title: API tokens
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens
downloaded: 2025-11-14 10:39:19
---

# 4 API tokens

#### Overview

This section allows to create and manage API tokens.

![](/documentation/current/assets/en/manual/web_interface/api_tokens.png)

You may filter API tokens by name, users to whom the tokens are assigned, expiry date, users that created tokens, or status (enabled/disabled). Click on the token status in the list to quickly enable/disable a token. You may also mass enable/disable tokens by selecting them in the list and then clicking on the _Enable/Disable_ buttons below the list.

To create a new token, press _Create API token_ button at the upper-right corner, then fill out the required fields in the token configuration screen:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/api_token_conf.png)

Name | Token's visible name.  
---|---  
User | User the token should be assigned to. To quickly select a user, start typing the username, first or last name, then select the required user from the auto-complete list. Alternatively, you can press the _Select_ button and select a user from the full user list. A token can be assigned only to one user.  
Description | Optional token description.  
Set expiration date and time | Unmark this checkbox if a token should not have an expiry date.  
Expiry date | Click on the calendar icon to select token expiry date or enter the date manually in a format YYYY-MM-DD hh:mm:ss  
Enabled | Unmark this checkbox if you need to create a token in a disabled state.  
  
Press _Add_ to create a token.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/users/api_token.png)

Copy the _Auth token_ value and save in a safe place **before closing the page** , then press Close. The token will appear in the list.

_Auth token_ value cannot be viewed again later. It is only available immediately after creating a token. If you lose a saved token you will have to regenerate it and doing so will create a new authorization string.

Click on the token name to edit the name, description, expiry date settings, or token status. Note that it is not possible to change to which user the token is assigned. Press _Update_ button to save changes. If a token has been lost or exposed, you may press _Regenerate_ button to generate new token value. A confirmation dialog box will appear, asking you to confirm this operation since after proceeding the previously generated token will become invalid.

Users without access to the _Administration_ menu section can see and modify details of tokens assigned to them in the _User profile → API tokens_ [section](/documentation/current/en/manual/web_interface/user_profile#api-tokens) only if _Manage API tokens_ is allowed in their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) permissions.