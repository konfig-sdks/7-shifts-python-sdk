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


class UserAssignmentsListDepartmentAssignmentsResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "department_id",
            "name",
            "location_id",
        }
        
        class properties:
            department_id = schemas.IntSchema
            location_id = schemas.IntSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            appear_on_schedule = schemas.BoolSchema
            __annotations__ = {
                "department_id": department_id,
                "location_id": location_id,
                "name": name,
                "appear_on_schedule": appear_on_schedule,
            }
    
    department_id: MetaOapg.properties.department_id
    name: MetaOapg.properties.name
    location_id: MetaOapg.properties.location_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appear_on_schedule"]) -> MetaOapg.properties.appear_on_schedule: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["department_id", "location_id", "name", "appear_on_schedule", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appear_on_schedule"]) -> typing.Union[MetaOapg.properties.appear_on_schedule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["department_id", "location_id", "name", "appear_on_schedule", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        department_id: typing.Union[MetaOapg.properties.department_id, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
        appear_on_schedule: typing.Union[MetaOapg.properties.appear_on_schedule, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserAssignmentsListDepartmentAssignmentsResponseDataItem':
        return super().__new__(
            cls,
            *args,
            department_id=department_id,
            name=name,
            location_id=location_id,
            appear_on_schedule=appear_on_schedule,
            _configuration=_configuration,
            **kwargs,
        )
