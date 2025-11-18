---
title: Web monitoring
source: https://www.zabbix.com/documentation/current/en/manual/web_monitoring
downloaded: 2025-11-14 10:36:53
---

# 9 Web monitoring

#### Overview

With Zabbix you can check several availability aspects of web sites.  

To perform web monitoring Zabbix server must be initially [configured](/documentation/current/en/manual/installation/install#from-the-sources) with cURL (libcurl) support.

To activate web monitoring you need to define web scenarios. A web scenario consists of one or several HTTP requests or "steps". The steps are periodically executed by Zabbix server in a pre-defined order. If a host is monitored by proxy, the steps are executed by the proxy.

Web scenarios are attached to hosts/templates in the same way as items, triggers, etc. That means that web scenarios can also be created on a template level and then applied to multiple hosts in one move.

The following information is collected in any web scenario:

  * average download speed per second for all steps of whole scenario
  * number of the step that failed
  * last error message

The following information is collected in any web scenario step:

  * download speed per second
  * response time
  * response code

For more details, see [web monitoring items](/documentation/current/en/manual/web_monitoring/items).

Data collected from executing web scenarios is kept in the database. The data is automatically used for graphs, triggers and notifications.

Zabbix can also check if a retrieved HTML page contains a pre-defined string. It can execute a simulated login and follow a path of simulated mouse clicks on the page.

Zabbix web monitoring supports both HTTP and HTTPS. When running a web scenario, Zabbix will optionally follow redirects (see option _Follow redirects_ below). Maximum number of redirects is hard-coded to 10 (using cURL option [CURLOPT_MAXREDIRS](http://curl.haxx.se/libcurl/c/CURLOPT_MAXREDIRS.html)). All cookies are preserved during the execution of a single scenario.

#### Configuring a web scenario

To configure a web scenario:

  * Go to: _Data collection → Hosts_ (or _Templates_)
  * Click on _Web_ in the row of the host/template
  * Click on _Create web scenario_ to the right (or on the scenario name to edit an existing scenario)
  * Enter parameters of the scenario in the form

The **Scenario** tab allows you to configure the general parameters of a web scenario.

![](/documentation/current/assets/en/manual/config/scenario.png)

All mandatory input fields are marked with a red asterisk.

Scenario parameters:

_Name_ | Unique scenario name.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported. _Note_ that if user macros are used, these macros will be left unresolved in [web monitoring item](/documentation/current/en/manual/web_monitoring/items) names.  
---|---  
_Update interval_ | How often the scenario will be executed.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 30s, 1m, 2h, 1d.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported. _Note_ that if a user macro is used and its value is changed (e.g. 5m → 30s), the next check will be executed according to the previous value (farther in the future with the example values).   
New web scenarios will be checked within 60 seconds of their creation.  
_Attempts_ | The number of attempts for executing web scenario steps. In case of network problems (timeout, no connectivity, etc) Zabbix can repeat executing a step several times. The figure set will equally affect each step of the scenario. Up to 10 attempts can be specified, default value is 1.  
_Note_ : Zabbix will not repeat a step because of a wrong response code or the mismatch of a required string.  
_Agent_ | Select a client agent.  
Zabbix will pretend to be the selected browser. This is useful when a website returns different content for different browsers.  
User macros can be used in this field.  
_HTTP proxy_ | You can specify an HTTP proxy to use, using the format `[protocol://][username[:password]@]proxy.example.com[:port]`.  
This sets the [CURLOPT_PROXY](https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html) cURL option.  
The optional `protocol://` prefix may be used to specify alternative proxy protocols (the protocol prefix support was added in cURL 7.21.7). With no protocol specified, the proxy will be treated as an HTTP proxy.  
By default, 1080 port will be used.  
If specified, the proxy will overwrite proxy related environment variables like http_proxy, HTTPS_PROXY. If not specified, the proxy will not overwrite proxy-related environment variables. The entered value is passed on "as is", no sanity checking takes place.  
You may also enter a SOCKS proxy address. If you specify the wrong protocol, the connection will fail and the item will become unsupported.  
_Note_ that only simple authentication is supported with HTTP proxy.  
User macros can be used in this field.  
_Variables_ | Variables that may be used in scenario steps (URL, post variables).  
They have the following format:  
**{macro1}** =value1  
**{macro2}** =value2  
**{macro3}** =regex:<regular expression>  
**{macro4}** =jsonpath:<jsonpath>  
**{macro5}** =xmlxpath:<xmlxpath>  
**{macro6}** ={{macro}.function()} (see [macro functions](/documentation/current/en/manual/config/macros/macro_functions))  
For example:  
{username}=Alexei  
{password}=kj3h5kJ34bd  
{hostid}=regex:hostid is ([0-9]+)  
{url}=jsonpath:$.host_url  
{status}=xmlxpath://host/response/status  
{newvar}={{myvar}.btoa()}  
The macros can then be referenced in the steps as {username}, {password}, {hostid}, etc. Zabbix will automatically replace them with actual values. Note that variables with `regex:` need one step to get the value of the regular expression so the extracted value can only be applied to the step after.  
If the value part starts with `regex:` then the part after it is treated as a regular expression that searches the web page and, if found, stores the match in the variable. At least one subgroup must be present so that the matched value can be extracted.  
User macros and {HOST.*} [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported.  
Variables are automatically URL-encoded when used in query fields or form data for post variables, but must be URL-encoded manually when used in raw post or directly in URL.  
_Headers_ | HTTP Headers are used when performing a request. Default and custom headers can be used.  
Headers will be assigned using default settings depending on the Agent type selected from a drop-down list on a scenario level, and will be applied to all the steps, unless they are custom defined on a step level.  
**It should be noted that defining the header on a step level automatically discards all the previously defined headers, except for a default header that is assigned by selecting the 'User-Agent' from a drop-down list on a scenario level.**  
However, even the 'User-Agent' default header can be overridden by specifying it on a step level.  
To unset the header on a scenario level, the header should be named and attributed with no value on a step level.  
Headers should be listed using the same syntax as they would appear in the HTTP protocol, optionally using some additional features supported by the [CURLOPT_HTTPHEADER](http://curl.haxx.se/libcurl/c/CURLOPT_HTTPHEADER.html) cURL option.  
For example:  
Accept-Charset=utf-8  
Accept-Language=en-US  
Content-Type=application/xml; charset=utf-8  
User macros and {HOST.*} [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported.  
_Enabled_ | The scenario is active if this box is checked, otherwise - disabled.  
  
Note that when editing an existing scenario, two extra buttons are available in the form:

![](/documentation/current/assets/en/manual/web_monitoring/buttons_clone.png) | Create another scenario based on the properties of the existing one.  
---|---  
![](/documentation/current/assets/en/manual/web_monitoring/buttons_clear.png) | Delete history and trend data for the scenario. This will make the server perform the scenario immediately after deleting the data.  
  
If _HTTP proxy_ field is left empty, another way for using an HTTP proxy is to set proxy related environment variables.

For HTTP checks - set the **http_proxy** environment variable for the Zabbix server user. For example, `http_proxy=http://proxy_ip:proxy_port`.

For HTTPS checks - set the **HTTPS_PROXY** environment variable. For example, `HTTPS_PROXY=http://proxy_ip:proxy_port`. More details are available by running a shell command: _# man curl_.

The **Steps** tab allows you to configure the web scenario steps. To add a web scenario step, click on _Add_ in the _Steps_ block.

![](/documentation/current/assets/en/manual/config/scenario_b.png)

Secret [user macros](/documentation/current/en/manual/config/macros/user_macros#configuration) must not be used in URLs as they will resolve to "******".

#### Configuring steps

![](/documentation/current/assets/en/manual/config/scenario_step.png)

Step parameters:

_Name_ | Unique step name.  
[User macros](/documentation/current/en/manual/config/macros/user_macros) are supported. _Note_ that if user macros are used, these macros will be left unresolved in [web monitoring item](/documentation/current/en/manual/web_monitoring/items) names.  
---|---  
_URL_ | URL to connect to and retrieve data. For example:  
https://www.example.com  
http://www.example.com/download  
Domain names can be specified in Unicode characters. They are automatically punycode-converted to ASCII when executing the web scenario step.  
The _Parse_ button can be used to separate optional query fields (like ?name=Admin&password=mypassword) from the URL, moving the attributes and values into _Query fields_ for automatic URL-encoding.  
Variables can be used in the URL, using the {macro} syntax. Variables can be URL-encoded manually using a {{macro}.urlencode()} syntax.  
User macros and {HOST.*} [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported.  
Limited to 2048 characters.  
_Query fields_ | HTTP GET variables for the URL.  
Specified as attribute and value pairs.  
Values are URL-encoded automatically. Values from scenario variables, user macros or {HOST.*} macros are resolved and then URL-encoded automatically. Using a {{macro}.urlencode()} syntax will double URL-encode them.  
User macros and {HOST.*} [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported.  
_Post_ | HTTP POST variables.  
In **Form data** mode, specified as attribute and value pairs.  
Values are URL-encoded automatically. Values from scenario variables, user macros or {HOST.*} macros are resolved and then URL-encoded automatically.  
In **Raw data** mode, attributes/values are displayed on a single line and concatenated with a **&** symbol.  
Raw values can be URL-encoded/decoded manually using a {{macro}.urlencode()} or {{macro}.urldecode()} syntax.  
For example: id=2345&userid={user}  
If {user} is defined as a variable of the web scenario, it will be replaced by its value when the step is executed. If you wish to URL-encode the variable, substitute {user} with {{user}.urlencode()}.  
User macros and {HOST.*} [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported.  
_Variables_ | Step-level variables that may be used for GET and POST functions.  
Specified as attribute and value pairs.  
Step-level variables override scenario-level variables or variables from the previous step. However, the value of a step-level variable only affects the step after (and not the current step).  
They have the following format:  
**{macro}** =value  
**{macro}** =regex:<regular expression>  
For more information see variable description on the [scenario](web_monitoring#configuring-a-web-scenario) level.  
Variables are automatically URL-encoded when used in query fields or form data for post variables, but must be URL-encoded manually when used in raw post or directly in URL.  
_Headers_ | Custom HTTP headers that will be sent when performing a request.  
Specified as attribute and value pairs.  
A header defined on a step level will be used for that particular step.  
**It should be noted that defining the header on a step level automatically discards all the previously defined headers, except for a default header that is assigned by selecting the 'User-Agent' from a drop-down list on a scenario level.**  
However, even the 'User-Agent' default header can be overridden by specifying it on a step level.  
For example, assigning the name to a header, but setting no value will unset the default header on a scenario level.  
User macros and {HOST.*} macros are supported.  
This sets the [CURLOPT_HTTPHEADER](http://curl.haxx.se/libcurl/c/CURLOPT_HTTPHEADER.html) cURL option.  
_Follow redirects_ | Mark the checkbox to follow HTTP redirects.  
This sets the [CURLOPT_FOLLOWLOCATION](http://curl.haxx.se/libcurl/c/CURLOPT_FOLLOWLOCATION.html) cURL option.  
_Retrieve mode_ | Select the retrieve mode:  
**Body** \- retrieve only body from the HTTP response  
**Headers** \- retrieve only headers from the HTTP response  
**Body and headers** \- retrieve body and headers from the HTTP response  
_Timeout_ | Zabbix will not spend more than the set amount of time on processing the URL (from one second to maximum of 1 hour). Actually this parameter defines the maximum time for making connection to the URL and maximum time for performing an HTTP request. Therefore, Zabbix will not spend more than **2 x Timeout** seconds on the step.  
[Time suffixes](/documentation/current/en/manual/appendix/suffixes) are supported, e.g. 30s, 1m, 1h. [User macros](/documentation/current/en/manual/config/macros/user_macros) are supported.  
_Required string_ | Required regular expression pattern.  
Unless retrieved content (HTML) matches the required pattern the step will fail. If empty, no check on required string is performed.  
For example:  
Homepage of Zabbix  
Welcome.*admin  
 _Note_ : Referencing [regular expressions](regular_expressions) created in the Zabbix frontend is not supported in this field.  
User macros and {HOST.*} [macros](/documentation/current/en/manual/appendix/macros/supported_by_location) are supported.  
_Required status codes_ | List of expected HTTP status codes. If Zabbix gets a code which is not in the list, the step will fail.  
If empty, no check on status codes is performed.  
For example: 200,201,210-299  
User macros are supported.  
  
Any changes in web scenario steps will only be saved when the whole scenario is saved.

See also a [real-life example](/documentation/current/en/manual/web_monitoring/example) of how web monitoring steps can be configured.

#### Configuring tags

The **Tags** tab allows to define scenario-level [tags](/documentation/current/en/manual/config/tagging).

![](/documentation/current/assets/en/manual/config/scenario_c.png)

Tagging allows to filter web scenarios and web monitoring [items](/documentation/current/en/manual/web_monitoring/items).

#### Configuring authentication

The **Authentication** tab allows you to configure scenario authentication options. A green dot next to the tab name indicates that some type of HTTP authentication is enabled.

![](/documentation/current/assets/en/manual/config/scenario_d.png)

Authentication parameters:

_HTTP authentication_ | Select the authentication option:  
**None** \- no authentication used;  
**Basic** \- basic authentication is used;  
**NTLM** \- NTLM ([Windows NT LAN Manager](http://en.wikipedia.org/wiki/NTLM)) authentication is used;  
**Kerberos** \- Kerberos authentication is used (see also: [Configuring Kerberos with Zabbix](/documentation/current/en/manual/appendix/items/kerberos));  
**Digest** \- Digest authentication is used.  
---|---  
_User_ | Enter the user name (up to 255 characters).  
This field is available if _HTTP authentication_ is set to Basic, NTLM, Kerberos, or Digest. User macros are supported.  
_Password_ | Enter the user password (up to 255 characters).  
This field is available if _HTTP authentication_ is set to Basic, NTLM, Kerberos, or Digest. User macros are supported.  
_SSL verify peer_ | Mark the checkbox to verify the SSL certificate of the web server.  
The server certificate will be automatically taken from system-wide certificate authority (CA) location. You can override the location of CA files using Zabbix server or proxy configuration parameter [SSLCALocation](/documentation/current/en/manual/appendix/config/zabbix_server#sslcalocation).  
This sets the [CURLOPT_SSL_VERIFYPEER](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYPEER.html) cURL option.  
_SSL verify host_ | Mark the checkbox to verify that the _Common Name_ field or the _Subject Alternate Name_ field of the web server certificate matches.  
This sets the [CURLOPT_SSL_VERIFYHOST](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYHOST.html) cURL option.  
_SSL certificate file_ | Name of the SSL certificate file used for client authentication. The certificate file must be in PEM1 format. If the certificate file contains also the private key, leave the _SSL key file_ field empty. If the key is encrypted, specify the password in _SSL key password_ field. The directory containing this file is specified by Zabbix server or proxy configuration parameter [SSLCertLocation](/documentation/current/en/manual/appendix/config/zabbix_server).  
`HOST.*` macros and user macros can be used in this field.  
This sets the [CURLOPT_SSLCERT](http://curl.haxx.se/libcurl/c/CURLOPT_SSLCERT.html) cURL option.  
_SSL key file_ | Name of the SSL private key file used for client authentication. The private key file must be in PEM1 format. The directory containing this file is specified by Zabbix server or proxy configuration parameter [SSLKeyLocation](/documentation/current/en/manual/appendix/config/zabbix_server).  
`HOST.*` macros and user macros can be used in this field.  
This sets the [CURLOPT_SSLKEY](http://curl.haxx.se/libcurl/c/CURLOPT_SSLKEY.html) cURL option.  
_SSL key password_ | SSL private key file password.  
User macros can be used in this field.  
This sets the [CURLOPT_KEYPASSWD](http://curl.haxx.se/libcurl/c/CURLOPT_KEYPASSWD.html) cURL option.  
  
[1] Zabbix supports certificate and private key files in PEM format only. In case you have your certificate and private key data in PKCS #12 format file (usually with extension *.p12 or *.pfx) you may generate the PEM file from it using the following commands:
    
    
    openssl pkcs12 -in ssl-cert.p12 -clcerts -nokeys -out ssl-cert.pem
           openssl pkcs12 -in ssl-cert.p12 -nocerts -nodes  -out ssl-cert.key

Copy

✔ Copied

Zabbix server picks up changes in certificates without a restart.

If you have client certificate and private key in a single file just specify it in a "SSL certificate file" field and leave "SSL key file" field empty. The certificate and key must still be in PEM format. Combining certificate and key is easy:
    
    
    cat client.crt client.key > client.pem

Copy

✔ Copied

#### Display

To view web scenarios configured for a host, go to _Monitoring → Hosts_ , locate the host in the list and click on the _Web_ hyperlink in the last column. Click on the scenario name to get detailed information.

![](/documentation/current/assets/en/manual/web_monitoring/scenario_details2.png)

An overview of web scenarios can also be displayed in _Dashboards_ by the Web monitoring widget.

Recent results of the web scenario execution are available in the _Monitoring → Latest data_ section.

#### Extended monitoring

Sometimes it is necessary to log received HTML page content. This is especially useful if some web scenario step fails. Debug level 5 (trace) serves that purpose. This level can be set in [server](/documentation/current/en/manual/appendix/config/zabbix_server#debuglevel) and [proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#debuglevel) configuration files or using a [runtime control](/documentation/current/en/manual/concepts/server#runtime-control) option (`-R log_level_increase="http poller,N"`, where N is the process number). The following examples demonstrate how extended monitoring can be started provided debug level 4 is already set:
    
    
    # Increase log level of all http pollers:
           zabbix_server -R log_level_increase="http poller"
           
           # Increase log level of second http poller:
           zabbix_server -R log_level_increase="http poller,2"

Copy

✔ Copied

If extended web monitoring is not required it can be stopped using the `-R log_level_decrease` option.