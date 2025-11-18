---
title: Implementation details of net.tcp.service and net.udp.service checks
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/service_check_details
downloaded: 2025-11-14 10:47:27
---

# 9 Implementation details of net.tcp.service and net.udp.service checks

Implementation of net.tcp.service and net.udp.service checks is detailed on this page for various services specified in the service parameter.

#### Item net.tcp.service parameters

**ftp**

Creates a TCP connection and expects the first 4 characters of the response to be "220 ", then sends "QUIT\r\n". Default port 21 is used if not specified.

**http**

Creates a TCP connection without expecting and sending anything. Default port 80 is used if not specified.

**https**

Uses (and only works with) libcurl, does not verify the authenticity of the certificate, does not verify the host name in the SSL certificate, only fetches the response header (HEAD request). Default port 443 is used if not specified.

**imap**

Creates a TCP connection and expects the first 4 characters of the response to be "* OK", then sends "a1 LOGOUT\r\n". Default port 143 is used if not specified.

**ldap**

Opens a connection to an LDAP server and performs an LDAP search operation with filter set to (objectClass=*). Expects successful retrieval of the first attribute of the first entry. Default port 389 is used if not specified.

**nntp**

Creates a TCP connection and expects the first 3 characters of the response to be "200" or "201", then sends "QUIT\r\n". Default port 119 is used if not specified.

**pop**

Creates a TCP connection and expects the first 3 characters of the response to be "+OK", then sends "QUIT\r\n". Default port 110 is used if not specified.

**smtp**

Creates a TCP connection and expects the first 3 characters of the response to be "220", followed by a space, the line ending or a dash. The lines containing a dash belong to a multiline response and the response will be re-read until a line without the dash is received. Then sends "QUIT\r\n". Default port 25 is used if not specified.

**ssh**

Creates a TCP connection. If the connection has been established, both sides exchange an identification string (SSH-major.minor-XXXX), where major and minor are protocol versions and XXXX is a string. Zabbix checks if the string matching the specification is found and then sends back the string "SSH-major.minor-zabbix_agent\r\n" or "0\n" on mismatch. Default port 22 is used if not specified.

**tcp**

Creates a TCP connection without expecting and sending anything. Unlike the other checks requires the port parameter to be specified.

**telnet**

Creates a TCP connection and expects a login prompt (':' at the end). Default port 23 is used if not specified.

#### Item net.udp.service parameters

**ntp**

Sends an SNTP packet over UDP and validates the response according to [RFC 4330, section 5](http://tools.ietf.org/html/rfc4330#section-5). Default port 123 is used if not specified.