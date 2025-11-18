---
title: Link indicators
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/maps/links
downloaded: 2025-11-14 10:35:55
---

# 3 Link indicators

#### Overview

You can assign indicators to a [link](/documentation/current/en/manual/config/visualization/maps/map#linking-elements) between elements in a network map.

The indicators can be based on triggers or item values. It's possible to display different link style and color:

  * when triggers go into a problem state;
  * when item value: 
    * reaches a threshold (for numeric items);
    * matches a regular expression (for text items).

When you configure a link, you set the default link type and color. By assigning indicators to a link, it becomes possible to make the link style and color depend on trigger status or item value.

For example, should any of the assigned triggers go into a problem state, the link style and color will change to reflect that. So maybe your default link was a green line. Now, with the trigger in the problem state, your link may become bold red (if you have defined it so).

Similarly, if an item value reaches a specified threshold or matches a specified regular expression, the link style may reflect that.

#### Configuration

##### Triggers

To assign triggers as link indicators, do the following:

  * select a map element
  * click on _Edit_ in the _Links_ section for the appropriate link
  * select _Trigger_ as the indicator type
  * click on _Add_ in the _Indicators_ block and select one or more triggers

![](/documentation/current/assets/en/manual/config/visualization/map_triggers.png)

All mandatory input fields are marked with a red asterisk.

Added triggers can be seen in the _Indicators_ list.

You can set the link type and color for each indicator directly from the list. When done, click on _Apply_ , close the form and click on _Update_ to save the map changes.

In _Monitoring → Maps_ the respective link type and color will be displayed if the **trigger** goes into a problem state.

![](/documentation/current/assets/en/manual/config/visualization/map_problem.png)

If multiple triggers go into a problem state, the problem with the highest severity will determine the link style and color. If multiple triggers with the same severity are assigned to the same map link, the one with the lowest ID takes precedence. Note also that:  
  
1\. _Minimum trigger severity_ and _Show suppressed problem_ settings from map configuration affect which problems are taken into account.  
2\. In the case of triggers with multiple problems (multiple problem generation), each problem may have a severity that differs from trigger severity (changed manually), may have different tags (due to macros), and may be suppressed.

##### Item values

To assign item values as link indicators, do the following:

  * select a map element
  * click on _Edit_ in the _Links_ section for the appropriate link
  * select _Item value_ as the indicator type
  * select the item
  * add one or more item value thresholds or patterns in the _Indicators_ block

![](/documentation/current/assets/en/manual/config/visualization/map_item_thresholds.png)

Added item thresholds/patterns can be seen in the _Indicators_ list.

You can set the link type and color for each indicator directly from the list. When done, click on _Apply_ , close the form and click on _Update_ to save the map changes.

In _Monitoring → Maps_ the respective link type and color will be displayed if the **item value** reaches the set threshold (for numeric data types) or matches the regular expression pattern (for text data types).

![](/documentation/current/assets/en/manual/config/visualization/map_item_value.png)