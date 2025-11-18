---
title: New template
source: https://www.zabbix.com/documentation/current/en/manual/quickstart/template
downloaded: 2025-11-14 10:34:31
---

# 6 New template

#### Overview

In this section you will learn how to set up a template.

Previously we learned how to set up an item, a trigger and how to get a problem notification for the host.

While all of these steps offer a great deal of flexibility in themselves, it may appear like a lot of steps to take if needed for, say, a thousand hosts. Some automation would be handy.

This is where templates come to help. Templates allow to group useful items, triggers and other entities so that those can be reused again and again by applying to hosts in a single step.

When a template is linked to a host, the host inherits all entities of the template. So, basically a pre-prepared bunch of checks can be applied very quickly.

#### Adding template

To start working with templates, we must first create one. To do that, in _Data collection_ > _Templates_ click on _Create template_. This will bring up a template configuration form.

![](/documentation/current/assets/en/manual/quickstart/new_template.png)

All mandatory input fields are marked with a red asterisk.

The required parameters to enter here are:

**_Template name_**

  * Enter a template name. Alpha-numericals, spaces and underscores are allowed.

**_Template groups_**

  * Select one or several groups by clicking _Select_ button. The template must belong to a group.

Access permissions to template groups are assigned in the [user group](/documentation/current/en/manual/quickstart/login#adding-permissions) configuration on the **Template permissions** tab in the same way as host permissions. All access permissions are assigned to groups, not individual templates, that's why including the template into at least one group is mandatory.

When done, click _Add_. Your new template should be visible in the list of templates. You can also use the [filter](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates#using-filter) to find your template.

![](/documentation/current/assets/en/manual/quickstart/template_list.png)

As you may see, the template is there, but it holds nothing in it - no items, triggers or other entities.

#### Adding item to template

To add an item to the template, open the item list for 'New host' by navigating to _Data collection → Hosts_ and clicking _Items_ next to 'New host'.

Then:

  * Mark the checkbox of the 'CPU Load' item in the list.
  * Click on _Copy_ below the list.
  * Select the _Templates_ tab.
  * Select the template to copy the item to.

![](/documentation/current/assets/en/manual/quickstart/copy_to_template.png)

All mandatory input fields are marked with a red asterisk.

  * Click on _Copy_.

If you now go to _Data collection_ > _Templates_ , 'New template' should have one new item in it.

We will stop at one item only for now, but similarly you can add any other items, triggers or other entities to the template until it's a fairly complete set of entities for given purpose (monitoring OS, monitoring single application).

#### Linking template to host

With a template ready, it only remains to add it to a host. For that, go to _Data collection > Hosts_, click on 'New host' to open its configuration form and find the **Templates** field.

Start typing _New template_ in the _Templates_ field. The name of template we have created should appear in the dropdown list. Scroll down to select. See that it appears in the _Templates_ field.

![](/documentation/current/assets/en/manual/quickstart/link_template.png)

Click _Update_ in the form to save the changes. The template is now added to the host, with all entities that it holds.

This way it can be applied to any other host as well. Any changes to the items, triggers and other entities at the template level will propagate to the hosts the template is linked to.

##### Linking pre-defined templates to hosts

As you may have noticed, Zabbix comes with a set of predefined templates for various OS, devices and applications. To get started with monitoring very quickly, you may link the appropriate one of them to a host, but beware that these templates need to be fine-tuned for your environment. Some checks may not be needed, and polling intervals may be way too frequent.

More information about [templates](/documentation/current/en/manual/config/templates) is available.