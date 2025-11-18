---
title: Trigger dependencies
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/dependencies
downloaded: 2025-11-14 10:35:34
---

# 3 Trigger dependencies

### Overview

Sometimes the availability of one host depends on another. A server that is behind a router will become unreachable if the router goes down. With triggers configured for both, you might get notifications about two hosts down - while only the router was the guilty party.

This is where some dependency between hosts might be useful. With dependency set, notifications of the dependents could be withheld and only the notification on the root problem sent.

While Zabbix does not support dependencies between hosts directly, they may be defined with another, more flexible method - trigger dependencies. A trigger may have one or more triggers it depends on.

So in our simple example we open the server trigger configuration form and set that it depends on the respective trigger of the router. With such dependency, the server trigger will not change its state as long as the trigger it depends on is in the 'PROBLEM' state - and thus no dependent actions will be taken and no notifications sent.

If both the server and the router are down and dependency is there, Zabbix will not execute actions for the dependent trigger.

While the parent trigger is in the PROBLEM state, its dependents may report values that cannot be trusted. Therefore dependent triggers will not be re-evaluated until the parent trigger (the router in the example above):

  * goes back from 'PROBLEM' to 'OK' state;
  * changes its state from 'PROBLEM' to 'UNKNOWN';
  * is closed manually, by correlation or with the help of [date and time](/documentation/current/en/manual/appendix/functions/time) and/or [nodata()](/documentation/current/en/manual/appendix/functions/history#nodata) functions;
  * is resolved by a value of an item not involved in the dependent trigger;
  * is disabled, has a disabled item or a disabled item host

In all of the cases mentioned above, the dependent trigger (server) will be re-evaluated only when a new metric for it is received. This means that the dependent trigger may not be updated immediately.

Also:

  * Trigger dependency may be added from any host trigger to any other host trigger, as long as it doesn't result in a circular dependency.
  * Trigger dependency may be added from one template to another. If some trigger from template A depends on some trigger from template B, template A may only be linked to a host (or another template) together with template B, but template B may be linked to a host (or another template) alone.
  * Trigger dependency may be added from a template trigger to a host trigger. In this case, linking such a template to a host will create a host trigger that depends on the same trigger template that the trigger was depending on. This allows to, for example, have a template where some triggers depend on the router (host) triggers. All hosts linked to this template will depend on that specific router.
  * Trigger dependency may not be added from a host trigger to a template trigger.
  * Trigger dependency may be added from a trigger prototype to another trigger prototype (within the same low-level discovery rule) or a real trigger. A trigger prototype may not depend on a trigger prototype from a different LLD rule or on a trigger created from trigger prototype. A host trigger prototype cannot depend on a trigger from a template.

### Configuration

To define a dependency, open the Dependencies tab in the trigger [configuration form](trigger#configuration). Click on _Add_ in the 'Dependencies' block and select one or more triggers that the trigger will depend on.

![](/documentation/current/assets/en/manual/config/triggers/dependency.png)

Click _Update_. Now the trigger has the indication of its dependency in the list.

![](/documentation/current/assets/en/manual/config/triggers/dependency_list.png)

##### Example of several dependencies

For example, the Host is behind the Router2 and the Router2 is behind the Router1.
    
    
    Zabbix - Router1 - Router2 - Host

Copy

✔ Copied

If the Router1 is down, then obviously the Host and the Router2 are also unreachable, yet receiving three notifications about the Host, the Router1 and the Router2 all being down is excessive.

So in this case we define two dependencies:
    
    
    the 'Host is down' trigger depends on the 'Router2 is down' trigger
           the 'Router2 is down' trigger depends on the 'Router1 is down' trigger

Copy

✔ Copied

Before changing the status of the 'Host is down' trigger, Zabbix will check for the corresponding trigger dependencies. If such are found and one of those triggers is in the 'Problem' state, then the trigger status will not be changed, the actions will not be executed and no notifications will be sent.

Zabbix performs this check recursively. If the Router1 or the Router2 is unreachable, the Host trigger won't be updated.