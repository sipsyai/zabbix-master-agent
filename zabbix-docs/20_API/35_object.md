---
title: Correlation object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/correlation/object
downloaded: 2025-11-14 10:40:28
---

# Correlation object

The following objects are directly related to the `correlation` API.

### Correlation

The correlation object has the following properties.

correlationid | ID | ID of the correlation.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
name | string | Name of the correlation.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
description | string | Description of the correlation.  
status | integer | Whether the correlation is enabled or disabled.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
  
### Correlation operation

The correlation operation object defines an operation that will be performed when a correlation is executed. It has the following properties.

type | integer | Type of operation.  
  
Possible values:  
0 - close old events;  
1 - close new event.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
  
### Correlation filter

The correlation filter object defines a set of conditions that must be met to perform the configured correlation operations. It has the following properties.

conditions | array | Set of filter conditions to use for filtering results. The conditions will be sorted in the order of their placement in the formula.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
evaltype | integer | Filter condition [evaluation method](/documentation/current/en/manual/config/event_correlation/global#configuration).  
  
Possible values:  
0 - And/Or;  
1 - And;  
2 - Or;  
3 - Custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
eval_formula | string | Generated expression that will be used for evaluating filter conditions. The expression contains IDs that reference specific filter conditions by its `formulaid`. The value of `eval_formula` is equal to the value of `formula` for filters with a custom expression.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
formula | string | User-defined expression to be used for evaluating conditions of filters with a custom expression. The expression must contain IDs that reference specific filter conditions by its `formulaid`. The IDs used in the expression must exactly match the ones defined in the filter conditions: no condition can remain unused or omitted.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `evaltype` is set to "custom expression"  
  
#### Correlation filter condition

The correlation filter condition object defines a specific condition that must be checked before running the correlation operations.

type | integer | Type of condition.  
  
Possible values:  
0 - old event tag;  
1 - new event tag;  
2 - new event host group;  
3 - event tag pair;  
4 - old event tag value;  
5 - new event tag value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
tag | string | Event tag (old or new).  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "old event tag", "new event tag", "old event tag value", or "new event tag value"  
groupid | ID | ID of the host group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "new event host group"  
oldtag | string | Old event tag.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "event tag pair"  
newtag | string | Old event tag.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "event tag pair"  
value | string | Event tag (old or new) value.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "old event tag value" or "new event tag value"  
formulaid | string | Arbitrary unique ID that is used to reference the condition from a custom expression. Can only contain capital-case letters. The ID must be defined by the user when modifying filter conditions, but will be generated anew when requesting them afterward.  
operator | integer | Condition operator.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `type` is set to "new event host group", "old event tag value", or "new event tag value"  
  
To better understand how to use filters with various types of expressions, see examples on the [correlation.get](get#retrieve-correlations) and [correlation.create](create#using-a-custom-expression-filter) method pages.

The following operators and values are supported for each condition type.

2 | Host group | =, <> | Host group ID.  
---|---|---|---  
4 | Old event tag value | =, <>, like, not like | string  
5 | New event tag value | =, <>, like, not like | string