---
title: Extensions
source: https://www.zabbix.com/documentation/current/en/manual/extensions
downloaded: 2025-11-14 10:46:17
---

# 21 Extensions

#### Overview

Although Zabbix offers a multiplicity of features, there is always room for additional functionality. Extensions are a convenient way of modifying and enhancing the monitoring capabilities of Zabbix without changing its source code.

You can extend Zabbix functionality either by using built-in extension options (trapper items, user parameters, etc.) or by using or creating custom extensions (loadable modules, plugins, etc.).

This section provides an overview with references to all the options for extending Zabbix.

#### Data collection with custom commands

##### Trapper items

[Trapper items](/documentation/current/en/manual/config/items/itemtypes/trapper) are items that accept incoming data instead of querying for it. Trapper items are useful for sending specific data to Zabbix server or proxy, for example, periodic availability and performance data in the case of long-running user scripts. Sending data to Zabbix server or proxy is possible using the [Zabbix sender](/documentation/current/en/manual/concepts/sender) utility or Zabbix sender [protocol](/documentation/current/en/manual/appendix/protocols/zabbix_sender). Sending data to Zabbix server is also possible using the [`history.push`](/documentation/current/en/manual/api/reference/history/push) API method.

##### External checks

An [external check](/documentation/current/en/manual/config/items/itemtypes/external) is an item for executing checks by running an executable, for example, a [shell script](/documentation/current/en/manual/appendix/command_execution) or a binary.

External checks are executed by Zabbix server or proxy (when host is monitored by proxy), and do not require an agent running on the host being monitored.

##### User parameters

A [user parameter](/documentation/current/en/manual/config/items/userparameters) is a user-defined command (associated with a user-defined key) that, when executed, can retrieve the data you need from the host where Zabbix agent is running. User parameters are useful for configuring agent or agent 2 items that are not predefined in Zabbix.

##### `system.run[]` Zabbix agent items

`system.run[]` Zabbix [agent item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.run) is an item for a user-defined command (associated with a predefined key `system.run[]`, for example, `system.run[myscript.sh]`) that can be executed on the host where Zabbix agent is running.

Note: `system.run[]` items are disabled by default and, if used, must be enabled ([allowed](/documentation/current/en/manual/config/items/restrict_checks)) and defined in the Zabbix agent or agent 2 configuration file (`AllowKey` configuration parameter).

User-defined commands in items such as external checks, user parameters and `system.run[]` Zabbix agent items are executed from the OS user that is used to run Zabbix components. To execute these commands, this user must have the necessary permissions.

##### HTTP agent items

[HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http) item is an item for executing data requests over HTTP/HTTPS. HTTP agent items are useful for sending requests to HTTP endpoints to retrieve data from services such as _Elasticsearch_ and _OpenWeatherMap_ , for checking the status of Zabbix API or the status of Apache or Nginx web server, etc. HTTP agent items (with trapping enabled) can also function as trapper items.

##### Script items

A [script item](/documentation/current/en/manual/config/items/itemtypes/script) is an item for executing user-defined JavaScript code that retrieves data over HTTP/HTTPS. Script items are useful when the functionality provided by HTTP agent items is not enough. For example, in demanding data collection scenarios that require multiple steps or complex logic, a script item can be configured to make an HTTP call, then process the data received, and then pass the transformed value to a second HTTP call.

HTTP agent items and script items are supported by Zabbix server and proxy, and do not require an agent running on the host being monitored.

#### Advanced extensions

##### Loadable modules

[Loadable modules](/documentation/current/en/manual/extensions/loadablemodules), written in C, are a versatile and performance-minded option for extending the functionality of Zabbix components (server, proxy, agent) on UNIX platforms. A loadable module is basically a shared library used by Zabbix daemon and loaded on startup. The library should contain certain functions, so that a Zabbix process may detect that the file is indeed a module it can load and work with.

Loadable modules have a number of benefits, including the ability to add new metrics or implement any other logic (for example, Zabbix [history data export](/documentation/current/en/manual/extensions/loadablemodules#providing-history-export-callbacks)), great performance, and the option to develop, use and share the functionality they provide. It contributes to trouble-free maintenance and helps to deliver new functionality easier and independently of the Zabbix core code base.

Loadable modules are especially useful in a complex monitoring setup. When monitoring embedded systems, having a large number of monitored parameters or heavy scripts with complex logic or long startup time, extensions such as user parameters, `system.run[]` Zabbix agent items, and external checks will have an impact on performance. Loadable modules offer a way of extending Zabbix functionality without sacrificing performance.

##### Plugins

[Plugins](/documentation/current/en/manual/extensions/plugins) provide an alternative to loadable modules (written in C). However, plugins are a way to extend Zabbix agent 2 only.

A plugin is a _Go_ package that defines the structure and implements one or several plugin interfaces (_Exporter_ , _Collector_ , _Configurator_ , _Runner_ , _Watcher_). Two types of Zabbix agent 2 plugins are supported:

  * [Built-in plugins](https://www.zabbix.com/documentation/guidelines/en/plugins/built_in_plugins) (supported since Zabbix 4.4.0)
  * [Loadable plugins](https://www.zabbix.com/documentation/guidelines/en/plugins/loadable_plugins) (supported since Zabbix 6.0.0)

See the list of [built-in plugins](/documentation/current/en/manual/extensions/plugins#built-in).

For instructions and tutorials on writing your own plugins, see [Developer center](/documentation/current/en/devel/plugins).

#### Alert customization

##### Webhooks

A [webhook](/documentation/current/en/manual/config/notifications/media/webhook) is a Zabbix [media type](/documentation/current/en/manual/config/notifications/media) that provides an option to extend Zabbix alerting capabilities to external software such as helpdesk systems, chats, or messengers. Similarly to script items, webhooks are useful for making HTTP calls using custom JavaScript code, for example, to push notifications to different platforms such as Microsoft Teams, Discord, and Jira. It is also possible to return some data (for example, about created helpdesk tickets) that is then displayed in Zabbix.

Existing webhooks are available in the Zabbix [Git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/media?at=refs%2Fheads%2Frelease%2F7.4). For custom webhook development, see [Webhook development guidelines](https://www.zabbix.com/documentation/guidelines/en/webhooks).

##### Alert scripts

An [alert script](/documentation/current/en/manual/config/notifications/media/script) is a Zabbix [media type](/documentation/current/en/manual/config/notifications/media) that provides an option to create an alternative way (script) to handle Zabbix alerts. Alert scripts are useful if you are not satisfied with the existing media types for sending alerts in Zabbix.

#### Frontend customization

##### Custom themes

It is possible to change Zabbix frontend visual appearance by using custom themes. See the [instructions](/documentation/current/en/manual/web_interface/theming) on creating and applying your own themes.

##### Frontend modules

[Frontend modules](/documentation/current/en/manual/extensions/frontendmodules) provide an option to extend Zabbix frontend functionality by adding third-party modules or by developing your own. With frontend modules you can add new menu items, their respective views, actions, etc.

#### Global scripts

A [global script](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts) is a user-defined set of commands that can be executed on a monitoring target (by shell (/bin/sh) interpreter), depending on the configured scope and user permissions. Global scripts can be configured for the following actions:

  * Action [operation](/documentation/current/en/manual/config/notifications/action/operation)
  * [Manual host action](/documentation/current/en/manual/web_interface/menu/host_menu#overview)
  * [Manual event action](/documentation/current/en/manual/web_interface/menu/event_menu#content)

Global scripts are useful in many cases. For example, if configured for action operations or manual host actions, you can use global scripts to automatically or manually execute [remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command) such as restarting an application (web server, middleware, CRM, etc.) or freeing disk space (removing older files, cleaning `/tmp`, etc). Or, another example, if configured for manual event actions, you can use global scripts to manage problem tickets in external systems.

Global scripts can be executed by Zabbix server, proxy or agent.

User-defined commands are executed from the OS user that is used to run Zabbix components. To execute these commands, this user must have the necessary permissions.

#### Zabbix API

[Zabbix API](/documentation/current/en/manual/api) is an HTTP-based API that is part of Zabbix frontend. With Zabbix API, you can do any of the following operations:

  * Programmatically retrieve and modify the configuration of Zabbix.
  * Import and export Zabbix configuration.
  * Access Zabbix historical and trend data.
  * Configure applications to work with Zabbix.
  * Integrate Zabbix with third-party software.
  * Automate routine tasks.

Zabbix API consists of a multiplicity of methods that are nominally grouped into separate APIs. Each method performs a specific task. For the available methods, as well as an overview of the functions provided by Zabbix API, see Zabbix API [Method reference](/documentation/current/en/manual/api/reference).