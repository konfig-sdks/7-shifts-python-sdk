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

from 7_shifts_python_sdk.pydantic.task_management_list_task_lists_summary200_response_data_task_lists import TaskManagementListTaskListsSummary200ResponseDataTaskLists

class TaskManagementListTaskListsSummary200ResponseData(BaseModel):
    total_completed_percentage: int = Field(alias='total_completed_percentage')

    total_in_progress_percentage: int = Field(alias='total_in_progress_percentage')

    total_incomplete_percentage: int = Field(alias='total_incomplete_percentage')

    report_time: datetime = Field(alias='report_time')

    # A date with YYYY-MM-DD format
    date: str = Field(alias='date')

    has_recent_task_completed: bool = Field(alias='has_recent_task_completed')

    task_lists: TaskManagementListTaskListsSummary200ResponseDataTaskLists = Field(alias='task_lists')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
