---
title: Custom alert scripts
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/script
downloaded: 2025-11-14 10:36:14
---

# 3 Custom alert scripts

### Overview

If you are not satisfied with the existing media types for sending alerts, there is an alternative way to do that. You can create a script that will handle the notification your way.

Custom alert scripts are executed on Zabbix server. These scripts must be located in the directory specified in the server configuration file [AlertScriptsPath](/documentation/current/en/manual/appendix/config/zabbix_server#alertscriptspath) parameter.

Here is an example of a custom alert script:
    
    
    #!/bin/bash
           
           to=$1
           subject=$2
           body=$3
           host=$4
           value=$5
           
           cat <<EOF | mail -s "$subject" "$to"
           $body
           
           Host: $host
           Value: $value
           EOF

Copy

✔ Copied

Zabbix checks for the exit code of the executed commands and scripts. Any exit code, which is different from **0** , is considered as a [command execution](/documentation/current/en/manual/appendix/command_execution) error. In such cases, Zabbix will try to repeat failed execution.

Environment variables are not preserved or created for the script, so they should be handled explicitly.

### Configuration

To configure custom alert scripts as a media type:

  1. Go to _Alerts → Media types_.
  2. Click on _Create media type_.

The **Media type** tab contains general media type attributes:

![](/documentation/current/assets/en/manual/config/notifications/media/media_script.png)

All mandatory input fields are marked with a red asterisk.

The following parameters are specific for the script media type:

_Script name_ | Enter the name of the script file (e.g., notification.sh) that is located in the directory specified in the [AlertScriptsPath](/documentation/current/en/manual/appendix/config/zabbix_server#alertscriptspath) server configuration parameter.  
---|---  
_Script parameters_ | Add optional script parameters that will be passed to the script as command-line arguments in the order in which they are defined.  
  
Script parameters support {ALERT.SENDTO}, {ALERT.SUBJECT}, {ALERT.MESSAGE} macros, and all [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) that are supported in notifications, as well as [user macros](/documentation/current/en/manual/appendix/macros/supported_by_location_user).  
  
See [common media type parameters](/documentation/current/en/manual/config/notifications/media#common-parameters) for details on how to configure default messages and alert processing options.

Even if an alert script does not use default messages, the message templates for operation types used by this media type must still be defined. Otherwise, a notification will not be sent.

If more than one script media type is configured, these scripts may be processed in parallel by the alerter processes. The total number of alerter processes is limited by the server configuration file [`StartAlerters`](/documentation/current/en/manual/appendix/config/zabbix_server#startalerters) parameter.

### Testing

To test a configured script media type:

  1. Locate the relevant script in the [list](/documentation/current/en/manual/config/notifications/media#overview) of media types.

  2. Click on _Test_ in the last column of the list; a testing form will open in a pop-up window. The testing form will contain the same number of parameters that are configured for the script media type.

  3. Edit the script parameter values if needed. Editing only affects the test procedure; the actual values will not be changed.

  4. Click on _Test_.

![](/documentation/current/assets/en/manual/config/notifications/media/script_test.png)

When testing a configured script media type, {ALERT.SENDTO}, {ALERT.SUBJECT}, {ALERT.MESSAGE} and user macros will resolve to their values, but macros that are related to events (e.g., {HOST.HOST}, {ITEM.LASTVALUE}, etc.) will not resolve, as during testing there is no related event to get the details from. Note that macros within {ALERT.SUBJECT} and {ALERT.MESSAGE} macros will also not resolve. For example, if the value of {ALERT.SUBJECT} is composed of "Problem: {EVENT.NAME}" then the {EVENT.NAME} macro will not be resolved.

### User media

Once the media type is configured, go to the _Users → Users_ section and edit a user profile by assigning this media type to the user. Steps for setting up user media, being common for all media types, are described on the [Media types](/documentation/current/en/manual/config/notifications/media#user-media) page.

Note that when defining the user media, the _Send to_ field cannot be empty. If this field is not used in the alert script, enter any combination of supported characters to bypass validation requirements.