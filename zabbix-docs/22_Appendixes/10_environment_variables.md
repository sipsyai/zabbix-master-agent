---
title: Environment variables
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/environment_variables
downloaded: 2025-11-14 10:47:08
---

# 10 Environment variables

#### Overview

Environment variables allow configuring Zabbix components without hardcoding values in configuration files. This makes it easy to manage configurations in dynamic environments, such as Docker, where variables can be passed at runtime to adapt to different setups.

In the simplest case, by setting the Zabbix server [DebugLevel](/documentation/current/en/manual/appendix/config/zabbix_server#debuglevel) configuration parameter value to an environment variable, you can then use it to configure the server on startup:
    
    
    # Zabbix server configuration file:
           DebugLevel=${NEW_DEBUG_LEVEL}
           
           # Starting Zabbix server:
           NEW_DEBUG_LEVEL=5 /usr/sbin/zabbix_server

Copy

✔ Copied

Environment variables are supported by the following Zabbix components:

  * [Server](/documentation/current/en/manual/appendix/config/zabbix_server)
  * [Proxy](/documentation/current/en/manual/appendix/config/zabbix_proxy)
  * Agent ([UNIX](/documentation/current/en/manual/appendix/config/zabbix_agentd) or [Windows](/documentation/current/en/manual/appendix/config/zabbix_agentd_win))
  * Agent 2 ([UNIX](/documentation/current/en/manual/appendix/config/zabbix_agent2) or [Windows](/documentation/current/en/manual/appendix/config/zabbix_agent2_win)), including [plugins](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins)
  * [Web service](/documentation/current/en/manual/appendix/config/zabbix_web_service)
  * Zabbix sender (when using the [-c, --config option](/documentation/current/en/manpages/zabbix_sender#options))

#### Important notes

  * When a configuration parameter is set to an environment variable, which is not specified when running the component, the default value of the parameter is used.
  * When using [runtime commands](/documentation/current/en/manual/concepts/agent#runtime-control) (e.g., to increase the agent log level), any previously used environment variables must be specified. This is because Zabbix components use their configuration file to execute runtime commands; if environment variables are omitted, configuration parameter default values will be used. See Examples.
  * The `userparameter_reload` [runtime command](/documentation/current/en/manual/concepts/agent#runtime-control) does not support reloading environment variables. During reload, variables are ignored, and only parameters with regular values are reloaded.
  * Process current environment variables, which were used in configuration files, are cleared after the Zabbix component is started. This ensures that child processes (e.g., remote scripts executed by Zabbix) cannot access these variables. However, note that process initial variables can still be retrieved (e.g., via the `/proc/<PID>/environ` file).

#### Syntax

Environment variables must use the following syntax: ${alphanumerics/underscores}.

The variable name may only include letters (a-z, A-Z), underscores (_), and digits (0-9), and must not begin with a digit.

Variables that do not match the required syntax or are combined with a regular value will be treated as regular values, which may produce errors.

Correct variable syntax:
    
    
    DebugLevel=${NEW_DEBUG_LEVEL}
           Hostname=${ZBX_HOSTNAME}
           LogFile=${LogFile_001}

Copy

✔ Copied

Incorrect variable syntax:
    
    
    DebugLevel=${5_DebugLevel}
           Hostname=${ZBX.HOSTNAME 1}
           LogFile=/${HOME}/zabbix/zabbix_server.log

Copy

✔ Copied

In Windows, environment variable names are case-insensitive.

#### Examples

The following examples show how to configure and use environment variables with Zabbix components.

##### Example 1: Configuring and testing Zabbix agent

1\. Set environment variables in the agent configuration file:
    
    
    Hostname=${ZBX_HOSTNAME}
           ServerActive=${ServerActive}

Copy

✔ Copied

2\. Test the configuration file:
    
    
    ZBX_HOSTNAME="New Zabbix agent" ServerActive=127.0.0.1 /usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf --test-config

Copy

✔ Copied

3\. Start agent with environment variables:
    
    
    ZBX_HOSTNAME="New Zabbix agent" ServerActive=127.0.0.1 /usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf

Copy

✔ Copied

When using [runtime commands](/documentation/current/en/manual/concepts/agent#runtime-control) (e.g., to increase the agent log level), any previously used environment variables must be specified:
    
    
    ZBX_HOSTNAME="New Zabbix agent" ServerActive=127.0.0.1 /usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf -R log_level_increase

Copy

✔ Copied

This is because agent uses its configuration file to execute runtime commands; if environment variables are omitted, configuration parameter default values will be used.

Alternatively, after setting environment variables in the agent configuration file, you may make them available to processes (e.g., by using the `export` command). This reduces the risk of unexpected behavior due to missing or incorrectly set variables.
    
    
    export ZBX_HOSTNAME="New Zabbix agent"
           export ServerActive=127.0.0.1
           /usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf --test-config
           /usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf
           /usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf -R log_level_increase

Copy

✔ Copied

##### Example 2: Configuring Zabbix agent for a container

If you're creating and configuring your own custom image for Zabbix components (e.g., Zabbix agent), you can define configuration parameters using environment variables and then start the container with those variables.

1\. When preparing the image, set environment variables in the agent configuration file:
    
    
    Hostname=${ZBX_HOSTNAME}
           BufferSize=${BUFSZ}
           ListenPort=${LISTENPORT}
           UserParameter=${_UsrPar01}
           UserParameter=${_UsrPar02}

Copy

✔ Copied

2\. After building the container image, start the agent container (e.g., Docker) with environment variables:
    
    
    docker run --name my-zabbix-agent -e ZBX_HOSTNAME="new-hostname" -e BUFSZ=1000 -e LISTENPORT=20050 -e _UsrPar01="key1,ls" -e _UsrPar02="key2,pwd" --init -d my-zabbix-agent:latest

Copy

✔ Copied

3\. When using [runtime commands](/documentation/current/en/manual/concepts/agent#runtime-control) (e.g., to increase the agent log level), access the container shell and execute the runtime command:
    
    
    docker exec -it <containerid> sh
           /usr/sbin/zabbix_agentd -R log_level_increase

Copy

✔ Copied

The `userparameter_reload` runtime command does not support reloading environment variables. During reload, variables are ignored, and only parameters with regular values are reloaded.