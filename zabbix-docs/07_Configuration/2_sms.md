---
title: SMS
source: https://www.zabbix.com/documentation/current/en/manual/config/notifications/media/sms
downloaded: 2025-11-14 10:36:13
---

# 2 SMS

#### Overview

Zabbix supports the sending of SMS messages using a serial GSM modem connected to Zabbix server's serial port.

Make sure that:

  * The speed of the serial device (normally /dev/ttyS0 under Linux) matches that of the GSM modem. Zabbix does not set the speed of the serial link. It uses default settings.
  * The 'zabbix' user has read/write access to the serial device. Run the command ls –l /dev/ttyS0 to see current permissions of the serial device.
  * The GSM modem has PIN entered and it preserves it after power reset. Alternatively you may disable PIN on the SIM card. PIN can be entered by issuing command AT+CPIN="NNNN" (NNNN is your PIN number, the quotes must be present) in a terminal software, such as Unix minicom or Windows HyperTerminal.

Zabbix has been tested with these GSM modems:

  * Siemens MC35
  * Teltonika ModemCOM/G10

To configure SMS as the delivery channel for messages, you also need to configure SMS as the media type and enter the respective phone numbers for the users.

#### Configuration

To configure SMS as the media type:

  * Go to _Alerts → Media types_
  * Click on _Create media type_ (or click on _SMS_ in the list of pre-defined media types).

The following parameters are specific for the SMS media type:

_GSM modem_ | Set the serial device name of the GSM modem.  
The path entered here will be validated against the [SMSDevices](/documentation/current/en/manual/appendix/config/zabbix_server#smsdevices) server parameter (if specified).  
---|---  
  
See [common media type parameters](/documentation/current/en/manual/config/notifications/media#common-parameters) for details on how to configure default messages and alert processing options. Note that parallel processing of sending SMS notifications is not possible.

#### User media

Once the SMS media type is configured, go to the _Users → Users_ section and edit user profile to assign SMS media to the user. Steps for setting up user media, being common for all media types, are described on the [Media types](/documentation/current/en/manual/config/notifications/media#user-media) page.