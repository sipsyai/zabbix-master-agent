---
title: Other event sources
source: https://www.zabbix.com/documentation/current/en/manual/config/events/sources
downloaded: 2025-11-14 10:35:41
---

# 2 Other event sources

#### Service events

Service events are generated only if service actions for these events are enabled. In this case, each service status change creates a new event:

  * Problem event - when service status is changed from OK to PROBLEM
  * OK event - when service status is changed from PROBLEM to OK

The event contains details of the service state change - when it happened and what the new state is.

#### Discovery events

Zabbix periodically scans the IP ranges defined in network discovery rules. Frequency of the check is configurable for each rule individually. Once a host or a service is discovered, a discovery event (or several events) are generated.

Zabbix generates the following events:

Service Up | Every time Zabbix detects active service.  
---|---  
Service Down | Every time Zabbix cannot detect service.  
Host Up | If at least one of the services is UP for the IP.  
Host Down | If all services are not responding.  
Service Discovered | If the service is back after downtime or discovered for the first time.  
Service Lost | If the service is lost after being up.  
Host Discovered | If host is back after downtime or discovered for the first time.  
Host Lost | If host is lost after being up.  
  
#### Active agent autoregistration events

Active agent autoregistration creates events in Zabbix.

If configured, active agent autoregistration event is created when a previously unknown active agent asks for checks or if the host metadata has changed. The server adds a new auto-registered host, using the received IP address and port of the agent.

For more information, see the [active agent autoregistration](/documentation/current/en/manual/discovery/auto_registration) page.

#### Internal events

Internal events happen when:

  * an item changes state from 'normal' to 'unsupported'
  * an item changes state from 'unsupported' to 'normal'
  * a low-level discovery rule changes state from 'normal' to 'unsupported'
  * a low-level discovery rule changes state from 'unsupported' to 'normal'
  * a trigger changes state from 'normal' to 'unknown'
  * a trigger changes state from 'unknown' to 'normal'

The aim of introducing internal events is to allow users to be notified when any internal event takes place, for example, an item becomes unsupported and stops gathering data.

Internal events are only created when internal actions for these events are enabled. To stop generation of internal events (for example, for items becoming unsupported), disable all actions for internal events in Alerts → Actions → Internal actions.

If internal actions are disabled, while an object is in the 'unsupported' state, recovery event for this object will still be created.  
  
If internal actions are enabled, while an object is in the 'unsupported' state, recovery event for this object will be created, even though 'problem event' has not been created for the object.

See also: [Receiving notification on unsupported items](/documentation/current/en/manual/config/notifications/unsupported_item)