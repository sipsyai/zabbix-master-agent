---
title: Honeycomb
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/honeycomb
downloaded: 2025-11-14 10:40:50
---

# 11 Honeycomb

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Honeycomb_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/honeycomb) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Honeycomb_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Honeycomb_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Host groups_ | 2 | groupids.0 | [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID.  
  
Note: To configure multiple host groups, create a dashboard widget field object for each host group with an incremented number in the property name.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Host groups (Widget)_ | 1 | groupids._reference | Instead of [Host group](/documentation/current/en/manual/api/reference/hostgroup/get) ID:  
`ABCDE._hostgroupids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for host groups.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Hosts_ | 3 | hostids.0 | [Host](/documentation/current/en/manual/api/reference/host/get) ID.  
  
Note: To configure multiple hosts, create a dashboard widget field object for each host with an incremented number in the property name. For multiple hosts, the parameter _Host groups_ must either be not configured at all or configured with at least one host group that the configured hosts belong to.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
| _Hosts (Widget/Dashboard)_ | 1 | hostids._reference | Instead of [Host](/documentation/current/en/manual/api/reference/host/get) ID:  
`DASHBOARD.hostids` \- set the [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts;  
`ABCDE._hostids` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Host tags_  
| _Evaluation type_ | 0 | evaltype_host | 0 - _(default)_ And/Or;  
2 - Or.  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag name_ | 1 | host_tags.0.tag | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Operator_ | 0 | host_tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Tag value_ | 1 | host_tags.0.value | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Host tags_  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
_Item patterns_ | 1 | items.0 | [Item](/documentation/current/en/manual/api/reference/item/get) name or pattern.  
  
Note: To configure multiple item patterns, create a dashboard widget field object for each item pattern with an incremented number in the property name.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
_Item tags_  
| _Evaluation type_ | 0 | evaltype_item | 0 - _(default)_ And/Or;  
2 - Or.  
_Tag name_ | 1 | item_tags.0.tag | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Item tags_  
_Operator_ | 0 | item_tags.0.operator | 0 - Contains;  
1 - Equals;  
2 - Does not contain;  
3 - Does not equal;  
4 - Exists;  
5 - Does not exist.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Item tags_  
_Tag value_ | 1 | item_tags.0.value | Any string value.  
  
Note: The number in the property name references tag order in the tag evaluation list.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if configuring _Item tags_  
_Show hosts in maintenance_ | 0 | maintenance | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Show_ | 0 | show.0 | 1 - Primary label;  
2 - Secondary label.  
  
Note: To configure multiple values, create a dashboard widget field object for each value with an incremented number in the property name.  
  
Default: 1, 2.  
_Reference_ | 1 | reference | Any string value consisting of 5 characters (e.g., `ABCDE` or `JBPNL`). This value must be unique within the dashboard to which the widget belongs.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_  
  
#### Advanced configuration

The following advanced configuration parameters are supported for the _Honeycomb_ widget.

The number in the _Thresholds_ property name (e.g. thresholds.0.color) references the threshold place in a list, sorted in ascending order. However, if thresholds are configured in a different order, the values will be sorted in ascending order after updating widget configuration in Zabbix frontend (e.g. `"thresholds.0.threshold":"5"` → `"thresholds.0.threshold":"1"`; `"thresholds.1.threshold":"1"` → `"thresholds.1.threshold": "5"`).

**_Primary label_**  
---  
_Type_ | 0 | primary_label_type | 0 - _(default)_ Text;  
1 - Value.  
_Text_ | 1 | primary_label | Any string value, including macros.  
Supported macros: {HOST.*}, {ITEM.*}, {INVENTORY.*}, user macros.  
  
Default: {HOST.NAME}  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Text"  
_Decimal places_ | 0 | primary_label_decimal_places | Possible values range from 0-6.  
  
Default: 2.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value"  
_Size_ (type) | 0 | primary_label_size_type | 0 - _(default)_ Auto;  
1 - Custom.  
_Size_ | 0 | primary_label_size | Possible values range from 1-100.  
  
Default: 20.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Size_ (type) is set to "Custom"  
_Bold_ | 0 | primary_label_bold | 0 - _(default)_ Disabled;  
1 - Enabled.  
_Color_ | 1 | primary_label_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: based on `theme` of [Settings object](/documentation/current/en/manual/api/reference/settings/object#settings) and [User object](/documentation/current/en/manual/api/reference/user/object#user):  
`1F2C33` for "blue-theme" or "hc-light";  
`EEEEEE` for "dark-theme" or "hc-dark".  
_Units_ (checkbox) | 0 | primary_label_units_show | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value"  
_Units_ (value) | 1 | primary_label_units | Any string value.  
  
`""` (empty)  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value" and _Units_ (checkbox) is set to "Enabled"  
_Position_ | 0 | primary_label_units_pos | 0 - Before value;  
1 - _(default)_ After value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value" and _Units_ (checkbox) is set to "Enabled"  
  
This parameter is ignored if set to one of the following [time-related units](/documentation/current/en/manual/config/items/item#configuration): unixtime, uptime, s.  
**_Secondary label_**  
_Type_ | 0 | secondary_label_type | 0 - Text;  
1 - _(default)_ Value.  
_Text_ | 1 | secondary_label | Any string value, including macros.  
Supported macros: {HOST.*}, {ITEM.*}, {INVENTORY.*}, user macros.  
  
Default: {{ITEM.LASTVALUE}.fmtnum(2)}  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Text"  
_Decimal places_ | 0 | secondary_label_decimal_places | Possible values range from 0-6.  
  
Default: 2.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value"  
_Size_ (type) | 0 | secondary_label_size_type | 0 - _(default)_ Auto;  
1 - Custom.  
_Size_ | 0 | secondary_label_size | Possible values range from 1-100.  
  
Default: 30.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Size_ (type) is set to "Custom"  
_Bold_ | 0 | secondary_label_bold | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Color_ | 1 | secondary_label_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: based on `theme` of [Settings object](/documentation/current/en/manual/api/reference/settings/object#settings) and [User object](/documentation/current/en/manual/api/reference/user/object#user):  
`1F2C33` for "blue-theme" or "hc-light";  
`EEEEEE` for "dark-theme" or "hc-dark".  
_Units_ (checkbox) | 0 | secondary_label_units_show | 0 - Disabled;  
1 - _(default)_ Enabled.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value"  
_Units_ (value) | 1 | secondary_label_units | Any string value.  
  
`""` (empty)  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value" and _Units_ (checkbox) is set to "Enabled"  
_Position_ | 0 | secondary_label_position | 0 - Before value;  
1 - _(default)_ After value.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Type_ is set to "Value" and _Units_ (checkbox) is set to "Enabled"  
  
This parameter is ignored if set to one of the following [time-related units](/documentation/current/en/manual/config/items/item#configuration): unixtime, uptime, s.  
**_Background color_**  
_Background color_ | 1 | bg_color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: based on `theme` of [Settings object](/documentation/current/en/manual/api/reference/settings/object#settings) and [User object](/documentation/current/en/manual/api/reference/user/object#user):  
`D9E7ED` for "blue-theme";  
`3D5059` for "dark-theme";  
`AAD7E9` for "hc-light";  
`335463` for "hc-dark".  
**_Thresholds_**  
_Color interpolation_ | 0 | interpolation | 0 - Disabled;  
1 - _(default)_ Enabled.  
_Color_ | 1 | thresholds.0.color | Hexadecimal color code (e.g. `FF0000`).  
_Threshold_ | 1 | thresholds.0.threshold | Any numeric value. [Suffixes](/documentation/current/en/manual/appendix/suffixes) (e.g. "1d", "2w", "4K", "8G") are supported.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Honeycomb_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring a _Honeycomb_ widget

Configure a _Honeycomb_ widget that displays the utilization of Zabbix server processes. In addition, change the primary label of honeycomb cells and visually fine-tune the widget with thresholds.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.create",
               "params": {
                   "name": "My dashboard",
                   "display_period": "30",
                   "auto_start": "1",
                   "pages": [
                       {
                           "widgets": [
                               {
                                   "type": "honeycomb",
                                   "name": "Honeycomb",
                                   "x": "0",
                                   "y": "0",
                                   "width": "24",
                                   "height": "5",
                                   "view_mode": "0",
                                   "fields": [
                                       {
                                           "type": 2,
                                           "name": "groupids.0",
                                           "value": 4
                                       },
                                       {
                                           "type": 3,
                                           "name": "hostids.0",
                                           "value": 10084
                                       },
                                       {
                                           "type": 1,
                                           "name": "items.0",
                                           "value": "Zabbix server: Utilization*"
                                       },
                                       {
                                           "type": 1,
                                           "name": "primary_label",
                                           "value": "{ITEM.NAME}"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.0.color",
                                           "value": "0EC9AC"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.0.threshold",
                                           "value": "0"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.1.color",
                                           "value": "FFD54F"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.1.threshold",
                                           "value": "70"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.2.color",
                                           "value": "FF465C"
                                       },
                                       {
                                           "type": 1,
                                           "name": "thresholds.2.threshold",
                                           "value": "90"
                                       },
                                       {
                                           "type": 1,
                                           "name": "reference",
                                           "value": "KSTMQ"
                                       }
                                   ]
                               }
                           ]
                       }
                   ],
                   "userGroups": [
                       {
                           "usrgrpid": 7,
                           "permission": 2
                       }
                   ],
                   "users": [
                       {
                           "userid": 1,
                           "permission": 3
                       }
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "dashboardids": [
                       "3"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### See also

  * [Dashboard widget field](/documentation/current/en/manual/api/reference/dashboard/object#dashboard-widget-field)
  * [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create)
  * [`dashboard.update`](/documentation/current/en/manual/api/reference/dashboard/update)