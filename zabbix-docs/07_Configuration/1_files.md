---
title: Export to files
source: https://www.zabbix.com/documentation/current/en/manual/config/export/files
downloaded: 2025-11-14 10:36:44
---

# 1 Export to files

#### Overview

It is possible to configure real-time exporting of trigger events, item values and trends in a newline-delimited JSON format.

Exporting is done into files, where each line of the export file is a JSON object. Value mappings are not applied.

In case of errors (data cannot be written to the export file or the export file cannot be renamed or a new one cannot be created after renaming it), the data item is dropped and never written to the export file. It is written only in the Zabbix database. Writing data to the export file is resumed when the writing problem is resolved.

For precise details on what information is exported, see the [export protocol](/documentation/current/en/manual/appendix/protocols/real_time_export) page.

Note that host/item can have no metadata (host groups, host name, item name) if the host/item was removed after the data was received, but before server exported data.

#### Configuration

Real-time export of trigger events, item values and trends is configured by specifying a directory for the export files - see the [ExportDir](/documentation/current/en/manual/appendix/config/zabbix_server#exportdir) parameter in server configuration.

Two other parameters are available:

  * `ExportFileSize` may be used to set the maximum allowed size of an individual export file. When a process needs to write to a file it checks the size of the file first. If it exceeds the configured size limit, the file is renamed by appending .old to its name and a new file with the original name is created.

A file will be created per each process that will write data (i.e. approximately 4-30 files). As the default size per export file is 1G, keeping large export files may drain the disk space fast.

  * `ExportType` allows to specify which entity types (events, history, trends) will be exported.