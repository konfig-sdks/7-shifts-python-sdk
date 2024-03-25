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

from 7_shifts_python_sdk.pydantic.task_management_get_task_lists_response_data_item_tasks_item_tags import TaskManagementGetTaskListsResponseDataItemTasksItemTags

class TaskManagementGetTaskListsResponseDataItemTasksItem(BaseModel):
    title: str = Field(alias='title')

    id: int = Field(alias='id')

    user_id: typing.Optional[int] = Field(alias='user_id')

    completed_at: typing.Optional[datetime] = Field(alias='completed_at')

    tags: typing.Optional[TaskManagementGetTaskListsResponseDataItemTasksItemTags] = Field(None, alias='tags')

    description: typing.Optional[str] = Field(None, alias='description')

    task_template_uuid: typing.Optional[str] = Field(None, alias='task_template_uuid')

    task_completion: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='task_completion')

    task_completion_event: typing.Optional[typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='task_completion_event')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
