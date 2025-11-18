---
title: Return values for net.dns.get
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/return_values_net_dns_get
downloaded: 2025-11-14 10:47:35
---

# 17 Return values for net.dns.get

#### Overview

This section provides return value details for the [`net.dns.get`](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent/zabbix_agent2#net.dns.get) Zabbix agent 2 item.

#### Details

The output of this item is an object containing DNS record information based on the parameters provided in the item key.

For example, the `net.dns.get[,example.com]` item may return the following JSON of a refused query:
    
    
    {
               "flags": [
                   "RA"
               ],
               "query_time": "0.019030",
               "question_section": [
                   {
                       "qclass": "IN",
                       "qname": "example.com.",
                       "qtype": "SOA"
                   }
               ],
               "response_code": "REFUSED",
               "zbx_error_code": 0
           }

Copy

✔ Copied

By specifying the IP address of the DNS server, the `net.dns.get[192.0.2.0,example.com]` item may return the following JSON:
    
    
    {
               "answer_section": [
                   {
                       "class": "IN",
                       "name": "example.com.",
                       "rdata": {
                           "expire": 1209600,
                           "mbox": "noc.dns.example.org.",
                           "minttl": 3600,
                           "ns": "ns.example.org.",
                           "refresh": 7200,
                           "retry": 3600,
                           "serial": 2022091378
                       },
                       "rdlength": 44,
                       "ttl": 1205,
                       "type": "SOA"
                   }
               ],
               "flags": [
                   "RA"
               ],
               "query_time": "0.029556",
               "question_section": [
                   {
                       "qclass": "IN",
                       "qname": "example.com.",
                       "qtype": "SOA"
                   }
               ],
               "response_code": "NOERROR",
               "zbx_error_code": 0
           }

Copy

✔ Copied

If there is a connection problem, the `net.dns.get[192.0.2.0,example.com]` item may an error:
    
    
    {
               "zbx_error_code": -1,
               "zbx_error_msg": "Communication error: read udp 192.0.2.0:12345->192.0.2.0:53: i/o timeout"
           }

Copy

✔ Copied

The following types of error codes are possible:

No errors and the DNS response was received and parsed. | 0 |   
---|---|---  
DNS is down. | -1 | "Communication error"  
Error occurs during JSON parsing | -2 | "Received unexpected response"  
  
With additional parameters, the `net.dns.get[192.0.2.0,example.com,ANY,5,5,tcp,"cdflag,rdflag,dnssec,nsid,edns0,aaflag,adflag"]` item may return the following JSON:
    
    
    {
               "additional_section": [
                   {
                       "extended_rcode": 32768,
                       "name": ".",
                       "rdata": {
                           "options": [
                           {
                               "code": 0,
                               "nsid": "67 70 64 6e 73 2d 6c 70 70"
                           }
                       ]
                   },
                       "rdlength": 13,
                       "type": "OPT",
                       "udp_payload": 512
                   }
               ],
               "answer_section": [
                   {
                       "class": "IN",
                       "name": "example.com.",
                       "rdata": {
                           "a": "192.0.2.0"
                       },
                       "rdlength": 4,
                       "ttl": 19308,
                       "type": "A"
                   },
                   {
                       "class": "IN",
                       "name": "example.com.",
                       "rdata": {
                           "algorithm": 13,
                           "expiration": 1704715951,
                           "inception": 1702910624,
                           "key_tag": 21021,
                           "labels": 2,
                           "orig_ttl": 86400,
                           "signature": "HVBOBcJJQy0S08J3f8kviPj8UkEUj7wmyiMyQqPSWgQIY9SCEJ5plq6KuxJmtAek1txZWXDo+6tpIC6DIVBnuw==",
                           "signer_name": "example.com.",
                           "type_covered": "A"
                       },
                       "rdlength": 95,
                       "ttl": 19308,
                       "type": "RRSIG"
                   }
               ],
               "flags": [
                   "RD",
                   "RA",
                   "AD",
                   "CD"
               ],
               "query_time": "0.058221",
               "question_section": [
                   {
                       "qclass": "IN",
                       "qname": "example.com.",
                       "qtype": "ANY"
                   }
               ],
               "response_code": "NOERROR",
               "zbx_error_code": 0
           }

Copy

✔ Copied

#### See also

For more information about DNS records, see:

  * [Domain Names - Implementation and Specification](https://datatracker.ietf.org/doc/html/rfc1035)
  * [Domain Name System (DNS) Parameters](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)