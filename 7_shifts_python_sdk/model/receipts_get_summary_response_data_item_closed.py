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


class ReceiptsGetSummaryResponseDataItemClosed(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            receipt_count = schemas.Int64Schema
            net_total = schemas.Int64Schema
            gross_total = schemas.Int64Schema
            tip_total = schemas.Int64Schema
            receipt_discounts = schemas.Int64Schema
            __annotations__ = {
                "receipt_count": receipt_count,
                "net_total": net_total,
                "gross_total": gross_total,
                "tip_total": tip_total,
                "receipt_discounts": receipt_discounts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_count"]) -> MetaOapg.properties.receipt_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_total"]) -> MetaOapg.properties.net_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_total"]) -> MetaOapg.properties.gross_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_total"]) -> MetaOapg.properties.tip_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_discounts"]) -> MetaOapg.properties.receipt_discounts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["receipt_count", "net_total", "gross_total", "tip_total", "receipt_discounts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_count"]) -> typing.Union[MetaOapg.properties.receipt_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_total"]) -> typing.Union[MetaOapg.properties.net_total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_total"]) -> typing.Union[MetaOapg.properties.gross_total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_total"]) -> typing.Union[MetaOapg.properties.tip_total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_discounts"]) -> typing.Union[MetaOapg.properties.receipt_discounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["receipt_count", "net_total", "gross_total", "tip_total", "receipt_discounts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        receipt_count: typing.Union[MetaOapg.properties.receipt_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        net_total: typing.Union[MetaOapg.properties.net_total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        gross_total: typing.Union[MetaOapg.properties.gross_total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tip_total: typing.Union[MetaOapg.properties.tip_total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        receipt_discounts: typing.Union[MetaOapg.properties.receipt_discounts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReceiptsGetSummaryResponseDataItemClosed':
        return super().__new__(
            cls,
            *args,
            receipt_count=receipt_count,
            net_total=net_total,
            gross_total=gross_total,
            tip_total=tip_total,
            receipt_discounts=receipt_discounts,
            _configuration=_configuration,
            **kwargs,
        )