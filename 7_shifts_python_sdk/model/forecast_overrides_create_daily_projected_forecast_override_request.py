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


class ForecastOverridesCreateDailyProjectedForecastOverrideRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "report_type",
            "value",
        }
        
        class properties:
            
            
            class date(
                schemas.DateSchema
            ):
            
            
                class MetaOapg:
                    format = 'date'
                    regex=[{
                        'pattern': r'^\d{4}-\d{2}-\d{2}$',
                    }]
            
            
            class value(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class report_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "sales": "SALES",
                    }
                
                @schemas.classproperty
                def SALES(cls):
                    return cls("sales")
            
            
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
            __annotations__ = {
                "date": date,
                "value": value,
                "report_type": report_type,
                "department_id": department_id,
            }
    
    date: MetaOapg.properties.date
    report_type: MetaOapg.properties.report_type
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_type"]) -> MetaOapg.properties.report_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "value", "report_type", "department_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_type"]) -> MetaOapg.properties.report_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "value", "report_type", "department_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, date, ],
        report_type: typing.Union[MetaOapg.properties.report_type, str, ],
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, ],
        department_id: typing.Union[MetaOapg.properties.department_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ForecastOverridesCreateDailyProjectedForecastOverrideRequest':
        return super().__new__(
            cls,
            *args,
            date=date,
            report_type=report_type,
            value=value,
            department_id=department_id,
            _configuration=_configuration,
            **kwargs,
        )
