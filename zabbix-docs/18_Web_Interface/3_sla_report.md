---
title: SLA report
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/services/sla_report
downloaded: 2025-11-14 10:38:44
---

# 3 SLA report  
  
### Overview

This section allows to view [SLA](/documentation/current/en/manual/it_services/sla) reports, based on the criteria selected in the filter.

SLA reports can also be displayed as a [dashboard widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/sla_report).

### Report

The filter allows to select the report based on the SLA name as well as the service name. It is also possible to limit the displayed period.

![](/documentation/current/assets/en/manual/web_interface/sla_report.png)

Each column (period) displays the SLI for that period. SLIs that are in breach of the set SLO are highlighted in red.

20 periods are displayed in the report. A maximum of 100 periods can be displayed, if both the _From_ date and _To_ date are specified.

### Report details

If you click on the service name in the report, you can access another report that displays a more detailed view.

![](/documentation/current/assets/en/manual/web_interface/sla_report_details.png)

Note that [negative problem duration](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems#negative-problem-duration) does not affect SLA calculation or reporting.