---
title: Building Zabbix agent on Windows
source: https://www.zabbix.com/documentation/current/en/manual/installation/install/win_agent
downloaded: 2025-11-14 10:34:04
---

# 1 Building Zabbix agent on Windows

#### Overview

This page demonstrates how to build Zabbix agent from source on Windows 10 (64-bit).

These instructions apply to Windows versions that support Visual Studio 2022.

Building Zabbix agent requires:

  * C compiler (included in Build Tools for Visual Studio 2022)
  * OpenSSL (for [encryption](/documentation/current/en/manual/encryption) features in Zabbix)
  * PCRE2 (Perl Compatible Regular Expressions; for regular expressions pattern matching features in Zabbix)

You can build Zabbix agent using one of the following methods:

  * Using vcpkg—an automated approach that simplifies dependency management using a C++ package manager.
  * Manual build—a manual approach that requires installing all dependencies before compiling the agent.

Depending on your monitoring needs, additional libraries may be required. For more information, see [Requirements](/documentation/current/en/manual/installation/requirements#agent).

Before starting the build process, please keep in mind:  
  

  * To execute commands, use the x64 Native Tools Command Prompt (included in Build Tools for Visual Studio 2022), launched by a user with sufficient permissions to write to protected folders.
  * It is recommended to create a working directory at `C:\Zabbix` for all source files and build folders. However, compiled components should be installed in `C:\Program Files\Zabbix\x64`.

#### Building Zabbix agent with vcpkg

This section contains instructions for building Zabbix agent with [vcpkg](https://learn.microsoft.com/en-us/vcpkg/get_started/overview), a package manager that simplifies dependency management and integration with C++ projects.

1\. Download and install [Build Tools for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022). During installation, make sure to select the _Desktop development with C++_ workload, which includes the tools required for building the agent with vcpkg:

  * C compiler (Microsoft Visual C++)
  * NMake command-line tool
  * vcpkg package manager
  * x64 Native Tools Command Prompt

2\. Initialize vcpkg and install the dependencies required for building Zabbix agent (note that this may take some time):
    
    
    cd C:\Zabbix
           vcpkg new --application
           vcpkg add port pcre2
           vcpkg add port openssl
           vcpkg install --triplet x64-windows-static --x-install-root="C:\Program Files\Zabbix\x64"

Copy

✔ Copied

3\. Download the [Zabbix source archive](https://www.zabbix.com/download_sources#74) and extract it to `C:\Zabbix\zabbix-7.4.0`.

4\. Navigate to the Zabbix build directory (`C:\Zabbix\zabbix-7.4.0\build\win32\project`) and create the following `build.bat` script; make sure to correctly specify the directories where OpenSSL and PCRE2 are installed:
    
    
    :: Set vcpkg installation path:
           set vcpkg=C:\Program Files\Zabbix\x64\x64-windows-static
           
           :: Run the build process:
           nmake -f Makefile CPU=AMD64 ^
               PCRE2INCDIR="%vcpkg%\include" ^
               PCRE2LIBDIR="%vcpkg%\lib" ^
               TLS=openssl ^
               TLSINCDIR="%vcpkg%\include" ^
               TLSLIBDIR="%vcpkg%\lib" ^
               LIBS="$(LIBS) Crypt32.lib" ^
               all

Copy

✔ Copied

5\. Compile Zabbix agent by executing the script:
    
    
    build.bat

Copy

✔ Copied

After compilation, Zabbix component binaries will be located in `C:\Zabbix\zabbix-7.4.0\bin\win64`. Zabbix agent configuration file is located in `C:\Zabbix\zabbix-7.4.0\conf`.

To run the agent, copy `zabbix_agent.exe` and its configuration file to a dedicated folder (e.g., `C:\Zabbix\agent`) and then run the agent:
    
    
    mkdir C:\Zabbix\agent
           copy C:\Zabbix\zabbix-7.4.0\bin\win64\zabbix_agent.exe C:\Zabbix\agent\
           copy C:\Zabbix\zabbix-7.4.0\conf\zabbix_agent.win.conf C:\Zabbix\agent\
           
           C:\Zabbix\agent\zabbix_agent.exe -c C:\Zabbix\agent\zabbix_agent.win.conf

Copy

✔ Copied

#### Building Zabbix agent manually

This method of building Zabbix agent is suitable for users who require full control over the build environment or are in a restricted environment where using vcpkg is not possible.

This section contains instructions for building Zabbix agent manually, which includes installing the required build tools and dependencies (Perl, OpenSSL, PCRE2), and then compiling the agent.

##### Installing build tools

1\. Download and install [Build Tools for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022). During installation, make sure to select the _Desktop development with C++_ workload, which includes the tools required for building the agent manually:

  * C compiler (Microsoft Visual C++)
  * NMake command-line tool
  * x64 Native Tools Command Prompt

##### Installing OpenSSL

To compile Zabbix agent without TLS support, proceed to the Installing PCRE2 section.

1\. Download and install [Strawberry Perl](https://strawberryperl.com/) (available as an MSI installer). During installation, make sure to specify `C:\Zabbix\Strawberry` as the installation folder.

2\. Install the `Text::Template` Perl module:
    
    
    cpanm Text::Template

Copy

✔ Copied

3\. Verify that the Netwide Assembler (NASM; required for compiling OpenSSL), was compiled during the installation of Strawberry Perl:
    
    
    nasm -v
           # NASM version 2.16.01 compiled on May  3 2024

Copy

✔ Copied

If NASM is not compiled, install it manually. For more information, refer to [NASM documentation](https://www.nasm.us/docs.php).

4\. Download the [OpenSSL source archive](https://openssl-library.org/source/) and extract it to `C:\Zabbix\openssl-3.5.0`.

5\. Navigate to the extracted directory and configure OpenSSL, for example:
    
    
    cd C:\Zabbix\openssl-3.5.0
           perl Configure VC-WIN64A no-shared no-capieng no-winstore no-srp no-gost no-dgram no-dtls1-method no-dtls1_2-method --api=1.1.0 --prefix="C:\Program Files\Zabbix\x64\OpenSSL" --openssldir="C:\Program Files\Zabbix\x64\OpenSSL"

Copy

✔ Copied

If you choose a custom directory for OpenSSL when compiling Zabbix agent on Windows (e.g., `C:\zabbix` or `C:\openssl-64bit`), make sure to revoke write access from non-administrator users to this directory. Otherwise, the agent will load SSL settings from a path that can be modified by unprivileged users, resulting in a potential security vulnerability.

  * The `no-shared` option makes libcrypto.lib and libssl.lib OpenSSL static libraries self-contained, so Zabbix binaries include OpenSSL without needing external DLLs. This means that Zabbix binaries can be copied to other Windows machines without OpenSSL libraries; however, when a new OpenSSL bugfix version is released, Zabbix agent will need to be recompiled.
  * Without the `no-shared` option, Zabbix relies on OpenSSL DLLs at runtime. This means that OpenSSL updates may not require recompiling Zabbix agent; however, when copying it to other machines, the OpenSSL DLLs must be also be copied.

For more information about other OpenSSL configuration options, refer to [OpenSSL documentation](https://github.com/openssl/openssl/blob/master/INSTALL.md#configuration-options).

6\. Compile OpenSSL and run tests (note that this may take some time):

Run the tests without administrative privileges; otherwise, it may lead to unexpected results or security risks. If some tests fail, refer to [OpenSSL documentation](https://github.com/openssl/openssl/blob/master/test/README.md) for troubleshooting.
    
    
    nmake
           nmake test
           ...
           All tests successful.
           Files=325, Tests=3101, 822 wallclock secs ( 4.81 usr +  0.81 sys =  5.62 CPU)
           Result: PASS

Copy

✔ Copied

7\. Install OpenSSL:
    
    
    nmake install

Copy

✔ Copied

To install only software components (libraries, header files, but no documentation), you may use `nmake install_sw`.

##### Installing PCRE2

1\. Download and install [CMake](https://cmake.org/download/) (available as an MSI installer). During installation, make sure to specify `C:\Zabbix\CMake` as the installation folder and select the _Add CMake to the PATH environment variable_ option.

2\. Download the [PCRE2 source archive](https://github.com/PCRE2Project/pcre2/releases/latest) and extract it to `C:\Zabbix\pcre2-10.45`.

3\. Create a `build` directory in the extracted PCRE2 directory and navigate to it:
    
    
    mkdir C:\Zabbix\pcre2-10.45\build
           cd C:\Zabbix\pcre2-10.45\build

Copy

✔ Copied

4\. Configure PCRE2:
    
    
    cmake -G "NMake Makefiles" -DPCRE_SUPPORT_UNICODE_PROPERTIES=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="C:\Program Files\Zabbix\x64\PCRE2" "C:\Zabbix\pcre2-10.45"

Copy

✔ Copied

If any errors occur, it is recommended to delete the CMake cache before attempting to repeat the CMake build process. The cache (`CMakeCachecache.txt`) can be located in the build directory of the extracted PCRE2 directory.

5\. Build PCRE2 using NMake:
    
    
    nmake

Copy

✔ Copied

6\. Install PCRE2:
    
    
    cmake --install .

Copy

✔ Copied

##### Compiling Zabbix agent

1\. Download the [Zabbix source archive](https://www.zabbix.com/download_sources#74) and extract it to `C:\Zabbix\zabbix-7.4.0`.

If you need to generate a source archive from the raw source repository (e.g., to apply custom patches or build from the latest source code), run the following commands on a **Linux** machine:
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git
           cd zabbix
           ./bootstrap.sh
           ./configure --enable-agent --enable-ipv6 --prefix=`pwd`
           make dist

Copy

✔ Copied

This will create a source archive, which can then be copied to a Windows machine.

2\. Navigate to the Zabbix build directory and compile Zabbix agent (or other components); make sure to correctly specify the directories where OpenSSL and PCRE2 are installed:
    
    
    cd C:\Zabbix\zabbix-7.4.0\build\win32\project
           
           # With TLS support:
           nmake /K -f Makefile_agent PCRE2INCDIR="C:\Program Files\Zabbix\x64\PCRE2\include" PCRE2LIBDIR="C:\Program Files\Zabbix\x64\PCRE2\lib" TLS=openssl TLSINCDIR="C:\Program Files\Zabbix\x64\OpenSSL\include" TLSLIBDIR="C:\Program Files\Zabbix\x64\OpenSSL\lib"
           nmake /K -f Makefile_get PCRE2INCDIR="C:\Program Files\Zabbix\x64\PCRE2\include" PCRE2LIBDIR="C:\Program Files\Zabbix\x64\PCRE2\lib" TLS=openssl TLSINCDIR="C:\Program Files\Zabbix\x64\OpenSSL\include" TLSLIBDIR="C:\Program Files\Zabbix\x64\OpenSSL\lib"
           nmake /K -f Makefile_sender PCRE2INCDIR="C:\Program Files\Zabbix\x64\PCRE2\include" PCRE2LIBDIR="C:\Program Files\Zabbix\x64\PCRE2\lib" TLS=openssl TLSINCDIR="C:\Program Files\Zabbix\x64\OpenSSL\include" TLSLIBDIR="C:\Program Files\Zabbix\x64\OpenSSL\lib"
           
           # Without TLS support:
           nmake /K -f Makefile_agent PCRE2INCDIR="C:\Program Files\Zabbix\x64\PCRE2\include" PCRE2LIBDIR="C:\Program Files\Zabbix\x64\PCRE2\lib"
           nmake /K -f Makefile_get PCRE2INCDIR="C:\Program Files\Zabbix\x64\PCRE2\include" PCRE2LIBDIR="C:\Program Files\Zabbix\x64\PCRE2\lib"
           nmake /K -f Makefile_sender PCRE2INCDIR="C:\Program Files\Zabbix\x64\PCRE2\include" PCRE2LIBDIR="C:\Program Files\Zabbix\x64\PCRE2\lib"

Copy

✔ Copied

After compilation, Zabbix component binaries will be located in `C:\Zabbix\zabbix-7.4.0\bin\win64`. Zabbix agent configuration file is located in `C:\Zabbix\zabbix-7.4.0\conf`.

To run the agent, copy `zabbix_agent.exe` and its configuration file to a dedicated folder (e.g., `C:\Zabbix\agent`) and then run the agent:
    
    
    mkdir C:\Zabbix\agent
           copy C:\Zabbix\zabbix-7.4.0\bin\win64\zabbix_agentd.exe C:\Zabbix\agent\
           copy C:\Zabbix\zabbix-7.4.0\conf\zabbix_agentd.win.conf C:\Zabbix\agent\
           
           C:\Zabbix\agent\zabbix_agentd.exe -c C:\Zabbix\agent\zabbix_agentd.win.conf -f

Copy

✔ Copied