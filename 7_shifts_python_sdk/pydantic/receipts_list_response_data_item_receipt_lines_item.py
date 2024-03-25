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

from 7_shifts_python_sdk.pydantic.receipts_list_response_data_item_receipt_lines_item_external_category_ids import ReceiptsListResponseDataItemReceiptLinesItemExternalCategoryIds

class ReceiptsListResponseDataItemReceiptLinesItem(BaseModel):
    # The id of the location where this receipt was created
    location_id: int = Field(alias='location_id')

    # The item ID available to the client
    external_item_id: str = Field(alias='external_item_id')

    external_category_ids: ReceiptsListResponseDataItemReceiptLinesItemExternalCategoryIds = Field(alias='external_category_ids')

    # Quantity of this item
    quantity: int = Field(alias='quantity')

    # Price in cents
    price: int = Field(alias='price')

    # Internal UUID of the receipt
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    # The item gross price in cents
    gross_item_price: typing.Optional[typing.Optional[int]] = Field(None, alias='gross_item_price')

    # The item net price pre-tax, post-discounts, pre-tips. In cents
    net_item_price: typing.Optional[typing.Optional[int]] = Field(None, alias='net_item_price')

    # The item discount in cents
    item_discount: typing.Optional[typing.Optional[int]] = Field(None, alias='item_discount')

    # ISO8601 date and time in UTC when receipt was created in 7shifts system
    created_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='created_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
