---
title: Building Zabbix agent 2 on Windows
source: https://www.zabbix.com/documentation/current/en/manual/installation/install/building_zabbix_agent_2_on_windows
downloaded: 2025-11-14 10:34:05
---

# 2 Building Zabbix agent 2 on Windows

#### Overview

This page demonstrates how to build Zabbix agent 2 from sources on Windows 10 (64-bit or 32-bit).

Both 32-bit and 64-bit versions can be built on a 64-bit platform, but only the 32-bit version can be built on a 32-bit platform.

Building Zabbix agent 2 requires:

  * MinGW build tools
  * Go programming language
  * OpenSSL (for [encryption](/documentation/current/en/manual/encryption) features in Zabbix)
  * PCRE2 (Perl Compatible Regular Expressions; for regular expressions pattern matching features in Zabbix)

You can build Zabbix agent 2 using one of the following methods:

  * Using vcpkg—an automated approach that simplifies dependency management using a C++ package manager.
  * Manual build—a manual approach that requires installing all dependencies before compiling the agent.

Before starting the build process, please keep in mind:  
  

  * To execute commands, use the Command Prompt, launched by a user with sufficient permissions to write to protected folders. However, when installing OpenSSL and PCRE2, use the MSYS2 terminal.
  * It is recommended to create a working directory at `C:\Zabbix` for all source files and build folders. However, compiled components should be installed in `C:\Zabbix\x64` (or `C:\Zabbix\x86` for 32-bit builds).

#### Building Zabbix agent 2 with vcpkg

This section contains instructions for building Zabbix agent with [vcpkg](https://learn.microsoft.com/en-us/vcpkg/get_started/overview), a package manager that simplifies dependency management and integration with C++ projects.

1\. Download and install [Build Tools for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022). During installation, make sure to select the _Desktop development with C++_ workload, which includes the vcpkg package manager.

2\. Download and install [Go](https://go.dev/dl/) (available as an MSI installer). During installation, make sure to specify `C:\Zabbix\Go` as the installation folder.

3\. Download the [MinGW distribution](https://github.com/niXman/mingw-builds-binaries/releases) that uses the Microsoft Visual C runtime library; for example:

  * For 64-bit builds: `x86_64-15.1.0-release-win32-seh-msvcrt-rt_v12-rev0.7z`
  * For 32-bit builds: `i686-15.1.0-release-win32-dwarf-msvcrt-rt_v12-rev0.7z`

Then, extract it to `C:\Zabbix\mingw64` (or `C:\Zabbix\mingw32` for 32-bit builds).

4\. Initialize vcpkg and install the dependencies required for building Zabbix agent 2 (note that this may take some time):
    
    
    cd C:\Zabbix
           
           set PATH=%PATH%;"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\vcpkg"
           vcpkg new --application
           vcpkg add port pcre2
           vcpkg add port libiconv
           vcpkg add port openssl
           
           # For 64-bit builds:
           set PATH=C:\Zabbix\mingw64\bin;%PATH%
           vcpkg install --triplet x64-mingw-static --x-install-root=x64
           
           # For 32-bit builds:
           set PATH=C:\Zabbix\mingw32\bin;%PATH%
           vcpkg install --triplet x86-mingw-static --x-install-root=x86

Copy

✔ Copied

5\. Download the [Zabbix source archive](https://www.zabbix.com/download_sources#74) and extract it to `C:\Zabbix\zabbix-7.4.0`.

6\. Navigate to the Zabbix build directory (`C:\Zabbix\zabbix-7.4.0\build\mingw`) and create the following `build.bat` script:

  * For 64-bit builds:

    
    
    :: Add MinGW and Go to the system `PATH` variable for the current session:
           set PATH=C:\Zabbix\mingw64\bin;%PATH%
           set PATH=C:\Zabbix\Go\bin;%PATH%
           
           :: Set vcpkg installation path:
           set vcpkg="C:\Zabbix\x64\x64-mingw-static"
           
           :: Set linker flags for Crypt32 library:
           SET CGO_LDFLAGS="-lCrypt32"
           
           :: Run the build process:
           mingw32-make GOFLAGS="-buildvcs=false" ARCH=AMD64 ^
               PCRE2="%vcpkg%" ^
               OPENSSL="%vcpkg%" ^
               all

Copy

✔ Copied

  * For 32-bit builds:

    
    
    :: Add MinGW and Go to the system `PATH` variable for the current session:
           set PATH=C:\Zabbix\mingw32\bin;%PATH%
           set PATH=C:\Zabbix\Go\bin;%PATH%
           
           :: Set vcpkg installation path:
           set vcpkg="C:\Zabbix\x86\x86-mingw-static"
           
           :: Set linker flags for Crypt32 library:
           SET CGO_LDFLAGS="-lCrypt32"
           
           :: Run the build process:
           mingw32-make GOFLAGS="-buildvcs=false" ARCH=x86 ^
               PCRE2="%vcpkg%" ^
               OPENSSL="%vcpkg%" ^
               all

Copy

✔ Copied

7\. Compile Zabbix agent 2 by executing the script:
    
    
    build.bat

Copy

✔ Copied

After compilation, the Zabbix agent 2 binary will be located in `C:\Zabbix\zabbix-7.4.0\bin\win64` (for 64-bit builds) or `C:\Zabbix\zabbix-7.4.0\bin\win32` (for 32-bit builds). Zabbix agent 2 configuration files are located in `C:\Zabbix\zabbix-7.4.0\src\go\conf`.

To run the agent, `zabbix_agent2.exe` and its configuration files to a dedicated folder (e.g., `C:\Zabbix\agent2`) and then run the agent:
    
    
    mkdir C:\Zabbix\agent2
           
           # For 64-bit builds:
           copy C:\Zabbix\zabbix-7.4.0\bin\win64\zabbix_agent2.exe C:\Zabbix\agent2\
           
           # For 32-bit builds:
           copy C:\Zabbix\zabbix-7.4.0\bin\win32\zabbix_agent2.exe C:\Zabbix\agent2\
           
           copy C:\Zabbix\zabbix-7.4.0\src\go\conf\zabbix_agent2.win.conf C:\Zabbix\agent2\
           xcopy /E /I C:\Zabbix\zabbix-7.4.0\src\go\conf\zabbix_agent2.d C:\Zabbix\agent2\zabbix_agent2.d\
           
           C:\Zabbix\agent2\zabbix_agent2.exe -c C:\Zabbix\agent2\zabbix_agent2.win.conf

Copy

✔ Copied

If necessary, continue with compiling Zabbix agent 2 loadable plugins.

##### Compiling Zabbix agent 2 loadable plugins

1\. Download the [Zabbix plugin source](https://cdn.zabbix.com/zabbix-agent2-plugins/sources/) that matches your Zabbix agent 2 version (e.g., `zabbix-agent2-plugin-ember-plus-7.4.0.tar.gz`) and extract it to `C:\Zabbix`.

2\. Navigate to the extracted plugin directory and compile the plugin:
    
    
    cd C:\Zabbix\zabbix-agent2-plugin-ember-plus-7.4.0
           
           # For 64-bit builds:
           mingw32-make ARCH=AMD64
           
           # For 32-bit builds:
           mingw32-make ARCH=x86

Copy

✔ Copied

After compilation, the Zabbix agent 2 plugin binary and its configuration file will be located in the same plugin directory.

The plugin executable may be placed anywhere as long as it is loadable by Zabbix agent 2. Specify the path to the plugin binary in the plugin configuration file, e.g., in ember.conf for the [Ember+ plugin](/documentation/current/en/manual/appendix/config/zabbix_agent2_plugins/ember_plus_plugin):
    
    
    Plugins.EmberPlus.System.Path=/path/to/executable/zabbix-agent2-plugin-ember-plus

Copy

✔ Copied

The path to the plugin configuration file must be specified in the [Include](/documentation/current/en/manual/appendix/config/zabbix_agent2_win#include) parameter of the Zabbix agent 2 configuration file:
    
    
    Include=/path/to/plugin/configuration/file/ember.conf

Copy

✔ Copied

#### Building Zabbix agent 2 manually

This method of building Zabbix agent 2 is suitable for users who require full control over the build environment or are in a restricted environment where using vcpkg is not possible.

This section contains instructions for building Zabbix agent 2 manually, which includes installing the required build tools and dependencies, and then compiling the agent.

##### Setting up build tools

1\. Download and install [MSYS2](https://www.msys2.org/) (available as an MSI installer). During installation, make sure to specify `C:\Zabbix\msys64` as the installation folder.

2\. Download and install [Go](https://go.dev/dl/) (available as an MSI installer; see currently supported [Go versions](/documentation/current/en/manual/installation/requirements#agent-2)). During installation, make sure to specify `C:\Zabbix\Go` as the installation folder.

3\. Download the [MinGW distribution](https://github.com/niXman/mingw-builds-binaries/releases) that uses the Microsoft Visual C runtime library; for example:

  * For 64-bit builds: `x86_64-15.1.0-release-win32-seh-msvcrt-rt_v12-rev0.7z`
  * For 32-bit builds: `i686-15.1.0-release-win32-dwarf-msvcrt-rt_v12-rev0.7z`

Then, extract it to `C:\Zabbix\mingw64` (or `C:\Zabbix\mingw32` for 32-bit builds).

##### Installing OpenSSL

To compile Zabbix agent without TLS support, proceed to the Installing PCRE2 section.

1\. Open the MSYS2 MSYS terminal with administrator privileges and run the following commands:
    
    
    pacman -S perl-Locale-Maketext-Simple
           pacman -S nasm
           pacman -S make
           pacman -S cmake

Copy

✔ Copied

2\. Download the [OpenSSL source archive](https://openssl-library.org/source/) and extract it to `C:\Zabbix\openssl-3.5.0`.

3\. Navigate to the extracted OpenSSL directory and create the following `build.sh` script:

  * For 64-bit builds:

    
    
    #!/usr/bin/env bash
           
           export PATH="/c/Zabbix/mingw64/bin:$PATH"
           export d="/c/Zabbix/x64/OpenSSL-Win64-350-static"
           
           perl Configure mingw64 no-shared no-capieng no-winstore no-srp no-gost no-dgram no-dtls1-method no-dtls1_2-method thread_scheme=winthreads --api=1.1.0 --prefix=$d --openssldir=$d
           
           make
           make install

Copy

✔ Copied

  * For 32-bit builds:

    
    
    #!/usr/bin/env bash
           
           export PATH="/c/Zabbix/mingw32/bin:$PATH"
           export d="/c/Zabbix/x86/OpenSSL-Win64-350-static"
           
           perl Configure mingw no-shared no-capieng no-winstore no-srp no-gost no-dgram no-dtls1-method no-dtls1_2-method thread_scheme=winthreads --api=1.1.0 --prefix=$d --openssldir=$d
           
           make
           make install

Copy

✔ Copied

Make sure to revoke write access from non-administrator users to the `C:\Zabbix\x64\OpenSSL-Win64-350-static` directory. Otherwise, the agent will load SSL settings from a path that can be modified by unprivileged users, resulting in a potential security vulnerability.

  * The `no-shared` option makes libcrypto.lib and libssl.lib OpenSSL static libraries self-contained, so Zabbix binaries include OpenSSL without needing external DLLs. This means that Zabbix binaries can be copied to other Windows machines without OpenSSL libraries; however, when a new OpenSSL bugfix version is released, Zabbix agent will need to be recompiled.
  * Without the `no-shared` option, Zabbix relies on OpenSSL DLLs at runtime. This means that OpenSSL updates may not require recompiling Zabbix agent; however, when copying it to other machines, the OpenSSL DLLs must be also be copied.

For more information about other OpenSSL configuration options, refer to [OpenSSL documentation](https://github.com/openssl/openssl/blob/master/INSTALL.md#configuration-options).

4\. Configure and install OpenSSL by executing the script (note that this may take some time):
    
    
    cd /c/Zabbix/openssl-3.5.0
           ./build.sh

Copy

✔ Copied

##### Installing PCRE2

1\. Download [PCRE2 source archive](https://github.com/PCRE2Project/pcre2/releases/latest) and extract it to `C:\Zabbix\pcre2-10.45`.

2\. Open the MSYS2 MSYS terminal with administrator privileges. Then, create a `build` directory in the extracted PCRE2 directory and navigate to it:
    
    
    mkdir /c/Zabbix/pcre2-10.45/build
           cd /c/Zabbix/pcre2-10.45/build

Copy

✔ Copied

3\. Configure PCRE2:
    
    
    # For 64-bit builds:
           export PATH="/c/Zabbix/mingw64/bin:$PATH"
           cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_C_FLAGS="-O2 -g" -DCMAKE_INSTALL_PREFIX="/c/Zabbix/x64/PCRE2" ..
           
           # For 32-bit builds:
           export PATH="/c/Zabbix/mingw32/bin:$PATH"
           cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_C_FLAGS="-m32 -O2 -g" -DCMAKE_EXE_LINKER_FLAGS="-Wl,-mi386pe" -DCMAKE_INSTALL_PREFIX="/c/Zabbix/x86/PCRE2" ..

Copy

✔ Copied

If any errors occur, it is recommended to delete the CMake cache before attempting to repeat the CMake build process. The cache (`CMakeCachecache.txt`) can be located in the build directory of the extracted PCRE2 directory.

4\. Install PCRE2:
    
    
    make install

Copy

✔ Copied

##### Compiling Zabbix agent 2

1\. Download the [Zabbix source archive](https://www.zabbix.com/download_sources#74) and extract it to `C:\Zabbix\zabbix-7.4.0`.

If you need to generate a source archive from the raw source repository (e.g., to apply custom patches or build from the latest source code), run the following commands on a **Linux** machine with [Go](https://go.dev/) installed (required for configuring Zabbix agent 2):
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git
           cd zabbix
           ./bootstrap.sh
           ./configure --enable-agent2 --enable-ipv6 --prefix=`pwd`
           make dist

Copy

✔ Copied

This will create a source archive, which can then be copied to a Windows machine.

2\. Open the Command Prompt with administrator privileges. Then, navigate to the Zabbix build directory and compile Zabbix agent; make sure to correctly specify the directories where OpenSSL and PCRE2 are installed:

  * For 64-bit builds:

    
    
    cd C:\Zabbix\zabbix-7.4.0\build\mingw
           set PATH=C:\Zabbix\mingw64\bin;%PATH%
           mklink /D C:\Zabbix\x64\OpenSSL-Win64-350-static\lib C:\Zabbix\x64\OpenSSL-Win64-350-static\lib64
           
           # With TLS support:
           mingw32-make ARCH=AMD64 PCRE2="C:\Zabbix\x64\PCRE2" OPENSSL="C:\Zabbix\x64\OpenSSL-Win64-350-static"
           
           # Without TLS support:
           mingw32-make ARCH=AMD64 PCRE2="C:\Zabbix\x64\PCRE2"

Copy

✔ Copied

  * For 32-bit builds:

    
    
    cd C:\Zabbix\zabbix-7.4.0\build\mingw
           set PATH=C:\Zabbix\mingw32\bin;%PATH%
           
           # With TLS support:
           mingw32-make ARCH=x86 PCRE2="C:\Zabbix\x86\PCRE2" OPENSSL="C:\Zabbix\x86\OpenSSL-Win64-350-static"
           
           # Without TLS support:
           mingw32-make ARCH=x86 PCRE2="C:\Zabbix\x86\PCRE2"

Copy

✔ Copied

After compilation, the Zabbix agent 2 binary will be located in `C:\Zabbix\zabbix-7.4.0\bin\win64` (or `C:\Zabbix\zabbix-7.4.0\bin\win32` for 32-bit builds). Zabbix agent 2 configuration files are located in `C:\Zabbix\zabbix-7.4.0\src\go\conf`.

To run the agent, copy the `zabbix_agent2.exe` binary and its configuration files to a dedicated folder (e.g., `C:\Zabbix\agent2`) and then run the agent:
    
    
    mkdir C:\Zabbix\agent2
           copy C:\Zabbix\zabbix-7.4.0\bin\win64\zabbix_agent2.exe C:\Zabbix\agent2\
           copy C:\Zabbix\zabbix-7.4.0\src\go\conf\zabbix_agent2.win.conf C:\Zabbix\agent2\
           xcopy /E /I C:\Zabbix\zabbix-7.4.0\src\go\conf\zabbix_agent2.d C:\Zabbix\agent2\zabbix_agent2.d\
           
           C:\Zabbix\agent2\zabbix_agent2.exe -c C:\Zabbix\agent2\zabbix_agent2.win.conf

Copy

✔ Copied

If necessary, continue with compiling Zabbix agent 2 loadable plugins.