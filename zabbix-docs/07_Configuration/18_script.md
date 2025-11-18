---
title: Script items
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/script
downloaded: 2025-11-14 10:35:19
---

# 18 Script items  
  
### Overview

Script items can be used to collect data by executing a user-defined JavaScript code with the ability to retrieve data over HTTP/HTTPS. In addition to the script, an optional list of parameters (pairs of name and value) and timeout can be specified.

This item type may be useful in data collection scenarios that require multiple steps or complex logic. As an example, a Script item can be configured to make an HTTP call, then process the data received in the first step in some way, and pass transformed value to the second HTTP call.

Script items are processed by Zabbix server or proxy pollers.

### Configuration

In the _Type_ field of [item configuration form](/documentation/current/en/manual/config/items/item) select Script then fill out required fields.

![script_item.png](/documentation/current/assets/en/manual/config/items/itemtypes/script_item.png)

All mandatory input fields are marked with a red asterisk.

The fields that require specific information for Script items are:

_Key_ | Enter a unique key that will be used to identify the item.  
---|---  
_Parameters_ | Specify the variables to be passed to the script as the attribute and value pairs.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported. To see which built-in macros are supported, do a search for "Script-type item" in the [supported macro](/documentation/current/en/manual/appendix/macros/supported_by_location) table.  
_Script_ | Enter JavaScript code in the modal editor that opens when clicking in the parameter field or on the pencil icon next to it. This code must provide the logic for returning the metric value.  
The code has access to all parameters and all [additional JavaScript objects](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects) added by Zabbix.  
See also: [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide).  
_Timeout_ | JavaScript execution timeout (1-600s; exceeding it will return an error).  
Note that depending on the script, it might take longer for the timeout to trigger.  
For more information on the _Timeout_ parameter, see [general item attributes](/documentation/current/en/manual/config/items/item#configuration).  
  
### Examples

##### Simple data collection

Collect the content of _https://www.example.com/release_notes_ :

  * Create an item with type "Script".
  * In the _Script_ field, enter:

    
    
    var request = new HttpRequest();
           return request.get("https://www.example.com/release_notes");

Copy

✔ Copied

##### Data collection with parameters

Collect the content of a specific page and make use of parameters:

  * Create an item with type "Script" and two parameters: 
    * **url : {$DOMAIN}** (the user macro {$DOMAIN} should be defined, preferably on the host level)
    * **subpage : /release_notes**

![](/documentation/current/assets/en/manual/config/items/itemtypes/script_example1.png)

  * In the _Script_ field, enter:

    
    
    var obj = JSON.parse(value);
           var url = obj.url;
           var subpage = obj.subpage;
           var request = new HttpRequest();
           return request.get(url + subpage);

Copy

✔ Copied

##### Multiple HTTP requests

Collect the content of both _https://www.example.com_ and _https://www.example.com/release_notes_ :

  * Create an item with type "Script".
  * In the _Script_ field, enter:

    
    
    var request = new HttpRequest();
           return request.get("https://www.example.com") + request.get("https://www.example.com/release_notes");

Copy

✔ Copied

##### Logging

Add the "Log test" entry to the Zabbix server log and receive the item value "1" in return:

  * Create an item with type "Script".
  * In the _Script_ field, enter:

    
    
    Zabbix.log(3, 'Log test');
           return 1;

Copy

✔ Copied