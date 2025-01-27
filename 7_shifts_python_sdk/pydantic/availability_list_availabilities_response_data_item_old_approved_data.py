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


class AvailabilityListAvailabilitiesResponseDataItemOldApprovedData(BaseModel):
    # Availability ID
    id: int = Field(alias='id')

    # User ID
    user_id: int = Field(alias='user_id')

    # Company ID
    company_id: int = Field(alias='company_id')

    # Week date of the availability
    week: typing.Optional[str] = Field(alias='week')

    # Week to date of the availability
    week_to: typing.Optional[str] = Field(alias='week_to')

    # If true, availability is repeating
    repeat: bool = Field(alias='repeat')

    # Indicates the status of the availability
    status: int = Field(alias='status')

    # The availability status for the day
    mon: int = Field(alias='mon')

    # The start time of the availability for the day
    mon_from: str = Field(alias='mon_from')

    # The end time of the availability for the day
    mon_to: str = Field(alias='mon_to')

    # Comments included in the days availability
    mon_comments: typing.Optional[str] = Field(alias='mon_comments')

    # The reason ID for the day
    mon_reason: str = Field(alias='mon_reason')

    # The availability status for the day
    tue: int = Field(alias='tue')

    # The start time of the availability for the day
    tue_from: str = Field(alias='tue_from')

    # The end time of the availability for the day
    tue_to: str = Field(alias='tue_to')

    # Comments included in the days availability
    tue_comments: typing.Optional[str] = Field(alias='tue_comments')

    # The reason ID for the day
    tue_reason: str = Field(alias='tue_reason')

    # The availability status for the day
    wed: int = Field(alias='wed')

    # The start time of the availability for the day
    wed_from: str = Field(alias='wed_from')

    # The end time of the availability for the day
    wed_to: str = Field(alias='wed_to')

    # Comments included in the days availability
    wed_comments: typing.Optional[str] = Field(alias='wed_comments')

    # The reason ID for the day
    wed_reason: str = Field(alias='wed_reason')

    # The availability status for the day
    thu: int = Field(alias='thu')

    # The start time of the availability for the day
    thu_from: str = Field(alias='thu_from')

    # The end time of the availability for the day
    thu_to: str = Field(alias='thu_to')

    # Comments included in the days availability
    thu_comments: typing.Optional[str] = Field(alias='thu_comments')

    # The reason ID for the day
    thu_reason: str = Field(alias='thu_reason')

    # The availability status for the day
    fri: int = Field(alias='fri')

    # The start time of the availability for the day
    fri_from: str = Field(alias='fri_from')

    # The end time of the availability for the day
    fri_to: str = Field(alias='fri_to')

    # Comments included in the days availability
    fri_comments: typing.Optional[str] = Field(alias='fri_comments')

    # The reason ID for the day
    fri_reason: str = Field(alias='fri_reason')

    # The availability status for the day
    sat: int = Field(alias='sat')

    # The start time of the availability for the day
    sat_from: str = Field(alias='sat_from')

    # The end time of the availability for the day
    sat_to: str = Field(alias='sat_to')

    # Comments included in the days availability
    sat_comments: typing.Optional[str] = Field(alias='sat_comments')

    # The reason ID for the day
    sat_reason: str = Field(alias='sat_reason')

    # The availability status for the day
    sun: int = Field(alias='sun')

    # The start time of the availability for the day
    sun_from: str = Field(alias='sun_from')

    # The end time of the availability for the day
    sun_to: str = Field(alias='sun_to')

    # Comments included in the days availability
    sun_comments: typing.Optional[str] = Field(alias='sun_comments')

    # The reason ID for the day
    sun_reason: str = Field(alias='sun_reason')

    # The created date of the shift in UTC
    created: typing.Optional[datetime] = Field(alias='created')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
