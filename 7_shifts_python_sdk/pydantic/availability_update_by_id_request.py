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


class AvailabilityUpdateByIdRequest(BaseModel):
    # Week date of the availability
    week: typing.Optional[typing.Optional[str]] = Field(None, alias='week')

    # Week to date of the availability
    week_to: typing.Optional[typing.Optional[str]] = Field(None, alias='week_to')

    # If true, availability is repeating
    repeat: typing.Optional[bool] = Field(None, alias='repeat')

    # The availability status for the day
    mon: typing.Optional[int] = Field(None, alias='mon')

    # The start time of the availability for the day
    mon_from: typing.Optional[str] = Field(None, alias='mon_from')

    # The end time of the availability for the day
    mon_to: typing.Optional[str] = Field(None, alias='mon_to')

    # Comments included in the days availability
    mon_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='mon_comments')

    # The reason ID for the day
    mon_reason: typing.Optional[str] = Field(None, alias='mon_reason')

    # The availability status for the day
    tue: typing.Optional[int] = Field(None, alias='tue')

    # The start time of the availability for the day
    tue_from: typing.Optional[str] = Field(None, alias='tue_from')

    # The end time of the availability for the day
    tue_to: typing.Optional[str] = Field(None, alias='tue_to')

    # Comments included in the days availability
    tue_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='tue_comments')

    # The reason ID for the day
    tue_reason: typing.Optional[str] = Field(None, alias='tue_reason')

    # The availability status for the day
    wed: typing.Optional[int] = Field(None, alias='wed')

    # The start time of the availability for the day
    wed_from: typing.Optional[str] = Field(None, alias='wed_from')

    # The end time of the availability for the day
    wed_to: typing.Optional[str] = Field(None, alias='wed_to')

    # Comments included in the days availability
    wed_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='wed_comments')

    # The reason ID for the day
    wed_reason: typing.Optional[str] = Field(None, alias='wed_reason')

    # The availability status for the day
    thu: typing.Optional[int] = Field(None, alias='thu')

    # The start time of the availability for the day
    thu_from: typing.Optional[str] = Field(None, alias='thu_from')

    # The end time of the availability for the day
    thu_to: typing.Optional[str] = Field(None, alias='thu_to')

    # Comments included in the days availability
    thu_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='thu_comments')

    # The reason ID for the day
    thu_reason: typing.Optional[str] = Field(None, alias='thu_reason')

    # The availability status for the day
    fri: typing.Optional[int] = Field(None, alias='fri')

    # The start time of the availability for the day
    fri_from: typing.Optional[str] = Field(None, alias='fri_from')

    # The end time of the availability for the day
    fri_to: typing.Optional[str] = Field(None, alias='fri_to')

    # Comments included in the days availability
    fri_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='fri_comments')

    # The reason ID for the day
    fri_reason: typing.Optional[str] = Field(None, alias='fri_reason')

    # The availability status for the day
    sat: typing.Optional[int] = Field(None, alias='sat')

    # The start time of the availability for the day
    sat_from: typing.Optional[str] = Field(None, alias='sat_from')

    # The end time of the availability for the day
    sat_to: typing.Optional[str] = Field(None, alias='sat_to')

    # Comments included in the days availability
    sat_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='sat_comments')

    # The reason ID for the day
    sat_reason: typing.Optional[str] = Field(None, alias='sat_reason')

    # The availability status for the day
    sun: typing.Optional[int] = Field(None, alias='sun')

    # The start time of the availability for the day
    sun_from: typing.Optional[str] = Field(None, alias='sun_from')

    # The end time of the availability for the day
    sun_to: typing.Optional[str] = Field(None, alias='sun_to')

    # Comments included in the days availability
    sun_comments: typing.Optional[typing.Optional[str]] = Field(None, alias='sun_comments')

    # The reason ID for the day
    sun_reason: typing.Optional[str] = Field(None, alias='sun_reason')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
