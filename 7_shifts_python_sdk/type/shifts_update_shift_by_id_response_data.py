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

from 7_shifts_python_sdk.type.shifts_update_shift_by_id_response_data_breaks import ShiftsUpdateShiftByIdResponseDataBreaks

class RequiredShiftsUpdateShiftByIdResponseData(TypedDict):
    # Shift ID
    id: int

    # User ID
    user_id: typing.Optional[int]

    # Start date time of the shift. UTC in ISO8601 format
    start: datetime

    # End date time of the shift. UTC in ISO8601 format
    end: datetime

    # If true the shift ends at closing time. If set end is not used.
    close: bool

    # If true the shift ends at business decline.
    business_decline: bool

    # Department ID. Required if the location uses departments.
    department_id: typing.Optional[int]

    # The ID of the location that the shift is assigned to.
    location_id: int

    # Role ID. Required if the location uses roles.
    role_id: typing.Optional[int]

    # Notes displayed on a shift
    notes: str

    # Whether or not the shift is a draft shift. Draft shifts are shifts that have not yet been published.
    draft: bool

    # Whether or not the individual assigned to the shift has been notified of the shifts existence.
    notified: bool

    # If true the shift is not assigned to any user. Open shifts can be requested by users.
    open: bool

    # Shifts in a template that could not be assigned to any eligible employees.
    unassigned: bool

    # Specify the minimum user skill level required for the shift. Levels 1 - beginner, 2 - intermediate, 3 - Experienced.
    unassigned_skill_level: int

    # Specifies the scope of who can pick up the shift.
    open_offer_type: typing.Optional[str]

    # Specified shift flags to track employee attendance
    attendance_status: str

    # Current publication status of the shift
    publish_status: str

    # The created date of the shift in UTC
    created: typing.Optional[datetime]

    # The last modified date of the shift in UTC
    modified: typing.Optional[datetime]

    # Whether or not this shift is deleted.
    deleted: bool

    # Whether or not this shift is soft-deleted.
    soft_deleted: typing.Optional[str]

    # Station Number
    station: int

    # Station name
    station_name: typing.Optional[str]

    # Station id
    station_id: typing.Optional[int]

class OptionalShiftsUpdateShiftByIdResponseData(TypedDict, total=False):
    # Read Only. The hourly wage for this shift. In cents.
    hourly_wage: typing.Union[int, float]

    # Specify the grace minutes they can clock-in late.
    late_minuets: int

    breaks: typing.Optional[ShiftsUpdateShiftByIdResponseDataBreaks]

class ShiftsUpdateShiftByIdResponseData(RequiredShiftsUpdateShiftByIdResponseData, OptionalShiftsUpdateShiftByIdResponseData):
    pass