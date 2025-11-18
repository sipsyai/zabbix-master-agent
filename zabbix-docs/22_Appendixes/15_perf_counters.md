---
title: Creating custom performance counter names for VMware
source: https://www.zabbix.com/documentation/current/en/manual/appendix/items/perf_counters
downloaded: 2025-11-14 10:47:33
---

# 15 Creating custom performance counter names for VMware  
  
### Overview

The VMware performance counter path has the `group/counter[rollup]` format where:

  * `group` \- the performance counter group, for example _cpu_
  * `counter` \- the performance counter name, for example _usagemhz_
  * `rollup` \- the performance counter rollup type, for example _average_

So the above example would give the following counter path: `cpu/usagemhz[average]`

The performance counter group descriptions, counter names and rollup types can be found in [VMware documentation](https://developer.broadcom.com/xapis/vsphere-web-services-api/latest/).

It is possible to obtain internal names and create custom performance counter names by using script item in Zabbix.

### Configuration

  1. Create disabled Script item on the main VMware host (where the **eventlog[]** item is present) with the following parameters:

![](/documentation/current/assets/en/manual/appendix/items/perf_counter_item.png)

  * _Name_ : VMware metrics
  * _Type_ : Script
  * _Key_ : vmware.metrics
  * _Type of information_ : Text
  * _Script_ : copy and paste the script provided below
  * _Timeout_ : 10
  * _History_ : Do not store
  * _Enabled_ : unmarked

#### Script
    
    
    try {
               Zabbix.log(4, 'vmware metrics script');
           
               var result, resp,
               req = new HttpRequest();
               req.addHeader('Content-Type: application/xml');
               req.addHeader('SOAPAction: "urn:vim25/6.0"');
           
               login = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:vim25">\
               <soapenv:Header/>\
               <soapenv:Body>\
                   <urn:Login>\
                       <urn:_this type="SessionManager">SessionManager</urn:_this>\
                       <urn:userName>{$VMWARE.USERNAME}</urn:userName>\
                       <urn:password>{$VMWARE.PASSWORD}</urn:password>\
                   </urn:Login>\
               </soapenv:Body>\
           </soapenv:Envelope>'
               resp = req.post("{$VMWARE.URL}", login);
               if (req.getStatus() != 200) {
                   throw 'Response code: '+req.getStatus();
               }
           
               query = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:vim25">\
           <soapenv:Header/>\
               <soapenv:Body>\
                   <urn:RetrieveProperties>\
                       <urn:_this type="PropertyCollector">propertyCollector</urn:_this>\
                       <urn:specSet>\
                           <urn:propSet>\
                              <urn:type>PerformanceManager</urn:type>\
                              <urn:pathSet>perfCounter</urn:pathSet>\
                           </urn:propSet>\
                           <urn:objectSet>\
                              <urn:obj type="PerformanceManager">PerfMgr</urn:obj>\
                           </urn:objectSet>\
                       </urn:specSet>\
                   </urn:RetrieveProperties>\
               </soapenv:Body>\
           </soapenv:Envelope>'
               resp = req.post("{$VMWARE.URL}", query);
               if (req.getStatus() != 200) {
                   throw 'Response code: '+req.getStatus();
               }
               Zabbix.log(4, 'vmware metrics=' + resp);
               result = resp;
           
               logout = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:vim25">\
               <soapenv:Header/>\
               <soapenv:Body>\
                   <urn:Logout>\
                       <urn:_this type="SessionManager">SessionManager</urn:_this>\
                   </urn:Logout>\
               </soapenv:Body>\
           </soapenv:Envelope>'
           
               resp = req.post("{$VMWARE.URL}",logout);         
               if (req.getStatus() != 200) {
                   throw 'Response code: '+req.getStatus();
               }
           
           } catch (error) {
               Zabbix.log(4, 'vmware call failed : '+error);
               result = {};
           }
           
           return result;

Copy

✔ Copied

Once the item is configured, press _Test_ button, then press _Get value_.

![](/documentation/current/assets/en/manual/appendix/items/perf_counter_item1.png)

Copy received XML to any XML formatter and find the desired metric.

An example of XML for one metric:
    
    
    <PerfCounterInfo xsi:type="PerfCounterInfo">
               <key>6</key>
               <nameInfo>
                   <label>Usage in MHz</label>
                   <summary>CPU usage in megahertz during the interval</summary>
                   <key>usagemhz</key>
               </nameInfo>
               <groupInfo>
                   <label>CPU</label>
                   <summary>CPU</summary>
                   <key>cpu</key>
               </groupInfo>
               <unitInfo>
                   <label>MHz</label>
                   <summary>Megahertz</summary>
                   <key>megaHertz</key>
               </unitInfo>
               <rollupType>average</rollupType>
               <statsType>rate</statsType>
               <level>1</level>
               <perDeviceLevel>3</perDeviceLevel>
           </PerfCounterInfo>

Copy

✔ Copied

Use XPath to extract the counter path from received XML. For the example above, the XPath will be:

group | //groupInfo[../key=6]/key | cpu  
---|---|---  
counter | //nameInfo[../key=6]/key | usagemhz  
rollup | //rollupType[../key=6] | average  
  
Resulting performance counter path in this case is: `cpu/usagemhz[average]`