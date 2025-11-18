---
title: Inclusion
source: https://www.zabbix.com/documentation/current/en/manual/appendix/config/special_notes_include
downloaded: 2025-11-14 10:47:09
---

# 11 Inclusion

#### Overview

Additional files or directories can be included into server/proxy/agent configuration using the `Include` parameter.

#### Notes on inclusion

If the `Include` parameter is used for including a file, the file must be readable.

If the `Include` parameter is used for including a directory:

  * All files in the directory must be readable.
  * No particular order of inclusion should be assumed (e.g. files are not included in alphabetical order). Therefore do not define one parameter in several ''Include'' files (e.g. to override a general setting with a specific one).
  * All files in the directory are included into configuration.
  * Beware of file backup copies automatically created by some text editors. For example, if editing the ''include/my_specific.conf'' file produces a backup copy ''include/my_specific_conf.BAK'' then both files will be included. Move ''include/my_specific.conf.BAK'' out of the "Include" directory. On Linux, contents of the ''Include'' directory can be checked with a ''ls -al'' command for unnecessary files.

If the `Include` parameter is used for including files using a pattern:

  * All files matching the pattern must be readable.
  * No particular order of inclusion should be assumed (e.g. files are not included in alphabetical order). Therefore do not define one parameter in several ''Include'' files (e.g. to override a general setting with a specific one).