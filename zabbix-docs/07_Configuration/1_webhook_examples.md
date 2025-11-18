---
title: Webhook script examples
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/webhook/webhook_examples
downloaded: 2025-11-14 10:36:17
---

# 1 Webhook script examples

#### Overview

Though Zabbix offers a large number of webhook integrations available out-of-the-box, you may want to create your own webhooks instead. This section provides examples of custom webhook scripts (used in the _Script_ parameter). See [webhook](/documentation/current/en/manual/config/notifications/media/webhook) section for description of other webhook parameters.

Do not use undeclared assignments in preprocessing JavaScript. Use `var` to declare local variables.

#### Jira webhook (custom)

![](/documentation/current/assets/en/manual/config/notifications/media/media_webhook_jira.png)

This script will create a JIRA issue and return some info on the created issue.
    
    
    try {
               Zabbix.log(4, '[ Jira webhook ] Started with params: ' + value);
           
               var result = {
                       'tags': {
                           'endpoint': 'jira'
                       }
                   },
                   params = JSON.parse(value),
                   req = new HttpRequest(),
                   fields = {},
                   resp;
           
               if (params.HTTPProxy) {
                   req.setProxy(params.HTTPProxy);
               }
           
               req.addHeader('Content-Type: application/json');
               req.addHeader('Authorization: Basic ' + params.authentication);
           
               fields.summary = params.summary;
               fields.description = params.description;
               fields.project = {key: params.project_key};
               fields.issuetype = {id: params.issue_id};
           
               resp = req.post('https://jira.example.com/rest/api/2/issue/',
                   JSON.stringify({"fields": fields})
               );
           
               if (req.getStatus() != 201) {
                   throw 'Response code: ' + req.getStatus();
               }
           
               resp = JSON.parse(resp);
               result.tags.issue_id = resp.id;
               result.tags.issue_key = resp.key;
           
               return JSON.stringify(result);
           }
           catch (error) {
               Zabbix.log(4, '[ Jira webhook ] Issue creation failed json : ' + JSON.stringify({"fields": fields}));
               Zabbix.log(3, '[ Jira webhook ] issue creation failed : ' + error);
           
               throw 'Failed with error: ' + error;
           }

Copy

✔ Copied

#### Slack webhook (custom)

This webhook will forward notifications from Zabbix to a Slack channel.

![](/documentation/current/assets/en/manual/config/notifications/media/webhook_slack1.png)
    
    
    try {
               var params = JSON.parse(value),
                   req = new HttpRequest(),
                   response;
           
               if (params.HTTPProxy) {
                   req.setProxy(params.HTTPProxy);
               }
           
               req.addHeader('Content-Type: application/x-www-form-urlencoded');
           
               Zabbix.log(4, '[ Slack webhook ] Webhook request with value=' + value);
           
               response = req.post(params.hook_url, 'payload=' + encodeURIComponent(value));
               Zabbix.log(4, '[ Slack webhook ] Responded with code: ' + req.getStatus() + '. Response: ' + response);
           
               try {
                   response = JSON.parse(response);
               }
               catch (error) {
                   if (req.getStatus() < 200 || req.getStatus() >= 300) {
                       throw 'Request failed with status code ' + req.getStatus();
                   }
                   else {
                       throw 'Request success, but response parsing failed.';
                   }
               }
           
               if (req.getStatus() !== 200 || !response.ok || response.ok === 'false') {
                   throw response.error;
               }
           
               return 'OK';
           }
           catch (error) {
               Zabbix.log(3, '[ Slack webhook ] Sending failed. Error: ' + error);
           
               throw 'Failed with error: ' + error;
           }

Copy

✔ Copied