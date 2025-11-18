---
title: Cookies used by Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/cookies
downloaded: 2025-11-14 10:39:42
---

# 10 Cookies used by Zabbix

#### Overview

This page provides a list of cookies used by Zabbix.

ZBX_SESSION_NAME | Zabbix frontend session data, stored as JSON encoded by base64 |  | Session (expires when the browsing session ends) | + | \+ (only if HTTPS is enabled on a web server)  
---|---|---|---|---|---  
tab | Active tab number; this cookie is only used on pages with multiple tabs (e.g. _Host_ , _Trigger_ or _Action_ configuration page) and is created, when a user navigates from a primary tab to another tab (such as _Tags_ or _Dependencies_ tab).  
  
0 is used for the primary tab. | Example: 1 | Session (expires when the browsing session ends) | - | -  
browserwarning_ignore | Whether a warning about using an outdated browser should be ignored. | yes | Session (expires when the browsing session ends) | - | -  
system-message-ok | A message to show as soon as page is reloaded. | Plain text message | Session (expires when the browsing session ends) or as soon as page is reloaded | + | -  
system-message-error | An error message to show as soon as page is reloaded. | Plain text message | Session (expires when the browsing session ends) or as soon as page is reloaded | + | -  
  
Forcing 'HttpOnly' flag on Zabbix cookies by a webserver directive is not supported.

#### Footnotes

**1** When `HttpOnly` is 'true' the cookie will be made accessible only through the HTTP protocol. This means that the cookie won't be accessible by scripting languages, such as JavaScript. This setting can effectively help to reduce identity theft through XSS attacks (although it is not supported by all browsers).

**2** `Secure` indicates that the cookie should only be transmitted over a secure HTTPS connection from the client. When set to 'true', the cookie will only be set if a secure connection exists.