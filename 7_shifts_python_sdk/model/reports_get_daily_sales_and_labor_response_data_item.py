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


class ReportsGetDailySalesAndLaborResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date",
            "projected_labor_cost",
            "sales_per_labor_hour",
            "items_per_labor_hour",
            "actual_labor_cost",
            "labor_percent",
            "actual_sales",
            "projected_items_per_labor_hour",
            "projected_sales",
            "projected_sales_per_labor_hour",
        }
        
        class properties:
            date = schemas.StrSchema
            actual_sales = schemas.Int64Schema
            projected_sales = schemas.Int64Schema
            actual_labor_cost = schemas.Int64Schema
            projected_labor_cost = schemas.Int64Schema
            sales_per_labor_hour = schemas.Float32Schema
            projected_sales_per_labor_hour = schemas.Float32Schema
            items_per_labor_hour = schemas.Float32Schema
            projected_items_per_labor_hour = schemas.Float32Schema
            labor_percent = schemas.Float32Schema
            
            
            class projected_sales_override(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'projected_sales_override':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class id(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            location_id = schemas.Int64Schema
            
            
            class department_id(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
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
            actual_items = schemas.Int64Schema
            projected_items = schemas.Int64Schema
            
            
            class projected_items_override(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'projected_items_override':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            labor_target = schemas.Float32Schema
            actual_labor_minutes = schemas.Int64Schema
            projected_labor_minutes = schemas.Int64Schema
            actual_ot_minutes = schemas.Int64Schema
            __annotations__ = {
                "date": date,
                "actual_sales": actual_sales,
                "projected_sales": projected_sales,
                "actual_labor_cost": actual_labor_cost,
                "projected_labor_cost": projected_labor_cost,
                "sales_per_labor_hour": sales_per_labor_hour,
                "projected_sales_per_labor_hour": projected_sales_per_labor_hour,
                "items_per_labor_hour": items_per_labor_hour,
                "projected_items_per_labor_hour": projected_items_per_labor_hour,
                "labor_percent": labor_percent,
                "projected_sales_override": projected_sales_override,
                "id": id,
                "location_id": location_id,
                "department_id": department_id,
                "actual_items": actual_items,
                "projected_items": projected_items,
                "projected_items_override": projected_items_override,
                "labor_target": labor_target,
                "actual_labor_minutes": actual_labor_minutes,
                "projected_labor_minutes": projected_labor_minutes,
                "actual_ot_minutes": actual_ot_minutes,
            }
    
    date: MetaOapg.properties.date
    projected_labor_cost: MetaOapg.properties.projected_labor_cost
    sales_per_labor_hour: MetaOapg.properties.sales_per_labor_hour
    items_per_labor_hour: MetaOapg.properties.items_per_labor_hour
    actual_labor_cost: MetaOapg.properties.actual_labor_cost
    labor_percent: MetaOapg.properties.labor_percent
    actual_sales: MetaOapg.properties.actual_sales
    projected_items_per_labor_hour: MetaOapg.properties.projected_items_per_labor_hour
    projected_sales: MetaOapg.properties.projected_sales
    projected_sales_per_labor_hour: MetaOapg.properties.projected_sales_per_labor_hour
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actual_sales"]) -> MetaOapg.properties.actual_sales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_sales"]) -> MetaOapg.properties.projected_sales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actual_labor_cost"]) -> MetaOapg.properties.actual_labor_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_labor_cost"]) -> MetaOapg.properties.projected_labor_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sales_per_labor_hour"]) -> MetaOapg.properties.sales_per_labor_hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_sales_per_labor_hour"]) -> MetaOapg.properties.projected_sales_per_labor_hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items_per_labor_hour"]) -> MetaOapg.properties.items_per_labor_hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_items_per_labor_hour"]) -> MetaOapg.properties.projected_items_per_labor_hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labor_percent"]) -> MetaOapg.properties.labor_percent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_sales_override"]) -> MetaOapg.properties.projected_sales_override: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actual_items"]) -> MetaOapg.properties.actual_items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_items"]) -> MetaOapg.properties.projected_items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_items_override"]) -> MetaOapg.properties.projected_items_override: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labor_target"]) -> MetaOapg.properties.labor_target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actual_labor_minutes"]) -> MetaOapg.properties.actual_labor_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projected_labor_minutes"]) -> MetaOapg.properties.projected_labor_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actual_ot_minutes"]) -> MetaOapg.properties.actual_ot_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "actual_sales", "projected_sales", "actual_labor_cost", "projected_labor_cost", "sales_per_labor_hour", "projected_sales_per_labor_hour", "items_per_labor_hour", "projected_items_per_labor_hour", "labor_percent", "projected_sales_override", "id", "location_id", "department_id", "actual_items", "projected_items", "projected_items_override", "labor_target", "actual_labor_minutes", "projected_labor_minutes", "actual_ot_minutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actual_sales"]) -> MetaOapg.properties.actual_sales: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_sales"]) -> MetaOapg.properties.projected_sales: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actual_labor_cost"]) -> MetaOapg.properties.actual_labor_cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_labor_cost"]) -> MetaOapg.properties.projected_labor_cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sales_per_labor_hour"]) -> MetaOapg.properties.sales_per_labor_hour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_sales_per_labor_hour"]) -> MetaOapg.properties.projected_sales_per_labor_hour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items_per_labor_hour"]) -> MetaOapg.properties.items_per_labor_hour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_items_per_labor_hour"]) -> MetaOapg.properties.projected_items_per_labor_hour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labor_percent"]) -> MetaOapg.properties.labor_percent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_sales_override"]) -> typing.Union[MetaOapg.properties.projected_sales_override, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actual_items"]) -> typing.Union[MetaOapg.properties.actual_items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_items"]) -> typing.Union[MetaOapg.properties.projected_items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_items_override"]) -> typing.Union[MetaOapg.properties.projected_items_override, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labor_target"]) -> typing.Union[MetaOapg.properties.labor_target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actual_labor_minutes"]) -> typing.Union[MetaOapg.properties.actual_labor_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projected_labor_minutes"]) -> typing.Union[MetaOapg.properties.projected_labor_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actual_ot_minutes"]) -> typing.Union[MetaOapg.properties.actual_ot_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "actual_sales", "projected_sales", "actual_labor_cost", "projected_labor_cost", "sales_per_labor_hour", "projected_sales_per_labor_hour", "items_per_labor_hour", "projected_items_per_labor_hour", "labor_percent", "projected_sales_override", "id", "location_id", "department_id", "actual_items", "projected_items", "projected_items_override", "labor_target", "actual_labor_minutes", "projected_labor_minutes", "actual_ot_minutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, ],
        projected_labor_cost: typing.Union[MetaOapg.properties.projected_labor_cost, decimal.Decimal, int, ],
        sales_per_labor_hour: typing.Union[MetaOapg.properties.sales_per_labor_hour, decimal.Decimal, int, float, ],
        items_per_labor_hour: typing.Union[MetaOapg.properties.items_per_labor_hour, decimal.Decimal, int, float, ],
        actual_labor_cost: typing.Union[MetaOapg.properties.actual_labor_cost, decimal.Decimal, int, ],
        labor_percent: typing.Union[MetaOapg.properties.labor_percent, decimal.Decimal, int, float, ],
        actual_sales: typing.Union[MetaOapg.properties.actual_sales, decimal.Decimal, int, ],
        projected_items_per_labor_hour: typing.Union[MetaOapg.properties.projected_items_per_labor_hour, decimal.Decimal, int, float, ],
        projected_sales: typing.Union[MetaOapg.properties.projected_sales, decimal.Decimal, int, ],
        projected_sales_per_labor_hour: typing.Union[MetaOapg.properties.projected_sales_per_labor_hour, decimal.Decimal, int, float, ],
        projected_sales_override: typing.Union[MetaOapg.properties.projected_sales_override, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        department_id: typing.Union[MetaOapg.properties.department_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        actual_items: typing.Union[MetaOapg.properties.actual_items, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        projected_items: typing.Union[MetaOapg.properties.projected_items, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        projected_items_override: typing.Union[MetaOapg.properties.projected_items_override, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        labor_target: typing.Union[MetaOapg.properties.labor_target, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        actual_labor_minutes: typing.Union[MetaOapg.properties.actual_labor_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        projected_labor_minutes: typing.Union[MetaOapg.properties.projected_labor_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        actual_ot_minutes: typing.Union[MetaOapg.properties.actual_ot_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetDailySalesAndLaborResponseDataItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            projected_labor_cost=projected_labor_cost,
            sales_per_labor_hour=sales_per_labor_hour,
            items_per_labor_hour=items_per_labor_hour,
            actual_labor_cost=actual_labor_cost,
            labor_percent=labor_percent,
            actual_sales=actual_sales,
            projected_items_per_labor_hour=projected_items_per_labor_hour,
            projected_sales=projected_sales,
            projected_sales_per_labor_hour=projected_sales_per_labor_hour,
            projected_sales_override=projected_sales_override,
            id=id,
            location_id=location_id,
            department_id=department_id,
            actual_items=actual_items,
            projected_items=projected_items,
            projected_items_override=projected_items_override,
            labor_target=labor_target,
            actual_labor_minutes=actual_labor_minutes,
            projected_labor_minutes=projected_labor_minutes,
            actual_ot_minutes=actual_ot_minutes,
            _configuration=_configuration,
            **kwargs,
        )
