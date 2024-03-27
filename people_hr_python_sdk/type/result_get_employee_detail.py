# coding: utf-8

"""
    PeopleHR API

    # Introduction  We think it's good to share. So we've created an open API to help you easily integrate People with other systems and applications, for seamless cross-platform data sharing.   The People API accepts and returns JSON data in the request body, with status indicating the outcome of the operation (sucess/failure).  # Developer Workbench  As well as this really useful documentation, we've also provided you with a handy API developer workbench. This allows you test your API calls against either a sandbox, or a live instance. A great place to start is the General Overview video, which explains how to use the workbench: https://intercom.help/peoplea-apps/api-and-integration/api  You can access the developer work bench here: https://api.peoplehr.net/pages/functional   # Sandbox If you need a sandbox account to test your creation, just email customerservices@peoplehr.com and we will help you set one up.   # Authentication The People API uses API keys for each call. To receive an API key, ask your system administrator to generate one from within Settings. For authentication, all API calls need the API key to be passed along with the JSON data sent as part of the http request. Never share your API keys. Keep them guarded and secure.   # Managed Lists  Within People, there are a number of fields called Managed Lists, better known as dropdowns. When you insert an item of data into a field that is a Managed List, then the API will automatically create you an entry in the Managed List for that field.  # Rate Limit Detail  The API rate limit is set to 30 calls a minute from a specific IP address. If you attempt to call the API above the rate limit, then an exception message will be returned. If you would like your rate limit increased, please submit a request to customerservices@peoplehr.com. In your email, please explain why you would like your limit increasing.   # Webhooks Detail  People provides an option to use webhooks to receive notifications of changes in particular transactions. If you are going to use the webhook mechanism, we advise you to set up a generic listener service to receive callbacks.   To set up a webhook listener URL, select Settings, API, and then enter your listner URL into the field.    The following actions are available and the data packet will return the following (example data shown):    New Starter Added > ActionId:1, Action:New Starter Added, EmployeeId:PW21    Employee personal detail update > ActionId:2, Action:Employee Detail Updated, EmployeeId:PW1, FieldName:Other Name(s), NewValue:Am, OldValue:zz, Reason:Test    Leaver > ActionId:3, Action:Marked Leaver, EmployeeId:PW21    Holiday added > ActionId:4, Action:Holiday Added, EmployeeId:PW13, HolidayType:A day or more, StartDate:2016-06-13, EndDate:2016-06-15, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.50, Comments:part day testing, IsToilHoliday:No    Holiday Updated > ActionId:5, Action:Holiday Updated, EmployeeId:PW51, HolidayType:A day or more, OriginalStartDate:2016-05-04, OriginalEndDate:2016-05-04, OriginalPartOfDay:, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-05-04, EndDate:2016-05-05, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1.50, Comments:Test, IsToilHoliday:No    Holiday Deleted > ActionId:6, Action:Holiday Deleted, EmployeeId:PW13, StartDate:2016-01-18, EndDate:2016-01-19, HolidayRecordedIn:Days, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.00, Comments:zz    Holiday Requested > ActionId:7, Action:New Holiday Request, EmployeeId:PW97, HolidayType:A day or more, StartDate:2017-06-22, EndDate:2017-06-23, HolidayRecordedIn:Days, PartOfDay: StartDatePartOfTheDay:, EndDatePartOfTheDay:, Duration:2.00, Comments:Graduation, IsToilHoliday:No    Holiday Approved > ActionId:8, Action:Holiday Approved, EmployeeId:PW391, StartDate:2017-06-15, EndDate:2017-06-15, HolidayRecordedIn:Days, Duration:0.5, Comments:, AuthorisedByFirstName:Richard, AuthorisedByLastName:Palmer, HolidayType:Less than a day, PartOfDay:AM, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No    Holiday Rejected > ActionId:9, Action:Holiday Rejected, EmployeeId:PW29, StartDate:2017-07-12, EndDate:2017-07-12, HolidayRecordedIn:Days, Duration:1, Comments:Unfortunately this is, fully booked, AuthorisedByFirstName:Debi, AuthorisedByLastName:Stokes, HolidayType:A day or more, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No    Sick Added > ActionId:10, Action:Sick Added, EmployeeId:PW13, Reason:Accident, StartDate:2016-01-19, EndDate:2016-01-19, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments:    Sick Updated > ActionId:11, Action:Sick Updated, EmployeeId:PW13, Reason:Accident, OriginalStartDate:2016-01-18, OriginalEndDate:2016-01-19, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-01-18, EndDate:2016-01-19, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1, Comments:    Sick Deleted > ActionId:12, Action:Sick Deleted, EmployeeId:PW13, Reason:Cold/Flu, StartDate:2016-01-21, EndDate:2016-01-21, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments:    Maternity / Paternity Added > ActionId:13, Action:Maternity/Paternity Added, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-24    Maternity / Paternity Updated > ActionId:14, Action:Maternity/Paternity Updated, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25    Maternity / Paternity Deleted > ActionId:15, Action:Maternity/Paternity Deleted, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25    Late Added > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:10, Comments:    Late Updated > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments:    Late Deleted > ActionId:17, Action:Late Deleted, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments:    Employee Deleted > ActionId:18, Action:Employee Deleted, EmployeeId:PW21    Other Event Updated > ActionId:21, Action:Other Event Updated, EmployeeId:PW5-2, OriginalStartDate:2016-06-25, OriginalEndDate:2016-06-25, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Days, OriginalDurationType:Days, OriginalDuration:1.00, OriginalStartTime:, OriginalEndTime:    Other Event Deleted > ActionId:22, Action:Other Event Deleted, EmployeeId:PW5-2, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Day, StartTime:, EndTime:    Other Event Requested > ActionId:23, Action:New Other Event Request, EmployeeId:S20, Reason:Flexi, StartDate:2017-06-16, StartTime:09:00:00, EndTime:12:30:00, Duration:210, Comments:, DurationType:Hours    Other Event Approved > ActionId:24, Action:Other Event Approved, EmployeeId:180, StartDate:2017-06-14, EndDate:2017-06-14, Comments:, AuthorisedByFirstName:Damith, Duration:2 Hrs 0 Mins (02:00 - 04:00), Reason:Short Leave    Other Event Rejected > ActionId:25, Action:Other Event Rejected, EmployeeId:312, StartDate:2017-09-13, EndDate:2017-09-13, Comments:already 2 x nurse on AL, AuthorisedByFirstName:Dirkje (Dorien), Duration:1 Day, Reason:Request To Work    Appraisals Logbook > ActionId:31, Action:Appraisal Add, EmployeeId:PW8996, TxnId:1, ScreenType:1    ActionId:32 > Action:Appraisal Update, EmployeeId:PW8996, TxnId:1, ScreenType:1    ActionId:33 > Action:Appraisal Delete, EmployeeId:PW8996, TxnId:1, ScreenType:1    Benefit Logbook > ActionId:34, Action:Benefit Add, EmployeeId:PW8996, TxnId:1, ScreenType:2    ActionId:35 > Action:Benefit Update, EmployeeId:PW8996, TxnId:1, ScreenType:2    ActionId:36 > Action:Benefit Delete, EmployeeId:PW8996, TxnId:1, ScreenType:2    CPD Logbook > ActionId:37, Action:CPD Add, EmployeeId:PW8996, TxnId:1, ScreenType:3    ActionId:38 > Action:CPD Update, EmployeeId:PW8996, TxnId:1, ScreenType:3    ActionId:39 > Action:CPD Delete, EmployeeId:PW8996, TxnId:1, ScreenType:3    Driving Licence Logbook > ActionId:40, Action:Driving Licence Add, EmployeeId:PW8996, TxnId:1, ScreenType:6    ActionId:41 > Action:Driving Licence Update, EmployeeId:PW8996, TxnId:1, ScreenType:6    ActionId:42 > Action:Driving Licence Delete, EmployeeId:PW8996, TxnId:1, ScreenType:6    Qualification Logbook > ActionId:43, Action:Qualification Add, EmployeeId:PW8996, TxnId:1, ScreenType:4    ActionId:44 > , Action:Qualification Update, EmployeeId:PW8996, TxnId:1, ScreenType:4    ActionId:45 > Action:Qualification Delete, EmployeeId:PW8996, TxnId:1, ScreenType:4    Training Logbook > ActionId:46, Action:Training Add, EmployeeId:PW8996, TxnId:1, ScreenType:5    ActionId:47 > Action:Training Update, EmployeeId:PW8996, TxnId:1, ScreenType:5    ActionId:48 > Action:Training Delete, EmployeeId:PW8996, TxnId:1, ScreenType:5    Vehicle Logbook > ActionId:49, Action:Vehicle Add, EmployeeId:PW8996, TxnId:1, ScreenType:7    ActionId:50 > Action:Vehicle Update, EmployeeId:PW8996, TxnId:1, ScreenType:7    ActionId:51 > Action:Vehicle Delete, EmployeeId:PW8996, TxnId:1, ScreenType:7    Custom Logbook > ActionId:52, Action:Custom Screen Add, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10    ActionId:53 > Action:Custom Screen Update, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10    ActionId:54 > Action:Custom Screen Delete, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10   Keys    The unique key for an event on the People calendar is Start Date and End Date -- you should also use the same key to identify record in your system that is consuming the data from People - the reason you need to do this is to locate the original record within your system when you get a notification of an update or a deletion - you will notice the message fragment contains the original dates - so you can locate the record - and the new dates.  Another more sophisticated option is to use the transaction ID. Holiday, Sick, Other Event and Maternity/Paternity transactions within People allow you to store an external transaction. Using this approach you could store the transaction id from a calendering system such as Outlook. If the holiday record on People is amended or deleted you will be able to determine the corresponding record in Outlook.    Take the following scenario:    If you create holidays through the API you will receive AnnualLeaveTxnId in the API result set. Any integration can store this as a reference from People HR holidays mapping    If you create holidays within the People HR UI, you will receive webhook details with holidays details. Integrated applications need to call people holidays GET details API with the current webhook details. That will give you AnnualLeaveTxnID & ReferenceId (If any). Now you can save the AnnualLeaveTxnId in an integrated application as People HR holidays mapping.    You can store third party application holidays/transaction references into the People HR system by calling the API Employee Holiday -> Update Holiday Reference ID    If you want to update/delete any holidays from People HR that are already mapped with third party applications/integrations, you can call holidays API to match with reference ID. You will get assoicated data with the reference ID that you actually need to update/ delete holidays from the people system (Employee Holiday -> UpdateHoliday or Employee Holiday -> DeleteHoliday).   Start Part of Day and End Part of Day In People it is possible to record half days both at the beginning of a holiday or sick event or at the end. You can determine this by looking at the StartPartOfDay and EndPartOfDay values which will either be blank, AM or PM.    # Examples We've put a few examples together for you that might help you get started:  HTML Coding Examples: https://help.peoplehr.com/en/articles/981415-api-html-examples  c# Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-c-code-snippet  Objective C Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-code-snippets-objective-c  How to use Postman with the API: http://intercom.help/peoplea-apps/api-and-integration/api-using-postman  <!-- ReDoc-Inject: <security-definitions> --> 

    The version of the OpenAPI document: 3.1
    Contact: customerservices@peoplehr.com
    Created by: https://www.peoplehr.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from people_hr_python_sdk.type.background_detail_object import BackgroundDetailObject
from people_hr_python_sdk.type.bank_detail_object import BankDetailObject
from people_hr_python_sdk.type.company_object import CompanyObject
from people_hr_python_sdk.type.contact_detail_object import ContactDetailObject
from people_hr_python_sdk.type.date_of_birth_object import DateOfBirthObject
from people_hr_python_sdk.type.department_object import DepartmentObject
from people_hr_python_sdk.type.email_id_object import EmailIdObject
from people_hr_python_sdk.type.employee_id_array_object import EmployeeIdArrayObject
from people_hr_python_sdk.type.employment_detail_object import EmploymentDetailObject
from people_hr_python_sdk.type.employment_type_object import EmploymentTypeObject
from people_hr_python_sdk.type.first_name_object import FirstNameObject
from people_hr_python_sdk.type.gender_object import GenderObject
from people_hr_python_sdk.type.job_role_object import JobRoleObject
from people_hr_python_sdk.type.known_as_object import KnownAsObject
from people_hr_python_sdk.type.last_name_object import LastNameObject
from people_hr_python_sdk.type.location_object import LocationObject
from people_hr_python_sdk.type.lst_field_history_jobrole import LstFieldHistoryJobrole
from people_hr_python_sdk.type.nationality_object import NationalityObject
from people_hr_python_sdk.type.nis_number_object import NISNumberObject
from people_hr_python_sdk.type.notice_period_object import NoticePeriodObject
from people_hr_python_sdk.type.other_contact_object import OtherContactObject
from people_hr_python_sdk.type.other_name_object import OtherNameObject
from people_hr_python_sdk.type.probation_end_date_object import ProbationEndDateObject
from people_hr_python_sdk.type.reports_to_object import ReportsToObject
from people_hr_python_sdk.type.result_get_employee_detail_company_effective_date import ResultGetEmployeeDetailCompanyEffectiveDate
from people_hr_python_sdk.type.result_get_employee_detail_department_effective_date import ResultGetEmployeeDetailDepartmentEffectiveDate
from people_hr_python_sdk.type.result_get_employee_detail_employee_status import ResultGetEmployeeDetailEmployeeStatus
from people_hr_python_sdk.type.result_get_employee_detail_employment_type_effective_date import ResultGetEmployeeDetailEmploymentTypeEffectiveDate
from people_hr_python_sdk.type.result_get_employee_detail_holiday_allowance_days import ResultGetEmployeeDetailHolidayAllowanceDays
from people_hr_python_sdk.type.result_get_employee_detail_holiday_allowance_mins import ResultGetEmployeeDetailHolidayAllowanceMins
from people_hr_python_sdk.type.result_get_employee_detail_job_role_change_date import ResultGetEmployeeDetailJobRoleChangeDate
from people_hr_python_sdk.type.result_get_employee_detail_location_effective_date import ResultGetEmployeeDetailLocationEffectiveDate
from people_hr_python_sdk.type.result_get_employee_detail_reports_to_effective_date import ResultGetEmployeeDetailReportsToEffectiveDate
from people_hr_python_sdk.type.result_get_employee_detail_reports_to_email_address import ResultGetEmployeeDetailReportsToEmailAddress
from people_hr_python_sdk.type.result_get_employee_detail_reports_to_employee_id import ResultGetEmployeeDetailReportsToEmployeeId
from people_hr_python_sdk.type.right_to_work_object import RightToWorkObject
from people_hr_python_sdk.type.start_date_object import StartDateObject
from people_hr_python_sdk.type.title_object import TitleObject

class RequiredResultGetEmployeeDetail(TypedDict):
    pass

class OptionalResultGetEmployeeDetail(TypedDict, total=False):
    # EmployeeId contain displayValue and FieldHistory array
    EmployeeId: EmployeeIdArrayObject

    #  Title 
    Title: TitleObject

    # FirstName of employee 
    FirstName: FirstNameObject

    # LastName of employee 
    LastName: LastNameObject

    # OtherName of employee 
    OtherName: OtherNameObject

    # KnownAs
    KnownAs: KnownAsObject

    # EmailId of employee
    EmailId: EmailIdObject

    # StartDate of employee
    StartDate: StartDateObject

    # DateOfBirth of employee
    DateOfBirth: DateOfBirthObject

    # JobRole of employee
    JobRole: JobRoleObject

    # Company name of employee
    Company: CompanyObject

    CompanyEffectiveDate: ResultGetEmployeeDetailCompanyEffectiveDate

    # Location name of employee
    Location: LocationObject

    LocationEffectiveDate: ResultGetEmployeeDetailLocationEffectiveDate

    # Department name of employee
    Department: DepartmentObject

    DepartmentEffectiveDate: ResultGetEmployeeDetailDepartmentEffectiveDate

    JobRoleChangeDate: ResultGetEmployeeDetailJobRoleChangeDate

    # Reports to value
    ReportsTo: ReportsToObject

    ReportsToEffectiveDate: ResultGetEmployeeDetailReportsToEffectiveDate

    ReportsToEmployeeId: ResultGetEmployeeDetailReportsToEmployeeId

    ReportsToEmailAddress: ResultGetEmployeeDetailReportsToEmailAddress

    # NIS number value
    NISNumber: NISNumberObject

    # Nationality value
    Nationality: NationalityObject

    # Employment type value
    EmploymentType: EmploymentTypeObject

    EmploymentTypeEffectiveDate: ResultGetEmployeeDetailEmploymentTypeEffectiveDate

    EmployeeStatus: ResultGetEmployeeDetailEmployeeStatus

    HolidayAllowanceDays: ResultGetEmployeeDetailHolidayAllowanceDays

    HolidayAllowanceMins: ResultGetEmployeeDetailHolidayAllowanceMins

    # Notice period value
    NoticePeriod: NoticePeriodObject

    # Probation end date value
    ProbationEndDate: ProbationEndDateObject

    # Gender value
    Gender: GenderObject

    # Contact detail value
    ContactDetail: ContactDetailObject

    # Other Contact detail value
    OtherContact: OtherContactObject

    # Right to work value
    RightToWork: RightToWorkObject

    # Background detail value
    BackgroundDetail: BackgroundDetailObject

    # Bank detail value
    BankDetail: BankDetailObject

    # Employment detail value
    EmploymentDetail: EmploymentDetailObject

    # LeavingDate default value 
    LeavingDate: str

    # ReasonforLeaving default value 
    ReasonForLeaving: str

    # Employee Image default value 
    EmployeeImage: str

    # APIColumn1 default value 
    APIColumn1: str

    # APIColumn2 default value 
    APIColumn2: str

    # APIColumn3 default value 
    APIColumn3: str

    # APIColumn4 default value 
    APIColumn4: str

    # APIColumn5 default value 
    APIColumn5: str

    # list of Field history job role
    lstFieldHistoryJobrole: LstFieldHistoryJobrole

class ResultGetEmployeeDetail(RequiredResultGetEmployeeDetail, OptionalResultGetEmployeeDetail):
    pass
