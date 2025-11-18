---
title: New item
source: https://www.zabbix.com/documentation/current/en/manual/quickstart/item
downloaded: 2025-11-14 10:34:28
---

# 3 New item

#### Overview

In this section, you will learn how to set up an item.

Items are the basis of gathering data in Zabbix. Without items, there is no data - because only an item defines a single metric or what kind of data to collect from a host.

#### Adding item

All items are grouped around hosts. That is why to configure a sample item we go to _Data collection > Hosts_ and find the "New host" we have created.

Click on the _Items_ link in the row of "New host", and then click on _Create item_. This will present us with an item definition form.

![](/documentation/current/assets/en/manual/quickstart/new_item.png)

All mandatory input fields are marked with a red asterisk.

For our sample item, the essential information to enter is:

**_Name_**

  * Enter _CPU load_ as the value. This will be the item name displayed in lists and elsewhere.

**_Key_**

  * Manually enter _system.cpu.load_ as the value. This is the technical name of an item that identifies the type of information that will be gathered. The particular key is just one of [pre-defined keys](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) that come with Zabbix agent.

**_Type of information_**

  * This attribute defines the format of the expected data. For the _system.cpu.load_ key, this field will be automatically set to _Numeric (float)_.

You may also want to reduce the number of days [item history](/documentation/current/en/manual/config/items/history_and_trends) will be kept, to 7 or 14. This is good practice to relieve the database from keeping lots of historical values.

[Other options](/documentation/current/en/manual/config/items/item#configuration) will suit us with their defaults for now.

When done, click _Add_. The new item should appear in the item list, and you should see a success message.

![](/documentation/current/assets/en/manual/quickstart/item_created.png)

#### Viewing data

With an item defined, you might be curious if it is actually gathering data. For that, go to _Monitoring > Latest data_, select 'New host' in the filter and click on _Apply_.

![](/documentation/current/assets/en/manual/quickstart/latest_data.png)

With that said, it may take up to 60 seconds for the first data to arrive. That, by default, is how often the server reads configuration changes and picks up new items to execute.

If you see no value in the 'Change' column, maybe only one value has been received so far. Wait 30 seconds for another value to arrive.

If you do not see information about the item as in the screenshot, make sure that:

  * you have filled out the item 'Key' and 'Type of information' fields exactly as in the screenshot;
  * both the agent and the server are running;
  * host status is 'Monitored' and its availability icon is green;
  * the host selected in the host filter is correct;
  * the item is enabled.

##### Graphs

With the item working for a while, it might be time to see something visual. [Simple graphs](/documentation/current/en/manual/config/visualization/graphs/simple) are available for any monitored numeric item without any additional configuration. These graphs are generated on runtime.

To view the graph, go to _Monitoring > Latest data_ and click on the 'Graph' link next to the item.

![](/documentation/current/assets/en/manual/quickstart/simple_graph.png)