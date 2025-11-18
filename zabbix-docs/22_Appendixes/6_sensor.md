---
title: Sensor
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/sensor
downloaded: 2025-11-14 10:47:24
---

# 6 Sensor

Each sensor chip gets its own directory in the sysfs /sys/devices tree. To find all sensor chips, it is easier to follow the device symlinks from /sys/class/hwmon/hwmon*, where * is a real number (0,1,2,...).

The sensor readings are located either in /sys/class/hwmon/hwmon*/ directory for virtual devices, or in /sys/class/hwmon/hwmon*/device directory for non-virtual devices. A file, called name, located inside hwmon* or hwmon*/device directories contains the name of the chip, which corresponds to the name of the kernel driver used by the sensor chip.

There is only one sensor reading value per file. The common scheme for naming the files that contain sensor readings inside any of the directories mentioned above is: <type><number>_<item>, where

  * **type** \- for sensor chips is "in" (voltage), "temp" (temperature), "fan" (fan), etc.,
  * **item** \- "input" (measured value), "max" (high threshold), "min" (low threshold), etc.,
  * **number** \- always used for elements that can be present more than once (usually starts from 1, except for voltages which start from 0). If files do not refer to a specific element they have a simple name with no number.

The information regarding sensors available on the host can be acquired using **sensor-detect** and **sensors** tools (lm-sensors package: <http://lm-sensors.org/>). **Sensors-detect** helps to determine which modules are necessary for available sensors. When modules are loaded the **sensors** program can be used to show the readings of all sensor chips. The labeling of sensor readings, used by this program, can be different from the common naming scheme (<type><number>_<item> ):

  * if there is a file called <type><number>_label, then the label inside this file will be used instead of <type><number><item> name;
  * if there is no <type><number>_label file, then the program searches inside the /etc/sensors.conf (could be also /etc/sensors3.conf, or different) for the name substitution.

This labeling allows user to determine what kind of hardware is used. If there is neither <type><number>_label file nor label inside the configuration file the type of hardware can be determined by the name attribute (hwmon*/device/name). The actual names of sensors, which zabbix_agent accepts, can be obtained by running **sensors** program with -u parameter (**sensors -u**).

In **sensor** program the available sensors are separated by the bus type (ISA adapter, PCI adapter, SPI adapter, Virtual device, ACPI interface, HID adapter).

##### On Linux 2.4:

(Sensor readings are obtained from /proc/sys/dev/sensors directory)

  * **device** \- device name (if <mode> is used, it is a regular expression);
  * **sensor** \- sensor name (if <mode> is used, it is a regular expression);
  * **mode** \- possible values: avg, max, min (if this parameter is omitted, device and sensor are treated verbatim).

Example key: sensor[w83781d-i2c-0-2d,temp1]

##### On Linux 2.6+:

(Sensor readings are obtained from /sys/class/hwmon directory)

  * **device** \- device name (non regular expression). The device name could be the actual name of the device (e.g 0000:00:18.3) or the name acquired using sensors program (e.g. k8temp-pci-00c3). It is up to the user to choose which name to use;
  * **sensor** \- sensor name (non regular expression);
  * **mode** \- possible values: avg, max, min (if this parameter is omitted, device and sensor are treated verbatim).

Example key:

sensor[k8temp-pci-00c3,temp,max] or sensor[0000:00:18.3,temp1]

sensor[smsc47b397-isa-0880,in,avg] or sensor[smsc47b397.2176,in1]

#### Obtaining sensor names

Sensor labels, as printed by the _sensors_ command, cannot always be used directly because the naming of labels may be different for each sensor chip vendor. For example, _sensors_ output might contain the following lines:
    
    
    $ sensors
           in0:         +2.24 V  (min =  +0.00 V, max =  +3.32 V)   
           Vcore:       +1.15 V  (min =  +0.00 V, max =  +2.99 V)   
           +3.3V:       +3.30 V  (min =  +2.97 V, max =  +3.63 V)   
           +12V:       +13.00 V  (min =  +0.00 V, max = +15.94 V)
           M/B Temp:    +30.0°C  (low  = -127.0°C, high = +127.0°C)

Copy

✔ Copied

Out of these, only one label may be used directly:
    
    
    $ zabbix_get -s 127.0.0.1 -k sensor[lm85-i2c-0-2e,in0]
           2.240000

Copy

✔ Copied

Attempting to use other labels (like _Vcore_ or _+12V_) will not work.
    
    
    $ zabbix_get -s 127.0.0.1 -k sensor[lm85-i2c-0-2e,Vcore]
           ZBX_NOTSUPPORTED

Copy

✔ Copied

To find out the actual sensor name, which can be used by Zabbix to retrieve the sensor readings, run _sensors -u_. In the output, the following may be observed:
    
    
    $ sensors -u
           ...
           Vcore:
             in1_input: 1.15
             in1_min: 0.00
             in1_max: 2.99
             in1_alarm: 0.00
           ...    
           +12V:
             in4_input: 13.00
             in4_min: 0.00
             in4_max: 15.94
             in4_alarm: 0.00
           ...

Copy

✔ Copied

So _Vcore_ should be queried as _in1_ , and _+12V_ should be queried as _in4_. According to [specification](https://www.kernel.org/doc/Documentation/hwmon/sysfs-interface), these are voltages on chip pins and generally speaking may need scaling.
    
    
    $ zabbix_get -s 127.0.0.1 -k sensor[lm85-i2c-0-2e,in1]
           1.301000

Copy

✔ Copied

Not only voltage (in), but also current (curr), temperature (temp) and fan speed (fan) readings can be retrieved by Zabbix.