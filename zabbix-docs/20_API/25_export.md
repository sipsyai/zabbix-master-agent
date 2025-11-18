---
title: configuration.export
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/configuration/export
downloaded: 2025-11-14 10:40:18
---

# configuration.export

### Description

`string configuration.export(object parameters)`

This method allows to export configuration data as a serialized string.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters defining the objects to be exported and the format to use.

format | string | Format in which the data must be exported.  
  
Possible values:  
`yaml` \- YAML;  
`xml` \- XML;  
`json` \- JSON;  
`raw` \- unprocessed PHP array.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
prettyprint | boolean | Make the output more human readable by adding indentation.  
  
Possible values:  
`true` \- add indentation;  
`false` \- _(default)_ do not add indentation.  
options | object | Objects to be exported.  
  
The `options` object has the following parameters:  
`host_groups` \- `(array)` IDs of host groups to export;  
`hosts` \- `(array)` IDs of hosts to export;  
`images` \- `(array)` IDs of images to export;  
`maps` \- `(array)` IDs of maps to export;  
`mediaTypes` \- `(array)` IDs of media types to export;  
`template_groups` \- `(array)` IDs of template groups to export;  
`templates` \- `(array)` IDs of templates to export.  
  
_Admin_ and _User_ type users may export only those objects for which they have _read-only_ or _read-write_ [permission](/documentation/current/en/manual/api/reference/usergroup/object#permission), as well as images, but not media types.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
### Return values

`(string)` Returns a serialized string containing the requested configuration data.

### Examples

#### Exporting a template

Export the configuration of template "10571" as an XML string.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "configuration.export",
               "params": {
                   "options": {
                       "templates": [
                           "10571"
                       ]
                   },
                   "format": "xml"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<zabbix_export><version>7.4</version><template_groups><template_group><uuid>7df96b18c230490a9a0a9e2307226338</uuid><name>Templates</name></template_group></template_groups><templates><template><uuid>5aef0444a82a4d8cb7a95dc4c0c85330</uuid><template>New template</template><name>New template</name><groups><group><name>Templates</name></group></groups><items><item><uuid>7f1e6f1e48aa4a128e5b6a958a5d11c3</uuid><name>Zabbix agent ping</name><key>agent.ping</key></item><item><uuid>77ba228662be4570830aa3c503fcdc03</uuid><name>Apache server uptime</name><type>DEPENDENT</type><key>apache.server.uptime</key><delay>0</delay><trends>0</trends><value_type>TEXT</value_type><preprocessing><step><type>REGEX</type><parameters><parameter>&lt;dt&gt;Server uptime: (.*)&lt;\/dt&gt;</parameter><parameter>\\1</parameter></parameters></step></preprocessing><master_item><key>web.page.get[127.0.0.1/server-status]</key></master_item></item><item><uuid>6805d4c39a624a8bab2cc8ab63df1ab3</uuid><name>CPU load</name><key>system.cpu.load</key><value_type>FLOAT</value_type><triggers><trigger><uuid>ab4c2526c2bc42e48a633082255ebcb3</uuid><expression>avg(/New template/system.cpu.load,3m)&gt;2</expression><name>CPU load too high on {HOST.HOST} for 3 minutes</name><priority>WARNING</priority></trigger></triggers></item><item><uuid>590efe5731254f089265c76ff9320726</uuid><name>Apache server status</name><key>web.page.get[127.0.0.1/server-status]</key><trends>0</trends><value_type>TEXT</value_type></item></items><valuemaps><valuemap><uuid>8fd5814c45d44a00a15ac6eaae1f3946</uuid><name>Zabbix agent ping</name><mappings><mapping><value>1</value><newvalue>Available</newvalue></mapping><mapping><value>0</value><newvalue>Not available</newvalue></mapping></mappings></valuemap></valuemaps></template></templates></zabbix_export>\n",
               "id": 1
           }

Copy

✔ Copied

### Source

CConfiguration::export() in _ui/include/classes/api/services/CConfiguration.php_.