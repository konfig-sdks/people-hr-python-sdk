<div align="left">

[![Visit Peoplehr](./header.png)](https://peoplehr.com)

# Peoplehr<a id="peoplehr"></a>

# Introduction<a id="introduction"></a>
 We think it's good to share. So we've created an open API to help you easily integrate People with other systems and applications, for seamless cross-platform data sharing.

 The People API accepts and returns JSON data in the request body, with status indicating the outcome of the operation (sucess/failure).

# Developer Workbench<a id="developer-workbench"></a>
 As well as this really useful documentation, we've also provided you with a handy API developer workbench. This allows you test your API calls against either a sandbox, or a live instance. A great place to start is the General Overview video, which explains how to use the workbench: https://intercom.help/peoplea-apps/api-and-integration/api

You can access the developer work bench here: https://api.peoplehr.net/pages/functional 

# Sandbox<a id="sandbox"></a>
If you need a sandbox account to test your creation, just email customerservices@peoplehr.com and we will help you set one up. 

# Authentication<a id="authentication"></a>
The People API uses API keys for each call. To receive an API key, ask your system administrator to generate one from within Settings. For authentication, all API calls need the API key to be passed along with the JSON data sent as part of the http request. Never share your API keys. Keep them guarded and secure. 

# Managed Lists<a id="managed-lists"></a>
 Within People, there are a number of fields called Managed Lists, better known as dropdowns. When you insert an item of data into a field that is a Managed List, then the API will automatically create you an entry in the Managed List for that field.

# Rate Limit Detail<a id="rate-limit-detail"></a>
 The API rate limit is set to 30 calls a minute from a specific IP address. If you attempt to call the API above the rate limit, then an exception message will be returned. If you would like your rate limit increased, please submit a request to customerservices@peoplehr.com. In your email, please explain why you would like your limit increasing.


# Webhooks Detail<a id="webhooks-detail"></a>
 People provides an option to use webhooks to receive notifications of changes in particular transactions. If you are going to use the webhook mechanism, we advise you to set up a generic listener service to receive callbacks. 
 To set up a webhook listener URL, select Settings, API, and then enter your listner URL into the field.  

The following actions are available and the data packet will return the following (example data shown): 

 New Starter Added > ActionId:1, Action:New Starter Added, EmployeeId:PW21 

 Employee personal detail update > ActionId:2, Action:Employee Detail Updated, EmployeeId:PW1, FieldName:Other Name(s), NewValue:Am, OldValue:zz, Reason:Test 

 Leaver > ActionId:3, Action:Marked Leaver, EmployeeId:PW21 

 Holiday added > ActionId:4, Action:Holiday Added, EmployeeId:PW13, HolidayType:A day or more, StartDate:2016-06-13, EndDate:2016-06-15, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.50, Comments:part day testing, IsToilHoliday:No 

 Holiday Updated > ActionId:5, Action:Holiday Updated, EmployeeId:PW51, HolidayType:A day or more, OriginalStartDate:2016-05-04, OriginalEndDate:2016-05-04, OriginalPartOfDay:, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-05-04, EndDate:2016-05-05, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1.50, Comments:Test, IsToilHoliday:No 

 Holiday Deleted > ActionId:6, Action:Holiday Deleted, EmployeeId:PW13, StartDate:2016-01-18, EndDate:2016-01-19, HolidayRecordedIn:Days, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.00, Comments:zz 

 Holiday Requested > ActionId:7, Action:New Holiday Request, EmployeeId:PW97, HolidayType:A day or more, StartDate:2017-06-22, EndDate:2017-06-23, HolidayRecordedIn:Days, PartOfDay: StartDatePartOfTheDay:, EndDatePartOfTheDay:, Duration:2.00, Comments:Graduation, IsToilHoliday:No 

 Holiday Approved > ActionId:8, Action:Holiday Approved, EmployeeId:PW391, StartDate:2017-06-15, EndDate:2017-06-15, HolidayRecordedIn:Days, Duration:0.5, Comments:, AuthorisedByFirstName:Richard, AuthorisedByLastName:Palmer, HolidayType:Less than a day, PartOfDay:AM, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No 

 Holiday Rejected > ActionId:9, Action:Holiday Rejected, EmployeeId:PW29, StartDate:2017-07-12, EndDate:2017-07-12, HolidayRecordedIn:Days, Duration:1, Comments:Unfortunately this is, fully booked, AuthorisedByFirstName:Debi, AuthorisedByLastName:Stokes, HolidayType:A day or more, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No 

 Sick Added > ActionId:10, Action:Sick Added, EmployeeId:PW13, Reason:Accident, StartDate:2016-01-19, EndDate:2016-01-19, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments: 

 Sick Updated > ActionId:11, Action:Sick Updated, EmployeeId:PW13, Reason:Accident, OriginalStartDate:2016-01-18, OriginalEndDate:2016-01-19, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-01-18, EndDate:2016-01-19, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1, Comments: 

 Sick Deleted > ActionId:12, Action:Sick Deleted, EmployeeId:PW13, Reason:Cold/Flu, StartDate:2016-01-21, EndDate:2016-01-21, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments: 

 Maternity / Paternity Added > ActionId:13, Action:Maternity/Paternity Added, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-24 

 Maternity / Paternity Updated > ActionId:14, Action:Maternity/Paternity Updated, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25 

 Maternity / Paternity Deleted > ActionId:15, Action:Maternity/Paternity Deleted, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25 

 Late Added > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:10, Comments: 

 Late Updated > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments: 

 Late Deleted > ActionId:17, Action:Late Deleted, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments: 

 Employee Deleted > ActionId:18, Action:Employee Deleted, EmployeeId:PW21 

 Other Event Updated > ActionId:21, Action:Other Event Updated, EmployeeId:PW5-2, OriginalStartDate:2016-06-25, OriginalEndDate:2016-06-25, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Days, OriginalDurationType:Days, OriginalDuration:1.00, OriginalStartTime:, OriginalEndTime: 

 Other Event Deleted > ActionId:22, Action:Other Event Deleted, EmployeeId:PW5-2, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Day, StartTime:, EndTime: 

 Other Event Requested > ActionId:23, Action:New Other Event Request, EmployeeId:S20, Reason:Flexi, StartDate:2017-06-16, StartTime:09:00:00, EndTime:12:30:00, Duration:210, Comments:, DurationType:Hours 

 Other Event Approved > ActionId:24, Action:Other Event Approved, EmployeeId:180, StartDate:2017-06-14, EndDate:2017-06-14, Comments:, AuthorisedByFirstName:Damith, Duration:2 Hrs 0 Mins (02:00 - 04:00), Reason:Short Leave 

 Other Event Rejected > ActionId:25, Action:Other Event Rejected, EmployeeId:312, StartDate:2017-09-13, EndDate:2017-09-13, Comments:already 2 x nurse on AL, AuthorisedByFirstName:Dirkje (Dorien), Duration:1 Day, Reason:Request To Work 

 Appraisals Logbook > ActionId:31, Action:Appraisal Add, EmployeeId:PW8996, TxnId:1, ScreenType:1 

 ActionId:32 > Action:Appraisal Update, EmployeeId:PW8996, TxnId:1, ScreenType:1 

 ActionId:33 > Action:Appraisal Delete, EmployeeId:PW8996, TxnId:1, ScreenType:1 

 Benefit Logbook > ActionId:34, Action:Benefit Add, EmployeeId:PW8996, TxnId:1, ScreenType:2 

 ActionId:35 > Action:Benefit Update, EmployeeId:PW8996, TxnId:1, ScreenType:2 

 ActionId:36 > Action:Benefit Delete, EmployeeId:PW8996, TxnId:1, ScreenType:2 

 CPD Logbook > ActionId:37, Action:CPD Add, EmployeeId:PW8996, TxnId:1, ScreenType:3 

 ActionId:38 > Action:CPD Update, EmployeeId:PW8996, TxnId:1, ScreenType:3 

 ActionId:39 > Action:CPD Delete, EmployeeId:PW8996, TxnId:1, ScreenType:3 

 Driving Licence Logbook > ActionId:40, Action:Driving Licence Add, EmployeeId:PW8996, TxnId:1, ScreenType:6 

 ActionId:41 > Action:Driving Licence Update, EmployeeId:PW8996, TxnId:1, ScreenType:6 

 ActionId:42 > Action:Driving Licence Delete, EmployeeId:PW8996, TxnId:1, ScreenType:6 

 Qualification Logbook > ActionId:43, Action:Qualification Add, EmployeeId:PW8996, TxnId:1, ScreenType:4 

 ActionId:44 > , Action:Qualification Update, EmployeeId:PW8996, TxnId:1, ScreenType:4 

 ActionId:45 > Action:Qualification Delete, EmployeeId:PW8996, TxnId:1, ScreenType:4 

 Training Logbook > ActionId:46, Action:Training Add, EmployeeId:PW8996, TxnId:1, ScreenType:5 

 ActionId:47 > Action:Training Update, EmployeeId:PW8996, TxnId:1, ScreenType:5 

 ActionId:48 > Action:Training Delete, EmployeeId:PW8996, TxnId:1, ScreenType:5 

 Vehicle Logbook > ActionId:49, Action:Vehicle Add, EmployeeId:PW8996, TxnId:1, ScreenType:7 

 ActionId:50 > Action:Vehicle Update, EmployeeId:PW8996, TxnId:1, ScreenType:7 

 ActionId:51 > Action:Vehicle Delete, EmployeeId:PW8996, TxnId:1, ScreenType:7 

 Custom Logbook > ActionId:52, Action:Custom Screen Add, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10 

 ActionId:53 > Action:Custom Screen Update, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10 

 ActionId:54 > Action:Custom Screen Delete, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10


Keys 

 The unique key for an event on the People calendar is Start Date and End Date -- you should also use the same key to identify record in your system that is consuming the data from People - the reason you need to do this is to locate the original record within your system when you get a notification of an update or a deletion - you will notice the message fragment contains the original dates - so you can locate the record - and the new dates. 
Another more sophisticated option is to use the transaction ID. Holiday, Sick, Other Event and Maternity/Paternity transactions within People allow you to store an external transaction. Using this approach you could store the transaction id from a calendering system such as Outlook. If the holiday record on People is amended or deleted you will be able to determine the corresponding record in Outlook. 

 Take the following scenario: 

 If you create holidays through the API you will receive AnnualLeaveTxnId in the API result set. Any integration can store this as a reference from People HR holidays mapping 

 If you create holidays within the People HR UI, you will receive webhook details with holidays details. Integrated applications need to call people holidays GET details API with the current webhook details. That will give you AnnualLeaveTxnID & ReferenceId (If any). Now you can save the AnnualLeaveTxnId in an integrated application as People HR holidays mapping. 

 You can store third party application holidays/transaction references into the People HR system by calling the API Employee Holiday -> Update Holiday Reference ID 

 If you want to update/delete any holidays from People HR that are already mapped with third party applications/integrations, you can call holidays API to match with reference ID. You will get assoicated data with the reference ID that you actually need to update/ delete holidays from the people system (Employee Holiday -> UpdateHoliday or Employee Holiday -> DeleteHoliday).


Start Part of Day and End Part of Day
In People it is possible to record half days both at the beginning of a holiday or sick event or at the end. You can determine this by looking at the StartPartOfDay and EndPartOfDay values which will either be blank, AM or PM.



# Examples<a id="examples"></a>
We've put a few examples together for you that might help you get started:

HTML Coding Examples: https://help.peoplehr.com/en/articles/981415-api-html-examples

c# Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-c-code-snippet

Objective C Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-code-snippets-objective-c

How to use Postman with the API: http://intercom.help/peoplea-apps/api-and-integration/api-using-postman

<!-- ReDoc-Inject: <security-definitions> -->



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`peoplehr.applicant.check_duplicate_applicant`](#peoplehrapplicantcheck_duplicate_applicant)
  * [`peoplehr.applicant.create_new_applicant`](#peoplehrapplicantcreate_new_applicant)
  * [`peoplehr.applicant.upload_document`](#peoplehrapplicantupload_document)
  * [`peoplehr.background_check.add_detail`](#peoplehrbackground_checkadd_detail)
  * [`peoplehr.background_check.delete_detail`](#peoplehrbackground_checkdelete_detail)
  * [`peoplehr.background_check.get_detail_by_employee_id`](#peoplehrbackground_checkget_detail_by_employee_id)
  * [`peoplehr.background_check.update_detail`](#peoplehrbackground_checkupdate_detail)
  * [`peoplehr.email_transaction.submit_email_inbox`](#peoplehremail_transactionsubmit_email_inbox)
  * [`peoplehr.employee.add_image_by_id`](#peoplehremployeeadd_image_by_id)
  * [`peoplehr.employee.add_new_employee`](#peoplehremployeeadd_new_employee)
  * [`peoplehr.employee.authenticate_user`](#peoplehremployeeauthenticate_user)
  * [`peoplehr.employee.get_detail_by_id`](#peoplehremployeeget_detail_by_id)
  * [`peoplehr.employee.list_employee_detail`](#peoplehremployeelist_employee_detail)
  * [`peoplehr.employee.update_detail`](#peoplehremployeeupdate_detail)
  * [`peoplehr.employee.update_employee_id_details`](#peoplehremployeeupdate_employee_id_details)
  * [`peoplehr.employee.update_leaver_status_by_id`](#peoplehremployeeupdate_leaver_status_by_id)
  * [`peoplehr.employee_absence.create_new_absence`](#peoplehremployee_absencecreate_new_absence)
  * [`peoplehr.employee_absence.get_detail`](#peoplehremployee_absenceget_detail)
  * [`peoplehr.employee_absence.remove_absence`](#peoplehremployee_absenceremove_absence)
  * [`peoplehr.employee_absence.update_absence_record`](#peoplehremployee_absenceupdate_absence_record)
  * [`peoplehr.employee_appraisal.create_new_appraisal`](#peoplehremployee_appraisalcreate_new_appraisal)
  * [`peoplehr.employee_appraisal.delete_appraisal`](#peoplehremployee_appraisaldelete_appraisal)
  * [`peoplehr.employee_appraisal.get_by_appraisal_id`](#peoplehremployee_appraisalget_by_appraisal_id)
  * [`peoplehr.employee_appraisal.get_by_employee_id`](#peoplehremployee_appraisalget_by_employee_id)
  * [`peoplehr.employee_appraisal.update_user_appraisal`](#peoplehremployee_appraisalupdate_user_appraisal)
  * [`peoplehr.employee_benefit.create_new_benefit`](#peoplehremployee_benefitcreate_new_benefit)
  * [`peoplehr.employee_benefit.delete_benefit`](#peoplehremployee_benefitdelete_benefit)
  * [`peoplehr.employee_benefit.get_by_benefit_id_details`](#peoplehremployee_benefitget_by_benefit_id_details)
  * [`peoplehr.employee_benefit.get_by_employee_id_details`](#peoplehremployee_benefitget_by_employee_id_details)
  * [`peoplehr.employee_benefit.update_details`](#peoplehremployee_benefitupdate_details)
  * [`peoplehr.employee_cpd.create_new_cpd`](#peoplehremployee_cpdcreate_new_cpd)
  * [`peoplehr.employee_cpd.delete_cpd`](#peoplehremployee_cpddelete_cpd)
  * [`peoplehr.employee_cpd.get_by_cpd_id`](#peoplehremployee_cpdget_by_cpd_id)
  * [`peoplehr.employee_cpd.get_by_employee_id`](#peoplehremployee_cpdget_by_employee_id)
  * [`peoplehr.employee_cpd.update_cpd`](#peoplehremployee_cpdupdate_cpd)
  * [`peoplehr.employee_custom_screen.add_new_custom_screen_transaction`](#peoplehremployee_custom_screenadd_new_custom_screen_transaction)
  * [`peoplehr.employee_custom_screen.delete_custom_screen_transaction`](#peoplehremployee_custom_screendelete_custom_screen_transaction)
  * [`peoplehr.employee_custom_screen.get_by_custom_screen_transaction`](#peoplehremployee_custom_screenget_by_custom_screen_transaction)
  * [`peoplehr.employee_custom_screen.get_detail`](#peoplehremployee_custom_screenget_detail)
  * [`peoplehr.employee_custom_screen.get_screen_by_employee_id`](#peoplehremployee_custom_screenget_screen_by_employee_id)
  * [`peoplehr.employee_custom_screen.update_custom_screen_transaction`](#peoplehremployee_custom_screenupdate_custom_screen_transaction)
  * [`peoplehr.employee_document.get_all_documents`](#peoplehremployee_documentget_all_documents)
  * [`peoplehr.employee_document.get_document_by_id`](#peoplehremployee_documentget_document_by_id)
  * [`peoplehr.employee_document.submit_document_details`](#peoplehremployee_documentsubmit_document_details)
  * [`peoplehr.employee_driving.add_new_driving_license`](#peoplehremployee_drivingadd_new_driving_license)
  * [`peoplehr.employee_driving.get_driving_license_by_driving_id`](#peoplehremployee_drivingget_driving_license_by_driving_id)
  * [`peoplehr.employee_driving.get_driving_license_by_employee_id`](#peoplehremployee_drivingget_driving_license_by_employee_id)
  * [`peoplehr.employee_driving.remove_driving_license`](#peoplehremployee_drivingremove_driving_license)
  * [`peoplehr.employee_driving.update_driving_license`](#peoplehremployee_drivingupdate_driving_license)
  * [`peoplehr.employee_holiday.add_new_holiday`](#peoplehremployee_holidayadd_new_holiday)
  * [`peoplehr.employee_holiday.get_holiday_detail`](#peoplehremployee_holidayget_holiday_detail)
  * [`peoplehr.employee_holiday.remove_holiday_detail`](#peoplehremployee_holidayremove_holiday_detail)
  * [`peoplehr.employee_holiday.update_detail`](#peoplehremployee_holidayupdate_detail)
  * [`peoplehr.employee_project_timesheet.add_new_project_task_detail`](#peoplehremployee_project_timesheetadd_new_project_task_detail)
  * [`peoplehr.employee_project_timesheet.add_new_project_task_detail_0`](#peoplehremployee_project_timesheetadd_new_project_task_detail_0)
  * [`peoplehr.employee_project_timesheet.add_project_detail`](#peoplehremployee_project_timesheetadd_project_detail)
  * [`peoplehr.employee_project_timesheet.create_timesheet`](#peoplehremployee_project_timesheetcreate_timesheet)
  * [`peoplehr.employee_project_timesheet.delete_timesheet`](#peoplehremployee_project_timesheetdelete_timesheet)
  * [`peoplehr.employee_project_timesheet.edit_project_details`](#peoplehremployee_project_timesheetedit_project_details)
  * [`peoplehr.employee_project_timesheet.edit_task_detail`](#peoplehremployee_project_timesheetedit_task_detail)
  * [`peoplehr.employee_project_timesheet.get_all_project_task`](#peoplehremployee_project_timesheetget_all_project_task)
  * [`peoplehr.employee_project_timesheet.get_all_project_task_detail`](#peoplehremployee_project_timesheetget_all_project_task_detail)
  * [`peoplehr.employee_project_timesheet.get_by_transaction_id`](#peoplehremployee_project_timesheetget_by_transaction_id)
  * [`peoplehr.employee_project_timesheet.get_project_timesheet_detail`](#peoplehremployee_project_timesheetget_project_timesheet_detail)
  * [`peoplehr.employee_project_timesheet.list_all_timesheet_project`](#peoplehremployee_project_timesheetlist_all_timesheet_project)
  * [`peoplehr.employee_project_timesheet.update_project_task_detail`](#peoplehremployee_project_timesheetupdate_project_task_detail)
  * [`peoplehr.employee_project_timesheet.update_timesheet`](#peoplehremployee_project_timesheetupdate_timesheet)
  * [`peoplehr.employee_qualification.add_new_qualification`](#peoplehremployee_qualificationadd_new_qualification)
  * [`peoplehr.employee_qualification.delete_qualification`](#peoplehremployee_qualificationdelete_qualification)
  * [`peoplehr.employee_qualification.get_by_employee_id`](#peoplehremployee_qualificationget_by_employee_id)
  * [`peoplehr.employee_qualification.get_by_qualification_id`](#peoplehremployee_qualificationget_by_qualification_id)
  * [`peoplehr.employee_qualification.update_qualification`](#peoplehremployee_qualificationupdate_qualification)
  * [`peoplehr.employee_salary.add_new_salary`](#peoplehremployee_salaryadd_new_salary)
  * [`peoplehr.employee_salary.delete_salary`](#peoplehremployee_salarydelete_salary)
  * [`peoplehr.employee_salary.get_salary_detail`](#peoplehremployee_salaryget_salary_detail)
  * [`peoplehr.employee_timesheet.create_new_timesheet`](#peoplehremployee_timesheetcreate_new_timesheet)
  * [`peoplehr.employee_timesheet.delete_timesheet`](#peoplehremployee_timesheetdelete_timesheet)
  * [`peoplehr.employee_timesheet.get_detail_list`](#peoplehremployee_timesheetget_detail_list)
  * [`peoplehr.employee_timesheet.update_details`](#peoplehremployee_timesheetupdate_details)
  * [`peoplehr.employee_training.add_training_detail`](#peoplehremployee_trainingadd_training_detail)
  * [`peoplehr.employee_training.get_detail`](#peoplehremployee_trainingget_detail)
  * [`peoplehr.employee_training.remove_detail`](#peoplehremployee_trainingremove_detail)
  * [`peoplehr.employee_training.update_training_detail`](#peoplehremployee_trainingupdate_training_detail)
  * [`peoplehr.employee_vehicle.create_new_vehicle_detail`](#peoplehremployee_vehiclecreate_new_vehicle_detail)
  * [`peoplehr.employee_vehicle.delete_detail`](#peoplehremployee_vehicledelete_detail)
  * [`peoplehr.employee_vehicle.get_by_vehicle_detail_id`](#peoplehremployee_vehicleget_by_vehicle_detail_id)
  * [`peoplehr.employee_vehicle.get_detail_by_employee_id`](#peoplehremployee_vehicleget_detail_by_employee_id)
  * [`peoplehr.employee_vehicle.update_detail`](#peoplehremployee_vehicleupdate_detail)
  * [`peoplehr.employeee_late.create_new_late`](#peoplehremployeee_latecreate_new_late)
  * [`peoplehr.employeee_late.delete_late`](#peoplehremployeee_latedelete_late)
  * [`peoplehr.employeee_late.get_by_employee_id`](#peoplehremployeee_lateget_by_employee_id)
  * [`peoplehr.employeee_late.update_late`](#peoplehremployeee_lateupdate_late)
  * [`peoplehr.history.get_by_employee_id_and_field_name`](#peoplehrhistoryget_by_employee_id_and_field_name)
  * [`peoplehr.holiday_entitlement.get_holiday_entitlement`](#peoplehrholiday_entitlementget_holiday_entitlement)
  * [`peoplehr.holiday_entitlement.get_next_year_entitlement`](#peoplehrholiday_entitlementget_next_year_entitlement)
  * [`peoplehr.holiday_entitlement.update_holiday_entitlement`](#peoplehrholiday_entitlementupdate_holiday_entitlement)
  * [`peoplehr.holiday_entitlement.update_next_year_entitlement`](#peoplehrholiday_entitlementupdate_next_year_entitlement)
  * [`peoplehr.maternity_paternity_.add_new_details`](#peoplehrmaternity_paternity_add_new_details)
  * [`peoplehr.maternity_paternity_.delete_details`](#peoplehrmaternity_paternity_delete_details)
  * [`peoplehr.maternity_paternity_.get_by_employee_id`](#peoplehrmaternity_paternity_get_by_employee_id)
  * [`peoplehr.maternity_paternity_.get_details_by_mat_pat_id`](#peoplehrmaternity_paternity_get_details_by_mat_pat_id)
  * [`peoplehr.maternity_paternity_.update_details`](#peoplehrmaternity_paternity_update_details)
  * [`peoplehr.other_event.create_event_leave`](#peoplehrother_eventcreate_event_leave)
  * [`peoplehr.other_event.delete_event`](#peoplehrother_eventdelete_event)
  * [`peoplehr.other_event.get_detail`](#peoplehrother_eventget_detail)
  * [`peoplehr.other_event.get_entitlement`](#peoplehrother_eventget_entitlement)
  * [`peoplehr.other_event.insert_update_entitlement`](#peoplehrother_eventinsert_update_entitlement)
  * [`peoplehr.other_event.update_event_leave`](#peoplehrother_eventupdate_event_leave)
  * [`peoplehr.query.get_by_query_name`](#peoplehrqueryget_by_query_name)
  * [`peoplehr.query.get_result_by_query_id`](#peoplehrqueryget_result_by_query_id)
  * [`peoplehr.right_to_work.add_detail`](#peoplehrright_to_workadd_detail)
  * [`peoplehr.right_to_work.delete_detail`](#peoplehrright_to_workdelete_detail)
  * [`peoplehr.right_to_work.get_detail`](#peoplehrright_to_workget_detail)
  * [`peoplehr.right_to_work.update_detail`](#peoplehrright_to_workupdate_detail)
  * [`peoplehr.vacancy.add_new_vacancy`](#peoplehrvacancyadd_new_vacancy)
  * [`peoplehr.vacancy.get_all_vacancies`](#peoplehrvacancyget_all_vacancies)
  * [`peoplehr.vacancy.get_detail`](#peoplehrvacancyget_detail)
  * [`peoplehr.work_pattern.get_work_detail`](#peoplehrwork_patternget_work_detail)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=PeopleHR&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from people_hr_python_sdk import PeopleHr, ApiException

peoplehr = PeopleHr(
)

try:
    # Check duplicate applicant
    check_duplicate_applicant_response = peoplehr.applicant.check_duplicate_applicant(
        api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
        action="string_example",
        first_name="Ranjit",
        last_name="Johnson",
        vacancy_reference="VA4",
        email="vaibhavid@itgurussoftware.com",
    )
    print(check_duplicate_applicant_response)
except ApiException as e:
    print("Exception when calling ApplicantApi.check_duplicate_applicant: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from people_hr_python_sdk import PeopleHr, ApiException

peoplehr = PeopleHr(
)

async def main():
    try:
        # Check duplicate applicant
        check_duplicate_applicant_response = await peoplehr.applicant.acheck_duplicate_applicant(
            api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
            action="string_example",
            first_name="Ranjit",
            last_name="Johnson",
            vacancy_reference="VA4",
            email="vaibhavid@itgurussoftware.com",
        )
        print(check_duplicate_applicant_response)
    except ApiException as e:
        print("Exception when calling ApplicantApi.check_duplicate_applicant: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from people_hr_python_sdk import PeopleHr, ApiException

peoplehr = PeopleHr(
)

try:
    # Check duplicate applicant
    check_duplicate_applicant_response = peoplehr.applicant.raw.check_duplicate_applicant(
        api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
        action="string_example",
        first_name="Ranjit",
        last_name="Johnson",
        vacancy_reference="VA4",
        email="vaibhavid@itgurussoftware.com",
    )
    pprint(check_duplicate_applicant_response.body)
    pprint(check_duplicate_applicant_response.body["is_error"])
    pprint(check_duplicate_applicant_response.body["status"])
    pprint(check_duplicate_applicant_response.body["message"])
    pprint(check_duplicate_applicant_response.body["result"])
    pprint(check_duplicate_applicant_response.headers)
    pprint(check_duplicate_applicant_response.status)
    pprint(check_duplicate_applicant_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApplicantApi.check_duplicate_applicant: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `peoplehr.applicant.check_duplicate_applicant`<a id="peoplehrapplicantcheck_duplicate_applicant"></a>

This API is used to Check duplicate applicant



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_duplicate_applicant_response = peoplehr.applicant.check_duplicate_applicant(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    first_name="Ranjit",
    last_name="Johnson",
    vacancy_reference="VA4",
    email="vaibhavid@itgurussoftware.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for applicant api to check duplicate applicant

##### action: `str`<a id="action-str"></a>

Action default value

##### first_name: [`FirstName`](./people_hr_python_sdk/type/first_name.py)<a id="first_name-firstnamepeople_hr_python_sdktypefirst_namepy"></a>

First name for check duplicate applicant

##### last_name: [`LastName`](./people_hr_python_sdk/type/last_name.py)<a id="last_name-lastnamepeople_hr_python_sdktypelast_namepy"></a>

Last name for check duplicate applicant

##### vacancy_reference: `str`<a id="vacancy_reference-str"></a>

VacancyReference default value 

##### email: [`Email`](./people_hr_python_sdk/type/email.py)<a id="email-emailpeople_hr_python_sdktypeemailpy"></a>

Email for check duplicate applicant

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckDuplicateApplicantParameter`](./people_hr_python_sdk/type/check_duplicate_applicant_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCheckDuplicateApplicant`](./people_hr_python_sdk/pydantic/error_for_check_duplicate_applicant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Applicant  -  CheckDuplicateApplicant` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.applicant.create_new_applicant`<a id="peoplehrapplicantcreate_new_applicant"></a>

This API is used to create new applicant



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_applicant_response = peoplehr.applicant.create_new_applicant(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    first_name="Ranjit",
    last_name="Johnson",
    documents=[
        {
            "document_name": "xyz.png",
            "url": "www.google.com/doc2.docx",
        }
    ],
    skills="C#, Asp.net, JQuery",
    vacancy_reference="VA4",
    email="vaibhavid@itgurussoftware.com",
    gender="true",
    date_of_birth="1999-01-02",
    post_code="413608",
    address="Shiv Colony, Thergaon - Pune",
    phone_number="8899556885",
    other_contact_details="8899556885",
    source="Facebook",
    additional_questions=[
        {
2,
1,
        }
    ],
    internal_questions=[
        {
2,
1,
        }
    ],
    recruitment_cost=50,
    date_last_contacted="2016-01-13",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for applicant api to Create new applicant

##### action: `str`<a id="action-str"></a>

Action default value

##### first_name: [`FirstName`](./people_hr_python_sdk/type/first_name.py)<a id="first_name-firstnamepeople_hr_python_sdktypefirst_namepy"></a>

First name for create new applicant

##### last_name: [`LastName`](./people_hr_python_sdk/type/last_name.py)<a id="last_name-lastnamepeople_hr_python_sdktypelast_namepy"></a>

Last name for create new applicant

##### documents: [`DocumentsForCreateNewApplicantArray`](./people_hr_python_sdk/type/documents_for_create_new_applicant_array.py)<a id="documents-documentsforcreatenewapplicantarraypeople_hr_python_sdktypedocuments_for_create_new_applicant_arraypy"></a>

Documents for create new applicant

##### skills: `str`<a id="skills-str"></a>

Skills default value

##### vacancy_reference: `str`<a id="vacancy_reference-str"></a>

VacancyReference default value 

##### email: [`Email`](./people_hr_python_sdk/type/email.py)<a id="email-emailpeople_hr_python_sdktypeemailpy"></a>

Email for create new applicant

##### gender: [`Gender`](./people_hr_python_sdk/type/gender.py)<a id="gender-genderpeople_hr_python_sdktypegenderpy"></a>

Gender for create new applicant

##### date_of_birth: `date`<a id="date_of_birth-date"></a>

DateOfBirth default value 

##### post_code: [`PostCode`](./people_hr_python_sdk/type/post_code.py)<a id="post_code-postcodepeople_hr_python_sdktypepost_codepy"></a>

Post code for create new applicant

##### address: `str`<a id="address-str"></a>

Address default value 

##### phone_number: `str`<a id="phone_number-str"></a>

Phone number default value

##### other_contact_details: `str`<a id="other_contact_details-str"></a>

Other contact details default value

##### source: `str`<a id="source-str"></a>

Source default value

##### additional_questions: [`AdditionalQuestionsForCreatenewApplicantArray`](./people_hr_python_sdk/type/additional_questions_for_createnew_applicant_array.py)<a id="additional_questions-additionalquestionsforcreatenewapplicantarraypeople_hr_python_sdktypeadditional_questions_for_createnew_applicant_arraypy"></a>

Source for create new applicant

##### internal_questions: [`InternalQuestionsForCreateNewApplicantArray`](./people_hr_python_sdk/type/internal_questions_for_create_new_applicant_array.py)<a id="internal_questions-internalquestionsforcreatenewapplicantarraypeople_hr_python_sdktypeinternal_questions_for_create_new_applicant_arraypy"></a>

Internal questions for create new applicant

##### recruitment_cost: `int`<a id="recruitment_cost-int"></a>

Recruitment cost default value

##### date_last_contacted: `date`<a id="date_last_contacted-date"></a>

Date last contacted default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateApplicantDetailParameter`](./people_hr_python_sdk/type/create_applicant_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCreateNewApplicant`](./people_hr_python_sdk/pydantic/error_for_create_new_applicant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Applicant  -  CreateNewApplicant` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.applicant.upload_document`<a id="peoplehrapplicantupload_document"></a>

This API is used to upload applicant document



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_document_response = peoplehr.applicant.upload_document(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    applicant_id=90,
    document_name="Abc.txt",
    file="Pass base64 string",
    description="Description here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Employee late api to upload applicant document

##### action: `str`<a id="action-str"></a>

Action default value

##### applicant_id: [`Bigint`](./people_hr_python_sdk/type/bigint.py)<a id="applicant_id-bigintpeople_hr_python_sdktypebigintpy"></a>

Applicant id default value

##### document_name: `str`<a id="document_name-str"></a>

DocumentName value

##### file: `str`<a id="file-str"></a>

File value

##### description: `str`<a id="description-str"></a>

Description value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadapplicantdocumentParameter`](./people_hr_python_sdk/type/uploadapplicantdocument_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForuploadapplicantdocument`](./people_hr_python_sdk/pydantic/error_foruploadapplicantdocument.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Applicant  -  uploadapplicantdocument` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.background_check.add_detail`<a id="peoplehrbackground_checkadd_detail"></a>

This API is used to add background check detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_detail_response = peoplehr.background_check.add_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    type_of_check="DBS Enhanced",
    document_name="Abc.txt",
    file="Pass base64 string",
    date_completed="2016-04-15",
    expiry_date="2018-07-07",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for background check api to AddBackgroundCheckDetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for Add Background Check Detail

##### type_of_check: `str`<a id="type_of_check-str"></a>

Type Of Check default value 

##### document_name: `str`<a id="document_name-str"></a>

DocumentName value

##### file: `str`<a id="file-str"></a>

File value

##### date_completed: `date`<a id="date_completed-date"></a>

Date Completed default value 

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddBackgroundCheckDetailParameter`](./people_hr_python_sdk/type/add_background_check_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddBackgroundCheckDetail`](./people_hr_python_sdk/pydantic/error_for_add_background_check_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Background Check  -  AddBackgroundCheckDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.background_check.delete_detail`<a id="peoplehrbackground_checkdelete_detail"></a>

This API is used to Delete Background Check Detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_detail_response = peoplehr.background_check.delete_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    background_check_txn_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for background check api to  delete background check detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete background check detail

##### background_check_txn_id: `int`<a id="background_check_txn_id-int"></a>

BackgroundCheckTxnId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteBackgroundCheckDetailParameter`](./people_hr_python_sdk/type/delete_background_check_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteBackgroundCheckDetail`](./people_hr_python_sdk/pydantic/error_for_delete_background_check_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Background Check  -  DeleteBackgroundCheckDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.background_check.get_detail_by_employee_id`<a id="peoplehrbackground_checkget_detail_by_employee_id"></a>

This API is used to Get Background Check Detail By EmployeeId


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_by_employee_id_response = peoplehr.background_check.get_detail_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for background check api to Get Background Check Detail By EmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to Get Background Check Detail By EmployeeId

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetBackgroundCheckDetailByEmployeeIdParameter`](./people_hr_python_sdk/type/get_background_check_detail_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetBackgroundCheckDetailByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_background_check_detail_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Background Check  -  GetBackgroundCheckDetailByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.background_check.update_detail`<a id="peoplehrbackground_checkupdate_detail"></a>

This API is used to update background check detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_detail_response = peoplehr.background_check.update_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    background_check_txn_id=1,
    type_of_check="DBS Enhanced",
    document_name="Abc.txt",
    file="Pass base64 string",
    date_completed="2016-04-15",
    expiry_date="2018-07-07",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for background check api to UpdateBackgroundCheckDetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for Update Background Check Detail

##### background_check_txn_id: `int`<a id="background_check_txn_id-int"></a>

BackgroundCheckTxnId default value 

##### type_of_check: `str`<a id="type_of_check-str"></a>

Type Of Check default value 

##### document_name: `str`<a id="document_name-str"></a>

DocumentName value

##### file: `str`<a id="file-str"></a>

File value

##### date_completed: `date`<a id="date_completed-date"></a>

Date Completed default value 

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateBackgroundCheckDetailParameter`](./people_hr_python_sdk/type/update_background_check_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateBackgroundCheckDetail`](./people_hr_python_sdk/pydantic/error_for_update_background_check_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Background Check  -  UpdateBackgroundCheckDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.email_transaction.submit_email_inbox`<a id="peoplehremail_transactionsubmit_email_inbox"></a>

This API is used for Email Inbox


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_email_inbox_response = peoplehr.email_transaction.submit_email_inbox(
    action="string_example",
    email_from="rajendra.petave@itgurussoftware.com",
    email_to=[
        {
            "email_id": "raj@itgurus.com",
        }
    ],
    email_subject="[Recipient email address] Email Subject",
    email_cc=[
        {
            "email_id": "raj@itgurus.com",
        }
    ],
    email_bcc=[
        {
            "email_id": "raj@itgurus.com",
        }
    ],
    attachment=[
        {
            "file_name": "abc.doc",
            "size": "15728640",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

Action default value

##### email_from: [`EmailFrom`](./people_hr_python_sdk/type/email_from.py)<a id="email_from-emailfrompeople_hr_python_sdktypeemail_frompy"></a>

Email From for Email Inbox

##### email_to: [`Result1ForEmailToForEmailInbox`](./people_hr_python_sdk/type/result1_for_email_to_for_email_inbox.py)<a id="email_to-result1foremailtoforemailinboxpeople_hr_python_sdktyperesult1_for_email_to_for_email_inboxpy"></a>

Email To for Email Inbox

##### email_subject: [`EmailSubject`](./people_hr_python_sdk/type/email_subject.py)<a id="email_subject-emailsubjectpeople_hr_python_sdktypeemail_subjectpy"></a>

Email Subject for Email Inbox

##### email_cc: [`Result1ForEmailCcForEmailInbox`](./people_hr_python_sdk/type/result1_for_email_cc_for_email_inbox.py)<a id="email_cc-result1foremailccforemailinboxpeople_hr_python_sdktyperesult1_for_email_cc_for_email_inboxpy"></a>

Email Cc for Email Inbox

##### email_bcc: [`Result1ForEmailBccForEmailInbox`](./people_hr_python_sdk/type/result1_for_email_bcc_for_email_inbox.py)<a id="email_bcc-result1foremailbccforemailinboxpeople_hr_python_sdktyperesult1_for_email_bcc_for_email_inboxpy"></a>

Email Bcc for Email Inbox

##### attachment: [`Result1ForAttachmentForEmailInbox`](./people_hr_python_sdk/type/result1_for_attachment_for_email_inbox.py)<a id="attachment-result1forattachmentforemailinboxpeople_hr_python_sdktyperesult1_for_attachment_for_email_inboxpy"></a>

Attachment for Email Inbox

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailInboxParameter`](./people_hr_python_sdk/type/email_inbox_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForEmailInbox`](./people_hr_python_sdk/pydantic/error_for_email_inbox.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Email Transaction  -  EmailInbox` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.add_image_by_id`<a id="peoplehremployeeadd_image_by_id"></a>

This API is used to add employee image by id


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_image_by_id_response = peoplehr.employee.add_image_by_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    employee_image_name="xyz.png",
    employee_image="Pass base64 string",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to AddEmployeeImage

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add employee image 

##### employee_image_name: `str`<a id="employee_image_name-str"></a>

EmployeeImageName default value 

##### employee_image: `str`<a id="employee_image-str"></a>

EmployeeImage default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddEmployeeImageById2`](./people_hr_python_sdk/type/add_employee_image_by_id2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddEmployeeImageById`](./people_hr_python_sdk/pydantic/error_for_add_employee_image_by_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  AddEmployeeImage` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.add_new_employee`<a id="peoplehremployeeadd_new_employee"></a>

This API is used to create new employee


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_employee_response = peoplehr.employee.add_new_employee(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    first_name="Ranjit",
    last_name="Johnson",
    start_date="2016-07-27",
    job_role="Software Enginner",
    job_role_effective_date="2014-01-01",
    location="Mumbai",
    department="IT",
    title="Mr.",
    email="vaibhavid@itgurussoftware.com",
    gender="true",
    date_of_birth="1999-01-02",
    reports_to="firstname.lastname@itgurusssoftware.com",
    company="Company name",
    national_insurance_number="AAAAAAAAAAAAAAAAAAA",
    nationality="Indian",
    employment_type="Full time",
    entitlement_this_year="12.50",
    entitlement_next_year="0",
    address="Shiv Colony, Thergaon - Pune",
    personal_phone_number="999890988772",
    payroll_company="Your payroll company's name ",
    payroll_id="Your Payroll ID",
    time__attendance_id="Your Time & Attendance ID",
    rota_id="Your Rota ID",
    crm_id="Your CRM ID",
    ats_id="Your ATS ID",
    performance_id="Your Performance ID",
    benefits_id="Your Benefits ID",
    system1_id="Your System One ID",
    system2_id="Your System Two ID",
    system3_id="Your System Three ID",
    api_column1="APIColumn1 Value",
    api_column2="APIColumn2 Value",
    api_column3="APIColumn3 Value",
    api_column4="APIColumn4 Value",
    api_column5="APIColumn5 Value",
    personal_email="abc@itgurussoftware.com",
    method_of_recruitment="Method Of Recruitment",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to createNewEmployee

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for create new employee

##### first_name: [`FirstName`](./people_hr_python_sdk/type/first_name.py)<a id="first_name-firstnamepeople_hr_python_sdktypefirst_namepy"></a>

FirstName for create new employee

##### last_name: [`LastName`](./people_hr_python_sdk/type/last_name.py)<a id="last_name-lastnamepeople_hr_python_sdktypelast_namepy"></a>

LastName for create new employee

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### job_role: [`JobRole`](./people_hr_python_sdk/type/job_role.py)<a id="job_role-jobrolepeople_hr_python_sdktypejob_rolepy"></a>

Job role for create new employee

##### job_role_effective_date: `date`<a id="job_role_effective_date-date"></a>

JobRoleEffectiveDate default value 

##### location: `str`<a id="location-str"></a>

Location default value 

##### department: `str`<a id="department-str"></a>

Department default value 

##### title: [`Title`](./people_hr_python_sdk/type/title.py)<a id="title-titlepeople_hr_python_sdktypetitlepy"></a>

Title for create new employee

##### email: [`Email`](./people_hr_python_sdk/type/email.py)<a id="email-emailpeople_hr_python_sdktypeemailpy"></a>

Email for create new employee

##### gender: [`Gender`](./people_hr_python_sdk/type/gender.py)<a id="gender-genderpeople_hr_python_sdktypegenderpy"></a>

Gender value for create new employee

##### date_of_birth: `date`<a id="date_of_birth-date"></a>

DateOfBirth default value 

##### reports_to: [`ReportsTo`](./people_hr_python_sdk/type/reports_to.py)<a id="reports_to-reportstopeople_hr_python_sdktypereports_topy"></a>

Reports To for create new employee

##### company: [`Company`](./people_hr_python_sdk/type/company.py)<a id="company-companypeople_hr_python_sdktypecompanypy"></a>

Company name for create new employee

##### national_insurance_number: [`NationalInsuranceNumber`](./people_hr_python_sdk/type/national_insurance_number.py)<a id="national_insurance_number-nationalinsurancenumberpeople_hr_python_sdktypenational_insurance_numberpy"></a>

National insurance number for create new employee

##### nationality: [`Nationality`](./people_hr_python_sdk/type/nationality.py)<a id="nationality-nationalitypeople_hr_python_sdktypenationalitypy"></a>

Nationality for create new employee

##### employment_type: [`EmploymentType`](./people_hr_python_sdk/type/employment_type.py)<a id="employment_type-employmenttypepeople_hr_python_sdktypeemployment_typepy"></a>

Employment type for create new employee

##### entitlement_this_year: `str`<a id="entitlement_this_year-str"></a>

Entitlement this year default value 

##### entitlement_next_year: `str`<a id="entitlement_next_year-str"></a>

Entitlement next year default value 

##### address: `str`<a id="address-str"></a>

Address default value 

##### personal_phone_number: [`PersonalPhoneNumber`](./people_hr_python_sdk/type/personal_phone_number.py)<a id="personal_phone_number-personalphonenumberpeople_hr_python_sdktypepersonal_phone_numberpy"></a>

PersonalPhoneNumber for create new employee

##### payroll_company: [`PayrollCompany`](./people_hr_python_sdk/type/payroll_company.py)<a id="payroll_company-payrollcompanypeople_hr_python_sdktypepayroll_companypy"></a>

Payroll company for create new employee

##### payroll_id: [`PayrollID`](./people_hr_python_sdk/type/payroll_id.py)<a id="payroll_id-payrollidpeople_hr_python_sdktypepayroll_idpy"></a>

Payroll id for create new employee

##### time__attendance_id: [`TimeAttendanceID`](./people_hr_python_sdk/type/time_attendance_id.py)<a id="time__attendance_id-timeattendanceidpeople_hr_python_sdktypetime_attendance_idpy"></a>

Time & attendance id for create new employee

##### rota_id: [`RotaID`](./people_hr_python_sdk/type/rota_id.py)<a id="rota_id-rotaidpeople_hr_python_sdktyperota_idpy"></a>

Rota id for create new employee

##### crm_id: [`CRMID`](./people_hr_python_sdk/type/crmid.py)<a id="crm_id-crmidpeople_hr_python_sdktypecrmidpy"></a>

CRM id for create new employee

##### ats_id: [`ATSID`](./people_hr_python_sdk/type/atsid.py)<a id="ats_id-atsidpeople_hr_python_sdktypeatsidpy"></a>

ATS id for create new employee

##### performance_id: [`PerformanceID`](./people_hr_python_sdk/type/performance_id.py)<a id="performance_id-performanceidpeople_hr_python_sdktypeperformance_idpy"></a>

Performance id for create new employee

##### benefits_id: [`BenefitsID`](./people_hr_python_sdk/type/benefits_id.py)<a id="benefits_id-benefitsidpeople_hr_python_sdktypebenefits_idpy"></a>

Benefits id for create new employee

##### system1_id: [`System1ID`](./people_hr_python_sdk/type/system1_id.py)<a id="system1_id-system1idpeople_hr_python_sdktypesystem1_idpy"></a>

System1 id for create new employee

##### system2_id: [`System2ID`](./people_hr_python_sdk/type/system2_id.py)<a id="system2_id-system2idpeople_hr_python_sdktypesystem2_idpy"></a>

System2 id for create new employee

##### system3_id: [`System3ID`](./people_hr_python_sdk/type/system3_id.py)<a id="system3_id-system3idpeople_hr_python_sdktypesystem3_idpy"></a>

System3 id for create new employee

##### api_column1: `str`<a id="api_column1-str"></a>

APIColumn1 default value 

##### api_column2: `str`<a id="api_column2-str"></a>

APIColumn2 default value 

##### api_column3: `str`<a id="api_column3-str"></a>

APIColumn3 default value 

##### api_column4: `str`<a id="api_column4-str"></a>

APIColumn4 default value 

##### api_column5: `str`<a id="api_column5-str"></a>

APIColumn5 default value 

##### personal_email: [`PersonalEmail`](./people_hr_python_sdk/type/personal_email.py)<a id="personal_email-personalemailpeople_hr_python_sdktypepersonal_emailpy"></a>

Personal email for create new employee

##### method_of_recruitment: [`MethodOfRecruitment`](./people_hr_python_sdk/type/method_of_recruitment.py)<a id="method_of_recruitment-methodofrecruitmentpeople_hr_python_sdktypemethod_of_recruitmentpy"></a>

Method of recruitment for create new employee

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmployeeDetailParameter`](./people_hr_python_sdk/type/create_employee_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCreateNewEmployeeDetail`](./people_hr_python_sdk/pydantic/error_for_create_new_employee_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  CreateNewEmployee` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.authenticate_user`<a id="peoplehremployeeauthenticate_user"></a>

This API is used to check authentication for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authenticate_user_response = peoplehr.employee.authenticate_user(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    email_address="ranjit@peoplehr.com",
    password="Password2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to checkAuthentication

##### action: `str`<a id="action-str"></a>

Action default value

##### email_address: [`EmailAddress`](./people_hr_python_sdk/type/email_address.py)<a id="email_address-emailaddresspeople_hr_python_sdktypeemail_addresspy"></a>

Email address of user

##### password: [`Password`](./people_hr_python_sdk/type/password.py)<a id="password-passwordpeople_hr_python_sdktypepasswordpy"></a>

Password of user

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckAuthentication2`](./people_hr_python_sdk/type/check_authentication2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckAuthenticationResult`](./people_hr_python_sdk/pydantic/check_authentication_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  CheckAuthentication` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.get_detail_by_id`<a id="peoplehremployeeget_detail_by_id"></a>

This API is used to get employee detail by id


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_by_id_response = peoplehr.employee.get_detail_by_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to GetEmployeeDetailById

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to get employee detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetEmployeeDetailByIdParameter`](./people_hr_python_sdk/type/get_employee_detail_by_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetEmployeeDetailById`](./people_hr_python_sdk/pydantic/error_for_get_employee_detail_by_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  GetEmployeeDetailById` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.list_employee_detail`<a id="peoplehremployeelist_employee_detail"></a>

This API is used to get employee detail list. Please note the History fields have been deprecated and will not return any data. To retrieve History data the individual employee record needs to be retrieved using the GetEmployeeDetail method call, this will return the History data.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_detail_response = peoplehr.employee.list_employee_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    include_leavers="false",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for GetAllEmployeeDetail

##### action: `str`<a id="action-str"></a>

Action default value

##### include_leavers: [`IncludeLeavers`](./people_hr_python_sdk/type/include_leavers.py)<a id="include_leavers-includeleaverspeople_hr_python_sdktypeinclude_leaverspy"></a>

Include leavers for get all employee detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAllEmployeeDetailParameter`](./people_hr_python_sdk/type/get_all_employee_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAllEmployeeDetail`](./people_hr_python_sdk/pydantic/error_for_get_all_employee_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  GetAllEmployeeDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.update_detail`<a id="peoplehremployeeupdate_detail"></a>

This API is used to update employee details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_detail_response = peoplehr.employee.update_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    reason_for_change="Reason for change",
    employee_id="PW180",
    first_name="Ranjit",
    last_name="Johnson",
    gender="true",
    start_date="2016-07-27",
    reports_to_effective_date="2014-01-01",
    company_effective_date="2014-01-01",
    job_role="Software Enginner",
    job_role_effective_date="2014-01-01",
    location="Mumbai",
    location_effective_date="2014-01-01",
    department="IT",
    department_effective_date="2014-01-01",
    employment_type_effective_date="2014-01-01",
    title="Mr.",
    email="vaibhavid@itgurussoftware.com",
    date_of_birth="1999-01-02",
    reports_to="firstname.lastname@itgurusssoftware.com",
    company="Company name",
    national_insurance_number="AAAAAAAAAAAAAAAAAAA",
    nationality="Indian",
    employment_type="Full time",
    address="Shiv Colony, Thergaon - Pune",
    personal_phone_number="999890988772",
    payroll_company="Your payroll company's name ",
    payroll_id="Your Payroll ID",
    time__attendance_id="Your Time & Attendance ID",
    rota_id="Your Rota ID",
    crm_id="Your CRM ID",
    ats_id="Your ATS ID",
    performance_id="Your Performance ID",
    benefits_id="Your Benefits ID",
    system1_id="Your System One ID",
    system2_id="Your System Two ID",
    system3_id="Your System Three ID",
    api_column1="APIColumn1 Value",
    api_column2="APIColumn2 Value",
    api_column3="APIColumn3 Value",
    api_column4="APIColumn4 Value",
    api_column5="APIColumn5 Value",
    personal_email="abc@itgurussoftware.com",
    method_of_recruitment="Method Of Recruitment",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to updateEmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### reason_for_change: [`ReasonForChange`](./people_hr_python_sdk/type/reason_for_change.py)<a id="reason_for_change-reasonforchangepeople_hr_python_sdktypereason_for_changepy"></a>

Reason for change employee id

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update employee data

##### first_name: [`FirstName`](./people_hr_python_sdk/type/first_name.py)<a id="first_name-firstnamepeople_hr_python_sdktypefirst_namepy"></a>

FirstName for update employee data

##### last_name: [`LastName`](./people_hr_python_sdk/type/last_name.py)<a id="last_name-lastnamepeople_hr_python_sdktypelast_namepy"></a>

LastName for update employee data

##### gender: [`Gender`](./people_hr_python_sdk/type/gender.py)<a id="gender-genderpeople_hr_python_sdktypegenderpy"></a>

Gender value for update employee data

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### reports_to_effective_date: `date`<a id="reports_to_effective_date-date"></a>

ReportsToEffectiveDate default value 

##### company_effective_date: `date`<a id="company_effective_date-date"></a>

CompanyEffectiveDate default value 

##### job_role: [`JobRole`](./people_hr_python_sdk/type/job_role.py)<a id="job_role-jobrolepeople_hr_python_sdktypejob_rolepy"></a>

Job role for update employee data

##### job_role_effective_date: `date`<a id="job_role_effective_date-date"></a>

JobRoleEffectiveDate default value 

##### location: `str`<a id="location-str"></a>

Location default value 

##### location_effective_date: `date`<a id="location_effective_date-date"></a>

LocationEffectiveDate default value 

##### department: `str`<a id="department-str"></a>

Department default value 

##### department_effective_date: `date`<a id="department_effective_date-date"></a>

DepartmentEffectiveDate default value 

##### employment_type_effective_date: `date`<a id="employment_type_effective_date-date"></a>

EmploymentTypeEffectiveDate default value 

##### title: [`Title`](./people_hr_python_sdk/type/title.py)<a id="title-titlepeople_hr_python_sdktypetitlepy"></a>

Title for update employee data

##### email: [`Email`](./people_hr_python_sdk/type/email.py)<a id="email-emailpeople_hr_python_sdktypeemailpy"></a>

Email for update employee data

##### date_of_birth: `date`<a id="date_of_birth-date"></a>

DateOfBirth default value 

##### reports_to: [`ReportsTo`](./people_hr_python_sdk/type/reports_to.py)<a id="reports_to-reportstopeople_hr_python_sdktypereports_topy"></a>

Reports To for update employee data

##### company: [`Company`](./people_hr_python_sdk/type/company.py)<a id="company-companypeople_hr_python_sdktypecompanypy"></a>

Company name for update employee data

##### national_insurance_number: [`NationalInsuranceNumber`](./people_hr_python_sdk/type/national_insurance_number.py)<a id="national_insurance_number-nationalinsurancenumberpeople_hr_python_sdktypenational_insurance_numberpy"></a>

National insurance number for update employee data

##### nationality: [`Nationality`](./people_hr_python_sdk/type/nationality.py)<a id="nationality-nationalitypeople_hr_python_sdktypenationalitypy"></a>

Nationality for update employee data

##### employment_type: [`EmploymentType`](./people_hr_python_sdk/type/employment_type.py)<a id="employment_type-employmenttypepeople_hr_python_sdktypeemployment_typepy"></a>

Employment type for update employee data

##### address: `str`<a id="address-str"></a>

Address default value 

##### personal_phone_number: [`PersonalPhoneNumber`](./people_hr_python_sdk/type/personal_phone_number.py)<a id="personal_phone_number-personalphonenumberpeople_hr_python_sdktypepersonal_phone_numberpy"></a>

PersonalPhoneNumber for update employee data

##### payroll_company: [`PayrollCompany`](./people_hr_python_sdk/type/payroll_company.py)<a id="payroll_company-payrollcompanypeople_hr_python_sdktypepayroll_companypy"></a>

Payroll company for update employee data

##### payroll_id: [`PayrollID`](./people_hr_python_sdk/type/payroll_id.py)<a id="payroll_id-payrollidpeople_hr_python_sdktypepayroll_idpy"></a>

Payroll id for update employee data

##### time__attendance_id: [`TimeAttendanceID`](./people_hr_python_sdk/type/time_attendance_id.py)<a id="time__attendance_id-timeattendanceidpeople_hr_python_sdktypetime_attendance_idpy"></a>

Time & attendance id for update employee data

##### rota_id: [`RotaID`](./people_hr_python_sdk/type/rota_id.py)<a id="rota_id-rotaidpeople_hr_python_sdktyperota_idpy"></a>

Rota id for update employee data

##### crm_id: [`CRMID`](./people_hr_python_sdk/type/crmid.py)<a id="crm_id-crmidpeople_hr_python_sdktypecrmidpy"></a>

CRM id for update employee data

##### ats_id: [`ATSID`](./people_hr_python_sdk/type/atsid.py)<a id="ats_id-atsidpeople_hr_python_sdktypeatsidpy"></a>

ATS id for update employee data

##### performance_id: [`PerformanceID`](./people_hr_python_sdk/type/performance_id.py)<a id="performance_id-performanceidpeople_hr_python_sdktypeperformance_idpy"></a>

Performance id for update employee data

##### benefits_id: [`BenefitsID`](./people_hr_python_sdk/type/benefits_id.py)<a id="benefits_id-benefitsidpeople_hr_python_sdktypebenefits_idpy"></a>

Benefits id for update employee data

##### system1_id: [`System1ID`](./people_hr_python_sdk/type/system1_id.py)<a id="system1_id-system1idpeople_hr_python_sdktypesystem1_idpy"></a>

System1 id for update employee data\\\"

##### system2_id: [`System2ID`](./people_hr_python_sdk/type/system2_id.py)<a id="system2_id-system2idpeople_hr_python_sdktypesystem2_idpy"></a>

System2 id for update employee data\\\"

##### system3_id: [`System3ID`](./people_hr_python_sdk/type/system3_id.py)<a id="system3_id-system3idpeople_hr_python_sdktypesystem3_idpy"></a>

System3 id for update employee data\\\"

##### api_column1: `str`<a id="api_column1-str"></a>

APIColumn1 default value 

##### api_column2: `str`<a id="api_column2-str"></a>

APIColumn2 default value 

##### api_column3: `str`<a id="api_column3-str"></a>

APIColumn3 default value 

##### api_column4: `str`<a id="api_column4-str"></a>

APIColumn4 default value 

##### api_column5: `str`<a id="api_column5-str"></a>

APIColumn5 default value 

##### personal_email: [`PersonalEmail`](./people_hr_python_sdk/type/personal_email.py)<a id="personal_email-personalemailpeople_hr_python_sdktypepersonal_emailpy"></a>

Personal email for update employee data\\\"

##### method_of_recruitment: [`MethodOfRecruitment`](./people_hr_python_sdk/type/method_of_recruitment.py)<a id="method_of_recruitment-methodofrecruitmentpeople_hr_python_sdktypemethod_of_recruitmentpy"></a>

Method of recruitment for update employee data\\\"

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeDetail3`](./people_hr_python_sdk/type/update_employee_detail3.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateEmployeeDetail`](./people_hr_python_sdk/pydantic/error_for_update_employee_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  UpdateEmployeeDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.update_employee_id_details`<a id="peoplehremployeeupdate_employee_id_details"></a>

This API is used to update employee id details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employee_id_details_response = peoplehr.employee.update_employee_id_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    reason_for_change="Reason for change",
    old_employee_id="PW1",
    new_employee_id="PW2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to updateEmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### reason_for_change: [`ReasonForChange`](./people_hr_python_sdk/type/reason_for_change.py)<a id="reason_for_change-reasonforchangepeople_hr_python_sdktypereason_for_changepy"></a>

Reason for change employee id

##### old_employee_id: [`OldEmployeeId`](./people_hr_python_sdk/type/old_employee_id.py)<a id="old_employee_id-oldemployeeidpeople_hr_python_sdktypeold_employee_idpy"></a>

Old employee id for update employee data

##### new_employee_id: [`NewEmployeeId`](./people_hr_python_sdk/type/new_employee_id.py)<a id="new_employee_id-newemployeeidpeople_hr_python_sdktypenew_employee_idpy"></a>

New employee id for update employee data

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeId2`](./people_hr_python_sdk/type/update_employee_id2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateEmployeeId`](./people_hr_python_sdk/pydantic/error_for_update_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  UpdateEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee.update_leaver_status_by_id`<a id="peoplehremployeeupdate_leaver_status_by_id"></a>

This API is used to update/mark employee leaver status by id


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_leaver_status_by_id_response = peoplehr.employee.update_leaver_status_by_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    reasonfor_leaving="Reason for leaving employee",
    final_employment_date="2014-01-02",
    additional_comments="Additional comments",
    final_working_date="2014-01-02",
    markas_leaver_immediately=False,
    reports_to="firstname.lastname@itgurusssoftware.com",
    re_employable="false",
    supporting_comments="xyzfgfdgd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to markAsLeaverById

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for mark as leaver by id

##### reasonfor_leaving: `str`<a id="reasonfor_leaving-str"></a>

ReasonforLeaving default value 

##### final_employment_date: `date`<a id="final_employment_date-date"></a>

FinalEmploymentDate default value 

##### additional_comments: [`AdditionalComments`](./people_hr_python_sdk/type/additional_comments.py)<a id="additional_comments-additionalcommentspeople_hr_python_sdktypeadditional_commentspy"></a>

Additional comments for mark as leaver by id

##### final_working_date: `str`<a id="final_working_date-str"></a>

FinalWorkingDate default value 

##### markas_leaver_immediately: `bool`<a id="markas_leaver_immediately-bool"></a>

MarkasLeaverImmediately default value 

##### reports_to: [`ReportsTo`](./people_hr_python_sdk/type/reports_to.py)<a id="reports_to-reportstopeople_hr_python_sdktypereports_topy"></a>

Reports to for mark as leaver by id

##### re_employable: `str`<a id="re_employable-str"></a>

ReEmployable default value 

##### supporting_comments: [`SupportingComments`](./people_hr_python_sdk/type/supporting_comments.py)<a id="supporting_comments-supportingcommentspeople_hr_python_sdktypesupporting_commentspy"></a>

Supporting comments for mark as leaver by id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MarkAsLeaverById2`](./people_hr_python_sdk/type/mark_as_leaver_by_id2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForMarkAsLeaverById`](./people_hr_python_sdk/pydantic/error_for_mark_as_leaver_by_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee  -  MarkAsLeaverById` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_absence.create_new_absence`<a id="peoplehremployee_absencecreate_new_absence"></a>

This API is used to add absence for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_absence_response = peoplehr.employee_absence.create_new_absence(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    duration_type=1,
    reason="Resaon here",
    start_date="2016-07-27",
    end_date="2017-07-27",
    part_of_day="AM",
    duration=1,
    absence_paid_status=1,
    emergency_leave="true",
    add_comments=[
        {
            "comment": "Comment goes here",
        }
    ],
    add_files=[
        {
            "document_name": "bird1.png",
            "file": "pass base64 string",
            "description": "Something write here",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to checkAuthentication

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for add new absence

##### duration_type: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="duration_type-bytepeople_hr_python_sdktypebytepy"></a>

Duration type default value 

##### reason: `str`<a id="reason-str"></a>

Duration Default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### part_of_day: [`PartOfDay`](./people_hr_python_sdk/type/part_of_day.py)<a id="part_of_day-partofdaypeople_hr_python_sdktypepart_of_daypy"></a>

PartOfDay for add new absence

##### duration: `int`<a id="duration-int"></a>

Duration Default value 

##### absence_paid_status: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="absence_paid_status-bytepeople_hr_python_sdktypebytepy"></a>

AbsencePaidStatus default value 

##### emergency_leave: [`EmergencyLeave`](./people_hr_python_sdk/type/emergency_leave.py)<a id="emergency_leave-emergencyleavepeople_hr_python_sdktypeemergency_leavepy"></a>

EmergencyLeave for add new absence

##### add_comments: [`AddCommentsArrayForAbsence`](./people_hr_python_sdk/type/add_comments_array_for_absence.py)<a id="add_comments-addcommentsarrayforabsencepeople_hr_python_sdktypeadd_comments_array_for_absencepy"></a>

AddComments array list

##### add_files: [`AddFilesArrayForAbsence`](./people_hr_python_sdk/type/add_files_array_for_absence.py)<a id="add_files-addfilesarrayforabsencepeople_hr_python_sdktypeadd_files_array_for_absencepy"></a>

AddFiles array list

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddAbsenceOfEmployeeParameter`](./people_hr_python_sdk/type/add_absence_of_employee_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddEmployeeAbsence`](./people_hr_python_sdk/pydantic/error_for_add_employee_absence.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAbsence  -  AddAbsence` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_absence.get_detail`<a id="peoplehremployee_absenceget_detail"></a>

This API is used to employee absence details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = peoplehr.employee_absence.get_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to GetAbsenceDetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

 Employee id for get absence detail

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAbsenceDetailParameter`](./people_hr_python_sdk/type/get_absence_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAbsenceDetail`](./people_hr_python_sdk/pydantic/error_for_get_absence_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAbsence  -  GetAbsenceDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_absence.remove_absence`<a id="peoplehremployee_absenceremove_absence"></a>

This API is used to delete absence  for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_absence_response = peoplehr.employee_absence.remove_absence(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to delete absence

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for delete absence

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteAbsenceOfEmployeeParameter`](./people_hr_python_sdk/type/delete_absence_of_employee_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForEmployeeAbsenceDelete`](./people_hr_python_sdk/pydantic/error_for_employee_absence_delete.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAbsence  -  DeleteAbsence` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_absence.update_absence_record`<a id="peoplehremployee_absenceupdate_absence_record"></a>

This API is used to update absence  for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_absence_record_response = peoplehr.employee_absence.update_absence_record(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    old_start_date="2017-07-18",
    old_end_date="2017-07-18",
    duration_type=1,
    reason="Resaon here",
    start_date="2016-07-27",
    end_date="2017-07-27",
    duration=1,
    absence_paid_status=1,
    emergency_leave="true",
    part_of_day="true",
    add_comments=[
        {
            "comment": "Comment goes here",
        }
    ],
    add_files=[
        {
            "document_name": "bird1.png",
            "file": "pass base64 string",
            "description": "Something write here",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to UpdateAbsence

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for update absence

##### old_start_date: `date`<a id="old_start_date-date"></a>

Old start date default value 

##### old_end_date: `date`<a id="old_end_date-date"></a>

Old end date default value 

##### duration_type: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="duration_type-bytepeople_hr_python_sdktypebytepy"></a>

Duration type default value 

##### reason: `str`<a id="reason-str"></a>

Duration Default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### duration: `int`<a id="duration-int"></a>

Duration Default value 

##### absence_paid_status: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="absence_paid_status-bytepeople_hr_python_sdktypebytepy"></a>

AbsencePaidStatus default value 

##### emergency_leave: [`EmergencyLeave`](./people_hr_python_sdk/type/emergency_leave.py)<a id="emergency_leave-emergencyleavepeople_hr_python_sdktypeemergency_leavepy"></a>

EmergencyLeave for update absence

##### part_of_day: [`PartOfDayForUpdateAbsence`](./people_hr_python_sdk/type/part_of_day_for_update_absence.py)<a id="part_of_day-partofdayforupdateabsencepeople_hr_python_sdktypepart_of_day_for_update_absencepy"></a>

PartOfDay for update absence

##### add_comments: [`AddCommentsArrayForAbsence`](./people_hr_python_sdk/type/add_comments_array_for_absence.py)<a id="add_comments-addcommentsarrayforabsencepeople_hr_python_sdktypeadd_comments_array_for_absencepy"></a>

AddComments array list

##### add_files: [`AddFilesArrayForAbsence`](./people_hr_python_sdk/type/add_files_array_for_absence.py)<a id="add_files-addfilesarrayforabsencepeople_hr_python_sdktypeadd_files_array_for_absencepy"></a>

AddFiles array list

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateAbsenceDetailParameter`](./people_hr_python_sdk/type/update_absence_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateAbsenceDetails`](./people_hr_python_sdk/pydantic/error_for_update_absence_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAbsence  -  UpdateAbsence` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_appraisal.create_new_appraisal`<a id="peoplehremployee_appraisalcreate_new_appraisal"></a>

This API is used to add new appraisal for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_appraisal_response = peoplehr.employee_appraisal.create_new_appraisal(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    appraisal_review_date="2017-05-01",
    reviewer="rajendra.petave@itgurussoftware.com",
    notes="notes goes here",
    action_plan="11",
    objectives="121",
    custom_columns=[
        {
            "column_name": "123.pdf",
            "column_value": "asddds",
        }
    ],
    add_files=[
        {
            "document_name": "123.pdf",
            "file": "pass base64 string",
            "description": "dsadsadasdasd",
            "document_category": "catagory",
            "signature_required": "false",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to AddNewAppraisal

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add new appraisal

##### appraisal_review_date: `date`<a id="appraisal_review_date-date"></a>

AppraisalReviewDate Default value 

##### reviewer: `str`<a id="reviewer-str"></a>

Reviewer value 

##### notes: `str`<a id="notes-str"></a>

##### action_plan: `str`<a id="action_plan-str"></a>

##### objectives: `str`<a id="objectives-str"></a>

##### custom_columns: [`CustomColumnsArrayForAddNewAppraisal`](./people_hr_python_sdk/type/custom_columns_array_for_add_new_appraisal.py)<a id="custom_columns-customcolumnsarrayforaddnewappraisalpeople_hr_python_sdktypecustom_columns_array_for_add_new_appraisalpy"></a>

Custom columns

##### add_files: [`AddFilesArrayForAddNewAppraisal`](./people_hr_python_sdk/type/add_files_array_for_add_new_appraisal.py)<a id="add_files-addfilesarrayforaddnewappraisalpeople_hr_python_sdktypeadd_files_array_for_add_new_appraisalpy"></a>

Add Files info.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewAppraisalParameter`](./people_hr_python_sdk/type/add_new_appraisal_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewAppraisal`](./people_hr_python_sdk/pydantic/error_for_add_new_appraisal.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAppraisal  -  AddNewAppraisal` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_appraisal.delete_appraisal`<a id="peoplehremployee_appraisaldelete_appraisal"></a>

This API is used to Delete Appraisal for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_appraisal_response = peoplehr.employee_appraisal.delete_appraisal(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    appraisal_id=383,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to DeleteAppraisal

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for delete appraisal

##### appraisal_id: `int`<a id="appraisal_id-int"></a>

Appraisal id  default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteAppraisalParameter`](./people_hr_python_sdk/type/delete_appraisal_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteAppraisal`](./people_hr_python_sdk/pydantic/error_for_delete_appraisal.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAppraisal  -  DeleteAppraisal` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_appraisal.get_by_appraisal_id`<a id="peoplehremployee_appraisalget_by_appraisal_id"></a>

This API is used to Get By Appraisal Id  details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_appraisal_id_response = peoplehr.employee_appraisal.get_by_appraisal_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    appraisal_id=383,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to GetByAppraisalId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

 Employee id for get by appraisal id

##### appraisal_id: `int`<a id="appraisal_id-int"></a>

Appraisal id  default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetByAppraisalIdForEmployeeAppraisal`](./people_hr_python_sdk/type/get_by_appraisal_id_for_employee_appraisal.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetByAppraisalId`](./people_hr_python_sdk/pydantic/error_for_get_by_appraisal_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAppraisal  -  GetByAppraisalId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_appraisal.get_by_employee_id`<a id="peoplehremployee_appraisalget_by_employee_id"></a>

This API is used to Get By Employee Id Appraisal details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = peoplehr.employee_appraisal.get_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to GetByEmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

 Employee id for get by employee id

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetByEmployeeIdForEmployeeAppraisal`](./people_hr_python_sdk/type/get_by_employee_id_for_employee_appraisal.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForEmployeeAppraisalGetEmployeeById`](./people_hr_python_sdk/pydantic/error_for_employee_appraisal_get_employee_by_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAppraisal  -  GetByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_appraisal.update_user_appraisal`<a id="peoplehremployee_appraisalupdate_user_appraisal"></a>

This API is used to Update Appraisal for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_appraisal_response = peoplehr.employee_appraisal.update_user_appraisal(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    appraisal_review_date="2017-05-01",
    reviewer="rajendra.petave@itgurussoftware.com",
    notes="notes goes here",
    action_plan="11",
    objectives="121",
    custom_columns=[
        {
            "column_name": "123.pdf",
            "column_value": "adsdsd",
        }
    ],
    add_files=[
        {
            "document_name": "123.pdf",
            "file": "pass base64 string",
            "description": "dsadsadasdasd",
            "document_category": "catagory",
            "signature_required": "true",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to UpdateAppraisal

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for update appraisal

##### appraisal_review_date: `date`<a id="appraisal_review_date-date"></a>

AppraisalReviewDate Default value 

##### reviewer: `str`<a id="reviewer-str"></a>

Reviewer value 

##### notes: `str`<a id="notes-str"></a>

##### action_plan: `str`<a id="action_plan-str"></a>

##### objectives: `str`<a id="objectives-str"></a>

##### custom_columns: [`CustomColumnsArrayForUpdateAppraisal`](./people_hr_python_sdk/type/custom_columns_array_for_update_appraisal.py)<a id="custom_columns-customcolumnsarrayforupdateappraisalpeople_hr_python_sdktypecustom_columns_array_for_update_appraisalpy"></a>

Custom Columns of user

##### add_files: [`AddFilesArrayForUpdateAppraisal`](./people_hr_python_sdk/type/add_files_array_for_update_appraisal.py)<a id="add_files-addfilesarrayforupdateappraisalpeople_hr_python_sdktypeadd_files_array_for_update_appraisalpy"></a>

Add Files Info.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateAppraisalParameter`](./people_hr_python_sdk/type/update_appraisal_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateAppraisal`](./people_hr_python_sdk/pydantic/error_for_update_appraisal.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeAppraisal  -  UpdateAppraisal` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_benefit.create_new_benefit`<a id="peoplehremployee_benefitcreate_new_benefit"></a>

This API is used to Add new benefit details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_benefit_response = peoplehr.employee_benefit.create_new_benefit(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    benefit="Date Awarded",
    date_awarded=2017-05-05,
    expiry_date="2018-07-07",
    recover_on_termination="true",
    custom_columns=[
        {
            "column_name": "abc",
            "column_value": "",
        }
    ],
    add_files=[
        {
            "document_name": "123.png",
            "file": "pass base64 string",
            "description": "dsadsadasdasd",
            "document_category": "catagory",
            "signature_required": "true",
        }
    ],
    value="1000.10",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to AddNewBenefit

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for add new benefit

##### benefit: `str`<a id="benefit-str"></a>

Benefit default value

##### date_awarded: [`String`](./people_hr_python_sdk/type/string.py)<a id="date_awarded-stringpeople_hr_python_sdktypestringpy"></a>

Date awarded default value

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### recover_on_termination: [`RecoverOnTermination`](./people_hr_python_sdk/type/recover_on_termination.py)<a id="recover_on_termination-recoveronterminationpeople_hr_python_sdktyperecover_on_terminationpy"></a>

RecoverOnTermination for add new benefit

##### custom_columns: [`CustomColumnsArrayForAddNewBenefit`](./people_hr_python_sdk/type/custom_columns_array_for_add_new_benefit.py)<a id="custom_columns-customcolumnsarrayforaddnewbenefitpeople_hr_python_sdktypecustom_columns_array_for_add_new_benefitpy"></a>

CustomColumns value

##### add_files: [`AddFilesArrayForAddNewBenefit`](./people_hr_python_sdk/type/add_files_array_for_add_new_benefit.py)<a id="add_files-addfilesarrayforaddnewbenefitpeople_hr_python_sdktypeadd_files_array_for_add_new_benefitpy"></a>

AddFiles contain file info.

##### value: `str`<a id="value-str"></a>

Value default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewBenefitParameter`](./people_hr_python_sdk/type/add_new_benefit_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewBenefitApi`](./people_hr_python_sdk/pydantic/error_for_add_new_benefit_api.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeBenefit  -  AddNewBenefit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_benefit.delete_benefit`<a id="peoplehremployee_benefitdelete_benefit"></a>

This API is used to Delete Benefit Details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_benefit_response = peoplehr.employee_benefit.delete_benefit(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    benefit_id=382,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to DeleteBenefit

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for delete benefit

##### benefit_id: `int`<a id="benefit_id-int"></a>

Benefit id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteBenefitParameter`](./people_hr_python_sdk/type/delete_benefit_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteBenefit`](./people_hr_python_sdk/pydantic/error_for_delete_benefit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeBenefit  -  DeleteBenefit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_benefit.get_by_benefit_id_details`<a id="peoplehremployee_benefitget_by_benefit_id_details"></a>

This API is used to get by  benefit id details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_benefit_id_details_response = peoplehr.employee_benefit.get_by_benefit_id_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    benefit_id=382,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to GetBenefitByBenefitId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for get benefit by benefit id

##### benefit_id: `int`<a id="benefit_id-int"></a>

Benefit id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetByBenefitIdParameter`](./people_hr_python_sdk/type/get_by_benefit_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetByBenefitIdApi`](./people_hr_python_sdk/pydantic/error_for_get_by_benefit_id_api.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeBenefit  -  GetBenefitByBenefitId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_benefit.get_by_employee_id_details`<a id="peoplehremployee_benefitget_by_employee_id_details"></a>

This API is used to get by employee id details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_details_response = peoplehr.employee_benefit.get_by_employee_id_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to GetBenefitByEmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for get benefit by employee id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetBenefitByEmployeeIdParameter`](./people_hr_python_sdk/type/get_benefit_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetBenefitByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_benefit_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeBenefit  -  GetBenefitByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_benefit.update_details`<a id="peoplehremployee_benefitupdate_details"></a>

This API is used to Update Benefit Details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = peoplehr.employee_benefit.update_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    benefit="Date Awarded",
    benefit_id=382,
    date_awarded=2017-05-05,
    recover_on_termination="true",
    expiry_date="2018-07-07",
    value="1000.10",
    custom_columns=[
        {
            "column_name": "abc",
            "column_value": "",
        }
    ],
    add_files=[
        {
            "document_name": "123.png",
            "file": "pass base64 string",
            "description": "dsadsadasdasd",
            "document_category": "catagory",
            "signature_required": "true",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to UpdateBenefit

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for update benefit

##### benefit: `str`<a id="benefit-str"></a>

Benefit default value

##### benefit_id: `int`<a id="benefit_id-int"></a>

Benefit id default value

##### date_awarded: [`String`](./people_hr_python_sdk/type/string.py)<a id="date_awarded-stringpeople_hr_python_sdktypestringpy"></a>

Date awarded default value

##### recover_on_termination: [`RecoverOnTermination`](./people_hr_python_sdk/type/recover_on_termination.py)<a id="recover_on_termination-recoveronterminationpeople_hr_python_sdktyperecover_on_terminationpy"></a>

RecoverOnTermination for update benefit

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### value: `str`<a id="value-str"></a>

Value default value

##### custom_columns: [`CustomColumnsArrayForAddNewBenefit`](./people_hr_python_sdk/type/custom_columns_array_for_add_new_benefit.py)<a id="custom_columns-customcolumnsarrayforaddnewbenefitpeople_hr_python_sdktypecustom_columns_array_for_add_new_benefitpy"></a>

CustomColumns contain column name and column value

##### add_files: [`AddFilesArrayForUpdateBenefit`](./people_hr_python_sdk/type/add_files_array_for_update_benefit.py)<a id="add_files-addfilesarrayforupdatebenefitpeople_hr_python_sdktypeadd_files_array_for_update_benefitpy"></a>

AddFiles contain file info.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateBenefitParameter`](./people_hr_python_sdk/type/update_benefit_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateBenefitApi`](./people_hr_python_sdk/pydantic/error_for_update_benefit_api.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeBenefit  -  UpdateBenefit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_cpd.create_new_cpd`<a id="peoplehremployee_cpdcreate_new_cpd"></a>

This API is used to add new CPD for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_cpd_response = peoplehr.employee_cpd.create_new_cpd(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    activity="Activity name",
    start_date="2016-07-27",
    custom_columns=[
        {
            "column_name": "Column_Name",
            "column_value": "29153",
        }
    ],
    add_files=[
        {
            "document_name": "DocumentName.pdf",
            "file": "Base64 Data",
            "description": "Description goes here",
            "document_category": "Benefit",
            "signature_required": "false",
        }
    ],
    end_date="2017-07-27",
    roll_number="45",
    date_admitted="2017-01-01",
    hours_required=20,
    hours_accredited=21,
    notes="notes goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to add CPD detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for add new CPD

##### activity: `str`<a id="activity-str"></a>

Activity default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### custom_columns: [`CustomColumnsArrayForEmployeeCPD`](./people_hr_python_sdk/type/custom_columns_array_for_employee_cpd.py)<a id="custom_columns-customcolumnsarrayforemployeecpdpeople_hr_python_sdktypecustom_columns_array_for_employee_cpdpy"></a>

CustomColumns for add new cpd

##### add_files: [`AddFilesArrayForEmployeeCPD`](./people_hr_python_sdk/type/add_files_array_for_employee_cpd.py)<a id="add_files-addfilesarrayforemployeecpdpeople_hr_python_sdktypeadd_files_array_for_employee_cpdpy"></a>

AddFiles for add new cpd

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### roll_number: `str`<a id="roll_number-str"></a>

Roll number default value 

##### date_admitted: `date`<a id="date_admitted-date"></a>

Date admitted default value 

##### hours_required: `int`<a id="hours_required-int"></a>

Hours required default value 

##### hours_accredited: `int`<a id="hours_accredited-int"></a>

Hours accredited default value 

##### notes: `str`<a id="notes-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddnewCPDParameter`](./people_hr_python_sdk/type/addnew_cpd_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewCPD`](./people_hr_python_sdk/pydantic/error_for_add_new_cpd.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee CPD  -  AddNewCPD` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_cpd.delete_cpd`<a id="peoplehremployee_cpddelete_cpd"></a>

This API is used to delete CPD for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_cpd_response = peoplehr.employee_cpd.delete_cpd(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    cpdid=148,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to delete CPD detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for delete CPD

##### cpdid: `int`<a id="cpdid-int"></a>

CPDId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteCPDParameter`](./people_hr_python_sdk/type/delete_cpd_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteCPD`](./people_hr_python_sdk/pydantic/error_for_delete_cpd.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee CPD  -  DeleteCPD` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_cpd.get_by_cpd_id`<a id="peoplehremployee_cpdget_by_cpd_id"></a>

This API is used to Get By CPDId for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_cpd_id_response = peoplehr.employee_cpd.get_by_cpd_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    cpdid=148,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get by cpd id

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get by cpd id

##### cpdid: `int`<a id="cpdid-int"></a>

CPDId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetByCPDIdParameter`](./people_hr_python_sdk/type/get_by_cpdid_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetByCPDId`](./people_hr_python_sdk/pydantic/error_for_get_by_cpdid.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee CPD  -  GetByCPDId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_cpd.get_by_employee_id`<a id="peoplehremployee_cpdget_by_employee_id"></a>

This API is used to Get CPD By EmployeeId for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = peoplehr.employee_cpd.get_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get cpd by employee id

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get cpd by employee id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetCPDByEmployeeIdParameter`](./people_hr_python_sdk/type/get_cpdby_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetCPDByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_cpdby_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee CPD  -  GetCPDByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_cpd.update_cpd`<a id="peoplehremployee_cpdupdate_cpd"></a>

This API is used to update CPD for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_cpd_response = peoplehr.employee_cpd.update_cpd(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    cpdid=148,
    activity="Activity name",
    start_date="2016-07-27",
    end_date="2017-07-27",
    roll_number="45",
    date_admitted="2017-01-01",
    hours_required=20,
    hours_accredited=21,
    notes="notes goes here",
    custom_columns=[
        {
            "column_name": "Column_Name",
            "column_value": "29153",
        }
    ],
    add_files=[
        {
            "document_name": "DocumentName.pdf",
            "file": "Base64 Data",
            "description": "Description goes here",
            "document_category": "Benefit",
            "signature_required": "false",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to update CPD detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for update CPD

##### cpdid: `int`<a id="cpdid-int"></a>

CPDId default value 

##### activity: `str`<a id="activity-str"></a>

Activity default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### roll_number: `str`<a id="roll_number-str"></a>

Roll number default value 

##### date_admitted: `date`<a id="date_admitted-date"></a>

Date admitted default value 

##### hours_required: `int`<a id="hours_required-int"></a>

Hours required default value 

##### hours_accredited: `int`<a id="hours_accredited-int"></a>

Hours accredited default value 

##### notes: `str`<a id="notes-str"></a>

##### custom_columns: [`CustomColumnsArrayForEmployeeCPD`](./people_hr_python_sdk/type/custom_columns_array_for_employee_cpd.py)<a id="custom_columns-customcolumnsarrayforemployeecpdpeople_hr_python_sdktypecustom_columns_array_for_employee_cpdpy"></a>

CustomColumns for update CPD

##### add_files: [`AddFilesArrayForEmployeeCPD`](./people_hr_python_sdk/type/add_files_array_for_employee_cpd.py)<a id="add_files-addfilesarrayforemployeecpdpeople_hr_python_sdktypeadd_files_array_for_employee_cpdpy"></a>

AddFiles for update CPD

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCPDParameter`](./people_hr_python_sdk/type/update_cpd_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateCPD`](./people_hr_python_sdk/pydantic/error_for_update_cpd.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee CPD  -  UpdateCPD` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_custom_screen.add_new_custom_screen_transaction`<a id="peoplehremployee_custom_screenadd_new_custom_screen_transaction"></a>

This API is used to add new custom screen transaction details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_custom_screen_transaction_response = peoplehr.employee_custom_screen.add_new_custom_screen_transaction(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    screen_id=123,
    custom_columns=[
        {
            "column_name": "Column 1 Name",
            "column_value": "Abcd",
        }
    ],
    add_files=[
        {
            "document_name": "123.pdf",
            "file": "Pass base64 string",
            "description": "File description",
            "document_category": "Custom Category",
            "signature_required": "false",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee custom screen api to AddNewCustomScreenTransaction

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for add new custom screen transaction

##### screen_id: `int`<a id="screen_id-int"></a>

Screen Id value

##### custom_columns: [`CustomColumnsForEmployeeCustomScreenObject`](./people_hr_python_sdk/type/custom_columns_for_employee_custom_screen_object.py)<a id="custom_columns-customcolumnsforemployeecustomscreenobjectpeople_hr_python_sdktypecustom_columns_for_employee_custom_screen_objectpy"></a>

CustomColumns for add new custom screen transaction

##### add_files: [`AddFilesForEmployeeCustomScreenObject`](./people_hr_python_sdk/type/add_files_for_employee_custom_screen_object.py)<a id="add_files-addfilesforemployeecustomscreenobjectpeople_hr_python_sdktypeadd_files_for_employee_custom_screen_objectpy"></a>

AddFiles for add new custom screen transaction

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewCustomScreenTransactionParameter`](./people_hr_python_sdk/type/add_new_custom_screen_transaction_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewCustomScreenTransaction`](./people_hr_python_sdk/pydantic/error_for_add_new_custom_screen_transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Custom Screen  -  AddNewCustomScreenTransaction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_custom_screen.delete_custom_screen_transaction`<a id="peoplehremployee_custom_screendelete_custom_screen_transaction"></a>

This API is used to delete custom screen transaction details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_custom_screen_transaction_response = peoplehr.employee_custom_screen.delete_custom_screen_transaction(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    screen_id=123,
    custom_screen_transaction_id=12345,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee custom screen api to DeleteCustomScreenTransaction

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for delete custom screen transaction

##### screen_id: `int`<a id="screen_id-int"></a>

Screen Id value

##### custom_screen_transaction_id: `int`<a id="custom_screen_transaction_id-int"></a>

Custom Screen Transaction Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteCustomScreenTransactionParameter`](./people_hr_python_sdk/type/delete_custom_screen_transaction_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteCustomScreenTransaction`](./people_hr_python_sdk/pydantic/error_for_delete_custom_screen_transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Custom Screen  -  DeleteCustomScreenTransaction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_custom_screen.get_by_custom_screen_transaction`<a id="peoplehremployee_custom_screenget_by_custom_screen_transaction"></a>

This API is used to get by custom screen transaction id detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_custom_screen_transaction_response = peoplehr.employee_custom_screen.get_by_custom_screen_transaction(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    screen_id=123,
    custom_screen_transaction_id=12345,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee custom screen api to GetByCustomScreenTransactionId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for employee custom screen

##### screen_id: `int`<a id="screen_id-int"></a>

Screen Id value

##### custom_screen_transaction_id: `int`<a id="custom_screen_transaction_id-int"></a>

Custom Screen Transaction Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetByCustomScreenTransactionIdParameter`](./people_hr_python_sdk/type/get_by_custom_screen_transaction_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetByCustomScreenTransactionId`](./people_hr_python_sdk/pydantic/error_for_get_by_custom_screen_transaction_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Custom Screen  -  GetByCustomScreenTransactionId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_custom_screen.get_detail`<a id="peoplehremployee_custom_screenget_detail"></a>

This API is used to get custom screen details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = peoplehr.employee_custom_screen.get_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee custom screen api to GetCustomScreenDetail

##### action: `str`<a id="action-str"></a>

Action default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetCustomScreenDetailParameter`](./people_hr_python_sdk/type/get_custom_screen_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetCustomScreenDetail`](./people_hr_python_sdk/pydantic/error_for_get_custom_screen_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Custom Screen  -  GetCustomScreenDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_custom_screen.get_screen_by_employee_id`<a id="peoplehremployee_custom_screenget_screen_by_employee_id"></a>

This API is used to get custom screen by employee id detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_screen_by_employee_id_response = peoplehr.employee_custom_screen.get_screen_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    screen_id=123,
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee custom screen api to GetCustomScreenByEmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### screen_id: `int`<a id="screen_id-int"></a>

Screen Id value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for get custom screen by employeeId

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetCustomScreenByEmployeeIdParameter`](./people_hr_python_sdk/type/get_custom_screen_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetCustomScreenByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_custom_screen_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Custom Screen  -  GetCustomScreenByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_custom_screen.update_custom_screen_transaction`<a id="peoplehremployee_custom_screenupdate_custom_screen_transaction"></a>

This API is used to update custom screen transaction details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_screen_transaction_response = peoplehr.employee_custom_screen.update_custom_screen_transaction(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    screen_id=123,
    custom_screen_transaction_id=12345,
    custom_columns=[
        {
            "column_name": "Column 1 Name",
            "column_value": "Abcd",
        }
    ],
    add_files=[
        {
            "document_name": "123.pdf",
            "file": "Pass base64 string",
            "description": "File description",
            "document_category": "Custom Category",
            "signature_required": "false",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee custom screen api to UpdateCustomScreenTransaction

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for update custom screen transaction

##### screen_id: `int`<a id="screen_id-int"></a>

Screen Id value

##### custom_screen_transaction_id: `int`<a id="custom_screen_transaction_id-int"></a>

Custom Screen Transaction Id

##### custom_columns: [`CustomColumnsForEmployeeCustomScreenObject`](./people_hr_python_sdk/type/custom_columns_for_employee_custom_screen_object.py)<a id="custom_columns-customcolumnsforemployeecustomscreenobjectpeople_hr_python_sdktypecustom_columns_for_employee_custom_screen_objectpy"></a>

CustomColumns for update custom screen transaction

##### add_files: [`AddFilesForEmployeeCustomScreenObject`](./people_hr_python_sdk/type/add_files_for_employee_custom_screen_object.py)<a id="add_files-addfilesforemployeecustomscreenobjectpeople_hr_python_sdktypeadd_files_for_employee_custom_screen_objectpy"></a>

AddFiles for update custom screen transaction

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCustomScreenTransactionParameter`](./people_hr_python_sdk/type/update_custom_screen_transaction_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateCustomScreenTransaction`](./people_hr_python_sdk/pydantic/error_for_update_custom_screen_transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Custom Screen  -  UpdateCustomScreenTransaction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_document.get_all_documents`<a id="peoplehremployee_documentget_all_documents"></a>

This API is used to GEt All Document Detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_documents_response = peoplehr.employee_document.get_all_documents(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get all document

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for get all document 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAllDocumentParameter`](./people_hr_python_sdk/type/get_all_document_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAllDocument`](./people_hr_python_sdk/pydantic/error_for_get_all_document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeDocument  -  GetAllDocument` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_document.get_document_by_id`<a id="peoplehremployee_documentget_document_by_id"></a>

This API is used to get Document By Id for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_document_by_id_response = peoplehr.employee_document.get_document_by_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    document_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for GetDocumentByID

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for get document by id

##### document_id: [`LongInteger`](./people_hr_python_sdk/type/long_integer.py)<a id="document_id-longintegerpeople_hr_python_sdktypelong_integerpy"></a>

DocumentId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetDocumentByIDParameter`](./people_hr_python_sdk/type/get_document_by_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetDocumentById`](./people_hr_python_sdk/pydantic/error_for_get_document_by_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeDocument  -  GetDocumentById` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_document.submit_document_details`<a id="peoplehremployee_documentsubmit_document_details"></a>

This API is used to Upload Employee Document details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_document_details_response = peoplehr.employee_document.submit_document_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    category="Catagory",
    employee_access="true",
    manager_access="true",
    signature_required="true",
    document_name="Abc.txt",
    description="Description here",
    file="Pass base64 string",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to Upload Employee Document

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

 Employee id for upload employee document

##### category: `str`<a id="category-str"></a>

Category default value 

##### employee_access: [`EmployeeAccess`](./people_hr_python_sdk/type/employee_access.py)<a id="employee_access-employeeaccesspeople_hr_python_sdktypeemployee_accesspy"></a>

EmployeeAccess for upload employee document 

##### manager_access: [`ManagerAccess`](./people_hr_python_sdk/type/manager_access.py)<a id="manager_access-manageraccesspeople_hr_python_sdktypemanager_accesspy"></a>

ManagerAccess for upload employee document 

##### signature_required: [`SignatureRequired`](./people_hr_python_sdk/type/signature_required.py)<a id="signature_required-signaturerequiredpeople_hr_python_sdktypesignature_requiredpy"></a>

SignatureRequired for upload employee document

##### document_name: `str`<a id="document_name-str"></a>

DocumentName value

##### description: `str`<a id="description-str"></a>

Description value

##### file: `str`<a id="file-str"></a>

File value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadEmployeeDocumentParameter`](./people_hr_python_sdk/type/upload_employee_document_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUploadEmployeeDocument`](./people_hr_python_sdk/pydantic/error_for_upload_employee_document.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeDocument  -  UploadEmployeeDocument` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_driving.add_new_driving_license`<a id="peoplehremployee_drivingadd_new_driving_license"></a>

This API is used to Add new driving license


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_driving_license_response = peoplehr.employee_driving.add_new_driving_license(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    license_number="Li555",
    license_type="2 wheeler",
    expiry_date="2018-07-07",
    comments="Comments goes here",
    custom_columns=[
        {
            "column_name": "Vehicle 1",
            "column_value": "ABC",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Base 64 code",
            "descriptions": "Descriptions goes here",
            "document_category": "Custom Catagory",
            "signature_required": "False",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for add new driving license

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for add new driving license

##### license_number: [`LicenseNumber`](./people_hr_python_sdk/type/license_number.py)<a id="license_number-licensenumberpeople_hr_python_sdktypelicense_numberpy"></a>

License number for add new driving license

##### license_type: `str`<a id="license_type-str"></a>

License type

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### custom_columns: [`CustomColumnsForEmployeeDriving`](./people_hr_python_sdk/type/custom_columns_for_employee_driving.py)<a id="custom_columns-customcolumnsforemployeedrivingpeople_hr_python_sdktypecustom_columns_for_employee_drivingpy"></a>

Custom columns for add new driving license

##### add_files: [`AddFilesForEmployeeDriving`](./people_hr_python_sdk/type/add_files_for_employee_driving.py)<a id="add_files-addfilesforemployeedrivingpeople_hr_python_sdktypeadd_files_for_employee_drivingpy"></a>

Add files for add new driving license

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewDrivingLicenseParameter`](./people_hr_python_sdk/type/add_new_driving_license_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewDrivingLicense`](./people_hr_python_sdk/pydantic/error_for_add_new_driving_license.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Driving  -  AddNewDrivingLicense` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_driving.get_driving_license_by_driving_id`<a id="peoplehremployee_drivingget_driving_license_by_driving_id"></a>

This API is used to get driving license by drivingId


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_driving_license_by_driving_id_response = peoplehr.employee_driving.get_driving_license_by_driving_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    driving_id=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get driving license by drivingid

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for get driving license by drivingid

##### driving_id: `int`<a id="driving_id-int"></a>

Driving id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetDrivingLicenseByDrivingIdParameter`](./people_hr_python_sdk/type/get_driving_license_by_driving_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetDrivingLicenseByDrivingId`](./people_hr_python_sdk/pydantic/error_for_get_driving_license_by_driving_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Driving  -  GetDrivingLicenseByDrivingId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_driving.get_driving_license_by_employee_id`<a id="peoplehremployee_drivingget_driving_license_by_employee_id"></a>

This API is used to get driving license by employeeid


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_driving_license_by_employee_id_response = peoplehr.employee_driving.get_driving_license_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get driving license by EmployeeId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get driving license by EmployeeId

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetDrivingLicenseByEmployeeIdParameter`](./people_hr_python_sdk/type/get_driving_license_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetDrivingLicenseByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_driving_license_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Driving  -  GetDrivingLicenseByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_driving.remove_driving_license`<a id="peoplehremployee_drivingremove_driving_license"></a>

This API is used to delete driving license


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_driving_license_response = peoplehr.employee_driving.remove_driving_license(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    driving_id=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for delete driving license

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for delete driving license

##### driving_id: `int`<a id="driving_id-int"></a>

Driving id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteDrivingLicenseParameter`](./people_hr_python_sdk/type/delete_driving_license_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteDrivingLicense`](./people_hr_python_sdk/pydantic/error_for_delete_driving_license.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Driving  -  DeleteDrivingLicense` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_driving.update_driving_license`<a id="peoplehremployee_drivingupdate_driving_license"></a>

This API is used to update driving license


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_driving_license_response = peoplehr.employee_driving.update_driving_license(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    driving_id=2,
    license_number="Li555",
    license_type="2 wheeler",
    expiry_date="2018-07-07",
    comments="Comments goes here",
    custom_columns=[
        {
            "column_name": "Vehicle 1",
            "column_value": "ABC",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Base 64 code",
            "descriptions": "Descriptions goes here",
            "document_category": "Custom Catagory",
            "signature_required": "False",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for update driving license

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for update driving license

##### driving_id: `int`<a id="driving_id-int"></a>

Driving id default value

##### license_number: [`LicenseNumber`](./people_hr_python_sdk/type/license_number.py)<a id="license_number-licensenumberpeople_hr_python_sdktypelicense_numberpy"></a>

License number for update driving license

##### license_type: `str`<a id="license_type-str"></a>

License type

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### custom_columns: [`CustomColumnsForEmployeeDriving`](./people_hr_python_sdk/type/custom_columns_for_employee_driving.py)<a id="custom_columns-customcolumnsforemployeedrivingpeople_hr_python_sdktypecustom_columns_for_employee_drivingpy"></a>

Custom columns for update driving license

##### add_files: [`AddFilesForEmployeeDriving`](./people_hr_python_sdk/type/add_files_for_employee_driving.py)<a id="add_files-addfilesforemployeedrivingpeople_hr_python_sdktypeadd_files_for_employee_drivingpy"></a>

Add files for update driving license

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateDrivingLicenseParameter`](./people_hr_python_sdk/type/update_driving_license_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateDrivingLicense`](./people_hr_python_sdk/pydantic/error_for_update_driving_license.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Driving  -  UpdateDrivingLicense` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_holiday.add_new_holiday`<a id="peoplehremployee_holidayadd_new_holiday"></a>

This API is used to add new holiday


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_holiday_response = peoplehr.employee_holiday.add_new_holiday(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    duration_type=1,
    start_date="2016-07-27",
    end_date="2017-07-27",
    duration_in_days=1,
    duration_in_minutes=450,
    part_of_day="AM",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee holiday to AddNewHoliday

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add new holiday

##### duration_type: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="duration_type-bytepeople_hr_python_sdktypebytepy"></a>

Duration type default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### duration_in_days: `int`<a id="duration_in_days-int"></a>

Duration in days default value 

##### duration_in_minutes: `int`<a id="duration_in_minutes-int"></a>

Duration in minutes default value 

##### part_of_day: [`PartOfDay`](./people_hr_python_sdk/type/part_of_day.py)<a id="part_of_day-partofdaypeople_hr_python_sdktypepart_of_daypy"></a>

Part of day for add new holiday

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewHolidayParameter`](./people_hr_python_sdk/type/add_new_holiday_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewHoliday`](./people_hr_python_sdk/pydantic/error_for_add_new_holiday.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Holiday  -  AddNewHoliday` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_holiday.get_holiday_detail`<a id="peoplehremployee_holidayget_holiday_detail"></a>

This API is used to get holiday detail list


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_holiday_detail_response = peoplehr.employee_holiday.get_holiday_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for GetHolidayDetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for get holiday detail

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetHolidayDetailParameter`](./people_hr_python_sdk/type/get_holiday_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetHolidayDetail`](./people_hr_python_sdk/pydantic/error_for_get_holiday_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Holiday  -  GetHolidayDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_holiday.remove_holiday_detail`<a id="peoplehremployee_holidayremove_holiday_detail"></a>

This API is used to delete holiday detail



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_holiday_detail_response = peoplehr.employee_holiday.remove_holiday_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for DeleteHoliday

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for delete holiday

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteHolidayParameter`](./people_hr_python_sdk/type/delete_holiday_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteHolidy`](./people_hr_python_sdk/pydantic/error_for_delete_holidy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Holiday  -  DeleteHoliday` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_holiday.update_detail`<a id="peoplehremployee_holidayupdate_detail"></a>

This API is used to update holiday detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_detail_response = peoplehr.employee_holiday.update_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    old_start_date="2017-07-18",
    old_end_date="2017-07-18",
    duration_type=1,
    start_date="2016-07-27",
    end_date="2017-07-27",
    duration_in_days=1,
    duration_in_minutes=450,
    part_of_day="AM",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for UpdateHoliday

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update holiday

##### old_start_date: `date`<a id="old_start_date-date"></a>

Old start date default value 

##### old_end_date: `date`<a id="old_end_date-date"></a>

Old end date default value 

##### duration_type: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="duration_type-bytepeople_hr_python_sdktypebytepy"></a>

Duration type default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### duration_in_days: `int`<a id="duration_in_days-int"></a>

Duration in days default value 

##### duration_in_minutes: `int`<a id="duration_in_minutes-int"></a>

Duration in minutes default value 

##### part_of_day: [`PartOfDay`](./people_hr_python_sdk/type/part_of_day.py)<a id="part_of_day-partofdaypeople_hr_python_sdktypepart_of_daypy"></a>

Part of day for update holiday

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateHolidayParameter`](./people_hr_python_sdk/type/update_holiday_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateHoliday`](./people_hr_python_sdk/pydantic/error_for_update_holiday.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Holiday  -  UpdateHoliday` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.add_new_project_task_detail`<a id="peoplehremployee_project_timesheetadd_new_project_task_detail"></a>

This API is used to add new project task detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_project_task_detail_response = peoplehr.employee_project_timesheet.add_new_project_task_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_task_name="ABC",
    in_use="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to add new project task

##### action: `str`<a id="action-str"></a>

Action default value

##### project_task_name: [`ProjectTaskName`](./people_hr_python_sdk/type/project_task_name.py)<a id="project_task_name-projecttasknamepeople_hr_python_sdktypeproject_task_namepy"></a>

Task Name for new project task detail

##### in_use: `str`<a id="in_use-str"></a>

InUse default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewProjectTaskParameter`](./people_hr_python_sdk/type/add_new_project_task_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewProjectTask`](./people_hr_python_sdk/pydantic/error_for_add_new_project_task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  AddNewProjectTask` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.add_new_project_task_detail_0`<a id="peoplehremployee_project_timesheetadd_new_project_task_detail_0"></a>

This API is used to add new project task detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_project_task_detail_0_response = peoplehr.employee_project_timesheet.add_new_project_task_detail_0(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_task_detail_name="XYZ",
    in_use="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to add new project task detail

##### action: `str`<a id="action-str"></a>

Action default value

##### project_task_detail_name: [`ProjectTaskDetailName`](./people_hr_python_sdk/type/project_task_detail_name.py)<a id="project_task_detail_name-projecttaskdetailnamepeople_hr_python_sdktypeproject_task_detail_namepy"></a>

Project task detail name for add new project task detail

##### in_use: `str`<a id="in_use-str"></a>

InUse default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewProjectTaskDetailParameter`](./people_hr_python_sdk/type/add_new_project_task_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewProjectTaskDetail`](./people_hr_python_sdk/pydantic/error_for_add_new_project_task_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  AddNewProjectTaskDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.add_project_detail`<a id="peoplehremployee_project_timesheetadd_project_detail"></a>

This API is used to add new project details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_project_detail_response = peoplehr.employee_project_timesheet.add_project_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_name="Project Name",
    in_use="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to add new project

##### action: `str`<a id="action-str"></a>

Action default value

##### project_name: `str`<a id="project_name-str"></a>

ProjectName default value 

##### in_use: `str`<a id="in_use-str"></a>

InUse default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewProjectParameter`](./people_hr_python_sdk/type/add_new_project_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewProject`](./people_hr_python_sdk/pydantic/error_for_add_new_project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  AddNewProject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.create_timesheet`<a id="peoplehremployee_project_timesheetcreate_timesheet"></a>

This API is used to create project timesheet for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_timesheet_response = peoplehr.employee_project_timesheet.create_timesheet(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    project_timesheet_date="2014-01-01",
    timesheet_project="Project name goes here",
    timesheet_task="Time sheet tasks goes here",
    timesheet_detail="Time sheet details goes here",
    start_time="02:00",
    end_time="04:00",
    total_hours="02:00",
    quantity=0,
    notes="notes goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get project time sheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for create project timesheet

##### project_timesheet_date: `date`<a id="project_timesheet_date-date"></a>

ProjectTimesheetDate default value 

##### timesheet_project: `str`<a id="timesheet_project-str"></a>

TimesheetProject default value 

##### timesheet_task: `str`<a id="timesheet_task-str"></a>

TimesheetTask default value 

##### timesheet_detail: `str`<a id="timesheet_detail-str"></a>

TimesheetDetail default value 

##### start_time: `str`<a id="start_time-str"></a>

StartTime default value 

##### end_time: `str`<a id="end_time-str"></a>

EndTime default value 

##### total_hours: `str`<a id="total_hours-str"></a>

TotalHours default value 

##### quantity: `int`<a id="quantity-int"></a>

Quantity default value 

##### notes: `str`<a id="notes-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateProjectTimesheetParameter`](./people_hr_python_sdk/type/create_project_timesheet_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCreateProjectTimesheet`](./people_hr_python_sdk/pydantic/error_for_create_project_timesheet.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  CreateProjectTimesheet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.delete_timesheet`<a id="peoplehremployee_project_timesheetdelete_timesheet"></a>

This API is used to delete project timesheet for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_timesheet_response = peoplehr.employee_project_timesheet.delete_timesheet(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    transaction_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get project time sheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete project timesheet detail

##### transaction_id: `int`<a id="transaction_id-int"></a>

TransactionId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteProjectTimesheetParameter`](./people_hr_python_sdk/type/delete_project_timesheet_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteProjectTimesheet`](./people_hr_python_sdk/pydantic/error_for_delete_project_timesheet.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  DeleteProjectTimesheet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.edit_project_details`<a id="peoplehremployee_project_timesheetedit_project_details"></a>

This API is used to edit project details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_project_details_response = peoplehr.employee_project_timesheet.edit_project_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_name="Project Name",
    new_project_name="updated Project Name",
    in_use="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to edit project

##### action: `str`<a id="action-str"></a>

Action default value

##### project_name: `str`<a id="project_name-str"></a>

ProjectName default value 

##### new_project_name: `str`<a id="new_project_name-str"></a>

NewProjectName default value 

##### in_use: `str`<a id="in_use-str"></a>

InUse default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EditProjectParameter`](./people_hr_python_sdk/type/edit_project_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForEditProject`](./people_hr_python_sdk/pydantic/error_for_edit_project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  EditProject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.edit_task_detail`<a id="peoplehremployee_project_timesheetedit_task_detail"></a>

This API is used to edit project task detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_task_detail_response = peoplehr.employee_project_timesheet.edit_task_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_task_detail_name="XYZ",
    new_project_task_detail_name="New Project Task Detail Name goes here",
    in_use="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to edit project task detail

##### action: `str`<a id="action-str"></a>

Action default value

##### project_task_detail_name: [`ProjectTaskDetailName`](./people_hr_python_sdk/type/project_task_detail_name.py)<a id="project_task_detail_name-projecttaskdetailnamepeople_hr_python_sdktypeproject_task_detail_namepy"></a>

Project task detail name for edit project task detail

##### new_project_task_detail_name: `str`<a id="new_project_task_detail_name-str"></a>

New ProjectTaskDetailName default value 

##### in_use: `str`<a id="in_use-str"></a>

InUse default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EditProjectTaskDetailParameter`](./people_hr_python_sdk/type/edit_project_task_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForEditProjectTaskDetail`](./people_hr_python_sdk/pydantic/error_for_edit_project_task_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  EditProjectTaskDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.get_all_project_task`<a id="peoplehremployee_project_timesheetget_all_project_task"></a>

This API is used to get all project task detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_project_task_response = peoplehr.employee_project_timesheet.get_all_project_task(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_task_name="ABC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get all project task

##### action: `str`<a id="action-str"></a>

Action default value

##### project_task_name: [`ProjectTaskName`](./people_hr_python_sdk/type/project_task_name.py)<a id="project_task_name-projecttasknamepeople_hr_python_sdktypeproject_task_namepy"></a>

Task Name to get all Project task

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAllProjectTaskParameter`](./people_hr_python_sdk/type/get_all_project_task_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAllProjectTask`](./people_hr_python_sdk/pydantic/error_for_get_all_project_task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  GetAllProjectTask` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.get_all_project_task_detail`<a id="peoplehremployee_project_timesheetget_all_project_task_detail"></a>

This API is used to get all project task detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_project_task_detail_response = peoplehr.employee_project_timesheet.get_all_project_task_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_task_detail_name="XYZ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee Project timesheet api to get all project task detail

##### action: `str`<a id="action-str"></a>

Action default value

##### project_task_detail_name: [`ProjectTaskDetailName`](./people_hr_python_sdk/type/project_task_detail_name.py)<a id="project_task_detail_name-projecttaskdetailnamepeople_hr_python_sdktypeproject_task_detail_namepy"></a>

Project task name for get all project task detail  

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAllProjectTaskDetailParameter`](./people_hr_python_sdk/type/get_all_project_task_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAllProjectTaskDetail`](./people_hr_python_sdk/pydantic/error_for_get_all_project_task_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  GetAllProjectTaskDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.get_by_transaction_id`<a id="peoplehremployee_project_timesheetget_by_transaction_id"></a>

This API is used to get project timesheet by transactionid for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_transaction_id_response = peoplehr.employee_project_timesheet.get_by_transaction_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    transaction_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get project time sheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for get project timesheet detail

##### transaction_id: `int`<a id="transaction_id-int"></a>

TransactionId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetProjectTimesheetByTransactionId`](./people_hr_python_sdk/type/get_project_timesheet_by_transaction_id.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetProjectTimesheetByTransactionId`](./people_hr_python_sdk/pydantic/error_for_get_project_timesheet_by_transaction_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  GetProjectTimesheetByTransactionId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.get_project_timesheet_detail`<a id="peoplehremployee_project_timesheetget_project_timesheet_detail"></a>

This API is used to get project time sheet detail for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_project_timesheet_detail_response = peoplehr.employee_project_timesheet.get_project_timesheet_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get project time sheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetProjectTimesheetDetail`](./people_hr_python_sdk/type/get_project_timesheet_detail.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetProjectTimesheetDetail`](./people_hr_python_sdk/pydantic/error_for_get_project_timesheet_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  GetProjectTimesheetDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.list_all_timesheet_project`<a id="peoplehremployee_project_timesheetlist_all_timesheet_project"></a>

This API is used to get all timesheet project detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_timesheet_project_response = peoplehr.employee_project_timesheet.list_all_timesheet_project(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_name="Project Name",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get all project time sheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### project_name: `str`<a id="project_name-str"></a>

ProjectName default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAllTimesheetProjectParameter`](./people_hr_python_sdk/type/get_all_timesheet_project_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAllTimesheetProject`](./people_hr_python_sdk/pydantic/error_for_get_all_timesheet_project.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  GetAllTimesheetProject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.update_project_task_detail`<a id="peoplehremployee_project_timesheetupdate_project_task_detail"></a>

This API is used to edit project task detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_project_task_detail_response = peoplehr.employee_project_timesheet.update_project_task_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    project_task_name="ABC",
    new_project_task_name="XYZ",
    in_use="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee Project timesheet api to edit project task detail

##### action: `str`<a id="action-str"></a>

Action default value

##### project_task_name: [`ProjectTaskName`](./people_hr_python_sdk/type/project_task_name.py)<a id="project_task_name-projecttasknamepeople_hr_python_sdktypeproject_task_namepy"></a>

Project Task Name for edit project task detail

##### new_project_task_name: [`NewProjectTaskName`](./people_hr_python_sdk/type/new_project_task_name.py)<a id="new_project_task_name-newprojecttasknamepeople_hr_python_sdktypenew_project_task_namepy"></a>

New_ProjectTaskName for edit project task detail

##### in_use: `str`<a id="in_use-str"></a>

InUse default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EditProjectTaskParameter`](./people_hr_python_sdk/type/edit_project_task_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForEditProjectTask`](./people_hr_python_sdk/pydantic/error_for_edit_project_task.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  EditProjectTask` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_project_timesheet.update_timesheet`<a id="peoplehremployee_project_timesheetupdate_timesheet"></a>

This API is used to update project timesheet for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_timesheet_response = peoplehr.employee_project_timesheet.update_timesheet(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    transaction_id=1,
    timesheet_project="Project name goes here",
    timesheet_task="Time sheet tasks goes here",
    timesheet_detail="Time sheet details goes here",
    start_time="02:00",
    end_time="04:00",
    total_hours="02:00",
    quantity=0,
    notes="notes goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to get project time sheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for update project timesheet

##### transaction_id: `int`<a id="transaction_id-int"></a>

TransactionId default value 

##### timesheet_project: `str`<a id="timesheet_project-str"></a>

TimesheetProject default value 

##### timesheet_task: `str`<a id="timesheet_task-str"></a>

TimesheetTask default value 

##### timesheet_detail: `str`<a id="timesheet_detail-str"></a>

TimesheetDetail default value 

##### start_time: `str`<a id="start_time-str"></a>

StartTime default value 

##### end_time: `str`<a id="end_time-str"></a>

EndTime default value 

##### total_hours: `str`<a id="total_hours-str"></a>

TotalHours default value 

##### quantity: `int`<a id="quantity-int"></a>

Quantity default value 

##### notes: `str`<a id="notes-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProjectTimesheetParameter`](./people_hr_python_sdk/type/update_project_timesheet_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateProjectTimesheet`](./people_hr_python_sdk/pydantic/error_for_update_project_timesheet.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Project Timesheet  -  UpdateProjectTimesheet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_qualification.add_new_qualification`<a id="peoplehremployee_qualificationadd_new_qualification"></a>

This API is used to Add new qualification


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_qualification_response = peoplehr.employee_qualification.add_new_qualification(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    qualification="MSC",
    subject="Computer science",
    date_passed="2017-05-01",
    expiry_date="2018-07-07",
    comments="Comments goes here",
    custom_columns=[
        {
            "column_name": "Vehicle 1",
            "column_value": "ABC",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Base 64 code",
            "descriptions": "Descriptions goes here",
            "document_category": "Custom Catagory",
            "signature_required": "False",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for add new qualification

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add new qualification

##### qualification: `str`<a id="qualification-str"></a>

Qualification

##### subject: `str`<a id="subject-str"></a>

Subject

##### date_passed: `date`<a id="date_passed-date"></a>

Date passed default value

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### custom_columns: [`CustomColumnsForEmployeeQualification`](./people_hr_python_sdk/type/custom_columns_for_employee_qualification.py)<a id="custom_columns-customcolumnsforemployeequalificationpeople_hr_python_sdktypecustom_columns_for_employee_qualificationpy"></a>

CustomColumns for add new qualification

##### add_files: [`AddFilesForEmployeeQualification`](./people_hr_python_sdk/type/add_files_for_employee_qualification.py)<a id="add_files-addfilesforemployeequalificationpeople_hr_python_sdktypeadd_files_for_employee_qualificationpy"></a>

AddFiles for add new qualification

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewQualificationParameter`](./people_hr_python_sdk/type/add_new_qualification_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewQualification`](./people_hr_python_sdk/pydantic/error_for_add_new_qualification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Qualification  -  AddNewQualification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_qualification.delete_qualification`<a id="peoplehremployee_qualificationdelete_qualification"></a>

This API is used to delete qualification


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_qualification_response = peoplehr.employee_qualification.delete_qualification(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    qualification_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for delete qualification

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete qualification

##### qualification_id: `int`<a id="qualification_id-int"></a>

Qualification id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteQualificationParameter`](./people_hr_python_sdk/type/delete_qualification_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteQualification`](./people_hr_python_sdk/pydantic/error_for_delete_qualification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Qualification  -  DeleteQualification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_qualification.get_by_employee_id`<a id="peoplehremployee_qualificationget_by_employee_id"></a>

This API is used to get qualification by EmployeeId 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = peoplehr.employee_qualification.get_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

API key for get qualification by employeeid

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get qualification by employeeid

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetQualificationByEmployeeIdParameter`](./people_hr_python_sdk/type/get_qualification_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetQualificationByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_qualification_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Qualification  -  GetQualificationByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_qualification.get_by_qualification_id`<a id="peoplehremployee_qualificationget_by_qualification_id"></a>

This API is used to Get qualification by qualification Id 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_qualification_id_response = peoplehr.employee_qualification.get_by_qualification_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    qualification_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIkey for get qualification by qualificationId

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for get qualification by qualificationId

##### qualification_id: `int`<a id="qualification_id-int"></a>

Qualification id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetQualificationByQualificationIdParameter`](./people_hr_python_sdk/type/get_qualification_by_qualification_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetQualificationByQualificationId`](./people_hr_python_sdk/pydantic/error_for_get_qualification_by_qualification_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Qualification  -  GetQualificationByQualificationId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_qualification.update_qualification`<a id="peoplehremployee_qualificationupdate_qualification"></a>

This API is used to Update qualification


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_qualification_response = peoplehr.employee_qualification.update_qualification(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    qualification_id=1,
    qualification="MSC",
    subject="Computer science",
    date_passed="2017-05-01",
    expiry_date="2018-07-07",
    comments="Comments goes here",
    custom_columns=[
        {
            "column_name": "Vehicle 1",
            "column_value": "ABC",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Base 64 code",
            "descriptions": "Descriptions goes here",
            "document_category": "Custom Catagory",
            "signature_required": "False",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for update qualification

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update qualification

##### qualification_id: `int`<a id="qualification_id-int"></a>

Qualification id default value

##### qualification: `str`<a id="qualification-str"></a>

Qualification

##### subject: `str`<a id="subject-str"></a>

Subject

##### date_passed: `date`<a id="date_passed-date"></a>

Date passed default value

##### expiry_date: `date`<a id="expiry_date-date"></a>

ExpiryDate default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### custom_columns: [`CustomColumnsForEmployeeQualification`](./people_hr_python_sdk/type/custom_columns_for_employee_qualification.py)<a id="custom_columns-customcolumnsforemployeequalificationpeople_hr_python_sdktypecustom_columns_for_employee_qualificationpy"></a>

Custom columns

##### add_files: [`AddFilesForEmployeeQualification`](./people_hr_python_sdk/type/add_files_for_employee_qualification.py)<a id="add_files-addfilesforemployeequalificationpeople_hr_python_sdktypeadd_files_for_employee_qualificationpy"></a>

Add files

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateQualificationParameter`](./people_hr_python_sdk/type/update_qualification_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateQualification`](./people_hr_python_sdk/pydantic/error_for_update_qualification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Qualification  -  UpdateQualification` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_salary.add_new_salary`<a id="peoplehremployee_salaryadd_new_salary"></a>

This API is used to Create New Salary for given user


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_salary_response = peoplehr.employee_salary.add_new_salary(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    effective_from="2014-01-01",
    salary_type="Annual",
    payment_frequency="Monthly",
    salary_amount=1000,
    currency_code="ASD",
    change_reason="New Reason1",
    deductions=[
        {
            "deduction": "Social Club 1",
            "display_as_amount_or_percentage": "false",
            "amount": 100,
            "percentage": 10,
            "comments": "Comments for deduction social",
            "include_in_total_salary": "false",
        }
    ],
    entitlements=[
        {
            "entitlement": "entitlement_example",
            "display_as_amount_or_percentage": "false",
            "amount": 100,
            "percentage": 10,
            "comments": "Comments for deduction social",
            "include_in_total_salary": "false",
        }
    ],
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Create New Salary of employee 

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for create new salary

##### effective_from: `date`<a id="effective_from-date"></a>

EffectiveFrom default value 

##### salary_type: [`SalaryType`](./people_hr_python_sdk/type/salary_type.py)<a id="salary_type-salarytypepeople_hr_python_sdktypesalary_typepy"></a>

SalaryType for create new salary

##### payment_frequency: [`PaymentFrequency`](./people_hr_python_sdk/type/payment_frequency.py)<a id="payment_frequency-paymentfrequencypeople_hr_python_sdktypepayment_frequencypy"></a>

PaymentFrequency for create new salary

##### salary_amount: `int`<a id="salary_amount-int"></a>

SalaryAmount default value 

##### currency_code: `str`<a id="currency_code-str"></a>

CurrencyCode default value 

##### change_reason: `str`<a id="change_reason-str"></a>

ChangeReason default value 

##### deductions: [`DeductionsArray`](./people_hr_python_sdk/type/deductions_array.py)<a id="deductions-deductionsarraypeople_hr_python_sdktypedeductions_arraypy"></a>

Deductions of user Array

##### entitlements: [`EntitlementsArray`](./people_hr_python_sdk/type/entitlements_array.py)<a id="entitlements-entitlementsarraypeople_hr_python_sdktypeentitlements_arraypy"></a>

Entitlements of user

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateNewSalaryParameter`](./people_hr_python_sdk/type/create_new_salary_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCreateNewSalary1`](./people_hr_python_sdk/pydantic/error_for_create_new_salary1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeSalary  -  CreateNewSalary` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_salary.delete_salary`<a id="peoplehremployee_salarydelete_salary"></a>

This API is used to delete Salary details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_salary_response = peoplehr.employee_salary.delete_salary(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    effective_from="2014-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for delete Salary of employee

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for delete salary

##### effective_from: `date`<a id="effective_from-date"></a>

EffectiveFrom default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteSalaryParameter`](./people_hr_python_sdk/type/delete_salary_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteSalary`](./people_hr_python_sdk/pydantic/error_for_delete_salary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeSalary  -  DeleteSalary` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_salary.get_salary_detail`<a id="peoplehremployee_salaryget_salary_detail"></a>

This API is used to Get employee salary details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_salary_detail_response = peoplehr.employee_salary.get_salary_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    is_include_history=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for GetSalaryDetail of employee

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for get salary detail

##### is_include_history: `bool`<a id="is_include_history-bool"></a>

IsIncludeHistory Default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetSalaryDetail2`](./people_hr_python_sdk/type/get_salary_detail2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetSalaryDetail`](./people_hr_python_sdk/pydantic/error_for_get_salary_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/EmployeeSalary  -  GetSalaryDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_timesheet.create_new_timesheet`<a id="peoplehremployee_timesheetcreate_new_timesheet"></a>

This API is used to create new employee Timesheet


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_timesheet_response = peoplehr.employee_timesheet.create_new_timesheet(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    timesheet_date="2017-01-01",
    time_in1="09:35",
    time_out1="04:00",
    time_in2="09:45",
    time_out2="04:10",
    time_in3="09:55",
    time_out3="04:20",
    time_in4="600",
    time_out4="04:40",
    time_in5="610",
    time_out5="04:50",
    time_in6="630",
    time_out6="05:00",
    time_in7="650",
    time_out7="05:10",
    time_in8="670",
    time_out8="05:20",
    time_in9="690",
    time_out9="05:30",
    time_in10="710",
    time_out10="06:00",
    time_in11="720",
    time_out11="06:10",
    time_in12="750",
    time_out12="06:20",
    time_in13="770",
    time_out13="06:30",
    time_in14="180",
    time_out14="06:50",
    time_in15="03:10",
    time_out15="420",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee timesheet api to create employee's new timesheet

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to create new employee timesheet

##### timesheet_date: `date`<a id="timesheet_date-date"></a>

TimesheetDate default value 

##### time_in1: `str`<a id="time_in1-str"></a>

##### time_out1: `str`<a id="time_out1-str"></a>

TimeOut1 default value

##### time_in2: `str`<a id="time_in2-str"></a>

TimeIn2 default value

##### time_out2: `str`<a id="time_out2-str"></a>

TimeOut2 default value

##### time_in3: `str`<a id="time_in3-str"></a>

TimeIn3 default value

##### time_out3: `str`<a id="time_out3-str"></a>

TimeOut3 default value

##### time_in4: `str`<a id="time_in4-str"></a>

TimeIn4 default value

##### time_out4: `str`<a id="time_out4-str"></a>

TimeOut4 default value

##### time_in5: `str`<a id="time_in5-str"></a>

TimeIn5 default value

##### time_out5: `str`<a id="time_out5-str"></a>

TimeOut5 default value

##### time_in6: `str`<a id="time_in6-str"></a>

TimeIn6 default value

##### time_out6: `str`<a id="time_out6-str"></a>

TimeOut6 default value

##### time_in7: `str`<a id="time_in7-str"></a>

TimeIn7 default value

##### time_out7: `str`<a id="time_out7-str"></a>

TimeOut7 default value

##### time_in8: `str`<a id="time_in8-str"></a>

TimeIn8 default value

##### time_out8: `str`<a id="time_out8-str"></a>

TimeOut8 default value

##### time_in9: `str`<a id="time_in9-str"></a>

TimeIn9 default value

##### time_out9: `str`<a id="time_out9-str"></a>

TimeOut9 default value

##### time_in10: `str`<a id="time_in10-str"></a>

TimeIn10 default value

##### time_out10: `str`<a id="time_out10-str"></a>

TimeOut10 default value

##### time_in11: `str`<a id="time_in11-str"></a>

TimeIn11 default value

##### time_out11: `str`<a id="time_out11-str"></a>

TimeOut11 default value

##### time_in12: `str`<a id="time_in12-str"></a>

TimeIn12 default value

##### time_out12: `str`<a id="time_out12-str"></a>

TimeOut12 default value

##### time_in13: `str`<a id="time_in13-str"></a>

TimeIn13 default value

##### time_out13: `str`<a id="time_out13-str"></a>

TimeOut13 default value

##### time_in14: `str`<a id="time_in14-str"></a>

TimeIn14 default value

##### time_out14: `str`<a id="time_out14-str"></a>

TimeOut14 default value

##### time_in15: `str`<a id="time_in15-str"></a>

TimeIn15 default value

##### time_out15: `str`<a id="time_out15-str"></a>

TimeOut15 default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateNewTimesheetDefinition`](./people_hr_python_sdk/type/create_new_timesheet_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCreateNewEmployeeTimesheetDetail`](./people_hr_python_sdk/pydantic/error_for_create_new_employee_timesheet_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Timesheet  -  CreateNewTimesheet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_timesheet.delete_timesheet`<a id="peoplehremployee_timesheetdelete_timesheet"></a>

This API is used to delete employee Timesheet


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_timesheet_response = peoplehr.employee_timesheet.delete_timesheet(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    timesheet_date="2017-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for delete employee timesheet

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete employee timesheet

##### timesheet_date: `date`<a id="timesheet_date-date"></a>

TimesheetDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteTimesheetdefinition`](./people_hr_python_sdk/type/delete_timesheetdefinition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteEmployeeTimesheetDetail`](./people_hr_python_sdk/pydantic/error_for_delete_employee_timesheet_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Timesheet  -  DeleteTimesheet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_timesheet.get_detail_list`<a id="peoplehremployee_timesheetget_detail_list"></a>

This API is used to get employee timesheet detail list


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_list_response = peoplehr.employee_timesheet.get_detail_list(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get employee timesheet detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for get employee timesheet detail

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetTimesheetdefinition`](./people_hr_python_sdk/type/get_timesheetdefinition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetTimesheetDetail`](./people_hr_python_sdk/pydantic/error_for_get_timesheet_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Timesheet  -  GetTimesheetDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_timesheet.update_details`<a id="peoplehremployee_timesheetupdate_details"></a>

This API is used to update employee timesheet details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = peoplehr.employee_timesheet.update_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    timesheet_date="2017-01-01",
    time_in1="09:35",
    time_out1="04:00",
    time_in2="09:45",
    time_out2="04:10",
    time_in3="09:55",
    time_out3="04:20",
    time_in4="600",
    time_out4="04:40",
    time_in5="610",
    time_out5="04:50",
    time_in6="630",
    time_out6="05:00",
    time_in7="650",
    time_out7="05:10",
    time_in8="670",
    time_out8="05:20",
    time_in9="690",
    time_out9="05:30",
    time_in10="710",
    time_out10="06:00",
    time_in11="720",
    time_out11="06:10",
    time_in12="750",
    time_out12="06:20",
    time_in13="770",
    time_out13="06:30",
    time_in14="180",
    time_out14="06:50",
    time_in15="03:10",
    time_out15="420",
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey to update employee Timesheet

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update employee timesheet

##### timesheet_date: `date`<a id="timesheet_date-date"></a>

TimesheetDate default value 

##### time_in1: `str`<a id="time_in1-str"></a>

##### time_out1: `str`<a id="time_out1-str"></a>

TimeOut1 default value

##### time_in2: `str`<a id="time_in2-str"></a>

TimeIn2 default value

##### time_out2: `str`<a id="time_out2-str"></a>

TimeOut2 default value

##### time_in3: `str`<a id="time_in3-str"></a>

TimeIn3 default value

##### time_out3: `str`<a id="time_out3-str"></a>

TimeOut3 default value

##### time_in4: `str`<a id="time_in4-str"></a>

TimeIn4 default value

##### time_out4: `str`<a id="time_out4-str"></a>

TimeOut4 default value

##### time_in5: `str`<a id="time_in5-str"></a>

TimeIn5 default value

##### time_out5: `str`<a id="time_out5-str"></a>

TimeOut5 default value

##### time_in6: `str`<a id="time_in6-str"></a>

TimeIn6 default value

##### time_out6: `str`<a id="time_out6-str"></a>

TimeOut6 default value

##### time_in7: `str`<a id="time_in7-str"></a>

TimeIn7 default value

##### time_out7: `str`<a id="time_out7-str"></a>

TimeOut7 default value

##### time_in8: `str`<a id="time_in8-str"></a>

TimeIn8 default value

##### time_out8: `str`<a id="time_out8-str"></a>

TimeOut8 default value

##### time_in9: `str`<a id="time_in9-str"></a>

TimeIn9 default value

##### time_out9: `str`<a id="time_out9-str"></a>

TimeOut9 default value

##### time_in10: `str`<a id="time_in10-str"></a>

TimeIn10 default value

##### time_out10: `str`<a id="time_out10-str"></a>

TimeOut10 default value

##### time_in11: `str`<a id="time_in11-str"></a>

TimeIn11 default value

##### time_out11: `str`<a id="time_out11-str"></a>

TimeOut11 default value

##### time_in12: `str`<a id="time_in12-str"></a>

TimeIn12 default value

##### time_out12: `str`<a id="time_out12-str"></a>

TimeOut12 default value

##### time_in13: `str`<a id="time_in13-str"></a>

TimeIn13 default value

##### time_out13: `str`<a id="time_out13-str"></a>

TimeOut13 default value

##### time_in14: `str`<a id="time_in14-str"></a>

TimeIn14 default value

##### time_out14: `str`<a id="time_out14-str"></a>

TimeOut14 default value

##### time_in15: `str`<a id="time_in15-str"></a>

TimeIn15 default value

##### time_out15: `str`<a id="time_out15-str"></a>

TimeOut15 default value

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTimesheetDefinition`](./people_hr_python_sdk/type/update_timesheet_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateEmployeeTimesheetDetail`](./people_hr_python_sdk/pydantic/error_for_update_employee_timesheet_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Timesheet  -  UpdateTimesheet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_training.add_training_detail`<a id="peoplehremployee_trainingadd_training_detail"></a>

This API is used to Add Training Detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_training_detail_response = peoplehr.employee_training.add_training_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    training_type="Java",
    description="Description here",
    importance=1,
    status=2,
    in_progress=10,
    training_date="2017-10-10",
    trainind_end_date="2015-10-11",
    training_expiry_date="2015-10-12",
    cost="0.01",
    provider="John",
    notes="notes goes here",
    custom_columns=[
        {
            "column_name": "Vehicle 1",
            "column_value": "ABC",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Base 64 code",
            "descriptions": "Descriptions goes here",
            "document_category": "Custom Catagory",
            "signature_required": "False",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for add training detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add training detail

##### training_type: `str`<a id="training_type-str"></a>

Training type

##### description: `str`<a id="description-str"></a>

Description value

##### importance: `int`<a id="importance-int"></a>

Importance default value

##### status: `int`<a id="status-int"></a>

Status default value

##### in_progress: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="in_progress-bytepeople_hr_python_sdktypebytepy"></a>

InProgress default value

##### training_date: `date`<a id="training_date-date"></a>

Training date default value

##### trainind_end_date: `date`<a id="trainind_end_date-date"></a>

Training end date default value

##### training_expiry_date: `date`<a id="training_expiry_date-date"></a>

Training expiry date default value

##### cost: `str`<a id="cost-str"></a>

Cost default value

##### provider: `str`<a id="provider-str"></a>

Provider default value

##### notes: `str`<a id="notes-str"></a>

##### custom_columns: [`CustomColumnsForEmployeeTraining`](./people_hr_python_sdk/type/custom_columns_for_employee_training.py)<a id="custom_columns-customcolumnsforemployeetrainingpeople_hr_python_sdktypecustom_columns_for_employee_trainingpy"></a>

Custom columns for add training detail

##### add_files: [`AddFilesForEmployeeTraining`](./people_hr_python_sdk/type/add_files_for_employee_training.py)<a id="add_files-addfilesforemployeetrainingpeople_hr_python_sdktypeadd_files_for_employee_trainingpy"></a>

Add files for add training detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddTrainingDetailParameter`](./people_hr_python_sdk/type/add_training_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddTrainingDetail`](./people_hr_python_sdk/pydantic/error_for_add_training_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Training  -  addtrainingdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_training.get_detail`<a id="peoplehremployee_trainingget_detail"></a>

This API is used to Get  training detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = peoplehr.employee_training.get_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get training detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get training detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetTrainingDetailParameter`](./people_hr_python_sdk/type/get_training_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetTrainingDetail`](./people_hr_python_sdk/pydantic/error_for_get_training_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Training  -  GetTrainingDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_training.remove_detail`<a id="peoplehremployee_trainingremove_detail"></a>

This API is used to delete training detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_detail_response = peoplehr.employee_training.remove_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    training_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for delete training detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete training detail

##### training_id: `int`<a id="training_id-int"></a>

Training Id default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteTrainingDetailParameter`](./people_hr_python_sdk/type/delete_training_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorFordeletetrainingdetail`](./people_hr_python_sdk/pydantic/error_fordeletetrainingdetail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Training  -  deletetrainingdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_training.update_training_detail`<a id="peoplehremployee_trainingupdate_training_detail"></a>

This API is used to update training detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_training_detail_response = peoplehr.employee_training.update_training_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    training_type="Java",
    description="Description here",
    importance=1,
    status=2,
    in_progress=10,
    training_date="2017-10-10",
    trainind_end_date="2015-10-11",
    training_expiry_date="2015-10-12",
    cost="0.01",
    provider="John",
    notes="notes goes here",
    custom_columns=[
        {
            "column_name": "Vehicle 1",
            "column_value": "ABC",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Base 64 code",
            "descriptions": "Descriptions goes here",
            "document_category": "Custom Catagory",
            "signature_required": "False",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for update training detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update training detail

##### training_type: `str`<a id="training_type-str"></a>

Training type

##### description: `str`<a id="description-str"></a>

Description value

##### importance: `int`<a id="importance-int"></a>

Importance default value

##### status: `int`<a id="status-int"></a>

Status default value

##### in_progress: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="in_progress-bytepeople_hr_python_sdktypebytepy"></a>

InProgress default value

##### training_date: `date`<a id="training_date-date"></a>

Training date default value

##### trainind_end_date: `date`<a id="trainind_end_date-date"></a>

Training end date default value

##### training_expiry_date: `date`<a id="training_expiry_date-date"></a>

Training expiry date default value

##### cost: `str`<a id="cost-str"></a>

Cost default value

##### provider: `str`<a id="provider-str"></a>

Provider default value

##### notes: `str`<a id="notes-str"></a>

##### custom_columns: [`CustomColumnsForEmployeeTraining`](./people_hr_python_sdk/type/custom_columns_for_employee_training.py)<a id="custom_columns-customcolumnsforemployeetrainingpeople_hr_python_sdktypecustom_columns_for_employee_trainingpy"></a>

Custom columns for update training detail

##### add_files: [`AddFilesForEmployeeTraining`](./people_hr_python_sdk/type/add_files_for_employee_training.py)<a id="add_files-addfilesforemployeetrainingpeople_hr_python_sdktypeadd_files_for_employee_trainingpy"></a>

Add files for update training detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateTrainingDetailParameter`](./people_hr_python_sdk/type/update_training_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateTrainingDetail`](./people_hr_python_sdk/pydantic/error_for_update_training_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Training  -  updatetrainingdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_vehicle.create_new_vehicle_detail`<a id="peoplehremployee_vehiclecreate_new_vehicle_detail"></a>

This API is used to create employee's new vehicle detail

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_vehicle_detail_response = peoplehr.employee_vehicle.create_new_vehicle_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    registration="RG003",
    make="ABC",
    model="A123",
    colour="Black",
    engine_size="A101",
    fuel_type="DF001",
    insurance_company="DF001",
    policy_number="123456A",
    mot_expiry_date="2017-01-01",
    insurance_expiry_date="2017-01-01",
    comments="Comments goes here",
    custom_columns=[
        {
            "column_name": "Demo",
            "column_value": "",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Pass base64 string",
            "description": "XYZ",
            "document_category": "XYZ",
            "signature_required": "false",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey to add employee's new vehicle detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to add employee's new vehicle detail

##### registration: `str`<a id="registration-str"></a>

Registration default value 

##### make: `str`<a id="make-str"></a>

Make default value 

##### model: `str`<a id="model-str"></a>

Model default value 

##### colour: `str`<a id="colour-str"></a>

Colour default value 

##### engine_size: `str`<a id="engine_size-str"></a>

EngineSize default value 

##### fuel_type: `str`<a id="fuel_type-str"></a>

FuelType default value 

##### insurance_company: `str`<a id="insurance_company-str"></a>

InsuranceCompany default value 

##### policy_number: `str`<a id="policy_number-str"></a>

PolicyNumber default value 

##### mot_expiry_date: `date`<a id="mot_expiry_date-date"></a>

MOTExpiryDate default value 

##### insurance_expiry_date: `date`<a id="insurance_expiry_date-date"></a>

InsuranceExpiryDate default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### custom_columns: [`CustomColumnsForEmployeeVehicleAddArray`](./people_hr_python_sdk/type/custom_columns_for_employee_vehicle_add_array.py)<a id="custom_columns-customcolumnsforemployeevehicleaddarraypeople_hr_python_sdktypecustom_columns_for_employee_vehicle_add_arraypy"></a>

CustomColumns to add employee's new vehicle detail

##### add_files: [`AddFilesForEmployeeVehicleAddArray`](./people_hr_python_sdk/type/add_files_for_employee_vehicle_add_array.py)<a id="add_files-addfilesforemployeevehicleaddarraypeople_hr_python_sdktypeadd_files_for_employee_vehicle_add_arraypy"></a>

AddFiles to add employee's new vehicle detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewVehicleDetailDefinition`](./people_hr_python_sdk/type/add_new_vehicle_detail_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewVehicleDetail`](./people_hr_python_sdk/pydantic/error_for_add_new_vehicle_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Vehicle  -  AddNewVehicleDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_vehicle.delete_detail`<a id="peoplehremployee_vehicledelete_detail"></a>

This API is used to delete employee's vehicle detail

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_detail_response = peoplehr.employee_vehicle.delete_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    vehicle_id=123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey to delete employee vehicle detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to delete employee's vehicle detail

##### vehicle_id: `int`<a id="vehicle_id-int"></a>

VehicleId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteVehicleDetailDefinition`](./people_hr_python_sdk/type/delete_vehicle_detail_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteVehicleDetail`](./people_hr_python_sdk/pydantic/error_for_delete_vehicle_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Vehicle  -  DeleteVehicleDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_vehicle.get_by_vehicle_detail_id`<a id="peoplehremployee_vehicleget_by_vehicle_detail_id"></a>

This API is used to get employee's vehicle detail by vehicle id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_vehicle_detail_id_response = peoplehr.employee_vehicle.get_by_vehicle_detail_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    vehicle_id=123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey to get employee's vehicle detail by vehicle id

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to get employee's vehicle detail

##### vehicle_id: `int`<a id="vehicle_id-int"></a>

VehicleId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetVehicleDetailByVehicleIdDefinition`](./people_hr_python_sdk/type/get_vehicle_detail_by_vehicle_id_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetVehicleDetailByVehicleId`](./people_hr_python_sdk/pydantic/error_for_get_vehicle_detail_by_vehicle_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Vehicle  -  GetByVehicleDetailId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_vehicle.get_detail_by_employee_id`<a id="peoplehremployee_vehicleget_detail_by_employee_id"></a>

This API is used to get employee's vehicle detail by employee id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_by_employee_id_response = peoplehr.employee_vehicle.get_detail_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey to get employee's vehicle detail by employee id

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to get employee's vehicle detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetVehicleDetailByEmployeeIdDefinition`](./people_hr_python_sdk/type/get_vehicle_detail_by_employee_id_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetVehicleDetailByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_vehicle_detail_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Vehicle  -  GetVehicleByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employee_vehicle.update_detail`<a id="peoplehremployee_vehicleupdate_detail"></a>

This API is used to update employee's vehicle detail

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_detail_response = peoplehr.employee_vehicle.update_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    registration="RG003",
    make="ABC",
    model="A123",
    colour="Black",
    engine_size="A101",
    fuel_type="DF001",
    insurance_company="DF001",
    policy_number="123456A",
    mot_expiry_date="2017-01-01",
    insurance_expiry_date="2017-01-01",
    comments="Comments goes here",
    custom_columns=[
        {
            "column_name": "Demo",
            "column_value": "",
        }
    ],
    add_files=[
        {
            "document_name": "my.txt",
            "file": "Pass base64 string",
            "description": "XYZ",
            "document_category": "XYZ",
            "signature_required": "false",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey to update employee vehicle detail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to update employee's vehicle detail

##### registration: `str`<a id="registration-str"></a>

Registration default value 

##### make: `str`<a id="make-str"></a>

Make default value 

##### model: `str`<a id="model-str"></a>

Model default value 

##### colour: `str`<a id="colour-str"></a>

Colour default value 

##### engine_size: `str`<a id="engine_size-str"></a>

EngineSize default value 

##### fuel_type: `str`<a id="fuel_type-str"></a>

FuelType default value 

##### insurance_company: `str`<a id="insurance_company-str"></a>

InsuranceCompany default value 

##### policy_number: `str`<a id="policy_number-str"></a>

PolicyNumber default value 

##### mot_expiry_date: `date`<a id="mot_expiry_date-date"></a>

MOTExpiryDate default value 

##### insurance_expiry_date: `date`<a id="insurance_expiry_date-date"></a>

InsuranceExpiryDate default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### custom_columns: [`CustomColumnsForEmployeeVehicleUpdateArray`](./people_hr_python_sdk/type/custom_columns_for_employee_vehicle_update_array.py)<a id="custom_columns-customcolumnsforemployeevehicleupdatearraypeople_hr_python_sdktypecustom_columns_for_employee_vehicle_update_arraypy"></a>

CustomColumns to update employee's vehicle detail

##### add_files: [`AddFilesForEmployeeVehicleUpdateArray`](./people_hr_python_sdk/type/add_files_for_employee_vehicle_update_array.py)<a id="add_files-addfilesforemployeevehicleupdatearraypeople_hr_python_sdktypeadd_files_for_employee_vehicle_update_arraypy"></a>

AddFiles to update employee's vehicle detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateVehicleDetailDefinition`](./people_hr_python_sdk/type/update_vehicle_detail_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateVehicleDetail`](./people_hr_python_sdk/pydantic/error_for_update_vehicle_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employee Vehicle  -  UpdateVehicleDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employeee_late.create_new_late`<a id="peoplehremployeee_latecreate_new_late"></a>

This API is used for add new late



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_late_response = peoplehr.employeee_late.create_new_late(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    late_date="2017-07-18",
    how_late=10,
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Employee late to add new late

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add new late

##### late_date: `date`<a id="late_date-date"></a>

Late Date default value 

##### how_late: `int`<a id="how_late-int"></a>

How late default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewLateParameters`](./people_hr_python_sdk/type/add_new_late_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewLate`](./people_hr_python_sdk/pydantic/error_for_add_new_late.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employeee Late  -  AddNewLate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employeee_late.delete_late`<a id="peoplehremployeee_latedelete_late"></a>

This API is used to delete late



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_late_response = peoplehr.employeee_late.delete_late(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    late_date="2017-07-18",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Employee late api to delete late record

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete late record

##### late_date: `date`<a id="late_date-date"></a>

Late Date default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeedeletelateParameter`](./people_hr_python_sdk/type/employeedeletelate_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorFordeletelate`](./people_hr_python_sdk/pydantic/error_fordeletelate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employeee Late  -  DeleteLate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employeee_late.get_by_employee_id`<a id="peoplehremployeee_lateget_by_employee_id"></a>

This API is used for get late by employeeId



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = peoplehr.employeee_late.get_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Employee late api for Get late by employee

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for Get late by employee

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetLateByEmployeeIdParameter`](./people_hr_python_sdk/type/get_late_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetLateByEmployeeId`](./people_hr_python_sdk/pydantic/error_for_get_late_by_employee_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employeee Late  -  GetLateByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.employeee_late.update_late`<a id="peoplehremployeee_lateupdate_late"></a>

This API is used for update late



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_late_response = peoplehr.employeee_late.update_late(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    late_date="2017-07-18",
    how_late=10,
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Employee late to update late

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update late

##### late_date: `date`<a id="late_date-date"></a>

Late Date default value 

##### how_late: `int`<a id="how_late-int"></a>

How late default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateLateParameters`](./people_hr_python_sdk/type/update_late_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpadteLate`](./people_hr_python_sdk/pydantic/error_for_upadte_late.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Employeee Late  -  UpdateLate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.history.get_by_employee_id_and_field_name`<a id="peoplehrhistoryget_by_employee_id_and_field_name"></a>

This API is used to get history by employeeId and fieldname details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_and_field_name_response = peoplehr.history.get_by_employee_id_and_field_name(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    field_name="EMPLOYEE_PERSONAL_FIRST_NAME",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for History to GetHistoryByEmployeeIdAndFieldName

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for get history by employeeId and fieldName

##### field_name: `str`<a id="field_name-str"></a>

FieldName default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetHistoryByEmployeeIdAndFieldNameParameter`](./people_hr_python_sdk/type/get_history_by_employee_id_and_field_name_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetHistoryByEmployeeIdAndFieldName`](./people_hr_python_sdk/pydantic/error_for_get_history_by_employee_id_and_field_name.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/History  -  GetHistoryByEmployeeIdAndFieldName` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.holiday_entitlement.get_holiday_entitlement`<a id="peoplehrholiday_entitlementget_holiday_entitlement"></a>

This API is used to get holiday entitlement details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_holiday_entitlement_response = peoplehr.holiday_entitlement.get_holiday_entitlement(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for holiday entitlement api to GetHolidayEntitlement

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get holiday entitlement

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetHolidayEntitlementParameter`](./people_hr_python_sdk/type/get_holiday_entitlement_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetHolidayEntitlement`](./people_hr_python_sdk/pydantic/error_for_get_holiday_entitlement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Holiday Entitlement  -  GetHolidayEntitlement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.holiday_entitlement.get_next_year_entitlement`<a id="peoplehrholiday_entitlementget_next_year_entitlement"></a>

This API is used to get next year holiday entitlement details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_next_year_entitlement_response = peoplehr.holiday_entitlement.get_next_year_entitlement(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for holiday entitlement api to GetNextYearHolidayEntitlement

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for get next year holiday entitlement

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetNextYearHolidayEntitlementParameter`](./people_hr_python_sdk/type/get_next_year_holiday_entitlement_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetNextYearHolidayEntitlement`](./people_hr_python_sdk/pydantic/error_for_get_next_year_holiday_entitlement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Holiday Entitlement  -  GetNextYearHolidayEntitlement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.holiday_entitlement.update_holiday_entitlement`<a id="peoplehrholiday_entitlementupdate_holiday_entitlement"></a>

This API is used to update holiday entitlement details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_holiday_entitlement_response = peoplehr.holiday_entitlement.update_holiday_entitlement(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    reason_for_change="Reason for change",
    entitlement_this_year="12.50",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for holiday entitlement api to UpdateHolidayEntitlement

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for update holiday entitlement

##### reason_for_change: [`ReasonForChange`](./people_hr_python_sdk/type/reason_for_change.py)<a id="reason_for_change-reasonforchangepeople_hr_python_sdktypereason_for_changepy"></a>

ReasonForChange for update holiday entitlement

##### entitlement_this_year: `str`<a id="entitlement_this_year-str"></a>

Entitlement this year default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateHolidayEntitlementParameter`](./people_hr_python_sdk/type/update_holiday_entitlement_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateHolidayEntitlement`](./people_hr_python_sdk/pydantic/error_for_update_holiday_entitlement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Holiday Entitlement  -  UpdateHolidayEntitlement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.holiday_entitlement.update_next_year_entitlement`<a id="peoplehrholiday_entitlementupdate_next_year_entitlement"></a>

This API is used to update next year holiday entitlement details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_next_year_entitlement_response = peoplehr.holiday_entitlement.update_next_year_entitlement(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    reason_for_change="Reason for change",
    entitlement_next_year="0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for holiday entitlement api to UpdateNextYearHolidayEntitlement

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

EmployeeId for update next year holiday entitlement

##### reason_for_change: [`ReasonForChange`](./people_hr_python_sdk/type/reason_for_change.py)<a id="reason_for_change-reasonforchangepeople_hr_python_sdktypereason_for_changepy"></a>

ReasonForChange for update next year holiday entitlement

##### entitlement_next_year: `str`<a id="entitlement_next_year-str"></a>

Entitlement next year default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateNextYearHolidayEntitlementParameter`](./people_hr_python_sdk/type/update_next_year_holiday_entitlement_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateNextYearHolidayEntitlement`](./people_hr_python_sdk/pydantic/error_for_update_next_year_holiday_entitlement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Holiday Entitlement  -  UpdateNextYearHolidayEntitlement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.maternity_paternity_.add_new_details`<a id="peoplehrmaternity_paternity_add_new_details"></a>

This API is used to add new maternity paternity details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_details_response = peoplehr.maternity_paternity_.add_new_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    due_date="2017-05-20",
    actual_start_date="2017-05-20",
    actual_end_date="2017-05-21",
    add_comments=[
        {
            "comment": "Comments goes here",
        }
    ],
    add_files=[
        {
            "document_name": "123.png",
            "file": "pass base64 string",
            "description": "dsadsadasdasd",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to AddNewMaternityPaternity

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for add new maternity paternity

##### due_date: `date`<a id="due_date-date"></a>

Due Date default value

##### actual_start_date: `date`<a id="actual_start_date-date"></a>

Actual start date default value 

##### actual_end_date: `date`<a id="actual_end_date-date"></a>

Actual end date default value 

##### add_comments: [`AddCommentsArrayForMaternityPaternity`](./people_hr_python_sdk/type/add_comments_array_for_maternity_paternity.py)<a id="add_comments-addcommentsarrayformaternitypaternitypeople_hr_python_sdktypeadd_comments_array_for_maternity_paternitypy"></a>

AddComments value

##### add_files: [`AddFilesArrayForAddNewMaternityPaternity`](./people_hr_python_sdk/type/add_files_array_for_add_new_maternity_paternity.py)<a id="add_files-addfilesarrayforaddnewmaternitypaternitypeople_hr_python_sdktypeadd_files_array_for_add_new_maternity_paternitypy"></a>

AddFiles info.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewMaternityPaternityParameter`](./people_hr_python_sdk/type/add_new_maternity_paternity_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForAddNewMaternityPaternityApi`](./people_hr_python_sdk/pydantic/error_for_add_new_maternity_paternity_api.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Maternity Paternity  -  AddNewMaternityPaternity` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.maternity_paternity_.delete_details`<a id="peoplehrmaternity_paternity_delete_details"></a>

This API is used to Delete Maternity Paternity Details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_details_response = peoplehr.maternity_paternity_.delete_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    maternity_paternity_txn_id=339,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to DeleteMaternityPaternity

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id value

##### maternity_paternity_txn_id: `int`<a id="maternity_paternity_txn_id-int"></a>

MaternityPaternityTxnId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteMaternityPaternityParameter`](./people_hr_python_sdk/type/delete_maternity_paternity_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteMaternityPaternity`](./people_hr_python_sdk/pydantic/error_for_delete_maternity_paternity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Maternity Paternity  -  DeleteMaternityPaternity` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.maternity_paternity_.get_by_employee_id`<a id="peoplehrmaternity_paternity_get_by_employee_id"></a>

This API is used to get maternity paternity by employeeid details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = peoplehr.maternity_paternity_.get_by_employee_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    actual_start_date="2017-05-20",
    actual_end_date="2017-05-21",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get by maternity paternity by employeeid

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get by maternity paternity by employeeid

##### actual_start_date: `date`<a id="actual_start_date-date"></a>

Actual start date default value 

##### actual_end_date: `date`<a id="actual_end_date-date"></a>

Actual end date default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetMaternityPaternityByEmployeeIdParameter`](./people_hr_python_sdk/type/get_maternity_paternity_by_employee_id_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetByMaternityPaternityByEmpId`](./people_hr_python_sdk/pydantic/error_for_get_by_maternity_paternity_by_emp_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Maternity Paternity  -  GetMaternityPaternityByEmployeeId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.maternity_paternity_.get_details_by_mat_pat_id`<a id="peoplehrmaternity_paternity_get_details_by_mat_pat_id"></a>

This API is used to get by maternity paternity id details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_mat_pat_id_response = peoplehr.maternity_paternity_.get_details_by_mat_pat_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    maternity_paternity_txn_id=339,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for get by maternity paternity

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employeeid for get by maternity paternity

##### maternity_paternity_txn_id: `int`<a id="maternity_paternity_txn_id-int"></a>

MaternityPaternityTxnId default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetByMaternityPaternityParameter`](./people_hr_python_sdk/type/get_by_maternity_paternity_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetByMaternityPaternityId`](./people_hr_python_sdk/pydantic/error_for_get_by_maternity_paternity_id.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Maternity Paternity  -  GetByMaternityPaternityId` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.maternity_paternity_.update_details`<a id="peoplehrmaternity_paternity_update_details"></a>

This API is used to Update Maternity Paternity Details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = peoplehr.maternity_paternity_.update_details(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    maternity_paternity_txn_id=339,
    due_date="2017-05-20",
    actual_start_date="2017-05-20",
    actual_end_date="2017-05-21",
    add_comments=[
        {
            "comment": "Comments goes here",
        }
    ],
    add_files=[
        {
            "document_name": "123.png",
            "file": "pass base64 string",
            "description": "dsadsadasdasd",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for employee api to UpdateMaternityPaternity

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee Id for update maternity paternity

##### maternity_paternity_txn_id: `int`<a id="maternity_paternity_txn_id-int"></a>

MaternityPaternityTxnId default value 

##### due_date: `date`<a id="due_date-date"></a>

Due Date default value

##### actual_start_date: `date`<a id="actual_start_date-date"></a>

Actual start date default value 

##### actual_end_date: `date`<a id="actual_end_date-date"></a>

Actual end date default value 

##### add_comments: [`AddCommentsArrayForMaternityPaternity`](./people_hr_python_sdk/type/add_comments_array_for_maternity_paternity.py)<a id="add_comments-addcommentsarrayformaternitypaternitypeople_hr_python_sdktypeadd_comments_array_for_maternity_paternitypy"></a>

AddComments

##### add_files: [`AddFilesArrayForAddNewMaternityPaternity`](./people_hr_python_sdk/type/add_files_array_for_add_new_maternity_paternity.py)<a id="add_files-addfilesarrayforaddnewmaternitypaternitypeople_hr_python_sdktypeadd_files_array_for_add_new_maternity_paternitypy"></a>

AddFiles info.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateMaternityPaternityParameter`](./people_hr_python_sdk/type/update_maternity_paternity_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForUpdateMaternityPaternityApi`](./people_hr_python_sdk/pydantic/error_for_update_maternity_paternity_api.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Maternity Paternity  -  UpdateMaternityPaternity` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.other_event.create_event_leave`<a id="peoplehrother_eventcreate_event_leave"></a>

This API is used to Add Other Event


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_event_leave_response = peoplehr.other_event.create_event_leave(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    duration_type=1,
    other_event_reason="Jury Duty",
    start_date="2016-07-27",
    end_date="2017-07-27",
    duration_in_days=1,
    start_time="02:00",
    end_time="04:00",
    comments="Comments goes here",
    add_files=[
        {
            "document_name": "123.pdf",
            "file": "Pass base64 string",
            "descriptions": "dsadsadasdasd",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for other event api to add other event leave

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add other event leave

##### duration_type: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="duration_type-bytepeople_hr_python_sdktypebytepy"></a>

Duration type default value 

##### other_event_reason: `str`<a id="other_event_reason-str"></a>

Other Event Reason default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### duration_in_days: `int`<a id="duration_in_days-int"></a>

Duration in days default value 

##### start_time: `str`<a id="start_time-str"></a>

StartTime default value 

##### end_time: `str`<a id="end_time-str"></a>

EndTime default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### add_files: [`Result1Foraddothereventleave`](./people_hr_python_sdk/type/result1_foraddothereventleave.py)<a id="add_files-result1foraddothereventleavepeople_hr_python_sdktyperesult1_foraddothereventleavepy"></a>

Add files for add other event leave

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddothereventleaveParameter`](./people_hr_python_sdk/type/addothereventleave_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForaddothereventleave`](./people_hr_python_sdk/pydantic/error_foraddothereventleave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Other Event  -  addothereventleave` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.other_event.delete_event`<a id="peoplehrother_eventdelete_event"></a>

This API is used to Delete Other Event


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_event_response = peoplehr.other_event.delete_event(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    other_leave_txn_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for other event api to DeleteOtherEvent

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for Delete Other Event

##### other_leave_txn_id: `int`<a id="other_leave_txn_id-int"></a>

Other Leave Txn Id default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleteOtherEventParameter`](./people_hr_python_sdk/type/delete_other_event_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForDeleteOtherEvent`](./people_hr_python_sdk/pydantic/error_for_delete_other_event.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Other Event  -  DeleteOtherEvent` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.other_event.get_detail`<a id="peoplehrother_eventget_detail"></a>

This API is used to get other event detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = peoplehr.other_event.get_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    start_date="2016-07-27",
    end_date="2017-07-27",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for other event api to getothereventdetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to get other event detail

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetothereventdetailParameter`](./people_hr_python_sdk/type/getothereventdetail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForgetothereventdetail`](./people_hr_python_sdk/pydantic/error_forgetothereventdetail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Other Event  -  getothereventdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.other_event.get_entitlement`<a id="peoplehrother_eventget_entitlement"></a>

This API is used to get other event entitlement


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_entitlement_response = peoplehr.other_event.get_entitlement(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for other event api to getotherevententitlement

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to get other event entitlement

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetotherevententitlementParameter`](./people_hr_python_sdk/type/getotherevententitlement_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForgetotherevententitlement`](./people_hr_python_sdk/pydantic/error_forgetotherevententitlement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Other Event  -  getotherevententitlement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.other_event.insert_update_entitlement`<a id="peoplehrother_eventinsert_update_entitlement"></a>

This API is used to Insert Update Other Event Entitlement


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
insert_update_entitlement_response = peoplehr.other_event.insert_update_entitlement(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    other_event_reason="Jury Duty",
    entitlement_recorded_in=1,
    this_year_entitlement=0,
    next_year_entitlement=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for other event api to addotherevententitlement

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add other event entitlement

##### other_event_reason: `str`<a id="other_event_reason-str"></a>

Other Event Reason default value 

##### entitlement_recorded_in: `int`<a id="entitlement_recorded_in-int"></a>

Entitlement Recorded In default value 

##### this_year_entitlement: `Union[int, float]`<a id="this_year_entitlement-unionint-float"></a>

This Year Entitlement default value 

##### next_year_entitlement: `Union[int, float]`<a id="next_year_entitlement-unionint-float"></a>

Next Year Entitlement default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddotherevententitlementParameter`](./people_hr_python_sdk/type/addotherevententitlement_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForaddotherevententitlement`](./people_hr_python_sdk/pydantic/error_foraddotherevententitlement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Other Event  -  addotherevententitlement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.other_event.update_event_leave`<a id="peoplehrother_eventupdate_event_leave"></a>

This API is used to Update Other Event


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_event_leave_response = peoplehr.other_event.update_event_leave(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    other_event_txn_id=1,
    duration_type=1,
    other_event_reason="Jury Duty",
    start_date="2016-07-27",
    end_date="2017-07-27",
    duration_in_days=1,
    start_time="02:00",
    end_time="04:00",
    comments="Comments goes here",
    add_files=[
        {
            "document_name": "123.pdf",
            "file": "Pass base64 string",
            "descriptions": "dsadsadasdasd",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for other event api to update other event leave

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update other event leave

##### other_event_txn_id: `int`<a id="other_event_txn_id-int"></a>

OtherEventTxnId default value 

##### duration_type: [`Byte`](./people_hr_python_sdk/type/byte.py)<a id="duration_type-bytepeople_hr_python_sdktypebytepy"></a>

Duration type default value 

##### other_event_reason: `str`<a id="other_event_reason-str"></a>

Other Event Reason default value 

##### start_date: `date`<a id="start_date-date"></a>

StartDate default value 

##### end_date: `date`<a id="end_date-date"></a>

StartDate default value 

##### duration_in_days: `int`<a id="duration_in_days-int"></a>

Duration in days default value 

##### start_time: `str`<a id="start_time-str"></a>

StartTime default value 

##### end_time: `str`<a id="end_time-str"></a>

EndTime default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

##### add_files: [`Result1Forupdateothereventleave`](./people_hr_python_sdk/type/result1_forupdateothereventleave.py)<a id="add_files-result1forupdateothereventleavepeople_hr_python_sdktyperesult1_forupdateothereventleavepy"></a>

Add Files for update other event leave

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateothereventleaveParameter`](./people_hr_python_sdk/type/updateothereventleave_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForupdateothereventleave`](./people_hr_python_sdk/pydantic/error_forupdateothereventleave.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Other Event  -  updateothereventleave` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.query.get_by_query_name`<a id="peoplehrqueryget_by_query_name"></a>

This API is used to get query result By query name details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_query_name_response = peoplehr.query.get_by_query_name(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    query_name="Absence",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for query api to GetQueryResultByQueryName

##### action: `str`<a id="action-str"></a>

Action default value

##### query_name: `str`<a id="query_name-str"></a>

QueryName default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetQueryResultByQueryNameParameter`](./people_hr_python_sdk/type/get_query_result_by_query_name_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetQueryResultByQueryName`](./people_hr_python_sdk/pydantic/error_for_get_query_result_by_query_name.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Query  -  GetQueryResultByQueryName` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.query.get_result_by_query_id`<a id="peoplehrqueryget_result_by_query_id"></a>

Deprecated.This API is used to get query result by query id details. It has been superseeded by Get Query Result By QueryName which returns date information in a UTC YYYY/MM/DD format


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_result_by_query_id_response = peoplehr.query.get_result_by_query_id(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    query_name="Absence",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for Query api to GetQueryResult

##### action: `str`<a id="action-str"></a>

Action default value

##### query_name: `str`<a id="query_name-str"></a>

QueryName default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetQueryResultParameter`](./people_hr_python_sdk/type/get_query_result_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetQueryResult`](./people_hr_python_sdk/pydantic/error_for_get_query_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Query  -  GetQueryResult` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.right_to_work.add_detail`<a id="peoplehrright_to_workadd_detail"></a>

This API is used to add right to work detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_detail_response = peoplehr.right_to_work.add_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    document_name="Abc.txt",
    file="Pass base64 string",
    document_type="Insurance Period",
    document_id=1,
    valid_from="2014-04-01",
    valid_to="2014-04-01",
    duration=1,
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for right to work  api to addrighttoworkdetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for add right to work detail

##### document_name: `str`<a id="document_name-str"></a>

DocumentName value

##### file: `str`<a id="file-str"></a>

File value

##### document_type: `str`<a id="document_type-str"></a>

Document Type default value 

##### document_id: [`LongInteger`](./people_hr_python_sdk/type/long_integer.py)<a id="document_id-longintegerpeople_hr_python_sdktypelong_integerpy"></a>

DocumentId default value 

##### valid_from: `date`<a id="valid_from-date"></a>

Valid From default value 

##### valid_to: `date`<a id="valid_to-date"></a>

Valid To default value 

##### duration: `int`<a id="duration-int"></a>

Duration Default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNewRightToWorkDetailParameter`](./people_hr_python_sdk/type/add_new_right_to_work_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForaddrighttoworkdetail`](./people_hr_python_sdk/pydantic/error_foraddrighttoworkdetail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Right To Work  -  addrighttoworkdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.right_to_work.delete_detail`<a id="peoplehrright_to_workdelete_detail"></a>

This API is used to delete right to work detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_detail_response = peoplehr.right_to_work.delete_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    right_to_work_txn_id=215,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for right to work api to deleterighttoworkdetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for delete right to work detail

##### right_to_work_txn_id: `int`<a id="right_to_work_txn_id-int"></a>

RightToWorkTxnId default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeleterighttoworkdetailParameter`](./people_hr_python_sdk/type/deleterighttoworkdetail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorFordeleterighttoworkdetail`](./people_hr_python_sdk/pydantic/error_fordeleterighttoworkdetail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Right To Work  -  deleterighttoworkdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.right_to_work.get_detail`<a id="peoplehrright_to_workget_detail"></a>

This API is used to get right to work detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = peoplehr.right_to_work.get_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for right to work api to GetRightToWorkDetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id to get employee detail

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetRightToWorkDetailParameter`](./people_hr_python_sdk/type/get_right_to_work_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForgetrighttoworkdetail`](./people_hr_python_sdk/pydantic/error_forgetrighttoworkdetail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Right To Work  -  getrighttoworkdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.right_to_work.update_detail`<a id="peoplehrright_to_workupdate_detail"></a>

This API is used to update right to work details


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_detail_response = peoplehr.right_to_work.update_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    employee_id="PW180",
    right_to_work_txn_id=215,
    document_name="Abc.txt",
    file="Pass base64 string",
    document_type="Insurance Period",
    document_id=1,
    valid_from="2014-04-01",
    valid_to="2014-04-01",
    duration=1,
    comments="Comments goes here",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for right to work api to updaterighttoworkdetail

##### action: `str`<a id="action-str"></a>

Action default value

##### employee_id: [`EmployeeId`](./people_hr_python_sdk/type/employee_id.py)<a id="employee_id-employeeidpeople_hr_python_sdktypeemployee_idpy"></a>

Employee id for update right to work detail

##### right_to_work_txn_id: `int`<a id="right_to_work_txn_id-int"></a>

RightToWorkTxnId default value

##### document_name: `str`<a id="document_name-str"></a>

DocumentName value

##### file: `str`<a id="file-str"></a>

File value

##### document_type: `str`<a id="document_type-str"></a>

Document Type default value 

##### document_id: [`LongInteger`](./people_hr_python_sdk/type/long_integer.py)<a id="document_id-longintegerpeople_hr_python_sdktypelong_integerpy"></a>

DocumentId default value 

##### valid_from: `date`<a id="valid_from-date"></a>

Valid From default value 

##### valid_to: `date`<a id="valid_to-date"></a>

Valid To default value 

##### duration: `int`<a id="duration-int"></a>

Duration Default value 

##### comments: `str`<a id="comments-str"></a>

Comments default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdaterighttoworkdetailParameter`](./people_hr_python_sdk/type/updaterighttoworkdetail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForupdaterighttoworkdetail`](./people_hr_python_sdk/pydantic/error_forupdaterighttoworkdetail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Right To Work  -  updaterighttoworkdetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.vacancy.add_new_vacancy`<a id="peoplehrvacancyadd_new_vacancy"></a>

This API is used to create new vacancy


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_vacancy_response = peoplehr.vacancy.add_new_vacancy(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    vacancy_name="IT Programmer",
    vacancy_description="IT Programmer",
    reference="VA4",
    is_cover_letter_mandatory="false",
    is_resume_mandatory="false",
    is_hide_salary="false",
    vacancy_type="Internal",
    company="Company name",
    location="Mumbai",
    department="IT",
    closing_date="2016-07-31",
    comment="Comment",
    salary_range="10000",
    job_description="Job Description",
    job_title="Software Engineer",
    city="Mumbai",
    country="India",
    experience="4 Year",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for vacancy api to create new vacancy

##### action: `str`<a id="action-str"></a>

Action default value

##### vacancy_name: `str`<a id="vacancy_name-str"></a>

Vacancy name default value 

##### vacancy_description: `str`<a id="vacancy_description-str"></a>

Title default value 

##### reference: `str`<a id="reference-str"></a>

Reference default value 

##### is_cover_letter_mandatory: [`IsCoverLetterMandatory`](./people_hr_python_sdk/type/is_cover_letter_mandatory.py)<a id="is_cover_letter_mandatory-iscoverlettermandatorypeople_hr_python_sdktypeis_cover_letter_mandatorypy"></a>

Is cover letter mandatory for create new vacancy

##### is_resume_mandatory: [`IsResumeMandatory`](./people_hr_python_sdk/type/is_resume_mandatory.py)<a id="is_resume_mandatory-isresumemandatorypeople_hr_python_sdktypeis_resume_mandatorypy"></a>

Is resume mandatory for create new vacancy

##### is_hide_salary: [`IsHideSalary`](./people_hr_python_sdk/type/is_hide_salary.py)<a id="is_hide_salary-ishidesalarypeople_hr_python_sdktypeis_hide_salarypy"></a>

Is hide salary for create new vacancy

##### vacancy_type: [`VacancyType`](./people_hr_python_sdk/type/vacancy_type.py)<a id="vacancy_type-vacancytypepeople_hr_python_sdktypevacancy_typepy"></a>

Vacancy type for create new vacancy

##### company: [`Company`](./people_hr_python_sdk/type/company.py)<a id="company-companypeople_hr_python_sdktypecompanypy"></a>

Company name for create new vacancy

##### location: `str`<a id="location-str"></a>

Location default value 

##### department: `str`<a id="department-str"></a>

Department default value 

##### closing_date: `date`<a id="closing_date-date"></a>

ClosingDate default value 

##### comment: [`Comment`](./people_hr_python_sdk/type/comment.py)<a id="comment-commentpeople_hr_python_sdktypecommentpy"></a>

Comment for create new vacancy

##### salary_range: `str`<a id="salary_range-str"></a>

SalaryRange default value 

##### job_description: `str`<a id="job_description-str"></a>

Job description default value 

##### job_title: `str`<a id="job_title-str"></a>

Job title default value 

##### city: `str`<a id="city-str"></a>

city default value 

##### country: `str`<a id="country-str"></a>

Country default value 

##### experience: `str`<a id="experience-str"></a>

Experience default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateVacancyDetailParameter`](./people_hr_python_sdk/type/create_vacancy_detail_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForCreateNewVacancy`](./people_hr_python_sdk/pydantic/error_for_create_new_vacancy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Vacancy  -  CreateNewVacancy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.vacancy.get_all_vacancies`<a id="peoplehrvacancyget_all_vacancies"></a>

This API is used to get all vacancies detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_vacancies_response = peoplehr.vacancy.get_all_vacancies(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for vacancy api to get all vacancy

##### action: `str`<a id="action-str"></a>

Action default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetAllVacancyParameters`](./people_hr_python_sdk/type/get_all_vacancy_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetAllVacancy`](./people_hr_python_sdk/pydantic/error_for_get_all_vacancy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Vacancy  -  GetAllVacancies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.vacancy.get_detail`<a id="peoplehrvacancyget_detail"></a>

This API is used to get vacancy detail


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = peoplehr.vacancy.get_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    vacancy_reference="VA4",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for vacancy api to get vacancy

##### action: `str`<a id="action-str"></a>

Action default value

##### vacancy_reference: `str`<a id="vacancy_reference-str"></a>

VacancyReference default value 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GetVacancyParameters`](./people_hr_python_sdk/type/get_vacancy_parameters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForGetVacancy`](./people_hr_python_sdk/pydantic/error_for_get_vacancy.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Vacancy  -  GetVacancy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peoplehr.work_pattern.get_work_detail`<a id="peoplehrwork_patternget_work_detail"></a>

This API is used to get work pattern detail



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_detail_response = peoplehr.work_pattern.get_work_detail(
    api_key="5127e153-2c80-492b-a9e4-fb3e50af61a8",
    action="string_example",
    work_pattern_id=2,
    work_pattern_name="xyz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: [`APIKey`](./people_hr_python_sdk/type/api_key.py)<a id="api_key-apikeypeople_hr_python_sdktypeapi_keypy"></a>

APIKey for applicant api to get Work pattern parameter detail

##### action: `str`<a id="action-str"></a>

Action default value

##### work_pattern_id: `int`<a id="work_pattern_id-int"></a>

Work pattern id default value

##### work_pattern_name: `str`<a id="work_pattern_name-str"></a>

Work pattern name default value

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkPatternParameter`](./people_hr_python_sdk/type/work_pattern_parameter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ErrorForWorkPattern`](./people_hr_python_sdk/pydantic/error_for_work_pattern.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/WorkPattern  -  GetWorkPatternDetail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
