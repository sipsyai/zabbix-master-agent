---
title: HTTP agent
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/http
downloaded: 2025-11-14 10:35:17
---

# 16 HTTP agent

#### Overview

This item type allows data polling using the HTTP/HTTPS protocol. Trapping is also possible using the [Zabbix sender](/documentation/current/en/manual/concepts/sender) utility or Zabbix sender [protocol](/documentation/current/en/manual/appendix/protocols/zabbix_sender) (for sending data to Zabbix server or proxy), or using the [`history.push`](/documentation/current/en/manual/api/reference/history/push) API method (for sending data to Zabbix server).

HTTP item checks are executed by Zabbix server. However, when hosts are monitored by a Zabbix proxy, HTTP item checks are executed by the proxy.

HTTP item checks do not require any agent running on a host being monitored.

HTTP agent supports both HTTP and HTTPS. Zabbix will optionally follow redirects (see the _Follow redirects_ option below). Maximum number of redirects is hard-coded to 10 (using cURL option CURLOPT_MAXREDIRS).

Zabbix server/proxy must be initially configured with cURL (libcurl) support.

HTTP checks are executed asynchronously - it is not required to receive the response to one request before other checks are started. DNS resolving is asynchronous as well.

The maximum concurrency of asynchronous checks is 1000 (defined by [MaxConcurrentChecksPerPoller](/documentation/current/en/manual/appendix/config/zabbix_server#maxconcurrentchecksperpoller)).

The number of asynchronous HTTP agent pollers is defined by the [StartHTTPAgentPollers](/documentation/current/en/manual/appendix/config/zabbix_server#starthttpagentpollers) parameter.

The persistent connections cURL feature has been added to HTTP agent checks since Zabbix 7.0.

#### Configuration

To configure an HTTP item:

  * Go to: _Data collection_ → _Hosts_
  * Click on _Items_ in the row of the host
  * Click on _Create item_
  * Enter parameters of the item in the form

![](/documentation/current/assets/en/manual/config/items/itemtypes/http_item.png)

All mandatory input fields are marked with a red asterisk.

The fields that require specific information for HTTP items are:

_Type_ | Select **HTTP agent** here.  
---|---  
_Key_ | Enter a unique item key.  
_URL_ | URL to connect to and retrieve data. For example:  
https://www.example.com  
http://www.example.com/download  
Domain names can be specified in Unicode characters. They are automatically punycode-converted to ASCII when executing the HTTP check.  
The _Parse_ button can be used to separate optional query fields (like ?name=Admin&password=mypassword) from the URL, moving the attributes and values into _Query fields_ for automatic URL-encoding.  
Limited to 2048 characters.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
This sets the [CURLOPT_URL](https://curl.haxx.se/libcurl/c/CURLOPT_URL.html) cURL option.  
_Query fields_ | Variables for the URL (see above).  
Specified as attribute and value pairs.  
Values are URL-encoded automatically. Values from macros are resolved and then URL-encoded automatically.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
This sets the [CURLOPT_URL](https://curl.haxx.se/libcurl/c/CURLOPT_URL.html) cURL option.  
_Request type_ | Select request method type: _GET_ , _POST_ , _PUT_ or _HEAD_  
_Request body type_ | Select the request body type:  
**Raw data** \- custom HTTP request body, macros are substituted but no encoding is performed  
**JSON data** \- HTTP request body in JSON format. Macros can be used as string, number, true and false; macros used as strings must be enclosed in double quotes. Values from macros are resolved and then escaped automatically. If "Content-Type" is not specified in headers then it will default to "Content-Type: application/json"  
**XML data** \- HTTP request body in XML format. Macros can be used as a text node, attribute or CDATA section. Values from macros are resolved and then escaped automatically in a text node and attribute. If "Content-Type" is not specified in headers then it will default to "Content-Type: application/xml"  
_Note_ that selecting _XML data_ requires libxml2.  
_Request body_ | Enter the request body.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
_Headers_ | Custom HTTP headers that will be sent when performing a request.  
Specified as attribute and value pairs.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
This sets the [CURLOPT_HTTPHEADER](https://curl.haxx.se/libcurl/c/CURLOPT_HTTPHEADER.html) cURL option.  
_Required status codes_ | List of expected HTTP status codes. If Zabbix gets a code which is not in the list, the item will become unsupported. If empty, no check is performed.  
For example: 200,201,210-299  
Supported macros in the list: user macros, low-level discovery macros.  
This uses the [CURLINFO_RESPONSE_CODE](https://curl.haxx.se/libcurl/c/CURLINFO_RESPONSE_CODE.html) cURL option.  
_Follow redirects_ | Mark the checkbox to follow HTTP redirects.  
This sets the [CURLOPT_FOLLOWLOCATION](https://curl.haxx.se/libcurl/c/CURLOPT_FOLLOWLOCATION.html) cURL option.  
_Retrieve mode_ | Select the part of response that must be retrieved:  
**Body** \- body only  
**Headers** \- headers only  
**Body and headers** \- body and headers  
_Convert to JSON_ | Headers are saved as attribute and value pairs under the "header" key if _Retrieve mode_ is not set to _Body_.  
If 'Content-Type: application/json' is encountered then body is saved as an object, otherwise it is stored as string, for example:  
![](/documentation/current/assets/en/manual/config/items/itemtypes/http_conv_json.png)  
_HTTP proxy_ | You can specify an HTTP proxy to use, using the format `[protocol://][username[:password]@]proxy.example.com[:port]`.  
The optional `protocol://` prefix may be used to specify alternative proxy protocols (e.g. https, socks4, socks5; see [documentation](https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html); the protocol prefix support was added in cURL 7.21.7). With no protocol specified, the proxy will be treated as an HTTP proxy. If you specify the wrong protocol, the connection will fail and the item will become unsupported.  
By default, 1080 port will be used.  
If specified, the proxy will overwrite proxy related environment variables like http_proxy, HTTPS_PROXY. If not specified, the proxy will not overwrite proxy-related environment variables. The entered value is passed on "as is", no sanity checking takes place.  
_Note_ that only simple authentication is supported with HTTP proxy.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
This sets the [CURLOPT_PROXY](https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html) cURL option.  
_HTTP authentication_ | Select the authentication option:  
**None** \- no authentication used;  
**Basic** \- basic authentication is used;  
**NTLM** \- NTLM ([Windows NT LAN Manager](http://en.wikipedia.org/wiki/NTLM)) authentication is used;  
**Kerberos** \- Kerberos authentication is used (see also: [Configuring Kerberos with Zabbix](/documentation/current/en/manual/appendix/items/kerberos));  
**Digest** \- Digest authentication is used.  
This sets the [CURLOPT_HTTPAUTH](https://curl.haxx.se/libcurl/c/CURLOPT_HTTPAUTH.html) cURL option.  
_User name_ | Enter the user name (up to 255 characters).  
This field is available if _HTTP authentication_ is set to Basic, NTLM, Kerberos, or Digest. User macros and low-level discovery macros are supported.  
_Password_ | Enter the user password (up to 255 characters).  
This field is available if _HTTP authentication_ is set to Basic, NTLM, Kerberos, or Digest. User macros and low-level discovery macros are supported.  
_SSL verify peer_ | Mark the checkbox to verify the SSL certificate of the web server. The server certificate will be automatically taken from system-wide certificate authority (CA) location. You can override the location of CA files using Zabbix server or proxy configuration parameter SSLCALocation.  
This sets the [CURLOPT_SSL_VERIFYPEER](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYPEER.html) cURL option.  
_SSL verify host_ | Mark the checkbox to verify that the Common Name field or the Subject Alternate Name field of the web server certificate matches.  
This sets the [CURLOPT_SSL_VERIFYHOST](http://curl.haxx.se/libcurl/c/CURLOPT_SSL_VERIFYHOST.html) cURL option.  
_SSL certificate file_ | Name of the SSL certificate file used for client authentication. The certificate file must be in PEM1 format. If the certificate file contains also the private key, leave the SSL key file field empty. If the key is encrypted, specify the password in SSL key password field. The directory containing this file is specified by Zabbix server or proxy configuration parameter SSLCertLocation.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
This sets the [CURLOPT_SSLCERT](http://curl.haxx.se/libcurl/c/CURLOPT_SSLCERT.html) cURL option.  
_SSL key file_ | Name of the SSL private key file used for client authentication. The private key file must be in PEM1 format. The directory containing this file is specified by Zabbix server or proxy configuration parameter SSLKeyLocation.  
Supported macros: {HOST.IP}, {HOST.CONN}, {HOST.DNS}, {HOST.HOST}, {HOST.NAME}, {HOST.PORT}, {ITEM.ID}, {ITEM.KEY}, {ITEM.KEY.ORIG}, user macros, low-level discovery macros.  
This sets the [CURLOPT_SSLKEY](http://curl.haxx.se/libcurl/c/CURLOPT_SSLKEY.html) cURL option.  
_SSL key password_ | SSL private key file password.  
Supported macros: user macros, low-level discovery macros.  
This sets the [CURLOPT_KEYPASSWD](http://curl.haxx.se/libcurl/c/CURLOPT_KEYPASSWD.html) cURL option.  
_Timeout_ | Zabbix will not spend more than the set amount of time on processing the URL (1-600 seconds). Actually this parameter defines the maximum time for making a connection to the URL and maximum time for performing an HTTP request. Therefore, Zabbix will not spend more than 2 x _Timeout_ seconds on one check.  
This sets the [CURLOPT_TIMEOUT](https://curl.haxx.se/libcurl/c/CURLOPT_TIMEOUT.html) cURL option.  
For more information on the _Timeout_ parameter, see [general item attributes](/documentation/current/en/manual/config/items/item#configuration).  
_Enable trapping_ | With this checkbox marked, the item will also function as a trapper item and will accept data sent to Zabbix server or proxy using the [Zabbix sender](/documentation/current/en/manual/concepts/sender) utility or Zabbix sender [protocol](/documentation/current/en/manual/appendix/protocols/zabbix_sender), or will accept data sent to Zabbix server using the [`history.push`](/documentation/current/en/manual/api/reference/history/push) API method. For more information about sending data, see: [Trapper items](/documentation/current/en/manual/config/items/itemtypes/trapper#sending-data).  
_Allowed hosts_ | Visible only if _Enable trapping_ checkbox is marked.  
List of comma delimited IP addresses, optionally in CIDR notation, or DNS names.  
If specified, incoming connections will be accepted only from the hosts listed here.  
If IPv6 support is enabled then '127.0.0.1', '::127.0.0.1', '::ffff:127.0.0.1' are treated equally and '::/0' will allow any IPv4 or IPv6 address.  
'0.0.0.0/0' can be used to allow any IPv4 address.  
Note that "IPv4-compatible IPv6 addresses" (0000::/96 prefix) are supported but deprecated by [RFC4291](https://tools.ietf.org/html/rfc4291#section-2.5.5).  
Example: 127.0.0.1, 192.168.1.0/24, 192.168.3.1-255, 192.168.1-10.1-255, ::1,2001:db8::/32, mysqlserver1, zabbix.example.com, {HOST.HOST}  
Spaces and [user macros](/documentation/current/en/manual/config/macros/user_macros) are allowed in this field.  
Host macros: {HOST.HOST}, {HOST.NAME}, {HOST.IP}, {HOST.DNS}, {HOST.CONN} are allowed in this field.  
  
If the _HTTP proxy_ field is left empty, another way for using an HTTP proxy is to set proxy-related environment variables.

For HTTP - set the `http_proxy` environment variable for the Zabbix server user. For example:  
`http_proxy=http://proxy_ip:proxy_port`.

For HTTPS - set the `HTTPS_PROXY` environment variable. For example:  
`HTTPS_PROXY=http://proxy_ip:proxy_port`. More details are available by running a shell command: _# man curl_.

[1] Zabbix supports certificate and private key files in PEM format only. In case you have your certificate and private key data in PKCS #12 format file (usually with extension *.p12 or *.pfx) you may generate the PEM file from it using the following commands:
    
    
    openssl pkcs12 -in ssl-cert.p12 -clcerts -nokeys -out ssl-cert.pem
           openssl pkcs12 -in ssl-cert.p12 -nocerts -nodes  -out ssl-cert.key

Copy

✔ Copied

#### Examples

##### Example 1

Send simple GET requests to retrieve data from services such as Elasticsearch:

  * Create a GET item with URL: `localhost:9200/?pretty`
  * Notice the response:

    
    
        {
                 "name" : "YQ2VAY-",
                 "cluster_name" : "elasticsearch",
                 "cluster_uuid" : "kH4CYqh5QfqgeTsjh2F9zg",
                 "version" : {
                   "number" : "6.1.3",
                   "build_hash" : "af51318",
                   "build_date" : "2018-01-26T18:22:55.523Z",
                   "build_snapshot" : false,
                   "lucene_version" : "7.1.0",
                   "minimum_wire_compatibility_version" : "5.6.0",
                   "minimum_index_compatibility_version" : "5.0.0"
                 },
                 "tagline" : "You know, for search"
               }

Copy

✔ Copied

  * Now extract the version number using a JSONPath preprocessing step: `$.version.number`

##### Example 2

Send simple POST requests to retrieve data from services such as Elasticsearch:

  * Create a POST item with URL: `http://localhost:9200/str/values/_search?scroll=10s`
  * Configure the following POST body to obtain the processor load (1 min average per core)

    
    
        {
                   "query": {
                       "bool": {
                           "must": [{
                               "match": {
                                   "itemid": 28275
                               }
                           }],
                           "filter": [{
                               "range": {
                                   "clock": {
                                       "gt": 1517565836,
                                       "lte": 1517566137
                                   }
                               }
                           }]
                       }
                   }
               }

Copy

✔ Copied

  * Received:

    
    
        {
                   "_scroll_id": "DnF1ZXJ5VGhlbkZldGNoBQAAAAAAAAAkFllRMlZBWS1UU1pxTmdEeGVwQjRBTFEAAAAAAAAAJRZZUTJWQVktVFNacU5nRHhlcEI0QUxRAAAAAAAAACYWWVEyVkFZLVRTWnFOZ0R4ZXBCNEFMUQAAAAAAAAAnFllRMlZBWS1UU1pxTmdEeGVwQjRBTFEAAAAAAAAAKBZZUTJWQVktVFNacU5nRHhlcEI0QUxR",
                   "took": 18,
                   "timed_out": false,
                   "_shards": {
                       "total": 5,
                       "successful": 5,
                       "skipped": 0,
                       "failed": 0
                   },
                   "hits": {
                       "total": 1,
                       "max_score": 1.0,
                       "hits": [{
                           "_index": "dbl",
                           "_type": "values",
                           "_id": "dqX9VWEBV6sEKSMyk6sw",
                           "_score": 1.0,
                           "_source": {
                               "itemid": 28275,
                               "value": "0.138750",
                               "clock": 1517566136,
                               "ns": 25388713,
                               "ttl": 604800
                           }
                       }]
                   }
               }

Copy

✔ Copied

  * Now use a JSONPath preprocessing step to get the item value: `$.hits.hits[0]._source.value`

##### Example 3

Checking if Zabbix API is alive, using [apiinfo.version](/documentation/current/en/manual/api/reference/apiinfo/version).

  * Item configuration:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example3_a.png)

Note the use of the POST method with JSON data, setting request headers and asking to return headers only:

  * Item value preprocessing with regular expression to get HTTP code:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example3_b.png)

  * Checking the result in _Latest data_ :

![](/documentation/current/assets/en/manual/config/items/itemtypes/example3_c.png)

##### Example 4

Retrieving weather information by connecting to the Openweathermap public service.

  * Configure a master item for bulk data collection in a single JSON:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example4_a.png)

Note the usage of macros in query fields. Refer to the [Openweathermap API](https://openweathermap.org/current) for how to fill them.

Sample JSON returned in response to HTTP agent:
    
    
    {
               "body": {
                   "coord": {
                       "lon": 40.01,
                       "lat": 56.11
                   },
                   "weather": [{
                       "id": 801,
                       "main": "Clouds",
                       "description": "few clouds",
                       "icon": "02n"
                   }],
                   "base": "stations",
                   "main": {
                       "temp": 15.14,
                       "pressure": 1012.6,
                       "humidity": 66,
                       "temp_min": 15.14,
                       "temp_max": 15.14,
                       "sea_level": 1030.91,
                       "grnd_level": 1012.6
                   },
                   "wind": {
                       "speed": 1.86,
                       "deg": 246.001
                   },
                   "clouds": {
                       "all": 20
                   },
                   "dt": 1526509427,
                   "sys": {
                       "message": 0.0035,
                       "country": "RU",
                       "sunrise": 1526432608,
                       "sunset": 1526491828
                   },
                   "id": 487837,
                   "name": "Stavrovo",
                   "cod": 200
               }
           }

Copy

✔ Copied

The next task is to configure dependent items that extract data from the JSON.

  * Configure a sample dependent item for humidity:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example4_b.png)

Other weather metrics such as 'Temperature' are added in the same manner.

  * Sample dependent item value preprocessing with JSONPath:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example4_c.png)

  * Check the result of weather data in _Latest data_ :

![](/documentation/current/assets/en/manual/config/items/itemtypes/example4_d.png)

##### Example 5

Connecting to Nginx status page and getting its metrics in bulk.

  * Configure Nginx following the [official guide](https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html).
  * Configure a master item for bulk data collection:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example5_a.png)

Sample Nginx stub status output:
    
    
    Active connections: 1 Active connections:
           server accepts handled requests
            52 52 52 
           Reading: 0 Writing: 1 Waiting: 0

Copy

✔ Copied

The next task is to configure dependent items that extract data.

  * Configure a sample dependent item for requests per second:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example5_b.png)

  * Sample dependent item value preprocessing with regular expression `server accepts handled requests\s+([0-9]+) ([0-9]+) ([0-9]+)`:

![](/documentation/current/assets/en/manual/config/items/itemtypes/example5_c.png)

  * Check the complete result from stub module in _Latest data_ :

![](/documentation/current/assets/en/manual/config/items/itemtypes/example5_d.png)