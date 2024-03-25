# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from 7_shifts_python_sdk.type.shifts_create_new_shift_request_breaks import ShiftsCreateNewShiftRequestBreaks

class RequiredShiftsCreateNewShiftRequest(TypedDict):
    # Shift ID
    location_id: int

    # Start date time of the shift. UTC in ISO8601 format.
    start: datetime

    # End date time of the shift. UTC in ISO8601 format.
    end: datetime

class OptionalShiftsCreateNewShiftRequest(TypedDict, total=False):
    # User ID
    user_id: int

    # Department ID. Required if the location uses departments.
    department_id: typing.Optional[int]

    # Role ID. Required if the location uses roles.
    role_id: typing.Optional[int]

    # Station ID
    station_id: typing.Optional[int]

    # Set to true if the shift ends at closing time. If set, end is not used.
    close: typing.Optional[bool]

    # Set to true if the shift ends at business decline.
    business_decline: typing.Optional[bool]

    # Notes displayed on a shift.
    notes: typing.Optional[str]

    # If true the shift is not published.
    draft: typing.Optional[bool]

    # If true the user has been notified of the published shift.
    notified: typing.Optional[bool]

    # Set to true if the shift is not assigned to any user. Open shifts can be requested by users.
    open: typing.Optional[bool]

    # Set when open is true. Set to 1 for everyone can request an open shift; set to 1 if only offered to specified role.
    open_offer_type: typing.Optional[int]

    # Internal use only
    unassigned: typing.Optional[bool]

    # The skill level required for this shift.
    unassigned_skill_level: typing.Optional[int]

    # Shift status type. 0 - none, 1 - sick, 2 - no show, 3 - late, 4 - call out, 5 - left late.
    status: typing.Optional[int]

    # Number of minutes a user can clock in late after the shift starts.
    late_minutes: typing.Optional[int]

    breaks: typing.Optional[ShiftsCreateNewShiftRequestBreaks]

class ShiftsCreateNewShiftRequest(RequiredShiftsCreateNewShiftRequest, OptionalShiftsCreateNewShiftRequest):
    pass
