---
title: Host object
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/host/object
downloaded: 2025-11-14 10:41:55
---

# Host object

The following objects are directly related to the host API.

### Host

The host object has the following properties.

hostid | ID | ID of the host.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
\- _required_ for update operations  
---|---|---  
host | string | Technical name of the host.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ for create operations  
description | text | Description of the host.  
flags | integer | [Origin](/documentation/current/en/manual/api/reference_commentary#entity-origin-flags) of the host.  
  
Possible values:  
0 - a plain host;  
4 - a host converted from prototype.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
inventory_mode | integer | Host inventory population mode.  
  
Possible values:  
-1 - _(default)_ disabled;  
0 - manual;  
1 - automatic.  
ipmi_authtype | integer | IPMI authentication algorithm.  
  
Possible values:  
-1 - _(default)_ default;  
0 - none;  
1 - MD2;  
2 - MD5  
4 - straight;  
5 - OEM;  
6 - RMCP+.  
ipmi_password | string | IPMI password.  
ipmi_privilege | integer | IPMI privilege level.  
  
Possible values:  
1 - callback;  
2 - _(default)_ user;  
3 - operator;  
4 - admin;  
5 - OEM.  
ipmi_username | string | IPMI username.  
maintenance_from | timestamp | Starting time of the effective maintenance.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
maintenance_status | integer | Effective maintenance status.  
  
Possible values:  
0 - _(default)_ no maintenance;  
1 - maintenance in effect.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
maintenance_type | integer | Effective maintenance type.  
  
Possible values:  
0 - _(default)_ maintenance with data collection;  
1 - maintenance without data collection.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
maintenanceid | ID | ID of the maintenance that is currently in effect on the host.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
name | string | Visible name of the host.  
  
Default: `host` property value.  
monitored_by | integer | Source that is used to monitor the host.  
  
Possible values:  
0 - _(default)_ Zabbix server;  
1 - Proxy;  
2 - Proxy group.  
proxyid | ID | ID of the proxy that is used to monitor the host.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `monitored_by` is set to "Proxy"  
proxy_groupid | ID | ID of the proxy group that is used to monitor the host.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_ if `monitored_by` is set to "Proxy group"  
status | integer | Status and function of the host.  
  
Possible values:  
0 - _(default)_ enabled;  
1 - disabled.  
tls_connect | integer | Connections to host.  
  
Possible values:  
1 - _(default)_ No encryption;  
2 - PSK;  
4 - certificate.  
tls_accept | integer | Connections from host.  
  
Possible bitmap values:  
1 - _(default)_ No encryption;  
2 - PSK;  
4 - certificate.  
  
This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 6 for PSK and certificate).  
tls_issuer | string | Certificate issuer.  
tls_subject | string | Certificate subject.  
tls_psk_identity | string | PSK identity; must be paired with only one PSK (across [autoregistration](/documentation/current/en/manual/api/reference/autoregistration/object), [hosts](/documentation/current/en/manual/api/reference/host/object), and [proxies](/documentation/current/en/manual/api/reference/proxy/object)).  
  
Do not include sensitive information in the PSK identity, as it is sent unencrypted over the network to inform the receiver which PSK to use.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
\- _required_ if `tls_connect` is set to "PSK", or `tls_accept` contains the "PSK" bit  
tls_psk | string | Pre-shared key (PSK); must be at least 32 hex digits.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _write-only_  
\- _required_ if `tls_connect` is set to "PSK", or `tls_accept` contains the "PSK" bit  
active_available | integer | Host active interface availability status.  
  
Possible values:  
0 - interface status is unknown;  
1 - interface is available;  
2 - interface is not available.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
assigned_proxyid | ID | ID of the proxy assigned by Zabbix server, if the host is monitored by a proxy group.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_  
  
### Host inventory

The host inventory object has the following properties.

Each property has it's own unique ID number, which is used to associate host inventory fields with items.

4 | alias | string | Alias. | 128 characters  
---|---|---|---|---  
11 | asset_tag | string | Asset tag. | 64 characters  
28 | chassis | string | Chassis. | 64 characters  
23 | contact | string | Contact person. | 65535 characters for SQL databases  
32 | contract_number | string | Contract number. | 64 characters  
47 | date_hw_decomm | string | HW decommissioning date. | 64 characters  
46 | date_hw_expiry | string | HW maintenance expiry date. | 64 characters  
45 | date_hw_install | string | HW installation date. | 64 characters  
44 | date_hw_purchase | string | HW purchase date. | 64 characters  
34 | deployment_status | string | Deployment status. | 64 characters  
14 | hardware | string | Hardware. | 255 characters  
15 | hardware_full | string | Detailed hardware. | 65535 characters for SQL databases  
39 | host_netmask | string | Host subnet mask. | 39 characters  
38 | host_networks | string | Host networks. | 65535 characters for SQL databases  
40 | host_router | string | Host router. | 39 characters  
30 | hw_arch | string | HW architecture. | 32 characters  
33 | installer_name | string | Installer name. | 64 characters  
24 | location | string | Location. | 65535 characters for SQL databases  
25 | location_lat | string | Location latitude. | 16 characters  
26 | location_lon | string | Location longitude. | 16 characters  
12 | macaddress_a | string | MAC address A. | 64 characters  
13 | macaddress_b | string | MAC address B. | 64 characters  
29 | model | string | Model. | 64 characters  
3 | name | string | Name. | 128 characters  
27 | notes | string | Notes. | 65535 characters for SQL databases  
41 | oob_ip | string | OOB IP address. | 39 characters  
42 | oob_netmask | string | OOB host subnet mask. | 39 characters  
43 | oob_router | string | OOB router. | 39 characters  
5 | os | string | OS name. | 128 characters  
6 | os_full | string | Detailed OS name. | 255 characters  
7 | os_short | string | Short OS name. | 128 characters  
61 | poc_1_cell | string | Primary POC mobile number. | 64 characters  
58 | poc_1_email | string | Primary email. | 128 characters  
57 | poc_1_name | string | Primary POC name. | 128 characters  
63 | poc_1_notes | string | Primary POC notes. | 65535 characters for SQL databases  
59 | poc_1_phone_a | string | Primary POC phone A. | 64 characters  
60 | poc_1_phone_b | string | Primary POC phone B. | 64 characters  
62 | poc_1_screen | string | Primary POC screen name. | 64 characters  
68 | poc_2_cell | string | Secondary POC mobile number. | 64 characters  
65 | poc_2_email | string | Secondary POC email. | 128 characters  
64 | poc_2_name | string | Secondary POC name. | 128 characters  
70 | poc_2_notes | string | Secondary POC notes. | 65535 characters for SQL databases  
66 | poc_2_phone_a | string | Secondary POC phone A. | 64 characters  
67 | poc_2_phone_b | string | Secondary POC phone B. | 64 characters  
69 | poc_2_screen | string | Secondary POC screen name. | 64 characters  
8 | serialno_a | string | Serial number A. | 64 characters  
9 | serialno_b | string | Serial number B. | 64 characters  
48 | site_address_a | string | Site address A. | 128 characters  
49 | site_address_b | string | Site address B. | 128 characters  
50 | site_address_c | string | Site address C. | 128 characters  
51 | site_city | string | Site city. | 128 characters  
53 | site_country | string | Site country. | 64 characters  
56 | site_notes | string | Site notes. | 65535 characters for SQL databases  
55 | site_rack | string | Site rack location. | 128 characters  
52 | site_state | string | Site state. | 64 characters  
54 | site_zip | string | Site ZIP/postal code. | 64 characters  
16 | software | string | Software. | 255 characters  
18 | software_app_a | string | Software application A. | 64 characters  
19 | software_app_b | string | Software application B. | 64 characters  
20 | software_app_c | string | Software application C. | 64 characters  
21 | software_app_d | string | Software application D. | 64 characters  
22 | software_app_e | string | Software application E. | 64 characters  
17 | software_full | string | Software details. | 65535 characters for SQL databases  
10 | tag | string | Tag. | 64 characters  
1 | type | string | Type. | 64 characters  
2 | type_full | string | Type details. | 64 characters  
35 | url_a | string | URL A. | 2048 characters  
36 | url_b | string | URL B. | 2048 characters  
37 | url_c | string | URL C. | 2048 characters  
31 | vendor | string | Vendor. | 64 characters  
  
### Host tag

The host tag object has the following properties.

tag | string | Host tag name.  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _required_  
---|---|---  
value | string | Host tag value.  
automatic | integer | Type of host tag.  
  
Possible values:  
0 - _(default)_ manual (tag created by user);  
1 - automatic (tag created by low-level discovery)  
  
[Property behavior](/documentation/current/en/manual/api/reference_commentary#property-behavior):  
\- _read-only_