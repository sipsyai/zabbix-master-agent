---
title: JavaScript preprocessing
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/javascript
downloaded: 2025-11-14 10:34:50
---

# 5 JavaScript preprocessing  
  
### Overview

This section provides details of preprocessing by JavaScript.

Do not use undeclared assignments in preprocessing JavaScript. Use `var` to declare local variables.

### JavaScript preprocessing

JavaScript preprocessing is done by invoking JavaScript function with a single parameter 'value' and user-provided function body. The preprocessing step result is the value returned by this function, for example, to perform Fahrenheit to Celsius conversion, enter:
    
    
    return (value - 32)  * 5 / 9

Copy

✔ Copied

in JavaScript preprocessing parameters, which will be wrapped into a JavaScript function by server:
    
    
    function (value)
           {
              return (value - 32) * 5 / 9
           }

Copy

✔ Copied

The input parameter 'value' is always passed as a string. The return value is automatically coerced to string via toString() method (if it fails, then the error is returned as string value), with a few exceptions:

  * returning undefined value will result in an error;
  * returning null value will cause the input value to be discarded, much like 'Discard value' preprocessing on 'Custom on fail' action.

Errors can be returned by throwing values/objects (normally either strings or Error objects).

For example:
    
    
    if (value == 0)
               throw "Zero input value"
           return 1/value

Copy

✔ Copied

Each script has a 10-second execution timeout (depending on the script, it might take longer for the timeout to trigger); exceeding it will return error. A 512-megabyte heap limit is enforced.

The JavaScript preprocessing step bytecode is cached and reused when the step is applied next time. Any changes to the item's preprocessing steps will cause the cached script to be reset and recompiled later.

Consecutive runtime failures (3 in a row) will cause the engine to be reinitialized to mitigate the possibility of one script breaking the execution environment for the next scripts (this action is logged with DebugLevel 4 and higher).

JavaScript preprocessing is implemented with [Duktape](https://duktape.org/) JavaScript engine.

See also: [Additional JavaScript objects and global functions](/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects)

##### Using macros in scripts

It is possible to use user macros in JavaScript code. If a script contains user macros, these macros are resolved by server/proxy before executing specific preprocessing steps. Note that when testing preprocessing steps in the frontend, macro values will not be pulled and need to be entered manually.

Context is ignored when a macro is replaced with its value. Macro value is inserted in the code as is, it is not possible to add additional escaping before placing the value in the JavaScript code. Please be advised that this can cause JavaScript errors in some cases.

In an example below, if received value exceeds a {$THRESHOLD} macro value, the threshold value (if present) will be returned instead:
    
    
    var threshold = '{$THRESHOLD}';
           return (!isNaN(threshold) && value > threshold) ? threshold : value;

Copy

✔ Copied

### Examples

The following examples illustrate how you can use JavaScript preprocessing.

Each example contains a brief description, a function body for JavaScript preprocessing parameters, and the preprocessing step result - value returned by the function.

##### Example 1: Convert a number (scientific notation to integer)

Convert the number "2.62128e+07" from scientific notation to an integer.
    
    
    return (Number(value))

Copy

✔ Copied

Value returned by the function: 26212800.

##### Example 2: Convert a number (binary to decimal)

Convert the binary number "11010010" to a decimal number.
    
    
    return(parseInt(value,2))

Copy

✔ Copied

Value returned by the function: 210.

##### Example 3: Round a number

Round the number "18.2345" to 2 digits.
    
    
    return(Math.round(value* 100) / 100)

Copy

✔ Copied

Value returned by the function: 18.23.

##### Example 4: Count letters in a string

Count the number of letters in the string "Zabbix".
    
    
    return (value.length)

Copy

✔ Copied

Value returned by the function: 6.

##### Example 5: Get time remaining

Get the remaining time (in seconds) until the expiration date of a certificate (Feb 12 12:33:56 2022 GMT).
    
    
    var split = value.split(' '),
               MONTHS_LIST = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
               month_index = ('0' + (MONTHS_LIST.indexOf(split[0]) + 1)).slice(-2),
               ISOdate = split[3] + '-' + month_index + '-' + split[1] + 'T' + split[2],
               now = Date.now();
           
           return parseInt((Date.parse(ISOdate) - now) / 1000);

Copy

✔ Copied

Value returned by the function: 44380233.

##### Example 6: Remove JSON properties

Modify the JSON data structure by removing any properties with the key `"data_size"` or `"index_size"`.
    
    
    var obj=JSON.parse(value);
           
           for (i = 0; i < Object.keys(obj).length; i++) {
               delete obj[i]["data_size"];
               delete obj[i]["index_size"];
           }
           
           return JSON.stringify(obj)

Copy

✔ Copied

Value accepted by the function:
    
    
    [
               {
                   "table_name":"history",
                   "data_size":"326.05",
                   "index_size":"174.34"
               },
               {
                   "table_name":"history_log",
                   "data_size":"6.02",
                   "index_size":"3.45"
               }
           ]

Copy

✔ Copied

Value returned by the function:
    
    
    [
               {
                   "table_name":"history"
               },
               {
                   "table_name":"history_log"
               }
           ]

Copy

✔ Copied

##### Example 7: Convert Apache status to JSON

Convert the value received from a [web.page.get](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#web.page.gethostpathport) Zabbix agent item (e.g., web.page.get[http://127.0.0.1:80/server-status?auto]) to a JSON object.
    
    
    // Convert Apache status to JSON
           
           // Split the value into substrings and put these substrings into an array
           var lines = value.split('\n');
           
           // Create an empty object "output"
           var output = {};
           
           // Create an object "workers" with predefined properties
           var workers = {
               '_': 0, 'S': 0, 'R': 0, 'W': 0,
               'K': 0, 'D': 0, 'C': 0, 'L': 0,
               'G': 0, 'I': 0, '.': 0
           };
           
           // Add the substrings from the "lines" array to the "output" object as properties (key-value pairs)
           for (var i = 0; i < lines.length; i++) {
               var line = lines[i].match(/([A-z0-9 ]+): (.*)/);
           
               if (line !== null) {
                   output[line[1]] = isNaN(line[2]) ? line[2] : Number(line[2]);
               }
           }
           
           // Multiversion metrics
           output.ServerUptimeSeconds = output.ServerUptimeSeconds || output.Uptime;
           output.ServerVersion = output.ServerVersion || output.Server;
           
           // Parse "Scoreboard" property to get the worker count
           if (typeof output.Scoreboard === 'string') {
               for (var i = 0; i < output.Scoreboard.length; i++) {
                   var char = output.Scoreboard[i];
           
                   workers[char]++;
               }
           }
           
           // Add worker data to the "output" object
           output.Workers = {
               waiting: workers['_'], starting: workers['S'], reading: workers['R'],
               sending: workers['W'], keepalive: workers['K'], dnslookup: workers['D'],
               closing: workers['C'], logging: workers['L'], finishing: workers['G'],
               cleanup: workers['I'], slot: workers['.']
           };
           
           // Return JSON string
           return JSON.stringify(output);

Copy

✔ Copied

Value accepted by the function:
    
    
    HTTP/1.1 200 OK
           Date: Mon, 27 Mar 2023 11:08:39 GMT
           Server: Apache/2.4.52 (Ubuntu)
           Vary: Accept-Encoding
           Content-Encoding: gzip
           Content-Length: 405
           Content-Type: text/plain; charset=ISO-8859-1
           
           127.0.0.1
           ServerVersion: Apache/2.4.52 (Ubuntu)
           ServerMPM: prefork
           Server Built: 2023-03-08T17:32:01
           CurrentTime: Monday, 27-Mar-2023 14:08:39 EEST
           RestartTime: Monday, 27-Mar-2023 12:19:59 EEST
           ParentServerConfigGeneration: 1
           ParentServerMPMGeneration: 0
           ServerUptimeSeconds: 6520
           ServerUptime: 1 hour 48 minutes 40 seconds
           Load1: 0.56
           Load5: 0.33
           Load15: 0.28
           Total Accesses: 2476
           Total kBytes: 8370
           Total Duration: 52718
           CPUUser: 8.16
           CPUSystem: 3.44
           CPUChildrenUser: 0
           CPUChildrenSystem: 0
           CPULoad: .177914
           Uptime: 6520
           ReqPerSec: .379755
           BytesPerSec: 3461.58
           BytesPerReq: 3461.58
           DurationPerReq: 21.2916
           BusyWorkers: 2
           IdleWorkers: 6
           Scoreboard: ____KW__..............................................................................................................................................

Copy

✔ Copied

Value returned by the function:
    
    
    {
               "Date": "Mon, 27 Mar 2023 11:08:39 GMT",
               "Server": "Apache/2.4.52 (Ubuntu)",
               "Vary": "Accept-Encoding",
               "Encoding": "gzip",
               "Length": 405,
               "Type": "text/plain; charset=ISO-8859-1",
               "ServerVersion": "Apache/2.4.52 (Ubuntu)",
               "ServerMPM": "prefork",
               "Server Built": "2023-03-08T17:32:01",
               "CurrentTime": "Monday, 27-Mar-2023 14:08:39 EEST",
               "RestartTime": "Monday, 27-Mar-2023 12:19:59 EEST",
               "ParentServerConfigGeneration": 1,
               "ParentServerMPMGeneration": 0,
               "ServerUptimeSeconds": 6520,
               "ServerUptime": "1 hour 48 minutes 40 seconds",
               "Load1": 0.56,
               "Load5": 0.33,
               "Load15": 0.28,
               "Total Accesses": 2476,
               "Total kBytes": 8370,
               "Total Duration": 52718,
               "CPUUser": 8.16,
               "CPUSystem": 3.44,
               "CPUChildrenUser": 0,
               "CPUChildrenSystem": 0,
               "CPULoad": 0.177914,
               "Uptime": 6520,
               "ReqPerSec": 0.379755,
               "BytesPerSec": 1314.55,
               "BytesPerReq": 3461.58,
               "DurationPerReq": 21.2916,
               "BusyWorkers": 2,
               "IdleWorkers": 6,
               "Scoreboard": "____KW__..............................................................................................................................................",
               "Workers": {
                   "waiting": 6,
                   "starting": 0,
                   "reading": 0,
                   "sending": 1,
                   "keepalive": 1,
                   "dnslookup": 0,
                   "closing": 0,
                   "logging": 0,
                   "finishing": 0,
                   "cleanup": 0,
                   "slot": 142
               }
           }

Copy

✔ Copied