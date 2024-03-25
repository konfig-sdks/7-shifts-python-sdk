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

from 7_shifts_python_sdk.pydantic.receipts_get_summary_response_data_item_closed import ReceiptsGetSummaryResponseDataItemClosed
from 7_shifts_python_sdk.pydantic.receipts_get_summary_response_data_item_deleted import ReceiptsGetSummaryResponseDataItemDeleted
from 7_shifts_python_sdk.pydantic.receipts_get_summary_response_data_item_open import ReceiptsGetSummaryResponseDataItemOpen
from 7_shifts_python_sdk.pydantic.receipts_get_summary_response_data_item_voided import ReceiptsGetSummaryResponseDataItemVoided

class ReceiptsGetSummaryResponseDataItem(BaseModel):
    date: typing.Optional[date] = Field(None, alias='date')

    open: typing.Optional[ReceiptsGetSummaryResponseDataItemOpen] = Field(None, alias='open')

    closed: typing.Optional[ReceiptsGetSummaryResponseDataItemClosed] = Field(None, alias='closed')

    voided: typing.Optional[ReceiptsGetSummaryResponseDataItemVoided] = Field(None, alias='voided')

    deleted: typing.Optional[ReceiptsGetSummaryResponseDataItemDeleted] = Field(None, alias='deleted')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )