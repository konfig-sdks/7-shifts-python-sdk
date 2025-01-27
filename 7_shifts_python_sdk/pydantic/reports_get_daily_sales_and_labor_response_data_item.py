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


class ReportsGetDailySalesAndLaborResponseDataItem(BaseModel):
    # The date of the actual and projected data (y-m-d)
    date: str = Field(alias='date')

    # Actual Sales (in cents)
    actual_sales: int = Field(alias='actual_sales')

    # Projected Sales (in cents)
    projected_sales: int = Field(alias='projected_sales')

    # Actual Labor Cost (in cents)
    actual_labor_cost: int = Field(alias='actual_labor_cost')

    # Projected Labor Cost (in cents)
    projected_labor_cost: int = Field(alias='projected_labor_cost')

    # Sales Per Labor Hour (in cents, not rounded)
    sales_per_labor_hour: typing.Union[int, float] = Field(alias='sales_per_labor_hour')

    # Projected Sales Per Labor Hour (in cents, not rounded)
    projected_sales_per_labor_hour: typing.Union[int, float] = Field(alias='projected_sales_per_labor_hour')

    # Items Per Labor Hour
    items_per_labor_hour: typing.Union[int, float] = Field(alias='items_per_labor_hour')

    # Projected Items Per Labor Hour
    projected_items_per_labor_hour: typing.Union[int, float] = Field(alias='projected_items_per_labor_hour')

    # Labor Percent
    labor_percent: typing.Union[int, float] = Field(alias='labor_percent')

    # User specified override for projected sales
    projected_sales_override: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='projected_sales_override')

    # ID of the Daily Report
    id: typing.Optional[typing.Optional[int]] = Field(None, alias='id')

    # Location ID for the Daily Report
    location_id: typing.Optional[int] = Field(None, alias='location_id')

    # Department ID for the Daily Report
    department_id: typing.Optional[typing.Optional[int]] = Field(None, alias='department_id')

    # Number of items sold
    actual_items: typing.Optional[int] = Field(None, alias='actual_items')

    # Projected number of items sold
    projected_items: typing.Optional[int] = Field(None, alias='projected_items')

    # User specified override for projected number of items sold
    projected_items_override: typing.Optional[typing.Optional[int]] = Field(None, alias='projected_items_override')

    # the labor target
    labor_target: typing.Optional[typing.Union[int, float]] = Field(None, alias='labor_target')

    # Actual number of minutes worked
    actual_labor_minutes: typing.Optional[int] = Field(None, alias='actual_labor_minutes')

    # Projected number of minutes worked
    projected_labor_minutes: typing.Optional[int] = Field(None, alias='projected_labor_minutes')

    # Actual number of overtime minutes worked
    actual_ot_minutes: typing.Optional[int] = Field(None, alias='actual_ot_minutes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
