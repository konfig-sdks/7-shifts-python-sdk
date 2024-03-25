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


class ReceiptsGetReceiptResponseDataReceiptLinesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "external_category_ids",
            "quantity",
            "price",
            "location_id",
            "external_item_id",
        }
        
        class properties:
            
            
            class location_id(
                schemas.IntSchema
            ):
                pass
            external_item_id = schemas.StrSchema
        
            @staticmethod
            def external_category_ids() -> typing.Type['ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds']:
                return ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds
            quantity = schemas.IntSchema
            price = schemas.IntSchema
            
            
            class id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class gross_item_price(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gross_item_price':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class net_item_price(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'net_item_price':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class item_discount(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'item_discount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class created_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'created_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "location_id": location_id,
                "external_item_id": external_item_id,
                "external_category_ids": external_category_ids,
                "quantity": quantity,
                "price": price,
                "id": id,
                "gross_item_price": gross_item_price,
                "net_item_price": net_item_price,
                "item_discount": item_discount,
                "created_date": created_date,
            }
    
    external_category_ids: 'ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds'
    quantity: MetaOapg.properties.quantity
    price: MetaOapg.properties.price
    location_id: MetaOapg.properties.location_id
    external_item_id: MetaOapg.properties.external_item_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_item_id"]) -> MetaOapg.properties.external_item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_category_ids"]) -> 'ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_item_price"]) -> MetaOapg.properties.gross_item_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_item_price"]) -> MetaOapg.properties.net_item_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_discount"]) -> MetaOapg.properties.item_discount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_date"]) -> MetaOapg.properties.created_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["location_id", "external_item_id", "external_category_ids", "quantity", "price", "id", "gross_item_price", "net_item_price", "item_discount", "created_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_item_id"]) -> MetaOapg.properties.external_item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_category_ids"]) -> 'ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_item_price"]) -> typing.Union[MetaOapg.properties.gross_item_price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_item_price"]) -> typing.Union[MetaOapg.properties.net_item_price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_discount"]) -> typing.Union[MetaOapg.properties.item_discount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_date"]) -> typing.Union[MetaOapg.properties.created_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["location_id", "external_item_id", "external_category_ids", "quantity", "price", "id", "gross_item_price", "net_item_price", "item_discount", "created_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        external_category_ids: 'ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds',
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, ],
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
        external_item_id: typing.Union[MetaOapg.properties.external_item_id, str, ],
        id: typing.Union[MetaOapg.properties.id, None, str, schemas.Unset] = schemas.unset,
        gross_item_price: typing.Union[MetaOapg.properties.gross_item_price, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        net_item_price: typing.Union[MetaOapg.properties.net_item_price, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        item_discount: typing.Union[MetaOapg.properties.item_discount, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created_date: typing.Union[MetaOapg.properties.created_date, None, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReceiptsGetReceiptResponseDataReceiptLinesItem':
        return super().__new__(
            cls,
            *args,
            external_category_ids=external_category_ids,
            quantity=quantity,
            price=price,
            location_id=location_id,
            external_item_id=external_item_id,
            id=id,
            gross_item_price=gross_item_price,
            net_item_price=net_item_price,
            item_discount=item_discount,
            created_date=created_date,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.receipts_get_receipt_response_data_receipt_lines_item_external_category_ids import ReceiptsGetReceiptResponseDataReceiptLinesItemExternalCategoryIds
