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


class CompaniesGetLaborSettingsResponseData(BaseModel):
    company_id: int = Field(alias='company_id')

    # Number of consecutive days threshold an employee works before overtime
    consecutive_days_threshold: typing.Optional[int] = Field(alias='consecutive_days_threshold')

    # The overtime pay multiplier
    consecutive_days_multiplier: typing.Optional[typing.Union[int, float]] = Field(alias='consecutive_days_multiplier')

    # When true, the regular rate of pay considers the number of hours worked at different pay rates while calculating overtime
    regular_rate_of_pay_enabled: bool = Field(alias='regular_rate_of_pay_enabled')

    # When true, exception costs are displayed in reports
    exception_cost_enabled: bool = Field(alias='exception_cost_enabled')

    overtime_by_location_enabled: bool = Field(alias='overtime_by_location_enabled')

    # When true, use break conditions to alter labor costs and hour
    auto_break_enabled: bool = Field(alias='auto_break_enabled')

    auto_break_hours: typing.Union[int, float] = Field(alias='auto_break_hours')

    auto_break_minutes: int = Field(alias='auto_break_minutes')

    auto_break_hours_2: typing.Union[int, float] = Field(alias='auto_break_hours_2')

    auto_break_minutes_2: int = Field(alias='auto_break_minutes_2')

    overtime_enabled: bool = Field(alias='overtime_enabled')

    daily_overtime_threshold: typing.Union[int, float] = Field(alias='daily_overtime_threshold')

    daily_overtime_multiplier: typing.Union[int, float] = Field(alias='daily_overtime_multiplier')

    premium_overtime_threshold: typing.Optional[int] = Field(alias='premium_overtime_threshold')

    premium_overtime_multiplier: typing.Optional[typing.Union[int, float]] = Field(alias='premium_overtime_multiplier')

    weekly_overtime_threshold: typing.Union[int, float] = Field(alias='weekly_overtime_threshold')

    weekly_overtime_multiplier: typing.Union[int, float] = Field(alias='weekly_overtime_multiplier')

    ot_alerts_enabled: bool = Field(alias='ot_alerts_enabled')

    ot_alerts_buffer_minutes: typing.Optional[int] = Field(alias='ot_alerts_buffer_minutes')

    split_hours_on_holidays: bool = Field(alias='split_hours_on_holidays')

    # When true, allows employees to have a separate wage for
    wage_based_roles_enabled: bool = Field(alias='wage_based_roles_enabled')

    jurisdiction: typing.Optional[str] = Field(alias='jurisdiction')

    is_custom: bool = Field(alias='is_custom')

    # When true, minimum wage will be used when calculating overtime pay
    use_jurisdiction_minimum_wage_for_ot: bool = Field(alias='use_jurisdiction_minimum_wage_for_ot')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
