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


class LogBookCreateCategoryRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class col(
                schemas.IntSchema
            ):
                pass
            
            
            class sort(
                schemas.IntSchema
            ):
                pass
            
            
            class field_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DOLLAR(cls):
                    return cls("dollar")
                
                @schemas.classproperty
                def NUMBER(cls):
                    return cls("number")
                
                @schemas.classproperty
                def PERCENTAGE(cls):
                    return cls("percentage")
                
                @schemas.classproperty
                def TEXTAREA(cls):
                    return cls("textarea")
            notify = schemas.BoolSchema
            required = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "col": col,
                "sort": sort,
                "field_type": field_type,
                "notify": notify,
                "required": required,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["col"]) -> MetaOapg.properties.col: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_type"]) -> MetaOapg.properties.field_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notify"]) -> MetaOapg.properties.notify: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "col", "sort", "field_type", "notify", "required", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["col"]) -> typing.Union[MetaOapg.properties.col, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union[MetaOapg.properties.sort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_type"]) -> typing.Union[MetaOapg.properties.field_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notify"]) -> typing.Union[MetaOapg.properties.notify, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "col", "sort", "field_type", "notify", "required", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        col: typing.Union[MetaOapg.properties.col, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sort: typing.Union[MetaOapg.properties.sort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        field_type: typing.Union[MetaOapg.properties.field_type, str, schemas.Unset] = schemas.unset,
        notify: typing.Union[MetaOapg.properties.notify, bool, schemas.Unset] = schemas.unset,
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogBookCreateCategoryRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            col=col,
            sort=sort,
            field_type=field_type,
            notify=notify,
            required=required,
            _configuration=_configuration,
            **kwargs,
        )
