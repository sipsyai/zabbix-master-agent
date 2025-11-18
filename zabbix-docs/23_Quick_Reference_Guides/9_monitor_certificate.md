---
title: Monitor website certificates with Zabbix agent 2 (passive)
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_certificate
downloaded: 2025-11-14 10:48:11
---

# 9 Monitor website certificates with Zabbix agent 2 (passive)

#### Introduction

This guide provides a comprehensive overview of how to set up and monitor SSL/TLS certificates using the `web.certificate.get` key in Zabbix agent 2. It is designed to simplify certificate monitoring for single or multiple websites, ensuring administrators can quickly identify potential issues such as expired or invalid certificates.

**Who this guide is for**

This guide is designed for new Zabbix users and contains the minimum set of steps required to enable basic monitoring of website certificates. If you are looking for deep customization options or require more advanced configuration, see [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this guide, you need to [download and install](https://www.zabbix.com/download) Zabbix server, Zabbix frontend, and Zabbix agent 2 according to the instructions for your OS. This tutorial assumes that both the Zabbix server and agent are installed on the same machine; therefore, `127.0.0.1` is used in the configuration.

#### Configure Zabbix agent 2

1\. Open the Zabbix agent configuration file (default path: `/etc/zabbix/zabbix_agent2.conf`):
    
    
    sudo vi /etc/zabbix/zabbix_agent2.conf

Copy

✔ Copied

2\. Set the Server parameter to 127.0.0.1, since the agent and server are running on the same machine:
    
    
    Server=127.0.0.1

Copy

✔ Copied

3\. Save the file and restart the Zabbix agent 2 service:
    
    
    sudo systemctl restart zabbix-agent2

Copy

✔ Copied

4\. After setup and configuring Zabbix agent 2, test its availability with:
    
    
    zabbix_get -s 127.0.0.1 -k web.certificate.get[<website_DNS_name>]

Copy

✔ Copied

Zabbix agent 2 includes the WebCertificate plugin by default, so no separate installation or configuration is required.

#### Configure Zabbix frontend

1\. Log into Zabbix frontend.

2\. Navigate to _Monitoring > Hosts_.

3\. Click on an existing host where you want to monitor website certificates, or [create a host](/documentation/current/en/manual/config/hosts/host) if necessary:

  * In the _Host name_ field, enter a host name (e.g., "Certificate Monitoring").
  * In the _Templates_ field, type or select the template "Website certificate by Zabbix agent 2" that will be [linked](/documentation/current/en/manual/config/templates/linking) to the host.
  * In the _Host groups_ field, type or select a host group (e.g., "SSL/TLS Monitoring").
  * In the _Interfaces_ field, add an interface of type "Agent" and specify an IP address. For this example, "127.0.0.1" is used.

![](/documentation/current/assets/en/manual/guides/certificate_host.png)

  * In the _Macros_ tab, switch to _Inherited and host macros_ , look for the following macros and click on _Change_ next to the macro value to update it: 
    * `{$CERT.WEBSITE.HOSTNAME}` \- enter the desired website DNS name as the value.

![](/documentation/current/assets/en/manual/guides/certificate_macros.png)

4\. Click on _Add_ to add the host.

To monitor multiple websites, you can specify a comma-separated list of their hostnames in the `{$CERT.WEBSITE.HOSTNAME}` macro. Optionally, you can also provide a comma-separated list of ports in the `{$CERT.WEBSITE.PORT}` macro, where each port corresponds to the respective hostname in order. For example to monitor example.com and example.org on port 8443:

  * `{$CERT.WEBSITE.HOSTNAME}`: example.com,example.org
  * `{$CERT.WEBSITE.PORT}`: 443,8443

For each website specified in the `{$CERT.WEBSITE.HOSTNAME}` macro, Zabbix will create a corresponding set of items and triggers. This allows individual monitoring and alerting for each website's SSL certificate.

![](/documentation/current/assets/en/manual/guides/certificate_multiple_websites.png)

#### View collected metrics

Congratulations! At this point, Zabbix is already monitoring desired web certificate.

To view collected metrics, navigate to the [_Monitoring > Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/hosts) menu section and click on [_Latest data_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data) next to the host to view all the latest collected metrics in a list, like expiration date, issuer, and subject.

![](/documentation/current/assets/en/manual/guides/certificate_latestdata.png)

#### Set up problem alerts

Zabbix can notify you about infrastructure issues. This guide provides basic configuration steps for sending email alerts.

1\. Navigate to [_User settings > Profile_](/documentation/current/en/manual/web_interface/user_profile), switch to the _Media_ tab and [add your email](/documentation/current/en/manual/quickstart/login#adding-user).

![](/documentation/current/assets/en/manual/quickstart/new_media.png)

2\. Follow the guide for [Receiving a problem notification](/documentation/current/en/manual/quickstart/notification).

Next time, when Zabbix detects a problem, you should receive an alert via email.

#### Test your configuration

To test your configuration, we can simulate a real problem by updating the host configuration in Zabbix frontend.

1\. Open your "Certificate Monitoring" host configuration in Zabbix.

2\. Switch to the _Macros_ tab and select _Inherited and host macros_.

3\. Click on _Change_ next to the previously configured `{$CERT.EXPIRY.WARN}` macro value and set a very high number of days (greater than 365 days should be sufficient) to receive a warning before the certificate expires.

4\. Click on _Update_ to update the host configuration.

5\. In a few moments, Zabbix will detect the problem "SSL certificate expires soon", with the number of days until expiration. The problem will appear in [_Monitoring > Problems_](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems).

![](/documentation/current/assets/en/manual/guides/certificate_problem.png)

If alerts are configured, you will also receive the problem notification.

6\. Change the macro value back to its previous value to resolve the problem and continue monitoring the certificate values.

#### See also

  * [Zabbix agent 2](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2) \- lists item keys.
  * Template [_Website certificate by Zabbix agent 2_](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/certificate_agent2?at=refs%2Fheads%2Frelease%2F7.4) \- additional information about the _Website certificate by Zabbix agent 2_ template.
  * Template [_Website certificate by Zabbix agent 2 active_](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/certificate_agent2_active?at=refs%2Fheads%2Frelease%2F7.4) \- additional information about the _Website certificate by Zabbix agent 2 active_ template.
  * [Monitor websites with Browser items](/documentation/current/en/manual/guides/monitor_browser) \- how to start basic monitoring of websites with Browser items.