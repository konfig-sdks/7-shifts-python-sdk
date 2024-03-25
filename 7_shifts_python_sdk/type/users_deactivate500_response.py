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


class RequiredUsersDeactivate500Response(TypedDict):
    # A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
    title: str

    # The primary identifier for the problem type (URI reference).
    type: str

    # The HTTP status code.
    status: int

    # A human-readable explanation specific to this occurrence of the problem.
    detail: str

class OptionalUsersDeactivate500Response(TypedDict, total=False):
    # The error code can be used to look up the reason why the request failed.
    code: int

    # The request parameter that this error is related to.
    param: str

class UsersDeactivate500Response(RequiredUsersDeactivate500Response, OptionalUsersDeactivate500Response):
    pass
