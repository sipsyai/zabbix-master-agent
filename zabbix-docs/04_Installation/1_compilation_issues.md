---
title: Compilation issues
source: https://www.zabbix.com/documentation/current/en/manual/installation/known_issues/compilation_issues
downloaded: 2025-11-14 10:34:20
---

# 1 Compilation issues

These are the known issues regarding Zabbix compilation from sources. For all other cases, see the [Known issues](/documentation/current/en/manual/installation/known_issues) page.

#### Library in a non-standard location

Zabbix allows you to specify a library located in a non-standard location. In the example below, Zabbix will run `curl-config` from the specified non-standard location and use its output to determine the correct libcurl to use.
    
    
    $ ./configure --enable-server --with-mysql --with-libcurl=/usr/local/bin/curl-config

Copy

✔ Copied

This will work if it is the only libcurl installed in the system, but might not if there is another libcurl installed in a standard location (by the package manager, for example). Such is the case when you need a newer version of the library for Zabbix and the older one for other applications.

Therefore, specifying a component in a non-standard location will not always work when the same component also exists in a standard location.

For example, if you use a newer libcurl installed in `/usr/local` with the libcurl package still installed, Zabbix might pick up the wrong one and compilation will fail:
    
    
    usr/bin/ld: ../../src/libs/zbxhttp/libzbxhttp.a(http.o): in function 'zbx_http_convert_to_utf8':
           /tmp/zabbix-master/src/libs/zbxhttp/http.c:957: undefined reference to 'curl_easy_header'
           collect2: error: ld returned 1 exit status

Copy

✔ Copied

Here, the function `curl_easy_header()` is not available in the older `/usr/lib/x86_64-linux-gnu/libcurl.so`, but is available in the newer `/usr/local/lib/libcurl.so`.

The problem lies with the order of linker flags, and one solution is to specify the full path to the library in an LDFLAGS variable:
    
    
    $ LDFLAGS="-Wl,--no-as-needed /usr/local/lib/libcurl.so" ./configure --enable-server --with-mysql --with-libcurl=/usr/local/bin/curl-config

Copy

✔ Copied

Note the `-Wl,--no-as-needed` option which might be needed on some systems (see also: default linking options on [Debian-based](https://wiki.debian.org/ToolChain/DSOLinking) systems).

#### Stack size too small on some systems

If Zabbix crashes or freezes due to stack overflows, you can increase the per-thread stack size using the `--with-stacksize` option when [configuring the sources](/documentation/current/en/manual/installation/install#configure-the-sources). This issue may occur on systems with low default thread stack limits, especially during [preprocessing](/documentation/current/en/manual/config/items/preprocessing), where multiple threads are created.

The following example sets the stack size to 512 KB per thread:
    
    
    ./configure --enable-server --with-mysql --with-stacksize=512

Copy

✔ Copied

You can check the system thread stack limits at runtime using the `ulimit -s` command on Linux-based systems.