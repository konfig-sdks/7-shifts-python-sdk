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

from 7_shifts_python_sdk.type.roles_update_role_by_id_request_stations import RolesUpdateRoleByIdRequestStations

class RequiredRolesUpdateRoleByIdRequest(TypedDict):
    pass

class OptionalRolesUpdateRoleByIdRequest(TypedDict, total=False):
    # Department ID. If this role is not assigned to a department, this value will be zero
    department_id: int

    # The order in which the roles will be listed in the web app
    sort: int

    # A hex number representing the color
    color: str

    # Role name
    name: str

    # Job code
    job_code: str

    stations: RolesUpdateRoleByIdRequestStations

class RolesUpdateRoleByIdRequest(RequiredRolesUpdateRoleByIdRequest, OptionalRolesUpdateRoleByIdRequest):
    pass
