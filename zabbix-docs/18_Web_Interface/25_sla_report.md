---
title: SLA report
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/sla_report
downloaded: 2025-11-14 10:38:23
---

# 25 SLA report  
  
#### Overview

This widget is useful for displaying [SLA reports](/documentation/current/en/manual/web_interface/frontend_sections/services/sla_report). Functionally it is similar to the _Services_ -> _SLA report_ section.

#### Configuration

To configure, select _SLA report_ as type:

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/monitoring/sla_report.png)

In addition to the parameters that are [common](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#common-parameters) for all widgets, you may set the following specific options:

_SLA_ | Select the SLA for the report.  
---|---  
_Service_ | Select the service for the report.  
_Show periods_ | Set how many periods will be displayed in the widget (20 by default, 100 maximum).  
_From_ | Select the beginning date for the report.  
[Relative dates](/documentation/current/en/manual/web_interface/time_period_selector) are supported: `now`, `now/d`, `now/w-1w` etc; supported date modifiers: d, w, M, y.  
_To_ | Select the end date for the report.  
[Relative dates](/documentation/current/en/manual/web_interface/time_period_selector) are supported: `now`, `now/d`, `now/w-1w` etc; supported date modifiers: d, w, M, y.