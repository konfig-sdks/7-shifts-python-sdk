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

from 7_shifts_python_sdk.type.availability_get_by_id_response_data_old_approved_data import AvailabilityGetByIdResponseDataOldApprovedData

class RequiredAvailabilityGetByIdResponseData(TypedDict):
    # Availability ID
    id: int

    # User ID
    user_id: int

    # Company ID
    company_id: int

    # Week date of the availability
    week: typing.Optional[str]

    # Week to date of the availability
    week_to: typing.Optional[str]

    # If true, availability is repeating
    repeat: bool

    # Indicates the status of the availability
    status: int

    # The user ID of the user that approved/declined the availability
    status_action_user_id: typing.Optional[int]

    # The message when the availability was approved/declined
    status_action_message: typing.Optional[str]

    # The availability status for the day
    mon: int

    # The start time of the availability for the day
    mon_from: str

    # The end time of the availability for the day
    mon_to: str

    # Comments included in the days availability
    mon_comments: typing.Optional[str]

    # The reason ID for the day
    mon_reason: str

    # The availability status for the day
    tue: int

    # The start time of the availability for the day
    tue_from: str

    # The end time of the availability for the day
    tue_to: str

    # Comments included in the days availability
    tue_comments: typing.Optional[str]

    # The reason ID for the day
    tue_reason: str

    # The availability status for the day
    wed: int

    # The start time of the availability for the day
    wed_from: str

    # The end time of the availability for the day
    wed_to: str

    # Comments included in the days availability
    wed_comments: typing.Optional[str]

    # The reason ID for the day
    wed_reason: str

    # The availability status for the day
    thu: int

    # The start time of the availability for the day
    thu_from: str

    # The end time of the availability for the day
    thu_to: str

    # Comments included in the days availability
    thu_comments: typing.Optional[str]

    # The reason ID for the day
    thu_reason: str

    # The availability status for the day
    fri: int

    # The start time of the availability for the day
    fri_from: str

    # The end time of the availability for the day
    fri_to: str

    # Comments included in the days availability
    fri_comments: typing.Optional[str]

    # The reason ID for the day
    fri_reason: str

    # The availability status for the day
    sat: int

    # The start time of the availability for the day
    sat_from: str

    # The end time of the availability for the day
    sat_to: str

    # Comments included in the days availability
    sat_comments: typing.Optional[str]

    # The reason ID for the day
    sat_reason: str

    # The availability status for the day
    sun: int

    # The start time of the availability for the day
    sun_from: str

    # The end time of the availability for the day
    sun_to: str

    # Comments included in the days availability
    sun_comments: typing.Optional[str]

    # The reason ID for the day
    sun_reason: str

    # The created date of the shift in UTC
    created: typing.Optional[str]

    # The last modified date of the shift in UTC
    modified: typing.Optional[str]

class OptionalAvailabilityGetByIdResponseData(TypedDict, total=False):
    old_approved_data: typing.Optional[AvailabilityGetByIdResponseDataOldApprovedData]

class AvailabilityGetByIdResponseData(RequiredAvailabilityGetByIdResponseData, OptionalAvailabilityGetByIdResponseData):
    pass
