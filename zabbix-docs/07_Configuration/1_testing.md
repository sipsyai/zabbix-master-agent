---
title: Preprocessing testing
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/testing
downloaded: 2025-11-14 10:34:45
---

# 1 Preprocessing testing

### Testing

Testing preprocessing steps is useful to make sure that complex preprocessing pipelines yield the results that are expected from them, without waiting for the item value to be received and preprocessed.

![](/documentation/current/assets/en/manual/config/items/test_item_steps.png)

It is possible to test:

  * against a hypothetical value
  * against a real value from a host

Each preprocessing step can be tested individually as well as all steps can be tested together. When you click on the _Test_ or _Test all steps_ button respectively in the Actions block, a testing window is opened.

##### Testing hypothetical value

![](/documentation/current/assets/en/manual/config/items/test_item_p.png)

_Get value from host_ | If you want to test a hypothetical value, leave this checkbox unmarked.  
See also: Testing real value.  
---|---  
_Value_ | Enter the input value to test.  
Clicking in the parameter field or on the view/edit button ![](/documentation/current/assets/en/manual/config/items/pencil.png) will open a text area window for entering the value or code block.  
_Not supported_ | Mark this checkbox to test an unsupported value.  
This option is useful to test the _Check for not supported value_ preprocessing step.  
_Error_ | Enter the error text.  
This field is enabled when _Get value from host_ is unchecked, but _Not supported_ is checked.  
If _Get value from host_ is checked, this field gets filled with the actual error message (read-only) from the host.  
_Time_ | Time of the input value is displayed: `now` (read-only).  
_Previous value_ | Enter a previous input value to compare to.  
Only for _Change_ and _Throttling_ preprocessing steps.  
_Previous time_ | Enter the previous input value time to compare to.  
Only for _Change_ and _Throttling_ preprocessing steps.  
The default value is based on the 'Update interval' field value of the item (if '1m', then this field is filled with `now-1m`). If nothing is specified or the user has no access to the host, the default is `now-30s`.  
_Macros_ | If any macros are used, they are listed along with their values. The values are editable for testing purposes, but the changes will only be saved within the testing context.  
_End of line sequence_ | Select the end of line sequence for multiline input values:  
**LF** \- LF (line feed) sequence  
**CRLF** \- CRLF (carriage-return line-feed) sequence.  
_Preprocessing steps_ | Preprocessing steps are listed; the testing result is displayed for each step after the _Test_ button is clicked.  
Test results are truncated to a maximum size of 512KB when sent to the frontend. Test results can be copied (not more than the truncated 512KB). If a result is truncated, a warning icon is displayed. The warning description is displayed on mouseover. Note that data larger than 512KB is still processed fully by Zabbix server.  
If the step failed in testing, an error icon is displayed. The error description is displayed on mouseover.  
In case "Custom on fail" is specified for the step and that action is performed, a new line appears right after the preprocessing test step row, showing what action was done and what outcome it produced (error or value).  
_Result_ | The final result of testing preprocessing steps is displayed in all cases when all steps are tested together (when you click on the _Test all steps_ button).  
The type of conversion to the value type of the item is also displayed, for example `Result converted to Numeric (unsigned)`.  
Test results are truncated to a maximum size of 512KB when sent to the frontend. The final result can be copied (not more than the truncated 512KB). If a result is truncated, a warning icon is displayed. The warning description is displayed on mouseover. Note that data larger than 512KB is still processed fully by Zabbix server.  
  
Click on _Test_ to see the result after each preprocessing step.

Test values are stored between test sessions for either individual steps or all steps, allowing the user to change preprocessing steps or item configuration and then return to the testing window without having to re-enter information. Values are lost on a page refresh though.

The testing is done by Zabbix server. The frontend sends a corresponding request to the server and waits for the result. The request contains the input value and preprocessing steps (with expanded user macros). For _Change_ and _Throttling_ steps, an optional previous value and time can be specified. The server responds with results for each preprocessing step.

All technical errors or input validation errors are displayed in the error box at the top of the testing window.

##### Testing real value

To test preprocessing against a real value:

  * Mark the _Get value from host_ checkbox
  * Enter or verify host parameters (host address, port, proxy name/no proxy) and item-specific details (such as SNMPv2 community or SNMPv3 security credentials). These fields are context-aware: 
    * The values are pre-filled when possible, i.e., for items requiring an agent, by taking the information from the selected agent interface of the host
    * The values have to be filled manually for template items
    * Plain-text macro values are resolved
    * Where the field value (or part of the value) is a secret or Vault macro, the field will be empty and has to be filled out manually. If any item parameter contains a secret macro value, the following warning message is displayed: "Item contains user-defined macros with secret values. Values of these macros should be entered manually."
    * The fields are disabled when not needed in the context of the item type (e.g., the host address and the proxy fields are disabled for calculated items)
  * Click on _Get value and test_ to test the preprocessing

![](/documentation/current/assets/en/manual/config/items/test_item_p2.png)

If you have specified a value mapping in the item configuration form ('Show value' field), the item test dialog will show another line after the final result, named 'Result with value map applied'.

Parameters that are specific to getting a real value from a host:

_Get value from host_ | Mark this checkbox to get a real value from the host.  
---|---  
_Host address_ | Enter the host address.  
This field is automatically filled by the address of the item host interface.  
_Port_ | Enter the host port.  
This field is automatically filled by the port of item host interface.  
_Additional fields for SNMP interfaces  
(SNMP version, SNMP community, Context name, etc.)_ | See [Configuring SNMP monitoring](/documentation/current/en/manual/config/items/itemtypes/snmp#step-2) for additional details on configuring an SNMP interface (v1, v2 and v3).  
These fields are automatically filled from the item host interface.  
_Proxy_ | Specify the proxy if the host is monitored by a proxy.  
This field is automatically filled by the proxy of the host (if any).  
_Value_ | Value retrieved from the host.  
Clicking in the parameter field or on the view/edit button ![](/documentation/current/assets/en/manual/config/items/pencil.png) will open a text area window of the value or code block.  
Values are truncated to a maximum size of 512KB and only in the frontend. If a result is truncated, a warning icon is displayed. The warning description is displayed on mouseover. Note that data larger than 512KB is still processed fully by Zabbix server.  
  
For the rest of the parameters, see Testing hypothetical value above.