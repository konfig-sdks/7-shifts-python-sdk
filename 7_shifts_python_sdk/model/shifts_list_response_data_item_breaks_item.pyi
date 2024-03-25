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


class ShiftsListResponseDataItemBreaksItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "break_type_id",
            "shift_id",
            "length",
            "name",
            "id",
        }
        
        class properties:
            id = schemas.IntSchema
            shift_id = schemas.IntSchema
            name = schemas.StrSchema
            length = schemas.IntSchema
            break_type_id = schemas.IntSchema
            
            
            class start(
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
                ) -> 'start':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class end(
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
                ) -> 'end':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PAID(cls):
                    return cls("paid")
                
                @schemas.classproperty
                def UNPAID(cls):
                    return cls("unpaid")
            __annotations__ = {
                "id": id,
                "shift_id": shift_id,
                "name": name,
                "length": length,
                "break_type_id": break_type_id,
                "start": start,
                "end": end,
                "type": type,
            }
    
    break_type_id: MetaOapg.properties.break_type_id
    shift_id: MetaOapg.properties.shift_id
    length: MetaOapg.properties.length
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shift_id"]) -> MetaOapg.properties.shift_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["break_type_id"]) -> MetaOapg.properties.break_type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "shift_id", "name", "length", "break_type_id", "start", "end", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shift_id"]) -> MetaOapg.properties.shift_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["break_type_id"]) -> MetaOapg.properties.break_type_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "shift_id", "name", "length", "break_type_id", "start", "end", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        break_type_id: typing.Union[MetaOapg.properties.break_type_id, decimal.Decimal, int, ],
        shift_id: typing.Union[MetaOapg.properties.shift_id, decimal.Decimal, int, ],
        length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        start: typing.Union[MetaOapg.properties.start, None, str, datetime, schemas.Unset] = schemas.unset,
        end: typing.Union[MetaOapg.properties.end, None, str, datetime, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShiftsListResponseDataItemBreaksItem':
        return super().__new__(
            cls,
            *args,
            break_type_id=break_type_id,
            shift_id=shift_id,
            length=length,
            name=name,
            id=id,
            start=start,
            end=end,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
