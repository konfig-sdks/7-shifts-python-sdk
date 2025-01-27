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

from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response_users_item_weeks_item_lone_compliance_exceptions import ReportsGetWorkedHoursWagesResponseUsersItemWeeksItemLoneComplianceExceptions
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response_users_item_weeks_item_shifts import ReportsGetWorkedHoursWagesResponseUsersItemWeeksItemShifts

class ReportsGetWorkedHoursWagesResponseUsersItemWeeksItem(BaseModel):
    # Work week (first day of week)
    week: typing.Optional[str] = Field(None, alias='week')

    # Whether employee is salaried during the entire week
    salaried: typing.Optional[bool] = Field(None, alias='salaried')

    shifts: typing.Optional[ReportsGetWorkedHoursWagesResponseUsersItemWeeksItemShifts] = Field(None, alias='shifts')

    lone_compliance_exceptions: typing.Optional[ReportsGetWorkedHoursWagesResponseUsersItemWeeksItemLoneComplianceExceptions] = Field(None, alias='lone_compliance_exceptions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
