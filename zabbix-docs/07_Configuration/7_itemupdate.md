---
title: Mass update
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemupdate
downloaded: 2025-11-14 10:35:25
---

# 7 Mass update

#### Overview

Sometimes you may want to change some attribute for a number of items at once. Instead of opening each individual item for editing, you may use the mass update function for that.

#### Using mass update

To mass-update some items, do the following:

  * Mark the checkboxes of the items to update in the list
  * Click on _Mass update_ below the list
  * Navigate to the tab with required attributes (_Item_ , _Tags_ or _Preprocessing_)
  * Mark the checkboxes of the attributes to update
  * Enter new values for the attributes

![](/documentation/current/assets/en/manual/config/items/item_mass.png)

![](/documentation/current/assets/en/manual/config/items/item_mass_b.png)

The _Tags_ option allows to:

  * _Add_ \- add specified tags to the items (tags with the same name, but different values are not considered 'duplicates' and can be added to the same item).
  * _Replace_ \- remove the specified tags and add tags with new values
  * _Remove_ \- remove specified tags from the items

User macros, {INVENTORY.*} macros, {HOST.HOST}, {HOST.NAME}, {HOST.CONN}, {HOST.DNS}, {HOST.IP}, {HOST.PORT} and {HOST.ID} macros are supported in tags.

![](/documentation/current/assets/en/manual/config/items/item_mass_c.png)

Mark the checkbox next to _Preprocessing steps_ to activate mass update for preprocessing steps.

The _Preprocessing_ mass update allows to:

  * _Replace_ \- replace the existing preprocessing steps on the items with the preprocessing steps specified below
  * _Remove all_ \- remove all preprocessing steps from the items

When done, click on _Update_.