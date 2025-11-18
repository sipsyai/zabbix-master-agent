---
title: Web interface installation
source: https://www.zabbix.com/documentation/current/en/manual/installation/frontend
downloaded: 2025-11-14 10:34:12
---

# 6 Web interface installation

This section provides step-by-step instructions for installing Zabbix web interface. Zabbix frontend is written in PHP, so to run it a PHP supported webserver is needed.

You can find out more about setting up SSL for Zabbix frontend by referring to these [best practices](/documentation/current/en/manual/best_practices/security/cryptography#setting-up-ssl-for-zabbix-frontend).

#### Welcome screen

Open Zabbix frontend URL in the browser. If you have installed Zabbix from packages, the URL is:

  * for Apache: _http:// <server_ip_or_name>/zabbix_
  * for Nginx: _http:// <server_ip_or_name>_

You should see the first screen of the frontend installation wizard.

Use the _Default language_ drop-down menu to change system default language and continue the installation process in the selected language (optional). For more information, see [Installation of additional frontend languages](/documentation/current/en/manual/appendix/install/locales).

Note that setting the language to _English (en_US)_ will also enable the US time/date format in the frontend.

![](/documentation/current/assets/en/manual/installation/install_1.png)

#### Check of pre-requisites

Make sure that all Zabbix frontend mandatory pre-requisites are met.

![](/documentation/current/assets/en/manual/installation/install_2.png)

_PHP version_ | 8.0.0 |   
---|---|---  
_PHP option "memory_limit"_ | 128MB | In php.ini: memory_limit = 128M  
_PHP option "post_max_size"_ | 16MB | In php.ini: post_max_size = 16M  
_PHP option "upload_max_filesize"_ | 2MB | In php.ini: upload_max_filesize = 2M  
_PHP option "max_execution_time"_ | 300 seconds | In php.ini: max_execution_time = 300 (values 0 and -1 are also allowed)  
_PHP option "max_input_time"_ | 300 seconds | In php.ini: max_input_time = 300 (values 0 and -1 are also allowed)  
_PHP databases support_ | One of: MySQL, PostgreSQL | See [Requirements](/documentation/current/en/manual/installation/requirements#frontend) for the list of all mandatory and optional PHP extensions. Note that failed optional pre-requisites are displayed with a red _Warning_ status, and the setup process can proceed even if they are not met.  
_PHP bcmath_ | must be enabled  
_PHP mbstring_ | must be enabled  
_PHP option "mbstring.func_overload"_ | must be disabled | In php.ini: mbstring.func_overload = 0  
_PHP option "session.auto_start"_ | must be disabled | In php.ini: session.auto_start = 0  
_PHP option "arg_separator.output"_ | & | In php.ini: arg_separator.output = "&" (value "&amp;" is also allowed)  
  
If the Apache user or user group needs to be changed, verify the permissions to the session folder; otherwise, Zabbix setup may be unable to continue.

#### Configure DB connection

Enter details for connecting to the database. Zabbix database must already be created.

![](/documentation/current/assets/en/manual/installation/install_3a.png)

If the _Database TLS encryption_ option is checked, then additional fields for [configuring the TLS connection](/documentation/current/en/manual/appendix/install/db_encrypt) to the database appear in the form (MySQL or PostgreSQL only).

If _Store credentials in_ is set to HashiCorp Vault or CyberArk Vault, additional parameters will become available:

  * for [HashiCorp Vault](/documentation/current/en/manual/config/secrets/hashicorp): Vault API endpoint, vault prefix, secret path, and authentication token;

  * for [CyberArk Vault](/documentation/current/en/manual/config/secrets/cyberark): Vault API endpoint, vault prefix, secret query string, and certificates. Upon marking _Vault certificates_ checkbox, two new fields for specifying paths to SSL certificate file and SSL key file will appear.

![](/documentation/current/assets/en/manual/installation/install_3b.png)

#### Settings

Entering a name for Zabbix server is optional, however, if submitted, it will be displayed in the menu bar and page titles.

Set the default [time zone](/documentation/current/en/manual/web_interface/time_zone#overview) and theme for the frontend.

If the _Encrypt connections from Web interface_ option is checked, then additional fields for [configuring the TLS connection](/documentation/current/en/manual/appendix/install/frontend_encrypt) between Zabbix server and frontend appear in the form.

![](/documentation/current/assets/en/manual/installation/install_4.png)

#### Pre-installation summary

Review a summary of settings.

![](/documentation/current/assets/en/manual/installation/install_5.png)

The subpage will show the data if TLS configuration has been added.

![](/documentation/current/assets/en/manual/installation/tls_configuration.png)

#### Install

If installing Zabbix from sources, download the configuration file and place it under conf/ in the webserver HTML documents subdirectory where you copied Zabbix PHP files to.

![](/documentation/current/assets/en/manual/installation/install_6.png)

![](/documentation/current/assets/en/manual/installation/saving_zabbix_conf.png)

Providing the webserver user has write access to conf/ directory the configuration file would be saved automatically and it would be possible to proceed to the next step right away.

Finish the installation.

![](/documentation/current/assets/en/manual/installation/install_7.png)

#### Log in

Zabbix frontend is ready! The default user name is **Admin** , password **zabbix**.

![](/documentation/current/assets/en/manual/quickstart/login.png)

Proceed to [getting started with Zabbix](/documentation/current/en/manual/quickstart/login).