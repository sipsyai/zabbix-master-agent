---
title: modbus.get parameters
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/modbus
downloaded: 2025-11-14 10:47:32
---

# 14 modbus.get parameters

#### Overview

The table below presents details of the `modbus.get` [item](/documentation/current/en/manual/config/items/itemtypes/zabbix_agent#modbus) parameters.

#### Parameters

_endpoint_ | Protocol and address of the endpoint, defined as `protocol://connection_string`  
  
Possible protocol values: _rtu_ , _ascii_ (Agent 2 only), _tcp_  
  
Connection string format:  
  
with _tcp_ \- `address:port`  
with serial line: _rtu_ , _ascii_ \- `port_name:speed:params`  
where  
'speed' - 1200, 9600 etc  
'params' - data bits (5,6,7 or 8), parity (n,e or o for none/even/odd), stop bits (1 or 2) | protocol: none  
  
 _rtu/ascii_ protocol:  
port_name: none  
speed: 115200  
params: 8n1  
  
 _tcp_ protocol:  
address: none  
port: 502 | tcp://192.168.6.1:511  
tcp://192.168.6.2  
tcp://[::1]:511  
tcp://::1  
tcp://localhost:511  
tcp://localhost  
rtu://COM1:9600:8n  
ascii://COM2:1200:7o2  
rtu://ttyS0:9600  
ascii://ttyS1  
---|---|---|---  
_slave id_ | Modbus address of the device it is intended for (1 to 247), see [MODBUS Messaging Implementation Guide](https://modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf) (page 23)  
  
tcp device (not GW) will ignore the field | serial: 1  
  
tcp: 255 (0xFF) | 2  
_function_ | Empty or value of a supported function:  
  
1 - Read Coil,  
2 - Read Discrete Input,  
3 - Read Holding Registers,  
4 - Read Input Registers | empty | 3  
_address_ | Address of the first registry, coil or input.  
  
If 'function' is empty, then 'address' should be in range for:  
Coil - 00001 - 09999  
Discrete input - 10001 - 19999  
Input register - 30001 - 39999  
Holding register - 40001 - 49999  
  
If 'function' is not empty, the 'address' field will be from 0 till 65535 and used without modification (PDU) | empty function: 00001  
  
non-empty function: 0 | 9999  
_count_ | Count of sequenced 'type' which will be read from device, where:  
  
for Coil or Discrete input the 'type' = 1 bit  
for other cases: (count*sizeof(type))/2 = real count of registers for reading  
If 'offset' is not 0, the value will be added to 'real count'  
Acceptable range for 'real count' is 1:65535 | 1 | 2  
_type_ | Data type:  
  
for Read Coil and Read Discrete Input - _bit_  
  
for Read Holding Registers and Read Input Registers:  
_int8_ \- 8bit  
 _uint8_ \- 8bit (unsigned)  
_int16_ \- 16bit  
 _uint16_ \- 16bit (unsigned)  
_int32_ \- 32bit  
 _uint32_ \- 32bit (unsigned)  
_float_ \- 32bit  
 _uint64_ \- 64bit (unsigned)  
_double_ \- 64bit | bit  
uint16 | uint64  
_endianness_ | Endianness type:  
_be_ \- Big Endian  
 _le_ \- Little Endian  
 _mbe_ \- Mid-Big Endian  
 _mle_ \- Mid-Little Endian  
  
Limitations:  
for 1 bit - be  
for 8 bits - be,le  
for 16 bits - be,le | be | le  
_offset_ | Number of registers, starting from 'address', the result of which will be discarded.  
  
The size of each register is 16bit (needed to support equipment that does not support random read access). | 0 | 4