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


class TimePunchesCreateRequestBreaksItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "in",
            "paid",
        }
        
        class properties:
            paid = schemas.BoolSchema
            _in = schemas.DateTimeSchema
            out = schemas.DateTimeSchema
            
            
            class custom_break_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_break_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "paid": paid,
                "in": _in,
                "out": out,
                "custom_break_id": custom_break_id,
            }
    
    paid: MetaOapg.properties.paid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paid"]) -> MetaOapg.properties.paid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in"]) -> MetaOapg.properties._in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out"]) -> MetaOapg.properties.out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_break_id"]) -> MetaOapg.properties.custom_break_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paid", "in", "out", "custom_break_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paid"]) -> MetaOapg.properties.paid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in"]) -> MetaOapg.properties._in: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out"]) -> typing.Union[MetaOapg.properties.out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_break_id"]) -> typing.Union[MetaOapg.properties.custom_break_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paid", "in", "out", "custom_break_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        paid: typing.Union[MetaOapg.properties.paid, bool, ],
        out: typing.Union[MetaOapg.properties.out, str, datetime, schemas.Unset] = schemas.unset,
        custom_break_id: typing.Union[MetaOapg.properties.custom_break_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimePunchesCreateRequestBreaksItem':
        return super().__new__(
            cls,
            *args,
            paid=paid,
            out=out,
            custom_break_id=custom_break_id,
            _configuration=_configuration,
            **kwargs,
        )
