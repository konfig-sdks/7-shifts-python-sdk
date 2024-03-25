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


class TimePunchesListResponseDataItemBreaksItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "in",
            "user_id",
            "custom_break_id",
            "paid",
            "id",
            "out",
        }
        
        class properties:
            id = schemas.Int32Schema
            user_id = schemas.IntSchema
            custom_break_id = schemas.IntSchema
            paid = schemas.BoolSchema
            _in = schemas.DateTimeSchema
            
            
            class out(
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
                ) -> 'out':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "user_id": user_id,
                "custom_break_id": custom_break_id,
                "paid": paid,
                "in": _in,
                "out": out,
            }
    
    user_id: MetaOapg.properties.user_id
    custom_break_id: MetaOapg.properties.custom_break_id
    paid: MetaOapg.properties.paid
    id: MetaOapg.properties.id
    out: MetaOapg.properties.out
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_break_id"]) -> MetaOapg.properties.custom_break_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paid"]) -> MetaOapg.properties.paid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in"]) -> MetaOapg.properties._in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out"]) -> MetaOapg.properties.out: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "custom_break_id", "paid", "in", "out", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_break_id"]) -> MetaOapg.properties.custom_break_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paid"]) -> MetaOapg.properties.paid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in"]) -> MetaOapg.properties._in: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out"]) -> MetaOapg.properties.out: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "custom_break_id", "paid", "in", "out", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, ],
        custom_break_id: typing.Union[MetaOapg.properties.custom_break_id, decimal.Decimal, int, ],
        paid: typing.Union[MetaOapg.properties.paid, bool, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        out: typing.Union[MetaOapg.properties.out, None, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimePunchesListResponseDataItemBreaksItem':
        return super().__new__(
            cls,
            *args,
            user_id=user_id,
            custom_break_id=custom_break_id,
            paid=paid,
            id=id,
            out=out,
            _configuration=_configuration,
            **kwargs,
        )
