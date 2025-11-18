---
title: Webhook
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/webhook
downloaded: 2025-11-14 10:36:16
---

# 4 Webhook

#### Overview

The webhook media type is useful for making HTTP calls using custom JavaScript code for straightforward integration with external software such as helpdesk systems, chats, or messengers. You may choose to import an integration provided by Zabbix or create a custom integration from scratch.

#### Integrations

The following integrations are available allowing to use predefined webhook media types for pushing Zabbix notifications to:

  * [brevis.one](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/brevis.one/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Discord](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/discord/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Event-Driven Ansible](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/event_driven_ansible/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Express.ms messenger](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/express.ms/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [GitHub](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/github/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [GLPi](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/glpi/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [iLert](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/ilert/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [iTop](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/itop/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Jira](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/jira/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Jira Service Management](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/jira_service_management/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [ManageEngine ServiceDesk](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/manageengine_servicedesk/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Mantis Bug Tracker](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/mantisbt/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Mattermost](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/mattermost/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MS Teams](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/msteams/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MS Teams Workflows](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/msteams-workflow/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [LINE](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/line/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Opsgenie](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/opsgenie/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [OTRS CE](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/otrs_ce/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Pagerduty](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/pagerduty/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Pushover](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/pushover/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Redmine](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/redmine/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Rocket.Chat](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/rocketchat/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [ServiceNow](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/servicenow/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [SIGNL4](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/signl4/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Slack](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/slack/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [SolarWinds](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/solarwinds/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [SysAid](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/sysaid/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Telegram](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/telegram/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [TOPdesk](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/topdesk/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [VictorOps](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/victorops/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Zammad](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/zammad/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Zendesk](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media/zendesk/README.md?at=refs%2Fheads%2Frelease%2F7.4)

In addition to the services listed here, Zabbix can be integrated with **Spiceworks** (no webhook is required). To convert Zabbix notifications into Spiceworks tickets, create an [email media type](/documentation/current/en/manual/config/notifications/media/email) and enter Spiceworks helpdesk email address (e.g. help@zabbix.on.spiceworks.com) in the profile settings of a designated Zabbix user.

#### Configuration

To start using a webhook integration:

  1. Locate the required .yaml file in the `templates/media` directory of the downloaded Zabbix version or download it from Zabbix [git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media?at=refs%2Fheads%2Frelease%2F7.4).
  2. [Import](/documentation/current/en/manual/xml_export_import/media#importing) the file into your Zabbix installation. The webhook will appear in the list of media types.
  3. Configure the webhook according to instructions in the _Readme.md_ file (you may click on a webhook's name above to quickly access _Readme.md_).

To create a custom webhook from scratch:

  1. Go to _Alerts > Media types_.
  2. Click on _Create media type_.

The **Media type** tab contains various attributes specific for this media type:

![](/documentation/current/assets/en/manual/config/notifications/media/media_webhook_express.png)

All mandatory input fields are marked with a red asterisk.

The following parameters are specific for the webhook media type:

_Parameters_ | Specify the webhook variables as the attribute and value pairs.  
For preconfigured webhooks, a list of parameters varies, depending on the service. Check the webhook's _Readme.md_ file for parameter description.  
For new webhooks, several common variables are included by default (URL:<empty>, HTTPProxy:<empty>, To:{ALERT.SENDTO}, Subject:{ALERT.SUBJECT}, Message:{ALERT.MESSAGE}), feel free to keep or remove them.  
  
Webhook parameters support [user macros](/documentation/current/en/manual/appendix/macros/supported_by_location_user), all [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) that are supported in problem notifications and, additionally, {ALERT.SENDTO}, {ALERT.SUBJECT}, and {ALERT.MESSAGE} macros.  
  
If you specify an HTTP proxy, the field supports the same functionality as in the item configuration [HTTP proxy](/documentation/current/en/manual/config/items/itemtypes/http#configuration) field. The proxy string may be prefixed with `[scheme]://` to specify which kind of proxy is used (e.g., https, socks4, socks5; see [documentation](https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html)).  
---|---  
_Script_ | Enter JavaScript code in the modal editor that opens when clicking in the parameter field or on the pencil icon next to it. This code will perform the webhook operation.  
The script is a function code that accepts parameter - value pairs. The values should be converted into JSON objects using JSON.parse() method, for example: `var params = JSON.parse(value);`.  
  
The code has access to all parameters, it may perform HTTP GET, POST, PUT and DELETE requests and has control over HTTP headers and request body.  
The script must contain a return operator, otherwise it will not be valid. It may return OK status along with an optional list of tags and tag values (see _Process tags_ option) or an error string.  
  
Note that the script is executed only after an alert is created. If the script is configured to return and process tags, these tags will not get resolved in {EVENT.TAGS} and {EVENT.RECOVERY.TAGS} macros in the initial problem message and recovery messages because the script has not had the time to run yet.  
_Note_ : Using local variables (e.g. `var local = 1`) instead of a global one (e.g. `global = 1`) is recommended to ensure each script operates on its own data and to avoid collisions between simultaneous calls (see [known issues](/documentation/current/en/manual/installation/known_issues#preprocessing--global-variables-are-unsafe)).  
  
See also: [Webhook development guidelines](https://www.zabbix.com/documentation/guidelines/en/webhooks), [Webhook script examples](/documentation/current/en/manual/config/notifications/media/webhook/webhook_examples), [Additional JavaScript objects](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects).  
  
_Timeout_ | JavaScript execution timeout (1-60s, default 30s).  
Time suffixes are supported, e.g., 30s, 1m.  
_Process tags_ | Mark the checkbox to process returned JSON property values as tags. These tags are added to any existing problem tags.  
Note that when using [webhook tags](https://www.zabbix.com/documentation/guidelines/en/webhooks#webhook-tags), the webhook must return a JSON object containing at least an empty tags object: `var result = {tags: {}};`  
Examples of tags that can be returned: _jira-id:prod-1234_ , _responsible:John Smith_ , _processed: <no value>_  
_Include event menu entry_ | Mark the checkbox to include an entry in the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu) linking to a created external ticket.  
An entry will be included for each webhook that is enabled and has this checkbox marked. Note that if the _Menu entry name_ and _Menu entry URL_ parameters contain any [{EVENT.TAGS.<tag name>}](/documentation/current/en/manual/appendix/macros/supported_by_location#events) macros, an entry will be included only if these macros can be resolved (that is, the event has these tags defined).  
If marked, the webhook should not be used for sending notifications to different users (consider creating a [dedicated user](/documentation/current/en/manual/config/notifications/media/webhook#user-media) instead) and should not be used in multiple alert actions [for a single problem event](/documentation/current/en/manual/config/notifications/media/webhook#configuring-alert-actions).  
_Menu entry name_ | Specify the menu entry name.  
[{EVENT.TAGS.<tag name>}](/documentation/current/en/manual/appendix/macros/supported_by_location#events) macro is supported.  
This field is only mandatory if _Include event menu entry_ is marked.  
_Menu entry URL_ | Specify the underlying URL of the menu entry.  
[{EVENT.TAGS.<tag name>}](/documentation/current/en/manual/appendix/macros/supported_by_location#events) macro is supported.  
This field is only mandatory if _Include event menu entry_ is marked.  
  
See [common media type parameters](/documentation/current/en/manual/config/notifications/media#common-parameters) for details on how to configure default messages and alert processing options.

Even if a webhook doesn't use default messages, message templates for operation types used by this webhook must still be defined.

#### Testing

To test a configured webhook media type:

  1. Locate the relevant webhook in the [list](/documentation/current/en/manual/config/notifications/media#overview) of media types.
  2. Click on _Test_ in the last column of the list (a testing window will open).
  3. Edit the webhook parameter values as needed. Replace macros with example values; otherwise, macros will not resolve, and the test will fail.
  4. Click on _Test_.

Replacing or deleting values in the testing window affects the test procedure only, the actual webhook attribute values will remain unchanged.

![](/documentation/current/assets/en/manual/config/webhook_test1.png)

To view media type test log entries without leaving the test window, click on _Open log_ (a new pop-up window will open).

![](/documentation/current/assets/en/manual/config/mediatype_test2.png)

**If the webhook test is successful:**

  * _"Media type test successful."_ message is displayed.
  * Server response appears in the gray _Response_ field.
  * Response type (JSON or String) is specified below the _Response_ field.

**If the webhook test fails:**

  * _"Media type test failed."_ message is displayed, followed by additional failure details.

#### User media

Once the media type is configured, go to the _Users > Users_ section and assign the webhook media to an existing user or create a new user to represent the webhook. Steps for setting up user media for an existing user, being common for all media types, are described on the [Media types](/documentation/current/en/manual/config/notifications/media#user-media) page.

If a webhook uses tags to store ticket\message ID, avoid assigning the same webhook as a media to different users as doing so may cause webhook errors (applies to the majority of webhooks that utilize _Include event menu entry_ option). In this case, the best practice is to create a dedicated user to represent the webhook:

  1. After configuring the webhook media type, go to the _Users > Users_ section and create a dedicated Zabbix user to represent the webhook - for example, with a username _Slack_ for the Slack webhook. All settings, except media, can be left at their defaults as this user will not be logging into Zabbix.
  2. In the user profile, go to a tab _Media_ and [add a webhook](/documentation/current/en/manual/config/notifications/media#user-media) with the required contact information. If the webhook does not use a _Send to_ field, enter any combination of supported characters to bypass validation requirements.
  3. Grant this user at least read [permissions](/documentation/current/en/manual/config/users_and_usergroups/permissions#permissions-to-host-groups) to all hosts for which it should send the alerts.

When configuring alert action, add this user in the _Send to users_ field in Operation details - this will tell Zabbix to use the webhook for notifications from this action.

#### Configuring alert actions

Actions determine which notifications should be sent via the webhook. Steps for [configuring actions](/documentation/current/en/manual/config/notifications/action) involving webhooks are the same as for all other media types with these exceptions:

  * If a webhook uses [webhook tags](https://www.zabbix.com/documentation/guidelines/en/webhooks#webhook-tags) to store ticket\message ID and handle update\resolve operations, avoid using the same webhook in multiple alert actions for a single problem event. If {EVENT.TAGS.<tag name>} exists and gets updated in the webhook, its resulting value will be undefined. To avoid this, use a new tag name in the webhook for storing updated values. This applies to Jira, Jira Service Desk, Mattermost, Opsgenie, OTRS, Redmine, ServiceNow, Slack, Zammad, and Zendesk webhooks provided by Zabbix and to most webhooks utilizing the _Include event menu entry_ option. Note, however, that a single webhook can be used in multiple operations or escalation steps of the same action, as well as in different actions that will not be triggered by the same problem event due to different [conditions](/documentation/current/en/manual/config/notifications/action/conditions).
  * When using a webhook in actions for [internal events](/documentation/current/en/manual/config/events/sources#internal-events), ensure to mark the _Custom message_ checkbox and define a custom message in the action operation configuration. Otherwise, a notification will not be sent.