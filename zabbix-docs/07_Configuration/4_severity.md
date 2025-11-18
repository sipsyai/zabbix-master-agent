---
title: Trigger severity
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/severity
downloaded: 2025-11-14 10:35:35
---

# 4 Trigger severity

Trigger severity represents the level of importance of a trigger.

![](/documentation/current/assets/en/manual/config/triggers/trigger_severities.png)

Zabbix supports the following default trigger severities.

Not classified | Gray | Can be used where the severity level of an event is unknown, has not been determined, is not part of the regular monitoring scope, etc., for example, during initial configuration, as a placeholder for future assessment, or as part of an integration process.  
---|---|---  
Information | Light blue | Can be used for informational events that do not require immediate attention, but can still provide valuable insights.  
Warning | Yellow | Can be used to indicate a potential issue that might require investigation or action, but that is not critical.  
Average | Orange | Can be used to indicate a significant issue that should be addressed relatively soon to prevent further problems.  
High | Light red | Can be used to indicate critical issues that need immediate attention to avoid significant disruptions.  
Disaster | Red | Can be used to indicate a severe incident that requires immediate action to prevent, for example, system outages or data loss.  
  
Trigger severity names and colors can be [customized](/documentation/current/en/manual/config/triggers/customseverities).

Trigger severities are used for:

  * visual representation of triggers - different colors for different severities;
  * audio in global alarms - different audio for different severities;
  * user media - different media (notification channel) for different severities (for example, SMS for triggers of _High_ and _Disaster_ severity, and Email for triggers of other severities);
  * limiting actions by conditions against trigger severities.