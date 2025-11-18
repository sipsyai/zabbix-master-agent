---
title: Configuring a host
source: https://www.zabbix.com/documentation/current/en/manual/config/hosts/host
downloaded: 2025-11-14 10:34:36
---

# 2 Configuring a host

#### Overview

To configure a host in Zabbix frontend, do the following:

  * Go to: _Data collection > Hosts_ or _Monitoring > Hosts_
  * Click on _Create host_ in the upper-right corner of the screen (or on the host name to edit an existing host)
  * Enter parameters of the host in the form

You can also use the _Clone_ button in the configuration form of an existing host to create a new host. This host will have all of the properties of the existing host, including linked templates, entities (items, triggers, etc.) from those templates, as well as the entities directly attached to the existing host.

Note that when a host is cloned, it will retain all template entities as they are originally on the template. Any changes to those entities made on the existing host level (such as changed item interval, modified regular expression or added prototypes to the low-level discovery rule) will not be cloned to the new host; instead they will be as on the template.

Alternatively, you can use the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard) to configure a host through a guided, step-by-step interface.

#### Configuration

The **Host** tab contains general host attributes:

![](/documentation/current/assets/en/manual/config/host_a.png)

All mandatory input fields are marked with a red asterisk.

_Host name_ | Enter a unique host name. Alphanumerics, spaces, dots, dashes and underscores are allowed. However, leading and trailing spaces are disallowed.  
_Note:_ With Zabbix agent running on the host you are configuring, the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd) parameter _Hostname_ must have the same value as the host name entered here. The name in the parameter is needed in the processing of [active checks](/documentation/current/en/manual/appendix/items/activepassive).  
---|---  
_Visible name_ | Enter a unique visible name for the host. If you set this name, it will be the one visible in lists, maps, etc instead of the technical host name. This attribute has UTF-8 support.  
_Templates_ | Link [templates](/documentation/current/en/manual/config/templates) to the host. All entities (items, triggers, [etc.](/documentation/current/en/manual/config/templates/linking)) will be inherited from the template.  
To link a new template, start typing the template name in the text input field. A list of matching templates will appear; scroll down to select. Alternatively, you may click on _Select_ next to the field and select templates from the list in a popup window. All selected templates will be linked to the host when the host configuration form is saved or updated.  
To unlink a template, use one of the two options in the _Linked templates_ block:  
_Unlink_ \- unlink the template, but preserve its entities (items, triggers, [etc.](/documentation/current/en/manual/config/templates/linking));  
_Unlink and clear_ \- unlink the template and remove all its entities (items, triggers, [etc.](/documentation/current/en/manual/config/templates/linking)).  
Listed template names are clickable links leading to the template configuration form.  
_Host groups_ | Select [host groups](/documentation/current/en/manual/config/hosts/host_groups) the host belongs to. A host must belong to at least one host group. A new group can be created and linked to the host by adding a non-existing group name.  
_Interfaces_ | Several host interface types are supported for a host: _Agent_ , _SNMP_ , _JMX_ and _IPMI_.  
No interfaces are defined by default. To add a new interface, click on _Add_ in the _Interfaces_ block, select the interface type and enter _IP/DNS_ , _Connect to_ and _Port_ info.  
_Note:_ Interfaces that are used in any items cannot be removed and link _Remove_ is grayed out for them.  
The "IP" or "DNS" from an SNMP interface is also used for [SNMP traps](/documentation/current/en/manual/config/items/itemtypes/snmptrap).  
During matching, only the selected "IP" or "DNS" in the host interface is used.  
See [Configuring SNMP monitoring](/documentation/current/en/manual/config/items/itemtypes/snmp#configuring-snmp-monitoring) for additional details on configuring an SNMP interface (v1, v2 and v3).  
| _IP address_ | Host IP address (optional).  
_DNS name_ | Host DNS name (optional).  
_Connect to_ | Clicking the respective button will tell Zabbix server what to use to retrieve data from agents:  
**IP** \- Connect to the host IP address (recommended)  
**DNS** \- Connect to the host DNS name  
_Port_ | TCP/UDP port number. Default values are: 10050 for Zabbix agent, 161 for SNMP agent, 12345 for JMX and 623 for IPMI.  
_Default_ | Check the radio button to set the default interface.  
_Description_ | Enter the host description.  
_Monitored by_ | Select if the host is monitored by:  
**Server** \- host is monitored by Zabbix server;  
**Proxy** \- host is monitored by standalone proxy;  
**Proxy group** \- host is monitored by proxy group.  
_Proxy_ | The assigned proxy name is displayed (only if Zabbix server has assigned one from the selected proxy group).  
This field is displayed only if the host is monitored by a proxy group.  
_Enabled_ | When the checkbox is checked, the host is enabled - ready for monitoring.  
  
When the checkbox is unchecked, the host is disabled - not monitored:  
For passive data requests initiated by Zabbix server/proxy (for example, [Zabbix agent](/documentation/current/en/manual/appendix/items/activepassive#passive-checks), [SNMP agent](/documentation/current/en/manual/config/items/itemtypes/snmp), [simple checks](/documentation/current/en/manual/config/items/itemtypes/simple_checks)), monitoring is disabled after configuration synchronization. Triggers and actions linked to the host are also disabled only after the configuration is reloaded.  
For Zabbix agent [active checks](/documentation/current/en/manual/appendix/items/activepassive#active-checks), monitoring stops within the time frame (approx. 5 seconds) that Zabbix agent receives information about the host having been disabled. During this brief interval, the host will continue to locally collect data for the active checks and try sending it to the server/proxy; however, since the host is marked as _Disabled_ , the server/proxy will reject the data.  
  
When you disable the host, its items are immediately removed from the history cache (except for their last values, which are kept for logs).  
  
The **IPMI** tab contains IPMI management attributes.

_Authentication algorithm_ | Select the authentication algorithm.  
---|---  
_Privilege level_ | Select the privilege level.  
_Username_ | User name for authentication. User macros may be used.  
_Password_ | Password for authentication. User macros may be used.  
  
The **Tags** tab allows you to define host-level [tags](/documentation/current/en/manual/config/tagging). All problems of this host will be tagged with the values entered here.

![](/documentation/current/assets/en/manual/config/host_d.png)

User macros, {INVENTORY.*} macros, {HOST.HOST}, {HOST.NAME}, {HOST.CONN}, {HOST.DNS}, {HOST.IP}, {HOST.PORT} and {HOST.ID} macros are supported in tags.

The **Macros** tab allows you to define host-level [user macros](/documentation/current/en/manual/config/macros/user_macros) as a name-value pairs. Note that macro values can be kept as plain text, secret text or Vault secret. Adding a description is also supported.

![](/documentation/current/assets/en/manual/config/host_e.png)

You may also view here template-level and global user macros if you select the _Inherited and host macros_ option. That is where all defined user macros for the host are displayed with the value they resolve to as well as their origin.

![](/documentation/current/assets/en/manual/config/host_e2.png)

For convenience, links to respective templates and global macro configuration are provided. It is also possible to edit a template/global macro on the host level, effectively creating a copy of the macro on the host.

The **Inventory** tab allows you to manually enter [inventory](inventory) information for the host. You can also select to enable _Automatic_ inventory population, or disable inventory population for this host.

![](/documentation/current/assets/en/manual/config/host_f.png)

If inventory is enabled (manual or automatic), a green dot is displayed with the tab name.

##### Encryption

The **Encryption** tab allows you to require [encrypted](/documentation/current/en/manual/encryption) connections with the host.

_Connections to host_ | How Zabbix server or proxy connects to Zabbix agent on a host: no encryption (default), using PSK (pre-shared key) or certificate.  
---|---  
_Connections from host_ | Select what type of connections are allowed from the host (i.e. from Zabbix agent and Zabbix sender). Several connection types can be selected at the same time (useful for testing and switching to other connection type). Default is "No encryption".  
_Issuer_ | Allowed issuer of certificate. Certificate is first validated with CA (certificate authority). If it is valid, signed by the CA, then the _Issuer_ field can be used to further restrict allowed CA. This field is intended to be used if your Zabbix installation uses certificates from multiple CAs. If this field is empty then any CA is accepted.  
_Subject_ | Allowed subject of certificate. Certificate is first validated with CA. If it is valid, signed by the CA, then the _Subject_ field can be used to allow only one value of _Subject_ string. If this field is empty then any valid certificate signed by the configured CA is accepted.  
_PSK identity_ | Pre-shared key identity string.  
Do not put sensitive information in the PSK identity, it is transmitted unencrypted over the network to inform a receiver which PSK to use.  
_PSK_ | Pre-shared key (hex-string). Maximum length: 512 hex-digits (256-byte PSK) if Zabbix uses GnuTLS or OpenSSL library, 64 hex-digits (32-byte PSK) if Zabbix uses mbed TLS (PolarSSL) library. Example: 1f87b595725ac58dd977beef14b97461a7c1045b9a1c963065002c5473194952  
  
##### Value mapping

The **Value mapping** tab allows to configure human-friendly representation of item data in [value mappings](/documentation/current/en/manual/config/items/mapping).