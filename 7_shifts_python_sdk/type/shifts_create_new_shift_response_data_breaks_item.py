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


class RequiredShiftsCreateNewShiftResponseDataBreaksItem(TypedDict):
    # Break ID
    id: int

    # Shift ID
    shift_id: int

    # Break type name
    name: str

    # Break type length in minutes
    length: int

    # Break type ID
    break_type_id: int

class OptionalShiftsCreateNewShiftResponseDataBreaksItem(TypedDict, total=False):
    # Start date time of the break. UTC in ISO8601 format.
    start: typing.Optional[datetime]

    # End date time of the break. UTC in ISO8601 format.
    end: typing.Optional[datetime]

    # Break type paid or unpaid
    type: str

class ShiftsCreateNewShiftResponseDataBreaksItem(RequiredShiftsCreateNewShiftResponseDataBreaksItem, OptionalShiftsCreateNewShiftResponseDataBreaksItem):
    pass
