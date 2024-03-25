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

from 7_shifts_python_sdk.pydantic.receipts_get_receipt_response_data_receipt_lines import ReceiptsGetReceiptResponseDataReceiptLines
from 7_shifts_python_sdk.pydantic.receipts_get_receipt_response_data_tip_details import ReceiptsGetReceiptResponseDataTipDetails

class ReceiptsGetReceiptResponseData(BaseModel):
    # The id of the location where this receipt was created
    location_id: int = Field(alias='location_id')

    # ID available to the client in the POS UI. Be it a GUID, a receipt number, a composite of date and ID and terminal, etc
    receipt_id: str = Field(alias='receipt_id')

    # Net total of the receipt in cents, pre tax, post-discounts, pre tips
    net_total: int = Field(alias='net_total')

    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The id of the company
    company_id: typing.Optional[int] = Field(None, alias='company_id')

    # The ID of the POS system that generated the receipt
    pos_id: typing.Optional[int] = Field(None, alias='pos_id')

    # ISO8601 date and time in UTC when receipt was created
    receipt_date: typing.Optional[datetime] = Field(None, alias='receipt_date')

    # ISO8601 date and time in UTC when receipt was closed
    receipt_close_date: typing.Optional[datetime] = Field(None, alias='receipt_close_date')

    # Gross total of the receipt in cents
    gross_total: typing.Optional[int] = Field(None, alias='gross_total')

    # Total tips in cents
    tips: typing.Optional[int] = Field(None, alias='tips')

    # Total receipt discounts in cents
    total_receipt_discounts: typing.Optional[int] = Field(None, alias='total_receipt_discounts')

    # Item discounts in cents
    total_item_discounts: typing.Optional[int] = Field(None, alias='total_item_discounts')

    # ID available to the client in the POS UI. Representing the user responsible for creation of receipt.
    external_user_id: typing.Optional[typing.Optional[str]] = Field(None, alias='external_user_id')

    # ID of the revenue center
    revenue_center: typing.Optional[typing.Optional[str]] = Field(None, alias='revenue_center')

    receipt_lines: typing.Optional[ReceiptsGetReceiptResponseDataReceiptLines] = Field(None, alias='receipt_lines')

    tip_details: typing.Optional[ReceiptsGetReceiptResponseDataTipDetails] = Field(None, alias='tip_details')

    # Status of the receipt
    status: typing.Optional[Literal["open", "closed", "voided", "deleted"]] = Field(None, alias='status')

    # ISO8601 date and time in UTC when receipt was created in 7shifts system
    created_date: typing.Optional[datetime] = Field(None, alias='created_date')

    # ISO8601 date and time in UTC when receipt was last updated in 7shifts system
    modified_date: typing.Optional[datetime] = Field(None, alias='modified_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
