---
title: Templates and template groups
source: https://www.zabbix.com/documentation/current/en/manual/config/templates
downloaded: 2025-11-14 10:35:57
---

# 8 Templates and template groups

#### Overview

The use of templates is an excellent way of reducing one's workload and streamlining the Zabbix configuration. A template is a set of entities that can be conveniently applied to multiple hosts.

The entities may be:

  * items
  * triggers
  * graphs
  * dashboards
  * low-level discovery rules
  * web scenarios

As many hosts in real life are identical or fairly similar so it naturally follows that the set of entities (items, triggers, graphs,...) you have created for one host, may be useful for many. Of course, you could copy them to each new host, but that would be a lot of manual work. Instead, with templates you can copy them to one template and then apply the template to as many hosts as needed.

When a template is linked to a host, all entities (items, triggers, graphs,...) of the template are added to the host. Templates are assigned to each individual host directly (and not to a host group).

Templates are often used to group entities for particular services or applications (like Apache, MySQL, PostgreSQL, Postfix...) and then applied to hosts running those services.

Another benefit of using templates is when something has to be changed for all the hosts. Changing something on the template level once will propagate the change to all the linked hosts.

Templates are organized in [template groups](/documentation/current/en/manual/config/templates/template_groups).

Proceed to [creating and configuring a template](/documentation/current/en/manual/config/templates/template).