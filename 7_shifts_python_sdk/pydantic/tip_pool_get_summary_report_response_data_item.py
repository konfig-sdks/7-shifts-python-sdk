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

from 7_shifts_python_sdk.pydantic.tip_pool_get_summary_report_response_data_item_assigned_tips import TipPoolGetSummaryReportResponseDataItemAssignedTips
from 7_shifts_python_sdk.pydantic.tip_pool_get_summary_report_response_data_item_total import TipPoolGetSummaryReportResponseDataItemTotal
from 7_shifts_python_sdk.pydantic.tip_pool_get_summary_report_response_data_item_unassigned_tips import TipPoolGetSummaryReportResponseDataItemUnassignedTips

class TipPoolGetSummaryReportResponseDataItem(BaseModel):
    # The tip pool UUID
    tip_pool_uuid: str = Field(alias='tip_pool_uuid')

    # The tip pool name
    tip_pool_name: str = Field(alias='tip_pool_name')

    unassigned_tips: TipPoolGetSummaryReportResponseDataItemUnassignedTips = Field(alias='unassigned_tips')

    assigned_tips: TipPoolGetSummaryReportResponseDataItemAssignedTips = Field(alias='assigned_tips')

    total: TipPoolGetSummaryReportResponseDataItemTotal = Field(alias='total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )