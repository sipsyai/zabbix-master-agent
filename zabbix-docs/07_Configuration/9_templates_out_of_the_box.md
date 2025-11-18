---
title: Templates out of the box
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box
downloaded: 2025-11-14 10:36:03
---

# 9 Templates out of the box

#### Overview

Zabbix provides a growing set of pre-configured [templates](/documentation/current/en/manual/config/templates) to simplify and speed up the setup of monitoring targets.

All out-of-the-box templates are available in _Data collection_ > [_Templates_](/documentation/current/en/manual/web_interface/frontend_sections/data_collection/templates).

When upgrading Zabbix, existing templates are not updated automatically to avoid overwriting custom modifications. To upgrade existing templates or add new ones, see Template upgrade.

Please use the sidebar to access information about specific template types and operation requirements.

See also:

  * [Linking a template](/documentation/current/en/manual/config/templates/linking#linking-a-template)
  * [Known issues for templates](/documentation/current/en/manual/installation/known_issues#templates)

#### Template upgrade

To upgrade existing templates or add new ones after a Zabbix upgrade:

  1. Go to the [Zabbix Git repository](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates?at=refs%2Fheads%2Frelease%2F7.4).
  2. In the branch selector (under the _Source_ label), choose the branch that matches your Zabbix version (e.g., _release/7.4_ for Zabbix 7.4).
  3. Open the template you want to add or upgrade (e.g., [MySQL by Zabbix agent](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/mysql_agent?at=refs%2Fheads%2Frelease%2F7.4)).
  4. Copy the contents of the template file (e.g., `template_db_mysql_agent.yaml`) and save them to a local file.
  5. In Zabbix frontend, go to _Data collection_ > _Templates_ and [import](/documentation/current/en/manual/xml_export_import/templates#importing) the local file.

##### Host Wizard compatibility

To upgrade multiple templates that are compatible with the [Host Wizard](/documentation/current/en/manual/config/hosts/host_wizard), you can import the following template bundles:

  * [cloud_aws_azure.yaml](https://www.zabbix.com/documentation/7.4/assets/en/template_bundles/cloud_aws_azure.yaml)
  * [cloud_gcp_oracle.yaml](https://www.zabbix.com/documentation/7.4/assets/en/template_bundles/cloud_gcp_oracle.yaml)
  * [database.yaml](https://www.zabbix.com/documentation/7.4/assets/en/template_bundles/database.yaml)
  * [network_os.yaml](https://www.zabbix.com/documentation/7.4/assets/en/template_bundles/network_os.yaml)
  * [software.yaml](https://www.zabbix.com/documentation/7.4/assets/en/template_bundles/software.yaml)

For a full list of compatible templates, see [templates_in_bundles.md](https://www.zabbix.com/documentation/7.4/assets/en/template_bundles/templates_in_bundles.md).

To make a custom template compatible with the Host Wizard:

  1. In Zabbix frontend, go to _Data collection_ > _Templates_ and [export](/documentation/current/en/manual/xml_export_import/templates#exporting) the custom template.
  2. Edit the exported file: 
     * Add the `wizard_ready` [template element](/documentation/current/en/manual/xml_export_import/templates#templates-1) to indicate compatibility with the Host Wizard.
     * Optionally, add the `readme` or `config` [template element](/documentation/current/en/manual/xml_export_import/templates#templates-1) as needed.
  3. In Zabbix frontend, go to _Data collection_ > _Templates_ and [import](/documentation/current/en/manual/xml_export_import/templates#importing) the updated template file.