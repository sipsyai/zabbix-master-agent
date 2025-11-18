---
title: Building Zabbix agent on macOS
source: https://www.zabbix.com/documentation/current/en/manual/installation/install/mac_agent
downloaded: 2025-11-14 10:34:06
---

# 3 Building Zabbix agent on macOS

#### Overview

This section demonstrates how to build Zabbix macOS agent binaries from sources with or without TLS.

#### Prerequisites

You will need command line developer tools (Xcode is not required), Automake, pkg-config and PCRE (v8.x) or PCRE2 (v10.x). If you want to build agent binaries with TLS, you will also need OpenSSL or GnuTLS.

To install Automake and pkg-config, you will need a Homebrew package manager from <https://brew.sh/>. To install it, open terminal and run the following command:
    
    
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Copy

✔ Copied

Then install Automake and pkg-config:
    
    
    brew install automake
           brew install pkg-config

Copy

✔ Copied

Preparing PCRE, OpenSSL and GnuTLS libraries depends on the way how they are going to be linked to the agent.

If you intend to run agent binaries on a macOS machine that already has these libraries, you can use precompiled libraries that are provided by Homebrew. These are typically macOS machines that use Homebrew for building Zabbix agent binaries or for other purposes.

If agent binaries will be used on macOS machines that don't have the shared version of libraries, you should compile static libraries from sources and link Zabbix agent with them.

#### Building agent binaries with shared libraries

Install PCRE2 (replace _pcre2_ with _pcre_ in the commands below, if needed):
    
    
    brew install pcre2

Copy

✔ Copied

When building with TLS, install OpenSSL and/or GnuTLS:
    
    
    brew install openssl
           brew install gnutls

Copy

✔ Copied

Download Zabbix source:
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git

Copy

✔ Copied

Build agent without TLS:
    
    
    cd zabbix
           ./bootstrap.sh
           ./configure --sysconfdir=/usr/local/etc/zabbix --enable-agent --enable-ipv6
           make
           make install

Copy

✔ Copied

Build agent with OpenSSL:
    
    
    cd zabbix
           ./bootstrap.sh
           ./configure --sysconfdir=/usr/local/etc/zabbix --enable-agent --enable-ipv6 --with-openssl=/usr/local/opt/openssl
           make
           make install

Copy

✔ Copied

Build agent with GnuTLS:
    
    
    cd zabbix-source/
           ./bootstrap.sh
           ./configure --sysconfdir=/usr/local/etc/zabbix --enable-agent --enable-ipv6 --with-gnutls=/usr/local/opt/gnutls
           make
           make install

Copy

✔ Copied

#### Building agent binaries with static libraries without TLS

Let's assume that PCRE static libraries will be installed in `$HOME/static-libs`. We will use PCRE2 10.39.
    
    
    PCRE_PREFIX="$HOME/static-libs/pcre2-10.39"

Copy

✔ Copied

Download and build PCRE with Unicode properties support:
    
    
    mkdir static-libs-source
           cd static-libs-source
           curl --remote-name https://github.com/PhilipHazel/pcre2/releases/download/pcre2-10.39/pcre2-10.39.tar.gz
           tar xf pcre2-10.39.tar.gz
           cd pcre2-10.39
           ./configure --prefix="$PCRE_PREFIX" --disable-shared --enable-static --enable-unicode-properties
           make
           make check
           make install

Copy

✔ Copied

Download Zabbix source and build agent:
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git
           cd zabbix
           ./bootstrap.sh
           ./configure --sysconfdir=/usr/local/etc/zabbix --enable-agent --enable-ipv6 --with-libpcre2="$PCRE_PREFIX"
           make
           make install

Copy

✔ Copied

#### Building agent binaries with static libraries with OpenSSL

When building OpenSSL, it's recommended to run `make test` after successful building. Even if building was successful, tests sometimes fail. If this is the case, problems should be researched and resolved before continuing.

Let's assume that PCRE and OpenSSL static libraries will be installed in `$HOME/static-libs`. We will use PCRE2 10.39 and OpenSSL 1.1.1a.
    
    
    PCRE_PREFIX="$HOME/static-libs/pcre2-10.39"
           OPENSSL_PREFIX="$HOME/static-libs/openssl-1.1.1a"

Copy

✔ Copied

Let's build static libraries in `static-libs-source`:
    
    
    mkdir static-libs-source
           cd static-libs-source

Copy

✔ Copied

Download and build PCRE with Unicode properties support:
    
    
    curl --remote-name https://github.com/PhilipHazel/pcre2/releases/download/pcre2-10.39/pcre2-10.39.tar.gz
           tar xf pcre2-10.39.tar.gz
           cd pcre2-10.39
           ./configure --prefix="$PCRE_PREFIX" --disable-shared --enable-static --enable-unicode-properties
           make
           make check
           make install
           cd ..

Copy

✔ Copied

Download and build OpenSSL:
    
    
    curl --remote-name https://www.openssl.org/source/openssl-1.1.1a.tar.gz
           tar xf openssl-1.1.1a.tar.gz
           cd openssl-1.1.1a
           ./Configure --prefix="$OPENSSL_PREFIX" --openssldir="$OPENSSL_PREFIX" --api=1.1.0 no-shared no-capieng no-srp no-gost no-dgram no-dtls1-method no-dtls1_2-method darwin64-x86_64-cc
           make
           make test
           make install_sw
           cd ..

Copy

✔ Copied

Download Zabbix source and build agent:
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git
           cd zabbix
           ./bootstrap.sh
           ./configure --sysconfdir=/usr/local/etc/zabbix --enable-agent --enable-ipv6 --with-libpcre2="$PCRE_PREFIX" --with-openssl="$OPENSSL_PREFIX"
           make
           make install

Copy

✔ Copied

#### Building agent binaries with static libraries with GnuTLS

GnuTLS depends on the Nettle crypto backend and GMP arithmetic library. Instead of using full GMP library, this guide will use mini-gmp which is included in Nettle.

When building GnuTLS and Nettle, it's recommended to run `make check` after successful building. Even if building was successful, tests sometimes fail. If this is the case, problems should be researched and resolved before continuing.

Let's assume that PCRE, Nettle and GnuTLS static libraries will be installed in `$HOME/static-libs`. We will use PCRE2 10.39, Nettle 3.4.1 and GnuTLS 3.6.5.
    
    
    PCRE_PREFIX="$HOME/static-libs/pcre2-10.39"
           NETTLE_PREFIX="$HOME/static-libs/nettle-3.4.1"
           GNUTLS_PREFIX="$HOME/static-libs/gnutls-3.6.5"

Copy

✔ Copied

Let's build static libraries in `static-libs-source`:
    
    
    mkdir static-libs-source
           cd static-libs-source

Copy

✔ Copied

Download and build Nettle:
    
    
    curl --remote-name https://ftp.gnu.org/gnu/nettle/nettle-3.4.1.tar.gz
           tar xf nettle-3.4.1.tar.gz
           cd nettle-3.4.1
           ./configure --prefix="$NETTLE_PREFIX" --enable-static --disable-shared --disable-documentation --disable-assembler --enable-x86-aesni --enable-mini-gmp
           make
           make check
           make install
           cd ..

Copy

✔ Copied

Download and build GnuTLS:
    
    
    curl --remote-name https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.5.tar.xz
           tar xf gnutls-3.6.5.tar.xz
           cd gnutls-3.6.5
           PKG_CONFIG_PATH="$NETTLE_PREFIX/lib/pkgconfig" ./configure --prefix="$GNUTLS_PREFIX" --enable-static --disable-shared --disable-guile --disable-doc --disable-tools --disable-libdane --without-idn --without-p11-kit --without-tpm --with-included-libtasn1 --with-included-unistring --with-nettle-mini
           make
           make check
           make install
           cd ..

Copy

✔ Copied

Download Zabbix source and build agent:
    
    
    git clone https://git.zabbix.com/scm/zbx/zabbix.git
           cd zabbix
           ./bootstrap.sh
           CFLAGS="-Wno-unused-command-line-argument -framework Foundation -framework Security" \
           > LIBS="-lgnutls -lhogweed -lnettle" \
           > LDFLAGS="-L$GNUTLS_PREFIX/lib -L$NETTLE_PREFIX/lib" \
           > ./configure --sysconfdir=/usr/local/etc/zabbix --enable-agent --enable-ipv6 --with-libpcre2="$PCRE_PREFIX" --with-gnutls="$GNUTLS_PREFIX"
           make
           make install

Copy

✔ Copied