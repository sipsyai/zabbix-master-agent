---
title: Queue
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/queue
downloaded: 2025-11-14 10:39:32
---

# 7 Queue

#### Overview

In the _Administration → Queue_ section items that are waiting to be updated are displayed.

Ideally, when you open this section it should all be "green" meaning no items in the queue. If all items are updated without delay, there are none waiting. However, due to lacking server performance, some items may get delayed and the information is displayed in this section. For more details, see the [Queue](/documentation/current/en/manual/config/items/queue) section.

The Zabbix proxy is not aware of maintenance periods; see [Calculation of queues during maintenance](/documentation/current/en/manual/maintenance#calculation-of-queues-during-maintenance) for details.

The queue is available only if Zabbix server is running. Items are not counted in the queue if the item interface becomes unavailable due to connection problems or agent not working properly.

The _Administration → Queue_ section contains the following pages:

  * Queue overview — displays queue by item type;
  * Queue overview by proxy — displays queue by proxy;
  * Queue details — displays a list of delayed items.

The list of available pages appears upon pressing on _Queue_ in the _Administration_ menu section. It is also possible to switch between pages by using a title dropdown in the upper-left corner.

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/queue_menu.png) | ![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/queue_selector.png)  
---|---  
Third-level menu. | Title dropdown.  
  
##### Overview by item type

In this screen it is easy to locate if the problem is related to one or several item types.

![](/documentation/current/assets/en/manual/web_interface/queue.png)

Each line contains an item type. Each column shows the number of waiting items - waiting for 5-10 seconds/10-30 seconds/30-60 seconds/1-5 minutes/5-10 minutes or over 10 minutes respectively.

##### Overview by proxy

In this screen it is easy to locate if the problem is related to one of the proxies or the server.

![](/documentation/current/assets/en/manual/web_interface/queue_proxy.png)

Each line contains a proxy, with the server last in the list. Each column shows the number of waiting items - waiting for 5-10 seconds/10-30 seconds/30-60 seconds/1-5 minutes/5-10 minutes or over 10 minutes respectively.

##### List of waiting items

In this screen, each waiting item is listed.

![](/documentation/current/assets/en/manual/web_interface/queue_details.png)

Displayed data:

_Scheduled check_ | The time when the check was due is displayed.  
---|---  
_Delayed by_ | The length of the delay is displayed.  
_Host_ | Host of the item is displayed.  
_Name_ | Name of the waiting item is displayed.  
_Proxy_ | The proxy name is displayed, if the host is monitored by proxy.  
  
##### Possible error messages

You may encounter a situation when no data is displayed and the following error message appears:

![](/documentation/current/assets/en/manual/web_interface/error_message_1.png)

Error message in this case is the following:
    
    
    Cannot display item queue. Permission denied

Copy

✔ Copied

This happens when the PHP configuration parameters in the _zabbix.conf.php_ file - `$ZBX_SERVER` or both `$ZBX_SERVER` and `$ZBX_SERVER_PORT` \- point to an existing Zabbix server that uses a different database.