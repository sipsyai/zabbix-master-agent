---
title: Active agent autoregistration
source: https://www.zabbix.com/documentation/current/en/manual/discovery/auto_registration
downloaded: 2025-11-14 10:37:17
---

# 2 Active agent autoregistration

#### Overview

It is possible to allow active Zabbix agent autoregistration, after which the server can start monitoring them. This way new hosts can be added for monitoring without configuring them manually on the server.

Autoregistration can happen when a previously unknown active agent asks for checks.

The feature might be very handy for automatic monitoring of new Cloud nodes. As soon as you have a new node in the Cloud Zabbix will automatically start the collection of performance and availability data of the host.

Active agent autoregistration also supports the monitoring of added hosts with passive checks. When the active agent asks for checks, providing it has the 'ListenIP' or 'ListenPort' configuration parameters defined in the configuration file, these are sent along to the server. (If multiple IP addresses are specified, the first one is sent to the server.)

Server, when adding the new autoregistered host, uses the received IP address and port to configure the agent. If no IP address value is received, the one used for the incoming connection is used. If no port value is received, 10050 is used.

It is possible to specify that the host should be autoregistered with a DNS name as the default agent interface.

Autoregistration is rerun:

  * if host metadata information changes: 
    * due to HostMetadata changed and agent restarted
    * due to value returned by HostMetadataItem changed
  * for manually created hosts with metadata missing
  * if a host is manually changed to be monitored by another Zabbix proxy
  * if autoregistration for the same host comes from a new Zabbix proxy

The active agent autoregistration heartbeat for Zabbix server and Zabbix proxy is 120 seconds. So in case a discovered host is deleted, the autoregistration will be rerun in 120 seconds.

#### Configuration

##### Specify server

Make sure you have the Zabbix server identified in the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd) \- zabbix_agentd.conf
    
    
    ServerActive=10.0.0.1

Copy

✔ Copied

Unless you specifically define a _Hostname_ in zabbix_agentd.conf, the system hostname of agent location will be used by server for naming the host. The system hostname in Linux can be obtained by running the 'hostname' command.

If _Hostname_ is defined in Zabbix agent configuration as a comma-delimited list of hosts, hosts will be created for all listed hostnames.

Restart the agent after making any changes to the configuration file.

##### Action for active agent autoregistration

When server receives an autoregistration request from an agent it calls an [action](/documentation/current/en/manual/config/notifications/action). An action of event source "Autoregistration" must be configured for agent autoregistration.

Setting up [network discovery](network_discovery) is not required to have active agents autoregister.

In the Zabbix frontend, go to _Alerts → Actions_ , select _Autoregistration actions_ and click on _Create action_ :

  * In the Action tab, give your action a name
  * Optionally specify [conditions](/documentation/current/en/manual/config/notifications/action/conditions#autoregistration-actions). You can do a substring match or regular expression match in the conditions for host name/host metadata. If you are going to use the "Host metadata" condition, see the next section.
  * In the Operations tab, add relevant operations, such as - 'Add host', 'Add to host group' (for example, _Discovered hosts_), 'Link templates', etc.

If the hosts that will be autoregistering are likely to be supported for active monitoring only (such as hosts that are firewalled from your Zabbix server) then you might want to create a specific template like _Template_Linux-active_ to link to.

Created hosts are added to the _Discovered hosts_ group (by default, configurable in _Administration_ → _General_ → _[Other](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#other-parameters)_). If you wish hosts to be added to another group, add a _Remove from host group_ operation (specifying "Discovered hosts") and also add an _Add to host group_ operation (specifying another host group), because a host must belong to a host group.

#### Secure autoregistration

A secure way of autoregistration is possible by configuring PSK-based authentication with encrypted connections.

The level of encryption is configured globally in _Administration_ → _General_ → _[Autoregistration](/documentation/current/en/manual/web_interface/frontend_sections/administration/general#autoregistration)_. It is possible to select no encryption, TLS encryption with PSK authentication or both (so that some hosts may register without encryption while others through encryption).

Authentication by PSK is verified by Zabbix server before adding a host. If successful, the host is added and _[Connections from/to host](/documentation/current/en/manual/config/hosts/host#encryption)_ are set to 'PSK' only with identity/pre-shared key the same as in the global autoregistration setting.

To ensure security of autoregistration on installations using proxies, encryption between Zabbix server and proxy should be enabled.

#### Using DNS as default interface

HostInterface and HostInterfaceItem [configuration parameters](/documentation/current/en/manual/appendix/config/zabbix_agentd) allow to specify a custom value for the host interface during autoregistration.

More specifically, they are useful if the host should be autoregistered with a DNS name as the default agent interface rather than its IP address. In that case the DNS name should be specified or returned as the value of either HostInterface or HostInterfaceItem parameters. If the value of one of these parameters changes—for example, from an IP address to a DNS name or vice versa—the default interface of the autoregistered host will be updated accordingly. This update is applied to the existing host, not by creating a new one. To send the new value, the agent must be restarted so that it re-initiates the autoregistration process.

If HostInterface or HostInterfaceItem parameters are not configured, the listen_dns parameter is used instead. This value is determined by performing a reverse DNS lookup of the agent's IP address. If reverse DNS is not properly configured or returns an invalid name, it may result in incorrect or failed autoregistration due to an invalid interface value.

#### Using host metadata

When agent is sending an autoregistration request to the server it sends its hostname. In some cases (for example, Amazon cloud nodes) a hostname is not enough for Zabbix server to differentiate discovered hosts. Host metadata can be optionally used to send other information from an agent to the server.

Host metadata is configured in the agent [configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd) \- zabbix_agentd.conf. There are 2 ways of specifying host metadata in the configuration file:
    
    
    HostMetadata
           HostMetadataItem

Copy

✔ Copied

See the description of the options in the link above.

The HostMetadataItem parameter may return up to 65535 UTF-8 code points. A longer value will be truncated.

Note that on MySQL, the effective maximum length in characters will be less if the returned value contains multibyte characters. For example, a value containing 3-byte characters only will be limited to 21844 characters in total, while a value containing 4-byte characters only will be limited to 16383 symbols.

An autoregistration attempt happens every time an active agent sends a request to refresh active checks to the server. The delay between requests is specified in the [RefreshActiveChecks](/documentation/current/en/manual/appendix/config/zabbix_agentd) parameter of the agent. The first request is sent immediately after the agent is restarted.

##### Example 1

Using host metadata to distinguish between Linux and Windows hosts.

Say you would like the hosts to be autoregistered by the Zabbix server. You have active Zabbix agents (see "Configuration" section above) on your network. There are Windows hosts and Linux hosts on your network and you have "Linux by Zabbix agent" and "Windows by Zabbix agent" templates available in your Zabbix frontend. So at host registration, you would like the appropriate Linux/Windows template to be applied to the host being registered. By default, only the hostname is sent to the server at autoregistration, which might not be enough. In order to make sure the proper template is applied to the host you should use host metadata.

**Frontend configuration**

The first thing to do is to configure the frontend. Create 2 actions. The first action:

  * Name: Linux host autoregistration
  * Conditions: Host metadata contains _Linux_
  * Operations: Link templates: Linux

You can skip an "Add host" operation in this case. Linking a template to a host requires adding the host first so the server will do that automatically.

The second action:

  * Name: Windows host autoregistration
  * Conditions: Host metadata contains _Windows_
  * Operations: Link templates: Windows

**Agent configuration**

Now you need to configure the agents. Add the next line to the agent configuration files:
    
    
    HostMetadataItem=system.uname

Copy

✔ Copied

This way you make sure host metadata will contain "Linux" or "Windows" depending on the host an agent is running on. An example of host metadata in this case:
    
    
    Linux: Linux server3 3.2.0-4-686-pae #1 SMP Debian 3.2.41-2 i686 GNU/Linux
           Windows: Windows WIN-0PXGGSTYNHO 6.0.6001 Windows Server 2008 Service Pack 1 Intel IA-32

Copy

✔ Copied

Do not forget to restart the agent after making any changes to the configuration file.

##### Example 2

**_Step 1_**

Using host metadata to allow some basic protection against unwanted hosts registering.

**Frontend configuration**

Create an action in the frontend, using some hard-to-guess secret code to disallow unwanted hosts:

  * Name: Autoregistration action Linux
  * Conditions: 
    * Type of calculation: AND
    * Condition (A): Host metadata contains //Linux//
    * Condition (B): Host metadata contains //21df83bf21bf0be663090bb8d4128558ab9b95fba66a6dbf834f8b91ae5e08ae//
  * Operations: 
    * Send message to users: Admin via all media
    * Add to host groups: Linux servers
    * Link templates: Linux

Please note that this method alone does not provide strong protection because data is transmitted in plain text. Configuration cache reload is required for changes to have an immediate effect.

**Agent configuration**

Add the next line to the agent configuration file:
    
    
    HostMetadata=Linux    21df83bf21bf0be663090bb8d4128558ab9b95fba66a6dbf834f8b91ae5e08ae

Copy

✔ Copied

where "Linux" is a platform, and the rest of the string is the hard-to-guess secret text.

Do not forget to restart the agent after making any changes to the configuration file.

**_Step 2_**

It is possible to add additional monitoring for an already registered host.

**Frontend configuration**

Update the action in the frontend:

  * Name: Autoregistration action Linux
  * Conditions: 
    * Type of calculation: AND
    * Condition (A): Host metadata contains Linux
    * Condition (B): Host metadata contains 21df83bf21bf0be663090bb8d4128558ab9b95fba66a6dbf834f8b91ae5e08ae
  * Operations: 
    * Send message to users: Admin via all media
    * Add to host groups: Linux servers
    * Link templates: Linux
    * Link templates: MySQL by Zabbix Agent

**Agent configuration**

Update the next line in the agent configuration file:
    
    
    HostMetadata=MySQL on Linux 21df83bf21bf0be663090bb8d4128558ab9b95fba66a6dbf834f8b91ae5e08ae

Copy

✔ Copied

Do not forget to restart the agent after making any changes to the configuration file.