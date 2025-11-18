---
title: Item card
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/dashboard/widget_fields/item_card
downloaded: 2025-11-14 10:40:55
---

# 15 Item card

### Description

These parameters and the possible property values for the respective dashboard widget field objects allow to configure the [_Item card_](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card) widget in `dashboard.create` and `dashboard.update` methods.

Widget `fields` properties are not validated during the creation or update of a dashboard. This allows users to modify [built-in widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets) and create [custom widgets](/documentation/current/en/devel/modules/tutorials/widget), but also introduces the risk of creating or updating widgets incorrectly. To ensure the successful creation or update of the _Item card_ widget, please refer to the parameter behavior outlined in the tables below.

### Parameters

The following parameters are supported for the _Item card_ widget.

_Refresh interval_ | 0 | rf_rate | 0 - No refresh;  
10 - 10 seconds;  
30 - 30 seconds;  
60 - _(default)_ 1 minute;  
120 - 2 minutes;  
600 - 10 minutes;  
900 - 15 minutes.  
---|---|---|---  
_Item_ | 4 | itemid.0 | [Item](/documentation/current/en/manual/api/reference/item/get) ID.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Item (Widget)_ is not set  
| _Item (Widget)_ | 1 | itemid._reference | Instead of [Item](/documentation/current/en/manual/api/reference/item/get) ID:  
`ABCDE._itemid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for item.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _required_ if _Item_ is not set  
_Show_ | 0 | sections.0 | 0 - Description;  
1 - Error text;  
2 - Metrics;  
3 - Latest data;  
4 - Type of information;  
5 - Triggers;  
6 - Host interface;  
7 - Type;  
8 - Host inventory;  
9 - Tags.  
  
Note: The number in the property name references section order in the section list. To configure multiple sections, create a dashboard widget field object for each section with an incremented number in the property name.  
_Override host_ | 1 | override_hostid._reference | `ABCDE._hostid` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its _Reference_ parameter set to "`ABCDE`") as the data source for hosts;  
`DASHBOARD._hostid` \- set the dashboard [_Host_ selector](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#override-host) as the data source for hosts.  
  
Default: `""` (empty)  
  
This parameter is not supported if configuring the widget on a [template dashboard](/documentation/current/en/manual/api/reference/templatedashboard/object).  
  
#### Sparkline

The following parameters are supported if _Show_ is set to "Latest data".

_Width_ | 0 | sparkline.width | Possible values range from 0-10.  
  
Default: 1.  
---|---|---|---  
_Fill_ | 0 | sparkline.fill | Possible values range from 0-10.  
  
Default: 3.  
_Color_ | 1 | sparkline.color | Hexadecimal color code (e.g. `FF0000`).  
  
Default: `42A5F5`.  
_Time period_ | 1 | sparkline.time_period._reference | `DASHBOARD._timeperiod` \- set the [_Time period_ selector](/documentation/current/en/manual/web_interface/time_period_selector) as the data source;  
`ABCDE._timeperiod` \- set a [compatible widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets#widget-compatibility) (with its `reference` parameter equal to `ABCDE`) as the data source.  
  
Default: `""` (empty)  
  
Alternatively, you can set the time period only in the _From_ and _To_ parameters.  
| _From_ | 1 | sparkline.time_period.from | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
Default: now-1h.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set  
_To_ | 1 | sparkline.time_period.to | Valid time string in absolute (`YYYY-MM-DD hh:mm:ss`) or [relative](/documentation/current/en/manual/web_interface/time_period_selector) time syntax (`now`, `now/d`, `now/w-1w`, etc.).  
  
Default: now.  
  
[Parameter behavior](/documentation/current/en/manual/api/reference_commentary#parameter-behavior):  
\- _supported_ if _Time period_ is not set  
_History data_ | 0 | sparkline.history | 0 - _(default)_ Auto;  
1 - History;  
2 - Trends.  
  
### Examples

The following examples aim to only describe the configuration of the dashboard widget field objects for the _Item card_ widget. For more information on configuring a dashboard, see [`dashboard.create`](/documentation/current/en/manual/api/reference/dashboard/create).

#### Configuring an _Item card_ widget

Configure an _Item card_ widget that displays these sections: "Description", "Latest data", "Triggers", and "Tags".

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "dashboard.create",
               "params": {
                   "name": "My dashboard",
                   "display_period": 30,
                   "auto_start": 1,
                   "pages": [
                       {
                           "widgets": [
                               {
                                   "type": "itemcard",
                                   "name": "Item card",
                                   "x": 0,
                                   "y": 0,
                                   "width": 14,
                                   "height": 7,
                                   "view_mode": 0,
                                   "fields": [
                                       {
                                           "type": 4,
                                           "name": "itemid.0",
                                           "value": 42257
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.0",
                                           "value": 0
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.1",
                                           "value": 3
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.2",
                                           "value": 5
                                       },
                                       {
                                           "type": 0,
                                           "name": "sections.3",
                                           "value": 9
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