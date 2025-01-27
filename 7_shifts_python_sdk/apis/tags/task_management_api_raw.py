# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from 7_shifts_python_sdk.paths.v2_company_company_id_task_lists_list_id_tasks_task_id_clear.post import ClearTaskRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_list_templates.post import CreateTaskListTemplateRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_tags.post import CreateTaskTagsRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_list_templates_uuid.delete import DeleteTaskListTemplateRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_tags.delete import DeleteTaskTagsRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_list_templates_uuid.put import EditTaskListTemplateRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_management_settings.get import GetSettingsRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_lists_list_id.get import GetTaskListRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_list_templates_uuid.get import GetTaskListTemplateRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_list_templates.get import GetTaskListTemplatesRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_lists.get import GetTaskListsRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_list_daily_summary.get import ListTaskListsSummaryRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_task_lists_list_id_tasks_task_id_complete.post import MarkCompleteRaw


class TaskManagementApiRaw(
    ClearTaskRaw,
    CreateTaskListTemplateRaw,
    CreateTaskTagsRaw,
    DeleteTaskListTemplateRaw,
    DeleteTaskTagsRaw,
    EditTaskListTemplateRaw,
    GetSettingsRaw,
    GetTaskListRaw,
    GetTaskListTemplateRaw,
    GetTaskListTemplatesRaw,
    GetTaskListsRaw,
    ListTaskListsSummaryRaw,
    MarkCompleteRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
