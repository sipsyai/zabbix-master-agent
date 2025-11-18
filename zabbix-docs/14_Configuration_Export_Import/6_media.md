---
title: Media types
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import/media
downloaded: 2025-11-14 10:37:13
---

# 6 Media types

#### Overview

Media types are [exported](/documentation/current/en/manual/xml_export_import) with all related objects and object relations.

#### Exporting

To export media types, do the following:

  1. Go to _Alerts_ → _Media types_.
  2. Mark the checkboxes of the media types to export.
  3. Click _Export_ below the list.

![](/documentation/current/assets/en/manual/xml_export_import/export_mediatypes.png)

Depending on the selected format, media types are exported to a local file with a default name:

  * `zabbix_export_mediatypes.yaml` \- in YAML export (default option for export);
  * `zabbix_export_mediatypes.xml` \- in XML export;
  * `zabbix_export_mediatypes.json` \- in JSON export.

#### Importing

To import media types, do the following:

  1. Go to _Alerts_ → _Media types_.
  2. Click _Import_ in the upper-right corner.
  3. Select the import file.
  4. Mark the required options in import rules.
  5. Click _Import_ in the lower-right corner of the configuration form.

![](/documentation/current/assets/en/manual/xml_export_import/import_media.png)

Import rules:

_Update existing_ | Existing elements will be updated using data from the import file. Otherwise, they will not be updated.  
---|---  
_Create new_ | New elements will be created using data from the import file. Otherwise, they will not be created.  
  
A success or failure message of the import will be displayed in the frontend.

#### Export format

Export to YAML:
    
    
    zabbix_export:
             version: '7.4'
             media_types:
               - name: Pushover
                 type: WEBHOOK
                 parameters:
                   - name: endpoint
                     value: 'https://api.pushover.net/1/messages.json'
                   - name: eventid
                     value: '{EVENT.ID}'
                   - name: event_nseverity
                     value: '{EVENT.NSEVERITY}'
                   - name: event_source
                     value: '{EVENT.SOURCE}'
                   - name: event_value
                     value: '{EVENT.VALUE}'
                   - name: expire
                     value: '1200'
                   - name: message
                     value: '{ALERT.MESSAGE}'
                   - name: priority_average
                     value: '0'
                   - name: priority_default
                     value: '0'
                   - name: priority_disaster
                     value: '0'
                   - name: priority_high
                     value: '0'
                   - name: priority_information
                     value: '0'
                   - name: priority_not_classified
                     value: '0'
                   - name: priority_warning
                     value: '0'
                   - name: retry
                     value: '60'
                   - name: title
                     value: '{ALERT.SUBJECT}'
                   - name: token
                     value: '<PUSHOVER TOKEN HERE>'
                   - name: triggerid
                     value: '{TRIGGER.ID}'
                   - name: url
                     value: '{$ZABBIX.URL}'
                   - name: url_title
                     value: Zabbix
                   - name: user
                     value: '{ALERT.SENDTO}'
                 status: DISABLED
                 max_sessions: '0'
                 script: |
                   try {
                       var params = JSON.parse(value),
                           request = new HttpRequest(),
                           data,
                           response,
                           severities = [
                               {name: 'not_classified', color: '#97AAB3'},
                               {name: 'information', color: '#7499FF'},
                               {name: 'warning', color: '#FFC859'},
                               {name: 'average', color: '#FFA059'},
                               {name: 'high', color: '#E97659'},
                               {name: 'disaster', color: '#E45959'},
                               {name: 'resolved', color: '#009900'},
                               {name: 'default', color: '#000000'}
                           ],
                           priority;
                   
                       if (typeof params.HTTPProxy === 'string' && params.HTTPProxy.trim() !== '') {
                           request.setProxy(params.HTTPProxy);
                       }
               
                       if ([0, 1, 2, 3].indexOf(parseInt(params.event_source)) === -1) {
                           throw 'Incorrect "event_source" parameter given: "' + params.event_source + '".\nMust be 0-3.';
                       }
                  
                       if (params.event_value !== '0' && params.event_value !== '1'
                           && (params.event_source === '0' || params.event_source === '3')) {
                           throw 'Incorrect "event_value" parameter given: ' + params.event_value + '\nMust be 0 or 1.';
                       }
                 
                       if ([0, 1, 2, 3, 4, 5].indexOf(parseInt(params.event_nseverity)) === -1) {
                           params.event_nseverity = '7';
                       }
                 
                       if (params.event_value === '0') {
                           params.event_nseverity = '6';
                       }
                
                       priority = params['priority_' + severities[params.event_nseverity].name] || params.priority_default;
                 
                       if (isNaN(priority) || priority < -2 || priority > 2) {
                           throw '"priority" should be -2..2';
                       }
                 
                       if (params.event_source === '0' && isNaN(params.triggerid)) {
                           throw 'field "triggerid" is not a number';
                       }
                 
                       if (isNaN(params.eventid)) {
                           throw 'field "eventid" is not a number';
                       }
                 
                       if (typeof params.message !== 'string' || params.message.trim() === '') {
                           throw 'field "message" cannot be empty';
                       }
                   
                       data = {
                           token: params.token,
                           user: params.user,
                           title: params.title,
                           message: params.message,
                           url: (params.event_source === '0') 
                               ? params.url + '/tr_events.php?triggerid=' + params.triggerid + '&eventid=' + params.eventid
                               : params.url,
                           url_title: params.url_title,
                           priority: priority
                       };
                   
                       if (priority == 2) {
                           if (isNaN(params.retry) || params.retry < 30) {
                               throw 'field "retry" should be a number with value of at least 30 if "priority" is set to 2';
                           }
                  
                           if (isNaN(params.expire) || params.expire > 10800) {
                               throw 'field "expire" should be a number with value of at most 10800 if "priority" is set to 2';
                           }
                   
                           data.retry = params.retry;
                           data.expire = params.expire;
                       }
                  
                       data = JSON.stringify(data);
                       Zabbix.log(4, '[ Pushover Webhook ] Sending request: ' + params.endpoint + '\n' + data);
               
                       request.addHeader('Content-Type: application/json');
                       response = request.post(params.endpoint, data);
                  
                       Zabbix.log(4, '[ Pushover Webhook ] Received response with status code ' + request.getStatus() + '\n' + response);
                  
                       if (response !== null) {
                           try {
                               response = JSON.parse(response);
                           }
                           catch (error) {
                               Zabbix.log(4, '[ Pushover Webhook ] Failed to parse response received from Pushover');
                               response = null;
                           }
                       }
                  
                       if (request.getStatus() != 200 || response === null || typeof response !== 'object' || response.status !== 1) {
                           if (response !== null && typeof response === 'object' && typeof response.errors === 'object'
                                   && typeof response.errors[0] === 'string') {
                               throw response.errors[0];
                           }
                           else {
                               throw 'Unknown error. Check debug log for more information.';
                           }
                       }
                   
                       return 'OK';
                   }
                   catch (error) {
                       Zabbix.log(4, '[ Pushover Webhook ] Pushover notification failed: ' + error);
                       throw 'Pushover notification failed: ' + error;
                   }
                 description: |
                   Please refer to setup guide here: https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/pushover?at=refs%2Fheads%2Frelease%2F7.4
                   
                   Set token parameter with to your Pushover application key.
                   When assigning Pushover media to the Zabbix user - add user key into send to field.
                 message_templates:
                   - event_source: TRIGGERS
                     operation_mode: PROBLEM
                     subject: 'Problem: {EVENT.NAME}'
                     message: |
                       Problem started at {EVENT.TIME} on {EVENT.DATE}
                       Problem name: {EVENT.NAME}
                       Host: {HOST.NAME}
                       Severity: {EVENT.SEVERITY}
                       Operational data: {EVENT.OPDATA}
                       Original problem ID: {EVENT.ID}
                       {TRIGGER.URL}
                   - event_source: TRIGGERS
                     operation_mode: RECOVERY
                     subject: 'Resolved in {EVENT.DURATION}: {EVENT.NAME}'
                     message: |
                       Problem has been resolved at {EVENT.RECOVERY.TIME} on {EVENT.RECOVERY.DATE}
                       Problem name: {EVENT.NAME}
                       Problem duration: {EVENT.DURATION}
                       Host: {HOST.NAME}
                       Severity: {EVENT.SEVERITY}
                       Original problem ID: {EVENT.ID}
                       {TRIGGER.URL}
                   - event_source: TRIGGERS
                     operation_mode: UPDATE
                     subject: 'Updated problem in {EVENT.AGE}: {EVENT.NAME}'
                     message: |
                       {USER.FULLNAME} {EVENT.UPDATE.ACTION} problem at {EVENT.UPDATE.DATE} {EVENT.UPDATE.TIME}.
                       {EVENT.UPDATE.MESSAGE}
                     
                       Current problem status is {EVENT.STATUS}, age is {EVENT.AGE}, acknowledged: {EVENT.ACK.STATUS}.
                   - event_source: DISCOVERY
                     operation_mode: PROBLEM
                     subject: 'Discovery: {DISCOVERY.DEVICE.STATUS} {DISCOVERY.DEVICE.IPADDRESS}'
                     message: |
                       Discovery rule: {DISCOVERY.RULE.NAME}
                      
                       Device IP: {DISCOVERY.DEVICE.IPADDRESS}
                       Device DNS: {DISCOVERY.DEVICE.DNS}
                       Device status: {DISCOVERY.DEVICE.STATUS}
                       Device uptime: {DISCOVERY.DEVICE.UPTIME}
                       
                       Device service name: {DISCOVERY.SERVICE.NAME}
                       Device service port: {DISCOVERY.SERVICE.PORT}
                       Device service status: {DISCOVERY.SERVICE.STATUS}
                       Device service uptime: {DISCOVERY.SERVICE.UPTIME}
                   - event_source: AUTOREGISTRATION
                     operation_mode: PROBLEM
                     subject: 'Autoregistration: {HOST.HOST}'
                     message: |
                       Host name: {HOST.HOST}
                       Host IP: {HOST.IP}
                       Agent port: {HOST.PORT}

Copy

✔ Copied

#### Exported elements

Exported elements are explained in the table below.

name | string | (required) Media type name.  
---|---|---  
type | string | (required) Transport used by the media type.  
Possible values:1 EMAIL (0), SMS (1), SCRIPT (2), WEBHOOK (4).  
status | string | Whether the media type is enabled.  
Possible values:1 ENABLED (0, default), DISABLED (1)  
max_sessions | integer | The maximum number of alerts that can be processed in parallel.  
Possible values for SMS:1 1 (default).  
Possible values for other media types:1 0-100 (where 0 - unlimited).  
attempts | integer | The maximum number of attempts to send an alert.  
Possible values:1 1-10 (default: 3).  
attempt_interval | string | The interval (using seconds or [time suffix](/documentation/current/en/manual/appendix/suffixes#time-suffixes)) between retry attempts.  
Possible values:1 0-60s (default: 10s).  
description | string | Media type description.  
message_templates |  | Root element for media type message templates.  
| event_source | string | (required) Event source.  
Possible values:1 TRIGGERS (0), DISCOVERY (1), AUTOREGISTRATION (2), INTERNAL (3), SERVICE (4).  
operation_mode | string | Operation mode.  
Possible values:1 PROBLEM (0), RECOVERY (1), UPDATE (2).  
subject | string | Message subject.  
message | string | Message body.  
  
See also: [Media type object](/documentation/current/en/manual/api/reference/mediatype/object) (refer to the relevant property with a matching name).

**Email**

The following additional elements are exported only for the _Email_ media type.

provider | string | Email provider.  
---|---|---  
smtp_server | string | SMTP server.  
smtp_port | integer | SMTP server port to connect to.  
Default: 25.  
smtp_helo | string | SMTP helo.  
smtp_email | string | Email address from which notifications will be sent.  
smtp_security | string | SMTP connection security level to use.  
Possible values:1 NONE (0, default), STARTTLS (1), SSL_OR_TLS (2).  
smtp_verify_host | string | SSL verify host for SMTP.  
Possible values:1 NO (0, default), YES (1).  
smtp_verify_peer | string | SSL verify peer for SMTP.  
Possible values:1 NO (0, default), YES (1).  
smtp_authentication | string | SMTP authentication method to use.  
Possible values:1 NONE (0, default), PASSWORD (1), OAUTH (2).  
username | string | Username.  
password | string | Authentication password.  
redirection_url | string | Zabbix frontend URL to redirect back OAuth authorization.  
client_id | string | The client identifier registered within the OAuth authorization server.  
authorization_url | string | OAuth URL, with parameters, to get access and refresh tokens.  
token_url | string | OAuth URL to exchange authorization token to access and refresh tokens.  
message_format | string | Message format.  
Possible values:1 TEXT (0), HTML (1, default).  
  
See also: [Media type object](/documentation/current/en/manual/api/reference/mediatype/object) (refer to the relevant property with a matching name).

**SMS**

The following additional elements are exported only for the _SMS_ media type.

gsm_modem | string | (required) Serial device name of the GSM modem.  
---|---|---  
  
See also: [Media type object](/documentation/current/en/manual/api/reference/mediatype/object) (refer to the relevant property with a matching name).

**Script**

The following additional elements are exported only for the _Script_ media type.

script name | string | (required) Script name.  
---|---|---  
parameters |  | Root element for script parameters.  
| sortorder | string | (required) Order of the script parameters passed to the script as command-line arguments.  
value | string | Script parameter value.  
  
See also: [Media type object](/documentation/current/en/manual/api/reference/mediatype/object) (refer to the relevant property with a matching name).

**Webhook**

The following additional elements are exported only for the _Webhook_ media type.

script | string | Script.  
---|---|---  
timeout | string | Javascript script HTTP request timeout interval.  
Possible values:1 1-60s (default: 30s).  
process_tags | string | Whether to process returned tags.  
Possible values:1 NO (0, default), YES (1).  
show_event_menu | string | Indicates the presence of an entry in the event menu if the {EVENT.TAGS.*} macro was successfully resolved in `event_menu_url` and `event_menu_name` fields.  
Possible values:1 NO (0, default), YES (1).  
event_menu_url | string | URL of the event menu entry. Supports {EVENT.TAGS.*} macro.  
event_menu_name | string | Name of the event menu entry. Supports {EVENT.TAGS.*} macro.  
parameters |  | Root element for webhook media type parameters.  
| name | string | (required) Webhook parameter name.  
value | string | Webhook parameter value.  
  
See also: [Media type object](/documentation/current/en/manual/api/reference/mediatype/object) (refer to the relevant property with a matching name).

#### Footnotes

1 API integer values in brackets, for example, ENABLED (0), are mentioned only for reference. For more information, see the linked API object page in the table entry or at the end of each section.