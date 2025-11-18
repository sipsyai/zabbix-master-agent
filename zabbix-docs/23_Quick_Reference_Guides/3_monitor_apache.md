---
title: Monitor Apache via HTTP
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_apache
downloaded: 2025-11-14 10:48:05
---

# 3 Monitor Apache via HTTP

## Introduction

This page shows a quick and simple way to start monitoring an Apache web server without installing any additional software.

**Who this guide is for**

This guide is designed for new Zabbix users and contains the minimum set of steps required to enable basic monitoring of your Apache installation. If you are looking for deep customization options or require more advanced configuration, see [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this installation guide, you must [download and install](https://www.zabbix.com/download) Zabbix server and Zabbix frontend according to instructions for your OS.

## Prepare Apache

1\. Check, which Apache version you are using:

On RHEL-based system, run:
    
    
    httpd -v

Copy

✔ Copied

On Debian/Ubuntu, run:
    
    
    apache2 -v

Copy

✔ Copied

2\. Make sure that the [Status module](https://httpd.apache.org/docs/2.4/mod/mod_status.html) is enabled in your Apache instance.

On RHEL-based system, run:
    
    
    httpd -M | grep status
           status_module (shared)

Copy

✔ Copied

On Debian/Ubuntu, run:
    
    
    apache2ctl -M | grep status
           status_module (shared)

Copy

✔ Copied

If you don't see status_module in the list, enable the module by running:

On RHEL-based system, run:
    
    
    LoadModule status_module /usr/lib/apache2/modules/mod_status.so

Copy

✔ Copied

On Debian/Ubuntu, run:
    
    
    sudo /usr/sbin/a2enmod status

Copy

✔ Copied

3\. Edit Apache configuration file to allow access to status reports from Zabbix server IP.

On an RHEL-based system: `/etc/httpd/conf.modules.d/status.conf`:
    
    
    sudo vi /etc/httpd/conf.modules.d/status.conf

Copy

✔ Copied

On Debian/Ubuntu: `/etc/apache2/mods-enabled/status.conf`:
    
    
    sudo vi /etc/apache2/mods-enabled/status.conf

Copy

✔ Copied

Add the following lines to the file (**replace 198.51.100.255** with your Zabbix server IP address):

  * For Apache 2.2:  
<Location /server-status> SetHandler server-status

Order Deny,Allow Deny from all Allow from 198.51.100.255 </Location>

  * For Apache 2.4:  
<Location "/server-status"> SetHandler server-status Require ip 198.51.100.255 </Location>

4\. Restart Apache

On an RHEL-based system, run:
    
    
    sudo systemctl restart httpd

Copy

✔ Copied

On Debian/Ubuntu, run:
    
    
    sudo systemctl restart apache2 

Copy

✔ Copied

5\. To check, if everything is configured correctly, run (**replace 198.51.100.255** with your Zabbix server IP address):
    
    
    curl 198.51.100.255/server-status

Copy

✔ Copied

The response should contain Apache web server statistics.

## Configure Zabbix for monitoring

1\. Log into Zabbix frontend.

2\. [Create a host](/documentation/current/en/manual/config/hosts/host) in Zabbix web interface.

This host will represent your Apache server.

3\. In the _Interfaces_ parameter, add _Agent_ interface and specify your Apache instance IP address. **You don't need to install Zabbix agent on the machine** , the interface will only be used for resolving {HOST.CONN} macro. This macro is used in template items to locate Apache instance.

4\. In the _Templates_ parameter, type or select _Apache by HTTP_.

![](/documentation/current/assets/en/manual/guides/apache_host.png)

5\. Switch to the **Macros** tab and select _Inherited and host macros_ mode. Check that values of the macros {$APACHE.STATUS.PORT} and {$APACHE.STATUS.SCHEME} suit your installation settings. By default, the port is 80 and the scheme is http. Change macro values if you use different port and/or scheme.

![](/documentation/current/assets/en/manual/guides/apache_host_macros.png)

## View collected metrics

Congratulations! At this point, Zabbix is already monitoring your Apache web server.

To view collected metrics, open the _Monitoring- >Hosts_ [menu section](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) and click on the _Dashboards_ next to the host.

![](/documentation/current/assets/en/manual/guides/apache_hosts.png)

This action will take you to the host dashboard with most important metrics collected from Apache /server-status page.

![](/documentation/current/assets/en/manual/guides/apache_dashboard.png)

Alternatively, from the _Monitoring- >Hosts_, you can click on the _Latest data_ to view all the latest collected metrics in a list.

![](/documentation/current/assets/en/manual/guides/apache_latest_data.png)

## Set up problem alerts

Zabbix can notify you about a problem with your infrastructure using a variety of methods. This guide provides configuration steps for sending email alerts.

1\. Go to the _User settings - > Profile_, switch to the tab _Media_ and [add your email](/documentation/current/en/manual/quickstart/login#adding-user).

![](/documentation/current/assets/en/manual/quickstart/new_media.png)

2\. Follow the guide for [Receiving problem notification](/documentation/current/en/manual/quickstart/notification).

Next time, when Zabbix detects a problem you should receive an alert via email.

## Test your configuration

To simulate real problem and receive a test problem alert:

1\. Open the _Apache server_ host configuration in Zabbix.

2\. Switch to the Macros tab and select _Inherited and host macros_.

3\. Press _Change_ next to {$APACHE.STATUS.PORT} macro and set a different port.

4\. Press Update to save host configuration.

5\. In a few minutes, Zabbix will detect the problem _Apache service is down_ , because now it cannot connect to the instance. It will appear in the Monitoring->Problems section.

![](/documentation/current/assets/en/manual/guides/apache_problem.png)

If the alerts are configured, you will also receive the problem notification.

6\. Change the macro value back to resolve the problem and continue monitoring Apache.

**See also:**

  * [Web server hardening](/documentation/current/en/manual/best_practices/security/web_server) \- recommended settings for greater web server security.
  * [Creating an item](/documentation/current/en/manual/config/items/item) \- how to start monitoring additional metrics.
  * [HTTP items](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) \- how to monitor custom metrics using HTTP agent.
  * [Problem escalations](/documentation/current/en/manual/config/notifications/action/escalations) \- how to create multi-step alert scenarios (e.g., first send message to the system administrator, then, if a problem is not resolved in 45 minutes, send message to the data center manager).