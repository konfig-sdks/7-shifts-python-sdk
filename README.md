<div align="left">

[![Visit 7shifts](./header.png)](https://7shifts.com)

# 7shifts<a id="7shifts"></a>

7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.

7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.

Start your free trial or request a demo at www.7shifts.com.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`client7shifts.account.create_trial_account`](#client7shiftsaccountcreate_trial_account)
  * [`client7shifts.authentication.generate_o_auth_token`](#client7shiftsauthenticationgenerate_o_auth_token)
  * [`client7shifts.authentication.get_identity`](#client7shiftsauthenticationget_identity)
  * [`client7shifts.availability.create_new`](#client7shiftsavailabilitycreate_new)
  * [`client7shifts.availability.create_reason`](#client7shiftsavailabilitycreate_reason)
  * [`client7shifts.availability.delete_reason`](#client7shiftsavailabilitydelete_reason)
  * [`client7shifts.availability.get_by_id`](#client7shiftsavailabilityget_by_id)
  * [`client7shifts.availability.list_availabilities`](#client7shiftsavailabilitylist_availabilities)
  * [`client7shifts.availability.list_reasons`](#client7shiftsavailabilitylist_reasons)
  * [`client7shifts.availability.remove_by_id`](#client7shiftsavailabilityremove_by_id)
  * [`client7shifts.availability.update_by_id`](#client7shiftsavailabilityupdate_by_id)
  * [`client7shifts.availability.update_reason_by_id`](#client7shiftsavailabilityupdate_reason_by_id)
  * [`client7shifts.availability.update_status`](#client7shiftsavailabilityupdate_status)
  * [`client7shifts.companies.get_by_id`](#client7shiftscompaniesget_by_id)
  * [`client7shifts.companies.get_labor_settings`](#client7shiftscompaniesget_labor_settings)
  * [`client7shifts.companies.list`](#client7shiftscompanieslist)
  * [`client7shifts.companies.list_inactive_reasons`](#client7shiftscompanieslist_inactive_reasons)
  * [`client7shifts.companies.update_company_by_id`](#client7shiftscompaniesupdate_company_by_id)
  * [`client7shifts.day_part.get_settings`](#client7shiftsday_partget_settings)
  * [`client7shifts.departments.create_new_department`](#client7shiftsdepartmentscreate_new_department)
  * [`client7shifts.departments.delete_by_id`](#client7shiftsdepartmentsdelete_by_id)
  * [`client7shifts.departments.get_department`](#client7shiftsdepartmentsget_department)
  * [`client7shifts.departments.list`](#client7shiftsdepartmentslist)
  * [`client7shifts.departments.update_department`](#client7shiftsdepartmentsupdate_department)
  * [`client7shifts.engage.overview_by_location_id`](#client7shiftsengageoverview_by_location_id)
  * [`client7shifts.external_user_mappings.create_bulk_mappings`](#client7shiftsexternal_user_mappingscreate_bulk_mappings)
  * [`client7shifts.external_user_mappings.create_mapping`](#client7shiftsexternal_user_mappingscreate_mapping)
  * [`client7shifts.external_user_mappings.delete_mapping`](#client7shiftsexternal_user_mappingsdelete_mapping)
  * [`client7shifts.external_user_mappings.get_mapping_by_id`](#client7shiftsexternal_user_mappingsget_mapping_by_id)
  * [`client7shifts.external_user_mappings.list`](#client7shiftsexternal_user_mappingslist)
  * [`client7shifts.external_user_mappings.update_mapping_by_identifier`](#client7shiftsexternal_user_mappingsupdate_mapping_by_identifier)
  * [`client7shifts.forecast_overrides.bulk_create_projected_forecast_override`](#client7shiftsforecast_overridesbulk_create_projected_forecast_override)
  * [`client7shifts.forecast_overrides.bulk_create_projected_sales_interval_override`](#client7shiftsforecast_overridesbulk_create_projected_sales_interval_override)
  * [`client7shifts.forecast_overrides.create_daily_projected_forecast_override`](#client7shiftsforecast_overridescreate_daily_projected_forecast_override)
  * [`client7shifts.forecast_overrides.override_interval`](#client7shiftsforecast_overridesoverride_interval)
  * [`client7shifts.forecast_overrides.sync_projected_forecast_override`](#client7shiftsforecast_overridessync_projected_forecast_override)
  * [`client7shifts.forecast_overrides.sync_projected_sales_interval`](#client7shiftsforecast_overridessync_projected_sales_interval)
  * [`client7shifts.integration_mappings.create_sales_category_mappings_bulk`](#client7shiftsintegration_mappingscreate_sales_category_mappings_bulk)
  * [`client7shifts.integration_mappings.delete_sales_category_mappings`](#client7shiftsintegration_mappingsdelete_sales_category_mappings)
  * [`client7shifts.integration_mappings.list_sales_category_mappings`](#client7shiftsintegration_mappingslist_sales_category_mappings)
  * [`client7shifts.locations.create`](#client7shiftslocationscreate)
  * [`client7shifts.locations.get_location`](#client7shiftslocationsget_location)
  * [`client7shifts.locations.list_get`](#client7shiftslocationslist_get)
  * [`client7shifts.locations.remove_location_by_id`](#client7shiftslocationsremove_location_by_id)
  * [`client7shifts.locations.update_location_by_id`](#client7shiftslocationsupdate_location_by_id)
  * [`client7shifts.log_book.create_category`](#client7shiftslog_bookcreate_category)
  * [`client7shifts.log_book.create_comment`](#client7shiftslog_bookcreate_comment)
  * [`client7shifts.log_book.create_post`](#client7shiftslog_bookcreate_post)
  * [`client7shifts.log_book.delete_category_by_id`](#client7shiftslog_bookdelete_category_by_id)
  * [`client7shifts.log_book.delete_comment`](#client7shiftslog_bookdelete_comment)
  * [`client7shifts.log_book.delete_post`](#client7shiftslog_bookdelete_post)
  * [`client7shifts.log_book.get_comment`](#client7shiftslog_bookget_comment)
  * [`client7shifts.log_book.get_post`](#client7shiftslog_bookget_post)
  * [`client7shifts.log_book.list_categories`](#client7shiftslog_booklist_categories)
  * [`client7shifts.log_book.list_comments`](#client7shiftslog_booklist_comments)
  * [`client7shifts.log_book.list_posts`](#client7shiftslog_booklist_posts)
  * [`client7shifts.log_book.update_category_by_id`](#client7shiftslog_bookupdate_category_by_id)
  * [`client7shifts.receipts.create_receipt`](#client7shiftsreceiptscreate_receipt)
  * [`client7shifts.receipts.get_receipt`](#client7shiftsreceiptsget_receipt)
  * [`client7shifts.receipts.get_summary`](#client7shiftsreceiptsget_summary)
  * [`client7shifts.receipts.list`](#client7shiftsreceiptslist)
  * [`client7shifts.receipts.update_receipt`](#client7shiftsreceiptsupdate_receipt)
  * [`client7shifts.reports.get_daily_sales_and_labor`](#client7shiftsreportsget_daily_sales_and_labor)
  * [`client7shifts.reports.get_daily_stats`](#client7shiftsreportsget_daily_stats)
  * [`client7shifts.reports.get_worked_hours_wages`](#client7shiftsreportsget_worked_hours_wages)
  * [`client7shifts.roles.create_role`](#client7shiftsrolescreate_role)
  * [`client7shifts.roles.delete_role`](#client7shiftsrolesdelete_role)
  * [`client7shifts.roles.get_role`](#client7shiftsrolesget_role)
  * [`client7shifts.roles.list`](#client7shiftsroleslist)
  * [`client7shifts.roles.update_role_by_id`](#client7shiftsrolesupdate_role_by_id)
  * [`client7shifts.schedule_enforcement.list_scheduled_shifts`](#client7shiftsschedule_enforcementlist_scheduled_shifts)
  * [`client7shifts.schedule_events.create_event`](#client7shiftsschedule_eventscreate_event)
  * [`client7shifts.schedule_events.delete_event`](#client7shiftsschedule_eventsdelete_event)
  * [`client7shifts.schedule_events.get_event_by_id`](#client7shiftsschedule_eventsget_event_by_id)
  * [`client7shifts.schedule_events.list_events`](#client7shiftsschedule_eventslist_events)
  * [`client7shifts.schedule_events.update_event_by_id`](#client7shiftsschedule_eventsupdate_event_by_id)
  * [`client7shifts.shift_feedback.list`](#client7shiftsshift_feedbacklist)
  * [`client7shifts.shifts.create_new_shift`](#client7shiftsshiftscreate_new_shift)
  * [`client7shifts.shifts.delete_shift_by_id`](#client7shiftsshiftsdelete_shift_by_id)
  * [`client7shifts.shifts.get_shift_by_id`](#client7shiftsshiftsget_shift_by_id)
  * [`client7shifts.shifts.list`](#client7shiftsshiftslist)
  * [`client7shifts.shifts.update_shift_by_id`](#client7shiftsshiftsupdate_shift_by_id)
  * [`client7shifts.task_management.clear_task`](#client7shiftstask_managementclear_task)
  * [`client7shifts.task_management.create_task_list_template`](#client7shiftstask_managementcreate_task_list_template)
  * [`client7shifts.task_management.create_task_tags`](#client7shiftstask_managementcreate_task_tags)
  * [`client7shifts.task_management.delete_task_list_template`](#client7shiftstask_managementdelete_task_list_template)
  * [`client7shifts.task_management.delete_task_tags`](#client7shiftstask_managementdelete_task_tags)
  * [`client7shifts.task_management.edit_task_list_template`](#client7shiftstask_managementedit_task_list_template)
  * [`client7shifts.task_management.get_settings`](#client7shiftstask_managementget_settings)
  * [`client7shifts.task_management.get_task_list`](#client7shiftstask_managementget_task_list)
  * [`client7shifts.task_management.get_task_list_template`](#client7shiftstask_managementget_task_list_template)
  * [`client7shifts.task_management.get_task_list_templates`](#client7shiftstask_managementget_task_list_templates)
  * [`client7shifts.task_management.get_task_lists`](#client7shiftstask_managementget_task_lists)
  * [`client7shifts.task_management.list_task_lists_summary`](#client7shiftstask_managementlist_task_lists_summary)
  * [`client7shifts.task_management.mark_complete`](#client7shiftstask_managementmark_complete)
  * [`client7shifts.time_off.approve_request`](#client7shiftstime_offapprove_request)
  * [`client7shifts.time_off.create_request`](#client7shiftstime_offcreate_request)
  * [`client7shifts.time_off.decline_request`](#client7shiftstime_offdecline_request)
  * [`client7shifts.time_off.get_settings`](#client7shiftstime_offget_settings)
  * [`client7shifts.time_off.get_time_off_by_id`](#client7shiftstime_offget_time_off_by_id)
  * [`client7shifts.time_off.get_total_hours`](#client7shiftstime_offget_total_hours)
  * [`client7shifts.time_off.list`](#client7shiftstime_offlist)
  * [`client7shifts.time_off.remove`](#client7shiftstime_offremove)
  * [`client7shifts.time_off.set_time_off_settings`](#client7shiftstime_offset_time_off_settings)
  * [`client7shifts.time_off.update_time_off_by_id`](#client7shiftstime_offupdate_time_off_by_id)
  * [`client7shifts.time_punches.create`](#client7shiftstime_punchescreate)
  * [`client7shifts.time_punches.delete_by_id`](#client7shiftstime_punchesdelete_by_id)
  * [`client7shifts.time_punches.get_time_punch`](#client7shiftstime_punchesget_time_punch)
  * [`client7shifts.time_punches.list`](#client7shiftstime_puncheslist)
  * [`client7shifts.time_punches.update_by_id`](#client7shiftstime_punchesupdate_by_id)
  * [`client7shifts.tip_pool.get_detailed_report`](#client7shiftstip_poolget_detailed_report)
  * [`client7shifts.tip_pool.get_manual_entry_tips`](#client7shiftstip_poolget_manual_entry_tips)
  * [`client7shifts.tip_pool.get_settings`](#client7shiftstip_poolget_settings)
  * [`client7shifts.tip_pool.get_summary_report`](#client7shiftstip_poolget_summary_report)
  * [`client7shifts.tip_pool.save_manual_entry`](#client7shiftstip_poolsave_manual_entry)
  * [`client7shifts.user_assignments.create_department_assignment`](#client7shiftsuser_assignmentscreate_department_assignment)
  * [`client7shifts.user_assignments.create_location_assignment`](#client7shiftsuser_assignmentscreate_location_assignment)
  * [`client7shifts.user_assignments.create_role_assignment`](#client7shiftsuser_assignmentscreate_role_assignment)
  * [`client7shifts.user_assignments.delete_role_assignment`](#client7shiftsuser_assignmentsdelete_role_assignment)
  * [`client7shifts.user_assignments.list`](#client7shiftsuser_assignmentslist)
  * [`client7shifts.user_assignments.list_department_assignments`](#client7shiftsuser_assignmentslist_department_assignments)
  * [`client7shifts.user_assignments.list_location_assignments`](#client7shiftsuser_assignmentslist_location_assignments)
  * [`client7shifts.user_assignments.list_role_assignments`](#client7shiftsuser_assignmentslist_role_assignments)
  * [`client7shifts.user_assignments.remove_department_assignment`](#client7shiftsuser_assignmentsremove_department_assignment)
  * [`client7shifts.user_assignments.remove_location_assignment`](#client7shiftsuser_assignmentsremove_location_assignment)
  * [`client7shifts.user_wages.create`](#client7shiftsuser_wagescreate)
  * [`client7shifts.user_wages.list`](#client7shiftsuser_wageslist)
  * [`client7shifts.users.bulk_create`](#client7shiftsusersbulk_create)
  * [`client7shifts.users.create_new_user`](#client7shiftsuserscreate_new_user)
  * [`client7shifts.users.deactivate`](#client7shiftsusersdeactivate)
  * [`client7shifts.users.get_user_by_identifier`](#client7shiftsusersget_user_by_identifier)
  * [`client7shifts.users.list`](#client7shiftsuserslist)
  * [`client7shifts.users.update_user_by_identifier`](#client7shiftsusersupdate_user_by_identifier)
  * [`client7shifts.webhooks.create`](#client7shiftswebhookscreate)
  * [`client7shifts.webhooks.delete_webhook_by_id`](#client7shiftswebhooksdelete_webhook_by_id)
  * [`client7shifts.webhooks.get_webhook`](#client7shiftswebhooksget_webhook)
  * [`client7shifts.webhooks.list`](#client7shiftswebhookslist)
  * [`client7shifts.webhooks.update`](#client7shiftswebhooksupdate)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=7shifts&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from 7_shifts_python_sdk import Client7Shifts, ApiException

client7shifts = Client7Shifts(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        cookie_auth = 'YOUR_API_KEY',
)

try:
    # Create Trial Account
    create_trial_account_response = client7shifts.account.create_trial_account(
        email="string_example",
        firstname="string_example",
        lastname="string_example",
        company_name="string_example",
        country="CA",
        utm_source="string_example",
        mobile_phone="string_example",
        utm_campaign="string_example",
        utm_content="string_example",
        utm_medium="string_example",
        utm_term="string_example",
        x_api_version="2022-05-01",
        x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    )
    print(create_trial_account_response)
except ApiException as e:
    print("Exception when calling AccountApi.create_trial_account: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 422:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 401:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 500:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 403:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from 7_shifts_python_sdk import Client7Shifts, ApiException

client7shifts = Client7Shifts(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        cookie_auth = 'YOUR_API_KEY',
)

async def main():
    try:
        # Create Trial Account
        create_trial_account_response = await client7shifts.account.acreate_trial_account(
            email="string_example",
            firstname="string_example",
            lastname="string_example",
            company_name="string_example",
            country="CA",
            utm_source="string_example",
            mobile_phone="string_example",
            utm_campaign="string_example",
            utm_content="string_example",
            utm_medium="string_example",
            utm_term="string_example",
            x_api_version="2022-05-01",
            x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
        )
        print(create_trial_account_response)
    except ApiException as e:
        print("Exception when calling AccountApi.create_trial_account: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["title"])
            pprint(e.body["type"])
            pprint(e.body["status"])
            pprint(e.body["detail"])
            pprint(e.body["code"])
            pprint(e.body["param"])
        if e.status == 422:
            pprint(e.body["title"])
            pprint(e.body["type"])
            pprint(e.body["status"])
            pprint(e.body["detail"])
            pprint(e.body["code"])
            pprint(e.body["param"])
        if e.status == 401:
            pprint(e.body["title"])
            pprint(e.body["type"])
            pprint(e.body["status"])
            pprint(e.body["detail"])
            pprint(e.body["code"])
            pprint(e.body["param"])
        if e.status == 500:
            pprint(e.body["title"])
            pprint(e.body["type"])
            pprint(e.body["status"])
            pprint(e.body["detail"])
            pprint(e.body["code"])
            pprint(e.body["param"])
        if e.status == 403:
            pprint(e.body["title"])
            pprint(e.body["type"])
            pprint(e.body["status"])
            pprint(e.body["detail"])
            pprint(e.body["code"])
            pprint(e.body["param"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from 7_shifts_python_sdk import Client7Shifts, ApiException

client7shifts = Client7Shifts(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

        cookie_auth = 'YOUR_API_KEY',
)

try:
    # Create Trial Account
    create_trial_account_response = client7shifts.account.raw.create_trial_account(
        email="string_example",
        firstname="string_example",
        lastname="string_example",
        company_name="string_example",
        country="CA",
        utm_source="string_example",
        mobile_phone="string_example",
        utm_campaign="string_example",
        utm_content="string_example",
        utm_medium="string_example",
        utm_term="string_example",
        x_api_version="2022-05-01",
        x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    )
    pprint(create_trial_account_response.body)
    pprint(create_trial_account_response.body["object"])
    pprint(create_trial_account_response.body["data"])
    pprint(create_trial_account_response.headers)
    pprint(create_trial_account_response.status)
    pprint(create_trial_account_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountApi.create_trial_account: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 422:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 401:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 500:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    if e.status == 403:
        pprint(e.body["title"])
        pprint(e.body["type"])
        pprint(e.body["status"])
        pprint(e.body["detail"])
        pprint(e.body["code"])
        pprint(e.body["param"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `client7shifts.account.create_trial_account`<a id="client7shiftsaccountcreate_trial_account"></a>

Create Trial Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_trial_account_response = client7shifts.account.create_trial_account(
    email="string_example",
    firstname="string_example",
    lastname="string_example",
    company_name="string_example",
    country="CA",
    utm_source="string_example",
    mobile_phone="string_example",
    utm_campaign="string_example",
    utm_content="string_example",
    utm_medium="string_example",
    utm_term="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

The user's email

##### firstname: `str`<a id="firstname-str"></a>

The user's first name

##### lastname: `str`<a id="lastname-str"></a>

The user's last name

##### company_name: `str`<a id="company_name-str"></a>

The company's name

##### country: `str`<a id="country-str"></a>

The company's country

##### utm_source: `str`<a id="utm_source-str"></a>

The UTM source

##### mobile_phone: `str`<a id="mobile_phone-str"></a>

The user's mobile phone

##### utm_campaign: `str`<a id="utm_campaign-str"></a>

The UTM campaign

##### utm_content: `str`<a id="utm_content-str"></a>

The UTM content

##### utm_medium: `str`<a id="utm_medium-str"></a>

The UTM medium

##### utm_term: `str`<a id="utm_term-str"></a>

The UTM term

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccountCreateTrialAccountRequest`](./7_shifts_python_sdk/type/account_create_trial_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccountCreateTrialAccountResponse`](./7_shifts_python_sdk/pydantic/account_create_trial_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/partner_company_creation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.authentication.generate_o_auth_token`<a id="client7shiftsauthenticationgenerate_o_auth_token"></a>

Create OAuth Token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_o_auth_token_response = client7shifts.authentication.generate_o_auth_token(
    grant_type="client_credentials",
    client_id="string_example",
    client_secret="string_example",
    scope="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

Token grant type. For Partner OAuth tokens specifying client_credentials

##### client_id: `str`<a id="client_id-str"></a>

##### client_secret: `str`<a id="client_secret-str"></a>

##### scope: `str`<a id="scope-str"></a>

A space-delimited list of scopes.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationGenerateOAuthTokenRequest`](./7_shifts_python_sdk/type/authentication_generate_o_auth_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationGenerateOAuthTokenResponse`](./7_shifts_python_sdk/pydantic/authentication_generate_o_auth_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.authentication.get_identity`<a id="client7shiftsauthenticationget_identity"></a>

Retrieve Identity

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_identity_response = client7shifts.authentication.get_identity(
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationGetIdentityResponse`](./7_shifts_python_sdk/pydantic/authentication_get_identity_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/whoami` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.create_new`<a id="client7shiftsavailabilitycreate_new"></a>

Create Availability

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = client7shifts.availability.create_new(
    user_id=1,
    repeat=True,
    mon=1,
    mon_from="string_example",
    mon_to="string_example",
    mon_comments="string_example",
    mon_reason="string_example",
    tue=1,
    tue_from="string_example",
    tue_to="string_example",
    tue_comments="string_example",
    tue_reason="string_example",
    wed=1,
    wed_from="string_example",
    wed_to="string_example",
    wed_comments="string_example",
    wed_reason="string_example",
    thu=1,
    thu_from="string_example",
    thu_to="string_example",
    thu_comments="string_example",
    thu_reason="string_example",
    fri=1,
    fri_from="string_example",
    fri_to="string_example",
    fri_comments="string_example",
    fri_reason="string_example",
    sat=1,
    sat_from="string_example",
    sat_to="string_example",
    sat_comments="string_example",
    sat_reason="string_example",
    sun=1,
    sun_from="string_example",
    sun_to="string_example",
    sun_comments="string_example",
    sun_reason="string_example",
    company_id=1234,
    week="string_example",
    week_to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### repeat: `bool`<a id="repeat-bool"></a>

If true, availability is repeating

##### mon: `int`<a id="mon-int"></a>

The availability status for the day

##### mon_from: `str`<a id="mon_from-str"></a>

The start time of the availability for the day

##### mon_to: `str`<a id="mon_to-str"></a>

The end time of the availability for the day

##### mon_comments: `Optional[str]`<a id="mon_comments-optionalstr"></a>

Comments included in the days availability

##### mon_reason: `str`<a id="mon_reason-str"></a>

The reason ID for the day

##### tue: `int`<a id="tue-int"></a>

The availability status for the day

##### tue_from: `str`<a id="tue_from-str"></a>

The start time of the availability for the day

##### tue_to: `str`<a id="tue_to-str"></a>

The end time of the availability for the day

##### tue_comments: `Optional[str]`<a id="tue_comments-optionalstr"></a>

Comments included in the days availability

##### tue_reason: `str`<a id="tue_reason-str"></a>

The reason ID for the day

##### wed: `int`<a id="wed-int"></a>

The availability status for the day

##### wed_from: `str`<a id="wed_from-str"></a>

The start time of the availability for the day

##### wed_to: `str`<a id="wed_to-str"></a>

The end time of the availability for the day

##### wed_comments: `Optional[str]`<a id="wed_comments-optionalstr"></a>

Comments included in the days availability

##### wed_reason: `str`<a id="wed_reason-str"></a>

The reason ID for the day

##### thu: `int`<a id="thu-int"></a>

The availability status for the day

##### thu_from: `str`<a id="thu_from-str"></a>

The start time of the availability for the day

##### thu_to: `str`<a id="thu_to-str"></a>

The end time of the availability for the day

##### thu_comments: `Optional[str]`<a id="thu_comments-optionalstr"></a>

Comments included in the days availability

##### thu_reason: `str`<a id="thu_reason-str"></a>

The reason ID for the day

##### fri: `int`<a id="fri-int"></a>

The availability status for the day

##### fri_from: `str`<a id="fri_from-str"></a>

The start time of the availability for the day

##### fri_to: `str`<a id="fri_to-str"></a>

The end time of the availability for the day

##### fri_comments: `Optional[str]`<a id="fri_comments-optionalstr"></a>

Comments included in the days availability

##### fri_reason: `str`<a id="fri_reason-str"></a>

The reason ID for the day

##### sat: `int`<a id="sat-int"></a>

The availability status for the day

##### sat_from: `str`<a id="sat_from-str"></a>

The start time of the availability for the day

##### sat_to: `str`<a id="sat_to-str"></a>

The end time of the availability for the day

##### sat_comments: `Optional[str]`<a id="sat_comments-optionalstr"></a>

Comments included in the days availability

##### sat_reason: `str`<a id="sat_reason-str"></a>

The reason ID for the day

##### sun: `int`<a id="sun-int"></a>

The availability status for the day

##### sun_from: `str`<a id="sun_from-str"></a>

The start time of the availability for the day

##### sun_to: `str`<a id="sun_to-str"></a>

The end time of the availability for the day

##### sun_comments: `Optional[str]`<a id="sun_comments-optionalstr"></a>

Comments included in the days availability

##### sun_reason: `str`<a id="sun_reason-str"></a>

The reason ID for the day

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### week: `Optional[str]`<a id="week-optionalstr"></a>

Week date of the availability

##### week_to: `Optional[str]`<a id="week_to-optionalstr"></a>

Week to date of the availability

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AvailabilityCreateNewRequest`](./7_shifts_python_sdk/type/availability_create_new_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityCreateNewResponse`](./7_shifts_python_sdk/pydantic/availability_create_new_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availabilities` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.create_reason`<a id="client7shiftsavailabilitycreate_reason"></a>

Create Availability Reason

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_reason_response = client7shifts.availability.create_reason(
    reason="string_example",
    company_id=1234,
    comments_required=True,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reason: `str`<a id="reason-str"></a>

Availability reason

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### comments_required: `Optional[bool]`<a id="comments_required-optionalbool"></a>

Comments required

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AvailabilityCreateReasonRequest`](./7_shifts_python_sdk/type/availability_create_reason_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityCreateReasonResponse`](./7_shifts_python_sdk/pydantic/availability_create_reason_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availability_reasons` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.delete_reason`<a id="client7shiftsavailabilitydelete_reason"></a>

Delete Availability Reason

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.availability.delete_reason(
    company_id=1234,
    availability_reason_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### availability_reason_id: `int`<a id="availability_reason_id-int"></a>

Availability Reason ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availability_reasons/{availability_reason_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.get_by_id`<a id="client7shiftsavailabilityget_by_id"></a>

Retrieve Availability

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = client7shifts.availability.get_by_id(
    company_id=1234,
    availability_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### availability_id: `int`<a id="availability_id-int"></a>

Availability ID

#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityGetByIdResponse`](./7_shifts_python_sdk/pydantic/availability_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availabilities/{availability_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.list_availabilities`<a id="client7shiftsavailabilitylist_availabilities"></a>

List Availabilities

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_availabilities_response = client7shifts.availability.list_availabilities(
    company_id=1234,
    cursor="string_example",
    limit=100,
    location_id=1234,
    user_id=1234,
    status=1,
    repeating=True,
    week_gte="2020-01-01",
    week_to_include_repeating_gte="2020-01-01",
    order_field="string_example",
    order_dir=",iEEpmVvrKlTttzGFqCEGyGBLkBAsBQRJXFH_OJE_CWHioCHFdWvFEDxwNvqMvvkTRU",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number results desired per page.

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### status: `int`<a id="status-int"></a>

Return availabilities for a specified status (pending = 0, approved = 1, declined = 2).

##### repeating: `bool`<a id="repeating-bool"></a>

Return repeating or weekly availabilities.

##### week_gte: `str`<a id="week_gte-str"></a>

Return availabilities for a specific week.

##### week_to_include_repeating_gte: `str`<a id="week_to_include_repeating_gte-str"></a>

Return repeating availabilities that end before or on a specified week.

##### order_field: `str`<a id="order_field-str"></a>

The field that availabilities will be sorted by.

##### order_dir: `str`<a id="order_dir-str"></a>

The direction that availabilities will be sorted by.

#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityListAvailabilitiesResponse`](./7_shifts_python_sdk/pydantic/availability_list_availabilities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availabilities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.list_reasons`<a id="client7shiftsavailabilitylist_reasons"></a>

List Availability Reasons

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_reasons_response = client7shifts.availability.list_reasons(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    cursor="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityListReasonsResponse`](./7_shifts_python_sdk/pydantic/availability_list_reasons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availability_reasons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.remove_by_id`<a id="client7shiftsavailabilityremove_by_id"></a>

Delete Availability

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.availability.remove_by_id(
    company_id=1234,
    availability_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### availability_id: `int`<a id="availability_id-int"></a>

Availability ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availabilities/{availability_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.update_by_id`<a id="client7shiftsavailabilityupdate_by_id"></a>

Update Availability

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = client7shifts.availability.update_by_id(
    company_id=1234,
    availability_id=1234,
    week="string_example",
    week_to="string_example",
    repeat=True,
    mon=1,
    mon_from="string_example",
    mon_to="string_example",
    mon_comments="string_example",
    mon_reason="string_example",
    tue=1,
    tue_from="string_example",
    tue_to="string_example",
    tue_comments="string_example",
    tue_reason="string_example",
    wed=1,
    wed_from="string_example",
    wed_to="string_example",
    wed_comments="string_example",
    wed_reason="string_example",
    thu=1,
    thu_from="string_example",
    thu_to="string_example",
    thu_comments="string_example",
    thu_reason="string_example",
    fri=1,
    fri_from="string_example",
    fri_to="string_example",
    fri_comments="string_example",
    fri_reason="string_example",
    sat=1,
    sat_from="string_example",
    sat_to="string_example",
    sat_comments="string_example",
    sat_reason="string_example",
    sun=1,
    sun_from="string_example",
    sun_to="string_example",
    sun_comments="string_example",
    sun_reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### availability_id: `int`<a id="availability_id-int"></a>

Availability ID

##### week: `Optional[str]`<a id="week-optionalstr"></a>

Week date of the availability

##### week_to: `Optional[str]`<a id="week_to-optionalstr"></a>

Week to date of the availability

##### repeat: `bool`<a id="repeat-bool"></a>

If true, availability is repeating

##### mon: `int`<a id="mon-int"></a>

The availability status for the day

##### mon_from: `str`<a id="mon_from-str"></a>

The start time of the availability for the day

##### mon_to: `str`<a id="mon_to-str"></a>

The end time of the availability for the day

##### mon_comments: `Optional[str]`<a id="mon_comments-optionalstr"></a>

Comments included in the days availability

##### mon_reason: `str`<a id="mon_reason-str"></a>

The reason ID for the day

##### tue: `int`<a id="tue-int"></a>

The availability status for the day

##### tue_from: `str`<a id="tue_from-str"></a>

The start time of the availability for the day

##### tue_to: `str`<a id="tue_to-str"></a>

The end time of the availability for the day

##### tue_comments: `Optional[str]`<a id="tue_comments-optionalstr"></a>

Comments included in the days availability

##### tue_reason: `str`<a id="tue_reason-str"></a>

The reason ID for the day

##### wed: `int`<a id="wed-int"></a>

The availability status for the day

##### wed_from: `str`<a id="wed_from-str"></a>

The start time of the availability for the day

##### wed_to: `str`<a id="wed_to-str"></a>

The end time of the availability for the day

##### wed_comments: `Optional[str]`<a id="wed_comments-optionalstr"></a>

Comments included in the days availability

##### wed_reason: `str`<a id="wed_reason-str"></a>

The reason ID for the day

##### thu: `int`<a id="thu-int"></a>

The availability status for the day

##### thu_from: `str`<a id="thu_from-str"></a>

The start time of the availability for the day

##### thu_to: `str`<a id="thu_to-str"></a>

The end time of the availability for the day

##### thu_comments: `Optional[str]`<a id="thu_comments-optionalstr"></a>

Comments included in the days availability

##### thu_reason: `str`<a id="thu_reason-str"></a>

The reason ID for the day

##### fri: `int`<a id="fri-int"></a>

The availability status for the day

##### fri_from: `str`<a id="fri_from-str"></a>

The start time of the availability for the day

##### fri_to: `str`<a id="fri_to-str"></a>

The end time of the availability for the day

##### fri_comments: `Optional[str]`<a id="fri_comments-optionalstr"></a>

Comments included in the days availability

##### fri_reason: `str`<a id="fri_reason-str"></a>

The reason ID for the day

##### sat: `int`<a id="sat-int"></a>

The availability status for the day

##### sat_from: `str`<a id="sat_from-str"></a>

The start time of the availability for the day

##### sat_to: `str`<a id="sat_to-str"></a>

The end time of the availability for the day

##### sat_comments: `Optional[str]`<a id="sat_comments-optionalstr"></a>

Comments included in the days availability

##### sat_reason: `str`<a id="sat_reason-str"></a>

The reason ID for the day

##### sun: `int`<a id="sun-int"></a>

The availability status for the day

##### sun_from: `str`<a id="sun_from-str"></a>

The start time of the availability for the day

##### sun_to: `str`<a id="sun_to-str"></a>

The end time of the availability for the day

##### sun_comments: `Optional[str]`<a id="sun_comments-optionalstr"></a>

Comments included in the days availability

##### sun_reason: `str`<a id="sun_reason-str"></a>

The reason ID for the day

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AvailabilityUpdateByIdRequest`](./7_shifts_python_sdk/type/availability_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityUpdateByIdResponse`](./7_shifts_python_sdk/pydantic/availability_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availabilities/{availability_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.update_reason_by_id`<a id="client7shiftsavailabilityupdate_reason_by_id"></a>

Update Availability Reason

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_reason_by_id_response = client7shifts.availability.update_reason_by_id(
    reason="string_example",
    company_id=1234,
    availability_reason_id=1234,
    comments_required=True,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reason: `str`<a id="reason-str"></a>

Availability reason

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### availability_reason_id: `int`<a id="availability_reason_id-int"></a>

Availability Reason ID

##### comments_required: `Optional[bool]`<a id="comments_required-optionalbool"></a>

Comments required

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AvailabilityUpdateReasonByIdRequest`](./7_shifts_python_sdk/type/availability_update_reason_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AvailabilityUpdateReasonByIdResponse`](./7_shifts_python_sdk/pydantic/availability_update_reason_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availability_reasons/{availability_reason_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.availability.update_status`<a id="client7shiftsavailabilityupdate_status"></a>

Update Availability Status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.availability.update_status(
    status="approved",
    company_id=1234,
    availability_id=1234,
    message="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### availability_id: `int`<a id="availability_id-int"></a>

Availability ID

##### message: `str`<a id="message-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AvailabilityUpdateStatusRequest`](./7_shifts_python_sdk/type/availability_update_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/availabilities/{availability_id}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.companies.get_by_id`<a id="client7shiftscompaniesget_by_id"></a>

Retrieve Company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = client7shifts.companies.get_by_id(
    id=8655,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetByIdResponse`](./7_shifts_python_sdk/pydantic/companies_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.companies.get_labor_settings`<a id="client7shiftscompaniesget_labor_settings"></a>

Retrieve Labor Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_labor_settings_response = client7shifts.companies.get_labor_settings(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesGetLaborSettingsResponse`](./7_shifts_python_sdk/pydantic/companies_get_labor_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/labor_settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.companies.list`<a id="client7shiftscompanieslist"></a>

List Companies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.companies.list(
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    modified_since="2020-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### modified_since: `str`<a id="modified_since-str"></a>

Return companies that have been modified since the specified date. Format YYYY-MM-DD

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesListResponse`](./7_shifts_python_sdk/pydantic/companies_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.companies.list_inactive_reasons`<a id="client7shiftscompanieslist_inactive_reasons"></a>

List Inactive Reasons

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_inactive_reasons_response = client7shifts.companies.list_inactive_reasons(
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesListInactiveReasonsResponse`](./7_shifts_python_sdk/pydantic/companies_list_inactive_reasons_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/inactive_reasons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.companies.update_company_by_id`<a id="client7shiftscompaniesupdate_company_by_id"></a>

Update Company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_company_by_id_response = client7shifts.companies.update_company_by_id(
    id=1,
    name="string_example",
    country="string_example",
    photo="string_example",
    pos="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Company ID

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### country: `Optional[str]`<a id="country-optionalstr"></a>

##### photo: `Optional[str]`<a id="photo-optionalstr"></a>

##### pos: `Optional[str]`<a id="pos-optionalstr"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompaniesUpdateCompanyByIdRequest`](./7_shifts_python_sdk/type/companies_update_company_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesUpdateCompanyByIdResponse`](./7_shifts_python_sdk/pydantic/companies_update_company_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/companies/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.day_part.get_settings`<a id="client7shiftsday_partget_settings"></a>

Retrieve day part settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = client7shifts.day_part.get_settings(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID - null will fetch all day parts for company

#### 🔄 Return<a id="🔄-return"></a>

[`DayPartGetSettingsResponse`](./7_shifts_python_sdk/pydantic/day_part_get_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/day_part/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.departments.create_new_department`<a id="client7shiftsdepartmentscreate_new_department"></a>

Create Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_department_response = client7shifts.departments.create_new_department(
    location_id=3.14,
    name="string_example",
    default=True,
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `Union[int, float]`<a id="location_id-unionint-float"></a>

Location ID

##### name: `str`<a id="name-str"></a>

Department name

##### default: `bool`<a id="default-bool"></a>

If true department is set as the default for the location

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsCreateNewDepartmentRequest`](./7_shifts_python_sdk/type/departments_create_new_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsCreateNewDepartmentResponse`](./7_shifts_python_sdk/pydantic/departments_create_new_department_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.departments.delete_by_id`<a id="client7shiftsdepartmentsdelete_by_id"></a>

Delete Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.departments.delete_by_id(
    company_id=1234,
    department_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    transfer_to=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### transfer_to: `int`<a id="transfer_to-int"></a>

Department ID to move roles and shifts to

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/departments/{department_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.departments.get_department`<a id="client7shiftsdepartmentsget_department"></a>

Retrieve Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_department_response = client7shifts.departments.get_department(
    company_id=1234,
    department_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsGetDepartmentResponse`](./7_shifts_python_sdk/pydantic/departments_get_department_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/departments/{department_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.departments.list`<a id="client7shiftsdepartmentslist"></a>

List Departments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.departments.list(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    modified_since="2020-01-01",
    cursor="string_example",
    limit=1,
    location_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### modified_since: `str`<a id="modified_since-str"></a>

Return departments that have been modified since the specified date. Format YYYY-MM-DD

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

##### location_id: `int`<a id="location_id-int"></a>

Return departments that match the provided location ID

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsListResponse`](./7_shifts_python_sdk/pydantic/departments_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.departments.update_department`<a id="client7shiftsdepartmentsupdate_department"></a>

Update Department

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_department_response = client7shifts.departments.update_department(
    name="string_example",
    default=True,
    company_id=1234,
    department_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Department name

##### default: `bool`<a id="default-bool"></a>

If true department is set as the default for the location

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DepartmentsUpdateDepartmentRequest`](./7_shifts_python_sdk/type/departments_update_department_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsUpdateDepartmentResponse`](./7_shifts_python_sdk/pydantic/departments_update_department_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/departments/{department_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.engage.overview_by_location_id`<a id="client7shiftsengageoverview_by_location_id"></a>

Retrieve Engagement Overview

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
overview_by_location_id_response = client7shifts.engage.overview_by_location_id(
    company_id=384,
    location_id=408,
    date="2022-11-22",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    frequency="week",
    user_type="managers",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### date: `str`<a id="date-str"></a>

A date with YYYY-MM-DD format

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### frequency: `str`<a id="frequency-str"></a>

Length of the engage data set

##### user_type: `str`<a id="user_type-str"></a>

select user type for engage data

#### 🔄 Return<a id="🔄-return"></a>

[`EngageOverviewByLocationIdResponse`](./7_shifts_python_sdk/pydantic/engage_overview_by_location_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}/engage_overview` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.external_user_mappings.create_bulk_mappings`<a id="client7shiftsexternal_user_mappingscreate_bulk_mappings"></a>

Create User External Mappings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bulk_mappings_response = client7shifts.external_user_mappings.create_bulk_mappings(
    data=[
        {
            "external_user_id": "external_user_id_example",
            "phone_number": "3061234454",
        }
    ],
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`ExternalUserMappingsCreateBulkMappingsRequestData`](./7_shifts_python_sdk/type/external_user_mappings_create_bulk_mappings_request_data.py)<a id="data-externalusermappingscreatebulkmappingsrequestdata7_shifts_python_sdktypeexternal_user_mappings_create_bulk_mappings_request_datapy"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalUserMappingsCreateBulkMappingsRequest`](./7_shifts_python_sdk/type/external_user_mappings_create_bulk_mappings_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalUserMappingsCreateBulkMappingsResponse`](./7_shifts_python_sdk/pydantic/external_user_mappings_create_bulk_mappings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/external_user_mappings_bulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.external_user_mappings.create_mapping`<a id="client7shiftsexternal_user_mappingscreate_mapping"></a>

Create External User Mapping

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_mapping_response = client7shifts.external_user_mappings.create_mapping(
    user_id=1,
    external_user_id="string_example",
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

User ID in 7Shifts

##### external_user_id: `str`<a id="external_user_id-str"></a>

User ID in External System

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalUserMappingsCreateMappingRequest`](./7_shifts_python_sdk/type/external_user_mappings_create_mapping_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalUserMappingsCreateMappingResponse`](./7_shifts_python_sdk/pydantic/external_user_mappings_create_mapping_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/external_user_mappings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.external_user_mappings.delete_mapping`<a id="client7shiftsexternal_user_mappingsdelete_mapping"></a>

Delete External User Mapping

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.external_user_mappings.delete_mapping(
    company_id=1,
    identifier="46734",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### identifier: `str`<a id="identifier-str"></a>

User ID. Accepted values are 7Shifts user id, external user id or user email address. Use prefix ext: for external id or email: for email address

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/external_user_mappings/{identifier}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.external_user_mappings.get_mapping_by_id`<a id="client7shiftsexternal_user_mappingsget_mapping_by_id"></a>

Retrieve User External Mapping

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mapping_by_id_response = client7shifts.external_user_mappings.get_mapping_by_id(
    company_id=1,
    identifier="46734",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### identifier: `str`<a id="identifier-str"></a>

User ID. Accepted values are 7Shifts user id or external user id. Use prefix ext: for external id

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalUserMappingsGetMappingByIdResponse`](./7_shifts_python_sdk/pydantic/external_user_mappings_get_mapping_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/external_user_mappings/{identifier}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.external_user_mappings.list`<a id="client7shiftsexternal_user_mappingslist"></a>

List External User Mapping

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.external_user_mappings.list(
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
    user_id=1,
    external_user_id="string_example",
    modified_since="2020-01-01",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### user_id: `int`<a id="user_id-int"></a>

The 7shifts user ID

##### external_user_id: `str`<a id="external_user_id-str"></a>

The external user ID

##### modified_since: `str`<a id="modified_since-str"></a>

Return records that have been modified since the specified date. Format YYYY-MM-DD

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ExternalUserMappingsListResponse`](./7_shifts_python_sdk/pydantic/external_user_mappings_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/external_user_mappings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.external_user_mappings.update_mapping_by_identifier`<a id="client7shiftsexternal_user_mappingsupdate_mapping_by_identifier"></a>

Update External User Mappings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_mapping_by_identifier_response = client7shifts.external_user_mappings.update_mapping_by_identifier(
    company_id=1,
    identifier="46734",
    user_id=1,
    external_user_id="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### identifier: `str`<a id="identifier-str"></a>

User ID. Accepted values are 7Shifts user id or external user id. Use prefix ext: for external id

##### user_id: `int`<a id="user_id-int"></a>

User ID in 7Shifts

##### external_user_id: `str`<a id="external_user_id-str"></a>

User ID in External System

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExternalUserMappingsUpdateMappingByIdentifierRequest`](./7_shifts_python_sdk/type/external_user_mappings_update_mapping_by_identifier_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExternalUserMappingsUpdateMappingByIdentifierResponse`](./7_shifts_python_sdk/pydantic/external_user_mappings_update_mapping_by_identifier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/external_user_mappings/{identifier}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.forecast_overrides.bulk_create_projected_forecast_override`<a id="client7shiftsforecast_overridesbulk_create_projected_forecast_override"></a>

Create Bulk Daily Projected Forecast Overrides

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_create_projected_forecast_override_response = client7shifts.forecast_overrides.bulk_create_projected_forecast_override(
    data=[
        {
            "department_id": 1234,
            "date": "2020-01-01",
            "value": 1234,
            "report_type": "sales",
        }
    ],
    company_id=1,
    location_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`ForecastOverridesBulkCreateProjectedForecastOverrideRequestData`](./7_shifts_python_sdk/type/forecast_overrides_bulk_create_projected_forecast_override_request_data.py)<a id="data-forecastoverridesbulkcreateprojectedforecastoverriderequestdata7_shifts_python_sdktypeforecast_overrides_bulk_create_projected_forecast_override_request_datapy"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ForecastOverridesBulkCreateProjectedForecastOverrideRequest`](./7_shifts_python_sdk/type/forecast_overrides_bulk_create_projected_forecast_override_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ForecastOverridesBulkCreateProjectedForecastOverrideResponse`](./7_shifts_python_sdk/pydantic/forecast_overrides_bulk_create_projected_forecast_override_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/location/{location_id}/forecast_overrides` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.forecast_overrides.bulk_create_projected_sales_interval_override`<a id="client7shiftsforecast_overridesbulk_create_projected_sales_interval_override"></a>

Overrides many project sales intervals of 15 minutes or 1 hour. (In Development)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.forecast_overrides.bulk_create_projected_sales_interval_override(
    body=[
        {
            "start": "2020-12-30T20:00:00Z",
            "end": "2020-12-30T20:15:00Z",
            "value": 1234,
            "report_type": "sales",
        }
    ],
    company_id=1,
    location_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### requestBody: [`ForecastOverridesBulkCreateProjectedSalesIntervalOverrideRequest`](./7_shifts_python_sdk/type/forecast_overrides_bulk_create_projected_sales_interval_override_request.py)<a id="requestbody-forecastoverridesbulkcreateprojectedsalesintervaloverriderequest7_shifts_python_sdktypeforecast_overrides_bulk_create_projected_sales_interval_override_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}/forecast_overrides_intervals` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.forecast_overrides.create_daily_projected_forecast_override`<a id="client7shiftsforecast_overridescreate_daily_projected_forecast_override"></a>

Create Daily Projected Forecast Override

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_daily_projected_forecast_override_response = client7shifts.forecast_overrides.create_daily_projected_forecast_override(
    date="2020-01-01",
    value=1234,
    report_type="sales",
    company_id=1,
    location_id=1,
    department_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `date`<a id="date-date"></a>

The date of the daily report data to override. Format YYYY-MM-DD

##### value: `int`<a id="value-int"></a>

Override value. Currency values in cents

##### report_type: `str`<a id="report_type-str"></a>

Type of value to override. Default is sales

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `Optional[int]`<a id="department_id-optionalint"></a>

Department ID. Optional

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ForecastOverridesCreateDailyProjectedForecastOverrideRequest`](./7_shifts_python_sdk/type/forecast_overrides_create_daily_projected_forecast_override_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ForecastOverridesCreateDailyProjectedForecastOverrideResponse`](./7_shifts_python_sdk/pydantic/forecast_overrides_create_daily_projected_forecast_override_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/location/{location_id}/forecast_override` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.forecast_overrides.override_interval`<a id="client7shiftsforecast_overridesoverride_interval"></a>

Overrides the project sales interval of 15 minutes or 1 hour.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.forecast_overrides.override_interval(
    start="2020-12-30T20:00:00Z",
    end="2020-12-30T20:15:00Z",
    value=1234,
    company_id=1,
    location_id=1,
    department_id=1,
    report_type="sales",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start: `datetime`<a id="start-datetime"></a>

Starting date/time (UTC) of the interval for which you wish to update the sales projection.

##### end: `datetime`<a id="end-datetime"></a>

Ending date/time (UTC) of the interval for which you wish to update the sales projection.

##### value: `int`<a id="value-int"></a>

Override value. Currency value in cents. Only whole dollars are accepted.

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `Optional[int]`<a id="department_id-optionalint"></a>

Department ID

##### report_type: `str`<a id="report_type-str"></a>

Type of value to override. Default is sales

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ForecastOverridesOverrideIntervalRequest`](./7_shifts_python_sdk/type/forecast_overrides_override_interval_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}/forecast_override_interval` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.forecast_overrides.sync_projected_forecast_override`<a id="client7shiftsforecast_overridessync_projected_forecast_override"></a>

Sync Daily Projected Forecast Override

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.forecast_overrides.sync_projected_forecast_override(
    start_date="2020-01-01",
    report_type="sales",
    company_id=1,
    location_id=1,
    end_date="2020-01-01",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `date`<a id="start_date-date"></a>

The start date of the date range of override data to remove. Override data will be removed from only this date if no end date is provided. Format YYYY-MM-DD

##### report_type: `str`<a id="report_type-str"></a>

Type of override data to remove

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### end_date: `Optional[date]`<a id="end_date-optionaldate"></a>

The ending date of a date range of override data to remove. Optional. Format YYYY-MM-DD

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ForecastOverridesSyncProjectedForecastOverrideRequest`](./7_shifts_python_sdk/type/forecast_overrides_sync_projected_forecast_override_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/location/{location_id}/forecast_override` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.forecast_overrides.sync_projected_sales_interval`<a id="client7shiftsforecast_overridessync_projected_sales_interval"></a>

Syncs the overridden project sales interval of 15 minutes or 1 hour.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.forecast_overrides.sync_projected_sales_interval(
    start="2020-12-30T20:00:00Z",
    end="2020-12-30T20:15:00Z",
    company_id=1,
    location_id=1,
    report_type="sales",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start: `datetime`<a id="start-datetime"></a>

Starting date/time (UTC) of the interval for which you wish to update the sales projection.

##### end: `datetime`<a id="end-datetime"></a>

Ending date/time (UTC) of the interval for which you wish to update the sales projection.

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### report_type: `str`<a id="report_type-str"></a>

Type of value to override. Default is sales

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ForecastOverridesSyncProjectedSalesIntervalRequest`](./7_shifts_python_sdk/type/forecast_overrides_sync_projected_sales_interval_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}/forecast_override_interval` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.integration_mappings.create_sales_category_mappings_bulk`<a id="client7shiftsintegration_mappingscreate_sales_category_mappings_bulk"></a>

Create Sales Category Mappings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_sales_category_mappings_bulk_response = client7shifts.integration_mappings.create_sales_category_mappings_bulk(
    body=[
        {
            "external_category_id": "external_category_id_example",
        }
    ],
    company_id=1,
    location_id=1,
    department_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### requestBody: [`IntegrationMappingsCreateSalesCategoryMappingsBulkRequest`](./7_shifts_python_sdk/type/integration_mappings_create_sales_category_mappings_bulk_request.py)<a id="requestbody-integrationmappingscreatesalescategorymappingsbulkrequest7_shifts_python_sdktypeintegration_mappings_create_sales_category_mappings_bulk_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationMappingsCreateSalesCategoryMappingsBulkResponse`](./7_shifts_python_sdk/pydantic/integration_mappings_create_sales_category_mappings_bulk_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/location/{location_id}/sales_category_mappings_bulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.integration_mappings.delete_sales_category_mappings`<a id="client7shiftsintegration_mappingsdelete_sales_category_mappings"></a>

Delete Sales Category Mappings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.integration_mappings.delete_sales_category_mappings(
    company_id=1,
    location_id=1,
    external_id="external_id_example",
    department_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### external_id: `str`<a id="external_id-str"></a>

External Category ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/location/{location_id}/sales_category_mappings/{external_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.integration_mappings.list_sales_category_mappings`<a id="client7shiftsintegration_mappingslist_sales_category_mappings"></a>

List Sales Category Mappings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sales_category_mappings_response = client7shifts.integration_mappings.list_sales_category_mappings(
    company_id=1,
    location_id=1,
    department_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationMappingsListSalesCategoryMappingsResponse`](./7_shifts_python_sdk/pydantic/integration_mappings_list_sales_category_mappings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/location/{location_id}/sales_category_mappings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.locations.create`<a id="client7shiftslocationscreate"></a>

Create Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = client7shifts.locations.create(
    name="Quackers",
    country="CA",
    company_id=1234,
    formatted_address="701 Broadway Ave #200, MadeUpCity, SK SVN 1C3, Canada",
    state="true",
    city="Toronto",
    latitude="string_example",
    longitude="string_example",
    place_id="string_example",
    timezone="America/Chicago",
    holiday_pay=False,
    sun_hours_close="57030",
    mon_hours_close="57030",
    tue_hours_close="57030",
    wed_hours_close="57030",
    thu_hours_close="57030",
    fri_hours_close="57030",
    sat_hours_close="57030",
    sun_hours_open="57030",
    mon_hours_open="57030",
    tue_hours_open="57030",
    wed_hours_open="57030",
    thu_hours_open="57030",
    fri_hours_open="57030",
    sat_hours_open="57030",
    sun_is_closed=True,
    mon_is_closed=True,
    tue_is_closed=True,
    wed_is_closed=True,
    thu_is_closed=True,
    fri_is_closed=True,
    sat_is_closed=True,
    enable_shift_feedback=True,
    shift_feedback=True,
    coupon="Quakers",
    stripe_token_id="tok_1KG8LT2eZvKYlo2CODSv0IXB",
    copy_from_id=123,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Location name

##### country: `str`<a id="country-str"></a>

Country two letter abbreviation

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### formatted_address: `str`<a id="formatted_address-str"></a>

Full address

##### state: `Optional[str]`<a id="state-optionalstr"></a>

State or province

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City

##### latitude: `str`<a id="latitude-str"></a>

locations latitude coordinates

##### longitude: `str`<a id="longitude-str"></a>

locations longitude coordinates

##### place_id: `str`<a id="place_id-str"></a>

Google Places location Id

##### timezone: `str`<a id="timezone-str"></a>

Timezone. Valid zone info name

##### holiday_pay: `bool`<a id="holiday_pay-bool"></a>

When true, holiday pay is enabled

##### sun_hours_close: `str`<a id="sun_hours_close-str"></a>

Sunday closing time

##### mon_hours_close: `str`<a id="mon_hours_close-str"></a>

Monday closing time

##### tue_hours_close: `str`<a id="tue_hours_close-str"></a>

Tuesday closing time

##### wed_hours_close: `str`<a id="wed_hours_close-str"></a>

Wednesday closing time

##### thu_hours_close: `str`<a id="thu_hours_close-str"></a>

Thursday closing time

##### fri_hours_close: `str`<a id="fri_hours_close-str"></a>

Friday closing time

##### sat_hours_close: `str`<a id="sat_hours_close-str"></a>

Saturday closing time

##### sun_hours_open: `str`<a id="sun_hours_open-str"></a>

Sunday opening time

##### mon_hours_open: `Optional[str]`<a id="mon_hours_open-optionalstr"></a>

Monday opening time

##### tue_hours_open: `Optional[str]`<a id="tue_hours_open-optionalstr"></a>

Tuesday opening time

##### wed_hours_open: `Optional[str]`<a id="wed_hours_open-optionalstr"></a>

Wednesday opening time

##### thu_hours_open: `Optional[str]`<a id="thu_hours_open-optionalstr"></a>

Thursday opening time

##### fri_hours_open: `Optional[str]`<a id="fri_hours_open-optionalstr"></a>

Friday opening time

##### sat_hours_open: `Optional[str]`<a id="sat_hours_open-optionalstr"></a>

Saturday opening time

##### sun_is_closed: `Optional[bool]`<a id="sun_is_closed-optionalbool"></a>

If true, location is closed on Sunday

##### mon_is_closed: `Optional[bool]`<a id="mon_is_closed-optionalbool"></a>

If true, location is closed on Monday

##### tue_is_closed: `Optional[bool]`<a id="tue_is_closed-optionalbool"></a>

If true, location is closed on Tuesday

##### wed_is_closed: `Optional[bool]`<a id="wed_is_closed-optionalbool"></a>

If true, location is closed on Wednesday

##### thu_is_closed: `Optional[bool]`<a id="thu_is_closed-optionalbool"></a>

If true, location is closed on Thursday

##### fri_is_closed: `Optional[bool]`<a id="fri_is_closed-optionalbool"></a>

If true, location is closed on Friday

##### sat_is_closed: `Optional[bool]`<a id="sat_is_closed-optionalbool"></a>

If true, location is closed on Saturday

##### enable_shift_feedback: `bool`<a id="enable_shift_feedback-bool"></a>

If true end of shift feedback requests are enabled

##### shift_feedback: `bool`<a id="shift_feedback-bool"></a>

If true end of shift feedback requests are enabled

##### coupon: `Optional[str]`<a id="coupon-optionalstr"></a>

Optional coupon to apply to this location's billing

##### stripe_token_id: `str`<a id="stripe_token_id-str"></a>

Optional stripe payment token. If this is not provided, the account's default payment information will be used.

##### copy_from_id: `Optional[int]`<a id="copy_from_id-optionalint"></a>

Optional existing location id whose department and role structure the new location should copy

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsCreateRequest`](./7_shifts_python_sdk/type/locations_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LocationsCreateResponse`](./7_shifts_python_sdk/pydantic/locations_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.locations.get_location`<a id="client7shiftslocationsget_location"></a>

Retrieve Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_location_response = client7shifts.locations.get_location(
    company_id=1234,
    location_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetLocationResponse`](./7_shifts_python_sdk/pydantic/locations_get_location_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.locations.list_get`<a id="client7shiftslocationslist_get"></a>

List Locations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_get_response = client7shifts.locations.list_get(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    modified_since="2020-01-01",
    deleted=False,
    cursor="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### modified_since: `str`<a id="modified_since-str"></a>

Return locations that have been modified since the specified date. Format YYYY-MM-DD

##### deleted: `bool`<a id="deleted-bool"></a>

When TRUE the search will return deleted locations

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsListGetResponse`](./7_shifts_python_sdk/pydantic/locations_list_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.locations.remove_location_by_id`<a id="client7shiftslocationsremove_location_by_id"></a>

Delete Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.locations.remove_location_by_id(
    company_id=1234,
    location_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.locations.update_location_by_id`<a id="client7shiftslocationsupdate_location_by_id"></a>

Update Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_location_by_id_response = client7shifts.locations.update_location_by_id(
    company_id=1234,
    location_id=1234,
    name="Quackers",
    city="Toronto",
    country="CA",
    state="true",
    shift_feedback=True,
    formatted_address="200 Bathurst Street, Toronto, ON, Canada",
    lat=43.6478436,
    lng=-79.4043708,
    place_id="ChIJUyrhFOc0K4gRyuFq6AUlfmE",
    timezone="America/Chicago",
    hash="string_example",
    department_based_budget=False,
    holiday_pay=False,
    auto_send_log_book_time="57030",
    sun_hours_close="57030",
    mon_hours_close="57030",
    tue_hours_close="57030",
    wed_hours_close="57030",
    thu_hours_close="57030",
    fri_hours_close="57030",
    sat_hours_close="57030",
    sun_hours_open="57030",
    mon_hours_open="57030",
    tue_hours_open="57030",
    wed_hours_open="57030",
    thu_hours_open="57030",
    fri_hours_open="57030",
    sat_hours_open="57030",
    sun_is_closed=True,
    mon_is_closed=True,
    tue_is_closed=True,
    wed_is_closed=True,
    thu_is_closed=True,
    fri_is_closed=True,
    sat_is_closed=True,
    message="msg",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### name: `str`<a id="name-str"></a>

Location name

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City

##### country: `str`<a id="country-str"></a>

Country

##### state: `Optional[str]`<a id="state-optionalstr"></a>

State or province

##### shift_feedback: `bool`<a id="shift_feedback-bool"></a>

If true end of shift feedback requests are enabled

##### formatted_address: `str`<a id="formatted_address-str"></a>

##### lat: `Union[int, float]`<a id="lat-unionint-float"></a>

##### lng: `Union[int, float]`<a id="lng-unionint-float"></a>

##### place_id: `Optional[str]`<a id="place_id-optionalstr"></a>

##### timezone: `str`<a id="timezone-str"></a>

Timezone. Valid zone info name

##### hash: `str`<a id="hash-str"></a>

##### department_based_budget: `bool`<a id="department_based_budget-bool"></a>

##### holiday_pay: `Optional[bool]`<a id="holiday_pay-optionalbool"></a>

When true, holiday pay is enabled

##### auto_send_log_book_time: `str`<a id="auto_send_log_book_time-str"></a>

A timestamp with hh:mm:ss format

##### sun_hours_close: `Optional[str]`<a id="sun_hours_close-optionalstr"></a>

Sunday closing time

##### mon_hours_close: `Optional[str]`<a id="mon_hours_close-optionalstr"></a>

Monday closing time

##### tue_hours_close: `Optional[str]`<a id="tue_hours_close-optionalstr"></a>

Tuesday closing time

##### wed_hours_close: `Optional[str]`<a id="wed_hours_close-optionalstr"></a>

Wednesday closing time

##### thu_hours_close: `Optional[str]`<a id="thu_hours_close-optionalstr"></a>

Thursday closing time

##### fri_hours_close: `Optional[str]`<a id="fri_hours_close-optionalstr"></a>

Friday closing time

##### sat_hours_close: `Optional[str]`<a id="sat_hours_close-optionalstr"></a>

Saturday closing time

##### sun_hours_open: `Optional[str]`<a id="sun_hours_open-optionalstr"></a>

Sunday opening time

##### mon_hours_open: `Optional[str]`<a id="mon_hours_open-optionalstr"></a>

Monday opening time

##### tue_hours_open: `Optional[str]`<a id="tue_hours_open-optionalstr"></a>

Tuesday opening time

##### wed_hours_open: `Optional[str]`<a id="wed_hours_open-optionalstr"></a>

Wednesday opening time

##### thu_hours_open: `Optional[str]`<a id="thu_hours_open-optionalstr"></a>

Thursday opening time

##### fri_hours_open: `Optional[str]`<a id="fri_hours_open-optionalstr"></a>

Friday opening time

##### sat_hours_open: `Optional[str]`<a id="sat_hours_open-optionalstr"></a>

Saturday opening time

##### sun_is_closed: `Optional[bool]`<a id="sun_is_closed-optionalbool"></a>

If true, location is closed on Sunday

##### mon_is_closed: `Optional[bool]`<a id="mon_is_closed-optionalbool"></a>

If true, location is closed on Monday

##### tue_is_closed: `Optional[bool]`<a id="tue_is_closed-optionalbool"></a>

If true, location is closed on Tuesday

##### wed_is_closed: `Optional[bool]`<a id="wed_is_closed-optionalbool"></a>

If true, location is closed on Wednesday

##### thu_is_closed: `Optional[bool]`<a id="thu_is_closed-optionalbool"></a>

If true, location is closed on Thursday

##### fri_is_closed: `Optional[bool]`<a id="fri_is_closed-optionalbool"></a>

If true, location is closed on Friday

##### sat_is_closed: `Optional[bool]`<a id="sat_is_closed-optionalbool"></a>

If true, location is closed on Saturday

##### message: `str`<a id="message-str"></a>

Message visible to all employees

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LocationsUpdateLocationByIdRequest`](./7_shifts_python_sdk/type/locations_update_location_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LocationsUpdateLocationByIdResponse`](./7_shifts_python_sdk/pydantic/locations_update_location_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.create_category`<a id="client7shiftslog_bookcreate_category"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_category_response = client7shifts.log_book.create_category(
    name="string_example",
    company_id=1,
    col=1,
    sort=1,
    field_type="dollar",
    notify=True,
    required=True,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### col: `int`<a id="col-int"></a>

##### sort: `int`<a id="sort-int"></a>

##### field_type: `str`<a id="field_type-str"></a>

##### notify: `bool`<a id="notify-bool"></a>

##### required: `bool`<a id="required-bool"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LogBookCreateCategoryRequest`](./7_shifts_python_sdk/type/log_book_create_category_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LogBookCreateCategoryResponse`](./7_shifts_python_sdk/pydantic/log_book_create_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_categories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.create_comment`<a id="client7shiftslog_bookcreate_comment"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_comment_response = client7shifts.log_book.create_comment(
    log_book_id=1,
    message="a",
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### log_book_id: `int`<a id="log_book_id-int"></a>

##### message: `str`<a id="message-str"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LogBookCreateCommentRequest`](./7_shifts_python_sdk/type/log_book_create_comment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LogBookCreateCommentResponse`](./7_shifts_python_sdk/pydantic/log_book_create_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.create_post`<a id="client7shiftslog_bookcreate_post"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_post_response = client7shifts.log_book.create_post(
    location_id=1,
    log_book_category_id=1,
    date="2020-01-01",
    message="a",
    company_id=1,
    attachments=[
        {
            "file_name": "file_name_example",
            "file_content": "file_content_example",
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `int`<a id="location_id-int"></a>

##### log_book_category_id: `int`<a id="log_book_category_id-int"></a>

##### date: `str`<a id="date-str"></a>

The posted date. Format YYYY-MM-DD

##### message: `str`<a id="message-str"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### attachments: [`LogBookCreatePostRequestAttachments`](./7_shifts_python_sdk/type/log_book_create_post_request_attachments.py)<a id="attachments-logbookcreatepostrequestattachments7_shifts_python_sdktypelog_book_create_post_request_attachmentspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LogBookCreatePostRequest`](./7_shifts_python_sdk/type/log_book_create_post_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LogBookCreatePostResponse`](./7_shifts_python_sdk/pydantic/log_book_create_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_posts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.delete_category_by_id`<a id="client7shiftslog_bookdelete_category_by_id"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.log_book.delete_category_by_id(
    company_id=1,
    id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `int`<a id="id-int"></a>

Category ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_categories/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.delete_comment`<a id="client7shiftslog_bookdelete_comment"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.log_book.delete_comment(
    company_id=1,
    id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `int`<a id="id-int"></a>

Log Book Comment ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_comments/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.delete_post`<a id="client7shiftslog_bookdelete_post"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.log_book.delete_post(
    company_id=1,
    id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `int`<a id="id-int"></a>

Log Book Post ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_posts/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.get_comment`<a id="client7shiftslog_bookget_comment"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_comment_response = client7shifts.log_book.get_comment(
    company_id=1,
    id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `int`<a id="id-int"></a>

Log Book Comment ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`LogBookGetCommentResponse`](./7_shifts_python_sdk/pydantic/log_book_get_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_comments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.get_post`<a id="client7shiftslog_bookget_post"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_post_response = client7shifts.log_book.get_post(
    company_id=1,
    id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `int`<a id="id-int"></a>

Log Book Post ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`LogBookGetPostResponse`](./7_shifts_python_sdk/pydantic/log_book_get_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_posts/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.list_categories`<a id="client7shiftslog_booklist_categories"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_categories_response = client7shifts.log_book.list_categories(
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`LogBookListCategoriesResponse`](./7_shifts_python_sdk/pydantic/log_book_list_categories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.list_comments`<a id="client7shiftslog_booklist_comments"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_comments_response = client7shifts.log_book.list_comments(
    company_id=1,
    log_book_ids=[
        123,321
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### log_book_ids: List[`int`]<a id="log_book_ids-listint"></a>

Log book post id associated with log book comments

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`LogBookListCommentsResponse`](./7_shifts_python_sdk/pydantic/log_book_list_comments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.list_posts`<a id="client7shiftslog_booklist_posts"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_posts_response = client7shifts.log_book.list_posts(
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
    log_book_category_id=1,
    user_id=1,
    date="2020-01-01",
    posted_date_gte="2020-01-01",
    posted_date_lte="2020-01-01",
    message="string_example",
    order_field="date",
    order_dir="asc",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### log_book_category_id: `int`<a id="log_book_category_id-int"></a>

Log Book Category ID

##### user_id: `int`<a id="user_id-int"></a>

Post Author User ID

##### date: `str`<a id="date-str"></a>

Date of log book creation, format YYYY-MM-DD

##### posted_date_gte: `str`<a id="posted_date_gte-str"></a>

List only log book posts from dates inclusive after, format YYYY-MM-DD

##### posted_date_lte: `str`<a id="posted_date_lte-str"></a>

List only log book posts from dates inclusive before, format YYYY-MM-DD

##### message: `str`<a id="message-str"></a>

List only posts containing the message

##### order_field: `str`<a id="order_field-str"></a>

Order listed log book posts by a field

##### order_dir: `str`<a id="order_dir-str"></a>

Specified direction to order listed log book posts

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`LogBookListPostsResponse`](./7_shifts_python_sdk/pydantic/log_book_list_posts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_posts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.log_book.update_category_by_id`<a id="client7shiftslog_bookupdate_category_by_id"></a>

Beta

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_category_by_id_response = client7shifts.log_book.update_category_by_id(
    company_id=1,
    id=1,
    name="string_example",
    col=1,
    sort=1,
    field_type="dollar",
    notify=True,
    required=True,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `int`<a id="id-int"></a>

Category ID

##### name: `str`<a id="name-str"></a>

##### col: `int`<a id="col-int"></a>

##### sort: `int`<a id="sort-int"></a>

##### field_type: `str`<a id="field_type-str"></a>

##### notify: `bool`<a id="notify-bool"></a>

##### required: `bool`<a id="required-bool"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LogBookUpdateCategoryByIdRequest`](./7_shifts_python_sdk/type/log_book_update_category_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LogBookUpdateCategoryByIdResponse`](./7_shifts_python_sdk/pydantic/log_book_update_category_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/log_book_categories/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.receipts.create_receipt`<a id="client7shiftsreceiptscreate_receipt"></a>

Create Receipt

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_receipt_response = client7shifts.receipts.create_receipt(
    company_id=1,
    location_id=1,
    receipt_date="2021-01-01T00:00:00.000Z",
    net_total=1,
    gross_total=1,
    total_receipt_discounts=0,
    tips=1,
    external_user_id="string_example",
    revenue_center="string_example",
    receipt_lines=[
        {
            "external_item_id": "external_item_id_example",
            "external_category_ids": [
                "external_category_ids_example"
            ],
            "quantity": 1,
            "price": 1,
            "gross_item_price": 1,
            "net_item_price": 1,
            "item_discount": 0,
            "status": "open",
        }
    ],
    tip_details=[
        {
            "type": "cc",
            "value": 500,
        }
    ],
    status="open",
    order_type="dine_in",
    dining_option="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

The 7shifts location_id this receipt belongs to

##### receipt_date: `datetime`<a id="receipt_date-datetime"></a>

Receipt create date time. UTC date time in ISO8601 format

##### net_total: `int`<a id="net_total-int"></a>

The net total of the receipt pre tax, post-discounts, pre tips. In cents

##### gross_total: `Optional[int]`<a id="gross_total-optionalint"></a>

The gross total of the receipt in cents

##### total_receipt_discounts: `Optional[int]`<a id="total_receipt_discounts-optionalint"></a>

The total discounts of the receipt in cents

##### tips: `Optional[int]`<a id="tips-optionalint"></a>

Total tips in cents

##### external_user_id: `Optional[str]`<a id="external_user_id-optionalstr"></a>

External user ID of the sales receipt in your system (must be unique per 7shifts location).

##### revenue_center: `Optional[str]`<a id="revenue_center-optionalstr"></a>

Label for the revenue centre for the receipt

##### receipt_lines: List[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="receipt_lines-listdictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Receipt line items

##### tip_details: List[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="tip_details-listdictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Tip line items

##### status: `str`<a id="status-str"></a>

Status of the receipt

##### order_type: `Optional[str]`<a id="order_type-optionalstr"></a>

Order type

##### dining_option: `Optional[str]`<a id="dining_option-optionalstr"></a>

Dining option

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReceiptsCreateReceiptRequest`](./7_shifts_python_sdk/type/receipts_create_receipt_request.py)
Receipt

#### 🔄 Return<a id="🔄-return"></a>

[`ReceiptsCreateReceiptResponse`](./7_shifts_python_sdk/pydantic/receipts_create_receipt_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/receipts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.receipts.get_receipt`<a id="client7shiftsreceiptsget_receipt"></a>

Retrieve Receipt

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_receipt_response = client7shifts.receipts.get_receipt(
    company_id=1,
    receipt_id="receipt_id_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### receipt_id: `str`<a id="receipt_id-str"></a>

Receipt UUID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`ReceiptsGetReceiptResponse`](./7_shifts_python_sdk/pydantic/receipts_get_receipt_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/receipts/{receipt_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.receipts.get_summary`<a id="client7shiftsreceiptsget_summary"></a>

Retrieve Receipts Summary

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_summary_response = client7shifts.receipts.get_summary(
    company_id=1234,
    location_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    receipt_date_gte="2022-01-01",
    receipt_date_lte="2022-01-01",
    modified_since="2022-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### receipt_date_gte: `datetime`<a id="receipt_date_gte-datetime"></a>

Return receipts that were created on or after a specific date. Limit to 31-day range with receipt_date[lte].

##### receipt_date_lte: `datetime`<a id="receipt_date_lte-datetime"></a>

Return receipts that were created on or before a specific date. Limit to 31-day range with receipt_date[gte].

##### modified_since: `datetime`<a id="modified_since-datetime"></a>

Return receipts that were modified on or after a specific date. Limited to past 30 days.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceiptsGetSummaryResponse`](./7_shifts_python_sdk/pydantic/receipts_get_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/receipts_summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.receipts.list`<a id="client7shiftsreceiptslist"></a>

List Receipts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.receipts.list(
    company_id=1234,
    location_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    receipt_date_gte="2022-01-01",
    receipt_date_lte="2022-01-01",
    modified_since="2022-01-01",
    status="open",
    external_user_id="ABC123",
    cursor="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### receipt_date_gte: `datetime`<a id="receipt_date_gte-datetime"></a>

Return receipts that were created on or after a specific date

##### receipt_date_lte: `datetime`<a id="receipt_date_lte-datetime"></a>

Return receipts that were created on or before a specific date

##### modified_since: `datetime`<a id="modified_since-datetime"></a>

Return receipts that were modified on or after a specific date

##### status: `str`<a id="status-str"></a>

Filter receipts by status type

##### external_user_id: `str`<a id="external_user_id-str"></a>

Filter receipts by external user id

##### cursor: `str`<a id="cursor-str"></a>

An opaque cursor for the next or previous result set.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceiptsListResponse`](./7_shifts_python_sdk/pydantic/receipts_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/receipts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.receipts.update_receipt`<a id="client7shiftsreceiptsupdate_receipt"></a>

Update Receipt

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_receipt_response = client7shifts.receipts.update_receipt(
    net_total=1,
    company_id=1,
    receipt_id="ext:7890:rec_8522451",
    receipt_date="2021-01-01T00:00:00.000Z",
    gross_total=1,
    total_receipt_discounts=0,
    tips=1,
    external_user_id="string_example",
    revenue_center="string_example",
    receipt_lines=[
        {
            "external_item_id": "external_item_id_example",
            "external_category_ids": [
                "external_category_ids_example"
            ],
            "quantity": 1,
            "price": 1,
            "gross_item_price": 1,
            "net_item_price": 1,
            "item_discount": 0,
            "status": "open",
        }
    ],
    tip_details=[
        {
            "type": "cc",
            "value": 500,
        }
    ],
    status="open",
    order_type="dine_in",
    dining_option="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### net_total: `int`<a id="net_total-int"></a>

The net total of the receipt pre tax, post-discounts, pre tips. In cents

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### receipt_id: `str`<a id="receipt_id-str"></a>

Receipt ID.  Either 7shifts receipt UUID or a combination of the External ID of the sales receipt in your system and a Location ID. External ID's must start with 'ext:' and the format is ext:location_id:receipt_id.

##### receipt_date: `datetime`<a id="receipt_date-datetime"></a>

Receipt create date time. UTC date time in ISO8601 format

##### gross_total: `int`<a id="gross_total-int"></a>

The gross total of the receipt in cents

##### total_receipt_discounts: `int`<a id="total_receipt_discounts-int"></a>

The total discounts of the receipt in cents

##### tips: `int`<a id="tips-int"></a>

Total tips in cents

##### external_user_id: `str`<a id="external_user_id-str"></a>

External user ID of the sales receipt in your system (must be unique per 7shifts location).

##### revenue_center: `str`<a id="revenue_center-str"></a>

Label for the revenue center for the receipt

##### receipt_lines: [`ReceiptsUpdateReceiptRequestReceiptLines`](./7_shifts_python_sdk/type/receipts_update_receipt_request_receipt_lines.py)<a id="receipt_lines-receiptsupdatereceiptrequestreceiptlines7_shifts_python_sdktypereceipts_update_receipt_request_receipt_linespy"></a>

##### tip_details: [`ReceiptsUpdateReceiptRequestTipDetails`](./7_shifts_python_sdk/type/receipts_update_receipt_request_tip_details.py)<a id="tip_details-receiptsupdatereceiptrequesttipdetails7_shifts_python_sdktypereceipts_update_receipt_request_tip_detailspy"></a>

##### status: `str`<a id="status-str"></a>

Status of the receipt

##### order_type: `str`<a id="order_type-str"></a>

Order type

##### dining_option: `str`<a id="dining_option-str"></a>

Dining option

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReceiptsUpdateReceiptRequest`](./7_shifts_python_sdk/type/receipts_update_receipt_request.py)
Receipt

#### 🔄 Return<a id="🔄-return"></a>

[`ReceiptsUpdateReceiptResponse`](./7_shifts_python_sdk/pydantic/receipts_update_receipt_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/receipts/{receipt_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.reports.get_daily_sales_and_labor`<a id="client7shiftsreportsget_daily_sales_and_labor"></a>

Retrieve Daily Sales & Labor

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_daily_sales_and_labor_response = client7shifts.reports.get_daily_sales_and_labor(
    start_date="2019-12-01",
    end_date="2019-12-01",
    location_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    department_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `str`<a id="start_date-str"></a>

Starting date for which you want the daily sales and labor data for.

##### end_date: `str`<a id="end_date-str"></a>

Ending date for which you want the daily sales and labor data for.

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetDailySalesAndLaborResponse`](./7_shifts_python_sdk/pydantic/reports_get_daily_sales_and_labor_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/reports/daily_sales_and_labor` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.reports.get_daily_stats`<a id="client7shiftsreportsget_daily_stats"></a>

Retrieve Daily Stats

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_daily_stats_response = client7shifts.reports.get_daily_stats(
    company_id=1234,
    location_id=1,
    date="1970-01-01",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    department_id=1,
    include_future=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### date: `date`<a id="date-date"></a>

Date

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### include_future: `bool`<a id="include_future-bool"></a>

include future

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetDailyStatsResponse`](./7_shifts_python_sdk/pydantic/reports_get_daily_stats_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v2/company/{company_id}/location/{location_id}/daily_stats` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.reports.get_worked_hours_wages`<a id="client7shiftsreportsget_worked_hours_wages"></a>

Retrieve Worked Hours & Wages

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_worked_hours_wages_response = client7shifts.reports.get_worked_hours_wages(
    punches=True,
    company_id=1,
    _from="2019-12-01",
    to="2019-12-01",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1234,
    department_id=1234,
    role_id=1234,
    user_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### punches: `bool`<a id="punches-bool"></a>

Whether or not to use the punch labour source

##### company_id: `int`<a id="company_id-int"></a>

The company id to pull the report for.

##### _from: `str`<a id="_from-str"></a>

Starting date for which you want the report to start.

##### to: `str`<a id="to-str"></a>

Ending date for which you want the report to end.

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

The location id for which you want the report for.

##### department_id: `int`<a id="department_id-int"></a>

The department id for the report.

##### role_id: `int`<a id="role_id-int"></a>

The role id for the report

##### user_id: `int`<a id="user_id-int"></a>

The user id the report should be fetched for - internal use only

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetWorkedHoursWagesResponse`](./7_shifts_python_sdk/pydantic/reports_get_worked_hours_wages_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/reports/hours_and_wages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.roles.create_role`<a id="client7shiftsrolescreate_role"></a>

Create Role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_role_response = client7shifts.roles.create_role(
    name="string_example",
    color="string_example",
    location_id=1,
    department_id=1,
    company_id=1234,
    sort=0,
    job_code="string_example",
    stations=[
        {
            "name": "name_example",
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Role name

##### color: `str`<a id="color-str"></a>

A hex number representing the color

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID. If this role is not assigned to a department, this value will be zero

##### company_id: `int`<a id="company_id-int"></a>

The company id

##### sort: `int`<a id="sort-int"></a>

The order in which the roles will be listed in the web app

##### job_code: `str`<a id="job_code-str"></a>

Job code

##### stations: [`RolesCreateRoleRequestStations`](./7_shifts_python_sdk/type/roles_create_role_request_stations.py)<a id="stations-rolescreaterolerequeststations7_shifts_python_sdktyperoles_create_role_request_stationspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RolesCreateRoleRequest`](./7_shifts_python_sdk/type/roles_create_role_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RolesCreateRoleResponse`](./7_shifts_python_sdk/pydantic/roles_create_role_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/roles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.roles.delete_role`<a id="client7shiftsrolesdelete_role"></a>

Delete Role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.roles.delete_role(
    company_id=1,
    role_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/roles/{role_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.roles.get_role`<a id="client7shiftsrolesget_role"></a>

Retrieve Role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_role_response = client7shifts.roles.get_role(
    company_id=1234,
    role_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`RolesGetRoleResponse`](./7_shifts_python_sdk/pydantic/roles_get_role_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/roles/{role_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.roles.list`<a id="client7shiftsroleslist"></a>

List Roles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.roles.list(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
    department_id=1,
    ids=[
        123,321
    ],
    modified_since="2020-01-01",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### ids: List[`int`]<a id="ids-listint"></a>

Role IDs

##### modified_since: `str`<a id="modified_since-str"></a>

Return roles that have been modified since the specified date. Format YYYY-MM-DD

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`RolesListResponse`](./7_shifts_python_sdk/pydantic/roles_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/roles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.roles.update_role_by_id`<a id="client7shiftsrolesupdate_role_by_id"></a>

Update Role

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_role_by_id_response = client7shifts.roles.update_role_by_id(
    company_id=1234,
    role_id=1234,
    department_id=0,
    sort=0,
    color="76a939",
    name="Bartender",
    job_code="BOH-Bartender",
    stations=[
        {
            "name": "name_example",
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID. If this role is not assigned to a department, this value will be zero

##### sort: `int`<a id="sort-int"></a>

The order in which the roles will be listed in the web app

##### color: `str`<a id="color-str"></a>

A hex number representing the color

##### name: `str`<a id="name-str"></a>

Role name

##### job_code: `str`<a id="job_code-str"></a>

Job code

##### stations: [`RolesUpdateRoleByIdRequestStations`](./7_shifts_python_sdk/type/roles_update_role_by_id_request_stations.py)<a id="stations-rolesupdaterolebyidrequeststations7_shifts_python_sdktyperoles_update_role_by_id_request_stationspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RolesUpdateRoleByIdRequest`](./7_shifts_python_sdk/type/roles_update_role_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RolesUpdateRoleByIdResponse`](./7_shifts_python_sdk/pydantic/roles_update_role_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/roles/{role_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.schedule_enforcement.list_scheduled_shifts`<a id="client7shiftsschedule_enforcementlist_scheduled_shifts"></a>

List Scheduled Shifts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_scheduled_shifts_response = client7shifts.schedule_enforcement.list_scheduled_shifts(
    company_id=1234,
    id="punch_id:003184",
    location_id=5,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    grace_period=5,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### id: `str`<a id="id-str"></a>

Specified user_id of the user to check if scheduled. If the value begins with punch_id: then this specifies a user punch_id.

##### location_id: `int`<a id="location_id-int"></a>

Location ID.

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### grace_period: `int`<a id="grace_period-int"></a>

Grace period in minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleEnforcementListScheduledShiftsResponse`](./7_shifts_python_sdk/pydantic/schedule_enforcement_list_scheduled_shifts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shifts_scheduled/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.schedule_events.create_event`<a id="client7shiftsschedule_eventscreate_event"></a>

Create Event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_event_response = client7shifts.schedule_events.create_event(
    title="string_example",
    location_ids=[
        1
    ],
    start_date="2019-01-01",
    start_time="09:00:00",
    end_date="2019-01-02",
    end_time="61200",
    is_multi_day=True,
    company_id=1234,
    description="string_example",
    color="5ea17c",
    recurrence="Daily for 10 occurrences ==> (1997 9:00 AM EDT) September 2-11 DTSTART;TZID=America/New_York:19970902T090000 RRULE:FREQ=DAILY;COUNT=10",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The name of the event

##### location_ids: [`ScheduleEventsCreateEventRequestLocationIds`](./7_shifts_python_sdk/type/schedule_events_create_event_request_location_ids.py)<a id="location_ids-scheduleeventscreateeventrequestlocationids7_shifts_python_sdktypeschedule_events_create_event_request_location_idspy"></a>

##### start_date: `str`<a id="start_date-str"></a>

Start date

##### start_time: `str`<a id="start_time-str"></a>

Start time

##### end_date: `str`<a id="end_date-str"></a>

End date for multi-day events

##### end_time: `str`<a id="end_time-str"></a>

End time

##### is_multi_day: `bool`<a id="is_multi_day-bool"></a>

If true, the event is a multi-day event

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Description for event

##### color: `Optional[str]`<a id="color-optionalstr"></a>

A hex number representing the color

##### recurrence: `Optional[str]`<a id="recurrence-optionalstr"></a>

Recurrence rules as defined by the RFC 5545 spec

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ScheduleEventsCreateEventRequest`](./7_shifts_python_sdk/type/schedule_events_create_event_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleEventsCreateEventResponse`](./7_shifts_python_sdk/pydantic/schedule_events_create_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/events` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.schedule_events.delete_event`<a id="client7shiftsschedule_eventsdelete_event"></a>

Delete Event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_event_response = client7shifts.schedule_events.delete_event(
    company_id=1234,
    event_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    recurrence_target="[\"THIS\",\"THIS_AND_FUTURE\"]",
    start_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### event_id: `int`<a id="event_id-int"></a>

Event ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### recurrence_target: `str`<a id="recurrence_target-str"></a>

Recurrence Target

##### start_date: `str`<a id="start_date-str"></a>

Start of the targeted range for recurrence. Format YYYY-MM-DD HH:MM:SS

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleEventsDeleteEventResponse`](./7_shifts_python_sdk/pydantic/schedule_events_delete_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/events/{event_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.schedule_events.get_event_by_id`<a id="client7shiftsschedule_eventsget_event_by_id"></a>

Retrieve Event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_by_id_response = client7shifts.schedule_events.get_event_by_id(
    company_id=1234,
    event_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### event_id: `int`<a id="event_id-int"></a>

Event ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleEventsGetEventByIdResponse`](./7_shifts_python_sdk/pydantic/schedule_events_get_event_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/events/{event_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.schedule_events.list_events`<a id="client7shiftsschedule_eventslist_events"></a>

List Events

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_events_response = client7shifts.schedule_events.list_events(
    company_id=1234,
    start_date="2020-02-02",
    end_date="2020-02-08",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### start_date: `date`<a id="start_date-date"></a>

A date string to request only events within a range.  Format YYYY-MM-DD

##### end_date: `date`<a id="end_date-date"></a>

A date string to request only events within a range.  Format YYYY-MM-DD

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleEventsListEventsResponse`](./7_shifts_python_sdk/pydantic/schedule_events_list_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.schedule_events.update_event_by_id`<a id="client7shiftsschedule_eventsupdate_event_by_id"></a>

Update Event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_event_by_id_response = client7shifts.schedule_events.update_event_by_id(
    body=None,
    company_id=1234,
    event_id=1234,
    title="string_example",
    description="string_example",
    location_ids=[
        1
    ],
    start_date="2019-01-01",
    start_time="09:00:00",
    end_date="2019-01-02",
    end_time="61200",
    color="5ea17c",
    is_multi_day=True,
    recurrence="Daily for 10 occurrences ==> (1997 9:00 AM EDT) September 2-11 DTSTART;TZID=America/New_York:19970902T090000 RRULE:FREQ=DAILY;COUNT=10",
    recurrence_target="THIS",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### event_id: `int`<a id="event_id-int"></a>

Event ID

##### title: `str`<a id="title-str"></a>

The name of the event

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Description for event

##### location_ids: List[`int`]<a id="location_ids-listint"></a>

The list of locations where this event occurs

##### start_date: `str`<a id="start_date-str"></a>

Start date

##### start_time: `str`<a id="start_time-str"></a>

Start time

##### end_date: `str`<a id="end_date-str"></a>

End date for multi-day events

##### end_time: `str`<a id="end_time-str"></a>

End time

##### color: `Optional[str]`<a id="color-optionalstr"></a>

A hex number representing the color

##### is_multi_day: `bool`<a id="is_multi_day-bool"></a>

If true, the event is a multi-day event

##### recurrence: `Optional[str]`<a id="recurrence-optionalstr"></a>

Recurrence rules as defined by the RFC 5545 spec

##### recurrence_target: `Optional[str]`<a id="recurrence_target-optionalstr"></a>

describes which recurring events will be updated

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ScheduleEventsUpdateEventByIdRequest`](./7_shifts_python_sdk/type/schedule_events_update_event_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleEventsUpdateEventByIdResponse`](./7_shifts_python_sdk/pydantic/schedule_events_update_event_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/events/{event_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.shift_feedback.list`<a id="client7shiftsshift_feedbacklist"></a>

List Shift Feedback

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.shift_feedback.list(
    company_id=384,
    start_date="2023-01-01",
    end_date="2023-01-01",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=408,
    user_id=1007790,
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### start_date: `date`<a id="start_date-date"></a>

The start date of the range you want shift feedback for

##### end_date: `date`<a id="end_date-date"></a>

The end date of the range you want shift feedback for (inclusive)

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftFeedbackListResponse`](./7_shifts_python_sdk/pydantic/shift_feedback_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shift_feedback` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.shifts.create_new_shift`<a id="client7shiftsshiftscreate_new_shift"></a>

Create Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_shift_response = client7shifts.shifts.create_new_shift(
    location_id=1,
    start="1970-01-01T00:00:00.00Z",
    end="1970-01-01T00:00:00.00Z",
    company_id=1234,
    user_id=1,
    department_id=1,
    role_id=1,
    station_id=1,
    close=True,
    business_decline=True,
    notes="string_example",
    draft=True,
    notified=True,
    open=True,
    open_offer_type=1,
    unassigned=True,
    unassigned_skill_level=1,
    status=0,
    late_minutes=1,
    breaks=[
        {
            "break_type_id": 1,
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `int`<a id="location_id-int"></a>

Shift ID

##### start: `datetime`<a id="start-datetime"></a>

Start date time of the shift. UTC in ISO8601 format.

##### end: `datetime`<a id="end-datetime"></a>

End date time of the shift. UTC in ISO8601 format.

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### department_id: `Optional[int]`<a id="department_id-optionalint"></a>

Department ID. Required if the location uses departments.

##### role_id: `Optional[int]`<a id="role_id-optionalint"></a>

Role ID. Required if the location uses roles.

##### station_id: `Optional[int]`<a id="station_id-optionalint"></a>

Station ID

##### close: `Optional[bool]`<a id="close-optionalbool"></a>

Set to true if the shift ends at closing time. If set, end is not used.

##### business_decline: `Optional[bool]`<a id="business_decline-optionalbool"></a>

Set to true if the shift ends at business decline.

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes displayed on a shift.

##### draft: `Optional[bool]`<a id="draft-optionalbool"></a>

If true the shift is not published.

##### notified: `Optional[bool]`<a id="notified-optionalbool"></a>

If true the user has been notified of the published shift.

##### open: `Optional[bool]`<a id="open-optionalbool"></a>

Set to true if the shift is not assigned to any user. Open shifts can be requested by users.

##### open_offer_type: `Optional[int]`<a id="open_offer_type-optionalint"></a>

Set when open is true. Set to 1 for everyone can request an open shift; set to 1 if only offered to specified role.

##### unassigned: `Optional[bool]`<a id="unassigned-optionalbool"></a>

Internal use only

##### unassigned_skill_level: `Optional[int]`<a id="unassigned_skill_level-optionalint"></a>

The skill level required for this shift.

##### status: `Optional[int]`<a id="status-optionalint"></a>

Shift status type. 0 - none, 1 - sick, 2 - no show, 3 - late, 4 - call out, 5 - left late.

##### late_minutes: `Optional[int]`<a id="late_minutes-optionalint"></a>

Number of minutes a user can clock in late after the shift starts.

##### breaks: [`ShiftsCreateNewShiftRequestBreaks`](./7_shifts_python_sdk/type/shifts_create_new_shift_request_breaks.py)<a id="breaks-shiftscreatenewshiftrequestbreaks7_shifts_python_sdktypeshifts_create_new_shift_request_breakspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftsCreateNewShiftRequest`](./7_shifts_python_sdk/type/shifts_create_new_shift_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsCreateNewShiftResponse`](./7_shifts_python_sdk/pydantic/shifts_create_new_shift_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shifts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.shifts.delete_shift_by_id`<a id="client7shiftsshiftsdelete_shift_by_id"></a>

Delete Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.shifts.delete_shift_by_id(
    company_id=1,
    shift_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### shift_id: `int`<a id="shift_id-int"></a>

Shift ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shifts/{shift_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.shifts.get_shift_by_id`<a id="client7shiftsshiftsget_shift_by_id"></a>

Retrieve Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_shift_by_id_response = client7shifts.shifts.get_shift_by_id(
    company_id=1,
    shift_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    include_deleted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### shift_id: `int`<a id="shift_id-int"></a>

Shift ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Return the shift even if its deleted

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsGetShiftByIdResponse`](./7_shifts_python_sdk/pydantic/shifts_get_shift_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shifts/{shift_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.shifts.list`<a id="client7shiftsshiftslist"></a>

List Shifts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.shifts.list(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    cursor="string_example",
    limit=100,
    location_id=1234,
    shift_ids=[
        123,231,222
    ],
    department_id=1234,
    department_ids=[
        123,231,222
    ],
    role_id=1234,
    user_id=1234,
    start_lte="2021-01-30T08:30:00Z",
    start_gte="2021-01-30T08:30:00Z",
    end_lte="2021-01-30T08:30:00Z",
    end_gte="2021-01-30T08:30:00Z",
    deleted=False,
    draft=False,
    include_draft=False,
    open=True,
    modified_since="2021-01-30T08:30:00Z",
    sort_by=",iEEpmVvrKlTttzGFqCEGyGBLkBAsBQRJXFH_OJE_CWHioCHFdWvFEDxwNvqMvvkTRU",
    sort_dir=",iEEpmVvrKlTttzGFqCEGyGBLkBAsBQRJXFH_OJE_CWHioCHFdWvFEDxwNvqMvvkTRU",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### shift_ids: List[`int`]<a id="shift_ids-listint"></a>

A comma separated list of Shift IDs

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### department_ids: List[`int`]<a id="department_ids-listint"></a>

Department IDs

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### start_lte: `datetime`<a id="start_lte-datetime"></a>

Return shifts that start before or on specified date. In ISO8601 Format

##### start_gte: `datetime`<a id="start_gte-datetime"></a>

Return shifts that start after or on specified date time. In ISO8601 Format

##### end_lte: `datetime`<a id="end_lte-datetime"></a>

Return shifts that end before or on specified date time. In ISO8601 Format

##### end_gte: `datetime`<a id="end_gte-datetime"></a>

Return shifts that end after or on specified date time. In ISO8601 Format

##### deleted: `bool`<a id="deleted-bool"></a>

Return shifts that were published and have been deleted. Cannot be combined with draft.

##### draft: `bool`<a id="draft-bool"></a>

Return shifts that are in draft. Draft shifts have created, edited or deleted but not been published. Overrides deleted flag.

##### include_draft: `bool`<a id="include_draft-bool"></a>

Return shifts that are published, and also shifts in draft. Overrides deleted flag and draft flag.

##### open: `bool`<a id="open-bool"></a>

Return shifts that are open. Open shifts means anyone can request to take it and not assigned to any individual.

##### modified_since: `datetime`<a id="modified_since-datetime"></a>

Return only shifts that have been modified from specified date time. In ISO8601 Format

##### sort_by: `str`<a id="sort_by-str"></a>

Sort by either start or end

##### sort_dir: `str`<a id="sort_dir-str"></a>

Sort by direction (asc, desc)

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsListResponse`](./7_shifts_python_sdk/pydantic/shifts_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shifts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.shifts.update_shift_by_id`<a id="client7shiftsshiftsupdate_shift_by_id"></a>

Update Shift

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_shift_by_id_response = client7shifts.shifts.update_shift_by_id(
    company_id=1,
    shift_id=1,
    location_id=1,
    user_id=1,
    department_id=1,
    role_id=1,
    station_id=1,
    start="2021-01-01T00:00:00.000Z",
    end="2021-01-01T00:00:00.000Z",
    close=True,
    business_decline=True,
    notes="string_example",
    draft=True,
    open=True,
    open_offer_type=0,
    unassigned=True,
    unassigned_skill_level=1,
    status=0,
    late_minutes=1,
    breaks=[
        {
            "break_type_id": 1,
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### shift_id: `int`<a id="shift_id-int"></a>

Shift ID

##### location_id: `Optional[int]`<a id="location_id-optionalint"></a>

Location ID

##### user_id: `Optional[int]`<a id="user_id-optionalint"></a>

User ID

##### department_id: `Optional[int]`<a id="department_id-optionalint"></a>

Department ID. Required if the location uses departments

##### role_id: `Optional[int]`<a id="role_id-optionalint"></a>

Role ID. Required if the location uses roles

##### station_id: `Optional[int]`<a id="station_id-optionalint"></a>

The station assigned to the shift

##### start: `Optional[datetime]`<a id="start-optionaldatetime"></a>

Start date time of the shift. UTC in ISO8601 format

##### end: `Optional[datetime]`<a id="end-optionaldatetime"></a>

End date time of the shift. UTC in ISO8601 format

##### close: `Optional[bool]`<a id="close-optionalbool"></a>

Set to true if the shift ends at closing time. If set end is not used.

##### business_decline: `Optional[bool]`<a id="business_decline-optionalbool"></a>

Set to true if the shift ends at business decline.

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes displayed on a shift

##### draft: `Optional[bool]`<a id="draft-optionalbool"></a>

If true the shift is not published.

##### open: `Optional[bool]`<a id="open-optionalbool"></a>

Set to true if the shift is not assigned to any user. Open shifts can be requested by users.

##### open_offer_type: `Optional[int]`<a id="open_offer_type-optionalint"></a>

Set when open is true. Set to 0 when everyone at a location can request an open shift; set to 1 if only offered to specified role.

##### unassigned: `Optional[bool]`<a id="unassigned-optionalbool"></a>

When true the shift is unassigned. Internal use only.

##### unassigned_skill_level: `Optional[int]`<a id="unassigned_skill_level-optionalint"></a>

The skill level required for this shift.  * 1: Beginner  * 2: Intermediate  * 3: Experienced 

##### status: `Optional[int]`<a id="status-optionalint"></a>

Shift status type.  * 0: None  * 1: Sick  * 2: No Show  * 3: Late  * 4: Call Out  * 5: Left Late 

##### late_minutes: `Optional[int]`<a id="late_minutes-optionalint"></a>

Number of minutes a user can clock in late after the shift starts.

##### breaks: [`ShiftsUpdateShiftByIdRequestBreaks`](./7_shifts_python_sdk/type/shifts_update_shift_by_id_request_breaks.py)<a id="breaks-shiftsupdateshiftbyidrequestbreaks7_shifts_python_sdktypeshifts_update_shift_by_id_request_breakspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ShiftsUpdateShiftByIdRequest`](./7_shifts_python_sdk/type/shifts_update_shift_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ShiftsUpdateShiftByIdResponse`](./7_shifts_python_sdk/pydantic/shifts_update_shift_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/shifts/{shift_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.clear_task`<a id="client7shiftstask_managementclear_task"></a>

Clear task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
clear_task_response = client7shifts.task_management.clear_task(
    user_id=1,
    company_id=1234,
    list_id=1234,
    task_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### list_id: `int`<a id="list_id-int"></a>

Task List ID

##### task_id: `int`<a id="task_id-int"></a>

Task ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskManagementClearTaskRequest`](./7_shifts_python_sdk/type/task_management_clear_task_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementClearTaskResponse`](./7_shifts_python_sdk/pydantic/task_management_clear_task_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_lists/{list_id}/tasks/{task_id}/clear` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.create_task_list_template`<a id="client7shiftstask_managementcreate_task_list_template"></a>

Create Task List Template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_task_list_template_response = client7shifts.task_management.create_task_list_template(
    title="string_example",
    recurrence="RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=MO",
    assignments=[
        {
            "location_id": 1,
        }
    ],
    company_id=8655,
    description="string_example",
    due="0480-72-88",
    time_frame={
        "start": "09:00:00",
        "end": "86399",
    },
    task_templates=[
        {
            "title": "title_example",
            "description": "description_example",
            "sort": 1,
        }
    ],
    status=0,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### recurrence: `str`<a id="recurrence-str"></a>

recurrence rules as defined by the RFC 5545 spec

##### assignments: [`TaskManagementCreateTaskListTemplateRequestAssignments`](./7_shifts_python_sdk/type/task_management_create_task_list_template_request_assignments.py)<a id="assignments-taskmanagementcreatetasklisttemplaterequestassignments7_shifts_python_sdktypetask_management_create_task_list_template_request_assignmentspy"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### description: `str`<a id="description-str"></a>

##### due: `str`<a id="due-str"></a>

##### time_frame: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="time_frame-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### task_templates: [`TaskManagementCreateTaskListTemplateRequestTaskTemplates`](./7_shifts_python_sdk/type/task_management_create_task_list_template_request_task_templates.py)<a id="task_templates-taskmanagementcreatetasklisttemplaterequesttasktemplates7_shifts_python_sdktypetask_management_create_task_list_template_request_task_templatespy"></a>

##### status: `int`<a id="status-int"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskManagementCreateTaskListTemplateRequest`](./7_shifts_python_sdk/type/task_management_create_task_list_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementCreateTaskListTemplateResponse`](./7_shifts_python_sdk/pydantic/task_management_create_task_list_template_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_list_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.create_task_tags`<a id="client7shiftstask_managementcreate_task_tags"></a>

Create Task Tags

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.task_management.create_task_tags(
    tags=[
        {
            "user_id": 1,
            "task_id": 1,
        }
    ],
    company_id=1,
    company_id=1234,
    x_api_version="2022-05-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### requestBody: [`TaskManagementCreateTaskTagsRequest`](./7_shifts_python_sdk/type/task_management_create_task_tags_request.py)<a id="requestbody-taskmanagementcreatetasktagsrequest7_shifts_python_sdktypetask_management_create_task_tags_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.delete_task_list_template`<a id="client7shiftstask_managementdelete_task_list_template"></a>

Delete Task List Template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.task_management.delete_task_list_template(
    company_id=8655,
    uuid="uuid_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### uuid: `str`<a id="uuid-str"></a>

Task List Template UUID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_list_templates/{uuid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.delete_task_tags`<a id="client7shiftstask_managementdelete_task_tags"></a>

Delete Task Tags

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.task_management.delete_task_tags(
    company_id=1,
    uuids=[
        "string_example"
    ],
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### requestBody: [`TaskManagementDeleteTaskTagsRequest`](./7_shifts_python_sdk/type/task_management_delete_task_tags_request.py)<a id="requestbody-taskmanagementdeletetasktagsrequest7_shifts_python_sdktypetask_management_delete_task_tags_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_tags` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.edit_task_list_template`<a id="client7shiftstask_managementedit_task_list_template"></a>

edit task list template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
edit_task_list_template_response = client7shifts.task_management.edit_task_list_template(
    company_id=8655,
    uuid="8cff3c09-e328-4425-bea5-20151ddc805a",
    title="string_example",
    description="string_example",
    status=0,
    task_templates=[
        {
            "title": "title_example",
            "description": "description_example",
        }
    ],
    recurrence="RRULE:FREQ=WEEKLY;INTERVAL=1;WKST=MO",
    assignments=[
        {
            "location_id": 1,
        }
    ],
    due="0480-72-88",
    time_frame={
        "start": "09:00:00",
        "end": "86399",
    },
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### uuid: `str`<a id="uuid-str"></a>

Task List Template UUID

##### title: `str`<a id="title-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### status: `int`<a id="status-int"></a>

##### task_templates: [`TaskManagementEditTaskListTemplateRequestTaskTemplates`](./7_shifts_python_sdk/type/task_management_edit_task_list_template_request_task_templates.py)<a id="task_templates-taskmanagementedittasklisttemplaterequesttasktemplates7_shifts_python_sdktypetask_management_edit_task_list_template_request_task_templatespy"></a>

##### recurrence: `str`<a id="recurrence-str"></a>

recurrence rules as defined by the RFC 5545 spec

##### assignments: [`TaskManagementEditTaskListTemplateRequestAssignments`](./7_shifts_python_sdk/type/task_management_edit_task_list_template_request_assignments.py)<a id="assignments-taskmanagementedittasklisttemplaterequestassignments7_shifts_python_sdktypetask_management_edit_task_list_template_request_assignmentspy"></a>

##### due: `str`<a id="due-str"></a>

##### time_frame: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="time_frame-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskManagementEditTaskListTemplateRequest`](./7_shifts_python_sdk/type/task_management_edit_task_list_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementEditTaskListTemplateResponse`](./7_shifts_python_sdk/pydantic/task_management_edit_task_list_template_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_list_templates/{uuid}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.get_settings`<a id="client7shiftstask_managementget_settings"></a>

Gets task management settings for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = client7shifts.task_management.get_settings(
    company_id=1234,
    x_api_version="2022-05-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementGetSettingsResponse`](./7_shifts_python_sdk/pydantic/task_management_get_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_management_settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.get_task_list`<a id="client7shiftstask_managementget_task_list"></a>

Retrieve Task List

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_list_response = client7shifts.task_management.get_task_list(
    company_id=1234,
    list_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    user_id=5678,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### list_id: `int`<a id="list_id-int"></a>

List ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### user_id: `int`<a id="user_id-int"></a>

User ID

#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementGetTaskListResponse`](./7_shifts_python_sdk/pydantic/task_management_get_task_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_lists/{list_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.get_task_list_template`<a id="client7shiftstask_managementget_task_list_template"></a>

Retrieve Task List Template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_list_template_response = client7shifts.task_management.get_task_list_template(
    company_id=8655,
    uuid="uuid_example",
    x_api_version="2022-05-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### uuid: `str`<a id="uuid-str"></a>

Task List Template UUID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementGetTaskListTemplateResponse`](./7_shifts_python_sdk/pydantic/task_management_get_task_list_template_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_list_templates/{uuid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.get_task_list_templates`<a id="client7shiftstask_managementget_task_list_templates"></a>

Get task list templates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_list_templates_response = client7shifts.task_management.get_task_list_templates(
    company_id=8655,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
    department_id=1,
    role_id=1,
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementGetTaskListTemplates200Response`](./7_shifts_python_sdk/pydantic/task_management_get_task_list_templates200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_list_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.get_task_lists`<a id="client7shiftstask_managementget_task_lists"></a>

List Task Lists

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_task_lists_response = client7shifts.task_management.get_task_lists(
    company_id=8655,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    user_id=5678,
    location_id=8655,
    uuid="325bf7a2-21a8-4599-a377-2380140b6710",
    active_on_date="2019-11-05T00:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### uuid: `str`<a id="uuid-str"></a>

Task List Template UUID

##### active_on_date: `str`<a id="active_on_date-str"></a>

Show only tasks lists that were active on a date (YYYY-MM-DD)

#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementGetTaskListsResponse`](./7_shifts_python_sdk/pydantic/task_management_get_task_lists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.list_task_lists_summary`<a id="client7shiftstask_managementlist_task_lists_summary"></a>

List Task Lists Summary

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_task_lists_summary_response = client7shifts.task_management.list_task_lists_summary(
    company_id=1234,
    location_id=5678,
    date="2019-07-01T00:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### date: `str`<a id="date-str"></a>

Date of requested task lists

#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementListTaskListsSummary200Response`](./7_shifts_python_sdk/pydantic/task_management_list_task_lists_summary200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_list_daily_summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.task_management.mark_complete`<a id="client7shiftstask_managementmark_complete"></a>

Complete Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mark_complete_response = client7shifts.task_management.mark_complete(
    user_id=1,
    company_id=1234,
    list_id=1234,
    task_id=1234,
    completion_value=None,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### list_id: `int`<a id="list_id-int"></a>

Task List ID

##### task_id: `int`<a id="task_id-int"></a>

Task ID

##### completion_value: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./7_shifts_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="completion_value-unionbool-date-datetime-dict-float-int-list-str-none7_shifts_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskManagementMarkCompleteRequest`](./7_shifts_python_sdk/type/task_management_mark_complete_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskManagementMarkCompleteResponse`](./7_shifts_python_sdk/pydantic/task_management_mark_complete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/task_lists/{list_id}/tasks/{task_id}/complete` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.approve_request`<a id="client7shiftstime_offapprove_request"></a>

Approve Time Off Request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_request_response = client7shifts.time_off.approve_request(
    time_off_id=1234,
    status_action_message="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_id: `int`<a id="time_off_id-int"></a>

Time Off ID

##### status_action_message: `Optional[str]`<a id="status_action_message-optionalstr"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffApproveRequestRequest`](./7_shifts_python_sdk/type/time_off_approve_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffApproveRequest200Response`](./7_shifts_python_sdk/pydantic/time_off_approve_request200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off/{time_off_id}/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.create_request`<a id="client7shiftstime_offcreate_request"></a>

Create time off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = client7shifts.time_off.create_request(
    user_id=1,
    company_id=1,
    from_date="string_example",
    to_date="string_example",
    partial=True,
    status=1,
    category="string_example",
    partial_from="string_example",
    partial_to="string_example",
    comments="string_example",
    hours=[
        {
            "date": "date_example",
            "num_hours": 3.14,
        }
    ],
    status_action_user_id=1,
    status_action_message="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `int`<a id="user_id-int"></a>

##### company_id: `int`<a id="company_id-int"></a>

##### from_date: `str`<a id="from_date-str"></a>

##### to_date: `str`<a id="to_date-str"></a>

##### partial: `bool`<a id="partial-bool"></a>

##### status: `int`<a id="status-int"></a>

##### category: `str`<a id="category-str"></a>

##### partial_from: `Optional[str]`<a id="partial_from-optionalstr"></a>

##### partial_to: `Optional[str]`<a id="partial_to-optionalstr"></a>

##### comments: `str`<a id="comments-str"></a>

##### hours: [`TimeOffCreateRequestRequestHours`](./7_shifts_python_sdk/type/time_off_create_request_request_hours.py)<a id="hours-timeoffcreaterequestrequesthours7_shifts_python_sdktypetime_off_create_request_request_hourspy"></a>

##### status_action_user_id: `Optional[int]`<a id="status_action_user_id-optionalint"></a>

##### status_action_message: `str`<a id="status_action_message-str"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffCreateRequestRequest`](./7_shifts_python_sdk/type/time_off_create_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffCreateRequest200Response`](./7_shifts_python_sdk/pydantic/time_off_create_request200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.decline_request`<a id="client7shiftstime_offdecline_request"></a>

Decline Time Off Request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
decline_request_response = client7shifts.time_off.decline_request(
    time_off_id=1234,
    status_action_message="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_id: `int`<a id="time_off_id-int"></a>

Time Off ID

##### status_action_message: `Optional[str]`<a id="status_action_message-optionalstr"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffDeclineRequestRequest`](./7_shifts_python_sdk/type/time_off_decline_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffDeclineRequest200Response`](./7_shifts_python_sdk/pydantic/time_off_decline_request200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off/{time_off_id}/decline` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.get_settings`<a id="client7shiftstime_offget_settings"></a>

Retrieve Time Off Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = client7shifts.time_off.get_settings(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetSettings200Response`](./7_shifts_python_sdk/pydantic/time_off_get_settings200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off_settings/{company_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.get_time_off_by_id`<a id="client7shiftstime_offget_time_off_by_id"></a>

Retrieve Time Off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_by_id_response = client7shifts.time_off.get_time_off_by_id(
    time_off_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_id: `int`<a id="time_off_id-int"></a>

Time Off ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetTimeOffById200Response`](./7_shifts_python_sdk/pydantic/time_off_get_time_off_by_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off/{time_off_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.get_total_hours`<a id="client7shiftstime_offget_total_hours"></a>

Retrieve Time Off Hours

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_total_hours_response = client7shifts.time_off.get_total_hours(
    company_id=8655,
    employee_id=[
        ?employee_id=3&employee_id=4&employee_id=5
    ],
    date_start="2019-11-05T12:32:00-08:00:00",
    date_end="2019-11-05T12:32:00-08:00:00",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### employee_id: List[`int`]<a id="employee_id-listint"></a>

Employee IDs

##### date_start: `str`<a id="date_start-str"></a>

An ISO 8601 date string

##### date_end: `str`<a id="date_end-str"></a>

An ISO 8601 date string

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetTotalHours200Response`](./7_shifts_python_sdk/pydantic/time_off_get_total_hours200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off/total_hours` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.list`<a id="client7shiftstime_offlist"></a>

List Time Off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.time_off.list(
    company_id=8655,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1540,
    user_id=1122554,
    status=1,
    category="paid",
    to_date_gte="2020-01-01",
    sort_by="created",
    sort_dir="asc",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### status: `int`<a id="status-int"></a>

Status

##### category: `str`<a id="category-str"></a>

Category

##### to_date_gte: `str`<a id="to_date_gte-str"></a>

Return time offs that end after a specified date.

##### sort_by: `str`<a id="sort_by-str"></a>

Sort by column

##### sort_dir: `str`<a id="sort_dir-str"></a>

Sort by direction (asc, desc)

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffList200Response`](./7_shifts_python_sdk/pydantic/time_off_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.remove`<a id="client7shiftstime_offremove"></a>

Delete Time Off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.time_off.remove(
    time_off_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_id: `int`<a id="time_off_id-int"></a>

Time Off ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off/{time_off_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.set_time_off_settings`<a id="client7shiftstime_offset_time_off_settings"></a>

Create Time Off Settings

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_time_off_settings_response = client7shifts.time_off.set_time_off_settings(
    company_id=1234,
    paid_time_off=True,
    sick_time_off=True,
    time_off_request_comment=True,
    time_off_request_notice=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### paid_time_off: `bool`<a id="paid_time_off-bool"></a>

##### sick_time_off: `bool`<a id="sick_time_off-bool"></a>

##### time_off_request_comment: `bool`<a id="time_off_request_comment-bool"></a>

##### time_off_request_notice: `Union[int, float]`<a id="time_off_request_notice-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffSetTimeOffSettingsRequest`](./7_shifts_python_sdk/type/time_off_set_time_off_settings_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffSetTimeOffSettings200Response`](./7_shifts_python_sdk/pydantic/time_off_set_time_off_settings200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off_settings/{company_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_off.update_time_off_by_id`<a id="client7shiftstime_offupdate_time_off_by_id"></a>

Update Time Off

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_time_off_by_id_response = client7shifts.time_off.update_time_off_by_id(
    time_off_id=1234,
    user_id=1,
    from_date="string_example",
    to_date="string_example",
    partial=True,
    partial_from="string_example",
    partial_to="string_example",
    comments="string_example",
    status=1,
    status_action_message="string_example",
    category="string_example",
    hours=[
        {
            "date": "date_example",
            "num_hours": 3.14,
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_off_id: `int`<a id="time_off_id-int"></a>

Time Off ID

##### user_id: `int`<a id="user_id-int"></a>

##### from_date: `str`<a id="from_date-str"></a>

##### to_date: `str`<a id="to_date-str"></a>

##### partial: `bool`<a id="partial-bool"></a>

##### partial_from: `Optional[str]`<a id="partial_from-optionalstr"></a>

##### partial_to: `Optional[str]`<a id="partial_to-optionalstr"></a>

##### comments: `str`<a id="comments-str"></a>

##### status: `int`<a id="status-int"></a>

##### status_action_message: `str`<a id="status_action_message-str"></a>

##### category: `str`<a id="category-str"></a>

##### hours: [`TimeOffUpdateTimeOffByIdRequestHours`](./7_shifts_python_sdk/type/time_off_update_time_off_by_id_request_hours.py)<a id="hours-timeoffupdatetimeoffbyidrequesthours7_shifts_python_sdktypetime_off_update_time_off_by_id_request_hourspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffUpdateTimeOffByIdRequest`](./7_shifts_python_sdk/type/time_off_update_time_off_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffUpdateTimeOffById200Response`](./7_shifts_python_sdk/pydantic/time_off_update_time_off_by_id200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/time_off/{time_off_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_punches.create`<a id="client7shiftstime_punchescreate"></a>

Create Time Punch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = client7shifts.time_punches.create(
    location_id=1,
    user_id=1,
    clocked_in="2021-01-01T00:00:00.000Z",
    company_id=1234,
    department_id=1,
    role_id=1,
    clocked_out="2021-01-01T00:00:00.000Z",
    notes="string_example",
    tips=1,
    breaks=[
        {
            "paid": True,
            "_in": "2021-01-01T00:00:00.000Z",
            "out": "2021-01-01T00:00:00.000Z",
            "custom_break_id": 1234,
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `int`<a id="location_id-int"></a>

Location ID.

##### user_id: `int`<a id="user_id-int"></a>

The 7shifts ID of the user who is clocking in.

##### clocked_in: `datetime`<a id="clocked_in-datetime"></a>

The start date and time when the user clocked in. Formatted as ISO8601 datetime in UTC timezone.

##### company_id: `int`<a id="company_id-int"></a>

The company id

##### department_id: `int`<a id="department_id-int"></a>

Department ID. Defaults to 0 if not defined.

##### role_id: `int`<a id="role_id-int"></a>

The ID of the role that the user is clocking in to work for. Defaults to 0 if not defined.

##### clocked_out: `datetime`<a id="clocked_out-datetime"></a>

The start date and time when the user clocked out. Formatted as ISO8601 datetime in UTC timezone.

##### notes: `str`<a id="notes-str"></a>

Additional notes for a shift.

##### tips: `Optional[int]`<a id="tips-optionalint"></a>

Tips declared for the shift in cents

##### breaks: [`TimePunchesCreateRequestBreaks`](./7_shifts_python_sdk/type/time_punches_create_request_breaks.py)<a id="breaks-timepunchescreaterequestbreaks7_shifts_python_sdktypetime_punches_create_request_breakspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimePunchesCreateRequest`](./7_shifts_python_sdk/type/time_punches_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimePunchesCreateResponse`](./7_shifts_python_sdk/pydantic/time_punches_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/time_punches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_punches.delete_by_id`<a id="client7shiftstime_punchesdelete_by_id"></a>

Delete Time Punch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.time_punches.delete_by_id(
    company_id=1234,
    time_punch_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### time_punch_id: `int`<a id="time_punch_id-int"></a>

Time punch ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/time_punches/{time_punch_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_punches.get_time_punch`<a id="client7shiftstime_punchesget_time_punch"></a>

Retrieve Time Punch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_punch_response = client7shifts.time_punches.get_time_punch(
    company_id=1234,
    time_punch_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### time_punch_id: `int`<a id="time_punch_id-int"></a>

Time punch ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`TimePunchesGetTimePunchResponse`](./7_shifts_python_sdk/pydantic/time_punches_get_time_punch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/time_punches/{time_punch_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_punches.list`<a id="client7shiftstime_puncheslist"></a>

List Time Punches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.time_punches.list(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    location_id=1,
    department_id=1,
    role_id=1,
    user_id=1,
    approved=True,
    limit=20,
    modified_since="2020-12-30T15:00:00.000Z",
    clocked_in_lte="1970-01-01T00:00:00.00Z",
    clocked_in_gte="1970-01-01T00:00:00.00Z",
    clocked_out_lte="1970-01-01T00:00:00.00Z",
    clocked_out_gte="1970-01-01T00:00:00.00Z",
    include_deleted=False,
    deleted=False,
    localize_search_time=False,
    cursor="string_example",
    sort_by=",iEEpmVvrKlTttzGFqCEGyGBLkBAsBQRJXFH_OJE_CWHioCHFdWvFEDxwNvqMvvkTRU",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### approved: `Optional[bool]`<a id="approved-optionalbool"></a>

Returns time punches that have been approved. Default null, returns both approved and unapproved punches. If true returns only approved punches. If false returns only unapproved punches.

##### limit: `int`<a id="limit-int"></a>

The limit of results that will be returned.

##### modified_since: `datetime`<a id="modified_since-datetime"></a>

Return time punches that have been modified after the specified date time. UTC in ISO8601 Format

##### clocked_in_lte: `datetime`<a id="clocked_in_lte-datetime"></a>

Return time punches with clocked in before or on the specified date.  UTC in ISO8601 format

##### clocked_in_gte: `datetime`<a id="clocked_in_gte-datetime"></a>

Return time punches with clocked in after or on the specified date.  UTC in ISO8601 format

##### clocked_out_lte: `datetime`<a id="clocked_out_lte-datetime"></a>

Return time punches with clocked out before or on the specified date.  UTC in ISO8601 format

##### clocked_out_gte: `datetime`<a id="clocked_out_gte-datetime"></a>

Return time punches with clocked out after or on the specified date.  UTC in ISO8601 format

##### include_deleted: `bool`<a id="include_deleted-bool"></a>

Deprecated, see 'deleted'

##### deleted: `Optional[bool]`<a id="deleted-optionalbool"></a>

Returns punches filtered by deleted status.  Default false, returns undeleted punches. If true returns only deleted punches. if value is null then returns both deleted and undeleted punches.

##### localize_search_time: `bool`<a id="localize_search_time-bool"></a>

If true, convert any date ranges to consider the local timezone of the punches.  If false, date ranges will be in UTC

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### sort_by: `str`<a id="sort_by-str"></a>

The name of the field and direction you want the results ordered by.

#### 🔄 Return<a id="🔄-return"></a>

[`TimePunchesListResponse`](./7_shifts_python_sdk/pydantic/time_punches_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/time_punches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.time_punches.update_by_id`<a id="client7shiftstime_punchesupdate_by_id"></a>

Update Time Punch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = client7shifts.time_punches.update_by_id(
    company_id=1234,
    time_punch_id=1234,
    department_id=1,
    role_id=1,
    clocked_in="2021-01-01T00:00:00.000Z",
    clocked_out="2021-01-01T00:00:00.000Z",
    notes="string_example",
    tips=1,
    breaks=[
        {
            "paid": True,
            "_in": "2021-01-01T00:00:00.000Z",
            "out": "2021-01-01T00:00:00.000Z",
            "custom_break_id": 1234,
        }
    ],
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company id

##### time_punch_id: `int`<a id="time_punch_id-int"></a>

Time punch id

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### role_id: `int`<a id="role_id-int"></a>

The ID of the role that the user is clocking in to work for.

##### clocked_in: `datetime`<a id="clocked_in-datetime"></a>

The start date and time when the user clocked in. Formatted as ISO8601 datetime in UTC timezone.

##### clocked_out: `datetime`<a id="clocked_out-datetime"></a>

The start date and time when the user clocked out. Formatted as ISO8601 datetime in UTC timezone.

##### notes: `str`<a id="notes-str"></a>

Additional notes for a shift.

##### tips: `Optional[int]`<a id="tips-optionalint"></a>

Tips declared for the shift in cents

##### breaks: [`TimePunchesUpdateByIdRequestBreaks`](./7_shifts_python_sdk/type/time_punches_update_by_id_request_breaks.py)<a id="breaks-timepunchesupdatebyidrequestbreaks7_shifts_python_sdktypetime_punches_update_by_id_request_breakspy"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimePunchesUpdateByIdRequest`](./7_shifts_python_sdk/type/time_punches_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimePunchesUpdateByIdResponse`](./7_shifts_python_sdk/pydantic/time_punches_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/time_punches/{time_punch_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.tip_pool.get_detailed_report`<a id="client7shiftstip_poolget_detailed_report"></a>

Retreive Tip Pool Detailed Report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detailed_report_response = client7shifts.tip_pool.get_detailed_report(
    company_id=1234,
    location_id=1,
    start_date="2020-12-25",
    end_date="2020-12-25",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    tip_pool_uuid="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    day_part_uuid="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### start_date: `str`<a id="start_date-str"></a>

The start date in YYYY-MM-DD format

##### end_date: `str`<a id="end_date-str"></a>

The end date in YYYY-MM-DD format

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### tip_pool_uuid: `str`<a id="tip_pool_uuid-str"></a>

The tip pool UUID, when omitted the report will return all tip pools

##### day_part_uuid: `str`<a id="day_part_uuid-str"></a>

Daypart UUID, when omitted the report will return all dayparts

#### 🔄 Return<a id="🔄-return"></a>

[`TipPoolGetDetailedReportResponse`](./7_shifts_python_sdk/pydantic/tip_pool_get_detailed_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}/tip_pool_detailed_report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.tip_pool.get_manual_entry_tips`<a id="client7shiftstip_poolget_manual_entry_tips"></a>

Grabs manual entry tips for a tip pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_manual_entry_tips_response = client7shifts.tip_pool.get_manual_entry_tips(
    company_id=384,
    tip_pool_settings_uuid="1234",
    start_date="2021-01-01T00:00:00.000Z",
    end_date="2021-01-08T00:00:00.000Z",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

The company ID for the target tip pool settings

##### tip_pool_settings_uuid: `str`<a id="tip_pool_settings_uuid-str"></a>

The tip pool settings uuid

##### start_date: `date`<a id="start_date-date"></a>

The start date of the manual entry query range

##### end_date: `date`<a id="end_date-date"></a>

The end date of the manual entry query range

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`TipPoolGetManualEntryTipsResponse`](./7_shifts_python_sdk/pydantic/tip_pool_get_manual_entry_tips_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.tip_pool.get_settings`<a id="client7shiftstip_poolget_settings"></a>

Gets tip pool settings for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = client7shifts.tip_pool.get_settings(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`TipPoolGetSettingsResponse`](./7_shifts_python_sdk/pydantic/tip_pool_get_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/tip_pool_settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.tip_pool.get_summary_report`<a id="client7shiftstip_poolget_summary_report"></a>

Retreive Tip Pool Summary Report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_summary_report_response = client7shifts.tip_pool.get_summary_report(
    company_id=1234,
    location_id=1,
    start_date="2020-12-25",
    end_date="2020-12-25",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    tip_pool_uuid="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    day_part_uuid="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### start_date: `str`<a id="start_date-str"></a>

The start date in YYYY-MM-DD format

##### end_date: `str`<a id="end_date-str"></a>

The end date in YYYY-MM-DD format

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### tip_pool_uuid: `str`<a id="tip_pool_uuid-str"></a>

The tip pool UUID, when omitted the report will return all tip pools

##### day_part_uuid: `str`<a id="day_part_uuid-str"></a>

Daypart UUID, when omitted the report will return all dayparts

#### 🔄 Return<a id="🔄-return"></a>

[`TipPoolGetSummaryReportResponse`](./7_shifts_python_sdk/pydantic/tip_pool_get_summary_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/locations/{location_id}/tip_pool_summary_report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.tip_pool.save_manual_entry`<a id="client7shiftstip_poolsave_manual_entry"></a>

Saves manual entries for a tip pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
save_manual_entry_response = client7shifts.tip_pool.save_manual_entry(
    data=[
        {
            "tip_pool_settings_uuid": "tip_pool_settings_uuid_example",
            "entry_date": "2021-01-01",
            "tip_amount": 12.5,
            "created": "2021-02-12T12:00:00Z",
            "modified": "2021-02-12T13:00:00Z",
        }
    ],
    company_id=384,
    tip_pool_settings_uuid="1234",
    object="manual_tip_pooling",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`TipPoolSaveManualEntryRequestData`](./7_shifts_python_sdk/type/tip_pool_save_manual_entry_request_data.py)<a id="data-tippoolsavemanualentryrequestdata7_shifts_python_sdktypetip_pool_save_manual_entry_request_datapy"></a>

##### company_id: `int`<a id="company_id-int"></a>

The company ID for the target tip pool settings

##### tip_pool_settings_uuid: `str`<a id="tip_pool_settings_uuid-str"></a>

The tip pool settings uuid

##### object: `str`<a id="object-str"></a>

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TipPoolSaveManualEntryRequest`](./7_shifts_python_sdk/type/tip_pool_save_manual_entry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TipPoolSaveManualEntryResponse`](./7_shifts_python_sdk/pydantic/tip_pool_save_manual_entry_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.create_department_assignment`<a id="client7shiftsuser_assignmentscreate_department_assignment"></a>

Create Department Assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_department_assignment_response = client7shifts.user_assignments.create_department_assignment(
    department_id=1,
    company_id=1234,
    user_id=1,
    appear_on_schedule=True,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_id: `int`<a id="department_id-int"></a>

Department ID for user assignment

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### appear_on_schedule: `bool`<a id="appear_on_schedule-bool"></a>

Display the employee on the schedule for this department

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserAssignmentsCreateDepartmentAssignmentRequest`](./7_shifts_python_sdk/type/user_assignments_create_department_assignment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsCreateDepartmentAssignmentResponse`](./7_shifts_python_sdk/pydantic/user_assignments_create_department_assignment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/department_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.create_location_assignment`<a id="client7shiftsuser_assignmentscreate_location_assignment"></a>

Create Location Assignments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_location_assignment_response = client7shifts.user_assignments.create_location_assignment(
    location_id=1,
    company_id=1234,
    user_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### location_id: `int`<a id="location_id-int"></a>

Location ID for user assignment

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserAssignmentsCreateLocationAssignmentRequest`](./7_shifts_python_sdk/type/user_assignments_create_location_assignment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsCreateLocationAssignmentResponse`](./7_shifts_python_sdk/pydantic/user_assignments_create_location_assignment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/location_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.create_role_assignment`<a id="client7shiftsuser_assignmentscreate_role_assignment"></a>

Create Role Assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_role_assignment_response = client7shifts.user_assignments.create_role_assignment(
    role_id=1,
    company_id=1234,
    user_id=1,
    primary=True,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### role_id: `int`<a id="role_id-int"></a>

Role ID for user assignment

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### primary: `bool`<a id="primary-bool"></a>

Sets the role as primary for this user.  Only one role per department can be primary.

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserAssignmentsCreateRoleAssignmentRequest`](./7_shifts_python_sdk/type/user_assignments_create_role_assignment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsCreateRoleAssignmentResponse`](./7_shifts_python_sdk/pydantic/user_assignments_create_role_assignment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/role_assignments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.delete_role_assignment`<a id="client7shiftsuser_assignmentsdelete_role_assignment"></a>

Delete Role Assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.user_assignments.delete_role_assignment(
    company_id=1234,
    user_id=1,
    role_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/role_assignments/{role_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.list`<a id="client7shiftsuser_assignmentslist"></a>

List Assignments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.user_assignments.list(
    company_id=1234,
    user_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsListResponse`](./7_shifts_python_sdk/pydantic/user_assignments_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.list_department_assignments`<a id="client7shiftsuser_assignmentslist_department_assignments"></a>

List Department Assignments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_department_assignments_response = client7shifts.user_assignments.list_department_assignments(
    company_id=1234,
    user_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsListDepartmentAssignmentsResponse`](./7_shifts_python_sdk/pydantic/user_assignments_list_department_assignments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/department_assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.list_location_assignments`<a id="client7shiftsuser_assignmentslist_location_assignments"></a>

List Location Assignments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_location_assignments_response = client7shifts.user_assignments.list_location_assignments(
    company_id=1234,
    user_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsListLocationAssignmentsResponse`](./7_shifts_python_sdk/pydantic/user_assignments_list_location_assignments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/location_assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.list_role_assignments`<a id="client7shiftsuser_assignmentslist_role_assignments"></a>

List Role Assignments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_role_assignments_response = client7shifts.user_assignments.list_role_assignments(
    company_id=1234,
    user_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`UserAssignmentsListRoleAssignmentsResponse`](./7_shifts_python_sdk/pydantic/user_assignments_list_role_assignments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/role_assignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.remove_department_assignment`<a id="client7shiftsuser_assignmentsremove_department_assignment"></a>

Delete Department Assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.user_assignments.remove_department_assignment(
    company_id=1234,
    user_id=1,
    department_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### department_id: `int`<a id="department_id-int"></a>

Department ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/department_assignments/{department_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_assignments.remove_location_assignment`<a id="client7shiftsuser_assignmentsremove_location_assignment"></a>

Delete Location Assignment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.user_assignments.remove_location_assignment(
    company_id=1234,
    user_id=1,
    location_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### location_id: `int`<a id="location_id-int"></a>

Location ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/location_assignments/{location_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_wages.create`<a id="client7shiftsuser_wagescreate"></a>

Create User Wage

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = client7shifts.user_wages.create(
    effective_date="2020-01-01",
    wage_type="hourly",
    wage_cents=1,
    company_id=1,
    user_id=1,
    role_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

The wage effective date. Format YYYY-MM-DD

##### wage_type: `str`<a id="wage_type-str"></a>

The wage type

##### wage_cents: `int`<a id="wage_cents-int"></a>

The wage value. In cents

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### role_id: `int`<a id="role_id-int"></a>

Role ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserWagesCreateRequest`](./7_shifts_python_sdk/type/user_wages_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserWagesCreateResponse`](./7_shifts_python_sdk/pydantic/user_wages_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/wages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.user_wages.list`<a id="client7shiftsuser_wageslist"></a>

List User Wages

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.user_wages.list(
    company_id=1,
    user_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### user_id: `int`<a id="user_id-int"></a>

User ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`UserWagesListResponse`](./7_shifts_python_sdk/pydantic/user_wages_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{user_id}/wages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.users.bulk_create`<a id="client7shiftsusersbulk_create"></a>

Create Many Users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_create_response = client7shifts.users.bulk_create(
    body=[
        {
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "location_ids": [
                1
            ],
            "department_ids": [
                1
            ],
            "email": "example@7shifts.com",
            "mobile_number": "3061234454",
            "home_number": "3061234454",
            "hire_date": "2017-05-20",
            "type": "employee",
            "birth_date": "2017-07-21",
            "language": "en",
            "wage_cents": 2253,
            "wage_type": "hourly",
        }
    ],
    company_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### requestBody: [`UsersBulkCreateRequest`](./7_shifts_python_sdk/type/users_bulk_create_request.py)<a id="requestbody-usersbulkcreaterequest7_shifts_python_sdktypeusers_bulk_create_requestpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersBulkCreateResponse`](./7_shifts_python_sdk/pydantic/users_bulk_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/create_many_users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.users.create_new_user`<a id="client7shiftsuserscreate_new_user"></a>

Create User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = client7shifts.users.create_new_user(
    first_name="string_example",
    last_name="string_example",
    location_ids=[
        1
    ],
    department_ids=[
        1
    ],
    type="employee",
    company_id=1,
    preferred_first_name="string_example",
    preferred_last_name="string_example",
    role_ids=[
        1
    ],
    email="example@7shifts.com",
    mobile_number="3061234454",
    home_number="3061234454",
    address="string_example",
    postal_zip="string_example",
    city="string_example",
    prov_state="string_example",
    invite_user=True,
    notes="string_example",
    hire_date="2017-05-20",
    employee_id="string_example",
    punch_id="string_example",
    birth_date="2017-07-21",
    language="en",
    appear_as_employee=True,
    subscribe_to_updates=True,
    max_weekly_hours=1,
    wage_cents=2253,
    wage_type="hourly",
    wages=[
        {
            "effective_date": "2020-01-01",
        }
    ],
    permissions_template_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

The user's first name

##### last_name: `str`<a id="last_name-str"></a>

The user's last name

##### location_ids: [`UsersCreateNewUserRequestLocationIds`](./7_shifts_python_sdk/type/users_create_new_user_request_location_ids.py)<a id="location_ids-userscreatenewuserrequestlocationids7_shifts_python_sdktypeusers_create_new_user_request_location_idspy"></a>

##### department_ids: [`UsersCreateNewUserRequestDepartmentIds`](./7_shifts_python_sdk/type/users_create_new_user_request_department_ids.py)<a id="department_ids-userscreatenewuserrequestdepartmentids7_shifts_python_sdktypeusers_create_new_user_request_department_idspy"></a>

##### type: `str`<a id="type-str"></a>

The type of this user

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### preferred_first_name: `Optional[str]`<a id="preferred_first_name-optionalstr"></a>

An optional alternate first name

##### preferred_last_name: `Optional[str]`<a id="preferred_last_name-optionalstr"></a>

An optional alternate last name

##### role_ids: [`UsersCreateNewUserRequestRoleIds`](./7_shifts_python_sdk/type/users_create_new_user_request_role_ids.py)<a id="role_ids-userscreatenewuserrequestroleids7_shifts_python_sdktypeusers_create_new_user_request_role_idspy"></a>

##### email: `str`<a id="email-str"></a>

the user's email

##### mobile_number: `Optional[str]`<a id="mobile_number-optionalstr"></a>

The user's mobile phone number. Format with no spaces and include area code

##### home_number: `Optional[str]`<a id="home_number-optionalstr"></a>

The user's home phone number. Format with no spaces and include area code

##### address: `Optional[str]`<a id="address-optionalstr"></a>

The user's address

##### postal_zip: `Optional[str]`<a id="postal_zip-optionalstr"></a>

The user's postal code or zip code

##### city: `Optional[str]`<a id="city-optionalstr"></a>

The user's city

##### prov_state: `Optional[str]`<a id="prov_state-optionalstr"></a>

The user's province or state

##### invite_user: `Optional[bool]`<a id="invite_user-optionalbool"></a>

If true Invite the user to 7shifts

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes associated with this user

##### hire_date: `Optional[date]`<a id="hire_date-optionaldate"></a>

The hire date of this user. Format YYYY-MM-DD

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

Either an employee ID or an ID assigned by your payroll provider that is used in your payroll export

##### punch_id: `Optional[str]`<a id="punch_id-optionalstr"></a>

The punch ID they punch in/out with. If no value is provided a new one will be created

##### birth_date: `Optional[date]`<a id="birth_date-optionaldate"></a>

The user's birthdate. Format YYYY-MM-DD

##### language: `str`<a id="language-str"></a>

The user's preferred language. Default value is en

##### appear_as_employee: `Optional[bool]`<a id="appear_as_employee-optionalbool"></a>

User should appear in the system as an employee. Applies to admin users only

##### subscribe_to_updates: `Optional[bool]`<a id="subscribe_to_updates-optionalbool"></a>

Subscribe this user to updates from 7shifts. This includes announcing new features for 7shifts

##### max_weekly_hours: `Optional[int]`<a id="max_weekly_hours-optionalint"></a>

The maximum weekly hours this user is set to work

##### wage_cents: `Optional[Union[int, float]]`<a id="wage_cents-optionalunionint-float"></a>

##### wage_type: `Optional[str]`<a id="wage_type-optionalstr"></a>

The wage type

##### wages: [`UsersCreateNewUserRequestWages`](./7_shifts_python_sdk/type/users_create_new_user_request_wages.py)<a id="wages-userscreatenewuserrequestwages7_shifts_python_sdktypeusers_create_new_user_request_wagespy"></a>

##### permissions_template_id: `Optional[int]`<a id="permissions_template_id-optionalint"></a>

Id of a permissions template the user will be assigned to and granted permissions from.

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateNewUserRequest`](./7_shifts_python_sdk/type/users_create_new_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersCreateNewUserResponse`](./7_shifts_python_sdk/pydantic/users_create_new_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.users.deactivate`<a id="client7shiftsusersdeactivate"></a>

Deactivate User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.users.deactivate(
    inactive_reason="string_example",
    company_id=1,
    identifier=1,
    inactive_comments="string_example",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inactive_reason: `Optional[str]`<a id="inactive_reason-optionalstr"></a>

Enum value. See inactive_reasons endpoint for list of values.

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### identifier: `int`<a id="identifier-int"></a>

User ID

##### inactive_comments: `Optional[str]`<a id="inactive_comments-optionalstr"></a>

Comments related to this user deletion.

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersDeactivateRequest`](./7_shifts_python_sdk/type/users_deactivate_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{identifier}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.users.get_user_by_identifier`<a id="client7shiftsusersget_user_by_identifier"></a>

Retrieve User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_identifier_response = client7shifts.users.get_user_by_identifier(
    company_id=1,
    identifier="46734",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### identifier: `str`<a id="identifier-str"></a>

User ID. Accepted values are 7shifts user id or punch id. Use prefix punch: for punch id

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetUserByIdentifierResponse`](./7_shifts_python_sdk/pydantic/users_get_user_by_identifier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{identifier}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.users.list`<a id="client7shiftsuserslist"></a>

List Users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.users.list(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    modified_since="2020-01-01",
    location_id=1,
    department_id=1,
    role_id=1,
    status="active",
    name="string_example",
    sort_by="firstname.asc,lastname.desc",
    cursor="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### modified_since: `str`<a id="modified_since-str"></a>

Return users that have been modified since the specified date. Format YYYY-MM-DD

##### location_id: `int`<a id="location_id-int"></a>

Location ID (cannot be used in conjunction with Department ID and Role ID)

##### department_id: `int`<a id="department_id-int"></a>

Department ID (cannot be used in conjunction with Location ID and Role ID)

##### role_id: `int`<a id="role_id-int"></a>

Role ID (cannot be used in conjunction with Location ID and Department ID)

##### status: `str`<a id="status-str"></a>

The user status

##### name: `str`<a id="name-str"></a>

Filter by partial or full employee name

##### sort_by: `str`<a id="sort_by-str"></a>

Sort the paginated result by the given field and direction.

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListResponse`](./7_shifts_python_sdk/pydantic/users_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.users.update_user_by_identifier`<a id="client7shiftsusersupdate_user_by_identifier"></a>

Update User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_by_identifier_response = client7shifts.users.update_user_by_identifier(
    company_id=1,
    identifier=1,
    first_name="string_example",
    last_name="string_example",
    preferred_first_name="string_example",
    preferred_last_name="string_example",
    email="example@7shifts.com",
    mobile_number="3061234454",
    home_number="3061234454",
    address="string_example",
    postal_zip="string_example",
    city="string_example",
    prov_state="string_example",
    notes="string_example",
    hire_date="2017-05-20",
    type="employee",
    employee_id="string_example",
    punch_id="string_example",
    birth_date="2017-07-21",
    language="en",
    appear_as_employee=True,
    subscribe_to_updates=True,
    max_weekly_hours=1,
    active=True,
    pronouns="string_example",
    permissions_template_id=1,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### identifier: `int`<a id="identifier-int"></a>

User ID

##### first_name: `str`<a id="first_name-str"></a>

The user's first name

##### last_name: `str`<a id="last_name-str"></a>

The user's last name

##### preferred_first_name: `Optional[str]`<a id="preferred_first_name-optionalstr"></a>

An optional alternate first name

##### preferred_last_name: `Optional[str]`<a id="preferred_last_name-optionalstr"></a>

An optional alternate last name

##### email: `str`<a id="email-str"></a>

the user's email

##### mobile_number: `Optional[str]`<a id="mobile_number-optionalstr"></a>

The user's mobile phone number. Format with no spaces and include area code

##### home_number: `Optional[str]`<a id="home_number-optionalstr"></a>

The user's home phone number. Format with no spaces and include area code

##### address: `Optional[str]`<a id="address-optionalstr"></a>

The user's address

##### postal_zip: `Optional[str]`<a id="postal_zip-optionalstr"></a>

The user's postal code or zip code

##### city: `Optional[str]`<a id="city-optionalstr"></a>

The user's city

##### prov_state: `Optional[str]`<a id="prov_state-optionalstr"></a>

The user's province or state

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes associated with this user

##### hire_date: `Optional[date]`<a id="hire_date-optionaldate"></a>

The hire date of this user. Format YYYY-MM-DD

##### type: `str`<a id="type-str"></a>

The type of this user

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

Either an employee ID or an ID assigned by your payroll provider that is used in your payroll export

##### punch_id: `Optional[str]`<a id="punch_id-optionalstr"></a>

The punch ID they punch in/out with. If no value is provided a new one will be created

##### birth_date: `Optional[date]`<a id="birth_date-optionaldate"></a>

The user's birthdate. Format YYYY-MM-DD

##### language: `str`<a id="language-str"></a>

The user's preferred language. Default value is en

##### appear_as_employee: `bool`<a id="appear_as_employee-bool"></a>

User should appear in the system as an employee. Applies to admin users only

##### subscribe_to_updates: `bool`<a id="subscribe_to_updates-bool"></a>

Subscribe this user to updates from 7shifts. This includes announcing new features for 7shifts

##### max_weekly_hours: `int`<a id="max_weekly_hours-int"></a>

The maximum weekly hours this user is set to work

##### active: `bool`<a id="active-bool"></a>

User status. If false the user is unable to login

##### pronouns: `Optional[str]`<a id="pronouns-optionalstr"></a>

The user's pronouns

##### permissions_template_id: `Optional[int]`<a id="permissions_template_id-optionalint"></a>

Permission Template ID the user is assigned to

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateUserByIdentifierRequest`](./7_shifts_python_sdk/type/users_update_user_by_identifier_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersUpdateUserByIdentifierResponse`](./7_shifts_python_sdk/pydantic/users_update_user_by_identifier_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/users/{identifier}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.webhooks.create`<a id="client7shiftswebhookscreate"></a>

Create Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = client7shifts.webhooks.create(
    url="string_example",
    method="post",
    event="schedule.published",
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

Webhook URL

##### method: `str`<a id="method-str"></a>

Webhook Method

##### event: `str`<a id="event-str"></a>

Event

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreateRequest`](./7_shifts_python_sdk/type/webhooks_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksCreateResponse`](./7_shifts_python_sdk/pydantic/webhooks_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.webhooks.delete_webhook_by_id`<a id="client7shiftswebhooksdelete_webhook_by_id"></a>

Delete Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
client7shifts.webhooks.delete_webhook_by_id(
    company_id=1234,
    webhook_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### webhook_id: `int`<a id="webhook_id-int"></a>

Webhook ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/webhooks/{webhook_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.webhooks.get_webhook`<a id="client7shiftswebhooksget_webhook"></a>

Test Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webhook_response = client7shifts.webhooks.get_webhook(
    company_id=1234,
    topic="user.modified",
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    webhook_id=1234,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### topic: `str`<a id="topic-str"></a>

topic for the sample payload

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### webhook_id: `int`<a id="webhook_id-int"></a>

Webhook ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/test_webhook` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.webhooks.list`<a id="client7shiftswebhookslist"></a>

List Webhooks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = client7shifts.webhooks.list(
    company_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
    modified_since="2020-01-01",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

##### modified_since: `str`<a id="modified_since-str"></a>

Return webhooks that have been modified since the specified date. Format YYYY-MM-DD

##### cursor: `str`<a id="cursor-str"></a>

Cursor for the next or previous page of results.

##### limit: `int`<a id="limit-int"></a>

The number of results desired per page.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListResponse`](./7_shifts_python_sdk/pydantic/webhooks_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `client7shifts.webhooks.update`<a id="client7shiftswebhooksupdate"></a>

Update Webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = client7shifts.webhooks.update(
    url="string_example",
    company_id=1234,
    webhook_id=1234,
    x_api_version="2022-05-01",
    x_company_guid="1310bfe1-cb3f-4f24-98a2-fde2bc504108",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

Webhook URL

##### company_id: `int`<a id="company_id-int"></a>

Company ID

##### webhook_id: `int`<a id="webhook_id-int"></a>

Webhook ID

##### x_api_version: `str`<a id="x_api_version-str"></a>

7shifts API version

##### x_company_guid: `str`<a id="x_company_guid-str"></a>

Company GUID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateRequest`](./7_shifts_python_sdk/type/webhooks_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksUpdateResponse`](./7_shifts_python_sdk/pydantic/webhooks_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/company/{company_id}/webhooks/{webhook_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
