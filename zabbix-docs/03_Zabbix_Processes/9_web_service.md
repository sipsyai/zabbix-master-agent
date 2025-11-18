---
title: Web service
source: https://www.zabbix.com/documentation/current/en/manual/concepts/web_service
downloaded: 2025-11-14 10:33:59
---

# 9 Web service

#### Overview

Zabbix web service is a process that is used for communication with external web services. Currently, Zabbix web service is used for generating and sending [scheduled reports](/documentation/current/en/manual/config/reports) with plans to add additional functionality in the future.

Zabbix server connects to the web service via HTTP(S). Zabbix web service requires [Google Chrome](/documentation/current/en/manual/installation/requirements#web-service) to be installed on the same host; on some distributions the service may also work with Chromium (see [known issues](/documentation/current/en/manual/installation/known_issues#chromium-for-zabbix-web-service-on-ubuntu-20)).

#### Installation

The official zabbix-web-service package is available in the [Zabbix repository](https://repo.zabbix.com/zabbix/).

To compile Zabbix web service [from sources](/documentation/current/en/manual/installation/install#installing-zabbix-web-service), specify the `--enable-webservice` configure option.

To configure Zabbix web service, update the [`zabbix_web_service.conf`](/documentation/current/en/manual/appendix/config/zabbix_web_service) configuration file parameters.

It is strongly recommended to set up encryption between Zabbix server and Zabbix web service [using certificates](/documentation/current/en/manual/encryption/using_certificates). By default, data transmitted between Zabbix server and Zabbix web service is not encrypted, which can lead to unauthorized access.