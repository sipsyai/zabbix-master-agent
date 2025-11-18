---
title: Version compatibility
source: https://www.zabbix.com/documentation/current/en/manual/appendix/compatibility
downloaded: 2025-11-14 10:47:55
---

# 10 Version compatibility

#### Supported agents

To be compatible with Zabbix 7.4, Zabbix agent must not be older than version 1.4 and must not be newer than 7.4.

You may need to review the configuration of older agents as some parameters have changed, for example, parameters related to [logging](https://www.zabbix.com/documentation/3.0/manual/installation/upgrade_notes_300#changes_in_configuration_parameters_related_to_logging) for versions before 3.0.

To take full advantage of the latest functionality, metrics, improved performance and reduced memory usage, use the latest supported agent.

**Notes for Windows XP**

  * On 32-bit Windows XP, do not use Zabbix agents newer than 6.0.x;
  * On Windows XP/Server 2003, do not use agent templates that are newer than Zabbix 4.0.x. The newer templates use English performance counters, which are only supported since Windows Vista/Server 2008.

#### Supported agents 2

Older Zabbix agents 2 from version 4.4 onwards are compatible with Zabbix 7.4; Zabbix agent 2 must not be newer than 7.4.

Note that when using Zabbix agent 2 versions 4.4 and 5.0, the default interval of 10 minutes is used for refreshing unsupported items.

To take full advantage of the latest functionality, metrics, improved performance and reduced memory usage, use the latest supported agent 2.

#### Supported Zabbix proxies

For full compatibility with Zabbix 7.4, proxies must match the server's major version. Only Zabbix 7.4.x proxies are fully compatible with a Zabbix 7.4.x server.

Outdated proxies are partially supported: they can still collect data and execute scripts but cannot receive configuration updates, such as new items.

In relation to Zabbix server, proxies can be:

  * _Current_ (proxy and server have the same major version);
  * _Outdated_ (proxy version is older than server version, but is partially supported);
  * _Unsupported_ (proxy version is older than server previous LTS release version _or_ proxy version is newer than server major version).

Examples:

6.4 | 6.4 | 6.0, 6.2 | Older than 6.0; newer than 6.4  
---|---|---|---  
7.0 | 7.0 | 6.0, 6.2, 6.4 | Older than 6.0; newer than 7.0  
7.2 | 7.2 | 7.0 | Older than 7.0; newer than 7.2  
7.4 | 7.4 | 7.0 | Older than 7.0; newer than 7.4  
  
Functionality supported by proxies:

_Current_ | Yes | Yes | Yes  
---|---|---|---  
_Outdated_ | Yes | No | [Remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command) (e.g., shell scripts);  
Immediate item value checks (i.e., _[Execute now](/documentation/current/en/manual/config/items/check_now)_);  
Note: Preprocessing [tests with a real value](/documentation/current/en/manual/config/items/preprocessing/testing#testing-real-value) are not supported.  
_Unsupported_ | No | No | No  
  
Warnings about using incompatible Zabbix daemon versions are logged.

#### Supported XML files

XML files not older than version 1.8 are supported for import in Zabbix 7.4.

In the XML export format, trigger dependencies are stored by name only. If there are several triggers with the same name (for example, having different severities and expressions) that have a dependency defined between them, it is not possible to import them. Such dependencies must be manually removed from the XML file and re-added after import.