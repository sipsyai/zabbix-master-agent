---
title: Mass update
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/update
downloaded: 2025-11-14 10:35:37
---

# 6 Mass update

#### Overview

With mass update you may change some attribute for a number of triggers at once, saving you the need to open each individual trigger for editing.

#### Using mass update

To mass-update some triggers, do the following:

  * Mark the checkboxes of the triggers you want to update in the list
  * Click on _Mass update_ below the list
  * Navigate to the tab with required attributes (_Trigger_ , _Tags_ or _Dependencies_)
  * Mark the checkboxes of any attribute to update

![](/documentation/current/assets/en/manual/config/triggers/trigger_mass.png)

![](/documentation/current/assets/en/manual/config/triggers/trigger_mass_b.png)

The following options are available when selecting the respective button for tag update:

  * _Add_ \- allows to add new tags for the triggers;
  * _Replace_ \- will remove any existing tags from the trigger and replace them with the one(s) specified below;
  * _Remove_ \- will remove specified tags from triggers.

Note that tags with the same name but different values are not considered 'duplicates' and can be added to the same trigger.

![](/documentation/current/assets/en/manual/config/triggers/trigger_mass_c.png)

_Replace dependencies_ \- will remove any existing dependencies from the trigger and replace them with the one(s) specified.

Click on _Update_ to apply the changes.