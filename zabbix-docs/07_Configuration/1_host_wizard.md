---
title: Host Wizard
source: https://www.zabbix.com/documentation/current/en/manual/config/hosts/host_wizard
downloaded: 2025-11-14 10:34:35
---

# 1 Host Wizard

#### Overview

The Host Wizard is a guided, step-by-step interface for setting up your monitoring target (device, application, service, etc.) in Zabbix. It walks you through the following steps:

  * Selecting a template
  * Creating or selecting a host
  * Installing Zabbix agent or agent 2
  * Adding a host interface
  * Applying additional configuration to your monitoring target or the Zabbix host (if required by the template)

To access the Host Wizard in Zabbix frontend, do the following:

  * Go to: _Data collection_ > [_Hosts_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/hosts)
  * Click on _Host Wizard_ in the upper-right corner of the screen
  * Follow the instructions in the wizard

You can also edit an existing host by clicking its name (or the three dots icon next to it) in various frontend sections to access the Host Wizard from the [host menu](/documentation/current/en/manual/web_interface/menu/host_menu). Note that some steps are skipped when editing an existing host if it already includes the configuration required by the selected template.

Alternatively, you can use the classic approach to [creating and configuring a host](/documentation/current/en/manual/config/hosts/host).

#### Welcome to the Host Wizard

When you start the Host Wizard, a welcome screen is displayed:

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_welcome.png)

To skip this screen in future sessions, you can mark the _Do not show welcome screen_ checkbox and click _Next_.

If you start configuring settings in the next Host Wizard steps and try to close the wizard by clicking the close icon or pressing ESC, a confirmation screen will appear:

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_cancel.png)

Clicking _Yes_ will exit the Host Wizard without saving your progress. Clicking _No_ , ESC, or the close icon will return to the last step.

#### Select a template

The first step of setting up your monitoring target is to select a [template](/documentation/current/en/manual/config/templates)—a set of predefined configurations (metrics to be collected, conditions for generating alerts, etc.) designed for your monitoring target.

Zabbix [out-of-the-box templates](/documentation/current/en/manual/config/templates_out_of_the_box) offer a variety of predefined monitoring configurations for operating systems, applications, databases, network devices, services, and more.

In this step, you can:

  * Browse templates by class (Cloud, Database, Network, etc.) and subclass (e.g., automation, backup), which are based on template [tags](/documentation/current/en/manual/config/tagging).
  * Search templates by keywords in template name or template tag names and values.
  * Filter templates by data collection method (agent-based or agentless; agent-based templates include at least one [Zabbix agent](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent) item).
  * Filter templates by agent mode (active or passive; active templates include at least one Zabbix agent (active) item, while passive templates include at least one passive item; for details, see [Passive and active agent checks](/documentation/current/en/manual/appendix/items/activepassive)).
  * When using the Host Wizard to configure an existing host, you can also filter templates already linked to the host.

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_template.png)

When selecting a template, you will see the following message: _Some templates (n) are incompatible with the Host Wizard. See how to update them. Custom templates are not supported._ This indicates that some out-of-the-box templates are not yet compatible with the Host Wizard and need to be upgraded; see [upgrade instructions](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade).

The template you select will determine the next steps in the Host Wizard. For example, if you select the _MySQL by Zabbix agent_ template, which uses Zabbix agent for data collection, the wizard will guide you through the agent installation process.

#### Create or select a host

A template must be linked to a [host](/documentation/current/en/manual/config/hosts/host)—an entity in Zabbix that represents your monitoring target. When linked, the host receives all template entities, such as items (metrics to be collected) and triggers (conditions for generating alerts), that are required for monitoring.

Each host must also belong to at least one [host group](/documentation/current/en/manual/config/hosts/host_groups), which is used for organizing hosts and assigning user permissions to them.

In this step, you can:

  * Create a new host and host group by entering names for both.
  * Create a new host by entering its name, and select an existing host group, to which the new host will be assigned.
  * Select an existing host; you can also assign this host to additional host groups without removing it from any current groups.

Selecting an existing host does not remove or overwrite its current configuration unless stated explicitly in later steps. [Discovered hosts](/documentation/current/en/manual/discovery/low_level_discovery/host_prototypes#discovered-hosts) cannot be selected.

For example, you could create a new host named _MySQL server_ to represent the locally installed MySQL server that you want to monitor. The previously selected _MySQL by Zabbix agent_ template will be linked to this host. Additionally, you could select the existing _Databases_ host group (or create a new one, e.g., _MySQL servers_) to organize the host with other database-related hosts and later simplify permission management.

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_create_host.png)

#### Install Zabbix agent

Agent-based templates (such as _MySQL by Zabbix agent_) require installing Zabbix [agent](/documentation/current/en/manual/concepts/agent) or [agent 2](/documentation/current/en/manual/concepts/agent2)—a process deployed on your monitoring target to actively monitor local resources and applications (if required by the template).

In this step:

  * Verify Zabbix server, proxy, or cluster address (e.g., 192.0.2.0:10051). This value will be used to configure the [Server](/documentation/current/en/manual/appendix/config/zabbix_agentd#server) and [ServerActive](/documentation/current/en/manual/appendix/config/zabbix_agentd#serveractive) parameter for Zabbix agent.
  * Enter a new, unique, and non-secret pre-shared key identity (e.g., _PSK 001_ or _mysql-agent-psk1_), and generate the pre-shared key. These values will be used to configure [pre-shared key (PSK)](/documentation/current/en/manual/encryption/using_pre_shared_keys) encryption for the Zabbix host (e.g., _MySQL server_) and Zabbix agent.

When editing an existing host, the PSK configuration will overwrite all existing [encryption settings](/documentation/current/en/manual/config/hosts/host#encryption) on the host.

  * Select the operating system of the machine that hosts your monitoring target.
  * Install Zabbix agent on that system by running the provided script on it or by following the installation instructions.

For example, you could set _Pre-shared key identity_ to _PSK 001_ and generate a new _Pre-shared key_. Then, you could select _Linux_ as the operating system and run the provided script on that system. After installing Zabbix agent, return to the Host Wizard.

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_agent.png)

#### Add host interface

The [host interface](/documentation/current/en/manual/config/hosts/host#configuration) defines how Zabbix server connects to your monitoring target over the network. It defines connection parameters such as IP address, DNS name, port, and interface type (Agent, SNMP, JMX, or IPMI), depending on the data collection method required by the selected template.

In this step, enter the host interface details required by the selected template.

For example, you could use the default agent address (127.0.0.1) and port (10050) if Zabbix server, Zabbix agent, and the MySQL server are all running locally on the same machine.

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_interface.png)

#### Configure host

Some templates require additional configuration before the host can be created. These may include:

  * Manual configuration of your monitoring target (e.g., enabling specific services, creating service users, or granting permissions):

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_configure_host.png)

  * Defining [host macros](/documentation/current/en/manual/config/hosts/host#configuration)—variables that control item behavior, connection settings, authentication credentials, and other parameters:

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_configure_host_macros.png)

After completing all required configuration steps, click _Create_ to add the host to Zabbix (or _Update_ to update the configuration of an existing host):

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_configure_host_create.png)

#### Configuration complete

At this point, Zabbix is already monitoring your target.

For new hosts, click _Finish_ to navigate to the [Latest data](/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data) section and view the most recent data for your host. For existing hosts, click _Finish_ to close the Host Wizard and return to the screen where it was opened.

![](/documentation/current/assets/en/manual/config/hosts/host_wizard_complete.png)