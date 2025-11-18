---
title: Alert object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/alert/object
downloaded: 2025-11-14 10:40:03
---

# Alert object

The following objects are directly related to the `alert` API.

### Alert

Alerts are created by Zabbix server and cannot be modified via the API.

The alert object contains information about whether certain action operations have been executed successfully. It has the following properties.

alertid | ID | ID of the alert.  
---|---|---  
actionid | ID | ID of the action that generated the alert.  
alerttype | integer | Alert type.  
  
Possible values:  
0 - message;  
1 - remote command.  
clock | timestamp | Time when the alert was generated.  
error | string | Error text if there are problems sending a message or running a command.  
esc_step | integer | Action escalation step during which the alert was generated.  
eventid | ID | ID of the event that triggered the action.  
mediatypeid | ID | ID of the media type that was used to send the message.  
message | text | Message text.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `alerttype` is set to "message"  
retries | integer | Number of times Zabbix tried to send the message.  
sendto | string | Address, user name or other identifier of the recipient.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `alerttype` is set to "message"  
status | integer | Status indicating whether the action operation has been executed successfully.  
  
Possible values if `alerttype` is set to "message":  
0 - message not sent;  
1 - message sent;  
2 - failed after a number of retries;  
3 - new alert is not yet processed by alert manager.  
  
Possible values if `alerttype` is set to "remote command":  
0 - command not run;  
1 - command run;  
2 - tried to run the command on Zabbix agent, but it was unavailable.  
subject | string | Message subject.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _supported_ if `alerttype` is set to "message"  
userid | ID | ID of the user that the message was sent to.  
p_eventid | ID | ID of problem event, which generated the alert.  
acknowledgeid | ID | ID of acknowledgment, which generated the alert.