---
title: User parameters
source: https://www.zabbix.com/documentation/current/en/manual/config/items/userparameters
downloaded: 2025-11-14 10:35:22
---

# 5 User parameters

#### Overview

Sometimes you may want to run an agent check that does not come predefined with Zabbix. This is where user parameters come to help.

You may write a command that retrieves the data you need and include it in the user parameter in the [agent configuration file](/documentation/current/en/manual/appendix/config/zabbix_agentd) ('UserParameter' configuration parameter).

A user parameter has the following syntax:
    
    
    UserParameter=<key>,<command>

Copy

✔ Copied

As you can see, a user parameter also contains a key. The key will be necessary when configuring an item. Enter a key of your choice that will be easy to reference (it must be unique within a host).

Restart the agent or use the agent [runtime control](/documentation/current/en/manual/concepts/agent#runtime-control) option to pick up the new parameter, e. g.:
    
    
    zabbix_agentd -R userparameter_reload

Copy

✔ Copied

Then, when [configuring an item](/documentation/current/en/manual/config/items/item), enter the key to reference the command from the user parameter you want executed.

User parameters are commands executed by Zabbix agent. Note that up to 16MB of data can be returned before [item value preprocessing](/documentation/current/en/manual/config/items/preprocessing) steps.

**/bin/sh** is used as a command line interpreter under UNIX operating systems. User parameters obey the agent check timeout; if timeout is reached the forked user parameter process is terminated.

See also:

  * [Step-by-step tutorial](/documentation/current/en/manual/config/items/userparameters/extending_agent) on making use of user parameters
  * [Command execution](/documentation/current/en/manual/appendix/command_execution)

##### Examples of simple user parameters

A simple command:
    
    
    UserParameter=ping,echo 1

Copy

✔ Copied

The agent will always return '1' for an item with 'ping' key.

A more complex example:
    
    
    UserParameter=mysql.ping,mysqladmin -uroot ping | grep -c alive

Copy

✔ Copied

The agent will return '1', if MySQL server is alive, '0' - otherwise.

#### Flexible user parameters

Flexible user parameters accept parameters with the key. This way a flexible user parameter can be the basis for creating several items.

Flexible user parameters have the following syntax:
    
    
    UserParameter=key[*],command

Copy

✔ Copied

**Key** | Unique item key. The [*] defines that this key accepts parameters within the brackets.  
Parameters are given when configuring the item.  
---|---  
**Command** | Command to be executed to evaluate value of the key.  
_For flexible user parameters only_ :  
You may use positional references $1…$9 in the command to refer to the respective parameter in the item key.  
Zabbix parses the parameters enclosed in [ ] of the item key and substitutes $1,...,$9 in the command accordingly.  
$0 will be substituted by the original command (prior to expansion of $0,...,$9) to be run.  
Positional references are interpreted regardless of whether they are enclosed between double (") or single (') quotes.  
To use positional references unaltered, specify a double dollar sign - for example, awk '{print $$2}'. In this case `$$2` will actually turn into `$2` when executing the command.  
  
Positional references with the $ sign are searched for and replaced by Zabbix agent only for flexible user parameters. For simple user parameters, such reference processing is skipped and, therefore, any $ sign quoting is not necessary.

Certain symbols are not allowed in user parameters by default. See [UnsafeUserParameters](/documentation/current/en/manual/appendix/config/zabbix_agentd) documentation for a full list.

##### Example 1

Something very simple:
    
    
    UserParameter=ping[*],echo $1

Copy

✔ Copied

We may define unlimited number of items for monitoring all having format ping[something].

  * ping[0] - will always return '0'
  * ping[aaa] - will always return 'aaa'

##### Example 2

Let's add more sense!
    
    
    UserParameter=mysql.ping[*],mysqladmin -u$1 -p$2 ping | grep -c alive

Copy

✔ Copied

This parameter can be used for monitoring availability of MySQL database. We can pass user name and password:
    
    
    mysql.ping[zabbix,our_password]

Copy

✔ Copied

##### Example 3

How many lines matching a regular expression in a file?
    
    
    UserParameter=wc[*],grep -c "$2" $1

Copy

✔ Copied

This parameter can be used to calculate number of lines in a file.
    
    
    wc[/etc/passwd,root]
           wc[/etc/services,zabbix]

Copy

✔ Copied

#### Command result

The return value of the command is a standard output together with a standard error produced by the command.

An item that returns text (character, log, or text type of information) will not become unsupported in case of a standard error output.

The return value is limited to 16MB (including trailing whitespace that is truncated); [database limits](/documentation/current/en/manual/config/items/item#text-data-limits) also apply.

User parameters that return text (character, log, or text type of information) can also return a whitespace. In case of an invalid result, the item will become unsupported.