---
title: Global search
source: https://www.zabbix.com/documentation/current/en/manual/web_interface/global_search
downloaded: 2025-11-14 10:39:36
---

# 4 Global search

It is possible to search Zabbix frontend for hosts, host groups, templates and template groups.

The search input box is located below the Zabbix logo in the menu. The search can be started by pressing _Enter_ or clicking on the ![](/documentation/current/assets/en/manual/web_interface/search_icon.png) search icon.

![](/documentation/current/assets/en/manual/web_interface/global_search_dropdown.png)

If there is a host that contains the entered string in any part of the name, a dropdown will appear, listing all such hosts (with the matching part highlighted in orange). The dropdown will also list a host if that host's visible name is a match to the technical name entered as a search string; the matching host will be listed, but without any highlighting.

#### Searchable attributes

Hosts can be searched by the following properties:

  * Host name
  * Visible name
  * IP address
  * DNS name

Templates can be searched by name or visible name. If you search by a name that is different from the visible name (of a template/host), in the search results it is displayed below the visible name in parentheses.

Host and template groups can be searched by name. Specifying a parent group implicitly selects all nested groups.

#### Search results

Search results consist of four separate blocks for hosts, host groups, templates and template groups.

![](/documentation/current/assets/en/manual/web_interface/global_search_results.png)

It is possible to collapse/expand each individual block. The entry count is displayed at the bottom of each block, for example, _Displaying 13 of 13 found_. If there are no entries, the entry count is not displayed. Total entries displayed within one block are limited to 100.

Each entry provides links to monitoring and configuration data. See the [full list](/documentation/current/en/manual/web_interface/global_search#links-available) of links.

For all configuration data (such as items, triggers, graphs) the amount of entities found is displayed by a number next to the entity name, in gray. **Note** that if there are zero entities, no number is displayed.

Enabled hosts are displayed in blue, disabled hosts in red.

#### Links available

For each entry the following links are available:

  * Hosts 
    * Monitoring 
      * Latest data
      * Problems
      * Graphs
      * Host dashboards
      * Web scenarios
    * Configuration 
      * Items
      * Triggers
      * Graphs
      * Discovery rules
      * Web scenarios
  * Host groups 
    * Monitoring 
      * Latest data
      * Problems
      * Web scenarios
    * Configuration 
      * Hosts
  * Templates 
    * Configuration 
      * Items
      * Triggers
      * Graphs
      * Template dashboards
      * Discovery rules
      * Web scenarios
  * Template groups 
    * Configuration 
      * Templates