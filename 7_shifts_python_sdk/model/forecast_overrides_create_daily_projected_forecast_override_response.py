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


class ForecastOverridesCreateDailyProjectedForecastOverrideResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "data",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['ForecastOverridesCreateDailyProjectedForecastOverrideResponseData']:
                return ForecastOverridesCreateDailyProjectedForecastOverrideResponseData
            
            
            class object(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "forecast_override": "FORECAST_OVERRIDE",
                    }
                
                @schemas.classproperty
                def FORECAST_OVERRIDE(cls):
                    return cls("forecast_override")
            __annotations__ = {
                "data": data,
                "object": object,
            }
    
    data: 'ForecastOverridesCreateDailyProjectedForecastOverrideResponseData'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ForecastOverridesCreateDailyProjectedForecastOverrideResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ForecastOverridesCreateDailyProjectedForecastOverrideResponseData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: 'ForecastOverridesCreateDailyProjectedForecastOverrideResponseData',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ForecastOverridesCreateDailyProjectedForecastOverrideResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.forecast_overrides_create_daily_projected_forecast_override_response_data import ForecastOverridesCreateDailyProjectedForecastOverrideResponseData
