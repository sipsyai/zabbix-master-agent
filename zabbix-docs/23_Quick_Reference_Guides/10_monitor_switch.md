---
title: Monitor a network switch or router with Zabbix
source: https://www.zabbix.com/documentation/current/en/manual/guides/monitor_switch
downloaded: 2025-11-14 10:48:12
---

# 10 Monitor a network switch or router with Zabbix

## Introduction

This guide walks you through the steps required to start basic monitoring of your network switch or router using Zabbix. A Cisco router is used as an example, but the procedure applies to any SNMP-enabled network device.

**Who this guide is for**

This guide is designed for new Zabbix users and network administrators who want to quickly enable basic monitoring for network devices. If you require deep customization or advanced configuration options, please refer to the [SNMP agent](/documentation/current/en/manual/config/items/itemtypes/snmp) page or the [Configuration](/documentation/current/en/manual/config) section of Zabbix manual.

**Prerequisites**

Before proceeding with this guide, ensure that you have:

  * Zabbix server and Zabbix frontend installed: install according to the instructions for your operating system (see [Installation from packages](/documentation/current/en/manual/installation/install_from_packages) and [Web interface installation](/documentation/current/en/manual/installation/frontend)).
  * SNMP-enabled device: a network switch or router (for example, a Cisco router) with SNMP enabled.
  * [MIB files](/documentation/current/en/manual/config/items/itemtypes/snmp/mibs) installed: Installing MIB files enables Zabbix to translate numeric OIDs into human‐readable names and descriptions. Without proper MIB support, you may see only numeric values, making it harder to configure items and troubleshoot issues.

To install MIB files on Ubuntu:

1\. Install the MIB downloader package:
    
    
    sudo apt-get update
           sudo apt-get install snmp-mibs-downloader

Copy

✔ Copied

If you need to add vendor-specific MIBs (e.g., from Cisco, Juniper), place them in the appropriate MIB directory:

  * For Linux-based systems common locations include /usr/share/snmp/mibs/ or /usr/local/share/snmp/mibs/.
  * For Zabbix installations MIB files can be stored in /var/lib/zabbix/mibs/.

Ensure the MIBDIRS environment variable or the snmp.conf file includes the correct path.

To verify that your system recognizes the new MIBs, use:
    
    
    snmptranslate -IR -On <MIB-NAME>::<object>

Copy

✔ Copied

For detailed instructions, refer to your SNMP library documentation:

  * [Cisco MIBs](https://github.com/cisco/cisco-mibs)
  * [Juniper MIBs](https://apps.juniper.net/mib-explorer/)

2\. Edit `/etc/snmp/snmp.conf` and comment out the line that starts with `mibs :` to allow the system to load all available MIBs.

3\. Verify by running an `snmpwalk` (for example, `snmpwalk -v 2c -c <your_community_string> <device_IP>`) and check that OIDs are displayed with descriptive names.

This guide is based on the following setup:

  * Zabbix version: 7.2 (installed from packages)
  * OS distribution: Ubuntu
  * OS version: 24.04.2+
  * Zabbix components: server, frontend, and optionally agent (if monitoring local network metrics)
  * Database: MySQL
  * Web server: Apache
  * Network device: Cisco Catalyst 3750V2-24FS

It is assumed that your network device is already physically installed and connected.

## Configure the network device (Cisco router example)

For monitoring via SNMP, you must configure your network device to allow SNMP queries. The example below is for SNMPv2 and does not take into account existing settings. Caution: applying these commands may override current SNMP configurations.

For a Cisco router, the configuration typically involves steps written below.

### SNMPv2 Example

1\. Enable SNMP and set community string.

[Log in](https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb4982-access-an-smb-switch-cli-using-ssh-or-telnet.html) to your Cisco router's console and enter configuration mode:
    
    
    configure terminal

Copy

✔ Copied

Then, [enable SNMP](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/7282-12.html) by specifying a read-only community string. For example:
    
    
    snmp-server community <your_community_string> RO

Copy

✔ Copied

Replace `<your_community_string>` with your secure community string. Note: the RO (Read-Only) option allows SNMP to retrieve data from the device but prevents any configuration changes.

It is recommended to restrict SNMP access to only the necessary devices for security reasons. For further guidance on configuring access control lists (ACLs), refer to [Cisco's official documentation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus3000/sw/security/503_u2_2/Cisco_n3k_security_cg_503_u2_2_chapter7.html?dtid=osscdc000283).

2\. Save the configuration.

Save your changes to ensure SNMP settings persist after a reboot:
    
    
    write memory

Copy

✔ Copied

### SNMPv3 Example

SNMPv3 provides enhanced security with authentication and encryption. Its configuration is more secure than SNMPv2 and should be verified against your device-specific documentation.

1\. Create an SNMP group.

Configure an SNMPv3 group with privacy (encryption) enabled:
    
    
    configure terminal
           snmp-server group <your_group> v3 priv

Copy

✔ Copied

2\. Create an SNMP user.

Add an SNMPv3 user with authentication and privacy. Replace the placeholders with your desired values:
    
    
    snmp-server user <your_user> <your_group> v3 auth md5 <auth_password> priv aes 128 <priv_password>

Copy

✔ Copied

3\. Save the configuration:
    
    
    write memory

Copy

✔ Copied

For further details or model-specific instructions, you may refer to external [Cisco SNMP configuration tutorials](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-16/snmp-xe-16-book/nm-snmp-cfg-snmp-support.html). This guide, however, provides the basic steps for enabling SNMP monitoring.

## Configure Zabbix frontend

### Create a host in Zabbix frontend

1\. Log into Zabbix frontend.

2\. Add a new host.

Navigate to _Data collection > Hosts_ and click on _Create host_.

  * _Host name_ : enter a name for your device (e.g., "Cisco Router").
  * Host groups: select an existing group or create a new group such as "Network Devices".
  * Interfaces: 
    * Click _Add_ under Interfaces.
    * Choose _SNMP_ as the interface type.
    * Enter the IP address or DNS name of your Cisco router.
    * Set the default SNMP port (usually 161).
    * Use the drop-down menu to select the appropriate SNMP version (e.g. SNMPv2).
    * For SNMPv1/v2, enter the community string in the _SNMP community_ field. For SNMPv3, additional credentials (_Context name_ , _Security name_ , and _Security level_ , etc.) will be prompted.

3\. Link Templates

In the _Templates_ field, select the SNMP template that best matches your device. Zabbix provides a range of pre-built [SNMP templates](/documentation/current/en/manual/config/templates_out_of_the_box/network_devices#devices) for many device families. For example, if you are monitoring a Cisco device, choose the template that corresponds to your device's OS or model (such as Cisco IOS SNMP or Cisco Catalyst 3750<device model> SNMP).

4\. Click on _Add_ to save the host.

![](/documentation/current/assets/en/manual/guides/switch_host.png)

![](/documentation/current/assets/en/manual/guides/switch_host1.png)

## View collected metrics

Congratulations! Zabbix is now set up to monitor your network device.

Latest Data:

  * Navigate to Monitoring > Latest data in the Zabbix frontend.

![](/documentation/current/assets/en/manual/guides/switch_hosts.png)

  * Select your “Cisco Router” host (or discovered hosts) to view metrics such as hardware and network uptime, ICMP loss, ping, and response time, etc.

![](/documentation/current/assets/en/manual/guides/switch_data.png)

  * Graphs and screens:

To visualize the performance data, click on _Graphs_ next to the SNMP items to see detailed metrics.

As a next step, you can:

  * Add custom SNMP items to monitor additional metrics.
  * Set up problem alerts to receive notifications about potential issues.

### Create SNMP items

Once the host is set up, you can create items to monitor specific metrics. Note: this step is optional if you're using a template, as templates already contain default sets of items.

1\. Identify the SNMP OID:

Use the `snmpwalk` command to list available OIDs on your device. For example:
    
    
    snmpwalk -v 2c -c <your_community_string> <device_IP> .

Copy

✔ Copied

Find the OID for the metric you wish to monitor (for instance, IF-MIB::ifHCInOctets.3 for incoming traffic on port 3). To get the numeric OID, you can use:
    
    
    snmpget -v 2c -c <your_community_string> -On <device_IP> IF-MIB::ifHCInOctets.3

Copy

✔ Copied

2\. Create an SNMP item:

  * Navigate to _Data collection > Hosts_ and click on the _Items_ tab for your SNMP host and click _Create item_.
  * _Name_ : enter a descriptive name (e.g., “Port 3 Incoming Traffic”).
  * _Type_ : select _SNMP agent_.
  * _Key_ : provide a meaningful key (e.g., `cisco.ifHCInOctets.3`).
  * _Host interface_ : ensure the SNMP interface is selected.
  * _SNMP OID_ : enter the OID using one of the supported formats, for example: 
    * `get[1.3.6.1.2.1.31.1.1.1.6.3]` for a single value;
    * `walk[1.3.6.1.2.1.31.1.1.1.6.3]` to retrieve a subtree of values asynchronously.

![](/documentation/current/assets/en/manual/guides/switch_item.png)

  * _Preprocessing_ (if needed): if the item returns a cumulative counter (such as interface traffic), navigate to the _Preprocessing_ tab, and add a preprocessing step like “Change per second” to calculate the rate.

![](/documentation/current/assets/en/manual/guides/switch_preprocessing.png)

To retrieve multiple values in one SNMP transaction, you can specify several OIDs using the syntax `walk[OID1,OID2,...]`.

### Translating OIDs between Numeric and MIB Names

When working with SNMP, you might need to convert between numeric OIDs and their corresponding MIB names. This translation helps in identifying and troubleshooting metrics more easily.

  * Translating a MIB name to a numeric OID: use the `snmptranslate` command with the `-On` option. For example, to translate the MIB name `IF-MIB::ifHCInOctets.3` to its numeric OID, run:

    
    
    snmptranslate -On IF-MIB::ifHCInOctets.3

Copy

✔ Copied

This command might output:
    
    
    .1.3.6.1.2.1.31.1.1.1.6.3

Copy

✔ Copied

  * Translating a numeric OID to its MIB name: use the `snmptranslate` command with the `-IR` (or `-m ALL`) option to reverse the translation. For example, to translate the numeric OID `.1.3.6.1.2.1.31.1.1.1.6.3` back to its MIB name, run:

    
    
    snmptranslate -IR -On .1.3.6.1.2.1.31.1.1.1.6.3

Copy

✔ Copied

This command might output:
    
    
    IF-MIB::ifHCInOctets.3

Copy

✔ Copied

## Set up problem alerts

This guide provides basic configuration steps for sending email alerts.

1\. Navigate to [_User settings > Profile_](/documentation/current/en/manual/web_interface/user_profile), switch to the _Media_ tab and [add your email](/documentation/current/en/manual/quickstart/login#adding-user).

![](/documentation/current/assets/en/manual/quickstart/new_media.png)

2\. Follow the guide for [Receiving a problem notification](/documentation/current/en/manual/quickstart/notification).

Next time, when Zabbix detects a problem, you should receive an alert via email.

## Test your configuration

To ensure that Zabbix correctly detects network performance issues, simulate a real problem by increasing the ICMP ping response time threshold.

1\. Open your "Cisco Router" host configuration in Zabbix.

2\. Navigate to the _Macros_ tab and select _Inherited and host macros_.

3\. Locate the `{$ICMP_RESPONSE_TIME_WARN}` macro (or a similar response time threshold macro).

4\. Set a very low value (e.g., 0.001) to trigger an alert when the ping response exceeds this value.

5\. Click _Update_ to apply the changes.

6\. Wait a few moments for Zabbix to detect the simulated issue.

7\. Navigate to _Monitoring > Problems_ to verify that an alert appears (e.g., "High ICMP ping response time").

![](/documentation/current/assets/en/manual/guides/switch_problem.png)

If alerts are configured, you should also receive a problem alert.

8\. Revert the macro value to its original setting and click _Update_ to save the changes.

9\. Confirm that the problem is resolved and disappears from the _Problems_ section.

## Troubleshooting SNMP Monitoring

If you notice that the SNMP icon in the Zabbix frontend appears RED or no data is collected, try the following steps:

1\. Check SNMP connectivity.

For SNMPv2 run the following command from your Zabbix server:
    
    
    snmpwalk -v 2c -c <community_string> <device_IP> .

Copy

✔ Copied

This command verifies that the device responds to SNMP queries.

For SNMPv3, include the appropriate SNMPv3 credentials:
    
    
    snmpwalk -v3 -u <your_user> -l authPriv -a MD5 -A <auth_password> -x AES -X <priv_password> <device_IP> .

Copy

✔ Copied

This verifies that SNMPv3 credentials are correct and the device is responding securely.

2\. Ensure that MIB files are installed and enabled as described in the prerequisites. To ensure that, following command must not give error when you query a network device:
    
    
    snmpwalk -v 2c -c <your_community_string> <device_IP> ifInOctets

Copy

✔ Copied

This should return translated OIDs without errors.

3\. Confirm that the SNMP version and credentials configured in Zabbix match those set on your device. For instance, review the SNMP settings in the Zabbix host configuration and verify them against your device’s configuration. On a Cisco device, you might check the SNMP settings by running:
    
    
    show running-config | include snmp

Copy

✔ Copied

This ensures that the community string (for SNMPv2) or SNMPv3 user details are correct.

4\. Verify that SNMP is correctly enabled on your network device. On a Cisco router, log in to the console and run:
    
    
    show running-config | include snmp

Copy

✔ Copied

This command displays the active SNMP configuration and helps confirm that SNMP is properly configured.

5\. Ensure that no firewalls or network issues are blocking SNMP traffic (typically on port 161) between the Zabbix server and the device. You can test connectivity using:

nc -zv <device_IP> 161

`nc -zv` checks if port 161 is open and listening on the device.

Additionally, if you are using UFW on Ubuntu, check the firewall status:
    
    
    sudo ufw status

Copy

✔ Copied

Or, for iptables:
    
    
    sudo iptables -L -n

Copy

✔ Copied

6\. Review the Zabbix server log files for any SNMP-related errors to help pinpoint the issue:
    
    
    tail -f /tmp/zabbix_server.log

Copy

✔ Copied

`tail -f` allows you to monitor log updates in real time.

**See also:**

  * [Creating an item](/documentation/current/en/manual/config/items/item) \- learn how to add additional metrics.
  * [SNMP agent](/documentation/current/en/manual/config/items/itemtypes/snmp) \- additional information on SNMP monitoring with Zabbix.
  * [Standardized templates for network devices](/documentation/current/en/manual/config/templates_out_of_the_box/network_devices) \- information on available SNMP templates.
  * [Discovery of SNMP OIDs](/documentation/current/en/manual/discovery/low_level_discovery/examples/snmp_oids_walk) \- additional information on SNMP discovery on a switch.
  * [Configuring a network discovery rule](/documentation/current/en/manual/discovery/network_discovery/rule) \- additional information on how to configure a network discovery rule used by Zabbix to discover hosts and services.