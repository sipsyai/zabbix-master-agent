---
title: template.delete
source: https://www.zabbix.com/documentation/current/en/manual/api/reference/template/delete
downloaded: 2025-11-14 10:44:44
---

# template.delete

### Description

`object template.delete(array templateIds)`

This method allows to delete templates.

Deleting a template will cause deletion of all template entities (items, triggers, graphs, etc.). To leave template entities with the hosts, but delete the template itself, first unlink the template from required hosts using one of these methods: [template.update](/documentation/current/en/manual/api/reference/template/update), [template.massupdate](/documentation/current/en/manual/api/reference/template/massupdate), [host.update](/documentation/current/en/manual/api/reference/host/update), [host.massupdate](/documentation/current/en/manual/api/reference/host/massupdate).

This method is only available to _Admin_ and _Super admin_ user types. Permissions to call the method can be revoked in user role settings. See [User roles](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) for more information.

### Parameters

`(array)` IDs of the templates to delete.

### Return values

`(object)` Returns an object containing the IDs of the deleted templates under the `templateids` property.

### Examples

#### Deleting multiple templates

Delete two templates.

[Request](/documentation/current/en/manual/api#performing-requests):
    
    
    {
               "jsonrpc": "2.0",
               "method": "template.delete",
               "params": [
                   "13",
                   "32"
               ],
               "id": 1
           }

Copy

✔ Copied

Response:
    
    
    {
               "jsonrpc": "2.0",
               "result": {
                   "templateids": [
                       "13",
                       "32"
                   ]
               },
               "id": 1
           }

Copy

✔ Copied

### Source

CTemplate::delete() in _ui/include/classes/api/services/CTemplate.php_.