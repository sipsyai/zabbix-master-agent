---
title: JS
source: https://www.zabbix.com/documentation/current/en/manual/concepts/js
downloaded: 2025-11-14 10:33:58
---

# 8 JS

#### Overview

zabbix_js is a command line utility that can be used for embedded script testing.

This utility will execute a user script with a string parameter and print the result. Scripts are executed using the embedded Zabbix scripting engine.

In case of compilation or execution errors zabbix_js will print the error in stderr and exit with code 1.

#### Usage
    
    
    zabbix_js -s script-file -p input-param [-l log-level] [-t timeout]
           zabbix_js -s script-file -i input-file [-l log-level] [-t timeout]
           zabbix_js -h
           zabbix_js -V

Copy

✔ Copied

zabbix_js accepts the following command line parameters:
    
    
    -s, --script script-file          Specify the file name of the script to execute. If '-' is specified as file name, the script will be read from stdin.
           -i, --input input-file            Specify the file name of the input parameter. If '-' is specified as file name, the input will be read from stdin.
           -p, --param input-param           Specify the input parameter.
           -l, --loglevel log-level          Specify the log level.
           -t, --timeout timeout             Specify the timeout in seconds. Valid range: 1-600 seconds (default: 10 seconds).
           -h, --help                        Display help information.
           -V, --version                     Display the version number.
           -w <webdriver url>                Enables browser monitoring.

Copy

✔ Copied

Example:
    
    
    zabbix_js -s script-file.js -p example

Copy

✔ Copied