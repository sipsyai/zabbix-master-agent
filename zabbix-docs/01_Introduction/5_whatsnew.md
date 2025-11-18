---
title: What's new in Zabbix 7.4.0
source: https://www.zabbix.com/documentation/current/en/manual/introduction/whatsnew
downloaded: 2025-11-14 10:33:44
---

# 5 What's new in Zabbix 7.4.0

See [breaking changes](/documentation/current/en/manual/installation/upgrade_notes#breaking-changes) for this version.

#### Nested low-level discovery

It is now possible to create multi-level discovery of objects with the introduction of [discovery prototypes](/documentation/current/en/manual/discovery/low_level_discovery/discovery_prototypes) within a low-level discovery rule. For example, you may want to discover all database instances on a database server, then discover tablespaces for each instance, then discover tables for each tablespace.

Discovery prototypes are nested discovery rules within a "parent" discovery rule. Discovery prototypes have their own item, trigger, graph, host, and discovery prototypes.

A nested discovery prototype may use the same JSON value as the parent rule, but then use a different "slice" of data from the JSON value.

The levels of nesting for discovery prototypes are unlimited.

#### Host prototypes on discovered hosts

Host prototypes are now supported on [discovered hosts](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes#discovered-hosts), enabling Zabbix to automatically discover and monitor entities within other discovered entities (e.g., hypervisors, their virtual machines, and containers inside those virtual machines).

You can create host prototypes on discovered hosts by creating low-level discovery rules with host prototypes or by linking a template with host prototypes. Alternatively, you can link a template to the host prototype used for discovery, which will cause discovered hosts to inherit the host prototypes from the template.

If your current configuration includes host prototypes that use templates containing other host prototypes, please see [Upgrade notes](/documentation/current/en/manual/installation/upgrade_notes#host-prototypes-on-discovered-hosts).

#### OAuth 2.0 authentication

OAuth 2.0 authentication is now supported for the SMTP protocol. To configure OAuth authentication, select "OAuth" in the Authentication parameter when configuring an email [media type](/documentation/current/en/manual/config/notifications/media/email#configuration) and then specify parameters for the OAuth [token retrieval](/documentation/current/en/manual/config/notifications/media/email#oauth-tokens).

The retrieval of OAuth tokens has [automated features](/documentation/current/en/manual/config/notifications/media/email/gmail_office#oauth-tokens) for **Gmail** , **Gmail relay** and **Office365** email providers. It is only required to supply _Redirection endpoint_ , _Client ID_ and _Client secret_ parameter values. Zabbix will automatically fill the other required values (see [OAuth URL defaults by provider](/documentation/current/en/manual/config/notifications/media/email/gmail_office#oauth-url-defaults-by-provider)).

#### Host Wizard

The new [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard) introduces a guided, step-by-step interface for setting up your monitoring target (device, application, service, etc.) in Zabbix. It simplifies the configuration of new or existing hosts by walking users through key steps such as selecting a template, installing Zabbix agent, adding host interfaces, and more.

![](/documentation/current/assets/en/manual/introduction/host_wizard_template.png)

The Host Wizard can be accessed from [Data collection > Hosts](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts) or the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu) in various frontend sections.

If you're upgrading from an earlier Zabbix version, templates must be upgraded to work with the Host Wizard. For instructions, see [Template upgrade](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade).

## Widgets

#### Item card

The [Item card](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_card) widget has been added to dashboard widgets, offering a convenient way to view comprehensive information about a single item at a glance.

![](/documentation/current/assets/en/manual/introduction/item_card_new.png)

#### Item history

In the [Item history](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/item_history) widget the scrolling position will now be bottom if new values are configured to be positioned at the bottom. This is useful for reading the latest values of logs.

#### Real-time widget editing

While [editing widgets](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#editing-widgets), you can now preview widget configuration changes in real time. Additionally, widget configuration forms are now draggable, allowing you to reposition them as needed.

Note that the graph preview in the [graph widget](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph#configuration) form has been removed.

## Items

#### ICMP ping item with retry option

A new `icmppingretry[<target>,<retries>,<backoff>,<size>,<timeout>,<options>]` [simple check](/documentation/current/en/manual/config/items/itemtypes/simple_checks#icmppingretry) has been added for host accessibility monitoring by ICMP ping with the ability to modify retries.

## Functions

#### Timestamp tracking

New [history functions](/documentation/current/en/manual/appendix/functions/history) have been added for timestamp tracking:

  * `firstclock` \- timestamp of the oldest value within the defined evaluation period;
  * `lastclock` \- timestamp of the Nth most recent value within the defined evaluation period;
  * `logtimestamp` \- log message timestamp of the Nth most recent log item value.

## Macros

#### Item value time tracking

New [macros](/documentation/current/en/manual/appendix/macros/supported_by_location#items) have been added for item-value time tracking:

{ITEM.LASTVALUE.AGE} | The time that elapsed between the latest item value collection and macro evaluation.  
---|---  
{ITEM.LASTVALUE.DATE} | The date when the latest item value was collected.  
{ITEM.LASTVALUE.TIME} | The time when the latest item value was collected.  
{ITEM.LASTVALUE.TIMESTAMP} | The timestamp when the latest item value was collected.  
{ITEM.VALUE.AGE} | The time that elapsed between the item value collection and macro evaluation.  
{ITEM.VALUE.DATE} | The date when the item value was collected.  
{ITEM.VALUE.TIME} | The time when the item value was collected.  
{ITEM.VALUE.TIMESTAMP} | The timestamp when the item value was collected.  
  
## Notifications

#### Separate menu section for user notifications

For better visibility of user media, user notifications now have their own [menu section](/documentation/current/en/manual/web_interface/user_profile) under _User settings_.

![](/documentation/current/assets/en/manual/web_interface/user_settings_menu.png)

The new Notifications section contains two tabs - _Media_ and _Frontend notifications_ , which previously were part of the user profile section.

#### Managing own user media

All users are now allowed to manage their own media by default.

However, user permissions to change media details for themselves can be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit own media_ option).

Additionally, Super admin user permissions to change media details for others can also be granted/revoked based on their [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) (see _Create and edit user media_ option).

## Maps

#### Auto-hide labels

It is now possible to configure map element/link labels to be displayed only when they are hovered on or selected. This setting helps to reduce visual clutter in maps with many elements close to each other.

Auto-hiding of labels can be configured for all map elements/links globally or for an individual map element/link.

#### Proportional scaling of background images

It is now possible to proportionally scale background images to fit the map size.

#### Element ordering

It is now possible to bring one element in front of the other (or vice versa) by clicking on the element with the right mouse button and selecting _Bring forward_ /_Bring to front_ or _Send backward_ /_Send to back_ options.

![](/documentation/current/assets/en/manual/config/visualization/map_element_menu.png)

Additionally, if map elements contain both a link between them and a highlight, the link will now appear below the highlight.

#### Link indicators based on item value

In the previous versions it was possible to adjust link style and color if some trigger went into a problem state. Now similar functionality is available based on item values.

It is possible to have link style and color adjusted if an item value:

  * reaches a defined threshold (for numeric items);
  * matches a regular expression (for text items).

![](/documentation/current/assets/en/manual/introduction/value_as_indicator.png)

## Processes

#### Managing history cache

In some data collection scenarios, specific items can temporarily block the server/proxy history cache. This may delay writing history data to the database and slow down the system. To help manage the history cache, the following improvements have been introduced:

  * **Manual cache clearing:** The new history_cache_clear=target runtime command for Zabbix [server](/documentation/current/en/manual/concepts/server#runtime-control)/[proxy](/documentation/current/en/manual/concepts/proxy#runtime-control) allows you to manually clear the history cache for a specific item by its ID.
  * **Automatic cache clearing:** When you disable an item, it is immediately removed from the history cache (except for its last value, which is kept for logs). Similarly, when you disable a host, all its items are removed from the history cache (except for their last values).
  * **Cache diagnostics logging:** When the history cache is full, Zabbix server/proxy now logs history cache diagnostic information starting from [DebugLevel=3](/documentation/current/en/manual/appendix/config/zabbix_server#debuglevel) (previously DebugLevel=4). The log contains items with the most values in the history cache.

For long-term system stability, make sure that data collection is balanced with available resources (database performance, cache size, collection intervals, log item parameters, etc.). You can monitor Zabbix history cache using the [zabbix[wcache]](/documentation/current/en/manual/config/items/itemtypes/internal#wcache) internal item. You can also consider increasing the size of the history cache for Zabbix [server](/documentation/current/en/manual/appendix/config/zabbix_server#historycachesize)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#historycachesize).

#### History syncer transaction statistics

The history syncer process title now displays detailed statistics about history syncer transactions for Zabbix [server](/documentation/current/en/manual/concepts/server#history-syncer-transaction-statistics) and [proxy](/documentation/current/en/manual/concepts/proxy#history-syncer-transaction-statistics).

## Security

#### TLS encryption between frontend and server

It is now possible to [encrypt communication](/documentation/current/en/manual/appendix/install/frontend_encrypt) between Zabbix frontend and Zabbix server using TLS. This feature is controlled by new parameters in the [server configuration](/documentation/current/en/manual/appendix/config/zabbix_server) (TLSListen, TLSFrontendAccept, TLSFrontendCertIssuer, TLSFrontendCertSubject, FrontendAllowedIP).

#### Resolving secret vault macros by server/proxy independently

It is now possible to configure that vault secret macro values are retrieved by Zabbix server and Zabbix proxy independently if _Resolve secret vault macros by_ is [set to](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other) "Zabbix server and proxy".

## Plugins

#### Custom query path configuration for loadable plugins

The `Plugins.*.CustomQueriesPath` parameter in Zabbix agent 2 plugin configuration files for [MySQL](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mysql_plugin), [Oracle](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/oracle_plugin%5B), and [PostgreSQL](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/postgresql_plugin), as well as `Plugins.MSSQL.CustomQueriesDir` for [MSSQL](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/mssql_plugin), now has a default value. This functionality is disabled by default and can be enabled using the newly introduced `Plugins.*.CustomQueriesEnabled` parameter.

## Frontend

#### Inline validation in forms

Several frontend forms now support inline validation, showing any input errors immediately after you fill in the fields:

  * [Template](/documentation/current/en/manual/config/templates/template#creating-a-template) configuration
  * [Host](/documentation/current/en/manual/config/hosts/host#configuration) configuration
  * [Item](/documentation/current/en/manual/config/items/item#configuration) configuration
  * [Trigger](/documentation/current/en/manual/config/triggers/trigger#configuration) configuration

#### Default dashboard updated

The _Global view_ default [dashboard](/documentation/current/en/manual/web_interface/frontend_sections/dashboards) in new Zabbix installations has been updated to include the latest dashboard widgets.

![](/documentation/current/assets/en/manual/introduction/dashboard.png)

#### Enhanced color picker with palette support

The color picker in [graph](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/graph) and [pie chart](/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/pie_chart) widgets has been redesigned for improved usability. In addition to solid colors and hex input, you can now switch to a _Palette_ tab and pick from predefined color rows—each series gets its own distinct hue for clearer differentiation. The picker also offers full keyboard navigation and live validation.

![](/documentation/current/assets/en/manual/introduction/colors_solid_color.png) | In Zabbix 7.4 (_Solid color_ tab)  
---|---  
![](/documentation/current/assets/en/manual/introduction/colors_palette.png) | In Zabbix 7.4 (_Color palette_ tab)  
![](/documentation/current/assets/en/manual/introduction/colors_old.png) | Before Zabbix 7.4  
  
#### Modal forms

Several frontend forms are now opened in modal (pop-up) windows:

  * [Graph](/documentation/current/en/manual/config/visualization/graphs/custom#configuring-custom-graphs) configuration
  * [Graph prototype](/documentation/current/en/manual/discovery/low_level_discovery/graph_prototypes) configuration

#### Easier copying for preprocessing test results

It is now easier to copy values in preprocessing [test results](/documentation/current/en/manual/config/items/preprocessing/testing#testing-hypothetical-value) using the added _Copy to clipboard_ button.

![](/documentation/current/assets/en/manual/introduction/copy_pp_test_result.png)

Note that a similar button now replaces the _Copy_ link for created [API tokens](/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens).

## Documentation

#### Consolidated documentation pages for minor releases

Release documentation for minor versions of a major Zabbix release will now be collected in single documentation pages for [new features](/documentation/current/en/manual/introduction/whatsnew_minor) and [upgrade notes](/documentation/current/en/manual/installation/upgrade_notes_minor) respectively.