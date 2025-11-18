---
title: Nesting
source: https://www.zabbix.com/documentation/current/en/manual/config/templates/nesting
downloaded: 2025-11-14 10:36:01
---

# 4 Nesting

#### Overview

Nesting is a way of one template encompassing one or more other templates.

As it makes sense to separate out entities on individual templates for various services, applications, etc., you may end up with quite a few templates all of which may need to be linked to quite a few hosts. To simplify the picture, it is possible to link some templates together in a single template.

The benefit of nesting is that you have to link only one template to the host, and the host will automatically inherit all entities from the templates that are linked to the one template. For example, if we link _T1_ and _T2_ to _T3_ , we supplement _T3_ with all entities from _T1_ and _T2_ , but not vice versa. If we link _T1_ to _T2_ and _T3_ , we supplement _T2_ and _T3_ with entities from _T1_.

#### Configuring nested templates

To link templates, you need to take an existing template (or create a new one), and then:

  1. Open the [template configuration form](/documentation/current/en/manual/config/templates/template#creating-a-template).
  2. Find the _Templates_ field.
  3. Click on _Select_ to open the _Templates_ pop-up window.
  4. In the pop-up window, choose the required templates, and then click on _Select_ to add the templates to the list.
  5. Click on _Add_ or _Update_ in the template configuration form.

Thus, all entities of the configured template, as well as all entities of linked templates will now appear in the template configuration. This includes items, triggers, graphs, low-level discovery rules, and web scenarios, but excludes dashboards. However, linked template dashboards will, nevertheless, be inherited by hosts.

To unlink any of the linked templates, click on _Unlink_ or _Unlink and clear_ in the template configuration form, and then click on _Update_.

The _Unlink_ option will simply remove the association with the linked template, while not removing any of its entities (items, triggers, etc.).

The _Unlink and clear_ option will remove both the association with the linked template, as well as all its entities (items, triggers, etc.).