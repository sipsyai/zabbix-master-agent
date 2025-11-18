---
title: Restricting agent checks
source: https://www.zabbix.com/documentation/current/en/manual/config/items/restrict_checks
downloaded: 2025-11-14 10:35:30
---

# 12 Restricting agent checks

#### Overview

It is possible to restrict checks on the agent side by creating an item blacklist, a whitelist, or a combination of whitelist/blacklist.

To do that use a combination of two agent [configuration](/documentation/current/en/manual/appendix/config/zabbix_agentd) parameters:

  * `AllowKey=<pattern>` \- which checks are allowed; <pattern> is specified using a wildcard (*) expression
  * `DenyKey=<pattern>` \- which checks are denied; <pattern> is specified using a wildcard (*) expression

Note that:

  * All system.run[*] items (remote commands, scripts) are disabled by default, even when no deny keys are specified, it should be assumed that DenyKey=system.run[*] is implicitly appended.
  * Since Zabbix 5.0.2 the EnableRemoteCommands agent parameter is: 
    * deprecated by Zabbix agent
    * unsupported by Zabbix agent2

Therefore, to allow remote commands, specify an AllowKey=system.run[<command>,*] for each allowed command, * stands for wait and nowait mode. It is also possible to specify AllowKey=system.run[*] parameter to allow all commands with wait and nowait modes. To disallow specific remote commands, add DenyKey parameters with system.run[] commands before the AllowKey=system.run[*] parameter.

#### Important rules

  * A whitelist without a deny rule is only allowed for system.run[*] items. For all other items, AllowKey parameters are not allowed without a DenyKey parameter; in this case Zabbix agent **will not start** with only AllowKey parameters.
  * The order matters. The specified parameters are checked one by one according to their appearance order in the configuration file: 
    * As soon as an item key matches an allow/deny rule, the item is either allowed or denied; and rule checking stops. So if an item matches both an allow rule and a deny rule, the result will depend on which rule comes first.
    * The order affects also EnableRemoteCommands parameter (if used).
  * Unlimited numbers of AllowKey/DenyKey parameters is supported.
  * AllowKey, DenyKey rules do not affect HostnameItem, HostMetadataItem, HostInterfaceItem configuration parameters.
  * Key pattern is a wildcard expression where the wildcard (*) character matches any number of any characters in certain position. It might be used in both the key name and parameters.
  * If a specific item key is disallowed in the agent configuration, the item will be reported as unsupported (no hint is given as to the reason);
  * Zabbix agent with --print (-p) command line option will not show keys that are not allowed by configuration;
  * Zabbix agent with --test (-t) command line option will return "Unsupported item key." status for keys that are not allowed by configuration;
  * Denied remote commands will not be logged in the agent log (if LogRemoteCommands=1).

#### Use cases

##### Deny specific check

  * Blacklist a specific check with DenyKey parameter. Matching keys will be disallowed. All non-matching keys will be allowed, except system.run[] items.

For example:
    
    
    # Deny secure data access
           DenyKey=vfs.file.contents[/etc/passwd,*]

Copy

✔ Copied

A blacklist may not be a good choice, because a new Zabbix version may have new keys that are not explicitly restricted by the existing configuration. This could cause a security flaw.

##### Deny specific command, allow others

  * Blacklist a specific command with DenyKey parameter. Whitelist all other commands, with the AllowKey parameter.

    
    
    # Disallow specific command
           DenyKey=system.run[ls -l /]
            
           # Allow other scripts
           AllowKey=system.run[*]

Copy

✔ Copied

##### Allow specific check, deny others

  * Whitelist specific checks with AllowKey parameters, deny others with `DenyKey=*`

For example:
    
    
    # Allow reading logs:
           AllowKey=vfs.file.*[/var/log/*]
           
           # Allow localtime checks
           AllowKey=system.localtime[*]
           
           # Deny all other keys
           DenyKey=*

Copy

✔ Copied

##### Allow script with spaces in path and arguments

  * Whitelist a script located in a path that contains spaces and allow passing arguments to it. On Windows, escape spaces using `^` when specifying the path.

For example:
    
    
    # Allow running test.bat with or without arguments
           AllowKey=system.run["C:\Program^ Files\Zabbix^ Agent^ 2\scripts\test.bat*"]

Copy

✔ Copied

To test:
    
    
    PS C:\Program Files\Zabbix Agent 2> .\zabbix_get.exe -s 127.0.0.1 -k system.run["C:\Program^ Files\Zabbix^ Agent^ 2\scripts\test.bat caret"]

Copy

✔ Copied

This configuration allows execution of the script regardless of whether arguments are passed (such as `caret`) and ensures that `system.run` is permitted even if the script path contains spaces.

#### Pattern examples

_*_ | Matches all possible keys with or without parameters. | Any | None  
---|---|---|---  
_vfs.file.contents_ | Matches `vfs.file.contents` without parameters. | vfs.file.contents | vfs.file.contents[/etc/passwd]  
_vfs.file.contents[]_ | Matches `vfs.file.contents` with empty parameters. | vfs.file.contents[] | vfs.file.contents  
_vfs.file.contents[*]_ | Matches `vfs.file.contents` with any parameters; will not match `vfs.file.contents` without square brackets. | vfs.file.contents[]  
vfs.file.contents[/path/to/file] | vfs.file.contents  
_vfs.file.contents[/etc/passwd,*]_ | Matches `vfs.file.contents` with first parameters matching /etc/passwd and all other parameters having any value (also empty). | vfs.file.contents[/etc/passwd,]  
vfs.file.contents[/etc/passwd,utf8] | vfs.file.contents[/etc/passwd]  
vfs.file.contents[/var/log/zabbix_server.log]  
vfs.file.contents[]  
_vfs.file.contents[*passwd*]_ | Matches `vfs.file.contents` with first parameter matching *passwd* and no other parameters. | vfs.file.contents[/etc/passwd] | vfs.file.contents[/etc/passwd,]  
vfs.file.contents[/etc/passwd, utf8]  
_vfs.file.contents[*passwd*,*]_ | Matches `vfs.file.contents` with only first parameter matching *passwd* and all following parameters having any value (also empty). | vfs.file.contents[/etc/passwd,]  
vfs.file.contents[/etc/passwd, utf8] | vfs.file.contents[/etc/passwd]  
vfs.file.contents[/tmp/test]  
_vfs.file.contents[/var/log/zabbix_server.log,*,abc]_ | Matches `vfs.file.contents` with first parameter matching /var/log/zabbix_server.log, third parameter matching 'abc' and any (also empty) second parameter. | vfs.file.contents[/var/log/zabbix_server.log,,abc]  
vfs.file.contents[/var/log/zabbix_server.log,utf8,abc] | vfs.file.contents[/var/log/zabbix_server.log,,abc,def]  
_vfs.file.contents[/etc/passwd,utf8]_ | Matches `vfs.file.contents` with first parameter matching /etc/passwd, second parameter matching 'utf8' and no other arguments. | vfs.file.contents[/etc/passwd,utf8] | vfs.file.contents[/etc/passwd,]  
vfs.file.contents[/etc/passwd,utf16]  
_vfs.file.*_ | Matches any keys starting with `vfs.file.` without any parameters. | vfs.file.contents  
vfs.file.size | vfs.file.contents[]  
vfs.file.size[/var/log/zabbix_server.log]  
_vfs.file.*[*]_ | Matches any keys starting with `vfs.file.` with any parameters. | vfs.file.size.bytes[]  
vfs.file.size[/var/log/zabbix_server.log, utf8] | vfs.file.size.bytes  
_vfs.*.contents_ | Matches any key starting with `vfs.` and ending with `.contents` without any parameters. | vfs.mount.point.file.contents  
vfs..contents | vfs.contents  
  
#### system.run and AllowKey

A hypothetical script like 'myscript.sh' may be executed on a host via Zabbix agent in several ways:

1\. As an item key in a passive or active check, for example:

  * system.run[myscript.sh]
  * system.run[myscript.sh,wait]
  * system.run[myscript.sh,nowait]

Here the user may add "wait", "nowait" or omit the 2nd argument to use its default value in system.run[].

2\. As a global script (initiated by user in frontend or API).

A user configures this script in _Alerts_ → _Scripts_ , sets "Execute on: Zabbix agent" and puts "myscript.sh" into the script's "Commands" input field. When invoked from frontend or API the Zabbix server sends to agent:

  * system.run[myscript.sh,wait] - up to Zabbix 5.0.4
  * system.run[myscript.sh] - since 5.0.5

Here the user does not control the "wait"/"nowait" parameters.

3\. As a remote command from an action. The Zabbix server sends to agent:

  * system.run[myscript.sh,nowait]

Here again the user does not control the "wait"/"nowait" parameters.

What that means is if we set AllowKey like:
    
    
    AllowKey=system.run[myscript.sh]

Copy

✔ Copied

then

  * system.run[myscript.sh] - will be allowed
  * system.run[myscript.sh,wait], system.run[myscript.sh,nowait] will not be allowed - the script will not be run if invoked as a step of action

To allow all described variants you may add:
    
    
    AllowKey=system.run[myscript.sh,*] 
           DenyKey=system.run[*]

Copy

✔ Copied

to the agent/agent2 parameters.