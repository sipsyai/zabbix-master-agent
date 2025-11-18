---
title: CSV to JSON preprocessing
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/csv_to_json
downloaded: 2025-11-14 10:34:53
---

# 6 CSV to JSON preprocessing  
  
#### Overview

In this preprocessing step it is possible to convert CSV file data into JSON format. It's supported in:

  * items (item prototypes)
  * low-level discovery rules

#### Configuration

To configure a CSV to JSON preprocessing step:

  * Go to the Preprocessing tab in [item](/documentation/current/en/manual/config/items/preprocessing)/[discovery rule](/documentation/current/en/manual/discovery/low_level_discovery#preprocessing) configuration
  * Click on _Add_
  * Select the _CSV to JSON_ option

![](/documentation/current/assets/en/manual/appendix/csv_to_json_params.png)

The first parameter allows to set a custom delimiter. Note that if the first line of CSV input starts with "Sep=" and is followed by a single UTF-8 character then that character will be used as the delimiter in case the first parameter is not set. If the first parameter is not set and a delimiter is not retrieved from the "Sep=" line, then a comma is used as a separator.

The second optional parameter allows to set a quotation symbol.

If the _With header row_ checkbox is marked, the header line values will be interpreted as column names (see Header processing for more information).

If the _Custom on fail_ checkbox is marked, the item will not become unsupported in case of a failed preprocessing step. Additionally, custom error handling options may be set: discard the value, set a specified value or set a specified error message.

#### Header processing

The CSV file header line can be processed in two different ways:

  * If the _With header row_ checkbox is marked - header line values are interpreted as column names. In this case the column names must be unique and the data row should not contain more columns than the header row.
  * If the _With header row_ checkbox is not marked - the header line is interpreted as data. Column names are generated automatically (1,2,3,4...).

CSV file example:
    
    
    Nr,Item name,Key,Qty
           1,active agent item,agent.hostname,33
           "2","passive agent item","agent.version","44"
           3,"active,passive agent items",agent.ping,55

Copy

✔ Copied

A quotation character within a quoted field in the input must be escaped by preceding it with another quotation character.

**Processing header line**

JSON output when a header line is expected:
    
    
    [
              {
                 "Nr":"1",
                 "Item name":"active agent item",
                 "Key":"agent.hostname",
                 "Qty":"33"
              },
              {
                 "Nr":"2",
                 "Item name":"passive agent item",
                 "Key":"agent.version",
                 "Qty":"44"
              },
              {
                 "Nr":"3",
                 "Item name":"active,passive agent items",
                 "Key":"agent.ping",
                 "Qty":"55"
              }
           ]

Copy

✔ Copied

**No header line processing**

JSON output when a header line is not expected:
    
    
    [
              {
                 "1":"Nr",
                 "2":"Item name",
                 "3":"Key",
                 "4":"Qty"
              },
              {
                 "1":"1",
                 "2":"active agent item",
                 "3":"agent.hostname",
                 "4":"33"
              },
              {
                 "1":"2",
                 "2":"passive agent item",
                 "3":"agent.version",
                 "4":"44"
              },
              {
                 "1":"3",
                 "2":"active,passive agent items",
                 "3":"agent.ping",
                 "4":"55"
              }
           ]

Copy

✔ Copied