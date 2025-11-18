---
title: Ad-hoc graphs
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/graphs/adhoc
downloaded: 2025-11-14 10:35:50
---

# 3 Ad-hoc graphs

#### Overview

While a [simple graph](simple) is great for accessing data of one item and [custom graphs](custom) offer customization options, none of the two allow to quickly create a comparison graph for multiple items with little effort and no maintenance.

To address this issue, it is possible to create ad-hoc graphs for several items in a very quick way.

#### Configuration

To create an ad-hoc graph, do the following:

  * Go to _Monitoring_ → _Latest data_
  * Use filter to display items that you want
  * Mark checkboxes of the items you want to graph
  * Click on _Display stacked graph_ or _Display graph_ buttons

![](/documentation/current/assets/en/manual/config/visualization/ad_hoc_graphs.png)

Your graph is created instantly:

![](/documentation/current/assets/en/manual/config/visualization/ad_hoc_graph.png)

Note that to avoid displaying too many lines in the graph, only the average value for each item is displayed (min/max value lines are not displayed). Triggers and trigger information is not displayed in the graph.

In the created graph window you have the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) available and the possibility to switch from the "normal" line graph to a stacked one (and back).

![](/documentation/current/assets/en/manual/config/visualization/ad_hoc_stacked.png)