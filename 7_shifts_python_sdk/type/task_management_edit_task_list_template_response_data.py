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

from 7_shifts_python_sdk.type.task_management_edit_task_list_template_response_data_assignments import TaskManagementEditTaskListTemplateResponseDataAssignments
from 7_shifts_python_sdk.type.task_management_edit_task_list_template_response_data_task_templates import TaskManagementEditTaskListTemplateResponseDataTaskTemplates

class RequiredTaskManagementEditTaskListTemplateResponseData(TypedDict):
    title: str

    description: typing.Optional[str]

    id: int

    company_id: int

    uuid: str

    status: int

    created: typing.Optional[datetime]

    activated_at: typing.Optional[datetime]

    task_templates: TaskManagementEditTaskListTemplateResponseDataTaskTemplates

    assignments: TaskManagementEditTaskListTemplateResponseDataAssignments

    # recurrence rules as defined by the RFC 5545 spec
    recurrence: str

class OptionalTaskManagementEditTaskListTemplateResponseData(TypedDict, total=False):
    due: typing.Union[str]

    time_frame: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class TaskManagementEditTaskListTemplateResponseData(RequiredTaskManagementEditTaskListTemplateResponseData, OptionalTaskManagementEditTaskListTemplateResponseData):
    pass
