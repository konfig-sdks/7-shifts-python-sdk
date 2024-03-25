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


class RequiredDepartmentsUpdateDepartmentResponseData(TypedDict):
    # Department ID
    id: typing.Union[int, float]

    # Company ID
    company_id: typing.Union[int, float]

    # Location ID
    location_id: typing.Union[int, float]

    # Department name
    name: str

    # If true department is set as the default for the location
    default: bool

    # If true the location is deleted
    deleted: typing.Optional[str]

    created: str

    modified: str

class OptionalDepartmentsUpdateDepartmentResponseData(TypedDict, total=False):
    pass

class DepartmentsUpdateDepartmentResponseData(RequiredDepartmentsUpdateDepartmentResponseData, OptionalDepartmentsUpdateDepartmentResponseData):
    pass
