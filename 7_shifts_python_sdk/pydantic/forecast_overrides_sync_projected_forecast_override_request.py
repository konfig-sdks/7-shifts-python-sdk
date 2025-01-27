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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class ForecastOverridesSyncProjectedForecastOverrideRequest(BaseModel):
    # The start date of the date range of override data to remove. Override data will be removed from only this date if no end date is provided. Format YYYY-MM-DD
    start_date: date = Field(alias='start_date')

    # Type of override data to remove
    report_type: Literal["sales"] = Field(alias='report_type')

    # The ending date of a date range of override data to remove. Optional. Format YYYY-MM-DD
    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
