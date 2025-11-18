---
title: Additional JavaScript objects
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/javascript/javascript_objects
downloaded: 2025-11-14 10:34:51
---

# 1 Additional JavaScript objects

### Overview

This section describes Zabbix additions to the JavaScript language implemented with Duktape, and supported global JavaScript functions.

Do not use undeclared assignments in preprocessing JavaScript. Use `var` to declare local variables.

### Built-in objects

#### Zabbix

The Zabbix object provides interaction with the internal Zabbix functionality.

`log(loglevel, message)` | Writes <message> into Zabbix log using <loglevel> log level (see configuration file DebugLevel parameter).  
---|---  
  
Example:
    
    
    Zabbix.log(3, "this is a log entry written with 'Warning' log level")

Copy

✔ Copied

You may use the following aliases:

console.log(object) | Zabbix.log(4, JSON.stringify(object))  
---|---  
console.warn(object) | Zabbix.log(3, JSON.stringify(object))  
console.error(object) | Zabbix.log(2, JSON.stringify(object))  
  
The total size of all logged messages is limited to 8 MB per script execution.

`sleep(delay)` | Delay JavaScript execution by `delay` milliseconds.  
---|---  
  
Example (delay execution by 15 seconds):
    
    
    Zabbix.sleep(15000)

Copy

✔ Copied

#### HttpRequest

This object encapsulates cURL handle allowing to make simple HTTP requests. Errors are thrown as exceptions.

The initialization of multiple `HttpRequest` objects is limited to 10 per script execution.

`addHeader(value)` | Adds HTTP header field. This field is used for all following requests until cleared with the `clearHeader()` method.  
The total length of header fields that can be added to a single `HttpRequest` object is limited to 128 Kbytes (special characters and header names included).  
---|---  
`clearHeader()` | Clears HTTP header. If no header fields are set, `HttpRequest` will set Content-Type to application/json if the data being posted is JSON-formatted; text/plain otherwise.  
`connect(url)` | Sends HTTP CONNECT request to the URL and returns the response.  
`customRequest(method, url, data)` | Allows to specify any HTTP method in the first parameter. Sends the method request to the URL with optional _data_ payload and returns the response.  
`delete(url, data)` | Sends HTTP DELETE request to the URL with optional _data_ payload and returns the response.  
`getHeaders(<asArray>)` | Returns the object of received HTTP header fields.  
The `asArray` parameter may be set to "true" (e.g., `getHeaders(true)`), "false" or be undefined. If set to "true", the received HTTP header field values will be returned as arrays; this should be used to retrieve the field values of multiple same-name headers.  
If not set or set to "false", the received HTTP header field values will be returned as strings.  
`get(url, data)` | Sends HTTP GET request to the URL with optional _data_ payload and returns the response.  
`head(url)` | Sends HTTP HEAD request to the URL and returns the response.  
`options(url)` | Sends HTTP OPTIONS request to the URL and returns the response.  
`patch(url, data)` | Sends HTTP PATCH request to the URL with optional _data_ payload and returns the response.  
`put(url, data)` | Sends HTTP PUT request to the URL with optional _data_ payload and returns the response.  
`post(url, data)` | Sends HTTP POST request to the URL with optional _data_ payload and returns the response.  
`getStatus()` | Returns the status code of the last HTTP request.  
`setProxy(proxy)` | Sets HTTP proxy to "proxy" value. If this parameter is empty, then no proxy is used.  
`setHttpAuth(bitmask, username, password)` | Sets enabled HTTP authentication methods (HTTPAUTH_BASIC, HTTPAUTH_DIGEST, HTTPAUTH_NEGOTIATE, HTTPAUTH_NTLM, HTTPAUTH_NONE) in the 'bitmask' parameter.  
The HTTPAUTH_NONE flag allows to disable HTTP authentication.  
Examples:  
`request.setHttpAuth(HTTPAUTH_NTLM | HTTPAUTH_BASIC, username, password)`  
`request.setHttpAuth(HTTPAUTH_NONE)`  
`trace(url, data)` | Sends HTTP TRACE request to the URL with optional _data_ payload and returns the response.  
  
Example:
    
    
    try {
               Zabbix.log(4, 'jira webhook script value='+value);
             
               var result = {
                   'tags': {
                       'endpoint': 'jira'
                   }
               },
               params = JSON.parse(value),
               req = new HttpRequest(),
               fields = {},
               resp;
             
               req.addHeader('Content-Type: application/json');
               req.addHeader('Authorization: Basic '+params.authentication);
             
               fields.summary = params.summary;
               fields.description = params.description;
               fields.project = {"key": params.project_key};
               fields.issuetype = {"id": params.issue_id};
               resp = req.post('https://jira.example.com/rest/api/2/issue/',
                   JSON.stringify({"fields": fields})
               );
             
               if (req.getStatus() != 201) {
                   throw 'Response code: '+req.getStatus();
               }
             
               resp = JSON.parse(resp);
               result.tags.issue_id = resp.id;
               result.tags.issue_key = resp.key;
           } catch (error) {
               Zabbix.log(4, 'jira issue creation failed json : '+JSON.stringify({"fields": fields}));
               Zabbix.log(4, 'jira issue creation failed : '+error);
             
               result = {};
           }
             
           return JSON.stringify(result);

Copy

✔ Copied

#### XML

The XML object allows the processing of XML data in the item and low-level discovery preprocessing and webhooks.

In order to use XML object, server/proxy must be compiled with libxml2 support.

`XML.query(data, expression)` | Retrieves node content using XPath. Returns null if node is not found.  
**expression** \- an XPath expression;  
**data** \- XML data as a string.  
---|---  
`XML.toJson(data)` | Converts data in XML format to JSON.  
`XML.fromJson(object)` | Converts data in JSON format to XML.  
  
Example:

_Input:_
    
    
    <menu>
               <food type = "breakfast">
                   <name>Chocolate</name>
                   <price>$5.95</price>
                   <description></description>
                   <calories>650</calories>
               </food>
           </menu>

Copy

✔ Copied

_Output:_
    
    
    {
               "menu": {
                   "food": {
                       "@type": "breakfast",
                       "name": "Chocolate",
                       "price": "$5.95",
                       "description": null,
                       "calories": "650"
                   }
               }
           }

Copy

✔ Copied

##### Serialization rules

XML to JSON conversion will be processed according to the following rules (for JSON to XML conversions reversed rules are applied):

1\. XML attributes will be converted to keys that have their names prepended with '@'.

Example:

_Input:_
    
    
    <xml foo="FOO">
             <bar>
               <baz>BAZ</baz>
             </bar>
           </xml>

Copy

✔ Copied

_Output:_
    
    
    {
             "xml": {
               "@foo": "FOO",
               "bar": {
                 "baz": "BAZ"
               }
             }
           }

Copy

✔ Copied

2\. Self-closing elements (<foo/>) will be converted as having 'null' value.

Example:

_Input:_
    
    
    <xml>
             <foo/>
           </xml>

Copy

✔ Copied

_Output:_
    
    
    {
             "xml": {
               "foo": null
             }
           }

Copy

✔ Copied

3\. Empty attributes (with "" value) will be converted as having empty string ('') value.

Example:

_Input:_
    
    
    <xml>
             <foo bar="" />
           </xml>

Copy

✔ Copied

_Output:_
    
    
    {
             "xml": {
               "foo": {
                 "@bar": ""
               }
             }
           }

Copy

✔ Copied

4\. Multiple child nodes with the same element name will be converted to a single key that has an array of values as its value.

Example:

_Input:_
    
    
    <xml>
             <foo>BAR</foo>
             <foo>BAZ</foo>
             <foo>QUX</foo>
           </xml>

Copy

✔ Copied

_Output:_
    
    
    {
             "xml": {
               "foo": ["BAR", "BAZ", "QUX"]
             }
           }

Copy

✔ Copied

5\. If a text element has no attributes and no children, it will be converted as a string.

Example:

_Input:_
    
    
    <xml>
               <foo>BAZ</foo>
           </xml>

Copy

✔ Copied

_Output:_
    
    
    {
             "xml": {
               "foo": "BAZ"
              }
           }

Copy

✔ Copied

6\. If a text element has no children but has attributes, text content will be converted to an element with the key '#text' and content as a value; attributes will be converted as described in the serialization rule 1.

Example:

_Input:_
    
    
    <xml>
             <foo bar="BAR">
               BAZ
             </foo>
           </xml>

Copy

✔ Copied

_Output:_
    
    
    {
             "xml": {
               "foo": {
                 "@bar": "BAR",
                 "#text": "BAZ"
               }
             }
           }

Copy

✔ Copied

### Global JavaScript functions

Additional global JavaScript functions have been implemented with Duktape:

  * btoa(data) - encodes the data to base64 string;
  * atob(base64_string) - decodes base64 string as Uint8Array buffer.

    
    
    try {
               b64 = btoa("test string");
               buffer = atob(b64);
           
               // Note that decoding logic depends on the data format of the buffer.
               decoded = String.fromCharCode.apply(this, [].slice.call(buffer));
           } 
           catch (error) {
               return {'error.name' : error.name, 'error.message' : error.message};
           }

Copy

✔ Copied

  * md5(data) - calculates the MD5 hash of the data

  * sha256(data) - calculates the SHA256 hash of the data

  * hmac('<hash type>',key,data) - returns HMAC hash as hex formatted string; MD5 and SHA256 hash types are supported; key and data parameters support binary data. Examples:

    * `hmac('md5',key,data)`
    * `hmac('sha256',key,data)`
  * sign(hash,key,data) - returns calculated signature (RSA signature with SHA-256) as a string, where:  
**hash** \- only 'sha256' is allowed, otherwise an error is thrown;  
**key** \- the private key. It should correspond to PKCS#1 or PKCS#8 standard. The key can be provided in different forms:  

    * with spaces instead of newlines;
    * with escaped or non-escaped `\n` instead of newlines;
    * without any newlines as a single-line string;
    * as a JSON-formatted string.

The key also can be loaded from a user macro/secret macro/vault.

**data** \- the data that will be signed. It can be a string (binary data also supported) or buffer (Uint8Array/ArrayBuffer).  
OpenSSL or GnuTLS is used to calculate the signatures. If Zabbix was built without any of these encryption libraries, an error will be thrown ('missing OpenSSL or GnuTLS library').