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

from 7_shifts_python_sdk.type.task_management_get_task_list_templates200_response_data_item_assignments import TaskManagementGetTaskListTemplates200ResponseDataItemAssignments
from 7_shifts_python_sdk.type.task_management_get_task_list_templates200_response_data_item_task_templates import TaskManagementGetTaskListTemplates200ResponseDataItemTaskTemplates

class RequiredTaskManagementGetTaskListTemplates200ResponseDataItem(TypedDict):
    title: str

    description: typing.Optional[str]

    id: int

    company_id: int

    uuid: str

    status: int

    created: typing.Optional[datetime]

    activated_at: typing.Optional[datetime]

    task_templates: TaskManagementGetTaskListTemplates200ResponseDataItemTaskTemplates

    assignments: TaskManagementGetTaskListTemplates200ResponseDataItemAssignments

    # recurrence rules as defined by the RFC 5545 spec
    recurrence: str

class OptionalTaskManagementGetTaskListTemplates200ResponseDataItem(TypedDict, total=False):
    due: typing.Union[str]

    time_frame: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class TaskManagementGetTaskListTemplates200ResponseDataItem(RequiredTaskManagementGetTaskListTemplates200ResponseDataItem, OptionalTaskManagementGetTaskListTemplates200ResponseDataItem):
    pass