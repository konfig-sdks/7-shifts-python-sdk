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

from 7_shifts_python_sdk.type.receipts_list_response_data_item_receipt_lines_item_external_category_ids import ReceiptsListResponseDataItemReceiptLinesItemExternalCategoryIds

class RequiredReceiptsListResponseDataItemReceiptLinesItem(TypedDict):
    # The id of the location where this receipt was created
    location_id: int

    # The item ID available to the client
    external_item_id: str

    external_category_ids: ReceiptsListResponseDataItemReceiptLinesItemExternalCategoryIds

    # Quantity of this item
    quantity: int

    # Price in cents
    price: int

class OptionalReceiptsListResponseDataItemReceiptLinesItem(TypedDict, total=False):
    # Internal UUID of the receipt
    id: typing.Optional[str]

    # The item gross price in cents
    gross_item_price: typing.Optional[int]

    # The item net price pre-tax, post-discounts, pre-tips. In cents
    net_item_price: typing.Optional[int]

    # The item discount in cents
    item_discount: typing.Optional[int]

    # ISO8601 date and time in UTC when receipt was created in 7shifts system
    created_date: typing.Optional[datetime]

class ReceiptsListResponseDataItemReceiptLinesItem(RequiredReceiptsListResponseDataItemReceiptLinesItem, OptionalReceiptsListResponseDataItemReceiptLinesItem):
    pass