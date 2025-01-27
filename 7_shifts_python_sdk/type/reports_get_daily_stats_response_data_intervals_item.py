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


class RequiredReportsGetDailyStatsResponseDataIntervalsItem(TypedDict):
    pass

class OptionalReportsGetDailyStatsResponseDataIntervalsItem(TypedDict, total=False):
    day: date

    start: datetime

    end: datetime

    # The actual sales in cents
    actual_sales: int

    # The projected sales in cents
    projected_sales: int

    # The past actual sales in cents
    past_actual_sales: int

    # The past projected sales in cents
    past_projected_sales: int

    # The actual labor in cents
    actual_labor: int

    # The projected labor in cents
    projected_labor: int

    # The projected labor minutes
    projected_labor_minutes: typing.Union[int, float]

    # The current labor ratio
    labor_ratio: typing.Union[int, float]

    # The projected labor ratio
    projected_labor_ratio: typing.Union[int, float]

    # The actual sales per man hour
    actual_spmh: typing.Union[int, float]

    # The projected sales per man hour
    projected_spmh: typing.Union[int, float]

class ReportsGetDailyStatsResponseDataIntervalsItem(RequiredReportsGetDailyStatsResponseDataIntervalsItem, OptionalReportsGetDailyStatsResponseDataIntervalsItem):
    pass
