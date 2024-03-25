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


class ForecastOverridesOverrideIntervalRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "start",
            "end",
            "value",
        }
        
        class properties:
            start = schemas.DateTimeSchema
            end = schemas.DateTimeSchema
            
            
            class value(
                schemas.Int64Schema
            ):
                pass
            
            
            class department_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'department_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class report_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SALES(cls):
                    return cls("sales")
            __annotations__ = {
                "start": start,
                "end": end,
                "value": value,
                "department_id": department_id,
                "report_type": report_type,
            }
    
    start: MetaOapg.properties.start
    end: MetaOapg.properties.end
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_type"]) -> MetaOapg.properties.report_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["start", "end", "value", "department_id", "report_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_type"]) -> typing.Union[MetaOapg.properties.report_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start", "end", "value", "department_id", "report_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        start: typing.Union[MetaOapg.properties.start, str, datetime, ],
        end: typing.Union[MetaOapg.properties.end, str, datetime, ],
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, ],
        department_id: typing.Union[MetaOapg.properties.department_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        report_type: typing.Union[MetaOapg.properties.report_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ForecastOverridesOverrideIntervalRequest':
        return super().__new__(
            cls,
            *args,
            start=start,
            end=end,
            value=value,
            department_id=department_id,
            report_type=report_type,
            _configuration=_configuration,
            **kwargs,
        )
