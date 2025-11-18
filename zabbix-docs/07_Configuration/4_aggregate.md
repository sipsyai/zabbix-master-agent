---
title: Aggregation in graphs
source: https://www.zabbix.com/documentation/current/en/manual/config/visualization/graphs/aggregate
downloaded: 2025-11-14 10:35:51
---

# 4 Aggregation in graphs

#### Overview

Aggregation functions, available in the graph and pie chart widgets of the dashboard, allow displaying an aggregated value for the chosen interval (5 minutes, an hour, a day), instead of all values.

This section provides more detail on aggregation options in the graph widget.

The aggregation options are as follows:

  * min
  * max
  * avg
  * count
  * sum
  * first (first value displayed)
  * last (last value displayed)

The most exciting use of data aggregation is the possibility to create nice side-by-side comparisons of data for some period:

![](/documentation/current/assets/en/manual/config/visualization/aggregate_graph.png)

When hovering over a point in time in the graph, date and time is displayed in addition to items and their aggregated values. Items are displayed in parentheses, prefixed by the aggregation function used. If the graph widget has a [_Data set label_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph#data-set) configured, the label is displayed in parentheses, prefixed by the aggregation function used. Note that this is the date and time of the point in the graph, not of the actual values.

#### Configuration

The options for aggregation are available in data set settings when configuring a [graph widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph).

![](/documentation/current/assets/en/manual/config/visualization/aggregate_graph_options.png)

You may pick the aggregation function and the time interval. As the data set may comprise several items, there is also another option allowing to show aggregated data for each item separately or for all data set items as one aggregated value.

#### Use cases

##### Average request count to Nginx server

View the average request count per second per day to the Nginx server:

  * add the request count per second item to the data set
  * select the aggregate function `avg` and specify interval `1d`
  * a bar graph is displayed, where each bar represents the average number of requests per second per day

##### Minimum weekly disk space among clusters

View the lowest disk space among clusters over a week.

  * add to the data set: hosts `cluster*`, key "Free disk space on /data"
  * select the aggregate function `min` and specify interval `1w`
  * a bar graph is displayed, where each bar represents the minimum disk space per week for each /data volume of the cluster