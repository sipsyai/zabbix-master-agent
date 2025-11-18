---
title: Telnet checks
source: https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/telnet_checks
downloaded: 2025-11-14 10:35:11
---

# 10 Telnet checks  
  
#### Overview

Telnet checks are performed as agent-less monitoring. Zabbix agent is not needed for Telnet checks.

#### Configurable fields

Actual command(s) to be executed must be placed in the **Executed script** field in the item configuration.  
Multiple commands can be executed one after another by placing them on a new line. In this case returned value also will be formatted as multilined.

Supported characters that the shell prompt can end with:

  * $
  * #
  * >
  * %

A telnet prompt line which ended with one of these characters will be removed from the returned value, but only for the first command in the commands list, i.e. only at a start of the telnet session.

**telnet.run[ <unique short description>,<ip>,<port>,<encoding>]** | Run a command on a remote device using telnet connection  
---|---  
  
If a telnet check returns a value with non-ASCII characters and in non-UTF8 encoding then the _< encoding>_ parameter of the key should be properly specified. See [encoding of returned values](/documentation/current/en/manual/appendix/items/encoding_of_values) page for more details.