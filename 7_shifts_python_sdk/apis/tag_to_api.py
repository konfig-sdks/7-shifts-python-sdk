import typing_extensions

from 7_shifts_python_sdk.apis.tags import TagValues
from 7_shifts_python_sdk.apis.tags.task_management_api import TaskManagementApi
from 7_shifts_python_sdk.apis.tags.log_book_api import LogBookApi
from 7_shifts_python_sdk.apis.tags.user_assignments_api import UserAssignmentsApi
from 7_shifts_python_sdk.apis.tags.availability_api import AvailabilityApi
from 7_shifts_python_sdk.apis.tags.time_off_api import TimeOffApi
from 7_shifts_python_sdk.apis.tags.users_api import UsersApi
from 7_shifts_python_sdk.apis.tags.external_user_mappings_api import ExternalUserMappingsApi
from 7_shifts_python_sdk.apis.tags.forecast_overrides_api import ForecastOverridesApi
from 7_shifts_python_sdk.apis.tags.companies_api import CompaniesApi
from 7_shifts_python_sdk.apis.tags.locations_api import LocationsApi
from 7_shifts_python_sdk.apis.tags.departments_api import DepartmentsApi
from 7_shifts_python_sdk.apis.tags.roles_api import RolesApi
from 7_shifts_python_sdk.apis.tags.shifts_api import ShiftsApi
from 7_shifts_python_sdk.apis.tags.time_punches_api import TimePunchesApi
from 7_shifts_python_sdk.apis.tags.receipts_api import ReceiptsApi
from 7_shifts_python_sdk.apis.tags.schedule_events_api import ScheduleEventsApi
from 7_shifts_python_sdk.apis.tags.tip_pool_api import TipPoolApi
from 7_shifts_python_sdk.apis.tags.webhooks_api import WebhooksApi
from 7_shifts_python_sdk.apis.tags.reports_api import ReportsApi
from 7_shifts_python_sdk.apis.tags.integration_mappings_api import IntegrationMappingsApi
from 7_shifts_python_sdk.apis.tags.authentication_api import AuthenticationApi
from 7_shifts_python_sdk.apis.tags.user_wages_api import UserWagesApi
from 7_shifts_python_sdk.apis.tags.account_api import AccountApi
from 7_shifts_python_sdk.apis.tags.schedule_enforcement_api import ScheduleEnforcementApi
from 7_shifts_python_sdk.apis.tags.shift_feedback_api import ShiftFeedbackApi
from 7_shifts_python_sdk.apis.tags.engage_api import EngageApi
from 7_shifts_python_sdk.apis.tags.day_part_api import DayPartApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TASK_MANAGEMENT: TaskManagementApi,
        TagValues.LOG_BOOK: LogBookApi,
        TagValues.USER_ASSIGNMENTS: UserAssignmentsApi,
        TagValues.AVAILABILITY: AvailabilityApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.USERS: UsersApi,
        TagValues.EXTERNAL_USER_MAPPINGS: ExternalUserMappingsApi,
        TagValues.FORECAST_OVERRIDES: ForecastOverridesApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.ROLES: RolesApi,
        TagValues.SHIFTS: ShiftsApi,
        TagValues.TIME_PUNCHES: TimePunchesApi,
        TagValues.RECEIPTS: ReceiptsApi,
        TagValues.SCHEDULE_EVENTS: ScheduleEventsApi,
        TagValues.TIP_POOL: TipPoolApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.INTEGRATION_MAPPINGS: IntegrationMappingsApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.USER_WAGES: UserWagesApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.SCHEDULE_ENFORCEMENT: ScheduleEnforcementApi,
        TagValues.SHIFT_FEEDBACK: ShiftFeedbackApi,
        TagValues.ENGAGE: EngageApi,
        TagValues.DAY_PART: DayPartApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TASK_MANAGEMENT: TaskManagementApi,
        TagValues.LOG_BOOK: LogBookApi,
        TagValues.USER_ASSIGNMENTS: UserAssignmentsApi,
        TagValues.AVAILABILITY: AvailabilityApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.USERS: UsersApi,
        TagValues.EXTERNAL_USER_MAPPINGS: ExternalUserMappingsApi,
        TagValues.FORECAST_OVERRIDES: ForecastOverridesApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.ROLES: RolesApi,
        TagValues.SHIFTS: ShiftsApi,
        TagValues.TIME_PUNCHES: TimePunchesApi,
        TagValues.RECEIPTS: ReceiptsApi,
        TagValues.SCHEDULE_EVENTS: ScheduleEventsApi,
        TagValues.TIP_POOL: TipPoolApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.INTEGRATION_MAPPINGS: IntegrationMappingsApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.USER_WAGES: UserWagesApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.SCHEDULE_ENFORCEMENT: ScheduleEnforcementApi,
        TagValues.SHIFT_FEEDBACK: ShiftFeedbackApi,
        TagValues.ENGAGE: EngageApi,
        TagValues.DAY_PART: DayPartApi,
    }
)
