---
title: Media types
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/alerts/mediatypes
downloaded: 2025-11-14 10:39:13
---

# 2 Media types

#### Overview

In the _Alerts → Media types_ section users can configure and maintain media type information.

Media type information contains general instructions for using a medium as delivery channel for notifications. Specific details, such as the individual email addresses to send a notification to are kept with individual users.

A listing of existing media types with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/media_types.png)

Displayed data:

_Name_ | Name of the media type. Clicking on the name opens the media type [configuration form](/documentation/current/en/manual/config/notifications/media/email#configuration).  
---|---  
_Type_ | Type of the media (email, SMS, etc) is displayed.  
_Status_ | Media type status is displayed - _Enabled_ or _Disabled_.  
By clicking on the status you can change it.  
_Used in actions_ | Actions where the media type is used are displayed, preceded by the total number of these actions.  
Clicking on the action name opens the action configuration form. If the user has no permissions to the action, the name is not clickable.  
_Details_ | Detailed information of the media type is displayed.  
_Actions_ | The following action is available:  
**Test** \- click to open a testing form where you can enter media type parameters (e.g. a recipient address with test subject and body) and send a test message to verify that the configured media type works. See also: Media type testing for [Email](/documentation/current/en/manual/config/notifications/media/email#media-type-testing), [Webhook](/documentation/current/en/manual/config/notifications/media/webhook#media-type-testing), or [Script](/documentation/current/en/manual/config/notifications/media/script#media-type-testing).  
  
To configure a new media type, click on the _Create media type_ button in the upper-right corner.

To import a media type, click on the _Import_ button in the upper-right corner.

##### Mass editing options

Buttons below the list offer some mass-editing options:

  * _Enable_ \- change the media type status to _Enabled_
  * _Disable_ \- change the media type status to _Disabled_
  * _Export_ \- export the media types to a YAML, XML or JSON file
  * _Delete_ \- delete the media types

To use these options, mark the checkboxes before the respective media types, then click on the required button.

##### Using filter

You can use the filter to display only the media types you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of media types. If you click on it, a filter becomes available where you can filter media types by name and status. Additionally, you can use the filter to display actions in the _Used in actions_ column based on the scope of their media type usage (defined by the _Send to media type_ parameter in action [operation details](/documentation/current/en/manual/config/notifications/action/operation#operation-details)).

![](/documentation/current/assets/en/manual/web_interface/media_types_filter1.png)