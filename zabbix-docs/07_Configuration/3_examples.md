---
title: Preprocessing examples
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/examples
downloaded: 2025-11-14 10:34:47
---

# 3 Preprocessing examples

#### Overview

This section presents examples of using preprocessing steps to accomplish some practical tasks.

#### Filtering VMware event log records

This example uses the [Matches regular expression](/documentation/current/en/manual/config/items/preprocessing#matchesregexp) preprocessing step to filter unnecessary events from the VMware event log.

1\. On a working VMware Hypervisor host, check that the [vmware.eventlog](/documentation/current/en/manual/vm_monitoring/vmware_keys#vmware.eventlog) item is present and working properly. Note that the event log item could already be present on the hypervisor if a [VMware](/documentation/current/en/manual/config/templates_out_of_the_box/vmware) template has been linked during the host creation.

2\. On the VMware Hypervisor host, create a [dependent item](/documentation/current/en/manual/config/items/itemtypes/dependent_items) of _Log_ type and set the event log item as its master item.

3\. In the _Preprocessing_ tab of the dependent item, click _Add_ to create a preprocessing step and select _Matches regular expression_ from the drop-down. Then, specify one of the following patterns:

  * For filtering all log events:

    
    
    .* logged in .*

Copy

✔ Copied

  * For filtering lines containing usernames after "User":

    
    
    \bUser\s+\K\S+

Copy

✔ Copied

If the regular expression is not matched, then the dependent item becomes unsupported with a corresponding error message. To avoid this, mark the _Custom on fail_ checkbox and select an option such as discarding the value or setting a custom one. Please note that [discarded](/documentation/current/en/manual/config/items/preprocessing#discardunchanged) values are not stored in the database; as a result, triggers are not evaluated and trend data is not generated.

Alternatively, you may use the [Regular expression](/documentation/current/en/manual/config/items/preprocessing#regexp) preprocessing step to extract matching groups and control output:

  * For extracting and outputting the entire log event containing "logged in", specify the following parameters:

    
    
    Pattern: .*logged in.*
           Output: \0

Copy

✔ Copied

  * For extracting and outputting usernames following "User":

    
    
    Pattern: User (.*?)(?=\ )
           Output: \1

Copy

✔ Copied

#### Checking retrieved value type

This example uses the [Custom multiplier](/documentation/current/en/manual/config/items/preprocessing#multiplier) preprocessing step to check if the retrieved item value type is numeric.

In the _Preprocessing_ tab of an item, select the _Custom multiplier_ preprocessing step and specify the following parameter (multiplies the retrieved value by 1):
    
    
    1

Copy

✔ Copied

If preprocessing fails (e.g., input is not numeric), then the item becomes unsupported with a corresponding error message. To avoid this, mark the _Custom on fail_ checkbox and select an option such as discarding the value or setting a custom one. Please note that [discarded](/documentation/current/en/manual/config/items/preprocessing#discardunchanged) values are not stored in the database; as a result, triggers are not evaluated and trend data is not generated.

#### Checking for not supported value

This example uses the [Check for not supported value](/documentation/current/en/manual/config/items/preprocessing#checkunsupported) preprocessing step to check if the item value could not be retrieved.

When a Zabbix server/proxy poller process attempts to collect an item value, it may:

  * Return a valid result.
  * Return a result that initially seems valid but may become unsupported later (e.g., due to a value type mismatch after preprocessing).
  * Return an error of collecting the value, causing the item to become unsupported. Common causes include: 
    * Unknown item key (for Zabbix agent, Simple check, or Zabbix internal items)
    * Unknown OID (SNMP agent), unknown sensor (IPMI agent), or no JMX metric (JMX agent)
    * Cannot read trap file (SNMP trap)
    * Script not found (External check)
    * No such URL (HTTP agent, Browser)
    * Login failed (SSH agent, TELNET agent)
    * Invalid formula syntax (Calculated), JavaScript syntax error (Script), or invalid SQL (Database monitor)

To detect and handle errors of collecting item values, you can use the _Check for not supported value_ preprocessing step. Note that this step is always executed first and only detects errors that occur before preprocessing begins.

In the _Preprocessing_ tab of an item, select the _Check for not supported value_ preprocessing step and specify one of the following parameters:

  * For any errors:

    
    
    Parameter: any error

Copy

✔ Copied

  * For errors containing "cannot connect":

    
    
    Parameter: error matches
           Pattern: (?i)cannot connect

Copy

✔ Copied

Then, use the _Custom on fail_ option to discard the value (in this case, the error), set a custom value, or return a custom error message. Please note that [discarded](/documentation/current/en/manual/config/items/preprocessing#discardunchanged) values are not stored in the database; as a result, triggers are not evaluated and trend data is not generated.