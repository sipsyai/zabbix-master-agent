---
title: Secret user macros
source: https://www.zabbix.com/documentation/current/en/manual/config/macros/secret_macros
downloaded: 2025-11-14 10:36:32
---

# 4 Secret user macros

#### Overview

Zabbix provides two options for protecting sensitive information in user macro values:

  * Secret text
  * Vault secret

While the value of a secret macro is hidden, it can be revealed through use in items. For example, in an external script, an `echo` statement referencing a secret macro may be used to reveal the macro value to the frontend, because Zabbix server has access to the real macro value. See locations where secret macro values are unmasked.

Secret macros cannot be used in trigger expressions.

#### Secret text

With Secret text macros, the macro value is masked with asterisks.

To make a macro value secret, click on the button at the end of the _Value_ field and select the _Secret text_ option:

![](/documentation/current/assets/en/manual/config/macros/macro_value_type.png)

Once the configuration is saved, it will no longer be possible to view the value.

To change the macro value, hover over the _Value_ field and click the _Set new value_ button (appears on hover):

![](/documentation/current/assets/en/manual/config/macros/macro_type_secret2.png)

When you click the _Set new value_ button (or change the macro value type), the current value will be erased. You can restore the original value by clicking the ![](/documentation/current/assets/en/manual/config/macros/macro_type_secret3.png) arrow at the end of the _Value_ field (only available before saving the new configuration). Note that restoring the original value will not expose it.

URLs that contain a secret macro will not work, as the macro in them will be resolved as "******".

#### Vault secret

With Vault secret macros, the macro value is stored in an external secret management software (vault).

To configure a Vault secret macro, click on the button at the end of the _Value_ field and select the _Vault secret_ option:

![](/documentation/current/assets/en/manual/config/macros/macro_value_type1.png)

The macro value must point to a vault secret. The input format depends on the vault provider. For provider-specific configuration examples, see:

  * [HashiCorp](/documentation/current/en/manual/config/secrets/hashicorp#retrieving-user-macro-values)
  * [CyberArk](/documentation/current/en/manual/config/secrets/cyberark#user-macro-values)

Vault secret macro values are retrieved from the vault by Zabbix server (and Zabbix proxy, if _Resolve secret vault macros by_ is [set to](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) _Zabbix server and proxy_) on every refresh of configuration data and then stored in the configuration cache. Zabbix server and Zabbix proxy may use different vaults.

If _Resolve secret vault macros by_ is [set to](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) _Zabbix server_ , then vault secrets are retrieved by server only and Zabbix proxy receives values of Vault secret macros from Zabbix server on each configuration sync and stores them in its own configuration cache. That means a Zabbix proxy cannot start data collection after a restart until it receives the configuration update from Zabbix server.

To manually refresh secret values from the vault, use the `secrets_reload` [runtime control](/documentation/current/en/manual/concepts/server#runtime-control) option (server only).

Encryption must be enabled between Zabbix server and proxy; otherwise a server warning message is logged.

If a macro value cannot be retrieved successfully, the corresponding item using the value will turn unsupported.

#### Unmasked locations

This list provides locations of parameters where secret macro values are unmasked.

Secret macro values will remain masked in the locations below if referenced indirectly. For example, {ITEM.KEY}, {ITEM.KEY<1-9>}, {LLDRULE.KEY} [built-in macros](/documentation/current/en/manual/appendix/macros/supported_by_location#items) used in media types (Script or Webhook parameters) will resolve to item keys containing masked secret macros, such as `net.tcp.port[******,******]` instead of `net.tcp.port[192.0.2.0,80]`.

**Items, item prototypes, LLD rules**  
---  
| Item | _Item key parameters_  
Item prototype | _Item prototype key parameters_  
Low-level discovery rule | _Discovery item key parameters_  
SNMP agent | _SNMP community_  
_Context name_ (SNMPv3)  
_Security name_ (SNMPv3)  
_Authentication passphrase_ (SNMPv3)  
_Privacy passphrase_ (SNMPv3)  
HTTP agent | _URL_  
_Query fields_  
_Post_  
_Headers_  
_User name_  
_Password_  
_SSL key password_  
Script | _Parameters_  
_Script_  
Browser | _Parameters_  
_Script_  
Database monitor | _SQL query_  
TELNET agent | _Script_  
_User name_  
_Password_  
SSH agent | _Script_  
_User name_  
_Password_  
Simple check | _User name_  
_Password_  
JMX agent | _User name_  
_Password_  
**Item value preprocessing**  
| JavaScript preprocessing step | _Script_  
**Web scenarios**  
| Web scenario | _Variable value_  
_Header value_  
_URL_  
_Query field value_  
_Post field value_  
_Raw post_  
Web scenario authentication | _User_  
_Password_  
_SSL key password_  
**Connectors**  
| Connector | _URL_  
_Username_  
_Password_  
_Token_  
_HTTP proxy_  
_SSL certificate file_  
_SSL key file_  
_SSL key password_  
**Network discovery**  
| SNMP | _SNMP community_  
_Context name_ (SNMPv3)  
_Security name_ (SNMPv3)  
_Authentication passphrase_ (SNMPv3)  
_Privacy passphrase_ (SNMPv3)  
**Global scripts**  
| Webhook | _JavaScript script_  
_JavaScript script parameter value_  
Telnet | _Username_  
_Password_  
SSH | _Username_  
_Password_  
Script | _Script_  
**Media types**  
| Script | _Script parameters_  
Webhook | _Parameters_  
**IPMI management**  
| Host | _Username_  
_Password_