# coding: utf-8

"""
    PeopleHR API

    # Introduction  We think it's good to share. So we've created an open API to help you easily integrate People with other systems and applications, for seamless cross-platform data sharing.   The People API accepts and returns JSON data in the request body, with status indicating the outcome of the operation (sucess/failure).  # Developer Workbench  As well as this really useful documentation, we've also provided you with a handy API developer workbench. This allows you test your API calls against either a sandbox, or a live instance. A great place to start is the General Overview video, which explains how to use the workbench: https://intercom.help/peoplea-apps/api-and-integration/api  You can access the developer work bench here: https://api.peoplehr.net/pages/functional   # Sandbox If you need a sandbox account to test your creation, just email customerservices@peoplehr.com and we will help you set one up.   # Authentication The People API uses API keys for each call. To receive an API key, ask your system administrator to generate one from within Settings. For authentication, all API calls need the API key to be passed along with the JSON data sent as part of the http request. Never share your API keys. Keep them guarded and secure.   # Managed Lists  Within People, there are a number of fields called Managed Lists, better known as dropdowns. When you insert an item of data into a field that is a Managed List, then the API will automatically create you an entry in the Managed List for that field.  # Rate Limit Detail  The API rate limit is set to 30 calls a minute from a specific IP address. If you attempt to call the API above the rate limit, then an exception message will be returned. If you would like your rate limit increased, please submit a request to customerservices@peoplehr.com. In your email, please explain why you would like your limit increasing.   # Webhooks Detail  People provides an option to use webhooks to receive notifications of changes in particular transactions. If you are going to use the webhook mechanism, we advise you to set up a generic listener service to receive callbacks.   To set up a webhook listener URL, select Settings, API, and then enter your listner URL into the field.    The following actions are available and the data packet will return the following (example data shown):    New Starter Added > ActionId:1, Action:New Starter Added, EmployeeId:PW21    Employee personal detail update > ActionId:2, Action:Employee Detail Updated, EmployeeId:PW1, FieldName:Other Name(s), NewValue:Am, OldValue:zz, Reason:Test    Leaver > ActionId:3, Action:Marked Leaver, EmployeeId:PW21    Holiday added > ActionId:4, Action:Holiday Added, EmployeeId:PW13, HolidayType:A day or more, StartDate:2016-06-13, EndDate:2016-06-15, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.50, Comments:part day testing, IsToilHoliday:No    Holiday Updated > ActionId:5, Action:Holiday Updated, EmployeeId:PW51, HolidayType:A day or more, OriginalStartDate:2016-05-04, OriginalEndDate:2016-05-04, OriginalPartOfDay:, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-05-04, EndDate:2016-05-05, HolidayRecordedIn:Days, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1.50, Comments:Test, IsToilHoliday:No    Holiday Deleted > ActionId:6, Action:Holiday Deleted, EmployeeId:PW13, StartDate:2016-01-18, EndDate:2016-01-19, HolidayRecordedIn:Days, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:2.00, Comments:zz    Holiday Requested > ActionId:7, Action:New Holiday Request, EmployeeId:PW97, HolidayType:A day or more, StartDate:2017-06-22, EndDate:2017-06-23, HolidayRecordedIn:Days, PartOfDay: StartDatePartOfTheDay:, EndDatePartOfTheDay:, Duration:2.00, Comments:Graduation, IsToilHoliday:No    Holiday Approved > ActionId:8, Action:Holiday Approved, EmployeeId:PW391, StartDate:2017-06-15, EndDate:2017-06-15, HolidayRecordedIn:Days, Duration:0.5, Comments:, AuthorisedByFirstName:Richard, AuthorisedByLastName:Palmer, HolidayType:Less than a day, PartOfDay:AM, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No    Holiday Rejected > ActionId:9, Action:Holiday Rejected, EmployeeId:PW29, StartDate:2017-07-12, EndDate:2017-07-12, HolidayRecordedIn:Days, Duration:1, Comments:Unfortunately this is, fully booked, AuthorisedByFirstName:Debi, AuthorisedByLastName:Stokes, HolidayType:A day or more, PartOfDay:, StartDatePartOfTheDay:, EndDatePartOfTheDay:, IsToilHoliday:No    Sick Added > ActionId:10, Action:Sick Added, EmployeeId:PW13, Reason:Accident, StartDate:2016-01-19, EndDate:2016-01-19, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments:    Sick Updated > ActionId:11, Action:Sick Updated, EmployeeId:PW13, Reason:Accident, OriginalStartDate:2016-01-18, OriginalEndDate:2016-01-19, OriginalStartDatePartOfTheDay:, OriginalEndDatePartOfTheDay:, OriginalDuration:1.00, StartDate:2016-01-18, EndDate:2016-01-19, StartDatePartOfTheDay:, EndDatePartOfTheDay:AM, Duration:1, Comments:    Sick Deleted > ActionId:12, Action:Sick Deleted, EmployeeId:PW13, Reason:Cold/Flu, StartDate:2016-01-21, EndDate:2016-01-21, StartDatePartOfTheDay:AM, EndDatePartOfTheDay:, Duration:1, Comments:    Maternity / Paternity Added > ActionId:13, Action:Maternity/Paternity Added, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-24    Maternity / Paternity Updated > ActionId:14, Action:Maternity/Paternity Updated, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25    Maternity / Paternity Deleted > ActionId:15, Action:Maternity/Paternity Deleted, EmployeeId:PW13, StartDate:2016-01-23, EndDate:2016-01-25    Late Added > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:10, Comments:    Late Updated > ActionId:16, Action:Late Recorded, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments:    Late Deleted > ActionId:17, Action:Late Deleted, EmployeeId:PW13, Date:2016-01-26, HowLate:16, Comments:    Employee Deleted > ActionId:18, Action:Employee Deleted, EmployeeId:PW21    Other Event Updated > ActionId:21, Action:Other Event Updated, EmployeeId:PW5-2, OriginalStartDate:2016-06-25, OriginalEndDate:2016-06-25, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Days, OriginalDurationType:Days, OriginalDuration:1.00, OriginalStartTime:, OriginalEndTime:    Other Event Deleted > ActionId:22, Action:Other Event Deleted, EmployeeId:PW5-2, Reason:Dentist, StartDate:2016-06-25, EndDate:2016-06-26, Duration:2.00, Comments:, DurationType:Day, StartTime:, EndTime:    Other Event Requested > ActionId:23, Action:New Other Event Request, EmployeeId:S20, Reason:Flexi, StartDate:2017-06-16, StartTime:09:00:00, EndTime:12:30:00, Duration:210, Comments:, DurationType:Hours    Other Event Approved > ActionId:24, Action:Other Event Approved, EmployeeId:180, StartDate:2017-06-14, EndDate:2017-06-14, Comments:, AuthorisedByFirstName:Damith, Duration:2 Hrs 0 Mins (02:00 - 04:00), Reason:Short Leave    Other Event Rejected > ActionId:25, Action:Other Event Rejected, EmployeeId:312, StartDate:2017-09-13, EndDate:2017-09-13, Comments:already 2 x nurse on AL, AuthorisedByFirstName:Dirkje (Dorien), Duration:1 Day, Reason:Request To Work    Appraisals Logbook > ActionId:31, Action:Appraisal Add, EmployeeId:PW8996, TxnId:1, ScreenType:1    ActionId:32 > Action:Appraisal Update, EmployeeId:PW8996, TxnId:1, ScreenType:1    ActionId:33 > Action:Appraisal Delete, EmployeeId:PW8996, TxnId:1, ScreenType:1    Benefit Logbook > ActionId:34, Action:Benefit Add, EmployeeId:PW8996, TxnId:1, ScreenType:2    ActionId:35 > Action:Benefit Update, EmployeeId:PW8996, TxnId:1, ScreenType:2    ActionId:36 > Action:Benefit Delete, EmployeeId:PW8996, TxnId:1, ScreenType:2    CPD Logbook > ActionId:37, Action:CPD Add, EmployeeId:PW8996, TxnId:1, ScreenType:3    ActionId:38 > Action:CPD Update, EmployeeId:PW8996, TxnId:1, ScreenType:3    ActionId:39 > Action:CPD Delete, EmployeeId:PW8996, TxnId:1, ScreenType:3    Driving Licence Logbook > ActionId:40, Action:Driving Licence Add, EmployeeId:PW8996, TxnId:1, ScreenType:6    ActionId:41 > Action:Driving Licence Update, EmployeeId:PW8996, TxnId:1, ScreenType:6    ActionId:42 > Action:Driving Licence Delete, EmployeeId:PW8996, TxnId:1, ScreenType:6    Qualification Logbook > ActionId:43, Action:Qualification Add, EmployeeId:PW8996, TxnId:1, ScreenType:4    ActionId:44 > , Action:Qualification Update, EmployeeId:PW8996, TxnId:1, ScreenType:4    ActionId:45 > Action:Qualification Delete, EmployeeId:PW8996, TxnId:1, ScreenType:4    Training Logbook > ActionId:46, Action:Training Add, EmployeeId:PW8996, TxnId:1, ScreenType:5    ActionId:47 > Action:Training Update, EmployeeId:PW8996, TxnId:1, ScreenType:5    ActionId:48 > Action:Training Delete, EmployeeId:PW8996, TxnId:1, ScreenType:5    Vehicle Logbook > ActionId:49, Action:Vehicle Add, EmployeeId:PW8996, TxnId:1, ScreenType:7    ActionId:50 > Action:Vehicle Update, EmployeeId:PW8996, TxnId:1, ScreenType:7    ActionId:51 > Action:Vehicle Delete, EmployeeId:PW8996, TxnId:1, ScreenType:7    Custom Logbook > ActionId:52, Action:Custom Screen Add, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10    ActionId:53 > Action:Custom Screen Update, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10    ActionId:54 > Action:Custom Screen Delete, EmployeeId:PW8996, TxnId:1, ScreenType:8, CustomScreenId:10   Keys    The unique key for an event on the People calendar is Start Date and End Date -- you should also use the same key to identify record in your system that is consuming the data from People - the reason you need to do this is to locate the original record within your system when you get a notification of an update or a deletion - you will notice the message fragment contains the original dates - so you can locate the record - and the new dates.  Another more sophisticated option is to use the transaction ID. Holiday, Sick, Other Event and Maternity/Paternity transactions within People allow you to store an external transaction. Using this approach you could store the transaction id from a calendering system such as Outlook. If the holiday record on People is amended or deleted you will be able to determine the corresponding record in Outlook.    Take the following scenario:    If you create holidays through the API you will receive AnnualLeaveTxnId in the API result set. Any integration can store this as a reference from People HR holidays mapping    If you create holidays within the People HR UI, you will receive webhook details with holidays details. Integrated applications need to call people holidays GET details API with the current webhook details. That will give you AnnualLeaveTxnID & ReferenceId (If any). Now you can save the AnnualLeaveTxnId in an integrated application as People HR holidays mapping.    You can store third party application holidays/transaction references into the People HR system by calling the API Employee Holiday -> Update Holiday Reference ID    If you want to update/delete any holidays from People HR that are already mapped with third party applications/integrations, you can call holidays API to match with reference ID. You will get assoicated data with the reference ID that you actually need to update/ delete holidays from the people system (Employee Holiday -> UpdateHoliday or Employee Holiday -> DeleteHoliday).   Start Part of Day and End Part of Day In People it is possible to record half days both at the beginning of a holiday or sick event or at the end. You can determine this by looking at the StartPartOfDay and EndPartOfDay values which will either be blank, AM or PM.    # Examples We've put a few examples together for you that might help you get started:  HTML Coding Examples: https://help.peoplehr.com/en/articles/981415-api-html-examples  c# Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-c-code-snippet  Objective C Coding Examples: http://intercom.help/peoplea-apps/api-and-integration/api-code-snippets-objective-c  How to use Postman with the API: http://intercom.help/peoplea-apps/api-and-integration/api-using-postman  <!-- ReDoc-Inject: <security-definitions> --> 

    The version of the OpenAPI document: 3.1
    Contact: customerservices@peoplehr.com
    Created by: https://www.peoplehr.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from people_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from people_hr_python_sdk.api_response import AsyncGeneratorResponse
from people_hr_python_sdk import api_client, exceptions
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

from people_hr_python_sdk.model.title import Title as TitleSchema
from people_hr_python_sdk.model.gender import Gender as GenderSchema
from people_hr_python_sdk.model.job_role import JobRole as JobRoleSchema
from people_hr_python_sdk.model.system2_id import System2ID as System2IDSchema
from people_hr_python_sdk.model.performance_id import PerformanceID as PerformanceIDSchema
from people_hr_python_sdk.model.personal_phone_number import PersonalPhoneNumber as PersonalPhoneNumberSchema
from people_hr_python_sdk.model.payroll_id import PayrollID as PayrollIDSchema
from people_hr_python_sdk.model.reports_to import ReportsTo as ReportsToSchema
from people_hr_python_sdk.model.first_name import FirstName as FirstNameSchema
from people_hr_python_sdk.model.payroll_company import PayrollCompany as PayrollCompanySchema
from people_hr_python_sdk.model.method_of_recruitment import MethodOfRecruitment as MethodOfRecruitmentSchema
from people_hr_python_sdk.model.rota_id import RotaID as RotaIDSchema
from people_hr_python_sdk.model.nationality import Nationality as NationalitySchema
from people_hr_python_sdk.model.company import Company as CompanySchema
from people_hr_python_sdk.model.system1_id import System1ID as System1IDSchema
from people_hr_python_sdk.model.api_key import APIKey as APIKeySchema
from people_hr_python_sdk.model.create_employee_detail_parameter import CreateEmployeeDetailParameter as CreateEmployeeDetailParameterSchema
from people_hr_python_sdk.model.time_attendance_id import TimeAttendanceID as TimeAttendanceIDSchema
from people_hr_python_sdk.model.benefits_id import BenefitsID as BenefitsIDSchema
from people_hr_python_sdk.model.error_for_create_new_employee_detail import ErrorForCreateNewEmployeeDetail as ErrorForCreateNewEmployeeDetailSchema
from people_hr_python_sdk.model.personal_email import PersonalEmail as PersonalEmailSchema
from people_hr_python_sdk.model.national_insurance_number import NationalInsuranceNumber as NationalInsuranceNumberSchema
from people_hr_python_sdk.model.employee_id import EmployeeId as EmployeeIdSchema
from people_hr_python_sdk.model.system3_id import System3ID as System3IDSchema
from people_hr_python_sdk.model.crmid import CRMID as CRMIDSchema
from people_hr_python_sdk.model.atsid import ATSID as ATSIDSchema
from people_hr_python_sdk.model.email import Email as EmailSchema
from people_hr_python_sdk.model.employment_type import EmploymentType as EmploymentTypeSchema
from people_hr_python_sdk.model.last_name import LastName as LastNameSchema

from people_hr_python_sdk.type.job_role import JobRole
from people_hr_python_sdk.type.company import Company
from people_hr_python_sdk.type.error_for_create_new_employee_detail import ErrorForCreateNewEmployeeDetail
from people_hr_python_sdk.type.rota_id import RotaID
from people_hr_python_sdk.type.national_insurance_number import NationalInsuranceNumber
from people_hr_python_sdk.type.nationality import Nationality
from people_hr_python_sdk.type.crmid import CRMID
from people_hr_python_sdk.type.atsid import ATSID
from people_hr_python_sdk.type.title import Title
from people_hr_python_sdk.type.system3_id import System3ID
from people_hr_python_sdk.type.benefits_id import BenefitsID
from people_hr_python_sdk.type.gender import Gender
from people_hr_python_sdk.type.last_name import LastName
from people_hr_python_sdk.type.email import Email
from people_hr_python_sdk.type.employee_id import EmployeeId
from people_hr_python_sdk.type.api_key import APIKey
from people_hr_python_sdk.type.first_name import FirstName
from people_hr_python_sdk.type.time_attendance_id import TimeAttendanceID
from people_hr_python_sdk.type.system1_id import System1ID
from people_hr_python_sdk.type.method_of_recruitment import MethodOfRecruitment
from people_hr_python_sdk.type.create_employee_detail_parameter import CreateEmployeeDetailParameter
from people_hr_python_sdk.type.payroll_company import PayrollCompany
from people_hr_python_sdk.type.personal_phone_number import PersonalPhoneNumber
from people_hr_python_sdk.type.employment_type import EmploymentType
from people_hr_python_sdk.type.performance_id import PerformanceID
from people_hr_python_sdk.type.reports_to import ReportsTo
from people_hr_python_sdk.type.personal_email import PersonalEmail
from people_hr_python_sdk.type.system2_id import System2ID
from people_hr_python_sdk.type.payroll_id import PayrollID

from ...api_client import Dictionary
from people_hr_python_sdk.pydantic.personal_phone_number import PersonalPhoneNumber as PersonalPhoneNumberPydantic
from people_hr_python_sdk.pydantic.nationality import Nationality as NationalityPydantic
from people_hr_python_sdk.pydantic.last_name import LastName as LastNamePydantic
from people_hr_python_sdk.pydantic.system1_id import System1ID as System1IDPydantic
from people_hr_python_sdk.pydantic.employee_id import EmployeeId as EmployeeIdPydantic
from people_hr_python_sdk.pydantic.personal_email import PersonalEmail as PersonalEmailPydantic
from people_hr_python_sdk.pydantic.system2_id import System2ID as System2IDPydantic
from people_hr_python_sdk.pydantic.method_of_recruitment import MethodOfRecruitment as MethodOfRecruitmentPydantic
from people_hr_python_sdk.pydantic.rota_id import RotaID as RotaIDPydantic
from people_hr_python_sdk.pydantic.employment_type import EmploymentType as EmploymentTypePydantic
from people_hr_python_sdk.pydantic.first_name import FirstName as FirstNamePydantic
from people_hr_python_sdk.pydantic.email import Email as EmailPydantic
from people_hr_python_sdk.pydantic.api_key import APIKey as APIKeyPydantic
from people_hr_python_sdk.pydantic.gender import Gender as GenderPydantic
from people_hr_python_sdk.pydantic.reports_to import ReportsTo as ReportsToPydantic
from people_hr_python_sdk.pydantic.title import Title as TitlePydantic
from people_hr_python_sdk.pydantic.payroll_company import PayrollCompany as PayrollCompanyPydantic
from people_hr_python_sdk.pydantic.benefits_id import BenefitsID as BenefitsIDPydantic
from people_hr_python_sdk.pydantic.time_attendance_id import TimeAttendanceID as TimeAttendanceIDPydantic
from people_hr_python_sdk.pydantic.performance_id import PerformanceID as PerformanceIDPydantic
from people_hr_python_sdk.pydantic.job_role import JobRole as JobRolePydantic
from people_hr_python_sdk.pydantic.company import Company as CompanyPydantic
from people_hr_python_sdk.pydantic.payroll_id import PayrollID as PayrollIDPydantic
from people_hr_python_sdk.pydantic.national_insurance_number import NationalInsuranceNumber as NationalInsuranceNumberPydantic
from people_hr_python_sdk.pydantic.crmid import CRMID as CRMIDPydantic
from people_hr_python_sdk.pydantic.error_for_create_new_employee_detail import ErrorForCreateNewEmployeeDetail as ErrorForCreateNewEmployeeDetailPydantic
from people_hr_python_sdk.pydantic.system3_id import System3ID as System3IDPydantic
from people_hr_python_sdk.pydantic.atsid import ATSID as ATSIDPydantic
from people_hr_python_sdk.pydantic.create_employee_detail_parameter import CreateEmployeeDetailParameter as CreateEmployeeDetailParameterPydantic

# body param
SchemaForRequestBodyApplicationJson = CreateEmployeeDetailParameterSchema


request_body_create_employee_detail_parameter = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ErrorForCreateNewEmployeeDetailSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ErrorForCreateNewEmployeeDetail


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ErrorForCreateNewEmployeeDetail


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_new_employee_mapped_args(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if api_key is not None:
            _body["APIKey"] = api_key
        if action is not None:
            _body["Action"] = action
        if employee_id is not None:
            _body["EmployeeId"] = employee_id
        if title is not None:
            _body["Title"] = title
        if first_name is not None:
            _body["FirstName"] = first_name
        if last_name is not None:
            _body["LastName"] = last_name
        if email is not None:
            _body["Email"] = email
        if gender is not None:
            _body["Gender"] = gender
        if start_date is not None:
            _body["StartDate"] = start_date
        if date_of_birth is not None:
            _body["DateOfBirth"] = date_of_birth
        if reports_to is not None:
            _body["ReportsTo"] = reports_to
        if job_role is not None:
            _body["JobRole"] = job_role
        if job_role_effective_date is not None:
            _body["JobRoleEffectiveDate"] = job_role_effective_date
        if company is not None:
            _body["Company"] = company
        if location is not None:
            _body["Location"] = location
        if department is not None:
            _body["Department"] = department
        if national_insurance_number is not None:
            _body["NationalInsuranceNumber"] = national_insurance_number
        if nationality is not None:
            _body["Nationality"] = nationality
        if employment_type is not None:
            _body["EmploymentType"] = employment_type
        if entitlement_this_year is not None:
            _body["EntitlementThisYear"] = entitlement_this_year
        if entitlement_next_year is not None:
            _body["EntitlementNextYear"] = entitlement_next_year
        if address is not None:
            _body["Address"] = address
        if personal_phone_number is not None:
            _body["PersonalPhoneNumber"] = personal_phone_number
        if payroll_company is not None:
            _body["Payroll Company"] = payroll_company
        if payroll_id is not None:
            _body["Payroll ID"] = payroll_id
        if time__attendance_id is not None:
            _body["Time & Attendance ID"] = time__attendance_id
        if rota_id is not None:
            _body["Rota ID"] = rota_id
        if crm_id is not None:
            _body["CRM ID"] = crm_id
        if ats_id is not None:
            _body["ATS ID"] = ats_id
        if performance_id is not None:
            _body["Performance ID"] = performance_id
        if benefits_id is not None:
            _body["Benefits ID"] = benefits_id
        if system1_id is not None:
            _body["System1 ID"] = system1_id
        if system2_id is not None:
            _body["System2 ID"] = system2_id
        if system3_id is not None:
            _body["System3 ID"] = system3_id
        if api_column1 is not None:
            _body["APIColumn1"] = api_column1
        if api_column2 is not None:
            _body["APIColumn2"] = api_column2
        if api_column3 is not None:
            _body["APIColumn3"] = api_column3
        if api_column4 is not None:
            _body["APIColumn4"] = api_column4
        if api_column5 is not None:
            _body["APIColumn5"] = api_column5
        if personal_email is not None:
            _body["PersonalEmail"] = personal_email
        if method_of_recruitment is not None:
            _body["MethodOfRecruitment"] = method_of_recruitment
        args.body = _body
        return args

    async def _aadd_new_employee_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create New Employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Employee  -  CreateNewEmployee',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_create_employee_detail_parameter.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _add_new_employee_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create New Employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Employee  -  CreateNewEmployee',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_create_employee_detail_parameter.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class AddNewEmployeeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_new_employee(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_new_employee_mapped_args(
            api_key=api_key,
            action=action,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            job_role=job_role,
            job_role_effective_date=job_role_effective_date,
            location=location,
            department=department,
            title=title,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            reports_to=reports_to,
            company=company,
            national_insurance_number=national_insurance_number,
            nationality=nationality,
            employment_type=employment_type,
            entitlement_this_year=entitlement_this_year,
            entitlement_next_year=entitlement_next_year,
            address=address,
            personal_phone_number=personal_phone_number,
            payroll_company=payroll_company,
            payroll_id=payroll_id,
            time__attendance_id=time__attendance_id,
            rota_id=rota_id,
            crm_id=crm_id,
            ats_id=ats_id,
            performance_id=performance_id,
            benefits_id=benefits_id,
            system1_id=system1_id,
            system2_id=system2_id,
            system3_id=system3_id,
            api_column1=api_column1,
            api_column2=api_column2,
            api_column3=api_column3,
            api_column4=api_column4,
            api_column5=api_column5,
            personal_email=personal_email,
            method_of_recruitment=method_of_recruitment,
        )
        return await self._aadd_new_employee_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add_new_employee(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_new_employee_mapped_args(
            api_key=api_key,
            action=action,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            job_role=job_role,
            job_role_effective_date=job_role_effective_date,
            location=location,
            department=department,
            title=title,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            reports_to=reports_to,
            company=company,
            national_insurance_number=national_insurance_number,
            nationality=nationality,
            employment_type=employment_type,
            entitlement_this_year=entitlement_this_year,
            entitlement_next_year=entitlement_next_year,
            address=address,
            personal_phone_number=personal_phone_number,
            payroll_company=payroll_company,
            payroll_id=payroll_id,
            time__attendance_id=time__attendance_id,
            rota_id=rota_id,
            crm_id=crm_id,
            ats_id=ats_id,
            performance_id=performance_id,
            benefits_id=benefits_id,
            system1_id=system1_id,
            system2_id=system2_id,
            system3_id=system3_id,
            api_column1=api_column1,
            api_column2=api_column2,
            api_column3=api_column3,
            api_column4=api_column4,
            api_column5=api_column5,
            personal_email=personal_email,
            method_of_recruitment=method_of_recruitment,
        )
        return self._add_new_employee_oapg(
            body=args.body,
        )

class AddNewEmployee(BaseApi):

    async def aadd_new_employee(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
        validate: bool = False,
        **kwargs,
    ) -> ErrorForCreateNewEmployeeDetailPydantic:
        raw_response = await self.raw.aadd_new_employee(
            api_key=api_key,
            action=action,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            job_role=job_role,
            job_role_effective_date=job_role_effective_date,
            location=location,
            department=department,
            title=title,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            reports_to=reports_to,
            company=company,
            national_insurance_number=national_insurance_number,
            nationality=nationality,
            employment_type=employment_type,
            entitlement_this_year=entitlement_this_year,
            entitlement_next_year=entitlement_next_year,
            address=address,
            personal_phone_number=personal_phone_number,
            payroll_company=payroll_company,
            payroll_id=payroll_id,
            time__attendance_id=time__attendance_id,
            rota_id=rota_id,
            crm_id=crm_id,
            ats_id=ats_id,
            performance_id=performance_id,
            benefits_id=benefits_id,
            system1_id=system1_id,
            system2_id=system2_id,
            system3_id=system3_id,
            api_column1=api_column1,
            api_column2=api_column2,
            api_column3=api_column3,
            api_column4=api_column4,
            api_column5=api_column5,
            personal_email=personal_email,
            method_of_recruitment=method_of_recruitment,
            **kwargs,
        )
        if validate:
            return ErrorForCreateNewEmployeeDetailPydantic(**raw_response.body)
        return api_client.construct_model_instance(ErrorForCreateNewEmployeeDetailPydantic, raw_response.body)
    
    
    def add_new_employee(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
        validate: bool = False,
    ) -> ErrorForCreateNewEmployeeDetailPydantic:
        raw_response = self.raw.add_new_employee(
            api_key=api_key,
            action=action,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            job_role=job_role,
            job_role_effective_date=job_role_effective_date,
            location=location,
            department=department,
            title=title,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            reports_to=reports_to,
            company=company,
            national_insurance_number=national_insurance_number,
            nationality=nationality,
            employment_type=employment_type,
            entitlement_this_year=entitlement_this_year,
            entitlement_next_year=entitlement_next_year,
            address=address,
            personal_phone_number=personal_phone_number,
            payroll_company=payroll_company,
            payroll_id=payroll_id,
            time__attendance_id=time__attendance_id,
            rota_id=rota_id,
            crm_id=crm_id,
            ats_id=ats_id,
            performance_id=performance_id,
            benefits_id=benefits_id,
            system1_id=system1_id,
            system2_id=system2_id,
            system3_id=system3_id,
            api_column1=api_column1,
            api_column2=api_column2,
            api_column3=api_column3,
            api_column4=api_column4,
            api_column5=api_column5,
            personal_email=personal_email,
            method_of_recruitment=method_of_recruitment,
        )
        if validate:
            return ErrorForCreateNewEmployeeDetailPydantic(**raw_response.body)
        return api_client.construct_model_instance(ErrorForCreateNewEmployeeDetailPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_new_employee_mapped_args(
            api_key=api_key,
            action=action,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            job_role=job_role,
            job_role_effective_date=job_role_effective_date,
            location=location,
            department=department,
            title=title,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            reports_to=reports_to,
            company=company,
            national_insurance_number=national_insurance_number,
            nationality=nationality,
            employment_type=employment_type,
            entitlement_this_year=entitlement_this_year,
            entitlement_next_year=entitlement_next_year,
            address=address,
            personal_phone_number=personal_phone_number,
            payroll_company=payroll_company,
            payroll_id=payroll_id,
            time__attendance_id=time__attendance_id,
            rota_id=rota_id,
            crm_id=crm_id,
            ats_id=ats_id,
            performance_id=performance_id,
            benefits_id=benefits_id,
            system1_id=system1_id,
            system2_id=system2_id,
            system3_id=system3_id,
            api_column1=api_column1,
            api_column2=api_column2,
            api_column3=api_column3,
            api_column4=api_column4,
            api_column5=api_column5,
            personal_email=personal_email,
            method_of_recruitment=method_of_recruitment,
        )
        return await self._aadd_new_employee_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        api_key: APIKey,
        action: str,
        employee_id: EmployeeId,
        first_name: FirstName,
        last_name: LastName,
        start_date: date,
        job_role: JobRole,
        job_role_effective_date: date,
        location: str,
        department: str,
        title: typing.Optional[Title] = None,
        email: typing.Optional[Email] = None,
        gender: typing.Optional[Gender] = None,
        date_of_birth: typing.Optional[date] = None,
        reports_to: typing.Optional[ReportsTo] = None,
        company: typing.Optional[Company] = None,
        national_insurance_number: typing.Optional[NationalInsuranceNumber] = None,
        nationality: typing.Optional[Nationality] = None,
        employment_type: typing.Optional[EmploymentType] = None,
        entitlement_this_year: typing.Optional[str] = None,
        entitlement_next_year: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        personal_phone_number: typing.Optional[PersonalPhoneNumber] = None,
        payroll_company: typing.Optional[PayrollCompany] = None,
        payroll_id: typing.Optional[PayrollID] = None,
        time__attendance_id: typing.Optional[TimeAttendanceID] = None,
        rota_id: typing.Optional[RotaID] = None,
        crm_id: typing.Optional[CRMID] = None,
        ats_id: typing.Optional[ATSID] = None,
        performance_id: typing.Optional[PerformanceID] = None,
        benefits_id: typing.Optional[BenefitsID] = None,
        system1_id: typing.Optional[System1ID] = None,
        system2_id: typing.Optional[System2ID] = None,
        system3_id: typing.Optional[System3ID] = None,
        api_column1: typing.Optional[str] = None,
        api_column2: typing.Optional[str] = None,
        api_column3: typing.Optional[str] = None,
        api_column4: typing.Optional[str] = None,
        api_column5: typing.Optional[str] = None,
        personal_email: typing.Optional[PersonalEmail] = None,
        method_of_recruitment: typing.Optional[MethodOfRecruitment] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_new_employee_mapped_args(
            api_key=api_key,
            action=action,
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            job_role=job_role,
            job_role_effective_date=job_role_effective_date,
            location=location,
            department=department,
            title=title,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            reports_to=reports_to,
            company=company,
            national_insurance_number=national_insurance_number,
            nationality=nationality,
            employment_type=employment_type,
            entitlement_this_year=entitlement_this_year,
            entitlement_next_year=entitlement_next_year,
            address=address,
            personal_phone_number=personal_phone_number,
            payroll_company=payroll_company,
            payroll_id=payroll_id,
            time__attendance_id=time__attendance_id,
            rota_id=rota_id,
            crm_id=crm_id,
            ats_id=ats_id,
            performance_id=performance_id,
            benefits_id=benefits_id,
            system1_id=system1_id,
            system2_id=system2_id,
            system3_id=system3_id,
            api_column1=api_column1,
            api_column2=api_column2,
            api_column3=api_column3,
            api_column4=api_column4,
            api_column5=api_column5,
            personal_email=personal_email,
            method_of_recruitment=method_of_recruitment,
        )
        return self._add_new_employee_oapg(
            body=args.body,
        )

