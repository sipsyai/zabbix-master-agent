---
title: Scheduled reports
source: https://www.zabbix.com/documentation/current/en/manual/config/reports
downloaded: 2025-11-14 10:36:42
---

# 14 Scheduled reports

#### Overview

With the _Scheduled reports_ feature, you can set up a PDF version of a given dashboard to be sent to specified recipients at recurring intervals.

![](/documentation/current//assets/en/manual/web_interface/scheduled_report_pdf_example.png)

Pre-requisites:

  * Zabbix web service must be installed and configured correctly to enable scheduled report generation - see [Setting up scheduled reports](/documentation/current/en/manual/appendix/install/web_service) for instructions.
  * A user must have a [user role](/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles) of type _Admin_ or _Super admin_ with the following permissions: 
    * _Scheduled reports_ in the _Access to UI elements_ block (to view report settings)
    * _Manage scheduled reports_ in the _Access to actions_ block (to create/edit reports)

To create a scheduled report in Zabbix frontend, do the following:

  * Go to: _Reports_ > _Scheduled reports_.
  * Click _Create report_ in the upper-right corner of the screen.
  * Enter parameters of the report in the form.

You can also create a report by opening an existing one, clicking the _Clone_ button, and then saving it under a different name.

#### Configuration

The _Scheduled reports_ tab contains general report attributes.

![](/documentation/current/assets/en/manual/web_interface/scheduled_report.png)

All mandatory input fields are marked with a red asterisk.

_Owner_ | User that creates a report. _Super admin_ level users are allowed to change the owner. For _Admin_ level users, this field is read-only.  
---|---  
_Name_ | Name of the report; must be unique.  
_Dashboard_ | Dashboard on which the report is based; only one dashboard can be selected at a time. To select a dashboard, start typing the name - a list of matching dashboards will appear; scroll down to select. Alternatively, you may click _Select_ next to the field and select a dashboard from the displayed list.  
_Period_ | Period for which the report will be prepared. Select the previous day, week, month, or year.  
_Cycle_ | Report generation frequency. The reports can be sent daily, weekly, monthly, or yearly. "Weekly" mode allows to select days of the week when the report will be sent.  
_Start time_ | Time of the day in the format hh:mm when the report will be prepared. Note that Zabbix server time zone will be used.  
_Repeat on_ | Days of the week when the report will be sent. This field is available only if _Cycle_ is set to "Weekly".  
_Start date_ | Date when regular report generation should be started.  
_End date_ | Date when regular report generation should be stopped.  
_Subject_ | Subject of the report email. Supported macros: {TIME}, {TIMESTAMP}.  
_Message_ | Body of the report email. Supported macros: {TIME}, {TIMESTAMP}.  
_Subscriptions_ | List of report recipients. By default, includes only the report owner. Any Zabbix user with configured email media may be specified as a report recipient.  
Click _Add user_ or _Add user group_ to add more recipients.  
Click the username to edit settings:  
_Generate report by_ \- whether the report data should be generated based on the dashboard permissions of the current user or the recipient.  
_Status_ \- select "Include" to send the report to the user or "Exclude" to prevent sending the report to this user. At least one user must have the "Include" status. The "Exclude" status can be used to exclude specific users from a user group that is included.  
  
Note that users with insufficient permissions (that is, users with a role based on the _Admin_ user type who are not members of the same user group as the recipient or report owner) will see "Inaccessible user" or "Inaccessible user group" instead of the actual names in the fields _Recipient_ and _Generate report by_ ; the fields _Status_ and _Action_ will be displayed as read-only.  
_Enabled_ | Report status. Clearing this checkbox will disable the report.  
_Description_ | An optional description of the report. This description is for internal use and will not be sent to report recipients.  
  
##### Form buttons

Buttons at the bottom of the form allow to perform several operations.

![](/documentation/current/assets/en/manual/config/button_add.png) | Add a report. This button is only available for new reports.  
---|---  
![](/documentation/current/assets/en/manual/config/button_update.png) | Update the properties of a report.  
![](/documentation/current/assets/en/manual/config/button_clone.png) | Create another report based on the properties of the current report.  
![](/documentation/current/assets/en/manual/config/button_test.png) | Test if report configuration is correct by sending a report to the current user.  
![](/documentation/current/assets/en/manual/config/button_delete.png) | Delete the report.  
![](/documentation/current/assets/en/manual/config/button_cancel.png) | Cancel the editing of report properties.  
  
##### Testing

To test a report, click the _Test_ button at the bottom of the report configuration form.

The _Test_ button is not available if the report configuration form has been opened from the dashboard [action menu](/documentation/current/en/manual/web_interface/frontend_sections/dashboards#viewing-and-editing-a-dashboard).

If the configuration is correct, the test report is sent immediately to the current user. For test reports, subscribers and _Generate report by_ user settings are ignored.

If the configuration is incorrect, an error message is displayed describing the possible cause.

![](/documentation/current/assets/en/manual/web_interface/report_test_error.png)

##### Updating a report

To update an existing report, click the report name, make the required configuration changes, and then click the _Update_ button.

If an existing report is updated by another user and this user changes the Dashboard, upon clicking the _Update_ button, a warning message "Report generated by other users will be changed to the current user" will be displayed.

![](/documentation/current/assets/en/manual/web_interface/report_update.png)

Clicking _OK_ at this step will lead to the following changes:

  * _Generate report by_ settings will be updated to display the user who edited the report last (unless _Generate report by_ is set to the recipient).
  * Users that have been displayed as "Inaccessible user" or "Inaccessible user group" will be deleted from the list of report subscribers.

Clicking _Cancel_ will close the configuration form and cancel the report update.

##### Cloning a report

To quickly clone an existing report, click the _Clone_ button at the bottom of an existing report configuration form. When cloning a report created by another user, the current user becomes the owner of the new report.

Report settings will be copied to the new report configuration form with respect to user permissions:

  * If the user who clones a report has no permissions to a dashboard, the _Dashboard_ field will be cleared.
  * If the user who clones a report has no permissions to some users or user groups in the _Subscriptions_ list, inaccessible recipients will not be cloned.
  * _Generate report by_ settings will be updated to display the current user (unless _Generate report by_ is set to the recipient).

Change the required settings and the report name, then click _Add_.