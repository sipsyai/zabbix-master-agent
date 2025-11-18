---
title: Prometheus checks
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/prometheus
downloaded: 2025-11-14 10:35:18
---

# 17 Prometheus checks

#### Overview

Zabbix can query metrics exposed in the Prometheus line format.

Two steps are required to start gathering Prometheus data:

  * an [HTTP master item](/documentation/current/en/manual/config/items/itemtypes/http) pointing to the appropriate data endpoint, e.g. `https://<prometheus host>/metrics`
  * dependent items using a Prometheus preprocessing option to query required data from the metrics gathered by the master item

There are two Prometheus data preprocessing options:

  * _Prometheus pattern_ \- used in normal items to query Prometheus data
  * _Prometheus to JSON_ \- used in normal items and for low-level discovery. In this case queried Prometheus data are returned in a JSON format.

##### Bulk processing

Bulk processing is supported for dependent items. To enable caching and indexing, the _Prometheus pattern_ preprocessing must be the **first** preprocessing step. When _Prometheus pattern_ is first preprocessing step then the parsed Prometheus data is cached and indexed by the first `<label>==<value>` condition in the _Prometheus pattern_ preprocessing step. This cache is reused when processing other dependent items in this batch. For optimal performance, the first label should be the one with most different values.

If there is other preprocessing to be done before the first step, it should be moved either to the master item or to a new dependent item which would be used as the master item for the dependent items.

#### Configuration

Providing you have the HTTP master item configured, you need to create a [dependent item](/documentation/current/en/manual/config/items/itemtypes/dependent_items) that uses a Prometheus preprocessing step:

  * Enter general dependent item parameters in the configuration form
  * Go to the Preprocessing tab
  * Select a Prometheus preprocessing option (_Prometheus pattern_ or _Prometheus to JSON_)

![](/documentation/current/assets/en/manual/config/items/itemtypes/prometheus_item.png)

The following parameters are specific to the _Prometheus pattern_ preprocessing option:

_Pattern_ | To define the required data pattern you may use a query language that is similar to Prometheus query language (see comparison table), e.g.:  
<metric name> \- select by metric name  
{__name__="<metric name>"} - select by metric name  
{__name__=~"<regex>"} - select by metric name matching a regular expression  
{<label name>="<label value>",...} - select by label name  
{<label name>=~"<regex>",...} - select by label name matching a regular expression  
{__name__=~".*"}==<value> \- select by metric value  
Or a combination of the above:  
<metric name>{<label1 name>="<label1 value>",<label2 name>=~"<regex>",...}==<value>  
  
Label value can be any sequence of UTF-8 characters, but the backslash, double-quote and line feed characters have to be escaped as `\\`, `\"` and `\n` respectively; other characters shall not be escaped. | _wmi_os_physical_memory_free_bytes_  
 _cpu_usage_system{cpu="cpu-total"}_  
_cpu_usage_system{cpu=~".*"}_  
_cpu_usage_system{cpu="cpu-total",host=~".*"}_  
_wmi_service_state{name="dhcp"}==1_  
 _wmi_os_timezone{timezone=~".*"}==1_  
---|---|---  
_Result processing_ | Specify whether to return the value, the label or apply the appropriate function (if the pattern matches several lines and the result needs to be aggregated):  
**value** \- return metric value (error if multiple lines matched)  
**label** \- return value of the label specified in the _Label_ field (error if multiple metrics are matched)  
**sum** \- return the sum of values  
**min** \- return the minimum value  
**max** \- return the maximum value  
**avg** \- return the average value  
**count** \- return the count of values  
This field is only available for the _Prometheus pattern_ option. | See also examples of using parameters below.  
_Output_ | Define label name (optional). In this case the value corresponding to the label name is returned.  
This field is only available for the _Prometheus pattern_ option, if 'Label' is selected in the _Result processing_ field. |   
  
**Examples of using parameters**

  1. The most common use case is to return the **value**. To return the value of `/var/db` from:

> `node_disk_usage_bytes{path="/var/cache"} 2.1766144e+09`  
>  `node_disk_usage_bytes{path="/var/db"} 20480`  
>  `node_disk_usage_bytes{path="/var/dpkg"} 8192`  
>  `node_disk_usage_bytes{path="/var/empty"} 4096`

use the following parameters:

  * _Pattern_ \- `node_disk_usage_bytes{path="/var/db"}`
  * _Result processing_ \- select 'value'

  2. You may also be interested in the **average** value of all `node_disk_usage_bytes` parameters:

  * _Pattern_ \- `node_disk_usage_bytes`
  * _Result processing_ \- select 'avg'

  3. While Prometheus supports only numerical data, it is popular to use a workaround that allows to return the relevant textual description as well. This can be accomplished with a filter and specifying the label. So, to return the value of the 'color' label from

> `elasticsearch_cluster_health_status{cluster="elasticsearch",color="green"} 1`  
>  `elasticsearch_cluster_health_status{cluster="elasticsearch",color="red"} 0`  
>  `elasticsearch_cluster_health_status{cluster="elasticsearch",color="yellow"} 0`

use the following parameters:

  * _Pattern_ \- `elasticsearch_cluster_health_status {cluster="elasticsearch"} == 1`
  * _Result processing_ \- select 'label'
  * _Label_ \- specify 'color'

The filter (based on the numeric value '1') will match the appropriate row, while the label will return the health status description (currently 'green'; but potentially also 'red' or 'yellow').

#### Prometheus to JSON

Data from Prometheus can be used for low-level discovery. In this case data in JSON format are needed and the _Prometheus to JSON_ preprocessing option will return exactly that.

For more details, see [Discovery using Prometheus data](/documentation/current/en/manual/discovery/low_level_discovery/examples/prometheus).

#### Query language comparison

The following table lists differences and similarities between PromQL and Zabbix Prometheus preprocessing query language.

**Differences**  
---  
Query target | Prometheus server | Plain text in Prometheus exposition format  
Returns | Instant vector | Metric or label value (Prometheus pattern)  
Array of metrics for single value in JSON (Prometheus to JSON)  
Label matching operators | **=** , **!=** , **=~** , **!~** | **=** , **!=** , **=~** , **!~**  
Regular expression used in label or metric name matching | RE2 | PCRE  
Comparison operators | See [list](https://prometheus.io/docs/prometheus/latest/querying/operators/#comparison-binary-operators) | Only **==** (equal) is supported for value filtering  
**Similarities**  
Selecting by metric name that equals string | <metric name> or {__name__="<metric name>"} | <metric name> or {__name__="<metric name>"}  
Selecting by metric name that matches regular expression | {__name__=~"<regex>"} | {__name__=~"<regex>"}  
Selecting by <label name> value that equals string | {<label name>="<label value>",...} | {<label name>="<label value>",...}  
Selecting by <label name> value that matches regular expression | {<label name>=~"<regex>",...} | {<label name>=~"<regex>",...}  
Selecting by value that equals string | {__name__=~".*"} == <value> | {__name__=~".*"} == <value>