# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 7_shifts_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TASK_MANAGEMENT = "Task Management"
    LOG_BOOK = "Log Book"
    USER_ASSIGNMENTS = "User Assignments"
    AVAILABILITY = "Availability"
    TIME_OFF = "Time Off"
    USERS = "Users"
    EXTERNAL_USER_MAPPINGS = "External User Mappings"
    FORECAST_OVERRIDES = "Forecast Overrides"
    COMPANIES = "Companies"
    LOCATIONS = "Locations"
    DEPARTMENTS = "Departments"
    ROLES = "Roles"
    SHIFTS = "Shifts"
    TIME_PUNCHES = "Time Punches"
    RECEIPTS = "Receipts"
    SCHEDULE_EVENTS = "Schedule Events"
    TIP_POOL = "Tip Pool"
    WEBHOOKS = "Webhooks"
    REPORTS = "Reports"
    INTEGRATION_MAPPINGS = "Integration Mappings"
    AUTHENTICATION = "Authentication"
    USER_WAGES = "User Wages"
    ACCOUNT = "Account"
    SCHEDULE_ENFORCEMENT = "Schedule Enforcement"
    SHIFT_FEEDBACK = "Shift Feedback"
    ENGAGE = "Engage"
    DAY_PART = "Day Part"
