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


class CreateNewTimesheetDefinition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "APIKey",
            "Action",
            "EmployeeId",
            "TimesheetDate",
        }
        
        class properties:
        
            @staticmethod
            def APIKey() -> typing.Type['APIKey']:
                return APIKey
            Action = schemas.StrSchema
        
            @staticmethod
            def EmployeeId() -> typing.Type['EmployeeId']:
                return EmployeeId
            TimesheetDate = schemas.DateSchema
            TimeIn1 = schemas.StrSchema
            TimeOut1 = schemas.StrSchema
            TimeIn2 = schemas.StrSchema
            TimeOut2 = schemas.StrSchema
            TimeIn3 = schemas.StrSchema
            TimeOut3 = schemas.StrSchema
            TimeIn4 = schemas.StrSchema
            TimeOut4 = schemas.StrSchema
            TimeIn5 = schemas.StrSchema
            TimeOut5 = schemas.StrSchema
            TimeIn6 = schemas.StrSchema
            TimeOut6 = schemas.StrSchema
            TimeIn7 = schemas.StrSchema
            TimeOut7 = schemas.StrSchema
            TimeIn8 = schemas.StrSchema
            TimeOut8 = schemas.StrSchema
            TimeIn9 = schemas.StrSchema
            TimeOut9 = schemas.StrSchema
            TimeIn10 = schemas.StrSchema
            TimeOut10 = schemas.StrSchema
            TimeIn11 = schemas.StrSchema
            TimeOut11 = schemas.StrSchema
            TimeIn12 = schemas.StrSchema
            TimeOut12 = schemas.StrSchema
            TimeIn13 = schemas.StrSchema
            TimeOut13 = schemas.StrSchema
            TimeIn14 = schemas.StrSchema
            TimeOut14 = schemas.StrSchema
            TimeIn15 = schemas.StrSchema
            TimeOut15 = schemas.StrSchema
            Comments = schemas.StrSchema
            __annotations__ = {
                "APIKey": APIKey,
                "Action": Action,
                "EmployeeId": EmployeeId,
                "TimesheetDate": TimesheetDate,
                "TimeIn1": TimeIn1,
                "TimeOut1": TimeOut1,
                "TimeIn2": TimeIn2,
                "TimeOut2": TimeOut2,
                "TimeIn3": TimeIn3,
                "TimeOut3": TimeOut3,
                "TimeIn4": TimeIn4,
                "TimeOut4": TimeOut4,
                "TimeIn5": TimeIn5,
                "TimeOut5": TimeOut5,
                "TimeIn6": TimeIn6,
                "TimeOut6": TimeOut6,
                "TimeIn7": TimeIn7,
                "TimeOut7": TimeOut7,
                "TimeIn8": TimeIn8,
                "TimeOut8": TimeOut8,
                "TimeIn9": TimeIn9,
                "TimeOut9": TimeOut9,
                "TimeIn10": TimeIn10,
                "TimeOut10": TimeOut10,
                "TimeIn11": TimeIn11,
                "TimeOut11": TimeOut11,
                "TimeIn12": TimeIn12,
                "TimeOut12": TimeOut12,
                "TimeIn13": TimeIn13,
                "TimeOut13": TimeOut13,
                "TimeIn14": TimeIn14,
                "TimeOut14": TimeOut14,
                "TimeIn15": TimeIn15,
                "TimeOut15": TimeOut15,
                "Comments": Comments,
            }
    
    APIKey: 'APIKey'
    Action: MetaOapg.properties.Action
    EmployeeId: 'EmployeeId'
    TimesheetDate: MetaOapg.properties.TimesheetDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["APIKey"]) -> 'APIKey': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Action"]) -> MetaOapg.properties.Action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> 'EmployeeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimesheetDate"]) -> MetaOapg.properties.TimesheetDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn1"]) -> MetaOapg.properties.TimeIn1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut1"]) -> MetaOapg.properties.TimeOut1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn2"]) -> MetaOapg.properties.TimeIn2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut2"]) -> MetaOapg.properties.TimeOut2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn3"]) -> MetaOapg.properties.TimeIn3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut3"]) -> MetaOapg.properties.TimeOut3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn4"]) -> MetaOapg.properties.TimeIn4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut4"]) -> MetaOapg.properties.TimeOut4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn5"]) -> MetaOapg.properties.TimeIn5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut5"]) -> MetaOapg.properties.TimeOut5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn6"]) -> MetaOapg.properties.TimeIn6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut6"]) -> MetaOapg.properties.TimeOut6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn7"]) -> MetaOapg.properties.TimeIn7: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut7"]) -> MetaOapg.properties.TimeOut7: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn8"]) -> MetaOapg.properties.TimeIn8: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut8"]) -> MetaOapg.properties.TimeOut8: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn9"]) -> MetaOapg.properties.TimeIn9: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut9"]) -> MetaOapg.properties.TimeOut9: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn10"]) -> MetaOapg.properties.TimeIn10: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut10"]) -> MetaOapg.properties.TimeOut10: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn11"]) -> MetaOapg.properties.TimeIn11: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut11"]) -> MetaOapg.properties.TimeOut11: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn12"]) -> MetaOapg.properties.TimeIn12: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut12"]) -> MetaOapg.properties.TimeOut12: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn13"]) -> MetaOapg.properties.TimeIn13: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut13"]) -> MetaOapg.properties.TimeOut13: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn14"]) -> MetaOapg.properties.TimeIn14: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut14"]) -> MetaOapg.properties.TimeOut14: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeIn15"]) -> MetaOapg.properties.TimeIn15: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOut15"]) -> MetaOapg.properties.TimeOut15: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Comments"]) -> MetaOapg.properties.Comments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["APIKey", "Action", "EmployeeId", "TimesheetDate", "TimeIn1", "TimeOut1", "TimeIn2", "TimeOut2", "TimeIn3", "TimeOut3", "TimeIn4", "TimeOut4", "TimeIn5", "TimeOut5", "TimeIn6", "TimeOut6", "TimeIn7", "TimeOut7", "TimeIn8", "TimeOut8", "TimeIn9", "TimeOut9", "TimeIn10", "TimeOut10", "TimeIn11", "TimeOut11", "TimeIn12", "TimeOut12", "TimeIn13", "TimeOut13", "TimeIn14", "TimeOut14", "TimeIn15", "TimeOut15", "Comments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["APIKey"]) -> 'APIKey': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Action"]) -> MetaOapg.properties.Action: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> 'EmployeeId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimesheetDate"]) -> MetaOapg.properties.TimesheetDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn1"]) -> typing.Union[MetaOapg.properties.TimeIn1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut1"]) -> typing.Union[MetaOapg.properties.TimeOut1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn2"]) -> typing.Union[MetaOapg.properties.TimeIn2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut2"]) -> typing.Union[MetaOapg.properties.TimeOut2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn3"]) -> typing.Union[MetaOapg.properties.TimeIn3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut3"]) -> typing.Union[MetaOapg.properties.TimeOut3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn4"]) -> typing.Union[MetaOapg.properties.TimeIn4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut4"]) -> typing.Union[MetaOapg.properties.TimeOut4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn5"]) -> typing.Union[MetaOapg.properties.TimeIn5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut5"]) -> typing.Union[MetaOapg.properties.TimeOut5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn6"]) -> typing.Union[MetaOapg.properties.TimeIn6, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut6"]) -> typing.Union[MetaOapg.properties.TimeOut6, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn7"]) -> typing.Union[MetaOapg.properties.TimeIn7, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut7"]) -> typing.Union[MetaOapg.properties.TimeOut7, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn8"]) -> typing.Union[MetaOapg.properties.TimeIn8, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut8"]) -> typing.Union[MetaOapg.properties.TimeOut8, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn9"]) -> typing.Union[MetaOapg.properties.TimeIn9, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut9"]) -> typing.Union[MetaOapg.properties.TimeOut9, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn10"]) -> typing.Union[MetaOapg.properties.TimeIn10, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut10"]) -> typing.Union[MetaOapg.properties.TimeOut10, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn11"]) -> typing.Union[MetaOapg.properties.TimeIn11, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut11"]) -> typing.Union[MetaOapg.properties.TimeOut11, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn12"]) -> typing.Union[MetaOapg.properties.TimeIn12, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut12"]) -> typing.Union[MetaOapg.properties.TimeOut12, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn13"]) -> typing.Union[MetaOapg.properties.TimeIn13, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut13"]) -> typing.Union[MetaOapg.properties.TimeOut13, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn14"]) -> typing.Union[MetaOapg.properties.TimeIn14, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut14"]) -> typing.Union[MetaOapg.properties.TimeOut14, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeIn15"]) -> typing.Union[MetaOapg.properties.TimeIn15, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOut15"]) -> typing.Union[MetaOapg.properties.TimeOut15, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Comments"]) -> typing.Union[MetaOapg.properties.Comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["APIKey", "Action", "EmployeeId", "TimesheetDate", "TimeIn1", "TimeOut1", "TimeIn2", "TimeOut2", "TimeIn3", "TimeOut3", "TimeIn4", "TimeOut4", "TimeIn5", "TimeOut5", "TimeIn6", "TimeOut6", "TimeIn7", "TimeOut7", "TimeIn8", "TimeOut8", "TimeIn9", "TimeOut9", "TimeIn10", "TimeOut10", "TimeIn11", "TimeOut11", "TimeIn12", "TimeOut12", "TimeIn13", "TimeOut13", "TimeIn14", "TimeOut14", "TimeIn15", "TimeOut15", "Comments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        APIKey: 'APIKey',
        Action: typing.Union[MetaOapg.properties.Action, str, ],
        EmployeeId: 'EmployeeId',
        TimesheetDate: typing.Union[MetaOapg.properties.TimesheetDate, str, date, ],
        TimeIn1: typing.Union[MetaOapg.properties.TimeIn1, str, schemas.Unset] = schemas.unset,
        TimeOut1: typing.Union[MetaOapg.properties.TimeOut1, str, schemas.Unset] = schemas.unset,
        TimeIn2: typing.Union[MetaOapg.properties.TimeIn2, str, schemas.Unset] = schemas.unset,
        TimeOut2: typing.Union[MetaOapg.properties.TimeOut2, str, schemas.Unset] = schemas.unset,
        TimeIn3: typing.Union[MetaOapg.properties.TimeIn3, str, schemas.Unset] = schemas.unset,
        TimeOut3: typing.Union[MetaOapg.properties.TimeOut3, str, schemas.Unset] = schemas.unset,
        TimeIn4: typing.Union[MetaOapg.properties.TimeIn4, str, schemas.Unset] = schemas.unset,
        TimeOut4: typing.Union[MetaOapg.properties.TimeOut4, str, schemas.Unset] = schemas.unset,
        TimeIn5: typing.Union[MetaOapg.properties.TimeIn5, str, schemas.Unset] = schemas.unset,
        TimeOut5: typing.Union[MetaOapg.properties.TimeOut5, str, schemas.Unset] = schemas.unset,
        TimeIn6: typing.Union[MetaOapg.properties.TimeIn6, str, schemas.Unset] = schemas.unset,
        TimeOut6: typing.Union[MetaOapg.properties.TimeOut6, str, schemas.Unset] = schemas.unset,
        TimeIn7: typing.Union[MetaOapg.properties.TimeIn7, str, schemas.Unset] = schemas.unset,
        TimeOut7: typing.Union[MetaOapg.properties.TimeOut7, str, schemas.Unset] = schemas.unset,
        TimeIn8: typing.Union[MetaOapg.properties.TimeIn8, str, schemas.Unset] = schemas.unset,
        TimeOut8: typing.Union[MetaOapg.properties.TimeOut8, str, schemas.Unset] = schemas.unset,
        TimeIn9: typing.Union[MetaOapg.properties.TimeIn9, str, schemas.Unset] = schemas.unset,
        TimeOut9: typing.Union[MetaOapg.properties.TimeOut9, str, schemas.Unset] = schemas.unset,
        TimeIn10: typing.Union[MetaOapg.properties.TimeIn10, str, schemas.Unset] = schemas.unset,
        TimeOut10: typing.Union[MetaOapg.properties.TimeOut10, str, schemas.Unset] = schemas.unset,
        TimeIn11: typing.Union[MetaOapg.properties.TimeIn11, str, schemas.Unset] = schemas.unset,
        TimeOut11: typing.Union[MetaOapg.properties.TimeOut11, str, schemas.Unset] = schemas.unset,
        TimeIn12: typing.Union[MetaOapg.properties.TimeIn12, str, schemas.Unset] = schemas.unset,
        TimeOut12: typing.Union[MetaOapg.properties.TimeOut12, str, schemas.Unset] = schemas.unset,
        TimeIn13: typing.Union[MetaOapg.properties.TimeIn13, str, schemas.Unset] = schemas.unset,
        TimeOut13: typing.Union[MetaOapg.properties.TimeOut13, str, schemas.Unset] = schemas.unset,
        TimeIn14: typing.Union[MetaOapg.properties.TimeIn14, str, schemas.Unset] = schemas.unset,
        TimeOut14: typing.Union[MetaOapg.properties.TimeOut14, str, schemas.Unset] = schemas.unset,
        TimeIn15: typing.Union[MetaOapg.properties.TimeIn15, str, schemas.Unset] = schemas.unset,
        TimeOut15: typing.Union[MetaOapg.properties.TimeOut15, str, schemas.Unset] = schemas.unset,
        Comments: typing.Union[MetaOapg.properties.Comments, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateNewTimesheetDefinition':
        return super().__new__(
            cls,
            *args,
            APIKey=APIKey,
            Action=Action,
            EmployeeId=EmployeeId,
            TimesheetDate=TimesheetDate,
            TimeIn1=TimeIn1,
            TimeOut1=TimeOut1,
            TimeIn2=TimeIn2,
            TimeOut2=TimeOut2,
            TimeIn3=TimeIn3,
            TimeOut3=TimeOut3,
            TimeIn4=TimeIn4,
            TimeOut4=TimeOut4,
            TimeIn5=TimeIn5,
            TimeOut5=TimeOut5,
            TimeIn6=TimeIn6,
            TimeOut6=TimeOut6,
            TimeIn7=TimeIn7,
            TimeOut7=TimeOut7,
            TimeIn8=TimeIn8,
            TimeOut8=TimeOut8,
            TimeIn9=TimeIn9,
            TimeOut9=TimeOut9,
            TimeIn10=TimeIn10,
            TimeOut10=TimeOut10,
            TimeIn11=TimeIn11,
            TimeOut11=TimeOut11,
            TimeIn12=TimeIn12,
            TimeOut12=TimeOut12,
            TimeIn13=TimeIn13,
            TimeOut13=TimeOut13,
            TimeIn14=TimeIn14,
            TimeOut14=TimeOut14,
            TimeIn15=TimeIn15,
            TimeOut15=TimeOut15,
            Comments=Comments,
            _configuration=_configuration,
            **kwargs,
        )

from people_hr_python_sdk.model.api_key import APIKey
from people_hr_python_sdk.model.employee_id import EmployeeId
