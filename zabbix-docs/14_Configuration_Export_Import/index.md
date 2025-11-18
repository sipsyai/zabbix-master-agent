---
title: Configuration export/import
source: https://www.zabbix.com/documentation/current/en/manual/xml_export_import
downloaded: 2025-11-14 10:37:07
---

# 14 Configuration export/import

#### Overview

Zabbix export/import functionality makes it possible to exchange various configuration entities between one Zabbix system and another.

Typical use cases for this functionality:

  * share templates or network maps - Zabbix users may share their configuration parameters
  * upload a template to [Zabbix Community templates](https://github.com/zabbix/community-templates). Then others can download the template and import the file into Zabbix.
  * integrate with third-party tools - universal YAML, XML and JSON formats make integration and data import/export possible with third-party tools and applications

##### What can be exported/imported

Objects that can be exported/imported are:

  * [Host groups](/documentation/current/en/manual/xml_export_import/hostgroups) (_through Zabbix API only_)
  * [Template groups](/documentation/current/en/manual/xml_export_import/templategroups) (_through Zabbix API only_)
  * [Templates](/documentation/current/en/manual/xml_export_import/templates)
  * [Hosts](/documentation/current/en/manual/xml_export_import/hosts)
  * [Network maps](/documentation/current/en/manual/xml_export_import/maps)
  * [Media types](/documentation/current/en/manual/xml_export_import/media)
  * Images

##### Export format

Data can be exported using the Zabbix web frontend or [Zabbix API](/documentation/current/en/manual/api/reference/configuration). Supported export formats are YAML, XML and JSON.

#### Details about export

  * All supported elements are exported in one file.
  * Host and template entities (items, triggers, graphs, discovery rules) that are inherited from linked templates are not exported. Any changes made to those entities on a host level (such as changed item interval, modified regular expression or added prototypes to the low-level discovery rule) will be lost when exporting; when importing, all entities from linked templates are re-created as on the original linked template.
  * Entities created by low-level discovery and any entities depending on them are not exported. For example, a trigger created for an LLD-rule generated item will not be exported.
  * When the exported host/template contains entities supporting timeouts, the timeout values will be exported if these entities have their own timeouts configured.

#### Details about import

  * Import stops at the first error.
  * When updating existing images during image import, "imagetype" field is ignored, i.e., it is impossible to change image type via import.
  * When importing hosts/templates using the "Delete missing" option, host/template macros not present in the import file will be deleted from  
the host/template after the import.
  * Empty tags for items, triggers, graphs, discoveryRules, itemPrototypes, triggerPrototypes, graphPrototypes are meaningless, i.e., it's the same as if it was missing.
  * If entities of the imported host/template have their own timeouts configured, they will be applied; otherwise, proxy/global timeouts will be applied.
  * Import supports YAML, XML and JSON, the import file must have a correct file extension: .yaml and .yml for YAML, .xml for XML and .json for JSON. See [compatibility information](/documentation/current/en/manual/appendix/compatibility) about supported XML versions.
  * Import supports configuration files only in UTF-8 encoding (with or without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark)); other encodings (UTF16LE, UTF16BE, UTF32LE, UTF32BE, etc.) will result in an import conversion error.

#### YAML base format

The YAML export format contains the following nodes:

  * Root node for Zabbix YAML export
  * Export version

    
    
    zabbix_export:
             version: '7.4'

Copy

✔ Copied

Other nodes are dependent on exported objects.

#### XML format

The XML export format contains the following tags:

  * Default header for XML documents
  * Root tag for Zabbix XML export
  * Export version

    
    
    <?xml version="1.0" encoding="UTF-8"?>
           <zabbix_export>
               <version>7.4</version>
           </zabbix_export>

Copy

✔ Copied

Other tags are dependent on exported objects.

#### JSON format

The JSON export format contains the following objects:

  * Root object for Zabbix JSON export
  * Export version

    
    
    {
               "zabbix_export": {
                   "version": "7.4"
               }
           }

Copy

✔ Copied

Other objects are dependent on exported objects.