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


class ScheduleEnforcementListScheduledShiftsResponseDataItem(BaseModel):
    id: int = Field(alias='id')

    location_id: int = Field(alias='location_id')

    station_name: str = Field(alias='station_name')

    start: datetime = Field(alias='start')

    end: datetime = Field(alias='end')

    close: bool = Field(alias='close')

    business_decline: bool = Field(alias='business_decline')

    notes: str = Field(alias='notes')

    publish_status: Literal["draft", "published", "draft_deleted", "published_deleted"] = Field(alias='publish_status')

    open: bool = Field(alias='open')

    attendance_status: Literal["none", "sick", "no_show", "late"] = Field(alias='attendance_status')

    user_id: typing.Optional[typing.Optional[int]] = Field(None, alias='user_id')

    department_id: typing.Optional[typing.Optional[int]] = Field(None, alias='department_id')

    role_id: typing.Optional[typing.Optional[int]] = Field(None, alias='role_id')

    station_id: typing.Optional[typing.Optional[int]] = Field(None, alias='station_id')

    company_id: typing.Optional[typing.Optional[int]] = Field(None, alias='company_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
