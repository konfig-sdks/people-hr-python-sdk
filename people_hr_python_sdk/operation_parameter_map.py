operation_parameter_map = {
    '/Applicant  -  CheckDuplicateApplicant-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'VacancyReference'
            },
            {
                'name': 'Email'
            },
        ]
    },
    '/Applicant  -  CreateNewApplicant-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'Documents'
            },
            {
                'name': 'Skills'
            },
            {
                'name': 'VacancyReference'
            },
            {
                'name': 'Email'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'DateOfBirth'
            },
            {
                'name': 'PostCode'
            },
            {
                'name': 'Address'
            },
            {
                'name': 'PhoneNumber'
            },
            {
                'name': 'OtherContactDetails'
            },
            {
                'name': 'Source'
            },
            {
                'name': 'AdditionalQuestions'
            },
            {
                'name': 'InternalQuestions'
            },
            {
                'name': 'RecruitmentCost'
            },
            {
                'name': 'DateLastContacted'
            },
        ]
    },
    '/Applicant  -  uploadapplicantdocument-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ApplicantId'
            },
            {
                'name': 'DocumentName'
            },
            {
                'name': 'File'
            },
            {
                'name': 'Description'
            },
        ]
    },
    '/Background Check  -  AddBackgroundCheckDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TypeOfCheck'
            },
            {
                'name': 'DocumentName'
            },
            {
                'name': 'File'
            },
            {
                'name': 'DateCompleted'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Background Check  -  DeleteBackgroundCheckDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'BackgroundCheckTxnId'
            },
        ]
    },
    '/Background Check  -  GetBackgroundCheckDetailByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Background Check  -  UpdateBackgroundCheckDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'BackgroundCheckTxnId'
            },
            {
                'name': 'TypeOfCheck'
            },
            {
                'name': 'DocumentName'
            },
            {
                'name': 'File'
            },
            {
                'name': 'DateCompleted'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Email Transaction  -  EmailInbox-POST': {
        'parameters': [
            {
                'name': 'Action'
            },
            {
                'name': 'EmailFrom'
            },
            {
                'name': 'EmailTo'
            },
            {
                'name': 'EmailSubject'
            },
            {
                'name': 'EmailCc'
            },
            {
                'name': 'EmailBcc'
            },
            {
                'name': 'Attachment'
            },
        ]
    },
    '/Employee  -  AddEmployeeImage-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'EmployeeImageName'
            },
            {
                'name': 'EmployeeImage'
            },
        ]
    },
    '/Employee  -  CreateNewEmployee-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'JobRole'
            },
            {
                'name': 'JobRoleEffectiveDate'
            },
            {
                'name': 'Location'
            },
            {
                'name': 'Department'
            },
            {
                'name': 'Title'
            },
            {
                'name': 'Email'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'DateOfBirth'
            },
            {
                'name': 'ReportsTo'
            },
            {
                'name': 'Company'
            },
            {
                'name': 'NationalInsuranceNumber'
            },
            {
                'name': 'Nationality'
            },
            {
                'name': 'EmploymentType'
            },
            {
                'name': 'EntitlementThisYear'
            },
            {
                'name': 'EntitlementNextYear'
            },
            {
                'name': 'Address'
            },
            {
                'name': 'PersonalPhoneNumber'
            },
            {
                'name': 'Payroll Company'
            },
            {
                'name': 'Payroll ID'
            },
            {
                'name': 'Time & Attendance ID'
            },
            {
                'name': 'Rota ID'
            },
            {
                'name': 'CRM ID'
            },
            {
                'name': 'ATS ID'
            },
            {
                'name': 'Performance ID'
            },
            {
                'name': 'Benefits ID'
            },
            {
                'name': 'System1 ID'
            },
            {
                'name': 'System2 ID'
            },
            {
                'name': 'System3 ID'
            },
            {
                'name': 'APIColumn1'
            },
            {
                'name': 'APIColumn2'
            },
            {
                'name': 'APIColumn3'
            },
            {
                'name': 'APIColumn4'
            },
            {
                'name': 'APIColumn5'
            },
            {
                'name': 'PersonalEmail'
            },
            {
                'name': 'MethodOfRecruitment'
            },
        ]
    },
    '/Employee  -  CheckAuthentication-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmailAddress'
            },
            {
                'name': 'Password'
            },
        ]
    },
    '/Employee  -  GetEmployeeDetailById-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee  -  GetAllEmployeeDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'IncludeLeavers'
            },
        ]
    },
    '/Employee  -  UpdateEmployeeDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ReasonForChange'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'ReportsToEffectiveDate'
            },
            {
                'name': 'CompanyEffectiveDate'
            },
            {
                'name': 'JobRole'
            },
            {
                'name': 'JobRoleEffectiveDate'
            },
            {
                'name': 'Location'
            },
            {
                'name': 'LocationEffectiveDate'
            },
            {
                'name': 'Department'
            },
            {
                'name': 'DepartmentEffectiveDate'
            },
            {
                'name': 'EmploymentTypeEffectiveDate'
            },
            {
                'name': 'Title'
            },
            {
                'name': 'Email'
            },
            {
                'name': 'DateOfBirth'
            },
            {
                'name': 'ReportsTo'
            },
            {
                'name': 'Company'
            },
            {
                'name': 'NationalInsuranceNumber'
            },
            {
                'name': 'Nationality'
            },
            {
                'name': 'EmploymentType'
            },
            {
                'name': 'Address'
            },
            {
                'name': 'PersonalPhoneNumber'
            },
            {
                'name': 'Payroll Company'
            },
            {
                'name': 'Payroll ID'
            },
            {
                'name': 'Time & Attendance ID'
            },
            {
                'name': 'Rota ID'
            },
            {
                'name': 'CRM ID'
            },
            {
                'name': 'ATS ID'
            },
            {
                'name': 'Performance ID'
            },
            {
                'name': 'Benefits ID'
            },
            {
                'name': 'System1 ID'
            },
            {
                'name': 'System2 ID'
            },
            {
                'name': 'System3 ID'
            },
            {
                'name': 'APIColumn1'
            },
            {
                'name': 'APIColumn2'
            },
            {
                'name': 'APIColumn3'
            },
            {
                'name': 'APIColumn4'
            },
            {
                'name': 'APIColumn5'
            },
            {
                'name': 'PersonalEmail'
            },
            {
                'name': 'MethodOfRecruitment'
            },
        ]
    },
    '/Employee  -  UpdateEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ReasonForChange'
            },
            {
                'name': 'OldEmployeeId'
            },
            {
                'name': 'NewEmployeeId'
            },
        ]
    },
    '/Employee  -  MarkAsLeaverById-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ReasonforLeaving'
            },
            {
                'name': 'FinalEmploymentDate'
            },
            {
                'name': 'AdditionalComments'
            },
            {
                'name': 'FinalWorkingDate'
            },
            {
                'name': 'MarkasLeaverImmediately'
            },
            {
                'name': 'ReportsTo'
            },
            {
                'name': 'ReEmployable'
            },
            {
                'name': 'SupportingComments'
            },
        ]
    },
    '/EmployeeAbsence  -  AddAbsence-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DurationType'
            },
            {
                'name': 'Reason'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'PartOfDay'
            },
            {
                'name': 'Duration'
            },
            {
                'name': 'AbsencePaidStatus'
            },
            {
                'name': 'EmergencyLeave'
            },
            {
                'name': 'AddComments'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/EmployeeAbsence  -  GetAbsenceDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/EmployeeAbsence  -  DeleteAbsence-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/EmployeeAbsence  -  UpdateAbsence-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'OldStartDate'
            },
            {
                'name': 'OldEndDate'
            },
            {
                'name': 'DurationType'
            },
            {
                'name': 'Reason'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'Duration'
            },
            {
                'name': 'AbsencePaidStatus'
            },
            {
                'name': 'EmergencyLeave'
            },
            {
                'name': 'PartOfDay'
            },
            {
                'name': 'AddComments'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/EmployeeAppraisal  -  AddNewAppraisal-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'AppraisalReviewDate'
            },
            {
                'name': 'Reviewer'
            },
            {
                'name': 'Notes'
            },
            {
                'name': 'ActionPlan'
            },
            {
                'name': 'Objectives'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/EmployeeAppraisal  -  DeleteAppraisal-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'AppraisalId'
            },
        ]
    },
    '/EmployeeAppraisal  -  GetByAppraisalId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'AppraisalId'
            },
        ]
    },
    '/EmployeeAppraisal  -  GetByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/EmployeeAppraisal  -  UpdateAppraisal-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'AppraisalReviewDate'
            },
            {
                'name': 'Reviewer'
            },
            {
                'name': 'Notes'
            },
            {
                'name': 'ActionPlan'
            },
            {
                'name': 'Objectives'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/EmployeeBenefit  -  AddNewBenefit-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Benefit'
            },
            {
                'name': 'DateAwarded'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'RecoverOnTermination'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
            {
                'name': 'Value'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/EmployeeBenefit  -  DeleteBenefit-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'BenefitId'
            },
        ]
    },
    '/EmployeeBenefit  -  GetBenefitByBenefitId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'BenefitId'
            },
        ]
    },
    '/EmployeeBenefit  -  GetBenefitByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/EmployeeBenefit  -  UpdateBenefit-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Benefit'
            },
            {
                'name': 'BenefitId'
            },
            {
                'name': 'DateAwarded'
            },
            {
                'name': 'RecoverOnTermination'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Value'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee CPD  -  AddNewCPD-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Activity'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'RollNumber'
            },
            {
                'name': 'DateAdmitted'
            },
            {
                'name': 'HoursRequired'
            },
            {
                'name': 'HoursAccredited'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/Employee CPD  -  DeleteCPD-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'CPDId'
            },
        ]
    },
    '/Employee CPD  -  GetByCPDId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'CPDId'
            },
        ]
    },
    '/Employee CPD  -  GetCPDByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee CPD  -  UpdateCPD-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'CPDId'
            },
            {
                'name': 'Activity'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'RollNumber'
            },
            {
                'name': 'DateAdmitted'
            },
            {
                'name': 'HoursRequired'
            },
            {
                'name': 'HoursAccredited'
            },
            {
                'name': 'Notes'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Custom Screen  -  AddNewCustomScreenTransaction-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ScreenId'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Custom Screen  -  DeleteCustomScreenTransaction-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ScreenId'
            },
            {
                'name': 'CustomScreenTransactionId'
            },
        ]
    },
    '/Employee Custom Screen  -  GetByCustomScreenTransactionId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ScreenId'
            },
            {
                'name': 'CustomScreenTransactionId'
            },
        ]
    },
    '/Employee Custom Screen  -  GetCustomScreenDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
        ]
    },
    '/Employee Custom Screen  -  GetCustomScreenByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ScreenId'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee Custom Screen  -  UpdateCustomScreenTransaction-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ScreenId'
            },
            {
                'name': 'CustomScreenTransactionId'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/EmployeeDocument  -  GetAllDocument-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/EmployeeDocument  -  GetDocumentById-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DocumentId'
            },
        ]
    },
    '/EmployeeDocument  -  UploadEmployeeDocument-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Category'
            },
            {
                'name': 'EmployeeAccess'
            },
            {
                'name': 'ManagerAccess'
            },
            {
                'name': 'SignatureRequired'
            },
            {
                'name': 'DocumentName'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'File'
            },
        ]
    },
    '/Employee Driving  -  AddNewDrivingLicense-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'LicenseNumber'
            },
            {
                'name': 'LicenseType'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Driving  -  GetDrivingLicenseByDrivingId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DrivingId'
            },
        ]
    },
    '/Employee Driving  -  GetDrivingLicenseByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee Driving  -  DeleteDrivingLicense-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DrivingId'
            },
        ]
    },
    '/Employee Driving  -  UpdateDrivingLicense-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DrivingId'
            },
            {
                'name': 'LicenseNumber'
            },
            {
                'name': 'LicenseType'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Holiday  -  AddNewHoliday-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DurationType'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'DurationInDays'
            },
            {
                'name': 'DurationInMinutes'
            },
            {
                'name': 'PartOfDay'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Employee Holiday  -  GetHolidayDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Employee Holiday  -  DeleteHoliday-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Employee Holiday  -  UpdateHoliday-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'OldStartDate'
            },
            {
                'name': 'OldEndDate'
            },
            {
                'name': 'DurationType'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'DurationInDays'
            },
            {
                'name': 'DurationInMinutes'
            },
            {
                'name': 'PartOfDay'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Employee Project Timesheet  -  AddNewProjectTask-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectTaskName'
            },
            {
                'name': 'InUse'
            },
        ]
    },
    '/Employee Project Timesheet  -  AddNewProjectTaskDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectTaskDetailName'
            },
            {
                'name': 'InUse'
            },
        ]
    },
    '/Employee Project Timesheet  -  AddNewProject-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectName'
            },
            {
                'name': 'InUse'
            },
        ]
    },
    '/Employee Project Timesheet  -  CreateProjectTimesheet-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ProjectTimesheetDate'
            },
            {
                'name': 'TimesheetProject'
            },
            {
                'name': 'TimesheetTask'
            },
            {
                'name': 'TimesheetDetail'
            },
            {
                'name': 'StartTime'
            },
            {
                'name': 'EndTime'
            },
            {
                'name': 'TotalHours'
            },
            {
                'name': 'Quantity'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/Employee Project Timesheet  -  DeleteProjectTimesheet-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TransactionId'
            },
        ]
    },
    '/Employee Project Timesheet  -  EditProject-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectName'
            },
            {
                'name': 'NewProjectName'
            },
            {
                'name': 'InUse'
            },
        ]
    },
    '/Employee Project Timesheet  -  EditProjectTaskDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectTaskDetailName'
            },
            {
                'name': 'New_ProjectTaskDetailName'
            },
            {
                'name': 'InUse'
            },
        ]
    },
    '/Employee Project Timesheet  -  GetAllProjectTask-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectTaskName'
            },
        ]
    },
    '/Employee Project Timesheet  -  GetAllProjectTaskDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectTaskDetailName'
            },
        ]
    },
    '/Employee Project Timesheet  -  GetProjectTimesheetByTransactionId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TransactionId'
            },
        ]
    },
    '/Employee Project Timesheet  -  GetProjectTimesheetDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Employee Project Timesheet  -  GetAllTimesheetProject-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectName'
            },
        ]
    },
    '/Employee Project Timesheet  -  EditProjectTask-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'ProjectTaskName'
            },
            {
                'name': 'New_ProjectTaskName'
            },
            {
                'name': 'InUse'
            },
        ]
    },
    '/Employee Project Timesheet  -  UpdateProjectTimesheet-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TransactionId'
            },
            {
                'name': 'TimesheetProject'
            },
            {
                'name': 'TimesheetTask'
            },
            {
                'name': 'TimesheetDetail'
            },
            {
                'name': 'StartTime'
            },
            {
                'name': 'EndTime'
            },
            {
                'name': 'TotalHours'
            },
            {
                'name': 'Quantity'
            },
            {
                'name': 'Notes'
            },
        ]
    },
    '/Employee Qualification  -  AddNewQualification-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Qualification'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'DatePassed'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Qualification  -  DeleteQualification-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'QualificationId'
            },
        ]
    },
    '/Employee Qualification  -  GetQualificationByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee Qualification  -  GetQualificationByQualificationId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'QualificationId'
            },
        ]
    },
    '/Employee Qualification  -  UpdateQualification-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'QualificationId'
            },
            {
                'name': 'Qualification'
            },
            {
                'name': 'Subject'
            },
            {
                'name': 'DatePassed'
            },
            {
                'name': 'ExpiryDate'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/EmployeeSalary  -  CreateNewSalary-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'EffectiveFrom'
            },
            {
                'name': 'SalaryType'
            },
            {
                'name': 'PaymentFrequency'
            },
            {
                'name': 'SalaryAmount'
            },
            {
                'name': 'CurrencyCode'
            },
            {
                'name': 'ChangeReason'
            },
            {
                'name': 'Deductions'
            },
            {
                'name': 'Entitlements'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/EmployeeSalary  -  DeleteSalary-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'EffectiveFrom'
            },
        ]
    },
    '/EmployeeSalary  -  GetSalaryDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'IsIncludeHistory'
            },
        ]
    },
    '/Employee Timesheet  -  CreateNewTimesheet-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TimesheetDate'
            },
            {
                'name': 'TimeIn1'
            },
            {
                'name': 'TimeOut1'
            },
            {
                'name': 'TimeIn2'
            },
            {
                'name': 'TimeOut2'
            },
            {
                'name': 'TimeIn3'
            },
            {
                'name': 'TimeOut3'
            },
            {
                'name': 'TimeIn4'
            },
            {
                'name': 'TimeOut4'
            },
            {
                'name': 'TimeIn5'
            },
            {
                'name': 'TimeOut5'
            },
            {
                'name': 'TimeIn6'
            },
            {
                'name': 'TimeOut6'
            },
            {
                'name': 'TimeIn7'
            },
            {
                'name': 'TimeOut7'
            },
            {
                'name': 'TimeIn8'
            },
            {
                'name': 'TimeOut8'
            },
            {
                'name': 'TimeIn9'
            },
            {
                'name': 'TimeOut9'
            },
            {
                'name': 'TimeIn10'
            },
            {
                'name': 'TimeOut10'
            },
            {
                'name': 'TimeIn11'
            },
            {
                'name': 'TimeOut11'
            },
            {
                'name': 'TimeIn12'
            },
            {
                'name': 'TimeOut12'
            },
            {
                'name': 'TimeIn13'
            },
            {
                'name': 'TimeOut13'
            },
            {
                'name': 'TimeIn14'
            },
            {
                'name': 'TimeOut14'
            },
            {
                'name': 'TimeIn15'
            },
            {
                'name': 'TimeOut15'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Employee Timesheet  -  DeleteTimesheet-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TimesheetDate'
            },
        ]
    },
    '/Employee Timesheet  -  GetTimesheetDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Employee Timesheet  -  UpdateTimesheet-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TimesheetDate'
            },
            {
                'name': 'TimeIn1'
            },
            {
                'name': 'TimeOut1'
            },
            {
                'name': 'TimeIn2'
            },
            {
                'name': 'TimeOut2'
            },
            {
                'name': 'TimeIn3'
            },
            {
                'name': 'TimeOut3'
            },
            {
                'name': 'TimeIn4'
            },
            {
                'name': 'TimeOut4'
            },
            {
                'name': 'TimeIn5'
            },
            {
                'name': 'TimeOut5'
            },
            {
                'name': 'TimeIn6'
            },
            {
                'name': 'TimeOut6'
            },
            {
                'name': 'TimeIn7'
            },
            {
                'name': 'TimeOut7'
            },
            {
                'name': 'TimeIn8'
            },
            {
                'name': 'TimeOut8'
            },
            {
                'name': 'TimeIn9'
            },
            {
                'name': 'TimeOut9'
            },
            {
                'name': 'TimeIn10'
            },
            {
                'name': 'TimeOut10'
            },
            {
                'name': 'TimeIn11'
            },
            {
                'name': 'TimeOut11'
            },
            {
                'name': 'TimeIn12'
            },
            {
                'name': 'TimeOut12'
            },
            {
                'name': 'TimeIn13'
            },
            {
                'name': 'TimeOut13'
            },
            {
                'name': 'TimeIn14'
            },
            {
                'name': 'TimeOut14'
            },
            {
                'name': 'TimeIn15'
            },
            {
                'name': 'TimeOut15'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Employee Training  -  addtrainingdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TrainingType'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'Importance'
            },
            {
                'name': 'Status'
            },
            {
                'name': 'InProgress'
            },
            {
                'name': 'TrainingDate'
            },
            {
                'name': 'TrainindEndDate'
            },
            {
                'name': 'TrainingExpiryDate'
            },
            {
                'name': 'Cost'
            },
            {
                'name': 'Provider'
            },
            {
                'name': 'Notes'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Training  -  GetTrainingDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee Training  -  deletetrainingdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TrainingId'
            },
        ]
    },
    '/Employee Training  -  updatetrainingdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'TrainingType'
            },
            {
                'name': 'Description'
            },
            {
                'name': 'Importance'
            },
            {
                'name': 'Status'
            },
            {
                'name': 'InProgress'
            },
            {
                'name': 'TrainingDate'
            },
            {
                'name': 'TrainindEndDate'
            },
            {
                'name': 'TrainingExpiryDate'
            },
            {
                'name': 'Cost'
            },
            {
                'name': 'Provider'
            },
            {
                'name': 'Notes'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Vehicle  -  AddNewVehicleDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Registration'
            },
            {
                'name': 'Make'
            },
            {
                'name': 'Model'
            },
            {
                'name': 'Colour'
            },
            {
                'name': 'EngineSize'
            },
            {
                'name': 'FuelType'
            },
            {
                'name': 'InsuranceCompany'
            },
            {
                'name': 'PolicyNumber'
            },
            {
                'name': 'MOTExpiryDate'
            },
            {
                'name': 'InsuranceExpiryDate'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employee Vehicle  -  DeleteVehicleDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'VehicleId'
            },
        ]
    },
    '/Employee Vehicle  -  GetByVehicleDetailId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'VehicleId'
            },
        ]
    },
    '/Employee Vehicle  -  GetVehicleByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Employee Vehicle  -  UpdateVehicleDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Registration'
            },
            {
                'name': 'Make'
            },
            {
                'name': 'Model'
            },
            {
                'name': 'Colour'
            },
            {
                'name': 'EngineSize'
            },
            {
                'name': 'FuelType'
            },
            {
                'name': 'InsuranceCompany'
            },
            {
                'name': 'PolicyNumber'
            },
            {
                'name': 'MOTExpiryDate'
            },
            {
                'name': 'InsuranceExpiryDate'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'CustomColumns'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Employeee Late  -  AddNewLate-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'LateDate'
            },
            {
                'name': 'HowLate'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Employeee Late  -  DeleteLate-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'LateDate'
            },
        ]
    },
    '/Employeee Late  -  GetLateByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Employeee Late  -  UpdateLate-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'LateDate'
            },
            {
                'name': 'HowLate'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/History  -  GetHistoryByEmployeeIdAndFieldName-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'FieldName'
            },
        ]
    },
    '/Holiday Entitlement  -  GetHolidayEntitlement-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Holiday Entitlement  -  GetNextYearHolidayEntitlement-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Holiday Entitlement  -  UpdateHolidayEntitlement-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ReasonForChange'
            },
            {
                'name': 'EntitlementThisYear'
            },
        ]
    },
    '/Holiday Entitlement  -  UpdateNextYearHolidayEntitlement-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ReasonForChange'
            },
            {
                'name': 'EntitlementNextYear'
            },
        ]
    },
    '/Maternity Paternity  -  AddNewMaternityPaternity-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DueDate'
            },
            {
                'name': 'ActualStartDate'
            },
            {
                'name': 'ActualEndDate'
            },
            {
                'name': 'AddComments'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Maternity Paternity  -  DeleteMaternityPaternity-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'MaternityPaternityTxnId'
            },
        ]
    },
    '/Maternity Paternity  -  GetMaternityPaternityByEmployeeId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'ActualStartDate'
            },
            {
                'name': 'ActualEndDate'
            },
        ]
    },
    '/Maternity Paternity  -  GetByMaternityPaternityId-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'MaternityPaternityTxnId'
            },
        ]
    },
    '/Maternity Paternity  -  UpdateMaternityPaternity-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'MaternityPaternityTxnId'
            },
            {
                'name': 'DueDate'
            },
            {
                'name': 'ActualStartDate'
            },
            {
                'name': 'ActualEndDate'
            },
            {
                'name': 'AddComments'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Other Event  -  addothereventleave-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DurationType'
            },
            {
                'name': 'Other Event Reason'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'DurationInDays'
            },
            {
                'name': 'StartTime'
            },
            {
                'name': 'EndTime'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Other Event  -  DeleteOtherEvent-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'OtherLeaveTxnId'
            },
        ]
    },
    '/Other Event  -  getothereventdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/Other Event  -  getotherevententitlement-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Other Event  -  addotherevententitlement-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Other Event Reason'
            },
            {
                'name': 'Entitlement RecordedIn'
            },
            {
                'name': 'ThisYearEntitlement'
            },
            {
                'name': 'NextYearEntitlement'
            },
        ]
    },
    '/Other Event  -  updateothereventleave-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'OtherEventTxnId'
            },
            {
                'name': 'DurationType'
            },
            {
                'name': 'Other Event Reason'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'DurationInDays'
            },
            {
                'name': 'StartTime'
            },
            {
                'name': 'EndTime'
            },
            {
                'name': 'Comments'
            },
            {
                'name': 'AddFiles'
            },
        ]
    },
    '/Query  -  GetQueryResultByQueryName-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'QueryName'
            },
        ]
    },
    '/Query  -  GetQueryResult-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'QueryName'
            },
        ]
    },
    '/Right To Work  -  addrighttoworkdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'DocumentName'
            },
            {
                'name': 'File'
            },
            {
                'name': 'DocumentType'
            },
            {
                'name': 'DocumentId'
            },
            {
                'name': 'ValidFrom'
            },
            {
                'name': 'ValidTo'
            },
            {
                'name': 'Duration'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Right To Work  -  deleterighttoworkdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'RightToWorkTxnId'
            },
        ]
    },
    '/Right To Work  -  getrighttoworkdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
        ]
    },
    '/Right To Work  -  updaterighttoworkdetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'RightToWorkTxnId'
            },
            {
                'name': 'DocumentName'
            },
            {
                'name': 'File'
            },
            {
                'name': 'DocumentType'
            },
            {
                'name': 'DocumentId'
            },
            {
                'name': 'ValidFrom'
            },
            {
                'name': 'ValidTo'
            },
            {
                'name': 'Duration'
            },
            {
                'name': 'Comments'
            },
        ]
    },
    '/Vacancy  -  CreateNewVacancy-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'VacancyName'
            },
            {
                'name': 'VacancyDescription'
            },
            {
                'name': 'Reference'
            },
            {
                'name': 'IsCoverLetterMandatory'
            },
            {
                'name': 'IsResumeMandatory'
            },
            {
                'name': 'IsHideSalary'
            },
            {
                'name': 'VacancyType'
            },
            {
                'name': 'Company'
            },
            {
                'name': 'Location'
            },
            {
                'name': 'Department'
            },
            {
                'name': 'ClosingDate'
            },
            {
                'name': 'Comment'
            },
            {
                'name': 'SalaryRange'
            },
            {
                'name': 'JobDescription'
            },
            {
                'name': 'JobTitle'
            },
            {
                'name': 'City'
            },
            {
                'name': 'Country'
            },
            {
                'name': 'Experience'
            },
        ]
    },
    '/Vacancy  -  GetAllVacancies-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
        ]
    },
    '/Vacancy  -  GetVacancy-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'VacancyReference'
            },
        ]
    },
    '/WorkPattern  -  GetWorkPatternDetail-POST': {
        'parameters': [
            {
                'name': 'APIKey'
            },
            {
                'name': 'Action'
            },
            {
                'name': 'WorkPatternId'
            },
            {
                'name': 'WorkPatternName'
            },
        ]
    },
};