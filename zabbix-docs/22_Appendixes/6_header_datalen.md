---
title: Header
source: https://www.zabbix.com/documentation/current/en/manual/appendix/protocols/header_datalen
downloaded: 2025-11-14 10:47:16
---

#### Overview

The header is present in all request and response messages between Zabbix components. It is required to determine the message length, if it is compressed or not, if it is a large packet or not.

Zabbix communications protocol has 1GB packet size limit per connection. The limit of 1GB is applied to both the received packet data length and the uncompressed data length.

When sending configuration to Zabbix proxy, the packet size limit is increased to 4GB to allow syncing large configurations. When data length before compression exceeds 4GB, Zabbix server automatically starts using the large packet format (0x04 flag) which increases the packet size limit to 16GB.

Note that while a large packet format can be used for sending any data, currently only the Zabbix proxy configuration syncer can handle packets that are larger than 1GB.

#### Structure

The header consists of four fields. All numbers in the header are formatted as little-endian.

`<PROTOCOL>` | 4 | 4 | `"ZBXD"` or `5A 42 58 44`  
---|---|---|---  
`<FLAGS>` | 1 | 1 | Protocol flags:  
`0x01` \- Zabbix communications protocol  
`0x02` \- compression  
`0x04` \- large packet  
`<DATALEN>` | 4 | 8 | Data length.  
`<RESERVED>` | 4 | 8 | When compression is used (`0x02` flag) - the length of uncompressed data  
When compression is not used - `00 00 00 00`  
  
#### Examples

Here are some code snippets showing how to add Zabbix protocol header to the data you want to send in order to obtain the packet you should send to Zabbix so that it is interpreted correctly. These code snippets assume that the data is not larger than 1GB, thus the large packet format is not used.

##### Python
    
    
    packet = b"ZBXD\1" + struct.pack("<II", len(data), 0) + data

Copy

✔ Copied

or
    
    
    def zbx_create_header(plain_data_size, compressed_data_size=None):
               protocol = b"ZBXD"
               flags = 0x01
               if compressed_data_size is None:
                   datalen = plain_data_size
                   reserved = 0
               else:
                   flags |= 0x02
                   datalen = compressed_data_size
                   reserved = plain_data_size
               return protocol + struct.pack("<BII", flags, datalen, reserved)
           
           packet = zbx_create_header(len(data)) + data

Copy

✔ Copied

##### Perl
    
    
    my $packet = "ZBXD\1" . pack("(II)<", length($data), 0) . $data;

Copy

✔ Copied

or
    
    
    sub zbx_create_header($;$)
           {
               my $plain_data_size = shift;
               my $compressed_data_size = shift;
           
               my $protocol = "ZBXD";
               my $flags = 0x01;
               my $datalen;
               my $reserved;
           
               if (!defined($compressed_data_size))
               {
                   $datalen = $plain_data_size;
                   $reserved = 0;
               }
               else
               {
                   $flags |= 0x02;
                   $datalen = $compressed_data_size;
                   $reserved = $plain_data_size;
               }
           
               return $protocol . chr($flags) . pack("(II)<", $datalen, $reserved);
           }
           
           my $packet = zbx_create_header(length($data)) . $data;

Copy

✔ Copied

##### PHP
    
    
    $packet = "ZBXD\1" . pack("VV", strlen($data), 0) . $data;

Copy

✔ Copied

or
    
    
    function zbx_create_header($plain_data_size, $compressed_data_size = null)
           {
               $protocol = "ZBXD";
               $flags = 0x01;
               if (is_null($compressed_data_size))
               {
                   $datalen = $plain_data_size;
                   $reserved = 0;
               }
               else
               {
                   $flags |= 0x02;
                   $datalen = $compressed_data_size;
                   $reserved = $plain_data_size;
               }
               return $protocol . chr($flags) . pack("VV", $datalen, $reserved);
           }
           
           $packet = zbx_create_header(strlen($data)) . $data;

Copy

✔ Copied

##### Bash
    
    
    datalen=$(printf "%08x" ${#data})
           datalen="\\x${datalen:6:2}\\x${datalen:4:2}\\x${datalen:2:2}\\x${datalen:0:2}"
           printf "ZBXD\1${datalen}\0\0\0\0%s" "$data"

Copy

✔ Copied