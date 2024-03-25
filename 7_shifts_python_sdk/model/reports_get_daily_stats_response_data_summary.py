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


class ReportsGetDailyStatsResponseDataSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            current_actual_sales = schemas.IntSchema
            current_projected_sales = schemas.IntSchema
            past_actual_sales = schemas.IntSchema
            past_projected_sales = schemas.IntSchema
            current_actual_labor = schemas.IntSchema
            current_projected_labor = schemas.IntSchema
            past_actual_labor = schemas.IntSchema
            current_labor_ratio = schemas.NumberSchema
            current_labor_target = schemas.NumberSchema
            past_labor_ratio = schemas.NumberSchema
            current_spmh = schemas.NumberSchema
            past_spmh = schemas.NumberSchema
            __annotations__ = {
                "current_actual_sales": current_actual_sales,
                "current_projected_sales": current_projected_sales,
                "past_actual_sales": past_actual_sales,
                "past_projected_sales": past_projected_sales,
                "current_actual_labor": current_actual_labor,
                "current_projected_labor": current_projected_labor,
                "past_actual_labor": past_actual_labor,
                "current_labor_ratio": current_labor_ratio,
                "current_labor_target": current_labor_target,
                "past_labor_ratio": past_labor_ratio,
                "current_spmh": current_spmh,
                "past_spmh": past_spmh,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_actual_sales"]) -> MetaOapg.properties.current_actual_sales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_projected_sales"]) -> MetaOapg.properties.current_projected_sales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["past_actual_sales"]) -> MetaOapg.properties.past_actual_sales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["past_projected_sales"]) -> MetaOapg.properties.past_projected_sales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_actual_labor"]) -> MetaOapg.properties.current_actual_labor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_projected_labor"]) -> MetaOapg.properties.current_projected_labor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["past_actual_labor"]) -> MetaOapg.properties.past_actual_labor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_labor_ratio"]) -> MetaOapg.properties.current_labor_ratio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_labor_target"]) -> MetaOapg.properties.current_labor_target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["past_labor_ratio"]) -> MetaOapg.properties.past_labor_ratio: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_spmh"]) -> MetaOapg.properties.current_spmh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["past_spmh"]) -> MetaOapg.properties.past_spmh: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current_actual_sales", "current_projected_sales", "past_actual_sales", "past_projected_sales", "current_actual_labor", "current_projected_labor", "past_actual_labor", "current_labor_ratio", "current_labor_target", "past_labor_ratio", "current_spmh", "past_spmh", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_actual_sales"]) -> typing.Union[MetaOapg.properties.current_actual_sales, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_projected_sales"]) -> typing.Union[MetaOapg.properties.current_projected_sales, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["past_actual_sales"]) -> typing.Union[MetaOapg.properties.past_actual_sales, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["past_projected_sales"]) -> typing.Union[MetaOapg.properties.past_projected_sales, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_actual_labor"]) -> typing.Union[MetaOapg.properties.current_actual_labor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_projected_labor"]) -> typing.Union[MetaOapg.properties.current_projected_labor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["past_actual_labor"]) -> typing.Union[MetaOapg.properties.past_actual_labor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_labor_ratio"]) -> typing.Union[MetaOapg.properties.current_labor_ratio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_labor_target"]) -> typing.Union[MetaOapg.properties.current_labor_target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["past_labor_ratio"]) -> typing.Union[MetaOapg.properties.past_labor_ratio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_spmh"]) -> typing.Union[MetaOapg.properties.current_spmh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["past_spmh"]) -> typing.Union[MetaOapg.properties.past_spmh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current_actual_sales", "current_projected_sales", "past_actual_sales", "past_projected_sales", "current_actual_labor", "current_projected_labor", "past_actual_labor", "current_labor_ratio", "current_labor_target", "past_labor_ratio", "current_spmh", "past_spmh", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        current_actual_sales: typing.Union[MetaOapg.properties.current_actual_sales, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        current_projected_sales: typing.Union[MetaOapg.properties.current_projected_sales, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        past_actual_sales: typing.Union[MetaOapg.properties.past_actual_sales, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        past_projected_sales: typing.Union[MetaOapg.properties.past_projected_sales, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        current_actual_labor: typing.Union[MetaOapg.properties.current_actual_labor, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        current_projected_labor: typing.Union[MetaOapg.properties.current_projected_labor, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        past_actual_labor: typing.Union[MetaOapg.properties.past_actual_labor, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        current_labor_ratio: typing.Union[MetaOapg.properties.current_labor_ratio, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        current_labor_target: typing.Union[MetaOapg.properties.current_labor_target, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        past_labor_ratio: typing.Union[MetaOapg.properties.past_labor_ratio, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        current_spmh: typing.Union[MetaOapg.properties.current_spmh, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        past_spmh: typing.Union[MetaOapg.properties.past_spmh, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetDailyStatsResponseDataSummary':
        return super().__new__(
            cls,
            *args,
            current_actual_sales=current_actual_sales,
            current_projected_sales=current_projected_sales,
            past_actual_sales=past_actual_sales,
            past_projected_sales=past_projected_sales,
            current_actual_labor=current_actual_labor,
            current_projected_labor=current_projected_labor,
            past_actual_labor=past_actual_labor,
            current_labor_ratio=current_labor_ratio,
            current_labor_target=current_labor_target,
            past_labor_ratio=past_labor_ratio,
            current_spmh=current_spmh,
            past_spmh=past_spmh,
            _configuration=_configuration,
            **kwargs,
        )
