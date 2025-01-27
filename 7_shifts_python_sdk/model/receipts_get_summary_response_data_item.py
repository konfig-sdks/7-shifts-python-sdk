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


class ReceiptsGetSummaryResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            date = schemas.DateSchema
        
            @staticmethod
            def open() -> typing.Type['ReceiptsGetSummaryResponseDataItemOpen']:
                return ReceiptsGetSummaryResponseDataItemOpen
        
            @staticmethod
            def closed() -> typing.Type['ReceiptsGetSummaryResponseDataItemClosed']:
                return ReceiptsGetSummaryResponseDataItemClosed
        
            @staticmethod
            def voided() -> typing.Type['ReceiptsGetSummaryResponseDataItemVoided']:
                return ReceiptsGetSummaryResponseDataItemVoided
        
            @staticmethod
            def deleted() -> typing.Type['ReceiptsGetSummaryResponseDataItemDeleted']:
                return ReceiptsGetSummaryResponseDataItemDeleted
            __annotations__ = {
                "date": date,
                "open": open,
                "closed": closed,
                "voided": voided,
                "deleted": deleted,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["open"]) -> 'ReceiptsGetSummaryResponseDataItemOpen': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed"]) -> 'ReceiptsGetSummaryResponseDataItemClosed': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voided"]) -> 'ReceiptsGetSummaryResponseDataItemVoided': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> 'ReceiptsGetSummaryResponseDataItemDeleted': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "open", "closed", "voided", "deleted", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["open"]) -> typing.Union['ReceiptsGetSummaryResponseDataItemOpen', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed"]) -> typing.Union['ReceiptsGetSummaryResponseDataItemClosed', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voided"]) -> typing.Union['ReceiptsGetSummaryResponseDataItemVoided', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union['ReceiptsGetSummaryResponseDataItemDeleted', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "open", "closed", "voided", "deleted", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        open: typing.Union['ReceiptsGetSummaryResponseDataItemOpen', schemas.Unset] = schemas.unset,
        closed: typing.Union['ReceiptsGetSummaryResponseDataItemClosed', schemas.Unset] = schemas.unset,
        voided: typing.Union['ReceiptsGetSummaryResponseDataItemVoided', schemas.Unset] = schemas.unset,
        deleted: typing.Union['ReceiptsGetSummaryResponseDataItemDeleted', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReceiptsGetSummaryResponseDataItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            open=open,
            closed=closed,
            voided=voided,
            deleted=deleted,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.receipts_get_summary_response_data_item_closed import ReceiptsGetSummaryResponseDataItemClosed
from 7_shifts_python_sdk.model.receipts_get_summary_response_data_item_deleted import ReceiptsGetSummaryResponseDataItemDeleted
from 7_shifts_python_sdk.model.receipts_get_summary_response_data_item_open import ReceiptsGetSummaryResponseDataItemOpen
from 7_shifts_python_sdk.model.receipts_get_summary_response_data_item_voided import ReceiptsGetSummaryResponseDataItemVoided
