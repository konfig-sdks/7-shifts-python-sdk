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

from 7_shifts_python_sdk.pydantic.time_off_list200_response_data_item_hours import TimeOffList200ResponseDataItemHours

class TimeOffList200ResponseDataItem(BaseModel):
    id: int = Field(alias='id')

    user_id: int = Field(alias='user_id')

    company_id: int = Field(alias='company_id')

    from_date: str = Field(alias='from_date')

    to_date: str = Field(alias='to_date')

    partial: bool = Field(alias='partial')

    partial_from: typing.Optional[str] = Field(alias='partial_from')

    partial_to: typing.Optional[str] = Field(alias='partial_to')

    comments: str = Field(alias='comments')

    status: int = Field(alias='status')

    status_action_user_id: typing.Optional[int] = Field(alias='status_action_user_id')

    status_action_message: str = Field(alias='status_action_message')

    category: str = Field(alias='category')

    created: str = Field(alias='created')

    amount_of_hours: typing.Union[int, float] = Field(alias='amount_of_hours')

    hours: TimeOffList200ResponseDataItemHours = Field(alias='hours')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
