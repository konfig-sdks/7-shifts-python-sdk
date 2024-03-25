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

from 7_shifts_python_sdk.type.task_management_get_task_list_response_data_assignments import TaskManagementGetTaskListResponseDataAssignments
from 7_shifts_python_sdk.type.task_management_get_task_list_response_data_due_date import TaskManagementGetTaskListResponseDataDueDate
from 7_shifts_python_sdk.type.task_management_get_task_list_response_data_recurrence import TaskManagementGetTaskListResponseDataRecurrence
from 7_shifts_python_sdk.type.task_management_get_task_list_response_data_tasks import TaskManagementGetTaskListResponseDataTasks

class RequiredTaskManagementGetTaskListResponseData(TypedDict):
    title: str

    description: str

    id: int

    task_list_template_uuid: str

    start: datetime

    due: datetime

    due_date: TaskManagementGetTaskListResponseDataDueDate

    tasks: TaskManagementGetTaskListResponseDataTasks

    recurrence: TaskManagementGetTaskListResponseDataRecurrence

    assignments: TaskManagementGetTaskListResponseDataAssignments

class OptionalTaskManagementGetTaskListResponseData(TypedDict, total=False):
    time_frame: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class TaskManagementGetTaskListResponseData(RequiredTaskManagementGetTaskListResponseData, OptionalTaskManagementGetTaskListResponseData):
    pass
