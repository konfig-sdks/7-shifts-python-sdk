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

from 7_shifts_python_sdk.type.receipts_list_response_data_item_receipt_lines import ReceiptsListResponseDataItemReceiptLines
from 7_shifts_python_sdk.type.receipts_list_response_data_item_tip_details import ReceiptsListResponseDataItemTipDetails

class RequiredReceiptsListResponseDataItem(TypedDict):
    # The id of the location where this receipt was created
    location_id: int

    # ID available to the client in the POS UI. Be it a GUID, a receipt number, a composite of date and ID and terminal, etc
    receipt_id: str

    # Net total of the receipt in cents, pre tax, post-discounts, pre tips
    net_total: int

class OptionalReceiptsListResponseDataItem(TypedDict, total=False):
    uuid: str

    # The id of the company
    company_id: int

    # The ID of the POS system that generated the receipt
    pos_id: int

    # ISO8601 date and time in UTC when receipt was created
    receipt_date: datetime

    # ISO8601 date and time in UTC when receipt was closed
    receipt_close_date: datetime

    # Gross total of the receipt in cents
    gross_total: int

    # Total tips in cents
    tips: int

    # Total receipt discounts in cents
    total_receipt_discounts: int

    # Item discounts in cents
    total_item_discounts: int

    # ID available to the client in the POS UI. Representing the user responsible for creation of receipt.
    external_user_id: typing.Optional[str]

    # ID of the revenue center
    revenue_center: typing.Optional[str]

    receipt_lines: ReceiptsListResponseDataItemReceiptLines

    tip_details: ReceiptsListResponseDataItemTipDetails

    # Status of the receipt
    status: str

    # ISO8601 date and time in UTC when receipt was created in 7shifts system
    created_date: datetime

    # ISO8601 date and time in UTC when receipt was last updated in 7shifts system
    modified_date: datetime

class ReceiptsListResponseDataItem(RequiredReceiptsListResponseDataItem, OptionalReceiptsListResponseDataItem):
    pass