---
title: Web server
source: https://www.zabbix.com/documentation/current/en/manual/best_practices/security/web_server
downloaded: 2025-11-14 10:39:52
---

# 3 Web server

#### Overview

This section contains best practices for setting up the web server in a secure way.

#### Enabling Zabbix on root directory of URL

On RHEL-based systems, add a virtual host to Apache configuration (`/etc/httpd/conf/httpd.conf`) and set a permanent redirect for document root to Zabbix SSL URL. Note that `example.com` should be replaced with the actual name of the server.
    
    
    # Add lines:
           
           <VirtualHost *:*>
               ServerName example.com
               Redirect permanent / https://example.com
           </VirtualHost>

Copy

✔ Copied

Restart the Apache service to apply the changes:
    
    
    systemctl restart httpd.service

Copy

✔ Copied

#### Enabling HTTP Strict Transport Security (HSTS) on the web server

To protect Zabbix frontend against protocol downgrade attacks, we recommend enabling the [HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) policy on the web server.

To enable the HSTS policy for your Zabbix frontend in Apache configuration, follow these steps:

1\. Locate your virtual host's configuration file:

  * `/etc/httpd/conf/httpd.conf` on RHEL-based systems
  * `/etc/apache2/sites-available/000-default.conf` on Debian/Ubuntu

2\. Add the following directive to your virtual host's configuration file:
    
    
    <VirtualHost *:*>
               Header set Strict-Transport-Security "max-age=31536000"
           </VirtualHost>

Copy

✔ Copied

3\. Restart the Apache service to apply the changes:
    
    
    # On RHEL-based systems:
           systemctl restart httpd.service
           
           # On Debian/Ubuntu
           systemctl restart apache2.service

Copy

✔ Copied

#### Enforcing Secure and SameSite session cookies in Zabbix

When configuring Zabbix, it is essential to enforce secure and SameSite attributes for session cookies to enhance security and prevent cross-site request forgery (CSRF) attacks. However, enforcing `SameSite=Strict` may cause issues in certain scenarios, such as:

  * Dashboard URL widgets displaying "user not logged in" when embedding same-domain iframes.
  * Users accessing the dashboard via HTTP instead of HTTPS may face login issues.
  * Inability to share URLs to specific Zabbix menu sections or hosts.

To mitigate these issues, users should have a way to adjust the SameSite policy.

1\. Secure cookies

Setting the `secure` flag ensures that cookies are only transmitted over HTTPS, preventing exposure over unencrypted connections.

To enable secure cookies in Zabbix, add or modify the following setting in the web server configuration:

For Apache:
    
    
    Header always edit Set-Cookie ^(.*)$ $1;Secure

Copy

✔ Copied

For Nginx:
    
    
    proxy_cookie_path / "/; Secure";

Copy

✔ Copied

Ensure that your Zabbix frontend is accessed via HTTPS; otherwise, cookies with the `Secure` flag will not be sent.

2\. Configuring the SameSite attribute

Web server settings can also enforce the SameSite attribute:

For Apache:
    
    
    <IfModule mod_headers.c>
               Header onsuccess edit Set-Cookie (.*) "$1; SameSite=Strict"
           </IfModule>

Copy

✔ Copied

For Nginx (version 1.19.3+):
    
    
    proxy_cookie_flags ~ samesite=Strict; # Replace ~ with 'zbx_session' for specificity

Copy

✔ Copied

#### Enabling Content Security Policy (CSP) on the web server

To protect Zabbix frontend against Cross Site Scripting (XSS), data injection, and similar attacks, we recommend enabling Content Security Policy on the web server. To do so, configure the web server to return the [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy).

The following CSP header configuration is only for the default Zabbix frontend installation and for cases when all content originates from the site's domain (excluding subdomains). A different CSP header configuration may be required if you are, for example, configuring the [_URL_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/url) widget to display content from the site's subdomains or external domains, switching from _OpenStreetMap_ to another map engine, or adding external CSS or widgets. If you're using the Duo Universal Prompt [multi-factor authentication](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication/mfa) method, make sure to add "duo.com" to the CSP directive in your virtual host's configuration file.

To enable CSP for your Zabbix frontend in Apache configuration, follow these steps:

1\. Locate your virtual host's configuration file:

  * `/etc/httpd/conf/httpd.conf` on RHEL-based systems
  * `/etc/apache2/sites-available/000-default.conf` on Debian/Ubuntu

2\. Add the following directive to your virtual host's configuration file:
    
    
    <VirtualHost *:*>
               Header set Content-Security-Policy: "default-src 'self' *.openstreetmap.org; script-src 'self' 'unsafe-inline' 'unsafe-eval'; connect-src 'self'; img-src 'self' data: *.openstreetmap.org; style-src 'self' 'unsafe-inline'; base-uri 'self'; form-action 'self';"
           </VirtualHost>

Copy

✔ Copied

3\. Restart the Apache service to apply the changes:
    
    
    # On RHEL-based systems:
           systemctl restart httpd.service
           
           # On Debian/Ubuntu
           systemctl restart apache2.service

Copy

✔ Copied

#### Disabling web server information exposure

To improve security, disabling all web server signatures is recommended.

By default, the web server is exposing the software signature:

![](/documentation/current/assets/en/manual/installation/requirements/software_signature.png)

The signature can be disabled by adding the following parameters to the Apache configuration file:
    
    
    ServerSignature Off
           ServerTokens Prod

Copy

✔ Copied

PHP signature (X-Powered-By HTTP header) can be disabled by changing the `php.ini` configuration file (by default, the signature is disabled):
    
    
    expose_php = Off

Copy

✔ Copied

Web server restart is required for configuration file changes to be applied.

For additional security, you can use the _mod_security_ tool with Apache (package _libapache2-mod-security2_). This tool allows removing the server signature instead of removing only the version from the server signature. The server signature can be changed to any value by setting "SecServerSignature" to any desired value after installing _mod_security_.

Please refer to the documentation of your web server to find help on how to remove/change software signatures.

#### Disabling web server default error pages

To avoid information exposure, disabling the default error pages is recommended.

By default, a web server uses built-in error pages:

![](/documentation/current/assets/en/manual/installation/requirements/error_page_text.png)

These default error pages should be replaced/removed. For example, the "ErrorDocument" directive can be used to define a custom error page/text for the Apache web server.

Please refer to the documentation of your web server to find help on how to replace/remove default error pages.

#### Removing web server test page

To avoid information exposure, removing the web server test page is recommended.

By default, the Apache web server webroot contains the `index.html` test page:

![](/documentation/current/assets/en/manual/installation/requirements/test_page.png)

Please refer to the documentation of your web server to find help on how to remove default test pages.

#### Set X-Frame-Options HTTP response header

By default, Zabbix is configured with the _Use X-Frame-Options HTTP header_ parameter set to `SAMEORIGIN`. This means that content can only be loaded in a frame that has the same origin as the page itself.

Zabbix frontend elements that pull content from external URLs (namely, the URL [dashboard widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/url)) display retrieved content in a sandbox with all sandboxing restrictions enabled.

These settings enhance the security of the Zabbix frontend and provide protection against XSS and clickjacking attacks. _Super admin_ users can [modify](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#security) the _Use iframe sandboxing_ and _Use X-Frame-Options HTTP header_ parameters as needed. Please carefully weigh the risks and benefits before changing default settings. Turning iframe sandboxing or X-Frame-Options HTTP header off completely is not recommended.

#### Hiding the file with list of common passwords

To increase the complexity of password brute force attacks, limiting access to the `ui/data/top_passwords.txt` file is recommended. This file contains a list of the most common and context-specific passwords and prevents users from setting such passwords (if the _Avoid easy-to-guess passwords_ parameter is enabled in the [password policy](/documentation/current/en/manual/web_interface/frontend_sections/users/authentication#internal-authentication)).

To limit access to the `top_passwords.txt` file, modify your web server configuration.

On Apache, file access can be limited using the `.htaccess` file:
    
    
    <Files "top_passwords.txt">
               Order Allow,Deny
               Deny from all
           </Files>

Copy

✔ Copied

On NGINX, file access can be limited using the `location` directive:
    
    
    location = /data/top_passwords.txt {
               deny all;
               return 404;
           }

Copy

✔ Copied