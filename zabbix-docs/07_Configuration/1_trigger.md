---
title: Configuring a trigger
source: https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger
downloaded: 2025-11-14 10:35:32
---

# 1 Configuring a trigger

#### Overview

To configure a trigger, do the following:

  * Go to: _Data collection_ → _Hosts_
  * Click on _Triggers_ in the row of the host
  * Click on _Create trigger_ to the right (or on the trigger name to edit an existing trigger)
  * Enter parameters of the trigger in the form

See also [general information](/documentation/current/en/manual/config/triggers) on triggers and their calculation times.

#### Configuration

The **Trigger** tab contains all the essential trigger attributes.

![](/documentation/current/assets/en/manual/config/triggers/trigger.png)

All mandatory input fields are marked with a red asterisk.

_Name_ | Trigger name.  
Supported [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are: {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {HOST.CONN}, {HOST.DNS}, {HOST.IP}, {HOST.PORT}, {ITEM.VALUE}, {ITEM.VALUE.AGE}, {ITEM.VALUE.DATE}, {ITEM.VALUE.TIME}, {ITEM.VALUE.TIMESTAMP}, {ITEM.LASTVALUE}, {ITEM.LASTVALUE.AGE}, {ITEM.LASTVALUE.DATE}, {ITEM.LASTVALUE.TIME}, {ITEM.LASTVALUE.TIMESTAMP}, {ITEM.LOG.*} and {$MACRO} user macros.  
**$1, $2...$9** macros can be used to refer to the first, second...ninth constant of the expression.  
_Note_ : $1-$9 macros will resolve correctly if referring to constants in relatively simple, straightforward expressions. For example, the name "Processor load above $1 on {HOST.NAME}" will automatically change to "Processor load above 5 on New host" if the expression is last(/New host/system.cpu.load[percpu,avg1])>5  
---|---  
_Event name_ | If defined, this name will be used to create the problem event name, instead of the trigger name.  
The event name may be used to build meaningful alerts containing problem data (see [example](/documentation/current/en/manual/config/triggers/expression#example-18)).  
The same set of macros is supported as in the trigger name, plus {TIME}, {TIMESTAMP}, and {?EXPRESSION} expression macros.  
_Operational data_ | Operational data allow to define arbitrary strings along with macros. The macros will resolve dynamically to real time data in _Monitoring_ → _[Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems)_. While macros in the trigger name (see above) will resolve to their values at the moment of a problem happening and will become the basis of a static problem name, the macros in the operational data maintain the ability to display the very latest information dynamically. If no operational data is configured on a trigger level, the latest values of all items from the expression will be displayed.  
The same set of macros is supported as in the trigger name.  
_Severity_ | Set the required trigger [severity](severity) by clicking the buttons.  
_Expression_ | Logical [expression](expression) used to define the conditions of a problem.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes#time-suffixes) and [memory size suffixes](/documentation/current/en/manual/appendix/suffixes#memory-size-suffixes) are supported.  
A problem is created after all the conditions included in the expression are met, i.e. the expression evaluates to TRUE. The problem will be resolved as soon as the expression evaluates to FALSE, unless additional recovery conditions are specified in _Recovery expression_.  
_OK event generation_ | OK event generation options:  
**Expression** \- OK events are generated based on the same expression as problem events;  
**Recovery expression** \- OK events are generated if the problem expression evaluates to FALSE and the recovery expression evaluates to TRUE;  
**None** \- in this case the trigger will never return to an OK state on its own.  
_Recovery expression_ | Logical [expression](expression) (optional) defining additional conditions that have to be met before the problem is resolved, after the original problem expression has already been evaluated as FALSE.  
Recovery expression is useful for trigger [hysteresis](/documentation/current/en/manual/config/triggers/expression#hysteresis). It is **not** possible to resolve a problem by recovery expression alone if the problem expression is still TRUE.  
This field is only available if 'Recovery expression' is selected for _OK event generation_.  
_PROBLEM event generation mode_ | Mode for generating problem events:  
**Single** \- a single event is generated when a trigger goes into the 'Problem' state for the first time;  
**Multiple** \- an event is generated upon _every_ 'Problem' evaluation of the trigger.  
_OK event closes_ | Select if OK event closes:  
**All problems** \- all problems of this trigger  
**All problems if tag values match** \- only those trigger problems with matching event tag values  
_Tag for matching_ | Enter event tag name to use for event correlation.  
This field is displayed if 'All problems if tag values match' is selected for the _OK event closes_ property and is mandatory in this case.  
_Allow manual close_ | Check to allow [manual closing](/documentation/current/en/manual/config/events/manual_close) of problem events generated by this trigger. Manual closing is possible when acknowledging problem events.  
_Menu entry name_ | If not empty, the name entered here (up to 64 characters) is used in several frontend locations as a label for the trigger URL specified in the _Menu entry URL_ parameter. If empty, the default name _Trigger URL_ is used.  
The same set of macros is supported as in the trigger URL.  
_Menu entry URL_ | If not empty, the URL entered here (up to 2048 characters) is available as a link in the [event menu](/documentation/current/en/manual/web_interface/menu/event_menu) in several frontend locations, for example, when clicking on the problem name in _Monitoring →[Problems](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems)_ or _[Problems](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/problems#using-the-widget)_ dashboard widget.  
The same set of macros is supported as in the trigger name, plus {EVENT.ID}, {HOST.ID} and {TRIGGER.ID}. Note: user macros with secret values will not be resolved in the URL.  
_Description_ | Text field used to provide more information about this trigger. May contain instructions for fixing specific problem, contact detail of responsible staff, etc.  
The same set of macros is supported as in the trigger name.  
_Enabled_ | Unchecking this box will disable the trigger if required.  
Problems of a disabled trigger are no longer displayed in the frontend, but are not deleted.  
  
The **Tags** tab allows you to define trigger-level [tags](/documentation/current/en/manual/config/tagging). All problems of this trigger will be tagged with the values entered here.

![](/documentation/current/assets/en/manual/config/triggers/trigger_b.png)

In addition, the _Inherited and trigger tags_ option allows you to view tags defined on the template level if the trigger comes from that template. If there are multiple templates with the same tag, these tags are displayed once and template names are separated by commas. A trigger does not "inherit" and display host-level tags.

_Name/Value_ | Set custom tags to mark trigger events.  
Tags are a pair of tag name and value. You can use only the name or pair it with a value. A trigger may have several tags with the same name, but different values.  
User macros, user macros with context, low-level discovery macros and macro [functions](/documentation/current/en/manual/config/macros/macro_functions) with `{{ITEM.VALUE}}`, `{{ITEM.LASTVALUE}}` and low-level discovery macros are supported in event tags. Low-level discovery macros can be used inside macro context.  
{TRIGGER.ID} macro is supported in trigger tag values. It may be useful for identifying triggers created from trigger prototypes and, for example, suppressing problems from these triggers during maintenance.  
If the total length of expanded value exceeds 255, it will be cut to 255 characters.  
See all [macros](/documentation/current/en/manual/config/tagging#macro-support) supported for event tags.  
[Event tags](/documentation/current/en/manual/config/tagging) can be used for event correlation, in action conditions and will also be seen in _Monitoring_ → _Problems_ or the _Problems_ widget.  
---|---  
  
The **Dependencies** tab contains all the [dependencies](dependencies) of the trigger.

Click on _Add_ to add a new dependency.

You can also configure a trigger by opening an existing one, pressing the _Clone_ button and then saving under a different name.

#### Testing expressions

It is possible to test the configured trigger expression as to what the expression result would be depending on the received value.

The following expression from an official template is taken as an example:
    
    
    avg(/Cisco IOS SNMPv2/sensor.temp.value[ciscoEnvMonTemperatureValue.{#SNMPINDEX}],5m)>{$TEMP_WARN}
           or
           last(/Cisco IOS SNMPv2/sensor.temp.status[ciscoEnvMonTemperatureState.{#SNMPINDEX}])={$TEMP_WARN_STATUS}

Copy

✔ Copied

To test the expression, click on _Expression constructor_ under the expression field.

![](/documentation/current/assets/en/manual/config/triggers/trigger_test.png)

In the Expression constructor, all individual expressions are listed. To open the testing window, click on _Test_ below the expression list.

![](/documentation/current/assets/en/manual/config/triggers/expr_test_button.png)

In the testing window you can enter sample values ('80', '70', '0', '1' in this example) and then see the expression result, by clicking on the _Test_ button.

![](/documentation/current/assets/en/manual/config/triggers/expr_test.png)

The result of the individual expressions as well as the whole expression can be seen.

"TRUE" means that the specified expression is correct. In this particular case A, "80" is greater than the {$TEMP_WARN} specified value, "70" in this example. As expected, a "TRUE" result appears.

"FALSE" means that the specified expression is incorrect. In this particular case B, {$TEMP_WARN_STATUS} "1" needs to be equal with specified value, "0" in this example. As expected, a "FALSE" result appears.

The chosen expression type is "OR". If at least one of the specified conditions (A or B in this case) is TRUE, the overall result will be TRUE as well. Meaning that the current value exceeds the warning value and a problem has occurred.