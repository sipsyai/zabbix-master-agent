---
title: Audit log object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/auditlog/object
downloaded: 2025-11-14 10:40:07
---

# Audit log object

The following objects are directly related to the `auditlog` API.

### Audit log

The audit log object contains information about user actions. It has the following properties.

auditid | ID | ID of audit log entry. Generated using CUID algorithm.  
---|---|---  
userid | ID | Audit log entry author userid.  
username | string | Audit log entry author username.  
clock | timestamp | Audit log entry creation timestamp.  
ip | string | Audit log entry author IP address.  
action | integer | Audit log entry action.  
  
Possible values:  
0 - Add;  
1 - Update;  
2 - Delete;  
4 - Logout;  
7 - Execute;  
8 - Login;  
9 - Failed login;  
10 - History clear;  
11 - Config refresh;  
12 - Push.  
resourcetype | integer | Audit log entry resource type.  
  
Possible values:  
0 - User;  
3 - Media type;  
4 - Host;  
5 - Action;  
6 - Graph;  
11 - User group;  
13 - Trigger;  
14 - Host group;  
15 - Item;  
16 - Image;  
17 - Value map;  
18 - Service;  
19 - Map;  
22 - Web scenario;  
23 - Discovery rule;  
25 - Script;  
26 - Proxy;  
27 - Maintenance;  
28 - Regular expression;  
29 - Macro;  
30 - Template;  
31 - Trigger prototype;  
32 - Icon mapping;  
33 - Dashboard;  
34 - Event correlation;  
35 - Graph prototype;  
36 - Item prototype;  
37 - Host prototype;  
38 - Autoregistration;  
39 - Module;  
40 - Settings;  
41 - Housekeeping;  
42 - Authentication;  
43 - Template dashboard;  
44 - User role;  
45 - API token;  
46 - Scheduled report;  
47 - High availability node;  
48 - SLA;  
49 - User directory;  
50 - Template group;  
51 - Connector;  
52 - LLD rule;  
53 - History;  
54 - Multi-factor authentication;  
55 - Proxy group;  
56 - LLD rule prototype.  
resourceid | ID | Audit log entry resource identifier.  
resourcename | string | Audit log entry resource human readable name.  
recordsetid | ID | Audit log entry recordset ID. The audit log records created during the same operation will have the same recordset ID. Generated using CUID algorithm.  
details | text | Audit log entry details. The details are stored as a JSON object, where each property name is a path to the property or nested object in which the change occurred, and where each value contains the data (in array format) about the change in this property or nested object.  
  
Possible value formats:  
["add"] - Nested object has been added;  
["add", "<value>"] - The property of the added object equals <value>;  
["update"] - Nested object has been updated;  
["update", "<new value>", "<old value>"] - The property of the updated object was changed from <old value> to <new value>;  
["delete"] - Nested object has been deleted.