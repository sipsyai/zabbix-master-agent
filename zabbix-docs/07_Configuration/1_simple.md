---
title: Simple graphs
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/graphs/simple
downloaded: 2025-11-14 10:35:48
---

# 1 Simple graphs

#### Overview

Simple graphs are provided for the visualization of data gathered by items.

No configuration effort is required on the user part to view simple graphs. They are freely made available by Zabbix.

Just go to _Monitoring > Latest data_ and click on the Graph link for the respective item and a graph will be displayed.

![](/documentation/current/assets/en/manual/config/simple_graph.png)

Simple graphs are provided for all numeric items. For textual items, a link to History is available in _Monitoring > Latest data_.

#### Time period selector

The _Time period_ selector above the graph allows to select often required periods with one mouse click. For more information, see [_Time period selector_](/documentation/current/en/manual/web_interface/time_period_selector).

#### Recent data vs longer periods

For very recent data a **single** line is drawn connecting each received value. The single line is drawn as long as there is at least one horizontal pixel available for one value.

For data that show a longer period **three lines** are drawn - a dark green one shows the average, while a light pink and a light green line shows the maximum and minimum values at that point in time. The space between the highs and the lows is filled with yellow background.

Working time (working days) is displayed in graphs as a white background, while non-working time is displayed in gray (with the _Original blue_ default frontend theme).

![](/documentation/current/assets/en/manual/config/graph_working_time.png)

Working time is always displayed in simple graphs, whereas displaying it in [custom graphs](custom#configuring-custom-graphs) is a user preference.

Working time is not displayed if the graph shows more than 3 months.

##### Trigger lines

[Simple triggers](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph#displaying-options) are displayed as lines with black dashes over trigger severity color - take note of the blue line on the graph and the trigger information displayed in the legend. Up to 3 trigger lines can be displayed on the graph; if there are more triggers then the triggers with lower severity are prioritized. Triggers are always displayed in simple graphs, whereas displaying them in [custom graphs](custom#configuring-custom-graphs) is a user preference.

![simple_graph_trigger.png](/documentation/current/assets/en/manual/config/simple_graph_trigger.png)

##### Generating from history/trends

Graphs can be drawn based on either item [history or trends](/documentation/current/en/manual/config/items/history_and_trends).

For the users who have frontend [debug mode](/documentation/current/en/manual/web_interface/debug_mode) activated, a gray, vertical caption is displayed at the lower-right of a graph indicating where the data come from.

Several factors influence whether history of trends is used:

  * longevity of item history. For example, item history can be kept for 14 days. In that case, any data older than the fourteen days will be coming from trends.
  * data congestion in the graph. If the amount of seconds to display in a horizontal graph pixel exceeds 3600/16, trend data are displayed (even if item history is still available for the same period).
  * if trends are disabled, item history is used for graph building - if available for that period.

#### Absence of data

For items with a regular update interval, nothing is displayed in the graph if item data are not collected.

However, for trapper items and items with a scheduled update interval (and regular update interval set to 0), a straight line is drawn leading up to the first collected value and from the last collected value to the end of graph; the line is on the level of the first/last value respectively.

#### Switching to raw values

A dropdown on the upper right allows to switch from the simple graph to the _Values/500 latest values_ listings. This can be useful for viewing the numeric values making up the graph.

The values represented here are raw, i.e. no units or postprocessing of values is used. Value mapping, however, is applied.

#### Known issues

See [known issues](/documentation/current/en/manual/installation/known_issues#graphs) for graphs.