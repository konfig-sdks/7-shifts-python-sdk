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

from 7_shifts_python_sdk.type.log_book_create_post_response_data_attachments import LogBookCreatePostResponseDataAttachments

class RequiredLogBookCreatePostResponseData(TypedDict):
    id: int

    uuid: str

    location_id: int

    user_id: int

    log_book_category_id: int

    # The posted date. Format YYYY-MM-DD
    date: str

    message: str

    attachments: typing.Optional[LogBookCreatePostResponseDataAttachments]

    log_book_comment_count: int

    created: datetime

class OptionalLogBookCreatePostResponseData(TypedDict, total=False):
    pass

class LogBookCreatePostResponseData(RequiredLogBookCreatePostResponseData, OptionalLogBookCreatePostResponseData):
    pass
