import typing_extensions

from 7_shifts_python_sdk.paths import PathValues
from 7_shifts_python_sdk.apis.paths.oauth2_token import Oauth2Token
from 7_shifts_python_sdk.apis.paths.v2_whoami import V2Whoami
from 7_shifts_python_sdk.apis.paths.v2_partner_company_creation import V2PartnerCompanyCreation
from 7_shifts_python_sdk.apis.paths.v2_companies import V2Companies
from 7_shifts_python_sdk.apis.paths.v2_companies_id import V2CompaniesId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_labor_settings import V2CompanyCompanyIdLaborSettings
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_inactive_reasons import V2CompanyCompanyIdInactiveReasons
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations import V2CompanyCompanyIdLocations
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations_location_id import V2CompanyCompanyIdLocationsLocationId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_departments import V2CompanyCompanyIdDepartments
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_departments_department_id import V2CompanyCompanyIdDepartmentsDepartmentId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_roles import V2CompanyCompanyIdRoles
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_roles_role_id import V2CompanyCompanyIdRolesRoleId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users import V2CompanyCompanyIdUsers
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_create_many_users import V2CompanyCompanyIdCreateManyUsers
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_identifier import V2CompanyCompanyIdUsersIdentifier
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_wages import V2CompanyCompanyIdUsersUserIdWages
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_assignments import V2CompanyCompanyIdUsersUserIdAssignments
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_location_assignments import V2CompanyCompanyIdUsersUserIdLocationAssignments
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_location_assignments_location_id import V2CompanyCompanyIdUsersUserIdLocationAssignmentsLocationId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_department_assignments import V2CompanyCompanyIdUsersUserIdDepartmentAssignments
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_department_assignments_department_id import V2CompanyCompanyIdUsersUserIdDepartmentAssignmentsDepartmentId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_role_assignments import V2CompanyCompanyIdUsersUserIdRoleAssignments
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_users_user_id_role_assignments_role_id import V2CompanyCompanyIdUsersUserIdRoleAssignmentsRoleId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_shifts import V2CompanyCompanyIdShifts
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_shifts_shift_id import V2CompanyCompanyIdShiftsShiftId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_shifts_scheduled_id import V2CompanyCompanyIdShiftsScheduledId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_time_punches import V2CompanyCompanyIdTimePunches
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_time_punches_time_punch_id import V2CompanyCompanyIdTimePunchesTimePunchId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_receipts import V2CompanyCompanyIdReceipts
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_receipts_receipt_id import V2CompanyCompanyIdReceiptsReceiptId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_receipts_summary import V2CompanyCompanyIdReceiptsSummary
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_external_user_mappings_identifier import V2CompanyCompanyIdExternalUserMappingsIdentifier
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_external_user_mappings import V2CompanyCompanyIdExternalUserMappings
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_external_user_mappings_bulk import V2CompanyCompanyIdExternalUserMappingsBulk
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_events import V2CompanyCompanyIdEvents
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_events_event_id import V2CompanyCompanyIdEventsEventId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_management_settings import V2CompanyCompanyIdTaskManagementSettings
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_tags import V2CompanyCompanyIdTaskTags
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_list_templates import V2CompanyCompanyIdTaskListTemplates
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_list_templates_uuid import V2CompanyCompanyIdTaskListTemplatesUuid
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_lists import V2CompanyCompanyIdTaskLists
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_lists_list_id import V2CompanyCompanyIdTaskListsListId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_lists_list_id_tasks_task_id_clear import V2CompanyCompanyIdTaskListsListIdTasksTaskIdClear
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_lists_list_id_tasks_task_id_complete import V2CompanyCompanyIdTaskListsListIdTasksTaskIdComplete
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_task_list_daily_summary import V2CompanyCompanyIdTaskListDailySummary
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_log_book_categories import V2CompanyCompanyIdLogBookCategories
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_log_book_categories_id import V2CompanyCompanyIdLogBookCategoriesId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_log_book_posts import V2CompanyCompanyIdLogBookPosts
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_log_book_posts_id import V2CompanyCompanyIdLogBookPostsId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_log_book_comments import V2CompanyCompanyIdLogBookComments
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_log_book_comments_id import V2CompanyCompanyIdLogBookCommentsId
from 7_shifts_python_sdk.apis.paths.v2_reports_hours_and_wages import V2ReportsHoursAndWages
from 7_shifts_python_sdk.apis.paths.v2_reports_daily_sales_and_labor import V2ReportsDailySalesAndLabor
from 7_shifts_python_sdk.apis.paths.api_v2_company_company_id_location_location_id_daily_stats import ApiV2CompanyCompanyIdLocationLocationIdDailyStats
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_location_location_id_forecast_override import V2CompanyCompanyIdLocationLocationIdForecastOverride
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_location_location_id_forecast_overrides import V2CompanyCompanyIdLocationLocationIdForecastOverrides
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations_location_id_forecast_override_interval import V2CompanyCompanyIdLocationsLocationIdForecastOverrideInterval
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations_location_id_forecast_overrides_intervals import V2CompanyCompanyIdLocationsLocationIdForecastOverridesIntervals
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_tip_pool_settings import V2CompanyCompanyIdTipPoolSettings
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_tip_pool_tip_pool_settings_uuid_manual_entry import V2CompanyCompanyIdTipPoolTipPoolSettingsUuidManualEntry
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations_location_id_tip_pool_summary_report import V2CompanyCompanyIdLocationsLocationIdTipPoolSummaryReport
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations_location_id_tip_pool_detailed_report import V2CompanyCompanyIdLocationsLocationIdTipPoolDetailedReport
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_day_part_settings import V2CompanyCompanyIdDayPartSettings
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_availabilities import V2CompanyCompanyIdAvailabilities
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_availabilities_availability_id import V2CompanyCompanyIdAvailabilitiesAvailabilityId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_availabilities_availability_id_status import V2CompanyCompanyIdAvailabilitiesAvailabilityIdStatus
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_availability_reasons import V2CompanyCompanyIdAvailabilityReasons
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_availability_reasons_availability_reason_id import V2CompanyCompanyIdAvailabilityReasonsAvailabilityReasonId
from 7_shifts_python_sdk.apis.paths.v2_time_off import V2TimeOff
from 7_shifts_python_sdk.apis.paths.v2_time_off_time_off_id import V2TimeOffTimeOffId
from 7_shifts_python_sdk.apis.paths.v2_time_off_time_off_id_approve import V2TimeOffTimeOffIdApprove
from 7_shifts_python_sdk.apis.paths.v2_time_off_time_off_id_decline import V2TimeOffTimeOffIdDecline
from 7_shifts_python_sdk.apis.paths.v2_time_off_total_hours import V2TimeOffTotalHours
from 7_shifts_python_sdk.apis.paths.v2_time_off_settings_company_id import V2TimeOffSettingsCompanyId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_shift_feedback import V2CompanyCompanyIdShiftFeedback
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_locations_location_id_engage_overview import V2CompanyCompanyIdLocationsLocationIdEngageOverview
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_webhooks import V2CompanyCompanyIdWebhooks
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_webhooks_webhook_id import V2CompanyCompanyIdWebhooksWebhookId
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_test_webhook import V2CompanyCompanyIdTestWebhook
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_location_location_id_sales_category_mappings import V2CompanyCompanyIdLocationLocationIdSalesCategoryMappings
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_location_location_id_sales_category_mappings_bulk import V2CompanyCompanyIdLocationLocationIdSalesCategoryMappingsBulk
from 7_shifts_python_sdk.apis.paths.v2_company_company_id_location_location_id_sales_category_mappings_external_id import V2CompanyCompanyIdLocationLocationIdSalesCategoryMappingsExternalId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.V2_WHOAMI: V2Whoami,
        PathValues.V2_PARTNER_COMPANY_CREATION: V2PartnerCompanyCreation,
        PathValues.V2_COMPANIES: V2Companies,
        PathValues.V2_COMPANIES_ID: V2CompaniesId,
        PathValues.V2_COMPANY_COMPANY_ID_LABOR_SETTINGS: V2CompanyCompanyIdLaborSettings,
        PathValues.V2_COMPANY_COMPANY_ID_INACTIVE_REASONS: V2CompanyCompanyIdInactiveReasons,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS: V2CompanyCompanyIdLocations,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID: V2CompanyCompanyIdLocationsLocationId,
        PathValues.V2_COMPANY_COMPANY_ID_DEPARTMENTS: V2CompanyCompanyIdDepartments,
        PathValues.V2_COMPANY_COMPANY_ID_DEPARTMENTS_DEPARTMENT_ID: V2CompanyCompanyIdDepartmentsDepartmentId,
        PathValues.V2_COMPANY_COMPANY_ID_ROLES: V2CompanyCompanyIdRoles,
        PathValues.V2_COMPANY_COMPANY_ID_ROLES_ROLE_ID: V2CompanyCompanyIdRolesRoleId,
        PathValues.V2_COMPANY_COMPANY_ID_USERS: V2CompanyCompanyIdUsers,
        PathValues.V2_COMPANY_COMPANY_ID_CREATE_MANY_USERS: V2CompanyCompanyIdCreateManyUsers,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_IDENTIFIER: V2CompanyCompanyIdUsersIdentifier,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_WAGES: V2CompanyCompanyIdUsersUserIdWages,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_LOCATION_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdLocationAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_LOCATION_ASSIGNMENTS_LOCATION_ID: V2CompanyCompanyIdUsersUserIdLocationAssignmentsLocationId,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_DEPARTMENT_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdDepartmentAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_DEPARTMENT_ASSIGNMENTS_DEPARTMENT_ID: V2CompanyCompanyIdUsersUserIdDepartmentAssignmentsDepartmentId,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_ROLE_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdRoleAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_ROLE_ASSIGNMENTS_ROLE_ID: V2CompanyCompanyIdUsersUserIdRoleAssignmentsRoleId,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFTS: V2CompanyCompanyIdShifts,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFTS_SHIFT_ID: V2CompanyCompanyIdShiftsShiftId,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFTS_SCHEDULED_ID: V2CompanyCompanyIdShiftsScheduledId,
        PathValues.V2_COMPANY_COMPANY_ID_TIME_PUNCHES: V2CompanyCompanyIdTimePunches,
        PathValues.V2_COMPANY_COMPANY_ID_TIME_PUNCHES_TIME_PUNCH_ID: V2CompanyCompanyIdTimePunchesTimePunchId,
        PathValues.V2_COMPANY_COMPANY_ID_RECEIPTS: V2CompanyCompanyIdReceipts,
        PathValues.V2_COMPANY_COMPANY_ID_RECEIPTS_RECEIPT_ID: V2CompanyCompanyIdReceiptsReceiptId,
        PathValues.V2_COMPANY_COMPANY_ID_RECEIPTS_SUMMARY: V2CompanyCompanyIdReceiptsSummary,
        PathValues.V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS_IDENTIFIER: V2CompanyCompanyIdExternalUserMappingsIdentifier,
        PathValues.V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS: V2CompanyCompanyIdExternalUserMappings,
        PathValues.V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS_BULK: V2CompanyCompanyIdExternalUserMappingsBulk,
        PathValues.V2_COMPANY_COMPANY_ID_EVENTS: V2CompanyCompanyIdEvents,
        PathValues.V2_COMPANY_COMPANY_ID_EVENTS_EVENT_ID: V2CompanyCompanyIdEventsEventId,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_MANAGEMENT_SETTINGS: V2CompanyCompanyIdTaskManagementSettings,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_TAGS: V2CompanyCompanyIdTaskTags,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LIST_TEMPLATES: V2CompanyCompanyIdTaskListTemplates,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LIST_TEMPLATES_UUID: V2CompanyCompanyIdTaskListTemplatesUuid,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS: V2CompanyCompanyIdTaskLists,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID: V2CompanyCompanyIdTaskListsListId,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID_TASKS_TASK_ID_CLEAR: V2CompanyCompanyIdTaskListsListIdTasksTaskIdClear,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID_TASKS_TASK_ID_COMPLETE: V2CompanyCompanyIdTaskListsListIdTasksTaskIdComplete,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LIST_DAILY_SUMMARY: V2CompanyCompanyIdTaskListDailySummary,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_CATEGORIES: V2CompanyCompanyIdLogBookCategories,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_CATEGORIES_ID: V2CompanyCompanyIdLogBookCategoriesId,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_POSTS: V2CompanyCompanyIdLogBookPosts,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_POSTS_ID: V2CompanyCompanyIdLogBookPostsId,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_COMMENTS: V2CompanyCompanyIdLogBookComments,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_COMMENTS_ID: V2CompanyCompanyIdLogBookCommentsId,
        PathValues.V2_REPORTS_HOURS_AND_WAGES: V2ReportsHoursAndWages,
        PathValues.V2_REPORTS_DAILY_SALES_AND_LABOR: V2ReportsDailySalesAndLabor,
        PathValues.API_V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_DAILY_STATS: ApiV2CompanyCompanyIdLocationLocationIdDailyStats,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_FORECAST_OVERRIDE: V2CompanyCompanyIdLocationLocationIdForecastOverride,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_FORECAST_OVERRIDES: V2CompanyCompanyIdLocationLocationIdForecastOverrides,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_FORECAST_OVERRIDE_INTERVAL: V2CompanyCompanyIdLocationsLocationIdForecastOverrideInterval,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_FORECAST_OVERRIDES_INTERVALS: V2CompanyCompanyIdLocationsLocationIdForecastOverridesIntervals,
        PathValues.V2_COMPANY_COMPANY_ID_TIP_POOL_SETTINGS: V2CompanyCompanyIdTipPoolSettings,
        PathValues.V2_COMPANY_COMPANY_ID_TIP_POOL_TIP_POOL_SETTINGS_UUID_MANUAL_ENTRY: V2CompanyCompanyIdTipPoolTipPoolSettingsUuidManualEntry,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_TIP_POOL_SUMMARY_REPORT: V2CompanyCompanyIdLocationsLocationIdTipPoolSummaryReport,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_TIP_POOL_DETAILED_REPORT: V2CompanyCompanyIdLocationsLocationIdTipPoolDetailedReport,
        PathValues.V2_COMPANY_COMPANY_ID_DAY_PART_SETTINGS: V2CompanyCompanyIdDayPartSettings,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITIES: V2CompanyCompanyIdAvailabilities,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITIES_AVAILABILITY_ID: V2CompanyCompanyIdAvailabilitiesAvailabilityId,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITIES_AVAILABILITY_ID_STATUS: V2CompanyCompanyIdAvailabilitiesAvailabilityIdStatus,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITY_REASONS: V2CompanyCompanyIdAvailabilityReasons,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITY_REASONS_AVAILABILITY_REASON_ID: V2CompanyCompanyIdAvailabilityReasonsAvailabilityReasonId,
        PathValues.V2_TIME_OFF: V2TimeOff,
        PathValues.V2_TIME_OFF_TIME_OFF_ID: V2TimeOffTimeOffId,
        PathValues.V2_TIME_OFF_TIME_OFF_ID_APPROVE: V2TimeOffTimeOffIdApprove,
        PathValues.V2_TIME_OFF_TIME_OFF_ID_DECLINE: V2TimeOffTimeOffIdDecline,
        PathValues.V2_TIME_OFF_TOTAL_HOURS: V2TimeOffTotalHours,
        PathValues.V2_TIME_OFF_SETTINGS_COMPANY_ID: V2TimeOffSettingsCompanyId,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFT_FEEDBACK: V2CompanyCompanyIdShiftFeedback,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_ENGAGE_OVERVIEW: V2CompanyCompanyIdLocationsLocationIdEngageOverview,
        PathValues.V2_COMPANY_COMPANY_ID_WEBHOOKS: V2CompanyCompanyIdWebhooks,
        PathValues.V2_COMPANY_COMPANY_ID_WEBHOOKS_WEBHOOK_ID: V2CompanyCompanyIdWebhooksWebhookId,
        PathValues.V2_COMPANY_COMPANY_ID_TEST_WEBHOOK: V2CompanyCompanyIdTestWebhook,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS: V2CompanyCompanyIdLocationLocationIdSalesCategoryMappings,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS_BULK: V2CompanyCompanyIdLocationLocationIdSalesCategoryMappingsBulk,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS_EXTERNAL_ID: V2CompanyCompanyIdLocationLocationIdSalesCategoryMappingsExternalId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.V2_WHOAMI: V2Whoami,
        PathValues.V2_PARTNER_COMPANY_CREATION: V2PartnerCompanyCreation,
        PathValues.V2_COMPANIES: V2Companies,
        PathValues.V2_COMPANIES_ID: V2CompaniesId,
        PathValues.V2_COMPANY_COMPANY_ID_LABOR_SETTINGS: V2CompanyCompanyIdLaborSettings,
        PathValues.V2_COMPANY_COMPANY_ID_INACTIVE_REASONS: V2CompanyCompanyIdInactiveReasons,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS: V2CompanyCompanyIdLocations,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID: V2CompanyCompanyIdLocationsLocationId,
        PathValues.V2_COMPANY_COMPANY_ID_DEPARTMENTS: V2CompanyCompanyIdDepartments,
        PathValues.V2_COMPANY_COMPANY_ID_DEPARTMENTS_DEPARTMENT_ID: V2CompanyCompanyIdDepartmentsDepartmentId,
        PathValues.V2_COMPANY_COMPANY_ID_ROLES: V2CompanyCompanyIdRoles,
        PathValues.V2_COMPANY_COMPANY_ID_ROLES_ROLE_ID: V2CompanyCompanyIdRolesRoleId,
        PathValues.V2_COMPANY_COMPANY_ID_USERS: V2CompanyCompanyIdUsers,
        PathValues.V2_COMPANY_COMPANY_ID_CREATE_MANY_USERS: V2CompanyCompanyIdCreateManyUsers,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_IDENTIFIER: V2CompanyCompanyIdUsersIdentifier,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_WAGES: V2CompanyCompanyIdUsersUserIdWages,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_LOCATION_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdLocationAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_LOCATION_ASSIGNMENTS_LOCATION_ID: V2CompanyCompanyIdUsersUserIdLocationAssignmentsLocationId,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_DEPARTMENT_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdDepartmentAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_DEPARTMENT_ASSIGNMENTS_DEPARTMENT_ID: V2CompanyCompanyIdUsersUserIdDepartmentAssignmentsDepartmentId,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_ROLE_ASSIGNMENTS: V2CompanyCompanyIdUsersUserIdRoleAssignments,
        PathValues.V2_COMPANY_COMPANY_ID_USERS_USER_ID_ROLE_ASSIGNMENTS_ROLE_ID: V2CompanyCompanyIdUsersUserIdRoleAssignmentsRoleId,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFTS: V2CompanyCompanyIdShifts,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFTS_SHIFT_ID: V2CompanyCompanyIdShiftsShiftId,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFTS_SCHEDULED_ID: V2CompanyCompanyIdShiftsScheduledId,
        PathValues.V2_COMPANY_COMPANY_ID_TIME_PUNCHES: V2CompanyCompanyIdTimePunches,
        PathValues.V2_COMPANY_COMPANY_ID_TIME_PUNCHES_TIME_PUNCH_ID: V2CompanyCompanyIdTimePunchesTimePunchId,
        PathValues.V2_COMPANY_COMPANY_ID_RECEIPTS: V2CompanyCompanyIdReceipts,
        PathValues.V2_COMPANY_COMPANY_ID_RECEIPTS_RECEIPT_ID: V2CompanyCompanyIdReceiptsReceiptId,
        PathValues.V2_COMPANY_COMPANY_ID_RECEIPTS_SUMMARY: V2CompanyCompanyIdReceiptsSummary,
        PathValues.V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS_IDENTIFIER: V2CompanyCompanyIdExternalUserMappingsIdentifier,
        PathValues.V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS: V2CompanyCompanyIdExternalUserMappings,
        PathValues.V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS_BULK: V2CompanyCompanyIdExternalUserMappingsBulk,
        PathValues.V2_COMPANY_COMPANY_ID_EVENTS: V2CompanyCompanyIdEvents,
        PathValues.V2_COMPANY_COMPANY_ID_EVENTS_EVENT_ID: V2CompanyCompanyIdEventsEventId,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_MANAGEMENT_SETTINGS: V2CompanyCompanyIdTaskManagementSettings,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_TAGS: V2CompanyCompanyIdTaskTags,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LIST_TEMPLATES: V2CompanyCompanyIdTaskListTemplates,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LIST_TEMPLATES_UUID: V2CompanyCompanyIdTaskListTemplatesUuid,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS: V2CompanyCompanyIdTaskLists,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID: V2CompanyCompanyIdTaskListsListId,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID_TASKS_TASK_ID_CLEAR: V2CompanyCompanyIdTaskListsListIdTasksTaskIdClear,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID_TASKS_TASK_ID_COMPLETE: V2CompanyCompanyIdTaskListsListIdTasksTaskIdComplete,
        PathValues.V2_COMPANY_COMPANY_ID_TASK_LIST_DAILY_SUMMARY: V2CompanyCompanyIdTaskListDailySummary,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_CATEGORIES: V2CompanyCompanyIdLogBookCategories,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_CATEGORIES_ID: V2CompanyCompanyIdLogBookCategoriesId,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_POSTS: V2CompanyCompanyIdLogBookPosts,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_POSTS_ID: V2CompanyCompanyIdLogBookPostsId,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_COMMENTS: V2CompanyCompanyIdLogBookComments,
        PathValues.V2_COMPANY_COMPANY_ID_LOG_BOOK_COMMENTS_ID: V2CompanyCompanyIdLogBookCommentsId,
        PathValues.V2_REPORTS_HOURS_AND_WAGES: V2ReportsHoursAndWages,
        PathValues.V2_REPORTS_DAILY_SALES_AND_LABOR: V2ReportsDailySalesAndLabor,
        PathValues.API_V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_DAILY_STATS: ApiV2CompanyCompanyIdLocationLocationIdDailyStats,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_FORECAST_OVERRIDE: V2CompanyCompanyIdLocationLocationIdForecastOverride,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_FORECAST_OVERRIDES: V2CompanyCompanyIdLocationLocationIdForecastOverrides,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_FORECAST_OVERRIDE_INTERVAL: V2CompanyCompanyIdLocationsLocationIdForecastOverrideInterval,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_FORECAST_OVERRIDES_INTERVALS: V2CompanyCompanyIdLocationsLocationIdForecastOverridesIntervals,
        PathValues.V2_COMPANY_COMPANY_ID_TIP_POOL_SETTINGS: V2CompanyCompanyIdTipPoolSettings,
        PathValues.V2_COMPANY_COMPANY_ID_TIP_POOL_TIP_POOL_SETTINGS_UUID_MANUAL_ENTRY: V2CompanyCompanyIdTipPoolTipPoolSettingsUuidManualEntry,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_TIP_POOL_SUMMARY_REPORT: V2CompanyCompanyIdLocationsLocationIdTipPoolSummaryReport,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_TIP_POOL_DETAILED_REPORT: V2CompanyCompanyIdLocationsLocationIdTipPoolDetailedReport,
        PathValues.V2_COMPANY_COMPANY_ID_DAY_PART_SETTINGS: V2CompanyCompanyIdDayPartSettings,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITIES: V2CompanyCompanyIdAvailabilities,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITIES_AVAILABILITY_ID: V2CompanyCompanyIdAvailabilitiesAvailabilityId,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITIES_AVAILABILITY_ID_STATUS: V2CompanyCompanyIdAvailabilitiesAvailabilityIdStatus,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITY_REASONS: V2CompanyCompanyIdAvailabilityReasons,
        PathValues.V2_COMPANY_COMPANY_ID_AVAILABILITY_REASONS_AVAILABILITY_REASON_ID: V2CompanyCompanyIdAvailabilityReasonsAvailabilityReasonId,
        PathValues.V2_TIME_OFF: V2TimeOff,
        PathValues.V2_TIME_OFF_TIME_OFF_ID: V2TimeOffTimeOffId,
        PathValues.V2_TIME_OFF_TIME_OFF_ID_APPROVE: V2TimeOffTimeOffIdApprove,
        PathValues.V2_TIME_OFF_TIME_OFF_ID_DECLINE: V2TimeOffTimeOffIdDecline,
        PathValues.V2_TIME_OFF_TOTAL_HOURS: V2TimeOffTotalHours,
        PathValues.V2_TIME_OFF_SETTINGS_COMPANY_ID: V2TimeOffSettingsCompanyId,
        PathValues.V2_COMPANY_COMPANY_ID_SHIFT_FEEDBACK: V2CompanyCompanyIdShiftFeedback,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_ENGAGE_OVERVIEW: V2CompanyCompanyIdLocationsLocationIdEngageOverview,
        PathValues.V2_COMPANY_COMPANY_ID_WEBHOOKS: V2CompanyCompanyIdWebhooks,
        PathValues.V2_COMPANY_COMPANY_ID_WEBHOOKS_WEBHOOK_ID: V2CompanyCompanyIdWebhooksWebhookId,
        PathValues.V2_COMPANY_COMPANY_ID_TEST_WEBHOOK: V2CompanyCompanyIdTestWebhook,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS: V2CompanyCompanyIdLocationLocationIdSalesCategoryMappings,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS_BULK: V2CompanyCompanyIdLocationLocationIdSalesCategoryMappingsBulk,
        PathValues.V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS_EXTERNAL_ID: V2CompanyCompanyIdLocationLocationIdSalesCategoryMappingsExternalId,
    }
)
