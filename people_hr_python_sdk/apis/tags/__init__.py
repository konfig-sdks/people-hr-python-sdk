# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from people_hr_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EMPLOYEE_PROJECT_TIMESHEET = "Employee Project Timesheet"
    EMPLOYEE = "Employee"
    EMPLOYEE_CUSTOM_SCREEN = "Employee Custom Screen"
    OTHER_EVENT = "Other Event"
    EMPLOYEE_APPRAISAL = "Employee Appraisal"
    EMPLOYEE_BENEFIT = "Employee Benefit"
    EMPLOYEE_CPD = "Employee CPD"
    EMPLOYEE_DRIVING = "Employee Driving"
    EMPLOYEE_QUALIFICATION = "Employee Qualification"
    EMPLOYEE_VEHICLE = "Employee Vehicle"
    MATERNITY_PATERNITY_ = "Maternity Paternity "
    EMPLOYEE_HOLIDAY = "Employee Holiday"
    EMPLOYEE_ABSENCE = "Employee Absence"
    EMPLOYEE_TIMESHEET = "Employee Timesheet"
    EMPLOYEE_TRAINING = "Employee Training"
    HOLIDAY_ENTITLEMENT = "Holiday Entitlement"
    RIGHT_TO_WORK = "Right To Work"
    BACKGROUND_CHECK = "Background Check"
    EMPLOYEEE_LATE = "Employeee Late"
    EMPLOYEE_SALARY = "Employee Salary"
    EMPLOYEE_DOCUMENT = "Employee Document"
    VACANCY = "Vacancy"
    APPLICANT = "Applicant"
    QUERY = "Query"
    HISTORY = "History"
    EMAIL_TRANSACTION = "Email Transaction"
    WORK_PATTERN = "WorkPattern"
