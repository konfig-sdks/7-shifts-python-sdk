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

from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response_users_item_roles import ReportsGetWorkedHoursWagesResponseUsersItemRoles
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response_users_item_total import ReportsGetWorkedHoursWagesResponseUsersItemTotal
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response_users_item_user import ReportsGetWorkedHoursWagesResponseUsersItemUser
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response_users_item_weeks import ReportsGetWorkedHoursWagesResponseUsersItemWeeks

class ReportsGetWorkedHoursWagesResponseUsersItem(BaseModel):
    user: typing.Optional[ReportsGetWorkedHoursWagesResponseUsersItemUser] = Field(None, alias='user')

    weeks: typing.Optional[ReportsGetWorkedHoursWagesResponseUsersItemWeeks] = Field(None, alias='weeks')

    roles: typing.Optional[ReportsGetWorkedHoursWagesResponseUsersItemRoles] = Field(None, alias='roles')

    total: typing.Optional[ReportsGetWorkedHoursWagesResponseUsersItemTotal] = Field(None, alias='total')

    # Whether employee is salaried during the entire date range of the report
    salaried: typing.Optional[bool] = Field(None, alias='salaried')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
