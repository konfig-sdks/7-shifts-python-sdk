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


class ReceiptsUpdateReceiptRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "net_total",
        }
        
        class properties:
            net_total = schemas.IntSchema
            receipt_date = schemas.DateTimeSchema
            gross_total = schemas.IntSchema
            
            
            class total_receipt_discounts(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            tips = schemas.IntSchema
            external_user_id = schemas.StrSchema
            revenue_center = schemas.StrSchema
        
            @staticmethod
            def receipt_lines() -> typing.Type['ReceiptsUpdateReceiptRequestReceiptLines']:
                return ReceiptsUpdateReceiptRequestReceiptLines
        
            @staticmethod
            def tip_details() -> typing.Type['ReceiptsUpdateReceiptRequestTipDetails']:
                return ReceiptsUpdateReceiptRequestTipDetails
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "open": "OPEN",
                        "closed": "CLOSED",
                        "voided": "VOIDED",
                        "deleted": "DELETED",
                    }
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("closed")
                
                @schemas.classproperty
                def VOIDED(cls):
                    return cls("voided")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("deleted")
            
            
            class order_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "dine_in": "DINE_IN",
                        "delivery": "DELIVERY",
                        "take_out": "TAKE_OUT",
                    }
                
                @schemas.classproperty
                def DINE_IN(cls):
                    return cls("dine_in")
                
                @schemas.classproperty
                def DELIVERY(cls):
                    return cls("delivery")
                
                @schemas.classproperty
                def TAKE_OUT(cls):
                    return cls("take_out")
            dining_option = schemas.StrSchema
            __annotations__ = {
                "net_total": net_total,
                "receipt_date": receipt_date,
                "gross_total": gross_total,
                "total_receipt_discounts": total_receipt_discounts,
                "tips": tips,
                "external_user_id": external_user_id,
                "revenue_center": revenue_center,
                "receipt_lines": receipt_lines,
                "tip_details": tip_details,
                "status": status,
                "order_type": order_type,
                "dining_option": dining_option,
            }
    
    net_total: MetaOapg.properties.net_total
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_total"]) -> MetaOapg.properties.net_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_date"]) -> MetaOapg.properties.receipt_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_total"]) -> MetaOapg.properties.gross_total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_receipt_discounts"]) -> MetaOapg.properties.total_receipt_discounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tips"]) -> MetaOapg.properties.tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_user_id"]) -> MetaOapg.properties.external_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenue_center"]) -> MetaOapg.properties.revenue_center: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_lines"]) -> 'ReceiptsUpdateReceiptRequestReceiptLines': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_details"]) -> 'ReceiptsUpdateReceiptRequestTipDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_type"]) -> MetaOapg.properties.order_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dining_option"]) -> MetaOapg.properties.dining_option: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["net_total", "receipt_date", "gross_total", "total_receipt_discounts", "tips", "external_user_id", "revenue_center", "receipt_lines", "tip_details", "status", "order_type", "dining_option", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_total"]) -> MetaOapg.properties.net_total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_date"]) -> typing.Union[MetaOapg.properties.receipt_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_total"]) -> typing.Union[MetaOapg.properties.gross_total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_receipt_discounts"]) -> typing.Union[MetaOapg.properties.total_receipt_discounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tips"]) -> typing.Union[MetaOapg.properties.tips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_user_id"]) -> typing.Union[MetaOapg.properties.external_user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenue_center"]) -> typing.Union[MetaOapg.properties.revenue_center, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_lines"]) -> typing.Union['ReceiptsUpdateReceiptRequestReceiptLines', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_details"]) -> typing.Union['ReceiptsUpdateReceiptRequestTipDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_type"]) -> typing.Union[MetaOapg.properties.order_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dining_option"]) -> typing.Union[MetaOapg.properties.dining_option, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["net_total", "receipt_date", "gross_total", "total_receipt_discounts", "tips", "external_user_id", "revenue_center", "receipt_lines", "tip_details", "status", "order_type", "dining_option", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        net_total: typing.Union[MetaOapg.properties.net_total, decimal.Decimal, int, ],
        receipt_date: typing.Union[MetaOapg.properties.receipt_date, str, datetime, schemas.Unset] = schemas.unset,
        gross_total: typing.Union[MetaOapg.properties.gross_total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_receipt_discounts: typing.Union[MetaOapg.properties.total_receipt_discounts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tips: typing.Union[MetaOapg.properties.tips, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        external_user_id: typing.Union[MetaOapg.properties.external_user_id, str, schemas.Unset] = schemas.unset,
        revenue_center: typing.Union[MetaOapg.properties.revenue_center, str, schemas.Unset] = schemas.unset,
        receipt_lines: typing.Union['ReceiptsUpdateReceiptRequestReceiptLines', schemas.Unset] = schemas.unset,
        tip_details: typing.Union['ReceiptsUpdateReceiptRequestTipDetails', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        order_type: typing.Union[MetaOapg.properties.order_type, str, schemas.Unset] = schemas.unset,
        dining_option: typing.Union[MetaOapg.properties.dining_option, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReceiptsUpdateReceiptRequest':
        return super().__new__(
            cls,
            *args,
            net_total=net_total,
            receipt_date=receipt_date,
            gross_total=gross_total,
            total_receipt_discounts=total_receipt_discounts,
            tips=tips,
            external_user_id=external_user_id,
            revenue_center=revenue_center,
            receipt_lines=receipt_lines,
            tip_details=tip_details,
            status=status,
            order_type=order_type,
            dining_option=dining_option,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.receipts_update_receipt_request_receipt_lines import ReceiptsUpdateReceiptRequestReceiptLines
from 7_shifts_python_sdk.model.receipts_update_receipt_request_tip_details import ReceiptsUpdateReceiptRequestTipDetails