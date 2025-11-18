---
title: Scripts
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts
downloaded: 2025-11-14 10:39:14
---

# 3 Scripts

#### Overview

In the _Alerts → Scripts_ section user-defined global scripts can be configured and maintained.

Global scripts, depending on the configured scope and also user permissions, are available for execution:

  * from the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu) in various frontend locations (_Dashboard_ , _Problems_ , _Latest data_ , _Maps_ , etc.)
  * from the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu)
  * can be run as an action operation

The scripts are executed on Zabbix agent, Zabbix server (proxy) or Zabbix server only. See also [Command execution](/documentation/current/en/manual/appendix/command_execution).

Both on Zabbix agent and Zabbix proxy remote scripts are disabled by default. They can be enabled by:

  * For remote commands executed on Zabbix agent: 
    * adding an AllowKey=system.run[<command>,*] parameter for each allowed command in agent configuration, * stands for wait and nowait mode;
  * For remote commands executed on Zabbix proxy: 
    * **Warning: It is not required to enable remote commands on Zabbix proxy if remote commands are executed on Zabbix agent that is monitored by Zabbix proxy.** If, however, it is required to execute remote commands on Zabbix proxy, set _EnableRemoteCommands_ parameter to '1' in the proxy configuration.

Global script execution on Zabbix server can be disabled by setting EnableGlobalScripts=0 in server configuration. For new installations, since Zabbix 7.0, global script execution on Zabbix server is disabled by default.

A listing of existing scripts with their details is displayed.

![](/documentation/current/assets/en/manual/web_interface/scripts.png)

Displayed data:

_Name_ | Name of the script. Clicking on the script name opens the script [configuration form](scripts#configuring-a-global-script).  
---|---  
_Scope_ | Scope of the script - action operation, manual host action or manual event action. This setting determines where the script is available.  
_Used in actions_ | All actions where the script is used are displayed, preceded by the total number of these actions.  
Clicking on the action name opens the action configuration form. If the user has no permissions to the action, the name is not clickable.  
_Type_ | Script type is displayed - _URL_ , _Webhook_ , _Script_ , _SSH_ , _Telnet_ or _IPMI_ command.  
_Execute on_ | It is displayed whether the script will be executed on Zabbix agent, Zabbix proxy or server, or Zabbix server only.  
_Commands_ | All commands to be executed within the script are displayed.  
Nothing is displayed here for webhooks.  
_User group_ | The user group that the script is available to is displayed (or _All_ for all user groups).  
_Host group_ | The host group that the script is available for is displayed (or _All_ for all host groups).  
_Host access_ | The permission level for the host group is displayed - _Read_ or _Write_. Only users with the required permission level will have access to executing the script.  
  
To configure a new script, click on the _Create script_ button in the upper-right corner.

##### Mass editing options

A button below the list offers one mass-editing option:

  * _Delete_ \- delete the scripts

To use this option, mark the checkboxes before the respective scripts and click on _Delete_.

##### Using filter

You can use the filter to display only the scripts you are interested in. For better search performance, data is searched with macros unresolved.

The _Filter_ link is available above the list of scripts. If you click on it, a filter becomes available where you can filter scripts by name and scope.

![](/documentation/current/assets/en/manual/web_interface/script_filter.png)

#### Configuring a global script

![](/documentation/current/assets/en/manual/web_interface/script.png)

Script attributes:

_Name_ | Unique name of the script.  
E.g. `Clear /tmp filesystem`  
---|---  
_Scope_ | Scope of the script - action operation, manual host action or manual event action. This setting determines where the script can be used - in remote commands of action operations, from the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu) or from the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu) respectively.  
Setting the scope to 'Action operation' makes the script available for all users with access to _Alerts_ → _Actions_.  
If a script is actually used in an action, its scope cannot be changed away from 'action operation'.  
**Macro support**  
The scope affects the range of available macros. For example, user-related macros ({USER.*}) are supported in scripts to allow passing information about the user that launched the script. However, they are not supported if the script scope is action operation, as action operations are executed automatically.  
A {MANUALINPUT} macro allows to specify manual input at script execution time. It is supported for manual host action and manual event action scripts.  
To find out which other macros are supported, do a search for 'Trigger-based notifications and commands/Trigger-based commands', 'Manual host action scripts' and 'Manual event action scripts' in the [supported macro](/documentation/current/en/manual/appendix/macros/supported_by_location) table. Note that if a macro may resolve to a value with spaces (for example, host name), don't forget to quote as needed.  
_Menu path_ | The desired menu path to the script. For example, `Default` or `Default/`, will display the script in the respective directory. Menus can be nested, e.g. `Main menu/Sub menu1/Sub menu2`. When accessing scripts through the host/event menu in monitoring sections, they will be organized according to the given directories.  
This field is displayed only if 'Manual host action' or 'Manual event action' is selected as _Scope_.  
_Type_ | Click the respective button to select script type:  
**URL** , **Webhook** , **Script** , **SSH** , **Telnet** or **[IPMI](/documentation/current/en/manual/config/notifications/action/operation/remote_command#ipmi-remote-commands)** command.  
The type **URL** is available only when 'Manual host action' or 'Manual event action' is selected as _Scope_.  
| Script type: **URL**  
_URL_ | Specify the URL for quick access from the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu) or [event menu](/documentation/current/en/manual/web_interface/menu/event_menu).  
[Macros](/documentation/current/en/manual/appendix/macros/supported_by_location) and custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported. Macro support depends on the scope of the script (see _Scope_ above).  
Use the {MANUALINPUT} macro in this field to be able to specify manual input at script execution time, for example:  
`http://{MANUALINPUT}/zabbix/zabbix.php?action=dashboard.view`  
Macro values must not be URL-encoded.  
_Open in new window_ | Determines whether the URL should be opened in a new or the same browser tab.  
| Script type: **Webhook**  
_Parameters_ | Specify the webhook variables as attribute-value pairs.  
See also: [Webhook](/documentation/current/en/manual/config/notifications/media/webhook) media configuration.  
[Macros](/documentation/current/en/manual/appendix/macros/supported_by_location) and custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported in parameter values. Macro support depends on the scope of the script (see _Scope_ above).  
_Script_ | Enter the JavaScript code in the modal editor that opens when clicking in the parameter field or on the pencil icon next to it.  
Macro support depends on the scope of the script (see _Scope_ above).  
See also: [Webhook](/documentation/current/en/manual/config/notifications/media/webhook) media configuration, [Additional Javascript objects](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects).  
_Timeout_ | JavaScript execution timeout (1-60s, default 30s).  
Time suffixes are supported, e.g. 30s, 1m.  
| Script type: **Script**  
_Execute on_ | Click the respective button to execute the shell script on:  
**Zabbix agent** \- the script will be executed by Zabbix agent (if the system.run item is [allowed](/documentation/current/en/manual/config/items/restrict_checks)) on the host  
**Zabbix proxy or server** \- the script will be executed by Zabbix proxy or server - depending on whether the host is monitored by proxy or server.  
It will be executed on the proxy if enabled by [EnableRemoteCommands](/documentation/current/en/manual/appendix/config/zabbix_proxy#enableremotecommands).  
It will be executed on the server if global scripts are enabled by the [EnableGlobalScripts](/documentation/current/en/manual/appendix/config/zabbix_server#enableglobalscripts) server parameter.  
**Zabbix server** \- the script will be executed by Zabbix server only.  
This option will not be available if global scripts are disabled by the [EnableGlobalScripts](/documentation/current/en/manual/appendix/config/zabbix_server#enableglobalscripts) server parameter.  
_Commands_ | Enter full path to the commands to be executed within the script.  
Macro support depends on the scope of the script (see _Scope_ above). Custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
| Script type: **SSH**  
_Authentication method_ | Select authentication method - password or public key.  
_Username_ | Enter the username.  
_Password_ | Enter the password.  
This field is available if 'Password' is selected as the authentication method.  
_Public key file_ | Enter the path to the public key file.  
This field is available if 'Public key' is selected as the authentication method.  
_Private key file_ | Enter the path to the private key file.  
This field is available if 'Public key' is selected as the authentication method.  
_Passphrase_ | Enter the passphrase.  
This field is available if 'Public key' is selected as the authentication method.  
_Port_ | Enter the port.  
_Commands_ | Enter the commands.  
Macro support depends on the scope of the script (see _Scope_ above). Custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
| Script type: **Telnet**  
_Username_ | Enter the username.  
_Password_ | Enter the password.  
_Port_ | Enter the port.  
_Commands_ | Enter the commands.  
Macro support depends on the scope of the script (see _Scope_ above). Custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
| Script type: **IPMI**  
_Command_ | Enter the IPMI command.  
Macro support depends on the scope of the script (see _Scope_ above). Custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Description_ | Enter a description for the script.  
_Host group_ | Select the host group that the script will be available for (or _All_ for all host groups).  
_User group_ | Select the user group that the script will be available to (or _All_ for all user groups).  
This field is displayed only if 'Manual host action' or 'Manual event action' is selected as _Scope_.  
_Required host permissions_ | Select the permission level for the host group - _Read_ or _Write_. Only users with the required permission level will have access to executing the script.  
This field is displayed only if 'Manual host action' or 'Manual event action' is selected as _Scope_.  
_Advanced configuration_ | Click on the _Advanced configuration_ label to display advanced configuration options.  
This field is displayed only if 'Manual host action' or 'Manual event action' is selected as _Scope_.  
  
#### Advanced configuration

Advanced configuration options are available in a collapsible _Advanced configuration_ section:

![](/documentation/current/assets/en/manual/web_interface/script_advanced.png)

_Enable user input_ | Mark the checkbox to enable manual user input before executing the script.  
Manual user input will replace the {MANUALINPUT} macro value in the script.  
See also: Manual user input.  
---|---  
_Input prompt_ | Enter custom text prompting for custom user input. This text will be displayed above the input field in the _Manual input_ popup.  
To see a preview of the _Manual input_ popup, click on _Test user input_. The preview also allows to test if the input string complies with the input validation rule (see parameters below).  
Macro and user macro support depends on the scope of the script (see _Scope_ in general script configuration parameters).  
_Input type_ | Select the manual input type:  
**String** \- single string;  
**Dropdown** \- value is selected from multiple dropdown options.  
_Dropdown options_ | Enter unique values for the user input dropdown in a comma-delimited list.  
To include an empty option in the dropdown, add an extra comma at the beginning, middle, or end of the list.  
This field is displayed only if 'Dropdown' is selected as _Input type_.  
_Default input string_ | Enter the default string for user input (or none).  
This field will be validated against the regular expression provided in the _Input validation rule_ field.  
The value entered here will be displayed by default in the _Manual input_ popup.  
This field is displayed only if 'String' is selected as _Input type_.  
_Input validation rule_ | Enter a regular expression to validate the user input string.  
Global regular expressions are supported.  
This field is displayed only if 'String' is selected as _Input type_.  
_Enable confirmation_ | Mark the checkbox to display a confirmation message before executing the script. This feature might be especially useful with potentially dangerous operations (like a reboot script) or ones that might take a long time.  
_Confirmation text_ | Enter custom confirmation text for the confirmation popup enabled with the checkbox above (for example, _Remote system will be rebooted. Are you sure?_). To see how the text will look like, click on _Test confirmation_ next to the field.  
[Macros](/documentation/current/en/manual/appendix/macros/supported_by_location) and custom [user macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Note:_ the macros will not be expanded when testing the confirmation message.  
  
If both manual user input and a confirmation message are configured, they will be displayed in consecutive popup windows.

#### Manual user input

Manual user input allows to supply a custom parameter on each execution of the script. This saves the necessity to create multiple similar user scripts with only a single parameter difference.

For example, you may want to supply a different integer or a different URL address to the script during execution.

To enable manual user input:

  * use the {MANUALINPUT} macro in the script (commands, script, script parameter) where required; or in the URL field of URL scripts;
  * in advanced script configuration, enable manual user input and configure input options.

With user input enabled, before script execution, a _Manual input_ popup will appear to the user asking to supply a custom value. The supplied value will replace {MANUALINPUT} in the script.

Depending on the configuration, the user will be asked to enter a string value:

![](/documentation/current/assets/en/manual/web_interface/manual_input_field.png)

Or select the value from a dropdown of pre-determined options:

![](/documentation/current/assets/en/manual/web_interface/manual_input_field2.png)

Manual user input is available only for scripts where the scope is 'Manual host action' or 'Manual event action'.

#### Script execution and result

Scripts run by Zabbix server are executed in the order described in the [command execution page](/documentation/current/en/manual/appendix/command_execution).

The script result is displayed in a pop-up window that appears after the script is run. The return value of the script is a standard output:

  * If the script finishes successfully ([exit code](/documentation/current/en/manual/appendix/command_execution#exit-code-checking) `0`), the return value is limited to 16MB (including trailing whitespace that is truncated).
  * If the script exits with an error (non-zero exit code), the return value is a standard error limited to 2KB.

Zabbix does not store extended script output by default. To preserve full output details, you can implement logging within the script itself (e.g., redirect output to a local log file).

Note that for scripts executed either on Zabbix server or Zabbix proxy, [database limits](/documentation/current/en/manual/config/items/item#text-data-limits) also apply.

Below is an example of a script and the result window:
    
    
    uname -v
           /tmp/non_existing_script.sh
           echo "This script was started by {USER.USERNAME}"

Copy

✔ Copied

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/script_result.png)

The script result does not display the script itself.

#### Script timeout

##### Zabbix agent

You may encounter a situation when a timeout occurs while executing a script.

See an example of a script running on Zabbix agent and the result window below:
    
    
    sleep 5
           df -h

Copy

✔ Copied

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/script_timeout_1.png)

The error message, in this case, is the following:
    
    
    Timeout while executing a shell script.

Copy

✔ Copied

To avoid such situations, it is advised to optimize the script itself (in the example above, "5") instead of adjusting the `Timeout` parameter in [Zabbix agent configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd#timeout) and [Zabbix server configuration](/documentation/current/en/manual/appendix/config/zabbix_server#timeout). However, for Zabbix agent in active mode, the `Timeout` parameter in [Zabbix server configuration](/documentation/current/en/manual/appendix/config/zabbix_server#timeout) should be at least several seconds longer than the `RefreshActiveChecks` parameter in [Zabbix agent configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd#refreshactivechecks). This ensures that the server has enough time to receive the active check results from the agent. Note that script execution on an active agent is supported since Zabbix agent 7.0.

In case the `Timeout` parameter has been changed in [Zabbix agent configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd), the following error message will appear:
    
    
    Get value from agent failed: ZBX_TCP_READ() timed out.

Copy

✔ Copied

It means that the modification has been made in [Zabbix agent configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd), but it is required to modify the `Timeout` parameter in [Zabbix server configuration](/documentation/current/en/manual/appendix/config/zabbix_server) as well.

##### Zabbix server/proxy

See an example of a script running on Zabbix server and the result window below:
    
    
    sleep 11
           df -h

Copy

✔ Copied

![](/documentation/current/assets/en/manual/web_interface/frontend_sections/administration/script_timeout_3.png)

It is also advised to optimize the script itself (instead of adjusting `TrapperTimeout` parameter to a corresponding value (in our case, > `11`) by modifying the [Zabbix server configuration](/documentation/current/en/manual/appendix/config/zabbix_server)).