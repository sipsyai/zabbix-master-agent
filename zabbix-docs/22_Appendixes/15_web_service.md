---
title: Setting up scheduled reports
source: https://www.zabbix.com/documentation/current/en/manual/appendix/install/web_service
downloaded: 2025-11-14 10:46:42
---

# 15 Setting up scheduled reports

#### Overview

This section provides instructions on installing Zabbix web service and configuring Zabbix to enable generation of [scheduled reports](/documentation/current/en/manual/config/reports).

#### Installation

A new [Zabbix web service](/documentation/current/en/manual/concepts/web_service) process and [Google Chrome browser](/documentation/current/en/manual/installation/requirements#web-service) should be installed to enable generation of scheduled reports. The web service may be installed on the same machine where the Zabbix server is installed or on a different machine. Google Chrome browser should be installed on the same machine, where the web service is installed.

The official zabbix-web-service package is available in the [Zabbix repository](http://repo.zabbix.com/). Google Chrome browser is not included into these packages and has to be installed separately.

To compile Zabbix web service from sources, see [Installing Zabbix web service](/documentation/current/en/manual/installation/install#installing-zabbix-web-service).

After the installation, run zabbix_web_service on the machine, where the web service is installed:
    
    
    zabbix_web_service

Copy

✔ Copied

#### Configuration

To ensure proper communication between all elements involved make sure server configuration file and frontend configuration parameters are properly configured.

##### Zabbix server

The following parameters in Zabbix server configuration file need to be updated: _WebServiceURL_ and _StartReportWriters_.

**WebServiceURL**

This parameter is required to enable communication with the web service. The URL should be in the format `http[s]://host:port/report`.

  * By default, the web service listens on port 10053. A different port can be specified in the web service [configuration file](/documentation/current/en/manual/appendix/config/zabbix_web_service).
  * Specifying the `/report` path is mandatory (the path is hardcoded and cannot be changed).

Example:
    
    
    WebServiceURL=http://localhost:10053/report

Copy

✔ Copied

It is strongly recommended to set up encryption between Zabbix server and Zabbix web service [using certificates](/documentation/current/en/manual/encryption/using_certificates). By default, data transmitted between Zabbix server and Zabbix web service is not encrypted, which can lead to unauthorized access.

**StartReportWriters**

This parameter determines how many report writer processes should be started. If it is not set or equals 0, report generation is disabled. Based on the number and frequency of reports required, it is possible to enable from 1 to 100 report writer processes.

Example:
    
    
    StartReportWriters=3

Copy

✔ Copied

##### Zabbix frontend

A _Frontend URL_ parameter should be set to enable communication between Zabbix frontend and Zabbix web service:

  * Proceed to the _Administration → General → Other parameters_ frontend menu section
  * Specify the full URL of the Zabbix web interface in the _Frontend URL_ parameter

![frontend_url.png](/documentation/current/assets/en/manual/appendix/install/frontend_url.png)

Once the setup procedure is completed, you may want to configure and send a [test report](/documentation/current/en/manual/config/reports#testing) to make sure everything works correctly.