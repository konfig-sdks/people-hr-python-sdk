import typing_extensions

from people_hr_python_sdk.apis.tags import TagValues
from people_hr_python_sdk.apis.tags.employee_project_timesheet_api import EmployeeProjectTimesheetApi
from people_hr_python_sdk.apis.tags.employee_api import EmployeeApi
from people_hr_python_sdk.apis.tags.employee_custom_screen_api import EmployeeCustomScreenApi
from people_hr_python_sdk.apis.tags.other_event_api import OtherEventApi
from people_hr_python_sdk.apis.tags.employee_appraisal_api import EmployeeAppraisalApi
from people_hr_python_sdk.apis.tags.employee_benefit_api import EmployeeBenefitApi
from people_hr_python_sdk.apis.tags.employee_cpd_api import EmployeeCPDApi
from people_hr_python_sdk.apis.tags.employee_driving_api import EmployeeDrivingApi
from people_hr_python_sdk.apis.tags.employee_qualification_api import EmployeeQualificationApi
from people_hr_python_sdk.apis.tags.employee_vehicle_api import EmployeeVehicleApi
from people_hr_python_sdk.apis.tags.maternity_paternity_api import MaternityPaternityApi
from people_hr_python_sdk.apis.tags.employee_holiday_api import EmployeeHolidayApi
from people_hr_python_sdk.apis.tags.employee_absence_api import EmployeeAbsenceApi
from people_hr_python_sdk.apis.tags.employee_timesheet_api import EmployeeTimesheetApi
from people_hr_python_sdk.apis.tags.employee_training_api import EmployeeTrainingApi
from people_hr_python_sdk.apis.tags.holiday_entitlement_api import HolidayEntitlementApi
from people_hr_python_sdk.apis.tags.right_to_work_api import RightToWorkApi
from people_hr_python_sdk.apis.tags.background_check_api import BackgroundCheckApi
from people_hr_python_sdk.apis.tags.employeee_late_api import EmployeeeLateApi
from people_hr_python_sdk.apis.tags.employee_salary_api import EmployeeSalaryApi
from people_hr_python_sdk.apis.tags.employee_document_api import EmployeeDocumentApi
from people_hr_python_sdk.apis.tags.vacancy_api import VacancyApi
from people_hr_python_sdk.apis.tags.applicant_api import ApplicantApi
from people_hr_python_sdk.apis.tags.query_api import QueryApi
from people_hr_python_sdk.apis.tags.history_api import HistoryApi
from people_hr_python_sdk.apis.tags.email_transaction_api import EmailTransactionApi
from people_hr_python_sdk.apis.tags.work_pattern_api import WorkPatternApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEE_PROJECT_TIMESHEET: EmployeeProjectTimesheetApi,
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.EMPLOYEE_CUSTOM_SCREEN: EmployeeCustomScreenApi,
        TagValues.OTHER_EVENT: OtherEventApi,
        TagValues.EMPLOYEE_APPRAISAL: EmployeeAppraisalApi,
        TagValues.EMPLOYEE_BENEFIT: EmployeeBenefitApi,
        TagValues.EMPLOYEE_CPD: EmployeeCPDApi,
        TagValues.EMPLOYEE_DRIVING: EmployeeDrivingApi,
        TagValues.EMPLOYEE_QUALIFICATION: EmployeeQualificationApi,
        TagValues.EMPLOYEE_VEHICLE: EmployeeVehicleApi,
        TagValues.MATERNITY_PATERNITY_: MaternityPaternityApi,
        TagValues.EMPLOYEE_HOLIDAY: EmployeeHolidayApi,
        TagValues.EMPLOYEE_ABSENCE: EmployeeAbsenceApi,
        TagValues.EMPLOYEE_TIMESHEET: EmployeeTimesheetApi,
        TagValues.EMPLOYEE_TRAINING: EmployeeTrainingApi,
        TagValues.HOLIDAY_ENTITLEMENT: HolidayEntitlementApi,
        TagValues.RIGHT_TO_WORK: RightToWorkApi,
        TagValues.BACKGROUND_CHECK: BackgroundCheckApi,
        TagValues.EMPLOYEEE_LATE: EmployeeeLateApi,
        TagValues.EMPLOYEE_SALARY: EmployeeSalaryApi,
        TagValues.EMPLOYEE_DOCUMENT: EmployeeDocumentApi,
        TagValues.VACANCY: VacancyApi,
        TagValues.APPLICANT: ApplicantApi,
        TagValues.QUERY: QueryApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.EMAIL_TRANSACTION: EmailTransactionApi,
        TagValues.WORK_PATTERN: WorkPatternApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEE_PROJECT_TIMESHEET: EmployeeProjectTimesheetApi,
        TagValues.EMPLOYEE: EmployeeApi,
        TagValues.EMPLOYEE_CUSTOM_SCREEN: EmployeeCustomScreenApi,
        TagValues.OTHER_EVENT: OtherEventApi,
        TagValues.EMPLOYEE_APPRAISAL: EmployeeAppraisalApi,
        TagValues.EMPLOYEE_BENEFIT: EmployeeBenefitApi,
        TagValues.EMPLOYEE_CPD: EmployeeCPDApi,
        TagValues.EMPLOYEE_DRIVING: EmployeeDrivingApi,
        TagValues.EMPLOYEE_QUALIFICATION: EmployeeQualificationApi,
        TagValues.EMPLOYEE_VEHICLE: EmployeeVehicleApi,
        TagValues.MATERNITY_PATERNITY_: MaternityPaternityApi,
        TagValues.EMPLOYEE_HOLIDAY: EmployeeHolidayApi,
        TagValues.EMPLOYEE_ABSENCE: EmployeeAbsenceApi,
        TagValues.EMPLOYEE_TIMESHEET: EmployeeTimesheetApi,
        TagValues.EMPLOYEE_TRAINING: EmployeeTrainingApi,
        TagValues.HOLIDAY_ENTITLEMENT: HolidayEntitlementApi,
        TagValues.RIGHT_TO_WORK: RightToWorkApi,
        TagValues.BACKGROUND_CHECK: BackgroundCheckApi,
        TagValues.EMPLOYEEE_LATE: EmployeeeLateApi,
        TagValues.EMPLOYEE_SALARY: EmployeeSalaryApi,
        TagValues.EMPLOYEE_DOCUMENT: EmployeeDocumentApi,
        TagValues.VACANCY: VacancyApi,
        TagValues.APPLICANT: ApplicantApi,
        TagValues.QUERY: QueryApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.EMAIL_TRANSACTION: EmailTransactionApi,
        TagValues.WORK_PATTERN: WorkPatternApi,
    }
)
