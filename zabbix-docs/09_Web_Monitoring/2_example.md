---
title: Real-life scenario
source: https://www.zabbix.com/documentation/current/en/manual/web_monitoring/example
downloaded: 2025-11-14 10:36:55
---

# 2 Real-life scenario

#### Overview

This section presents a step-by-step real-life example of how web monitoring can be used.

Zabbix web monitoring will be used to monitor Zabbix frontend. The goal is to determine if it is available, provides the right content, and how quickly it works. To achieve this, several steps are required, including checking the availability of the first page, logging in with a username and password, verifying the login success, logging out, and confirming the logout.

#### Scenario

##### Add a new web scenario

Go to _Data collection → Hosts_ , pick a host and click on _Web_ in the row of that host. Then click on _Create web scenario_.

![](/documentation/current/assets/en/manual/web_monitoring/new_scenario.png)

In the new scenario form, fill out the following fields:

  * **Name** \- Frontend check
  * **Update interval** \- 1m
  * **Attempts** \- 1
  * **Agent** \- Zabbix

In the _Variables_ section, add two variables: _{password}_ and _{user}_. Enter your existing Zabbix user credentials as values.

For safety reasons, it is recommended to create a separate user with minimal permissions to use for monitoring purposes.

Optionally, switch to the _Tags_ tab and add web scenario tags.

Once fully configured, this web scenario will automatically add a Zabbix trapper item to the host. You can use web scenario tags to quickly identify related items and triggers or search through collected data. For example, suitable tags for this tutorial are `component: web-scenario` and/or `target: frontend`.

##### Configure web scenario steps

Switch to the _Steps_ tab and define steps for the scenario. Click on _Add_ button to add an individual step.

###### Common fields

For each step described below, fill out the following fields in addition to the step-specific fields:

  * **URL** \- the URL of Zabbix frontend
  * **Timeout** \- 15s
  * **Required status codes** \- 200

###### Web scenario step 1

Check that the first page responds correctly, returns HTTP response code 200 and contains the text "Zabbix SIA".

  * In the **Name** field, enter _First page_.
  * In the **Required string** field, enter _Zabbix SIA_.
  * Fill out the common fields.

When done configuring the step, press the _Add_ button.

![](/documentation/current/assets/en/manual/web_monitoring/scen_step1.png)

###### Web scenario step 2

Log in to the Zabbix frontend using the macros (variables) defined at the scenario level - _{user}_ and _{password}_.

  * In the **Name** field, enter _Login_.
  * In the **Post fields** section, add three post fields: 
    * _name_ with value _{user}_
    * _password_ with value _{password}_
    * _enter_ with value _Sign in_
  * In the **Variables** section, add a new variable _{csrf_token}_ with value _regex:([0-9a-z]{64})_. This variable will catch the value of the assigned CSRF token to reuse in step 4.
  * Fill out the common fields.

![](/documentation/current/assets/en/manual/web_monitoring/scen_step2.png)

Note that Zabbix frontend uses JavaScript redirect when logging in, so login must occur first, and logged-in features can be checked only in further steps. Additionally, the login step must use the full URL to **index.php** file.

###### Web scenario step 3

After logging in, verify success by checking for a string visible only when logged in - for example, _Administration_.

  * In the **Name** field, enter _Login check_.
  * In the **Required string** field, enter _Administration_.
  * Fill out the common fields.

![](/documentation/current/assets/en/manual/web_monitoring/scen_step3.png)

###### Web scenario step 4

Once the frontend's accessibility and login have been verified, add a logout step - otherwise the Zabbix database will become cluttered with many open session records.

  * In the **Name** field, enter _Logout_.
  * In the **Post fields** section, add two post fields: 
    * _reconnect_ with value _1_
    * __csrf_token_ with value _{csrf_token}_.
  * Fill out the common fields.

This step uses the variable {csrf_token} obtained in step 2

![](/documentation/current/assets/en/manual/web_monitoring/scen_step4.png)

###### Web scenario step 5

To confirm the logout, check for the **Username** string.

  * In the **Name** field, enter _Logout check_.
  * In the **Required string** field, enter _Username_.
  * Fill out the common fields.

![](/documentation/current/assets/en/manual/web_monitoring/scen_step5.png)

###### Full configuration of steps

A complete configuration of web scenario steps should look like this:

![](/documentation/current/assets/en/manual/web_monitoring/scenario_steps.png)

##### Check the results

Save the finished web monitoring scenario.

The scenario will be added to the host. To view web scenario information go to _Monitoring → Hosts_ , locate the host in the list and click on the Web hyperlink in the last column.

![](/documentation/current/assets/en/manual/web_interface/web_monitoring.png)

Click on the scenario name to see more detailed statistics:

![](/documentation/current/assets/en/manual/web_monitoring/scenario_details2.png)