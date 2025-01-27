# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 7_shifts_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    OAUTH2_TOKEN = "/oauth2/token"
    V2_WHOAMI = "/v2/whoami"
    V2_PARTNER_COMPANY_CREATION = "/v2/partner_company_creation"
    V2_COMPANIES = "/v2/companies"
    V2_COMPANIES_ID = "/v2/companies/{id}"
    V2_COMPANY_COMPANY_ID_LABOR_SETTINGS = "/v2/company/{company_id}/labor_settings"
    V2_COMPANY_COMPANY_ID_INACTIVE_REASONS = "/v2/company/{company_id}/inactive_reasons"
    V2_COMPANY_COMPANY_ID_LOCATIONS = "/v2/company/{company_id}/locations"
    V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID = "/v2/company/{company_id}/locations/{location_id}"
    V2_COMPANY_COMPANY_ID_DEPARTMENTS = "/v2/company/{company_id}/departments"
    V2_COMPANY_COMPANY_ID_DEPARTMENTS_DEPARTMENT_ID = "/v2/company/{company_id}/departments/{department_id}"
    V2_COMPANY_COMPANY_ID_ROLES = "/v2/company/{company_id}/roles"
    V2_COMPANY_COMPANY_ID_ROLES_ROLE_ID = "/v2/company/{company_id}/roles/{role_id}"
    V2_COMPANY_COMPANY_ID_USERS = "/v2/company/{company_id}/users"
    V2_COMPANY_COMPANY_ID_CREATE_MANY_USERS = "/v2/company/{company_id}/create_many_users"
    V2_COMPANY_COMPANY_ID_USERS_IDENTIFIER = "/v2/company/{company_id}/users/{identifier}"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_WAGES = "/v2/company/{company_id}/users/{user_id}/wages"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_ASSIGNMENTS = "/v2/company/{company_id}/users/{user_id}/assignments"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_LOCATION_ASSIGNMENTS = "/v2/company/{company_id}/users/{user_id}/location_assignments"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_LOCATION_ASSIGNMENTS_LOCATION_ID = "/v2/company/{company_id}/users/{user_id}/location_assignments/{location_id}"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_DEPARTMENT_ASSIGNMENTS = "/v2/company/{company_id}/users/{user_id}/department_assignments"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_DEPARTMENT_ASSIGNMENTS_DEPARTMENT_ID = "/v2/company/{company_id}/users/{user_id}/department_assignments/{department_id}"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_ROLE_ASSIGNMENTS = "/v2/company/{company_id}/users/{user_id}/role_assignments"
    V2_COMPANY_COMPANY_ID_USERS_USER_ID_ROLE_ASSIGNMENTS_ROLE_ID = "/v2/company/{company_id}/users/{user_id}/role_assignments/{role_id}"
    V2_COMPANY_COMPANY_ID_SHIFTS = "/v2/company/{company_id}/shifts"
    V2_COMPANY_COMPANY_ID_SHIFTS_SHIFT_ID = "/v2/company/{company_id}/shifts/{shift_id}"
    V2_COMPANY_COMPANY_ID_SHIFTS_SCHEDULED_ID = "/v2/company/{company_id}/shifts_scheduled/{id}"
    V2_COMPANY_COMPANY_ID_TIME_PUNCHES = "/v2/company/{company_id}/time_punches"
    V2_COMPANY_COMPANY_ID_TIME_PUNCHES_TIME_PUNCH_ID = "/v2/company/{company_id}/time_punches/{time_punch_id}"
    V2_COMPANY_COMPANY_ID_RECEIPTS = "/v2/company/{company_id}/receipts"
    V2_COMPANY_COMPANY_ID_RECEIPTS_RECEIPT_ID = "/v2/company/{company_id}/receipts/{receipt_id}"
    V2_COMPANY_COMPANY_ID_RECEIPTS_SUMMARY = "/v2/company/{company_id}/receipts_summary"
    V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS_IDENTIFIER = "/v2/company/{company_id}/external_user_mappings/{identifier}"
    V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS = "/v2/company/{company_id}/external_user_mappings"
    V2_COMPANY_COMPANY_ID_EXTERNAL_USER_MAPPINGS_BULK = "/v2/company/{company_id}/external_user_mappings_bulk"
    V2_COMPANY_COMPANY_ID_EVENTS = "/v2/company/{company_id}/events"
    V2_COMPANY_COMPANY_ID_EVENTS_EVENT_ID = "/v2/company/{company_id}/events/{event_id}"
    V2_COMPANY_COMPANY_ID_TASK_MANAGEMENT_SETTINGS = "/v2/company/{company_id}/task_management_settings"
    V2_COMPANY_COMPANY_ID_TASK_TAGS = "/v2/company/{company_id}/task_tags"
    V2_COMPANY_COMPANY_ID_TASK_LIST_TEMPLATES = "/v2/company/{company_id}/task_list_templates"
    V2_COMPANY_COMPANY_ID_TASK_LIST_TEMPLATES_UUID = "/v2/company/{company_id}/task_list_templates/{uuid}"
    V2_COMPANY_COMPANY_ID_TASK_LISTS = "/v2/company/{company_id}/task_lists"
    V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID = "/v2/company/{company_id}/task_lists/{list_id}"
    V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID_TASKS_TASK_ID_CLEAR = "/v2/company/{company_id}/task_lists/{list_id}/tasks/{task_id}/clear"
    V2_COMPANY_COMPANY_ID_TASK_LISTS_LIST_ID_TASKS_TASK_ID_COMPLETE = "/v2/company/{company_id}/task_lists/{list_id}/tasks/{task_id}/complete"
    V2_COMPANY_COMPANY_ID_TASK_LIST_DAILY_SUMMARY = "/v2/company/{company_id}/task_list_daily_summary"
    V2_COMPANY_COMPANY_ID_LOG_BOOK_CATEGORIES = "/v2/company/{company_id}/log_book_categories"
    V2_COMPANY_COMPANY_ID_LOG_BOOK_CATEGORIES_ID = "/v2/company/{company_id}/log_book_categories/{id}"
    V2_COMPANY_COMPANY_ID_LOG_BOOK_POSTS = "/v2/company/{company_id}/log_book_posts"
    V2_COMPANY_COMPANY_ID_LOG_BOOK_POSTS_ID = "/v2/company/{company_id}/log_book_posts/{id}"
    V2_COMPANY_COMPANY_ID_LOG_BOOK_COMMENTS = "/v2/company/{company_id}/log_book_comments"
    V2_COMPANY_COMPANY_ID_LOG_BOOK_COMMENTS_ID = "/v2/company/{company_id}/log_book_comments/{id}"
    V2_REPORTS_HOURS_AND_WAGES = "/v2/reports/hours_and_wages"
    V2_REPORTS_DAILY_SALES_AND_LABOR = "/v2/reports/daily_sales_and_labor"
    API_V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_DAILY_STATS = "/api/v2/company/{company_id}/location/{location_id}/daily_stats"
    V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_FORECAST_OVERRIDE = "/v2/company/{company_id}/location/{location_id}/forecast_override"
    V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_FORECAST_OVERRIDES = "/v2/company/{company_id}/location/{location_id}/forecast_overrides"
    V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_FORECAST_OVERRIDE_INTERVAL = "/v2/company/{company_id}/locations/{location_id}/forecast_override_interval"
    V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_FORECAST_OVERRIDES_INTERVALS = "/v2/company/{company_id}/locations/{location_id}/forecast_overrides_intervals"
    V2_COMPANY_COMPANY_ID_TIP_POOL_SETTINGS = "/v2/company/{company_id}/tip_pool_settings"
    V2_COMPANY_COMPANY_ID_TIP_POOL_TIP_POOL_SETTINGS_UUID_MANUAL_ENTRY = "/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry"
    V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_TIP_POOL_SUMMARY_REPORT = "/v2/company/{company_id}/locations/{location_id}/tip_pool_summary_report"
    V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_TIP_POOL_DETAILED_REPORT = "/v2/company/{company_id}/locations/{location_id}/tip_pool_detailed_report"
    V2_COMPANY_COMPANY_ID_DAY_PART_SETTINGS = "/v2/company/{company_id}/day_part/settings"
    V2_COMPANY_COMPANY_ID_AVAILABILITIES = "/v2/company/{company_id}/availabilities"
    V2_COMPANY_COMPANY_ID_AVAILABILITIES_AVAILABILITY_ID = "/v2/company/{company_id}/availabilities/{availability_id}"
    V2_COMPANY_COMPANY_ID_AVAILABILITIES_AVAILABILITY_ID_STATUS = "/v2/company/{company_id}/availabilities/{availability_id}/status"
    V2_COMPANY_COMPANY_ID_AVAILABILITY_REASONS = "/v2/company/{company_id}/availability_reasons"
    V2_COMPANY_COMPANY_ID_AVAILABILITY_REASONS_AVAILABILITY_REASON_ID = "/v2/company/{company_id}/availability_reasons/{availability_reason_id}"
    V2_TIME_OFF = "/v2/time_off"
    V2_TIME_OFF_TIME_OFF_ID = "/v2/time_off/{time_off_id}"
    V2_TIME_OFF_TIME_OFF_ID_APPROVE = "/v2/time_off/{time_off_id}/approve"
    V2_TIME_OFF_TIME_OFF_ID_DECLINE = "/v2/time_off/{time_off_id}/decline"
    V2_TIME_OFF_TOTAL_HOURS = "/v2/time_off/total_hours"
    V2_TIME_OFF_SETTINGS_COMPANY_ID = "/v2/time_off_settings/{company_id}"
    V2_COMPANY_COMPANY_ID_SHIFT_FEEDBACK = "/v2/company/{company_id}/shift_feedback"
    V2_COMPANY_COMPANY_ID_LOCATIONS_LOCATION_ID_ENGAGE_OVERVIEW = "/v2/company/{company_id}/locations/{location_id}/engage_overview"
    V2_COMPANY_COMPANY_ID_WEBHOOKS = "/v2/company/{company_id}/webhooks"
    V2_COMPANY_COMPANY_ID_WEBHOOKS_WEBHOOK_ID = "/v2/company/{company_id}/webhooks/{webhook_id}"
    V2_COMPANY_COMPANY_ID_TEST_WEBHOOK = "/v2/company/{company_id}/test_webhook"
    V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS = "/v2/company/{company_id}/location/{location_id}/sales_category_mappings"
    V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS_BULK = "/v2/company/{company_id}/location/{location_id}/sales_category_mappings_bulk"
    V2_COMPANY_COMPANY_ID_LOCATION_LOCATION_ID_SALES_CATEGORY_MAPPINGS_EXTERNAL_ID = "/v2/company/{company_id}/location/{location_id}/sales_category_mappings/{external_id}"
