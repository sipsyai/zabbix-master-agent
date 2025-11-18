---
title: Action log
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/action_log
downloaded: 2025-11-14 10:38:52
---

# 6 Action log

#### Overview

In the _Reports → Action log_ section users can view details of operations (notifications, remote commands) executed within an action.

![](/documentation/current/assets/en/manual/web_interface/action_log2.png)

Displayed data:

_Time_ | Timestamp of the operation.  
---|---  
_Action_ | Name of the action causing operations.  
_Media type_ | Media type (e.g. Email, Jira, etc.) used for sending a notification.  
For operations that executed remote commands, this column will be empty.  
_Recipient_ | Information about the notification recipient - username, name and surname (in parentheses), and additional information depending on the media type (email, username, etc.).  
For operations that executed remote commands, this column will be empty.  
_Message_ | The content of the message, remote command or global script name.  
A remote command is separated from the target host with a colon symbol: `<host>:<command>`. For example, if the remote command was executed on Zabbix server, then the information will have the following format: `Zabbix server:<command>`.  
_Status_ | Operation status:  
_In progress_ \- operation for sending a notification is in progress (the remaining number of times the server will try to send the notification is also displayed)  
_Sent_ \- notification has been sent  
 _Executed_ \- remote command has been executed  
 _Failed_ \- operation has not been completed  
_Info_ | Error information (if any) regarding the operation execution.  
  
#### Buttons

The button at the upper-right corner of the page offers the following option:

![](/documentation/current/assets/en/manual/web_interface/button_csv.png) | Export action log records from all pages to a CSV file. If a filter is applied, only the filtered records will be exported.  
In the exported CSV file the columns "Recipient" and "Message" are divided into several columns - "Recipient's Zabbix username", "Recipient's name", "Recipient's surname", "Recipient", and "Subject", "Message", "Command".  
---|---  
  
#### Using filter

The filter is located below the _Action log_ bar. It can be opened and collapsed by clicking on the _Filter_ tab at the upper-right corner of the page.

![](/documentation/current/assets/en/manual/web_interface/action_log_filter.png)

You may use the filter to narrow down the records by notification recipients, actions, media types, status, or by the message/remote command content (_Search string_). For better search performance, data is searched with macros unresolved.

#### Time period selector

The [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) allows to select often required periods with one mouse click. The _Time period_ selector can be expanded and collapsed by clicking the _Time period_ tab next to the filter.