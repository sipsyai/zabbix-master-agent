---
title: Time period selector
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/time_period_selector
downloaded: 2025-11-14 10:39:45
---

# 13 Time period selector

#### Overview

The _Time period_ selector allows to select often required periods with one mouse click. It can be expanded or collapsed by clicking the _Time period_ tab in the upper-right corner.

![](/documentation/current/assets/en/manual/web_interface/time_period_selector.png)

Options such as _Today_ , _This week_ , etc., display the whole period, including the hours/days in the future. Options such as _Today so far_ , _This week so far_ , etc., display only the hours passed.

Once a period is selected, it can be moved back and forth in time by clicking the ![](/documentation/current/assets/en/manual/config/visualization/arrow_left.png) ![](/documentation/current/assets/en/manual/config/visualization/arrow_right.png) arrow buttons. The _Zoom out_ button allows to zoom out the period by 50% in each direction.

For [graphs](/documentation/current/en/manual/config/visualization/graphs), selecting the displayed time period is also possible by highlighting an area in the graph with the left mouse button. Once you release the left mouse button, the graph will zoom into the highlighted area. Zooming out is also possible by double-clicking in the graph.

The _From/To_ fields display the selected period in either absolute time syntax (in format `Y-m-d H:i:s`) or relative time syntax. A relative time period can contain one or several mathematical operations (- or +), for example, `now-1d` or `now-1d-2h+5m`.

The following relative time abbreviations are supported:

  * `now`
  * `s` (seconds)
  * `m` (minutes)
  * `h` (hours)
  * `d` (days)
  * `w` (weeks)
  * `M` (months)
  * `y` (years)

Precision is supported in the _Time period_ selector (for example, `/M` in `now-1d/M`). Details of precision:

`m` | Y-m-d H:m:00 | Y-m-d H:m:59  
---|---|---  
`h` | Y-m-d H:00:00 | Y-m-d H:59:59  
`d` | Y-m-d 00:00:00 | Y-m-d 23:59:59  
`w` | Monday of the week 00:00:00 | Sunday of the week 23:59:59  
`M` | First day of the month 00:00:00 | Last day of the month 23:59:59  
`y` | 1st of January of the year 00:00:00 | 31st of December of the year 23:59:59  
  
It is also possible to select a time period using the _Date picker_. To open it, click the calendar icon next to the _From/To_ fields.

![](/documentation/current/assets/en/manual/config/date_picker.png)

Within the date picker, you can navigate between year/month/date using `Tab`, `Shift+Tab`, and keyboard arrow buttons. Pressing `Enter` confirms the selection.

#### Examples

`now/d` | `now/d` | 00:00 - 23:59 today  
---|---|---  
`now/d` | `now/d+1d` | 00:00 today - 23:59 tomorrow  
`now/w` | `now/w` | Monday 00:00:00 - Sunday 23:59:59 this week  
`now-1y/w` | `now-1y/w` | The week of Monday 00:00:00 - Sunday 23:59:59 one year ago  
  
Using "now/M+1M" for the _To_ parameter may add 31 days, which can result in the date shifting by 1-3 days depending on the number of days in the month. For example, if used in January, the result may be 02 March instead of the expected 28 February. To avoid this issue, use "now/M-3d+1M/M", which adjusts for month length accurately. Similarly, if configuring _From_ to go backward, use "now/M+3d-1M/M".