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


class RequiredForecastOverridesCreateDailyProjectedForecastOverrideRequest(TypedDict):
    # The date of the daily report data to override. Format YYYY-MM-DD
    date: date

    # Override value. Currency values in cents
    value: int

    # Type of value to override. Default is sales
    report_type: str

class OptionalForecastOverridesCreateDailyProjectedForecastOverrideRequest(TypedDict, total=False):
    # Department ID. Optional
    department_id: typing.Optional[int]

class ForecastOverridesCreateDailyProjectedForecastOverrideRequest(RequiredForecastOverridesCreateDailyProjectedForecastOverrideRequest, OptionalForecastOverridesCreateDailyProjectedForecastOverrideRequest):
    pass
