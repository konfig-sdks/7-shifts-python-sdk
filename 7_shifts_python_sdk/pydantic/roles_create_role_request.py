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

from 7_shifts_python_sdk.pydantic.roles_create_role_request_stations import RolesCreateRoleRequestStations

class RolesCreateRoleRequest(BaseModel):
    # Role name
    name: str = Field(alias='name')

    # A hex number representing the color
    color: str = Field(alias='color')

    # Location ID
    location_id: int = Field(alias='location_id')

    # Department ID. If this role is not assigned to a department, this value will be zero
    department_id: int = Field(alias='department_id')

    # The order in which the roles will be listed in the web app
    sort: typing.Optional[int] = Field(None, alias='sort')

    # Job code
    job_code: typing.Optional[str] = Field(None, alias='job_code')

    stations: typing.Optional[RolesCreateRoleRequestStations] = Field(None, alias='stations')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
