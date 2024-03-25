# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from 7_shifts_python_sdk import schemas  # noqa: F401


class TaskManagementGetTaskListTemplateResponseDataAssignments(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TaskManagementGetTaskListTemplateResponseDataAssignmentsItem']:
            return TaskManagementGetTaskListTemplateResponseDataAssignmentsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TaskManagementGetTaskListTemplateResponseDataAssignmentsItem'], typing.List['TaskManagementGetTaskListTemplateResponseDataAssignmentsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TaskManagementGetTaskListTemplateResponseDataAssignments':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TaskManagementGetTaskListTemplateResponseDataAssignmentsItem':
        return super().__getitem__(i)

from 7_shifts_python_sdk.model.task_management_get_task_list_template_response_data_assignments_item import TaskManagementGetTaskListTemplateResponseDataAssignmentsItem
