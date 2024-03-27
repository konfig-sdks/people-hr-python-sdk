# coding: utf-8

"""
    PeopleHR API

    # Introduction  We think it's good to share. So we've created an open API to help you easily integrate People with other systems and applications, for seamless cross-platform data sharing.   The People API accepts and returns JSON data in the request body, with status indicating the outcome of the operation (sucess/failure).  # Developer Workbench  As well as this really useful documentation, we've also provided you with a handy API developer workbench. This allows you test your API calls against either a sandbox, or a live instance. A great place to start is the General Overview video, which explains how to use the workbench: https://intercom.help/peoplea-apps/api-and-integration/api  You can access the developer work bench here: https://api.peoplehr.net/pages/functional   # Sandbox If you need a sandbox account to test your creation, just email customerservices@peoplehr.com and we will help you set one up.   # Authentication The People API uses API keys for each call. To receive an API key, ask your system administrator to generate one from within Settings. For authentication, all API calls need the API key to be passed along with the JSON data sent as part of the http request. Never share your API keys. Keep them guarded and secure.   # Managed Lists  Within People, there are a number of fields called Managed Lists, better known as dropdowns. When you insert an item of data into a field that is a Managed List, then the API will automatically create you an entry in the Managed List for that field.  # Rate Limit Detail  The API rate limit is set to 30 calls a minute from a specific IP address. If you attempt to call the API above the rate limit, then an exception message will be returned. If you would like your rate limit increased, please submit a request to customerservices@peoplehr.com. In your email, please explain why you would like your limit increasing.   # Webhooks Detail  People provides an option to use webhooks to receive notifications of changes in particular transactions. If you are going to use the webhook mechanism, we advise you to set up a generic listener service to receive callbacks.   To set up a webhook listener URL, select Settings, API, and then enter your listner URL into the field.    The following actions are available and the data packet will return the following (example data shown):    New Starter Added > ActionId:1, Action:New Starter Added, EmployeeId:PW21    Employee personal detail update > ActionId:2, Action:Employee Detail Updated, EmployeeId:PW1, FieldName:Other Name(s), NewValue:Am, OldValue:zz, Reason:Test    Leaver > ActionId:3, Action:Marked Leaver, EmployeeId:PW21    Holiday added > ActionId:4, Action:Holiday Added, EmployeeId:PW13, HolidayType:A day or more, StartDate:2016-06-13, EndDate:2016-06-15, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.50, Comments:part day testing, IsToilHoliday:No    Holiday Updated > ActionId:5, Action:Holiday Updated, EmployeeId:PW51, HolidayType:A day or more, OriginalStartDate:2016-05-04, OriginalEndDate:2016-05-04, OriginalPartOfDay:, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-05-04, EndDate:2016-05-05, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1.50, Comments:Test, IsToilHoliday:No    Holiday Deleted > ActionId:6, Action:Holiday Deleted, EmployeeId:PW13, StartDate:2016-01-18, EndDate:2016-01-19, HolidayRecordedIn:Days, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.00, Comments:zz    Holiday Requested > ActionId:7, Action:New Holiday Request, EmployeeId:PW97, HolidayType:A day or more, StartDate:2017-06-22, EndDate:2017-06-23, HolidayRecordedIn:Days, PartOfDay: StartDatePartOfTheDay:, EndDatePartOfTheDay:, Duration:2.00, Comments:Graduation, IsToilHoliday:No    Holiday Approved > ActionId:8, Action:Holiday Approved, EmployeeId:PW391, StartDate:2017-06-15, EndDate:2017-06-15, HolidayRecordedIn:Days, Duration:0.5, Comments:, AuthorisedByFirstName:Richard, AuthorisedByLastName:Palmer, HolidayType:Less than a day, PartOfDay:AM, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No    Holiday Rejected > ActionId:9, Action:Holiday Rejected, EmployeeId:PW29, StartDate:2017-07-12, EndDate:2017-07-12, HolidayRecordedIn:Days, Duration:1, Comments:Unfortunately this is, fully booked, AuthorisedByFirstName:Debi, AuthorisedByLastName:Stokes, HolidayType:A day or more, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No    Sick Added > ActionId:10, Action:Sick Added, EmployeeId:PW13, Reason:Accident, StartDate:2016-01-19, EndDate:2016-01-19, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments:    Sick Updated > ActionId:11, Action:Sick Updated, EmployeeId:PW13, Reason:Accident, OriginalStartDate:2016-01-18, OriginalEndDate:2016-01-19, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-01-18, EndDate:2016-01-19, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1, Comments:    Sick Deleted > ActionId:12, Action:Sick Deleted, EmployeeId:PW13, Reason:Cold/Flu, StartDate:2016-01-21, EndDate:2016-01-21, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments:    Maternity / Paternity Added > ActionId:13, Action:Maternity/Paternity Added, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-24    Maternity / Paternity Updated > ActionId:14, Action:Maternity/Paternity Updated, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25    Maternity / Paternity Deleted > ActionId:15, Action:Maternity/Paternity Deleted, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25    Late Added > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:10, Comments:    Late Updated > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments:    Late Deleted > ActionId:17, Action:Late Deleted, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments:    Employee Deleted > ActionId:18, Action:Employee Deleted, EmployeeId:PW21    Other Event Updated > ActionId:21, Action:Other Event Updated, EmployeeId:PW5-2, OriginalStartDate:2016-06-25, OriginalEndDate:2016-06-25, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Days, OriginalDurationType:Days, OriginalDuration:1.00, OriginalStartTime:, OriginalEndTime:    Other Event Deleted > ActionId:22, Action:Other Event Deleted, EmployeeId:PW5-2, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Day, StartTime:, EndTime:    Other Event Requested > ActionId:23, Action:New Other Event Request, EmployeeId:S20, Reason:Flexi, StartDate:2017-06-16, StartTime:09:00:00, EndTime:12:30:00, Duration:210, Comments:, DurationType:Hours    Other Event Approved > ActionId:24, Action:Other Event Approved, EmployeeId:180, StartDate:2017-06-14, EndDate:2017-06-14, Comments:, AuthorisedByFirstName:Damith, Duration:2 Hrs 0 Mins (02:00 - 04:00), Reason:Short Leave    Other Event Rejected > ActionId:25, Action:Other Event Rejected, EmployeeId:312, StartDate:2017-09-13, EndDate:2017-09-13, Comments:already 2 x nurse on AL, AuthorisedByFirstName:Dirkje (Dorien), Duration:1 Day, Reason:Request To Work    Appraisals Logbook > ActionId:31, Action:Appraisal Add, EmployeeId:PW8996, TxnId:1, ScreenType:1    ActionId:32 > Action:Appraisal Update, EmployeeId:PW8996, TxnId:1, ScreenType:1    ActionId:33 > Action:Appraisal Delete, EmployeeId:PW8996, TxnId:1, ScreenType:1    Benefit Logbook > ActionId:34, Action:Benefit Add, EmployeeId:PW8996, TxnId:1, ScreenType:2    ActionId:35 > Action:Benefit Update, EmployeeId:PW8996, TxnId:1, ScreenType:2    ActionId:36 > Action:Benefit Delete, EmployeeId:PW8996, TxnId:1, ScreenType:2    CPD Logbook > ActionId:37, Action:CPD Add, EmployeeId:PW8996, TxnId:1, ScreenType:3    ActionId:38 > Action:CPD Update, EmployeeId:PW8996, TxnId:1, ScreenType:3    ActionId:39 > Action:CPD Delete, EmployeeId:PW8996, TxnId:1, ScreenType:3    Driving Licence Logbook > ActionId:40, Action:Driving Licence Add, EmployeeId:PW8996, TxnId:1, ScreenType:6    ActionId:41 > Action:Driving Licence Update, EmployeeId:PW8996, TxnId:1, ScreenType:6    ActionId:42 > Action:Driving Licence Delete, EmployeeId:PW8996, TxnId:1, ScreenType:6    Qualification Logbook > ActionId:43, Action:Qualification Add, EmployeeId:PW8996, TxnId:1, ScreenType:4    ActionId:44 > , Action:Qualification Update, EmployeeId:PW8996, TxnId:1, ScreenType:4    ActionId:45 > Action:Qualification Delete, EmployeeId:PW8996, TxnId:1, ScreenType:4    Training Logbook > ActionId:46, Action:Training Add, EmployeeId:PW8996, TxnId:1, ScreenType:5    ActionId:47 > Action:Training Update, EmployeeId:PW8996, TxnId:1, ScreenType:5    ActionId:48 > Action:Training Delete, EmployeeId:PW8996, TxnId:1, ScreenType:5    Vehicle Logbook > ActionId:49, Action:Vehicle Add, EmployeeId:PW8996, TxnId:1, ScreenType:7    ActionId:50 > Action:Vehicle Update, EmployeeId:PW8996, TxnId:1, ScreenType:7    ActionId:51 > Action:Vehicle Delete, EmployeeId:PW8996, TxnId:1, ScreenType:7    Custom Logbook > ActionId:52, Action:Custom Screen Add, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10    ActionId:53 > Action:Custom Screen Update, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10    ActionId:54 > Action:Custom Screen Delete, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10   Keys    The unique key for an event on the People calendar is Start Date and End Date -- you should also use the same key to identify record in your system that is consuming the data from People - the reason you need to do this is to locate the original record within your system when you get a notification of an update or a deletion - you will notice the message fragment contains the original dates - so you can locate the record - and the new dates.  Another more sophisticated option is to use the transaction ID. Holiday, Sick, Other Event and Maternity/Paternity transactions within People allow you to store an external transaction. Using this approach you could store the transaction id from a calendering system such as Outlook. If the holiday record on People is amended or deleted you will be able to determine the corresponding record in Outlook.    Take the following scenario:    If you create holidays through the API you will receive AnnualLeaveTxnId in the API result set. Any integration can store this as a reference from People HR holidays mapping    If you create holidays within the People HR UI, you will receive webhook details with holidays details. Integrated applications need to call people holidays GET details API with the current webhook details. That will give you AnnualLeaveTxnID & ReferenceId (If any). Now you can save the AnnualLeaveTxnId in an integrated application as People HR holidays mapping.    You can store third party application holidays/transaction references into the People HR system by calling the API Employee Holiday -> Update Holiday Reference ID    If you want to update/delete any holidays from People HR that are already mapped with third party applications/integrations, you can call holidays API to match with reference ID. You will get assoicated data with the reference ID that you actually need to update/ delete holidays from the people system (Employee Holiday -> UpdateHoliday or Employee Holiday -> DeleteHoliday).   Start Part of Day and End Part of Day In People it is possible to record half days both at the beginning of a holiday or sick event or at the end. You can determine this by looking at the StartPartOfDay and EndPartOfDay values which will either be blank, AM or PM.    # Examples We've put a few examples together for you that might help you get started:  HTML Coding Examples: https://help.peoplehr.com/en/articles/981415-api-html-examples  c# Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-c-code-snippet  Objective C Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-code-snippets-objective-c  How to use Postman with the API: http://intercom.help/peoplea-apps/api-and-integration/api-using-postman  <!-- ReDoc-Inject: <security-definitions> --> 

    The version of the OpenAPI document: 3.1
    Contact: customerservices@peoplehr.com
    Created by: https://www.peoplehr.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from people_hr_python_sdk import schemas  # noqa: F401


class CreateEmployeeDetailParameter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "JobRole",
            "StartDate",
            "APIKey",
            "Action",
            "Department",
            "FirstName",
            "JobRoleEffectiveDate",
            "LastName",
            "EmployeeId",
            "Location",
        }
        
        class properties:
        
            @staticmethod
            def APIKey() -> typing.Type['APIKey']:
                return APIKey
            Action = schemas.StrSchema
        
            @staticmethod
            def EmployeeId() -> typing.Type['EmployeeId']:
                return EmployeeId
        
            @staticmethod
            def FirstName() -> typing.Type['FirstName']:
                return FirstName
        
            @staticmethod
            def LastName() -> typing.Type['LastName']:
                return LastName
            StartDate = schemas.DateSchema
        
            @staticmethod
            def JobRole() -> typing.Type['JobRole']:
                return JobRole
            JobRoleEffectiveDate = schemas.DateSchema
            Location = schemas.StrSchema
            Department = schemas.StrSchema
        
            @staticmethod
            def Title() -> typing.Type['Title']:
                return Title
        
            @staticmethod
            def Email() -> typing.Type['Email']:
                return Email
        
            @staticmethod
            def Gender() -> typing.Type['Gender']:
                return Gender
            DateOfBirth = schemas.DateSchema
        
            @staticmethod
            def ReportsTo() -> typing.Type['ReportsTo']:
                return ReportsTo
        
            @staticmethod
            def Company() -> typing.Type['Company']:
                return Company
        
            @staticmethod
            def NationalInsuranceNumber() -> typing.Type['NationalInsuranceNumber']:
                return NationalInsuranceNumber
        
            @staticmethod
            def Nationality() -> typing.Type['Nationality']:
                return Nationality
        
            @staticmethod
            def EmploymentType() -> typing.Type['EmploymentType']:
                return EmploymentType
            EntitlementThisYear = schemas.StrSchema
            EntitlementNextYear = schemas.StrSchema
            Address = schemas.StrSchema
        
            @staticmethod
            def PersonalPhoneNumber() -> typing.Type['PersonalPhoneNumber']:
                return PersonalPhoneNumber
        
            @staticmethod
            def payroll_company() -> typing.Type['PayrollCompany']:
                return PayrollCompany
        
            @staticmethod
            def payroll_id() -> typing.Type['PayrollID']:
                return PayrollID
        
            @staticmethod
            def time__attendance_id() -> typing.Type['TimeAttendanceID']:
                return TimeAttendanceID
        
            @staticmethod
            def rota_id() -> typing.Type['RotaID']:
                return RotaID
        
            @staticmethod
            def crm_id() -> typing.Type['CRMID']:
                return CRMID
        
            @staticmethod
            def ats_id() -> typing.Type['ATSID']:
                return ATSID
        
            @staticmethod
            def performance_id() -> typing.Type['PerformanceID']:
                return PerformanceID
        
            @staticmethod
            def benefits_id() -> typing.Type['BenefitsID']:
                return BenefitsID
        
            @staticmethod
            def system1_id() -> typing.Type['System1ID']:
                return System1ID
        
            @staticmethod
            def system2_id() -> typing.Type['System2ID']:
                return System2ID
        
            @staticmethod
            def system3_id() -> typing.Type['System3ID']:
                return System3ID
            APIColumn1 = schemas.StrSchema
            APIColumn2 = schemas.StrSchema
            APIColumn3 = schemas.StrSchema
            APIColumn4 = schemas.StrSchema
            APIColumn5 = schemas.StrSchema
        
            @staticmethod
            def PersonalEmail() -> typing.Type['PersonalEmail']:
                return PersonalEmail
        
            @staticmethod
            def MethodOfRecruitment() -> typing.Type['MethodOfRecruitment']:
                return MethodOfRecruitment
            __annotations__ = {
                "APIKey": APIKey,
                "Action": Action,
                "EmployeeId": EmployeeId,
                "FirstName": FirstName,
                "LastName": LastName,
                "StartDate": StartDate,
                "JobRole": JobRole,
                "JobRoleEffectiveDate": JobRoleEffectiveDate,
                "Location": Location,
                "Department": Department,
                "Title": Title,
                "Email": Email,
                "Gender": Gender,
                "DateOfBirth": DateOfBirth,
                "ReportsTo": ReportsTo,
                "Company": Company,
                "NationalInsuranceNumber": NationalInsuranceNumber,
                "Nationality": Nationality,
                "EmploymentType": EmploymentType,
                "EntitlementThisYear": EntitlementThisYear,
                "EntitlementNextYear": EntitlementNextYear,
                "Address": Address,
                "PersonalPhoneNumber": PersonalPhoneNumber,
                "Payroll Company": payroll_company,
                "Payroll ID": payroll_id,
                "Time & Attendance ID": time__attendance_id,
                "Rota ID": rota_id,
                "CRM ID": crm_id,
                "ATS ID": ats_id,
                "Performance ID": performance_id,
                "Benefits ID": benefits_id,
                "System1 ID": system1_id,
                "System2 ID": system2_id,
                "System3 ID": system3_id,
                "APIColumn1": APIColumn1,
                "APIColumn2": APIColumn2,
                "APIColumn3": APIColumn3,
                "APIColumn4": APIColumn4,
                "APIColumn5": APIColumn5,
                "PersonalEmail": PersonalEmail,
                "MethodOfRecruitment": MethodOfRecruitment,
            }
    
    JobRole: 'JobRole'
    StartDate: MetaOapg.properties.StartDate
    APIKey: 'APIKey'
    Action: MetaOapg.properties.Action
    Department: MetaOapg.properties.Department
    FirstName: 'FirstName'
    JobRoleEffectiveDate: MetaOapg.properties.JobRoleEffectiveDate
    LastName: 'LastName'
    EmployeeId: 'EmployeeId'
    Location: MetaOapg.properties.Location
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIKey"]) -> 'APIKey': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Action"]) -> MetaOapg.properties.Action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> 'EmployeeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> 'FirstName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> 'LastName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StartDate"]) -> MetaOapg.properties.StartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobRole"]) -> 'JobRole': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobRoleEffectiveDate"]) -> MetaOapg.properties.JobRoleEffectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Location"]) -> MetaOapg.properties.Location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Department"]) -> MetaOapg.properties.Department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Title"]) -> 'Title': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> 'Email': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Gender"]) -> 'Gender': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateOfBirth"]) -> MetaOapg.properties.DateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReportsTo"]) -> 'ReportsTo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Company"]) -> 'Company': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NationalInsuranceNumber"]) -> 'NationalInsuranceNumber': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Nationality"]) -> 'Nationality': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmploymentType"]) -> 'EmploymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EntitlementThisYear"]) -> MetaOapg.properties.EntitlementThisYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EntitlementNextYear"]) -> MetaOapg.properties.EntitlementNextYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address"]) -> MetaOapg.properties.Address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PersonalPhoneNumber"]) -> 'PersonalPhoneNumber': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Payroll Company"]) -> 'PayrollCompany': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Payroll ID"]) -> 'PayrollID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Time & Attendance ID"]) -> 'TimeAttendanceID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rota ID"]) -> 'RotaID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CRM ID"]) -> 'CRMID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ATS ID"]) -> 'ATSID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Performance ID"]) -> 'PerformanceID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Benefits ID"]) -> 'BenefitsID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["System1 ID"]) -> 'System1ID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["System2 ID"]) -> 'System2ID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["System3 ID"]) -> 'System3ID': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIColumn1"]) -> MetaOapg.properties.APIColumn1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIColumn2"]) -> MetaOapg.properties.APIColumn2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIColumn3"]) -> MetaOapg.properties.APIColumn3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIColumn4"]) -> MetaOapg.properties.APIColumn4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIColumn5"]) -> MetaOapg.properties.APIColumn5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PersonalEmail"]) -> 'PersonalEmail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MethodOfRecruitment"]) -> 'MethodOfRecruitment': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["APIKey", "Action", "EmployeeId", "FirstName", "LastName", "StartDate", "JobRole", "JobRoleEffectiveDate", "Location", "Department", "Title", "Email", "Gender", "DateOfBirth", "ReportsTo", "Company", "NationalInsuranceNumber", "Nationality", "EmploymentType", "EntitlementThisYear", "EntitlementNextYear", "Address", "PersonalPhoneNumber", "Payroll Company", "Payroll ID", "Time & Attendance ID", "Rota ID", "CRM ID", "ATS ID", "Performance ID", "Benefits ID", "System1 ID", "System2 ID", "System3 ID", "APIColumn1", "APIColumn2", "APIColumn3", "APIColumn4", "APIColumn5", "PersonalEmail", "MethodOfRecruitment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIKey"]) -> 'APIKey': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Action"]) -> MetaOapg.properties.Action: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> 'EmployeeId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> 'FirstName': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> 'LastName': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StartDate"]) -> MetaOapg.properties.StartDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobRole"]) -> 'JobRole': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobRoleEffectiveDate"]) -> MetaOapg.properties.JobRoleEffectiveDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Location"]) -> MetaOapg.properties.Location: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Department"]) -> MetaOapg.properties.Department: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Title"]) -> typing.Union['Title', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union['Email', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Gender"]) -> typing.Union['Gender', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateOfBirth"]) -> typing.Union[MetaOapg.properties.DateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReportsTo"]) -> typing.Union['ReportsTo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Company"]) -> typing.Union['Company', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NationalInsuranceNumber"]) -> typing.Union['NationalInsuranceNumber', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Nationality"]) -> typing.Union['Nationality', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmploymentType"]) -> typing.Union['EmploymentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EntitlementThisYear"]) -> typing.Union[MetaOapg.properties.EntitlementThisYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EntitlementNextYear"]) -> typing.Union[MetaOapg.properties.EntitlementNextYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address"]) -> typing.Union[MetaOapg.properties.Address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PersonalPhoneNumber"]) -> typing.Union['PersonalPhoneNumber', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Payroll Company"]) -> typing.Union['PayrollCompany', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Payroll ID"]) -> typing.Union['PayrollID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Time & Attendance ID"]) -> typing.Union['TimeAttendanceID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rota ID"]) -> typing.Union['RotaID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CRM ID"]) -> typing.Union['CRMID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ATS ID"]) -> typing.Union['ATSID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Performance ID"]) -> typing.Union['PerformanceID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Benefits ID"]) -> typing.Union['BenefitsID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["System1 ID"]) -> typing.Union['System1ID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["System2 ID"]) -> typing.Union['System2ID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["System3 ID"]) -> typing.Union['System3ID', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIColumn1"]) -> typing.Union[MetaOapg.properties.APIColumn1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIColumn2"]) -> typing.Union[MetaOapg.properties.APIColumn2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIColumn3"]) -> typing.Union[MetaOapg.properties.APIColumn3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIColumn4"]) -> typing.Union[MetaOapg.properties.APIColumn4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIColumn5"]) -> typing.Union[MetaOapg.properties.APIColumn5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PersonalEmail"]) -> typing.Union['PersonalEmail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MethodOfRecruitment"]) -> typing.Union['MethodOfRecruitment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["APIKey", "Action", "EmployeeId", "FirstName", "LastName", "StartDate", "JobRole", "JobRoleEffectiveDate", "Location", "Department", "Title", "Email", "Gender", "DateOfBirth", "ReportsTo", "Company", "NationalInsuranceNumber", "Nationality", "EmploymentType", "EntitlementThisYear", "EntitlementNextYear", "Address", "PersonalPhoneNumber", "Payroll Company", "Payroll ID", "Time & Attendance ID", "Rota ID", "CRM ID", "ATS ID", "Performance ID", "Benefits ID", "System1 ID", "System2 ID", "System3 ID", "APIColumn1", "APIColumn2", "APIColumn3", "APIColumn4", "APIColumn5", "PersonalEmail", "MethodOfRecruitment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        JobRole: 'JobRole',
        StartDate: typing.Union[MetaOapg.properties.StartDate, str, date, ],
        APIKey: 'APIKey',
        Action: typing.Union[MetaOapg.properties.Action, str, ],
        Department: typing.Union[MetaOapg.properties.Department, str, ],
        FirstName: 'FirstName',
        JobRoleEffectiveDate: typing.Union[MetaOapg.properties.JobRoleEffectiveDate, str, date, ],
        LastName: 'LastName',
        EmployeeId: 'EmployeeId',
        Location: typing.Union[MetaOapg.properties.Location, str, ],
        Title: typing.Union['Title', schemas.Unset] = schemas.unset,
        Email: typing.Union['Email', schemas.Unset] = schemas.unset,
        Gender: typing.Union['Gender', schemas.Unset] = schemas.unset,
        DateOfBirth: typing.Union[MetaOapg.properties.DateOfBirth, str, date, schemas.Unset] = schemas.unset,
        ReportsTo: typing.Union['ReportsTo', schemas.Unset] = schemas.unset,
        Company: typing.Union['Company', schemas.Unset] = schemas.unset,
        NationalInsuranceNumber: typing.Union['NationalInsuranceNumber', schemas.Unset] = schemas.unset,
        Nationality: typing.Union['Nationality', schemas.Unset] = schemas.unset,
        EmploymentType: typing.Union['EmploymentType', schemas.Unset] = schemas.unset,
        EntitlementThisYear: typing.Union[MetaOapg.properties.EntitlementThisYear, str, schemas.Unset] = schemas.unset,
        EntitlementNextYear: typing.Union[MetaOapg.properties.EntitlementNextYear, str, schemas.Unset] = schemas.unset,
        Address: typing.Union[MetaOapg.properties.Address, str, schemas.Unset] = schemas.unset,
        PersonalPhoneNumber: typing.Union['PersonalPhoneNumber', schemas.Unset] = schemas.unset,
        APIColumn1: typing.Union[MetaOapg.properties.APIColumn1, str, schemas.Unset] = schemas.unset,
        APIColumn2: typing.Union[MetaOapg.properties.APIColumn2, str, schemas.Unset] = schemas.unset,
        APIColumn3: typing.Union[MetaOapg.properties.APIColumn3, str, schemas.Unset] = schemas.unset,
        APIColumn4: typing.Union[MetaOapg.properties.APIColumn4, str, schemas.Unset] = schemas.unset,
        APIColumn5: typing.Union[MetaOapg.properties.APIColumn5, str, schemas.Unset] = schemas.unset,
        PersonalEmail: typing.Union['PersonalEmail', schemas.Unset] = schemas.unset,
        MethodOfRecruitment: typing.Union['MethodOfRecruitment', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateEmployeeDetailParameter':
        return super().__new__(
            cls,
            *args,
            JobRole=JobRole,
            StartDate=StartDate,
            APIKey=APIKey,
            Action=Action,
            Department=Department,
            FirstName=FirstName,
            JobRoleEffectiveDate=JobRoleEffectiveDate,
            LastName=LastName,
            EmployeeId=EmployeeId,
            Location=Location,
            Title=Title,
            Email=Email,
            Gender=Gender,
            DateOfBirth=DateOfBirth,
            ReportsTo=ReportsTo,
            Company=Company,
            NationalInsuranceNumber=NationalInsuranceNumber,
            Nationality=Nationality,
            EmploymentType=EmploymentType,
            EntitlementThisYear=EntitlementThisYear,
            EntitlementNextYear=EntitlementNextYear,
            Address=Address,
            PersonalPhoneNumber=PersonalPhoneNumber,
            APIColumn1=APIColumn1,
            APIColumn2=APIColumn2,
            APIColumn3=APIColumn3,
            APIColumn4=APIColumn4,
            APIColumn5=APIColumn5,
            PersonalEmail=PersonalEmail,
            MethodOfRecruitment=MethodOfRecruitment,
            _configuration=_configuration,
            **kwargs,
        )

from people_hr_python_sdk.model.api_key import APIKey
from people_hr_python_sdk.model.atsid import ATSID
from people_hr_python_sdk.model.benefits_id import BenefitsID
from people_hr_python_sdk.model.company import Company
from people_hr_python_sdk.model.crmid import CRMID
from people_hr_python_sdk.model.email import Email
from people_hr_python_sdk.model.employee_id import EmployeeId
from people_hr_python_sdk.model.employment_type import EmploymentType
from people_hr_python_sdk.model.first_name import FirstName
from people_hr_python_sdk.model.gender import Gender
from people_hr_python_sdk.model.job_role import JobRole
from people_hr_python_sdk.model.last_name import LastName
from people_hr_python_sdk.model.method_of_recruitment import MethodOfRecruitment
from people_hr_python_sdk.model.national_insurance_number import NationalInsuranceNumber
from people_hr_python_sdk.model.nationality import Nationality
from people_hr_python_sdk.model.payroll_company import PayrollCompany
from people_hr_python_sdk.model.payroll_id import PayrollID
from people_hr_python_sdk.model.performance_id import PerformanceID
from people_hr_python_sdk.model.personal_email import PersonalEmail
from people_hr_python_sdk.model.personal_phone_number import PersonalPhoneNumber
from people_hr_python_sdk.model.reports_to import ReportsTo
from people_hr_python_sdk.model.rota_id import RotaID
from people_hr_python_sdk.model.system1_id import System1ID
from people_hr_python_sdk.model.system2_id import System2ID
from people_hr_python_sdk.model.system3_id import System3ID
from people_hr_python_sdk.model.time_attendance_id import TimeAttendanceID
from people_hr_python_sdk.model.title import Title
