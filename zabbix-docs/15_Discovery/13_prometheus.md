---
title: Discovery using Prometheus data
source: https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery/examples/prometheus
downloaded: 2025-11-14 10:37:37
---

# 13 Discovery using Prometheus data

#### Overview

Data provided in Prometheus line format can be used for low-level discovery.

See [Prometheus checks](/documentation/current/en/manual/config/items/itemtypes/prometheus) for details how Prometheus data querying is implemented in Zabbix.

#### Configuration

The low-level discovery rule should be created as a [dependent item](/documentation/current/en/manual/config/items/itemtypes/dependent_items) to the HTTP master item that collects Prometheus data.

##### Prometheus to JSON

In the discovery rule, go to the Preprocessing tab and select the _Prometheus to JSON_ preprocessing option. Data in JSON format are needed for discovery and the _Prometheus to JSON_ preprocessing option will return exactly that, with the following attributes:

  * metric name
  * metric value
  * help (if present)
  * type (if present)
  * labels (if present)
  * raw line

For example, querying `wmi_logical_disk_free_bytes`:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_rule_prom_json.png)

from these Prometheus lines:
    
    
    # HELP wmi_logical_disk_free_bytes Free space in bytes (LogicalDisk.PercentFreeSpace)
           # TYPE wmi_logical_disk_free_bytes gauge
           wmi_logical_disk_free_bytes{volume="C:"} 3.5180249088e+11
           wmi_logical_disk_free_bytes{volume="D:"} 2.627731456e+09
           wmi_logical_disk_free_bytes{volume="HarddiskVolume4"} 4.59276288e+08

Copy

✔ Copied

will return:
    
    
    [
               {
                   "name": "wmi_logical_disk_free_bytes",
                   "help": "Free space in bytes (LogicalDisk.PercentFreeSpace)",
                   "type": "gauge",
                   "labels": {
                       "volume": "C:"
                    },
                   "value": "3.5180249088e+11",
                   "line_raw": "wmi_logical_disk_free_bytes{volume=\"C:\"} 3.5180249088e+11"
               },
               {
                   "name": "wmi_logical_disk_free_bytes",
                   "help": "Free space in bytes (LogicalDisk.PercentFreeSpace)",
                   "type": "gauge",
                   "labels": {
                       "volume": "D:"
                    },
                   "value": "2.627731456e+09",
                   "line_raw": "wmi_logical_disk_free_bytes{volume=\"D:\"} 2.627731456e+09"
               },
               {
                   "name": "wmi_logical_disk_free_bytes",
                   "help": "Free space in bytes (LogicalDisk.PercentFreeSpace)",
                   "type": "gauge",
                   "labels": {
                       "volume": "HarddiskVolume4"
                    },
                   "value": "4.59276288e+08",
                   "line_raw": "wmi_logical_disk_free_bytes{volume=\"HarddiskVolume4\"} 4.59276288e+08"
               }
           ]

Copy

✔ Copied

##### Mapping LLD macros

Next you have to go to the LLD macros tab and make the following mappings:
    
    
    {#VOLUME}=$.labels['volume']
           {#METRIC}=$['name']
           {#HELP}=$['help']

Copy

✔ Copied

##### Item prototype

You may want to create an item prototype like this:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_item_prototype_prom.png)

with preprocessing options:

![](/documentation/current/assets/en/manual/discovery/low_level_discovery/lld_item_prototype_prom_b.png)