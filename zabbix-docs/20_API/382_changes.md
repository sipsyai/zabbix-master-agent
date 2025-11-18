---
title: Appendix 2. Changes from 7.2 to 7.4
source: https://www.zabbix.com/documentation/current/en/manual/api/changes
downloaded: 2025-11-14 10:46:15
---

# Appendix 2. Changes from 7.2 to 7.4

## Backward incompatible changes

#### map

[ZBXNEXT-8784](https://support.zabbix.com/browse/ZBXNEXT-8784) Removed properties `linktriggerid` and `linkid` from the [map link trigger](/documentation/current/en/manual/api/reference/map/object#map-link-trigger) object.  

#### mediatype

[ZBX-26258](https://support.zabbix.com/browse/ZBX-26258) `mediatype.get`: Added strict validation of `selectUsers` parameter.  

#### user

[ZBX-26258](https://support.zabbix.com/browse/ZBX-26258) `user.get`: Added strict validation of method parameters.  
[ZBX-26258](https://support.zabbix.com/browse/ZBX-26258) `user.get`: Property `userid` is now returned only if explicitly requested or if `output` is set to "extend".  

#### usergroup

[ZBX-26258](https://support.zabbix.com/browse/ZBX-26258) `usergroup.get`: Added strict validation of `mfaids`, `selectUsers` parameters.  

## Other changes and bug fixes

#### dashboard

[ZBXNEXT-9087](https://support.zabbix.com/browse/ZBXNEXT-9087) Added new dashboard widget type [`itemcard`](/documentation/current/en/manual/api/reference/dashboard/widget_fields/item_card).  

#### discoveryruleprototype

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new LLD rule prototype API with methods `discoveryruleprototype.create`, `discoveryruleprototype.update`, `discoveryruleprototype.get`, `discoveryruleprototype.delete`.  

#### graph

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameter `selectDiscoveryData` to the `graph.get` method; deprecated the `selectGraphDiscovery` parameter.  

#### graphprototype

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameters `selectDiscoveryRulePrototype` and `selectDiscoveryData` to the `graphprototype.get` method.  

#### host

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameters `selectDiscoveryData` and `selectDiscoveryRules` to the `host.get` method; deprecated `selectHostDiscovery` and `selectDiscoveries` parameters.  

#### hostgroup

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameter `selectDiscoveryData` to the `hostgroup.get` method; deprecated the `selectGroupDiscoveries` parameter.  

#### hostprototype

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameters `selectDiscoveryRulePrototype` and `selectDiscoveryData` to the `hostprototype.get` method.  

#### item

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameter `selectDiscoveryData` to the `item.get` method; deprecated the `selectItemDiscovery` parameter.  

#### itemprototype

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameters `selectDiscoveryRulePrototype` and `selectDiscoveryData` to the `itemprototype.get` method.  

#### map

[ZBXNEXT-875](https://support.zabbix.com/browse/ZBXNEXT-875) Added property `zindex` to [map element](/documentation/current/en/manual/api/reference/map/object#map-element) object.  
[ZBXNEXT-2122](https://support.zabbix.com/browse/ZBXNEXT-2122) Added properties `edit_own_media` and `edit_user_media` to the role API [action](/documentation/current/en/manual/api/reference/role/object#action) object.  
[ZBXNEXT-8784](https://support.zabbix.com/browse/ZBXNEXT-8784) Added properties `background_scale`, `show_element_label`, `show_link_label` to [map](/documentation/current/en/manual/api/reference/map/object#map) object.  
[ZBXNEXT-8784](https://support.zabbix.com/browse/ZBXNEXT-8784) Added property `show_label` to [map element](/documentation/current/en/manual/api/reference/map/object#map-element) object.  
[ZBXNEXT-8784](https://support.zabbix.com/browse/ZBXNEXT-8784) Added properties `show_label`, `indicator_type`, `itemid`, `thresholds`, `highlights` to [map link](/documentation/current/en/manual/api/reference/map/object#map-link) object.  
[ZBXNEXT-8784](https://support.zabbix.com/browse/ZBXNEXT-8784) Added the [map link indicators](/documentation/current/en/manual/api/reference/map/object#map-link-indicators) object.  

#### mediatype

[ZBXNEXT-9805](https://support.zabbix.com/browse/ZBXNEXT-9805) Added option `2` ("OAuth token") to [mediatype](/documentation/current/en/manual/api/reference/mediatype/object#media-type) object `smtp_authentication` property.  
[ZBXNEXT-9805](https://support.zabbix.com/browse/ZBXNEXT-9805) Added properties `redirection_url`, `client_id`, `client_secret`, `authorization_url`, `token_url`, `tokens_status`, `access_token`, `access_token_updated`, `access_expires_in`, `refresh_token` to [mediatype](/documentation/current/en/manual/api/reference/mediatype/object#media-type) object.  

#### template

[ZBXNEXT-9872](https://support.zabbix.com/browse/ZBXNEXT-9827) Added new properties `readme` and `wizard_ready`.  
[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameter `selectDiscoveryRules` to the `template.get` method; deprecated the `selectDiscoveries` parameter.  

#### templatedashboard

[ZBXNEXT-9087](https://support.zabbix.com/browse/ZBXNEXT-9087) Added new template dashboard widget type [`itemcard`](/documentation/current/en/manual/api/reference/dashboard/widget_fields/item_card).  

#### trigger

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameter `selectDiscoveryData` to the `trigger.get` method; deprecated the `selectTriggerDiscovery` parameter.  

#### triggerprototype

[ZBXNEXT-1527](https://support.zabbix.com/browse/ZBXNEXT-1527) Added new parameters `selectDiscoveryRulePrototype` and `selectDiscoveryData` to the `triggerprototype.get` method.  

#### usermacro

[ZBXNEXT-9872](https://support.zabbix.com/browse/ZBXNEXT-9827) Added new property `config` to Host macro object.