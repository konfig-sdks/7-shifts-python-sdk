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

from 7_shifts_python_sdk.type.time_punches_update_by_id_request_breaks import TimePunchesUpdateByIdRequestBreaks

class RequiredTimePunchesUpdateByIdRequest(TypedDict):
    pass

class OptionalTimePunchesUpdateByIdRequest(TypedDict, total=False):
    # Department ID
    department_id: int

    # The ID of the role that the user is clocking in to work for.
    role_id: int

    # The start date and time when the user clocked in. Formatted as ISO8601 datetime in UTC timezone.
    clocked_in: datetime

    # The start date and time when the user clocked out. Formatted as ISO8601 datetime in UTC timezone.
    clocked_out: datetime

    # Additional notes for a shift.
    notes: str

    # Tips declared for the shift in cents
    tips: typing.Optional[int]

    breaks: TimePunchesUpdateByIdRequestBreaks

class TimePunchesUpdateByIdRequest(RequiredTimePunchesUpdateByIdRequest, OptionalTimePunchesUpdateByIdRequest):
    pass
