---
title: Escaping special characters from LLD macro values in JSONPath
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/jsonpath_functionality/escaping_lld_macros
downloaded: 2025-11-14 10:34:49
---

# 1 Escaping special characters from LLD macro values in JSONPath  
  
When low-level discovery macros are used in JSONPath preprocessing and their values are resolved, the following rules of escaping special characters are applied:

  * only backslash (\\) and double quote (") characters are considered for escaping;
  * if the resolved macro value contains these characters, each of them is escaped with a backslash;
  * if they are already escaped with a backslash, it is not considered as escaping and both the backslash and the following special characters are escaped once again.

For example:

$.[?(@.value == "{#MACRO}")] | special "value" | $.[?(@.value == "special \"value\"")]  
---|---|---  
c:\temp | $.[?(@.value == "c:\\\temp")]  
a\\\b | $.[?(@.value == "a\\\\\\\b")]  
  
When used in the expression, the macro that may have special characters should be enclosed in double quotes:

$.[?(@.value == "{#MACRO}")] | special "value" | $.[?(@.value == "special \"value\"")] | OK  
---|---|---|---  
$.[?(@.value == {#MACRO})] | $.[?(@.value == special \"value\")] | **Bad JSONPath expression**  
  
When used in the path, the macro that may have special characters should be enclosed in square brackets **and** double quotes:

$.["{#MACRO}"].value | c:\temp | $.["c:\\\temp"].value | OK  
---|---|---|---  
$.{#MACRO}.value | $.c:\\\temp.value | **Bad JSONPath expression**