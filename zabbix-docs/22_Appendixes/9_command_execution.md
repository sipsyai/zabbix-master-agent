---
title: Command execution
source: https://www.zabbix.com/documentation/current/en/manual/appendix/command_execution
downloaded: 2025-11-14 10:47:54
---

# 9 Command execution

Zabbix uses common functionality for external checks, user parameters, system.run items, custom alert scripts, remote commands and global scripts.

#### Execution steps

By default, all scripts in Zabbix are executed using the _sh_ shell, and it is not possible to modify the default shell. To utilize a different shell, you can employ a workaround: create a script file and invoke that script during command execution.

The command/script is executed similarly on both Unix and Windows platforms:

  1. Zabbix (the parent process) creates a pipe for communication
  2. Zabbix sets the pipe as the output for the to-be-created child process
  3. Zabbix creates the child process (runs the command/script)
  4. A new process group (in Unix) or a job (in Windows) is created for the child process
  5. Zabbix reads from the pipe until timeout occurs or no one is writing to the other end (ALL handles/file descriptors have been closed). Note that the child process can create more processes and exit before they exit or close the handle/file descriptor.
  6. If the timeout has not been reached, Zabbix waits until the initial child process exits or timeout occurs
  7. If the initial child process exited and the timeout has not been reached, Zabbix checks exit code of the initial child process and compares it to 0 (non-zero value is considered as execution failure, only for custom alert scripts, remote commands and user scripts executed on Zabbix server and Zabbix proxy)
  8. At this point it is assumed that everything is done and the whole process tree (i.e. the process group or the job) is terminated

Zabbix assumes that a command/script has done processing when the initial child process has exited AND no other process is still keeping the output handle/file descriptor open. When processing is done, ALL created processes are terminated.

All double quotes and backslashes in the command are escaped with backslashes and the command is enclosed in double quotes.

#### Exit code checking

Exit code are checked with the following conditions:

  * Only for custom alert scripts, remote commands and user scripts executed on Zabbix server and Zabbix proxy.
  * Any exit code that is different from 0 is considered as execution failure.
  * Contents of standard error and standard output for failed executions are collected and available in frontend (where execution result is displayed).
  * Additional log entry may be created for remote commands executed on Zabbix agent/proxy by enabling the LogRemoteCommands parameter on [agent](/documentation/current/en/manual/appendix/config/zabbix_agentd#logremotecommands)/[proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy#logremotecommands).

Possible frontend messages and log entries for failed commands/scripts:

  * Contents of standard error and standard output for failed executions (if any).
  * "Process exited with code: N." (for empty output, and exit code not equal to 0).
  * "Process killed by signal: N." (for process terminated by a signal, on Linux only).
  * "Process terminated unexpectedly." (for process terminated for unknown reasons).

#### See also

  * [External checks](/documentation/current/en/manual/config/items/itemtypes/external#external-check-result)
  * [User parameters](/documentation/current/en/manual/config/items/userparameters)
  * [system.run](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#system.run) items
  * [Custom alert scripts](/documentation/current/en/manual/config/notifications/media/script)
  * [Remote commands](/documentation/current/en/manual/config/notifications/action/operation/remote_command)
  * [Global scripts](/documentation/current/en/manual/web_interface/frontend_sections/alerts/scripts)