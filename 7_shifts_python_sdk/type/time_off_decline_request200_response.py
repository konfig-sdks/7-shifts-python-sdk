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

from 7_shifts_python_sdk.type.time_off_decline_request200_response_hours import TimeOffDeclineRequest200ResponseHours

class RequiredTimeOffDeclineRequest200Response(TypedDict):
    id: int

    user_id: int

    company_id: int

    from_date: str

    to_date: str

    partial: bool

    partial_from: typing.Optional[str]

    partial_to: typing.Optional[str]

    comments: str

    status: int

    status_action_user_id: typing.Optional[int]

    status_action_message: str

    category: str

    created: str

    amount_of_hours: typing.Union[int, float]

    hours: TimeOffDeclineRequest200ResponseHours

class OptionalTimeOffDeclineRequest200Response(TypedDict, total=False):
    pass

class TimeOffDeclineRequest200Response(RequiredTimeOffDeclineRequest200Response, OptionalTimeOffDeclineRequest200Response):
    pass
