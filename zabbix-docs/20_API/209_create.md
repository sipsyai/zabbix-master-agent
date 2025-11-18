---
title: mediatype.create
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/mediatype/create
downloaded: 2025-11-14 10:43:23
---

# mediatype.create  
  
### Description

`object mediatype.create(object/array mediaTypes)`

This method allows to create new media types.

This method is only available to _Super admin_ user type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object/array)` Media types to create.

Additionally to the [standard media type properties](object#media-type), the method accepts the following parameters.

message_templates | array | [Message templates](object#message-template) to be created for the media type.  
---|---|---  
  
### Return values

`(object)` Returns an object containing the IDs of the created media types under the `mediatypeids` property. The order of the returned IDs matches the order of the passed media types.

### Examples

#### Creating an email media type

Create a new email media type with a custom SMTP port and message templates.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mediatype.create",
               "params": {
                   "type": "0",
                   "name": "Email",
                   "smtp_server": "mail.example.com",
                   "smtp_helo": "example.com",
                   "smtp_email": "zabbix@example.com",
                   "smtp_port": "587",
                   "message_format": "1",
                   "message_templates": [
                       {
                           "eventsource": "0",
                           "recovery": "0",
                           "subject": "Problem: {EVENT.NAME}",
                           "message": "Problem \"{EVENT.NAME}\" on host \"{HOST.NAME}\" started at {EVENT.TIME}."
                       },
                       {
                           "eventsource": "0",
                           "recovery": "1",
                           "subject": "Resolved in {EVENT.DURATION}: {EVENT.NAME}",
                           "message": "Problem \"{EVENT.NAME}\" on host \"{HOST.NAME}\" has been resolved at {EVENT.RECOVERY.TIME} on {EVENT.RECOVERY.DATE}."
                       },
                       {
                           "eventsource": "0",
                           "recovery": "2",
                           "subject": "Updated problem in {EVENT.AGE}: {EVENT.NAME}",
                           "message": "{USER.FULLNAME} {EVENT.UPDATE.ACTION} problem \"{EVENT.NAME}\" on host \"{HOST.NAME}\" at {EVENT.UPDATE.DATE} {EVENT.UPDATE.TIME}."
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mediatypeids": [
                       "7"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a script media type

Create a new script media type with a custom value for the number of attempts and the interval between them.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mediatype.create",
               "params": {
                   "type": "1",
                   "name": "Push notifications",
                   "exec_path": "push-notification.sh",
                   "maxattempts": "5",
                   "attempt_interval": "11s",
                   "parameters": [
                       {
                           "sortorder": "0",
                           "value": "{ALERT.SENDTO}"
                       },
                       {
                           "sortorder": "1",
                           "value": "{ALERT.SUBJECT}"
                       },
                       {
                           "sortorder": "2",
                           "value": "{ALERT.MESSAGE}"
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mediatypeids": [
                       "8"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

#### Creating a webhook media type

Create a new webhook media type.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "mediatype.create",
               "params": {
                   "type": "4",
                   "name": "Webhook",
                   "script": "var Webhook = {\r\n    token: null,\r\n    to: null,\r\n    subject: null,\r\n    message: null,\r\n\r\n    sendMessage: function() {\r\n        // some logic\r\n    }\r\n}",
                   "parameters": [
                       {
                           "name": "Message",
                           "value": "{ALERT.MESSAGE}"
                       },
                       {
                           "name": "Subject",
                           "value": "{ALERT.SUBJECT}"
                       },
                       {
                           "name": "To",
                           "value": "{ALERT.SENDTO}"
                       },
                       {
                           "name": "Token",
                           "value": "<Token>"
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "mediatypeids": [
                       "9"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CMediaType::create() in _ui/include/classes/api/services/CMediaType.php_.