---
title: configuration.importcompare
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/configuration/importcompare
downloaded: 2025-11-14 10:40:20
---

# configuration.importcompare

### Description

`array configuration.importcompare(object parameters)`

This method allows to compare import file with current system elements and shows what will be changed if this import file will be imported.

This method is available to users of any type. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(object)` Parameters containing the possible data to import and rules how the data should be handled.

format | string | Format of the serialized string.  
  
Possible values:  
`yaml` \- YAML;  
`xml` \- XML;  
`json` \- JSON.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
---|---|---  
source | string | Serialized string containing the configuration data.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
rules | object | Rules on how new and existing objects should be compared.  
  
_Admin_ and _User_ type users may compare new objects only with existing ones for which they have _read-only_ or _read-write_ [permission](/documentation/current/en/manual/api/reference/usergroup/object#permission).  
  
The `rules` parameter is described in detail in the table below.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
If no rules are given, there will be nothing to update and result will be empty.

Comparison will be done only for host groups and templates. Triggers and graphs will be compared only for imported templates, any other will be considered as "new".

The `rules` object supports the following parameters.

discoveryRules | object | Rules on how to import LLD rules.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new LLD rules will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing LLD rules will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, LLD rules not present in the imported data will be deleted from the database; default: `false`.  
---|---|---  
graphs | object | Rules on how to import graphs.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new graphs will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing graphs will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, graphs not present in the imported data will be deleted from the database; default: `false`.  
host_groups | object | Rules on how to import host groups.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new host groups will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing host groups will be updated; default: `false`.  
template_groups | object | Rules on how to import template groups.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new template groups will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing template groups will be updated; default: `false`.  
hosts | object | Rules on how to import hosts.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new hosts will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing hosts will be updated; default: `false`.  
  
This parameter will make no difference to the output. It is allowed only for consistency with `configuration.import`.  
httptests | object | Rules on how to import web scenarios.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new web scenarios will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing web scenarios will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, web scenarios not present in the imported data will be deleted from the database; default: `false`.  
images | object | Rules on how to import images.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new images will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing images will be updated; default: `false`.  
  
This parameter will make no difference to the output. It is allowed only for consistency with `configuration.import`.  
items | object | Rules on how to import items.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new items will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing items will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, items not present in the imported data will be deleted from the database; default: `false`.  
maps | object | Rules on how to import maps.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new maps will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing maps will be updated; default: `false`.  
  
This parameter will make no difference to the output. It is allowed only for consistency with `configuration.import`.  
mediaTypes | object | Rules on how to import media types.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new media types will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing media types will be updated; default: `false`.  
  
This parameter will make no difference to the output. It is allowed only for consistency with `configuration.import`.  
templateLinkage | object | Rules on how to import template links.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, templates that are not linked to the host or template being imported, but are present in the imported data, will be linked; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, templates that are linked to the host or template being imported, but are not present in the imported data, will be unlinked without removing entities (items, triggers, etc.) inherited from the unlinked templates; default: `false`.  
templates | object | Rules on how to import templates.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new templates will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing templates will be updated; default: `false`.  
templateDashboards | object | Rules on how to import template dashboards.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new template dashboards will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing template dashboards will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, template dashboards not present in the imported data will be deleted from the database; default: `false`.  
triggers | object | Rules on how to import triggers.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new triggers will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing triggers will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, triggers not present in the imported data will be deleted from the database; default: `false`.  
valueMaps | object | Rules on how to import host or template value maps.  
  
Supported parameters:  
`createMissing` \- `(boolean)` if set to `true`, new value maps will be created; default: `false`;  
`updateExisting` \- `(boolean)` if set to `true`, existing value maps will be updated; default: `false`;  
`deleteMissing` \- `(boolean)` if set to `true`, value maps not present in the imported data will be deleted from the database; default: `false`.  
  
### Return values

`(array)` Returns an array with changes in configuration, that will be made.

### Examples

#### Comparing the import of a template

Compare the template contained in the XML string to the current system elements, and show what will be changed if this template will be imported.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "configuration.importcompare",
               "params": {
                   "format": "xml",
                   "rules": {
                       "discoveryRules": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       },
                       "graphs": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       },
                       "host_groups": {
                           "createMissing": true,
                           "updateExisting": true
                       },
                       "template_groups": {
                           "createMissing": true,
                           "updateExisting": true
                       },
                       "httptests": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       },
                       "items": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       },
                       "templateLinkage": {
                           "createMissing": true,
                           "deleteMissing": true
                       },
                       "templates": {
                           "createMissing": true,
                           "updateExisting": true
                       },
                       "templateDashboards": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       },
                       "triggers": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       },
                       "valueMaps": {
                           "createMissing": true,
                           "updateExisting": true,
                           "deleteMissing": true
                       }
                   },
                   "source": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<zabbix_export><version>7.4</version><template_groups><template_group><uuid>7df96b18c230490a9a0a9e2307226338</uuid><name>Templates</name></template_group></template_groups><templates><template><uuid>5aef0444a82a4d8cb7a95dc4c0c85330</uuid><template>New template</template><name>New template</name><groups><group><name>Templates</name></group></groups><items><item><uuid>7f1e6f1e48aa4a128e5b6a958a5d11c3</uuid><name>Zabbix agent ping</name><key>agent.ping</key><delay>3m</delay></item><item><uuid>77ba228662be4570830aa3c503fcdc03</uuid><name>Apache server uptime</name><type>DEPENDENT</type><key>apache.server.uptime</key><delay>0</delay><trends>0</trends><value_type>TEXT</value_type><preprocessing><step><type>REGEX</type><parameters><parameter>&lt;dt&gt;Server uptime: (.*)&lt;/dt&gt;</parameter><parameter>\\1</parameter></parameters></step></preprocessing><master_item><key>web.page.get[127.0.0.1/server-status]</key></master_item></item><item><uuid>648006da5971424ead0c47ddbbf1ea2e</uuid><name>CPU utilization</name><key>system.cpu.util</key><value_type>FLOAT</value_type><units>%</units><triggers><trigger><uuid>736225012c534ec480c2a66a91322ce0</uuid><expression>avg(/New template/system.cpu.util,3m)&gt;70</expression><name>CPU utilization too high on 'New host' for 3 minutes</name><priority>WARNING</priority></trigger></triggers></item><item><uuid>590efe5731254f089265c76ff9320726</uuid><name>Apache server status</name><key>web.page.get[127.0.0.1/server-status]</key><trends>0</trends><value_type>TEXT</value_type></item></items><valuemaps><valuemap><uuid>8fd5814c45d44a00a15ac6eaae1f3946</uuid><name>Zabbix agent ping</name><mappings><mapping><value>1</value><newvalue>Available</newvalue></mapping><mapping><value>0</value><newvalue>Not available</newvalue></mapping></mappings></valuemap></valuemaps></template></templates></zabbix_export>\n"
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "templates": {
                       "updated": [
                           {
                               "before": {
                                   "uuid": "5aef0444a82a4d8cb7a95dc4c0c85330",
                                   "template": "New template",
                                   "name": "New template",
                                   "groups": [
                                       {
                                           "name": "Templates"
                                       }
                                   ]
                               },
                               "after": {
                                   "uuid": "5aef0444a82a4d8cb7a95dc4c0c85330",
                                   "template": "New template",
                                   "name": "New template",
                                   "groups": [
                                       {
                                           "name": "Templates"
                                       }
                                   ]
                               },
                               "items": {
                                   "added": [
                                       {
                                           "after": {
                                               "uuid": "648006da5971424ead0c47ddbbf1ea2e",
                                               "name": "CPU utilization",
                                               "key": "system.cpu.util",
                                               "value_type": "FLOAT",
                                               "units": "%"
                                           },
                                           "triggers": {
                                               "added": [
                                                   {
                                                       "after": {
                                                           "uuid": "736225012c534ec480c2a66a91322ce0",
                                                           "expression": "avg(/New template/system.cpu.util,3m)>70",
                                                           "name": "CPU utilization too high on 'New host' for 3 minutes",
                                                           "priority": "WARNING"
                                                       }
                                                   }
                                               ]
                                           }
                                       }
                                   ],
                                   "removed": [
                                       {
                                           "before": {
                                               "uuid": "6805d4c39a624a8bab2cc8ab63df1ab3",
                                               "name": "CPU load",
                                               "key": "system.cpu.load",
                                               "value_type": "FLOAT"
                                           },
                                           "triggers": {
                                               "removed": [
                                                   {
                                                       "before": {
                                                           "uuid": "ab4c2526c2bc42e48a633082255ebcb3",
                                                           "expression": "avg(/New template/system.cpu.load,3m)>2",
                                                           "name": "CPU load too high on 'New host' for 3 minutes",
                                                           "priority": "WARNING"
                                                       }
                                                   }
                                               ]
                                           }
                                       }
                                   ],
                                   "updated": [
                                       {
                                           "before": {
                                               "uuid": "7f1e6f1e48aa4a128e5b6a958a5d11c3",
                                               "name": "Zabbix agent ping",
                                               "key": "agent.ping"
                                           },
                                           "after": {
                                               "uuid": "7f1e6f1e48aa4a128e5b6a958a5d11c3",
                                               "name": "Zabbix agent ping",
                                               "key": "agent.ping",
                                               "delay": "3m"
                                           }
                                       }
                                   ]
                               }
                           }
                       ]
                   }
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CConfiguration::importcompare() in _ui/include/classes/api/services/CConfiguration.php_.