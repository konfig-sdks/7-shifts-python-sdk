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

from 7_shifts_python_sdk.pydantic.time_punches_create_request_breaks import TimePunchesCreateRequestBreaks

class TimePunchesCreateRequest(BaseModel):
    # Location ID.
    location_id: int = Field(alias='location_id')

    # The 7shifts ID of the user who is clocking in.
    user_id: int = Field(alias='user_id')

    # The start date and time when the user clocked in. Formatted as ISO8601 datetime in UTC timezone.
    clocked_in: datetime = Field(alias='clocked_in')

    # Department ID. Defaults to 0 if not defined.
    department_id: typing.Optional[int] = Field(None, alias='department_id')

    # The ID of the role that the user is clocking in to work for. Defaults to 0 if not defined.
    role_id: typing.Optional[int] = Field(None, alias='role_id')

    # The start date and time when the user clocked out. Formatted as ISO8601 datetime in UTC timezone.
    clocked_out: typing.Optional[datetime] = Field(None, alias='clocked_out')

    # Additional notes for a shift.
    notes: typing.Optional[str] = Field(None, alias='notes')

    # Tips declared for the shift in cents
    tips: typing.Optional[typing.Optional[int]] = Field(None, alias='tips')

    breaks: typing.Optional[TimePunchesCreateRequestBreaks] = Field(None, alias='breaks')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
