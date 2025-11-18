---
title: History and trends
source: https://www.zabbix.com/documentation/current/en/manual/config/items/history_and_trends
downloaded: 2025-11-14 10:35:21
---

# 4 History and trends

#### Overview

History and trends are the two ways of storing collected data in Zabbix.

Whereas history keeps each collected value, trends keep averaged information on hourly basis and therefore are less resource-hungry.

#### Keeping history

You can set for how many days history will be kept:

  * in the item properties [form](/documentation/current/en/manual/config/items/item)
  * when mass-updating items
  * when [setting up](/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping) housekeeper tasks

Any older data will be removed by the housekeeper.

The general strong advice is to keep history for the smallest possible number of days and that way not to overload the database with lots of historical values.

Instead of keeping a long history, you can keep longer data of trends. For example, you could keep history for 14 days and trends for 5 years.

You can get a good idea of how much space is required by history versus trends data by referring to the [database sizing page](/documentation/current/en/manual/installation/requirements#database-size).

While keeping shorter history, you will still be able to review older data in graphs, as graphs will use trend values for displaying older data.

If history is set to '0', the item will update only dependent items and inventory. No trigger functions will be evaluated because trigger evaluation is based on history data only.

As an alternative way to preserve history consider to use [history export](/documentation/current/en/manual/extensions/loadablemodules#providing-history-export-callbacks) functionality of loadable modules.

#### Keeping trends

Trends is a built-in historical data reduction mechanism which stores minimum, maximum, average and the total number of values per every hour for numeric data types.

You can set for how many days trends will be kept:

  * in the item properties [form](/documentation/current/en/manual/config/items/item)
  * when mass-updating items
  * when setting up Housekeeper tasks

Trends usually can be kept for much longer than history. Any older data will be removed by the housekeeper.

Zabbix server accumulates trend data in runtime in the trend cache, as the data flows in. Server flushes **previous hour** trends of every item into the database (where frontend can find them) in these situations:

  * server receives the first current hour value of the item
  * 5 or less minutes of the current hour left and still no current hour values of the item
  * server stops

To see trends on a graph you need to wait at least to the beginning of the next hour (if item is updated frequently) and at most to the end of the next hour (if item is updated rarely), which is 2 hours maximum.

When server flushes trend cache and there are already trends in the database for this hour (for example, server has been restarted mid-hour), server needs to use update statements instead of simple inserts. Therefore on a bigger installation if restart is needed it is desirable to stop server in the end of one hour and start in the beginning of the next hour to avoid trend data overlap.

History tables do not participate in trend generation in any way.

If trends are set to '0', Zabbix server does not calculate or store trends at all.

The trends are calculated and stored with the same data type as the original values. As a result the average value calculations of unsigned data type values are rounded and the less the value interval is the less precise the result will be. For example if item has values 0 and 1, the average value will be 0, not 0.5.

Also restarting server might result in the precision loss of unsigned data type average value calculations for the current hour.