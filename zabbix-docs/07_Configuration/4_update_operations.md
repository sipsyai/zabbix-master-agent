---
title: Update operations
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/action/update_operations
downloaded: 2025-11-14 10:36:26
---

# 4 Update operations  
  
#### Overview

Update operations are available in actions with the following event sources:

  * _Triggers_ \- when problems are [updated](/documentation/current/en/manual/acknowledgment#updating-problems) by other users, i.e. commented upon, acknowledged, severity has been changed, closed (manually);
  * _Services_ \- when the severity of a service has changed but the service is still not recovered.

Please note that users do not receive notifications about their own updates.

Both messages and remote commands are supported in update operations. While several operations can be added, escalation is not supported - all operations are assigned to a single step and therefore will be performed simultaneously.

#### Configuring an update operation

To configure an update operation go to the _Operations_ tab in action [configuration](/documentation/current/en/manual/config/notifications/action).

![](/documentation/current/assets/en/manual/config/notifications/action_operation.png)

To configure details of a new update operation, click on ![](/documentation/current/assets/en/manual/config/add_link.png) in the _Update operations_ block. To edit an existing operation, click on ![](/documentation/current/assets/en/manual/config/edit_link.png) next to the operation. A pop-up window will open where you can edit the operation step details.

#### Update operation details

![](/documentation/current/assets/en/manual/config/update_operation_details.png)

Update operations offer the same set of parameters as [Recovery operations](/documentation/current/en/manual/config/notifications/action/recovery_operations#Recovery-operation-details).