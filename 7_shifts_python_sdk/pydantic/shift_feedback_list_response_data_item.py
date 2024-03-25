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


class ShiftFeedbackListResponseDataItem(BaseModel):
    # ID for the shift feedback
    id: int = Field(alias='id')

    # Location ID
    location_id: int = Field(alias='location_id')

    # Department ID
    department_id: int = Field(alias='department_id')

    # Role ID
    role_id: int = Field(alias='role_id')

    # Shift start time
    start: datetime = Field(alias='start')

    # Shift end time
    end: datetime = Field(alias='end')

    # Shift ID
    shift_id: int = Field(alias='shift_id')

    # User ID
    user_id: int = Field(alias='user_id')

    # If the user was notified to provide shift feedback
    notified: bool = Field(alias='notified')

    # Rating of the shift
    rating: int = Field(alias='rating')

    # Comments about the shift
    comments: str = Field(alias='comments')

    # If the shift feedback request was dismissed
    dismissed: bool = Field(alias='dismissed')

    # Station name
    station_name: str = Field(alias='station_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
