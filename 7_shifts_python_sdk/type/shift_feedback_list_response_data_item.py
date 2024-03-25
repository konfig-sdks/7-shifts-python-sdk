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


class RequiredShiftFeedbackListResponseDataItem(TypedDict):
    # ID for the shift feedback
    id: int

    # Location ID
    location_id: int

    # Department ID
    department_id: int

    # Role ID
    role_id: int

    # Shift start time
    start: datetime

    # Shift end time
    end: datetime

    # Shift ID
    shift_id: int

    # User ID
    user_id: int

    # If the user was notified to provide shift feedback
    notified: bool

    # Rating of the shift
    rating: int

    # Comments about the shift
    comments: str

    # If the shift feedback request was dismissed
    dismissed: bool

    # Station name
    station_name: str

class OptionalShiftFeedbackListResponseDataItem(TypedDict, total=False):
    pass

class ShiftFeedbackListResponseDataItem(RequiredShiftFeedbackListResponseDataItem, OptionalShiftFeedbackListResponseDataItem):
    pass
