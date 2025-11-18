---
title: Zabbix overview
source: https://www.zabbix.com/documentation/current/en/manual/introduction/overview
downloaded: 2025-11-14 10:33:43
---

# 4 Zabbix overview

#### Architecture

Zabbix consists of several major software components. Their responsibilities are outlined below.

##### Server

[Zabbix server](/documentation/current/en/manual/concepts/server) is the central component to which agents report availability and integrity information and statistics. The server is the central repository in which all configuration, statistical and operational data are stored.

##### Database storage

All configuration information as well as the data gathered by Zabbix is stored in a database.

##### Web interface

For an easy access to Zabbix from anywhere and from any platform, the web-based interface is provided. The interface is part of Zabbix server, and usually (but not necessarily) runs on the same physical machine as the one running the server.

##### Proxy

[Zabbix proxy](/documentation/current/en/manual/concepts/proxy) can collect performance and availability data on behalf of Zabbix server. A proxy is an optional part of Zabbix deployment; however, it may be very beneficial to distribute the load of a single Zabbix server.

##### Agent

Zabbix agents are deployed on monitoring targets to actively monitor local resources and applications and report the gathered data to Zabbix server. Since Zabbix 4.4, there are two types of agents available: the [Zabbix agent](/documentation/current/en/manual/concepts/agent) (lightweight, supported on many platforms, written in C) and the [Zabbix agent 2](/documentation/current/en/manual/concepts/agent2) (extra-flexible, easily extendable with plugins, written in Go).

#### Data flow

In addition it is important to take a step back and have a look at the overall data flow within Zabbix. In order to create an item that gathers data you must first create a host. Moving to the other end of the Zabbix spectrum you must first have an item to create a trigger. You must have a trigger to create an action. Thus if you want to receive an alert that your CPU load is too high on _Server X_ you must first create a host entry for _Server X_ followed by an item for monitoring its CPU, then a trigger which activates if the CPU is too high, followed by an action which sends you an email. While that may seem like a lot of steps, with the use of templating it really isn't. However, due to this design it is possible to create a very flexible setup.