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


class TaskManagementListTaskListsSummary200ResponseDataTaskListsItem(BaseModel):
    title: str = Field(alias='title')

    description: typing.Optional[str] = Field(alias='description')

    completion_status: Literal["complete", "in_progress", "incomplete"] = Field(alias='completion_status')

    total_tasks_completed: int = Field(alias='total_tasks_completed')

    total_tasks: int = Field(alias='total_tasks')

    completion_percentage: int = Field(alias='completion_percentage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
