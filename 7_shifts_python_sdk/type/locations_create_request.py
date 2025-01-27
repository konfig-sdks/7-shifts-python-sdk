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


class RequiredLocationsCreateRequest(TypedDict):
    # Location name
    name: str

    # Country two letter abbreviation
    country: str

class OptionalLocationsCreateRequest(TypedDict, total=False):
    # Full address
    formatted_address: str

    # State or province
    state: typing.Optional[str]

    # City
    city: typing.Optional[str]

    # locations latitude coordinates
    latitude: str

    # locations longitude coordinates
    longitude: str

    # Google Places location Id
    place_id: str

    # Timezone. Valid zone info name
    timezone: str

    # When true, holiday pay is enabled
    holiday_pay: bool

    # Sunday closing time
    sun_hours_close: str

    # Monday closing time
    mon_hours_close: str

    # Tuesday closing time
    tue_hours_close: str

    # Wednesday closing time
    wed_hours_close: str

    # Thursday closing time
    thu_hours_close: str

    # Friday closing time
    fri_hours_close: str

    # Saturday closing time
    sat_hours_close: str

    # Sunday opening time
    sun_hours_open: str

    # Monday opening time
    mon_hours_open: typing.Optional[str]

    # Tuesday opening time
    tue_hours_open: typing.Optional[str]

    # Wednesday opening time
    wed_hours_open: typing.Optional[str]

    # Thursday opening time
    thu_hours_open: typing.Optional[str]

    # Friday opening time
    fri_hours_open: typing.Optional[str]

    # Saturday opening time
    sat_hours_open: typing.Optional[str]

    # If true, location is closed on Sunday
    sun_is_closed: typing.Optional[bool]

    # If true, location is closed on Monday
    mon_is_closed: typing.Optional[bool]

    # If true, location is closed on Tuesday
    tue_is_closed: typing.Optional[bool]

    # If true, location is closed on Wednesday
    wed_is_closed: typing.Optional[bool]

    # If true, location is closed on Thursday
    thu_is_closed: typing.Optional[bool]

    # If true, location is closed on Friday
    fri_is_closed: typing.Optional[bool]

    # If true, location is closed on Saturday
    sat_is_closed: typing.Optional[bool]

    # If true end of shift feedback requests are enabled
    enable_shift_feedback: bool

    # If true end of shift feedback requests are enabled
    shift_feedback: bool

    # Optional coupon to apply to this location's billing
    coupon: typing.Optional[str]

    # Optional stripe payment token. If this is not provided, the account's default payment information will be used.
    stripe_token_id: str

    # Optional existing location id whose department and role structure the new location should copy
    copy_from_id: typing.Optional[int]

class LocationsCreateRequest(RequiredLocationsCreateRequest, OptionalLocationsCreateRequest):
    pass
