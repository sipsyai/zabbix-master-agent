---
title: URL
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/url
downloaded: 2025-11-14 10:38:29
---

# 31 URL  
  
#### Overview

This widget displays the content retrieved from the specified URL.

#### Configuration

To configure, select _URL_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/dashboards/widgets/url.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_URL_ | Enter the URL to display (up to 2048 characters).  
External URLs must start with `http://` or `https://`.  
Internal URLs support relative paths (for example, `zabbix.php?action=report.status`).  
{HOST.*} macros are supported.  
---|---  
_Override host_ | Select a compatible widget or the dashboard as the [data source](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/#dynamic-parameters) for hosts.  
This parameter is not available when configuring the widget on a [template dashboard](/documentation/current/en/manual/config/templates/template#adding-dashboards).  
  
Browsers might not load an HTTP page configured in the widget if Zabbix frontend is accessed over HTTPS.