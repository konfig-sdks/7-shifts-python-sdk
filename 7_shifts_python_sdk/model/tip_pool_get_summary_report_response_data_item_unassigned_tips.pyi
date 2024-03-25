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


class TipPoolGetSummaryReportResponseDataItemUnassignedTips(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "tip_in",
            "hours_worked",
        }
        
        class properties:
            hours_worked = schemas.NumberSchema
            tip_in = schemas.IntSchema
            __annotations__ = {
                "hours_worked": hours_worked,
                "tip_in": tip_in,
            }
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    net_sales = schemas.IntSchema
                    cc_tips = schemas.IntSchema
                    cc_tips_withheld = schemas.IntSchema
                    auto_grat_tips = schemas.IntSchema
                    cash_tips = schemas.IntSchema
                    declared_tips = schemas.IntSchema
                    __annotations__ = {
                        "net_sales": net_sales,
                        "cc_tips": cc_tips,
                        "cc_tips_withheld": cc_tips_withheld,
                        "auto_grat_tips": auto_grat_tips,
                        "cash_tips": cash_tips,
                        "declared_tips": declared_tips,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["net_sales"]) -> MetaOapg.properties.net_sales: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cc_tips"]) -> MetaOapg.properties.cc_tips: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cc_tips_withheld"]) -> MetaOapg.properties.cc_tips_withheld: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["auto_grat_tips"]) -> MetaOapg.properties.auto_grat_tips: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cash_tips"]) -> MetaOapg.properties.cash_tips: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["declared_tips"]) -> MetaOapg.properties.declared_tips: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["net_sales", "cc_tips", "cc_tips_withheld", "auto_grat_tips", "cash_tips", "declared_tips", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["net_sales"]) -> typing.Union[MetaOapg.properties.net_sales, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cc_tips"]) -> typing.Union[MetaOapg.properties.cc_tips, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cc_tips_withheld"]) -> typing.Union[MetaOapg.properties.cc_tips_withheld, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["auto_grat_tips"]) -> typing.Union[MetaOapg.properties.auto_grat_tips, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cash_tips"]) -> typing.Union[MetaOapg.properties.cash_tips, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["declared_tips"]) -> typing.Union[MetaOapg.properties.declared_tips, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["net_sales", "cc_tips", "cc_tips_withheld", "auto_grat_tips", "cash_tips", "declared_tips", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                net_sales: typing.Union[MetaOapg.properties.net_sales, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                cc_tips: typing.Union[MetaOapg.properties.cc_tips, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                cc_tips_withheld: typing.Union[MetaOapg.properties.cc_tips_withheld, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                auto_grat_tips: typing.Union[MetaOapg.properties.auto_grat_tips, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                cash_tips: typing.Union[MetaOapg.properties.cash_tips, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                declared_tips: typing.Union[MetaOapg.properties.declared_tips, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    net_sales=net_sales,
                    cc_tips=cc_tips,
                    cc_tips_withheld=cc_tips_withheld,
                    auto_grat_tips=auto_grat_tips,
                    cash_tips=cash_tips,
                    declared_tips=declared_tips,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
            ]

    
    tip_in: MetaOapg.properties.tip_in
    hours_worked: MetaOapg.properties.hours_worked
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours_worked"]) -> MetaOapg.properties.hours_worked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_in"]) -> MetaOapg.properties.tip_in: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hours_worked", "tip_in", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours_worked"]) -> MetaOapg.properties.hours_worked: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_in"]) -> MetaOapg.properties.tip_in: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hours_worked", "tip_in", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tip_in: typing.Union[MetaOapg.properties.tip_in, decimal.Decimal, int, ],
        hours_worked: typing.Union[MetaOapg.properties.hours_worked, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TipPoolGetSummaryReportResponseDataItemUnassignedTips':
        return super().__new__(
            cls,
            *args,
            tip_in=tip_in,
            hours_worked=hours_worked,
            _configuration=_configuration,
            **kwargs,
        )
