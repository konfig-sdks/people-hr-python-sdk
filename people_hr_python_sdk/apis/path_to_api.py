import typing_extensions

from people_hr_python_sdk.paths import PathValues
from people_hr_python_sdk.apis.paths.employee_____check_authentication import EmployeeCheckAuthentication
from people_hr_python_sdk.apis.paths.employee_____update_employee_id import EmployeeUpdateEmployeeId
from people_hr_python_sdk.apis.paths.employee_____get_all_employee_detail import EmployeeGetAllEmployeeDetail
from people_hr_python_sdk.apis.paths.employee_____get_employee_detail_by_id import EmployeeGetEmployeeDetailById
from people_hr_python_sdk.apis.paths.employee_____create_new_employee import EmployeeCreateNewEmployee
from people_hr_python_sdk.apis.paths.employee_____update_employee_detail import EmployeeUpdateEmployeeDetail
from people_hr_python_sdk.apis.paths.employee_____mark_as_leaver_by_id import EmployeeMarkAsLeaverById
from people_hr_python_sdk.apis.paths.employee_____add_employee_image import EmployeeAddEmployeeImage
from people_hr_python_sdk.apis.paths.employee_salary_____get_salary_detail import EmployeeSalaryGetSalaryDetail
from people_hr_python_sdk.apis.paths.employee_salary_____create_new_salary import EmployeeSalaryCreateNewSalary
from people_hr_python_sdk.apis.paths.employee_salary_____delete_salary import EmployeeSalaryDeleteSalary
from people_hr_python_sdk.apis.paths.employee_holiday_____add_new_holiday import EmployeeHolidayAddNewHoliday
from people_hr_python_sdk.apis.paths.employee_holiday_____update_holiday import EmployeeHolidayUpdateHoliday
from people_hr_python_sdk.apis.paths.employee_holiday_____get_holiday_detail import EmployeeHolidayGetHolidayDetail
from people_hr_python_sdk.apis.paths.employee_holiday_____delete_holiday import EmployeeHolidayDeleteHoliday
from people_hr_python_sdk.apis.paths.employee_absence_____get_absence_detail import EmployeeAbsenceGetAbsenceDetail
from people_hr_python_sdk.apis.paths.employee_absence_____delete_absence import EmployeeAbsenceDeleteAbsence
from people_hr_python_sdk.apis.paths.employee_absence_____add_absence import EmployeeAbsenceAddAbsence
from people_hr_python_sdk.apis.paths.employee_absence_____update_absence import EmployeeAbsenceUpdateAbsence
from people_hr_python_sdk.apis.paths.employee_document_____upload_employee_document import EmployeeDocumentUploadEmployeeDocument
from people_hr_python_sdk.apis.paths.employee_document_____get_all_document import EmployeeDocumentGetAllDocument
from people_hr_python_sdk.apis.paths.employee_document_____get_document_by_id import EmployeeDocumentGetDocumentById
from people_hr_python_sdk.apis.paths.employee_timesheet_____get_timesheet_detail import EmployeeTimesheetGetTimesheetDetail
from people_hr_python_sdk.apis.paths.employee_timesheet_____create_new_timesheet import EmployeeTimesheetCreateNewTimesheet
from people_hr_python_sdk.apis.paths.employee_timesheet_____update_timesheet import EmployeeTimesheetUpdateTimesheet
from people_hr_python_sdk.apis.paths.employee_timesheet_____delete_timesheet import EmployeeTimesheetDeleteTimesheet
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____get_project_timesheet_detail import EmployeeProjectTimesheetGetProjectTimesheetDetail
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____get_project_timesheet_by_transaction_id import EmployeeProjectTimesheetGetProjectTimesheetByTransactionId
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____create_project_timesheet import EmployeeProjectTimesheetCreateProjectTimesheet
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____update_project_timesheet import EmployeeProjectTimesheetUpdateProjectTimesheet
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____delete_project_timesheet import EmployeeProjectTimesheetDeleteProjectTimesheet
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____get_all_timesheet_project import EmployeeProjectTimesheetGetAllTimesheetProject
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____add_new_project import EmployeeProjectTimesheetAddNewProject
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____edit_project import EmployeeProjectTimesheetEditProject
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____get_all_project_task import EmployeeProjectTimesheetGetAllProjectTask
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____add_new_project_task import EmployeeProjectTimesheetAddNewProjectTask
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____edit_project_task import EmployeeProjectTimesheetEditProjectTask
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____get_all_project_task_detail import EmployeeProjectTimesheetGetAllProjectTaskDetail
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____add_new_project_task_detail import EmployeeProjectTimesheetAddNewProjectTaskDetail
from people_hr_python_sdk.apis.paths.employee_project_timesheet_____edit_project_task_detail import EmployeeProjectTimesheetEditProjectTaskDetail
from people_hr_python_sdk.apis.paths.employee_appraisal_____get_by_employee_id import EmployeeAppraisalGetByEmployeeId
from people_hr_python_sdk.apis.paths.employee_appraisal_____get_by_appraisal_id import EmployeeAppraisalGetByAppraisalId
from people_hr_python_sdk.apis.paths.employee_appraisal_____add_new_appraisal import EmployeeAppraisalAddNewAppraisal
from people_hr_python_sdk.apis.paths.employee_appraisal_____update_appraisal import EmployeeAppraisalUpdateAppraisal
from people_hr_python_sdk.apis.paths.employee_appraisal_____delete_appraisal import EmployeeAppraisalDeleteAppraisal
from people_hr_python_sdk.apis.paths.employee_benefit_____get_benefit_by_employee_id import EmployeeBenefitGetBenefitByEmployeeId
from people_hr_python_sdk.apis.paths.employee_benefit_____get_benefit_by_benefit_id import EmployeeBenefitGetBenefitByBenefitId
from people_hr_python_sdk.apis.paths.employee_benefit_____add_new_benefit import EmployeeBenefitAddNewBenefit
from people_hr_python_sdk.apis.paths.employee_benefit_____update_benefit import EmployeeBenefitUpdateBenefit
from people_hr_python_sdk.apis.paths.employee_benefit_____delete_benefit import EmployeeBenefitDeleteBenefit
from people_hr_python_sdk.apis.paths.employee_cpd_____get_cpdby_employee_id import EmployeeCPDGetCPDByEmployeeId
from people_hr_python_sdk.apis.paths.employee_cpd_____get_by_cpdid import EmployeeCPDGetByCPDId
from people_hr_python_sdk.apis.paths.employee_cpd_____add_new_cpd import EmployeeCPDAddNewCPD
from people_hr_python_sdk.apis.paths.employee_cpd_____update_cpd import EmployeeCPDUpdateCPD
from people_hr_python_sdk.apis.paths.employee_cpd_____delete_cpd import EmployeeCPDDeleteCPD
from people_hr_python_sdk.apis.paths.employee_driving_____get_driving_license_by_employee_id import EmployeeDrivingGetDrivingLicenseByEmployeeId
from people_hr_python_sdk.apis.paths.employee_driving_____get_driving_license_by_driving_id import EmployeeDrivingGetDrivingLicenseByDrivingId
from people_hr_python_sdk.apis.paths.employee_driving_____add_new_driving_license import EmployeeDrivingAddNewDrivingLicense
from people_hr_python_sdk.apis.paths.employee_driving_____update_driving_license import EmployeeDrivingUpdateDrivingLicense
from people_hr_python_sdk.apis.paths.employee_driving_____delete_driving_license import EmployeeDrivingDeleteDrivingLicense
from people_hr_python_sdk.apis.paths.employee_qualification_____get_qualification_by_employee_id import EmployeeQualificationGetQualificationByEmployeeId
from people_hr_python_sdk.apis.paths.employee_qualification_____get_qualification_by_qualification_id import EmployeeQualificationGetQualificationByQualificationId
from people_hr_python_sdk.apis.paths.employee_qualification_____add_new_qualification import EmployeeQualificationAddNewQualification
from people_hr_python_sdk.apis.paths.employee_qualification_____update_qualification import EmployeeQualificationUpdateQualification
from people_hr_python_sdk.apis.paths.employee_qualification_____delete_qualification import EmployeeQualificationDeleteQualification
from people_hr_python_sdk.apis.paths.employee_training_____get_training_detail import EmployeeTrainingGetTrainingDetail
from people_hr_python_sdk.apis.paths.employee_training_____addtrainingdetail import EmployeeTrainingAddtrainingdetail
from people_hr_python_sdk.apis.paths.employee_training_____updatetrainingdetail import EmployeeTrainingUpdatetrainingdetail
from people_hr_python_sdk.apis.paths.employee_training_____deletetrainingdetail import EmployeeTrainingDeletetrainingdetail
from people_hr_python_sdk.apis.paths.employee_vehicle_____add_new_vehicle_detail import EmployeeVehicleAddNewVehicleDetail
from people_hr_python_sdk.apis.paths.employee_vehicle_____update_vehicle_detail import EmployeeVehicleUpdateVehicleDetail
from people_hr_python_sdk.apis.paths.employee_vehicle_____delete_vehicle_detail import EmployeeVehicleDeleteVehicleDetail
from people_hr_python_sdk.apis.paths.employee_vehicle_____get_by_vehicle_detail_id import EmployeeVehicleGetByVehicleDetailId
from people_hr_python_sdk.apis.paths.employee_vehicle_____get_vehicle_by_employee_id import EmployeeVehicleGetVehicleByEmployeeId
from people_hr_python_sdk.apis.paths.employee_custom_screen_____get_custom_screen_detail import EmployeeCustomScreenGetCustomScreenDetail
from people_hr_python_sdk.apis.paths.employee_custom_screen_____get_custom_screen_by_employee_id import EmployeeCustomScreenGetCustomScreenByEmployeeId
from people_hr_python_sdk.apis.paths.employee_custom_screen_____get_by_custom_screen_transaction_id import EmployeeCustomScreenGetByCustomScreenTransactionId
from people_hr_python_sdk.apis.paths.employee_custom_screen_____add_new_custom_screen_transaction import EmployeeCustomScreenAddNewCustomScreenTransaction
from people_hr_python_sdk.apis.paths.employee_custom_screen_____update_custom_screen_transaction import EmployeeCustomScreenUpdateCustomScreenTransaction
from people_hr_python_sdk.apis.paths.employee_custom_screen_____delete_custom_screen_transaction import EmployeeCustomScreenDeleteCustomScreenTransaction
from people_hr_python_sdk.apis.paths.holiday_entitlement_____get_holiday_entitlement import HolidayEntitlementGetHolidayEntitlement
from people_hr_python_sdk.apis.paths.holiday_entitlement_____get_next_year_holiday_entitlement import HolidayEntitlementGetNextYearHolidayEntitlement
from people_hr_python_sdk.apis.paths.holiday_entitlement_____update_holiday_entitlement import HolidayEntitlementUpdateHolidayEntitlement
from people_hr_python_sdk.apis.paths.holiday_entitlement_____update_next_year_holiday_entitlement import HolidayEntitlementUpdateNextYearHolidayEntitlement
from people_hr_python_sdk.apis.paths.history_____get_history_by_employee_id_and_field_name import HistoryGetHistoryByEmployeeIdAndFieldName
from people_hr_python_sdk.apis.paths.query_____get_query_result import QueryGetQueryResult
from people_hr_python_sdk.apis.paths.query_____get_query_result_by_query_name import QueryGetQueryResultByQueryName
from people_hr_python_sdk.apis.paths.email_transaction_____email_inbox import EmailTransactionEmailInbox
from people_hr_python_sdk.apis.paths.right_to_work_____addrighttoworkdetail import RightToWorkAddrighttoworkdetail
from people_hr_python_sdk.apis.paths.right_to_work_____getrighttoworkdetail import RightToWorkGetrighttoworkdetail
from people_hr_python_sdk.apis.paths.right_to_work_____updaterighttoworkdetail import RightToWorkUpdaterighttoworkdetail
from people_hr_python_sdk.apis.paths.right_to_work_____deleterighttoworkdetail import RightToWorkDeleterighttoworkdetail
from people_hr_python_sdk.apis.paths.background_check_____get_background_check_detail_by_employee_id import BackgroundCheckGetBackgroundCheckDetailByEmployeeId
from people_hr_python_sdk.apis.paths.background_check_____add_background_check_detail import BackgroundCheckAddBackgroundCheckDetail
from people_hr_python_sdk.apis.paths.background_check_____update_background_check_detail import BackgroundCheckUpdateBackgroundCheckDetail
from people_hr_python_sdk.apis.paths.background_check_____delete_background_check_detail import BackgroundCheckDeleteBackgroundCheckDetail
from people_hr_python_sdk.apis.paths.other_event_____getothereventdetail import OtherEventGetothereventdetail
from people_hr_python_sdk.apis.paths.other_event_____getotherevententitlement import OtherEventGetotherevententitlement
from people_hr_python_sdk.apis.paths.other_event_____delete_other_event import OtherEventDeleteOtherEvent
from people_hr_python_sdk.apis.paths.other_event_____addothereventleave import OtherEventAddothereventleave
from people_hr_python_sdk.apis.paths.other_event_____updateothereventleave import OtherEventUpdateothereventleave
from people_hr_python_sdk.apis.paths.other_event_____addotherevententitlement import OtherEventAddotherevententitlement
from people_hr_python_sdk.apis.paths.vacancy_____create_new_vacancy import VacancyCreateNewVacancy
from people_hr_python_sdk.apis.paths.vacancy_____get_vacancy import VacancyGetVacancy
from people_hr_python_sdk.apis.paths.vacancy_____get_all_vacancies import VacancyGetAllVacancies
from people_hr_python_sdk.apis.paths.applicant_____create_new_applicant import ApplicantCreateNewApplicant
from people_hr_python_sdk.apis.paths.applicant_____uploadapplicantdocument import ApplicantUploadapplicantdocument
from people_hr_python_sdk.apis.paths.applicant_____check_duplicate_applicant import ApplicantCheckDuplicateApplicant
from people_hr_python_sdk.apis.paths.work_pattern_____get_work_pattern_detail import WorkPatternGetWorkPatternDetail
from people_hr_python_sdk.apis.paths.employeee_late_____get_late_by_employee_id import EmployeeeLateGetLateByEmployeeId
from people_hr_python_sdk.apis.paths.employeee_late_____add_new_late import EmployeeeLateAddNewLate
from people_hr_python_sdk.apis.paths.employeee_late_____update_late import EmployeeeLateUpdateLate
from people_hr_python_sdk.apis.paths.employeee_late_____delete_late import EmployeeeLateDeleteLate
from people_hr_python_sdk.apis.paths.maternity_paternity_____get_by_maternity_paternity_id import MaternityPaternityGetByMaternityPaternityId
from people_hr_python_sdk.apis.paths.maternity_paternity_____get_maternity_paternity_by_employee_id import MaternityPaternityGetMaternityPaternityByEmployeeId
from people_hr_python_sdk.apis.paths.maternity_paternity_____add_new_maternity_paternity import MaternityPaternityAddNewMaternityPaternity
from people_hr_python_sdk.apis.paths.maternity_paternity_____update_maternity_paternity import MaternityPaternityUpdateMaternityPaternity
from people_hr_python_sdk.apis.paths.maternity_paternity_____delete_maternity_paternity import MaternityPaternityDeleteMaternityPaternity

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EMPLOYEE__CHECK_AUTHENTICATION: EmployeeCheckAuthentication,
        PathValues.EMPLOYEE__UPDATE_EMPLOYEE_ID: EmployeeUpdateEmployeeId,
        PathValues.EMPLOYEE__GET_ALL_EMPLOYEE_DETAIL: EmployeeGetAllEmployeeDetail,
        PathValues.EMPLOYEE__GET_EMPLOYEE_DETAIL_BY_ID: EmployeeGetEmployeeDetailById,
        PathValues.EMPLOYEE__CREATE_NEW_EMPLOYEE: EmployeeCreateNewEmployee,
        PathValues.EMPLOYEE__UPDATE_EMPLOYEE_DETAIL: EmployeeUpdateEmployeeDetail,
        PathValues.EMPLOYEE__MARK_AS_LEAVER_BY_ID: EmployeeMarkAsLeaverById,
        PathValues.EMPLOYEE__ADD_EMPLOYEE_IMAGE: EmployeeAddEmployeeImage,
        PathValues.EMPLOYEE_SALARY__GET_SALARY_DETAIL: EmployeeSalaryGetSalaryDetail,
        PathValues.EMPLOYEE_SALARY__CREATE_NEW_SALARY: EmployeeSalaryCreateNewSalary,
        PathValues.EMPLOYEE_SALARY__DELETE_SALARY: EmployeeSalaryDeleteSalary,
        PathValues.EMPLOYEE_HOLIDAY__ADD_NEW_HOLIDAY: EmployeeHolidayAddNewHoliday,
        PathValues.EMPLOYEE_HOLIDAY__UPDATE_HOLIDAY: EmployeeHolidayUpdateHoliday,
        PathValues.EMPLOYEE_HOLIDAY__GET_HOLIDAY_DETAIL: EmployeeHolidayGetHolidayDetail,
        PathValues.EMPLOYEE_HOLIDAY__DELETE_HOLIDAY: EmployeeHolidayDeleteHoliday,
        PathValues.EMPLOYEE_ABSENCE__GET_ABSENCE_DETAIL: EmployeeAbsenceGetAbsenceDetail,
        PathValues.EMPLOYEE_ABSENCE__DELETE_ABSENCE: EmployeeAbsenceDeleteAbsence,
        PathValues.EMPLOYEE_ABSENCE__ADD_ABSENCE: EmployeeAbsenceAddAbsence,
        PathValues.EMPLOYEE_ABSENCE__UPDATE_ABSENCE: EmployeeAbsenceUpdateAbsence,
        PathValues.EMPLOYEE_DOCUMENT__UPLOAD_EMPLOYEE_DOCUMENT: EmployeeDocumentUploadEmployeeDocument,
        PathValues.EMPLOYEE_DOCUMENT__GET_ALL_DOCUMENT: EmployeeDocumentGetAllDocument,
        PathValues.EMPLOYEE_DOCUMENT__GET_DOCUMENT_BY_ID: EmployeeDocumentGetDocumentById,
        PathValues.EMPLOYEE_TIMESHEET__GET_TIMESHEET_DETAIL: EmployeeTimesheetGetTimesheetDetail,
        PathValues.EMPLOYEE_TIMESHEET__CREATE_NEW_TIMESHEET: EmployeeTimesheetCreateNewTimesheet,
        PathValues.EMPLOYEE_TIMESHEET__UPDATE_TIMESHEET: EmployeeTimesheetUpdateTimesheet,
        PathValues.EMPLOYEE_TIMESHEET__DELETE_TIMESHEET: EmployeeTimesheetDeleteTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_PROJECT_TIMESHEET_DETAIL: EmployeeProjectTimesheetGetProjectTimesheetDetail,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_PROJECT_TIMESHEET_BY_TRANSACTION_ID: EmployeeProjectTimesheetGetProjectTimesheetByTransactionId,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__CREATE_PROJECT_TIMESHEET: EmployeeProjectTimesheetCreateProjectTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__UPDATE_PROJECT_TIMESHEET: EmployeeProjectTimesheetUpdateProjectTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__DELETE_PROJECT_TIMESHEET: EmployeeProjectTimesheetDeleteProjectTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_ALL_TIMESHEET_PROJECT: EmployeeProjectTimesheetGetAllTimesheetProject,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__ADD_NEW_PROJECT: EmployeeProjectTimesheetAddNewProject,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__EDIT_PROJECT: EmployeeProjectTimesheetEditProject,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_ALL_PROJECT_TASK: EmployeeProjectTimesheetGetAllProjectTask,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__ADD_NEW_PROJECT_TASK: EmployeeProjectTimesheetAddNewProjectTask,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__EDIT_PROJECT_TASK: EmployeeProjectTimesheetEditProjectTask,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_ALL_PROJECT_TASK_DETAIL: EmployeeProjectTimesheetGetAllProjectTaskDetail,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__ADD_NEW_PROJECT_TASK_DETAIL: EmployeeProjectTimesheetAddNewProjectTaskDetail,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__EDIT_PROJECT_TASK_DETAIL: EmployeeProjectTimesheetEditProjectTaskDetail,
        PathValues.EMPLOYEE_APPRAISAL__GET_BY_EMPLOYEE_ID: EmployeeAppraisalGetByEmployeeId,
        PathValues.EMPLOYEE_APPRAISAL__GET_BY_APPRAISAL_ID: EmployeeAppraisalGetByAppraisalId,
        PathValues.EMPLOYEE_APPRAISAL__ADD_NEW_APPRAISAL: EmployeeAppraisalAddNewAppraisal,
        PathValues.EMPLOYEE_APPRAISAL__UPDATE_APPRAISAL: EmployeeAppraisalUpdateAppraisal,
        PathValues.EMPLOYEE_APPRAISAL__DELETE_APPRAISAL: EmployeeAppraisalDeleteAppraisal,
        PathValues.EMPLOYEE_BENEFIT__GET_BENEFIT_BY_EMPLOYEE_ID: EmployeeBenefitGetBenefitByEmployeeId,
        PathValues.EMPLOYEE_BENEFIT__GET_BENEFIT_BY_BENEFIT_ID: EmployeeBenefitGetBenefitByBenefitId,
        PathValues.EMPLOYEE_BENEFIT__ADD_NEW_BENEFIT: EmployeeBenefitAddNewBenefit,
        PathValues.EMPLOYEE_BENEFIT__UPDATE_BENEFIT: EmployeeBenefitUpdateBenefit,
        PathValues.EMPLOYEE_BENEFIT__DELETE_BENEFIT: EmployeeBenefitDeleteBenefit,
        PathValues.EMPLOYEE_CPD__GET_CPDBY_EMPLOYEE_ID: EmployeeCPDGetCPDByEmployeeId,
        PathValues.EMPLOYEE_CPD__GET_BY_CPDID: EmployeeCPDGetByCPDId,
        PathValues.EMPLOYEE_CPD__ADD_NEW_CPD: EmployeeCPDAddNewCPD,
        PathValues.EMPLOYEE_CPD__UPDATE_CPD: EmployeeCPDUpdateCPD,
        PathValues.EMPLOYEE_CPD__DELETE_CPD: EmployeeCPDDeleteCPD,
        PathValues.EMPLOYEE_DRIVING__GET_DRIVING_LICENSE_BY_EMPLOYEE_ID: EmployeeDrivingGetDrivingLicenseByEmployeeId,
        PathValues.EMPLOYEE_DRIVING__GET_DRIVING_LICENSE_BY_DRIVING_ID: EmployeeDrivingGetDrivingLicenseByDrivingId,
        PathValues.EMPLOYEE_DRIVING__ADD_NEW_DRIVING_LICENSE: EmployeeDrivingAddNewDrivingLicense,
        PathValues.EMPLOYEE_DRIVING__UPDATE_DRIVING_LICENSE: EmployeeDrivingUpdateDrivingLicense,
        PathValues.EMPLOYEE_DRIVING__DELETE_DRIVING_LICENSE: EmployeeDrivingDeleteDrivingLicense,
        PathValues.EMPLOYEE_QUALIFICATION__GET_QUALIFICATION_BY_EMPLOYEE_ID: EmployeeQualificationGetQualificationByEmployeeId,
        PathValues.EMPLOYEE_QUALIFICATION__GET_QUALIFICATION_BY_QUALIFICATION_ID: EmployeeQualificationGetQualificationByQualificationId,
        PathValues.EMPLOYEE_QUALIFICATION__ADD_NEW_QUALIFICATION: EmployeeQualificationAddNewQualification,
        PathValues.EMPLOYEE_QUALIFICATION__UPDATE_QUALIFICATION: EmployeeQualificationUpdateQualification,
        PathValues.EMPLOYEE_QUALIFICATION__DELETE_QUALIFICATION: EmployeeQualificationDeleteQualification,
        PathValues.EMPLOYEE_TRAINING__GET_TRAINING_DETAIL: EmployeeTrainingGetTrainingDetail,
        PathValues.EMPLOYEE_TRAINING__ADDTRAININGDETAIL: EmployeeTrainingAddtrainingdetail,
        PathValues.EMPLOYEE_TRAINING__UPDATETRAININGDETAIL: EmployeeTrainingUpdatetrainingdetail,
        PathValues.EMPLOYEE_TRAINING__DELETETRAININGDETAIL: EmployeeTrainingDeletetrainingdetail,
        PathValues.EMPLOYEE_VEHICLE__ADD_NEW_VEHICLE_DETAIL: EmployeeVehicleAddNewVehicleDetail,
        PathValues.EMPLOYEE_VEHICLE__UPDATE_VEHICLE_DETAIL: EmployeeVehicleUpdateVehicleDetail,
        PathValues.EMPLOYEE_VEHICLE__DELETE_VEHICLE_DETAIL: EmployeeVehicleDeleteVehicleDetail,
        PathValues.EMPLOYEE_VEHICLE__GET_BY_VEHICLE_DETAIL_ID: EmployeeVehicleGetByVehicleDetailId,
        PathValues.EMPLOYEE_VEHICLE__GET_VEHICLE_BY_EMPLOYEE_ID: EmployeeVehicleGetVehicleByEmployeeId,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__GET_CUSTOM_SCREEN_DETAIL: EmployeeCustomScreenGetCustomScreenDetail,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__GET_CUSTOM_SCREEN_BY_EMPLOYEE_ID: EmployeeCustomScreenGetCustomScreenByEmployeeId,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__GET_BY_CUSTOM_SCREEN_TRANSACTION_ID: EmployeeCustomScreenGetByCustomScreenTransactionId,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__ADD_NEW_CUSTOM_SCREEN_TRANSACTION: EmployeeCustomScreenAddNewCustomScreenTransaction,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__UPDATE_CUSTOM_SCREEN_TRANSACTION: EmployeeCustomScreenUpdateCustomScreenTransaction,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__DELETE_CUSTOM_SCREEN_TRANSACTION: EmployeeCustomScreenDeleteCustomScreenTransaction,
        PathValues.HOLIDAY_ENTITLEMENT__GET_HOLIDAY_ENTITLEMENT: HolidayEntitlementGetHolidayEntitlement,
        PathValues.HOLIDAY_ENTITLEMENT__GET_NEXT_YEAR_HOLIDAY_ENTITLEMENT: HolidayEntitlementGetNextYearHolidayEntitlement,
        PathValues.HOLIDAY_ENTITLEMENT__UPDATE_HOLIDAY_ENTITLEMENT: HolidayEntitlementUpdateHolidayEntitlement,
        PathValues.HOLIDAY_ENTITLEMENT__UPDATE_NEXT_YEAR_HOLIDAY_ENTITLEMENT: HolidayEntitlementUpdateNextYearHolidayEntitlement,
        PathValues.HISTORY__GET_HISTORY_BY_EMPLOYEE_ID_AND_FIELD_NAME: HistoryGetHistoryByEmployeeIdAndFieldName,
        PathValues.QUERY__GET_QUERY_RESULT: QueryGetQueryResult,
        PathValues.QUERY__GET_QUERY_RESULT_BY_QUERY_NAME: QueryGetQueryResultByQueryName,
        PathValues.EMAIL_TRANSACTION__EMAIL_INBOX: EmailTransactionEmailInbox,
        PathValues.RIGHT_TO_WORK__ADDRIGHTTOWORKDETAIL: RightToWorkAddrighttoworkdetail,
        PathValues.RIGHT_TO_WORK__GETRIGHTTOWORKDETAIL: RightToWorkGetrighttoworkdetail,
        PathValues.RIGHT_TO_WORK__UPDATERIGHTTOWORKDETAIL: RightToWorkUpdaterighttoworkdetail,
        PathValues.RIGHT_TO_WORK__DELETERIGHTTOWORKDETAIL: RightToWorkDeleterighttoworkdetail,
        PathValues.BACKGROUND_CHECK__GET_BACKGROUND_CHECK_DETAIL_BY_EMPLOYEE_ID: BackgroundCheckGetBackgroundCheckDetailByEmployeeId,
        PathValues.BACKGROUND_CHECK__ADD_BACKGROUND_CHECK_DETAIL: BackgroundCheckAddBackgroundCheckDetail,
        PathValues.BACKGROUND_CHECK__UPDATE_BACKGROUND_CHECK_DETAIL: BackgroundCheckUpdateBackgroundCheckDetail,
        PathValues.BACKGROUND_CHECK__DELETE_BACKGROUND_CHECK_DETAIL: BackgroundCheckDeleteBackgroundCheckDetail,
        PathValues.OTHER_EVENT__GETOTHEREVENTDETAIL: OtherEventGetothereventdetail,
        PathValues.OTHER_EVENT__GETOTHEREVENTENTITLEMENT: OtherEventGetotherevententitlement,
        PathValues.OTHER_EVENT__DELETE_OTHER_EVENT: OtherEventDeleteOtherEvent,
        PathValues.OTHER_EVENT__ADDOTHEREVENTLEAVE: OtherEventAddothereventleave,
        PathValues.OTHER_EVENT__UPDATEOTHEREVENTLEAVE: OtherEventUpdateothereventleave,
        PathValues.OTHER_EVENT__ADDOTHEREVENTENTITLEMENT: OtherEventAddotherevententitlement,
        PathValues.VACANCY__CREATE_NEW_VACANCY: VacancyCreateNewVacancy,
        PathValues.VACANCY__GET_VACANCY: VacancyGetVacancy,
        PathValues.VACANCY__GET_ALL_VACANCIES: VacancyGetAllVacancies,
        PathValues.APPLICANT__CREATE_NEW_APPLICANT: ApplicantCreateNewApplicant,
        PathValues.APPLICANT__UPLOADAPPLICANTDOCUMENT: ApplicantUploadapplicantdocument,
        PathValues.APPLICANT__CHECK_DUPLICATE_APPLICANT: ApplicantCheckDuplicateApplicant,
        PathValues.WORK_PATTERN__GET_WORK_PATTERN_DETAIL: WorkPatternGetWorkPatternDetail,
        PathValues.EMPLOYEEE_LATE__GET_LATE_BY_EMPLOYEE_ID: EmployeeeLateGetLateByEmployeeId,
        PathValues.EMPLOYEEE_LATE__ADD_NEW_LATE: EmployeeeLateAddNewLate,
        PathValues.EMPLOYEEE_LATE__UPDATE_LATE: EmployeeeLateUpdateLate,
        PathValues.EMPLOYEEE_LATE__DELETE_LATE: EmployeeeLateDeleteLate,
        PathValues.MATERNITY_PATERNITY__GET_BY_MATERNITY_PATERNITY_ID: MaternityPaternityGetByMaternityPaternityId,
        PathValues.MATERNITY_PATERNITY__GET_MATERNITY_PATERNITY_BY_EMPLOYEE_ID: MaternityPaternityGetMaternityPaternityByEmployeeId,
        PathValues.MATERNITY_PATERNITY__ADD_NEW_MATERNITY_PATERNITY: MaternityPaternityAddNewMaternityPaternity,
        PathValues.MATERNITY_PATERNITY__UPDATE_MATERNITY_PATERNITY: MaternityPaternityUpdateMaternityPaternity,
        PathValues.MATERNITY_PATERNITY__DELETE_MATERNITY_PATERNITY: MaternityPaternityDeleteMaternityPaternity,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EMPLOYEE__CHECK_AUTHENTICATION: EmployeeCheckAuthentication,
        PathValues.EMPLOYEE__UPDATE_EMPLOYEE_ID: EmployeeUpdateEmployeeId,
        PathValues.EMPLOYEE__GET_ALL_EMPLOYEE_DETAIL: EmployeeGetAllEmployeeDetail,
        PathValues.EMPLOYEE__GET_EMPLOYEE_DETAIL_BY_ID: EmployeeGetEmployeeDetailById,
        PathValues.EMPLOYEE__CREATE_NEW_EMPLOYEE: EmployeeCreateNewEmployee,
        PathValues.EMPLOYEE__UPDATE_EMPLOYEE_DETAIL: EmployeeUpdateEmployeeDetail,
        PathValues.EMPLOYEE__MARK_AS_LEAVER_BY_ID: EmployeeMarkAsLeaverById,
        PathValues.EMPLOYEE__ADD_EMPLOYEE_IMAGE: EmployeeAddEmployeeImage,
        PathValues.EMPLOYEE_SALARY__GET_SALARY_DETAIL: EmployeeSalaryGetSalaryDetail,
        PathValues.EMPLOYEE_SALARY__CREATE_NEW_SALARY: EmployeeSalaryCreateNewSalary,
        PathValues.EMPLOYEE_SALARY__DELETE_SALARY: EmployeeSalaryDeleteSalary,
        PathValues.EMPLOYEE_HOLIDAY__ADD_NEW_HOLIDAY: EmployeeHolidayAddNewHoliday,
        PathValues.EMPLOYEE_HOLIDAY__UPDATE_HOLIDAY: EmployeeHolidayUpdateHoliday,
        PathValues.EMPLOYEE_HOLIDAY__GET_HOLIDAY_DETAIL: EmployeeHolidayGetHolidayDetail,
        PathValues.EMPLOYEE_HOLIDAY__DELETE_HOLIDAY: EmployeeHolidayDeleteHoliday,
        PathValues.EMPLOYEE_ABSENCE__GET_ABSENCE_DETAIL: EmployeeAbsenceGetAbsenceDetail,
        PathValues.EMPLOYEE_ABSENCE__DELETE_ABSENCE: EmployeeAbsenceDeleteAbsence,
        PathValues.EMPLOYEE_ABSENCE__ADD_ABSENCE: EmployeeAbsenceAddAbsence,
        PathValues.EMPLOYEE_ABSENCE__UPDATE_ABSENCE: EmployeeAbsenceUpdateAbsence,
        PathValues.EMPLOYEE_DOCUMENT__UPLOAD_EMPLOYEE_DOCUMENT: EmployeeDocumentUploadEmployeeDocument,
        PathValues.EMPLOYEE_DOCUMENT__GET_ALL_DOCUMENT: EmployeeDocumentGetAllDocument,
        PathValues.EMPLOYEE_DOCUMENT__GET_DOCUMENT_BY_ID: EmployeeDocumentGetDocumentById,
        PathValues.EMPLOYEE_TIMESHEET__GET_TIMESHEET_DETAIL: EmployeeTimesheetGetTimesheetDetail,
        PathValues.EMPLOYEE_TIMESHEET__CREATE_NEW_TIMESHEET: EmployeeTimesheetCreateNewTimesheet,
        PathValues.EMPLOYEE_TIMESHEET__UPDATE_TIMESHEET: EmployeeTimesheetUpdateTimesheet,
        PathValues.EMPLOYEE_TIMESHEET__DELETE_TIMESHEET: EmployeeTimesheetDeleteTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_PROJECT_TIMESHEET_DETAIL: EmployeeProjectTimesheetGetProjectTimesheetDetail,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_PROJECT_TIMESHEET_BY_TRANSACTION_ID: EmployeeProjectTimesheetGetProjectTimesheetByTransactionId,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__CREATE_PROJECT_TIMESHEET: EmployeeProjectTimesheetCreateProjectTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__UPDATE_PROJECT_TIMESHEET: EmployeeProjectTimesheetUpdateProjectTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__DELETE_PROJECT_TIMESHEET: EmployeeProjectTimesheetDeleteProjectTimesheet,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_ALL_TIMESHEET_PROJECT: EmployeeProjectTimesheetGetAllTimesheetProject,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__ADD_NEW_PROJECT: EmployeeProjectTimesheetAddNewProject,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__EDIT_PROJECT: EmployeeProjectTimesheetEditProject,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_ALL_PROJECT_TASK: EmployeeProjectTimesheetGetAllProjectTask,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__ADD_NEW_PROJECT_TASK: EmployeeProjectTimesheetAddNewProjectTask,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__EDIT_PROJECT_TASK: EmployeeProjectTimesheetEditProjectTask,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__GET_ALL_PROJECT_TASK_DETAIL: EmployeeProjectTimesheetGetAllProjectTaskDetail,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__ADD_NEW_PROJECT_TASK_DETAIL: EmployeeProjectTimesheetAddNewProjectTaskDetail,
        PathValues.EMPLOYEE_PROJECT_TIMESHEET__EDIT_PROJECT_TASK_DETAIL: EmployeeProjectTimesheetEditProjectTaskDetail,
        PathValues.EMPLOYEE_APPRAISAL__GET_BY_EMPLOYEE_ID: EmployeeAppraisalGetByEmployeeId,
        PathValues.EMPLOYEE_APPRAISAL__GET_BY_APPRAISAL_ID: EmployeeAppraisalGetByAppraisalId,
        PathValues.EMPLOYEE_APPRAISAL__ADD_NEW_APPRAISAL: EmployeeAppraisalAddNewAppraisal,
        PathValues.EMPLOYEE_APPRAISAL__UPDATE_APPRAISAL: EmployeeAppraisalUpdateAppraisal,
        PathValues.EMPLOYEE_APPRAISAL__DELETE_APPRAISAL: EmployeeAppraisalDeleteAppraisal,
        PathValues.EMPLOYEE_BENEFIT__GET_BENEFIT_BY_EMPLOYEE_ID: EmployeeBenefitGetBenefitByEmployeeId,
        PathValues.EMPLOYEE_BENEFIT__GET_BENEFIT_BY_BENEFIT_ID: EmployeeBenefitGetBenefitByBenefitId,
        PathValues.EMPLOYEE_BENEFIT__ADD_NEW_BENEFIT: EmployeeBenefitAddNewBenefit,
        PathValues.EMPLOYEE_BENEFIT__UPDATE_BENEFIT: EmployeeBenefitUpdateBenefit,
        PathValues.EMPLOYEE_BENEFIT__DELETE_BENEFIT: EmployeeBenefitDeleteBenefit,
        PathValues.EMPLOYEE_CPD__GET_CPDBY_EMPLOYEE_ID: EmployeeCPDGetCPDByEmployeeId,
        PathValues.EMPLOYEE_CPD__GET_BY_CPDID: EmployeeCPDGetByCPDId,
        PathValues.EMPLOYEE_CPD__ADD_NEW_CPD: EmployeeCPDAddNewCPD,
        PathValues.EMPLOYEE_CPD__UPDATE_CPD: EmployeeCPDUpdateCPD,
        PathValues.EMPLOYEE_CPD__DELETE_CPD: EmployeeCPDDeleteCPD,
        PathValues.EMPLOYEE_DRIVING__GET_DRIVING_LICENSE_BY_EMPLOYEE_ID: EmployeeDrivingGetDrivingLicenseByEmployeeId,
        PathValues.EMPLOYEE_DRIVING__GET_DRIVING_LICENSE_BY_DRIVING_ID: EmployeeDrivingGetDrivingLicenseByDrivingId,
        PathValues.EMPLOYEE_DRIVING__ADD_NEW_DRIVING_LICENSE: EmployeeDrivingAddNewDrivingLicense,
        PathValues.EMPLOYEE_DRIVING__UPDATE_DRIVING_LICENSE: EmployeeDrivingUpdateDrivingLicense,
        PathValues.EMPLOYEE_DRIVING__DELETE_DRIVING_LICENSE: EmployeeDrivingDeleteDrivingLicense,
        PathValues.EMPLOYEE_QUALIFICATION__GET_QUALIFICATION_BY_EMPLOYEE_ID: EmployeeQualificationGetQualificationByEmployeeId,
        PathValues.EMPLOYEE_QUALIFICATION__GET_QUALIFICATION_BY_QUALIFICATION_ID: EmployeeQualificationGetQualificationByQualificationId,
        PathValues.EMPLOYEE_QUALIFICATION__ADD_NEW_QUALIFICATION: EmployeeQualificationAddNewQualification,
        PathValues.EMPLOYEE_QUALIFICATION__UPDATE_QUALIFICATION: EmployeeQualificationUpdateQualification,
        PathValues.EMPLOYEE_QUALIFICATION__DELETE_QUALIFICATION: EmployeeQualificationDeleteQualification,
        PathValues.EMPLOYEE_TRAINING__GET_TRAINING_DETAIL: EmployeeTrainingGetTrainingDetail,
        PathValues.EMPLOYEE_TRAINING__ADDTRAININGDETAIL: EmployeeTrainingAddtrainingdetail,
        PathValues.EMPLOYEE_TRAINING__UPDATETRAININGDETAIL: EmployeeTrainingUpdatetrainingdetail,
        PathValues.EMPLOYEE_TRAINING__DELETETRAININGDETAIL: EmployeeTrainingDeletetrainingdetail,
        PathValues.EMPLOYEE_VEHICLE__ADD_NEW_VEHICLE_DETAIL: EmployeeVehicleAddNewVehicleDetail,
        PathValues.EMPLOYEE_VEHICLE__UPDATE_VEHICLE_DETAIL: EmployeeVehicleUpdateVehicleDetail,
        PathValues.EMPLOYEE_VEHICLE__DELETE_VEHICLE_DETAIL: EmployeeVehicleDeleteVehicleDetail,
        PathValues.EMPLOYEE_VEHICLE__GET_BY_VEHICLE_DETAIL_ID: EmployeeVehicleGetByVehicleDetailId,
        PathValues.EMPLOYEE_VEHICLE__GET_VEHICLE_BY_EMPLOYEE_ID: EmployeeVehicleGetVehicleByEmployeeId,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__GET_CUSTOM_SCREEN_DETAIL: EmployeeCustomScreenGetCustomScreenDetail,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__GET_CUSTOM_SCREEN_BY_EMPLOYEE_ID: EmployeeCustomScreenGetCustomScreenByEmployeeId,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__GET_BY_CUSTOM_SCREEN_TRANSACTION_ID: EmployeeCustomScreenGetByCustomScreenTransactionId,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__ADD_NEW_CUSTOM_SCREEN_TRANSACTION: EmployeeCustomScreenAddNewCustomScreenTransaction,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__UPDATE_CUSTOM_SCREEN_TRANSACTION: EmployeeCustomScreenUpdateCustomScreenTransaction,
        PathValues.EMPLOYEE_CUSTOM_SCREEN__DELETE_CUSTOM_SCREEN_TRANSACTION: EmployeeCustomScreenDeleteCustomScreenTransaction,
        PathValues.HOLIDAY_ENTITLEMENT__GET_HOLIDAY_ENTITLEMENT: HolidayEntitlementGetHolidayEntitlement,
        PathValues.HOLIDAY_ENTITLEMENT__GET_NEXT_YEAR_HOLIDAY_ENTITLEMENT: HolidayEntitlementGetNextYearHolidayEntitlement,
        PathValues.HOLIDAY_ENTITLEMENT__UPDATE_HOLIDAY_ENTITLEMENT: HolidayEntitlementUpdateHolidayEntitlement,
        PathValues.HOLIDAY_ENTITLEMENT__UPDATE_NEXT_YEAR_HOLIDAY_ENTITLEMENT: HolidayEntitlementUpdateNextYearHolidayEntitlement,
        PathValues.HISTORY__GET_HISTORY_BY_EMPLOYEE_ID_AND_FIELD_NAME: HistoryGetHistoryByEmployeeIdAndFieldName,
        PathValues.QUERY__GET_QUERY_RESULT: QueryGetQueryResult,
        PathValues.QUERY__GET_QUERY_RESULT_BY_QUERY_NAME: QueryGetQueryResultByQueryName,
        PathValues.EMAIL_TRANSACTION__EMAIL_INBOX: EmailTransactionEmailInbox,
        PathValues.RIGHT_TO_WORK__ADDRIGHTTOWORKDETAIL: RightToWorkAddrighttoworkdetail,
        PathValues.RIGHT_TO_WORK__GETRIGHTTOWORKDETAIL: RightToWorkGetrighttoworkdetail,
        PathValues.RIGHT_TO_WORK__UPDATERIGHTTOWORKDETAIL: RightToWorkUpdaterighttoworkdetail,
        PathValues.RIGHT_TO_WORK__DELETERIGHTTOWORKDETAIL: RightToWorkDeleterighttoworkdetail,
        PathValues.BACKGROUND_CHECK__GET_BACKGROUND_CHECK_DETAIL_BY_EMPLOYEE_ID: BackgroundCheckGetBackgroundCheckDetailByEmployeeId,
        PathValues.BACKGROUND_CHECK__ADD_BACKGROUND_CHECK_DETAIL: BackgroundCheckAddBackgroundCheckDetail,
        PathValues.BACKGROUND_CHECK__UPDATE_BACKGROUND_CHECK_DETAIL: BackgroundCheckUpdateBackgroundCheckDetail,
        PathValues.BACKGROUND_CHECK__DELETE_BACKGROUND_CHECK_DETAIL: BackgroundCheckDeleteBackgroundCheckDetail,
        PathValues.OTHER_EVENT__GETOTHEREVENTDETAIL: OtherEventGetothereventdetail,
        PathValues.OTHER_EVENT__GETOTHEREVENTENTITLEMENT: OtherEventGetotherevententitlement,
        PathValues.OTHER_EVENT__DELETE_OTHER_EVENT: OtherEventDeleteOtherEvent,
        PathValues.OTHER_EVENT__ADDOTHEREVENTLEAVE: OtherEventAddothereventleave,
        PathValues.OTHER_EVENT__UPDATEOTHEREVENTLEAVE: OtherEventUpdateothereventleave,
        PathValues.OTHER_EVENT__ADDOTHEREVENTENTITLEMENT: OtherEventAddotherevententitlement,
        PathValues.VACANCY__CREATE_NEW_VACANCY: VacancyCreateNewVacancy,
        PathValues.VACANCY__GET_VACANCY: VacancyGetVacancy,
        PathValues.VACANCY__GET_ALL_VACANCIES: VacancyGetAllVacancies,
        PathValues.APPLICANT__CREATE_NEW_APPLICANT: ApplicantCreateNewApplicant,
        PathValues.APPLICANT__UPLOADAPPLICANTDOCUMENT: ApplicantUploadapplicantdocument,
        PathValues.APPLICANT__CHECK_DUPLICATE_APPLICANT: ApplicantCheckDuplicateApplicant,
        PathValues.WORK_PATTERN__GET_WORK_PATTERN_DETAIL: WorkPatternGetWorkPatternDetail,
        PathValues.EMPLOYEEE_LATE__GET_LATE_BY_EMPLOYEE_ID: EmployeeeLateGetLateByEmployeeId,
        PathValues.EMPLOYEEE_LATE__ADD_NEW_LATE: EmployeeeLateAddNewLate,
        PathValues.EMPLOYEEE_LATE__UPDATE_LATE: EmployeeeLateUpdateLate,
        PathValues.EMPLOYEEE_LATE__DELETE_LATE: EmployeeeLateDeleteLate,
        PathValues.MATERNITY_PATERNITY__GET_BY_MATERNITY_PATERNITY_ID: MaternityPaternityGetByMaternityPaternityId,
        PathValues.MATERNITY_PATERNITY__GET_MATERNITY_PATERNITY_BY_EMPLOYEE_ID: MaternityPaternityGetMaternityPaternityByEmployeeId,
        PathValues.MATERNITY_PATERNITY__ADD_NEW_MATERNITY_PATERNITY: MaternityPaternityAddNewMaternityPaternity,
        PathValues.MATERNITY_PATERNITY__UPDATE_MATERNITY_PATERNITY: MaternityPaternityUpdateMaternityPaternity,
        PathValues.MATERNITY_PATERNITY__DELETE_MATERNITY_PATERNITY: MaternityPaternityDeleteMaternityPaternity,
    }
)
