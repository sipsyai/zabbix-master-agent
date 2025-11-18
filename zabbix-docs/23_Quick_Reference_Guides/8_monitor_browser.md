---
title: Monitor websites with Browser items
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_browser
downloaded: 2025-11-14 10:48:10
---

# 8 Monitor websites with Browser items

#### Introduction

This page walks you through the steps required to start basic monitoring of websites with Browser items.

**Who this guide is for**

This guide is designed for new Zabbix users and contains the minimum set of steps required to enable basic monitoring of websites with Browser items. If you are looking for deep customization options or require more advanced configuration, see the [Browser items](/documentation/current/en/manual/config/items/itemtypes/browser) page or the [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this guide, you need to [download and install](https://www.zabbix.com/download) Zabbix server and Zabbix frontend according to the instructions for your OS.

This guide is based on the following setup:

  * Zabbix version: 7.2 PRE-RELEASE (installed from packages)
  * OS distribution: Ubuntu
  * OS version: 22.04 (Jammy)
  * Zabbix components: Server, Frontend, Agent
  * Database: MySQL
  * Web server: Apache

#### Configure WebDriver

Browser items require an automation framework (either Selenium Server or a plain WebDriver, for example, ChromeDriver) as a web testing endpoint that controls and interacts with a browser, executing test commands such as clicking buttons or entering text. As an example, this guide will use Selenium Server with Chrome in a Docker container.

It is assumed that Docker is already configured. This guide does not cover the configuration of Docker. For installation instructions, see [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

1\. Launch Selenium Server with Chrome in a Docker container with the following options:

  * **docker run --name browser** \- runs a new Docker container named "browser";
  * **-p 4444:4444** \- maps port 4444 on your host machine to port 4444 on the container (this is the port used by Selenium Server to accept commands);
  * **-p 7900:7900** \- maps port 7900 on your host machine to port 7900 on the container (this is the port used by the Virtual Network Computing (VNC) server, allowing you to view the browser GUI remotely; requires a VNC client);
  * **\--shm-size="2g"** \- allocates 2GB of shared memory to the container (this is important for Chrome to run properly, as it can require a significant amount of shared memory to avoid crashes);
  * **-d** \- runs the container in detached mode, meaning it will run in the background;
  * **selenium/standalone-chrome:latest** \- specifies the Docker image to use; in this case, the latest version of [Selenium Server with Chrome](https://hub.docker.com/r/selenium/standalone-chrome).

    
    
    docker run --name browser \
           -p 4444:4444 \
           -p 7900:7900 \
           --shm-size="2g" \
           -d selenium/standalone-chrome:latest

Copy

✔ Copied

2\. Ensure that the `browser` Docker container is running and accessible.

  * Retrieve the IP address of the container (in this example, 192.0.2.1):

    
    
    ip addr
           
           # 1: lo: <LOOPBACK,UP,LOWER_UP>
           #    ...
           # 3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> ...
           #    inet 192.0.2.1/16 brd 192.0.255.255 scope global docker0
           #    ...

Copy

✔ Copied

  * Test the connection to the container with [Ncat](https://nmap.org/ncat/):

    
    
    nc -zv 192.0.2.1 4444
           
           # Connection to 192.0.2.1 4444 port [tcp/*] succeeded!

Copy

✔ Copied

  * Retrieve the webpage content from Selenium Server with [curl](https://curl.se/):

    
    
    curl -L 192.0.2.1:4444
           
           # <!DOCTYPE html>
           # <html lang="en">
           # 
           # <head>
           #   <meta charset="utf-8"/>
           #   <link href="favicon.svg" rel="icon" type="image/svg">
           #   <meta content="width=device-width, initial-scale=1" name="viewport"/>
           #   <link href="logo192.png" rel="apple-touch-icon"/>
           #   <link href="manifest.json" rel="manifest"/>
           #   <title>Selenium Grid</title>
           # </head>
           # 
           # <body>
           # ...

Copy

✔ Copied

For troubleshooting, refer to [Docker documentation](https://docs.docker.com/engine/).

#### Configure Zabbix server

Browser items are executed and processed by _browser poller_ Zabbix processes that need to be enabled by adjusting the [StartBrowserPollers](/documentation/current/en/manual/appendix/config/zabbix_server#startbrowserpollers) server configuration parameter. Additionally, the [WebDriverURL](/documentation/current/en/manual/appendix/config/zabbix_server#webdriverurl) parameter should specify the previously configured web testing endpoint.

By default, the StartBrowserPollers parameter is set to 1, therefore you only need to specify the web testing endpoint.

1\. Open the Zabbix server configuration file.
    
    
    vi /etc/zabbix/zabbix_server.conf

Copy

✔ Copied

2\. Locate and set the [WebDriverURL](/documentation/current/en/manual/appendix/config/zabbix_server#webdriverurl) parameter in Zabbix server configuration file:
    
    
    ### Option: WebDriverURL
           #   WebDriver interface HTTP[S] URL. For example http://localhost:4444 used with Selenium WebDriver standalone server.
           #
           # Mandatory: no
           # Default:
           # WebDriverURL=
           
           WebDriverURL=192.0.2.1:4444

Copy

✔ Copied

3\. Restart Zabbix server.
    
    
    systemctl restart zabbix-server

Copy

✔ Copied

#### Configure Zabbix frontend

1\. Log into Zabbix frontend.

2\. [Create a host](/documentation/current/en/manual/config/hosts/host) in Zabbix web interface:

  * In the _Host name_ field, enter a host name (for example, "git.zabbix.com").
  * In the _Templates_ field, type or select the "Website by Browser" template. For more information on this template, see [Website by Browser](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/website_browser?at=refs%2Fheads%2Frelease%2F7.4).
  * In the _Host groups_ field, type or select a host group (for example, a new host group "Websites").

![](/documentation/current/assets/en/manual/guides/browser_host.png)

  * In the _Macros_ tab, switch to _Inherited and host macros_ , look for the following macros and click on _Change_ next to the macro value to update it: 
    * {$WEBSITE.DOMAIN} - Domain name (for example, git.zabbix.com/projects/ZBX/repos/zabbix/browse)
    * {$WEBSITE.GET.DATA.INTERVAL} - Item data update interval (for example, 15m)

![](/documentation/current/assets/en/manual/guides/browser_macros.png)

3\. Click the _Add_ button to create the host. This host will represent the website you want to monitor.

#### View collected metrics

Congratulations! At this point, Zabbix is already monitoring the website you specified.

To view collected metrics, navigate to the [_Monitoring → Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) menu section and click on _Dashboards_ next to the host.

![](/documentation/current/assets/en/manual/guides/browser_monitored_hosts.png)

This action will take you to the host dashboard (configured on the template level) with the most important metrics collected from the website.

![](/documentation/current/assets/en/manual/guides/browser_dashboard.png)

#### Set up problem alerts

Zabbix can notify you about a problem with your infrastructure using a variety of methods. This guide provides basic configuration steps for sending email alerts.

1\. Navigate to [_User settings → Profile_](/documentation/current/en/manual/web_interface/user_profile), switch to the _Media_ tab and [add your email](/documentation/current/en/manual/quickstart/login#adding-user).

![](/documentation/current/assets/en/manual/quickstart/new_media.png)

2\. Follow the guide for [Receiving a problem notification](/documentation/current/en/manual/quickstart/notification).

Next time, when Zabbix detects a problem, you should receive an alert via email.

#### Test your configuration

To test your configuration, we can simulate a real problem by updating the host configuration in Zabbix frontend.

1\. Open your website host configuration in Zabbix.

2\. Switch to the _Macros_ tab and select _Inherited and host macros_.

3\. Click on _Change_ next to, for example, the previously configured {$WEBSITE.DOMAIN} macro value and set an incorrect domain name (for example, /git.zabbix.com/projects/ZBX/repos/zabbix/browse).

4\. Click on _Update_ to update the host configuration.

5\. In a few moments, Zabbix will detect the problem "Failed to get JSON of the requested website", because it will not be able to connect to the specified website. The problem will appear in [_Monitoring → Problems_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems).

![](/documentation/current/assets/en/manual/guides/browser_problem.png)

If alerts are configured, you will also receive the problem notification.

6\. Change the macro value back to its previous value to resolve the problem and continue monitoring the website.

#### See also

  * [Creating an item](/documentation/current/en/manual/config/items/item) \- how to start monitoring additional metrics.
  * [Problem escalations](/documentation/current/en/manual/config/notifications/action/escalations) \- how to create multi-step alert scenarios (e.g., first send message to the system administrator, then, if a problem is not resolved in 45 minutes, send message to the data center manager).
  * [Browser items](/documentation/current/en/manual/config/items/itemtypes/browser) \- how to configure Browser items.
  * Template [Website by Browser](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/website_browser?at=refs%2Fheads%2Frelease%2F7.4) \- additional information about the _Website by Browser_ template.