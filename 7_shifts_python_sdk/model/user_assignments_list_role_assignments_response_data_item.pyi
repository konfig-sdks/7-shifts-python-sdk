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


class UserAssignmentsListRoleAssignmentsResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "is_primary",
            "role_id",
            "name",
            "skill_level",
            "sort",
        }
        
        class properties:
            role_id = schemas.IntSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            is_primary = schemas.BoolSchema
            skill_level = schemas.IntSchema
            sort = schemas.IntSchema
            location_id = schemas.IntSchema
            department_id = schemas.IntSchema
            __annotations__ = {
                "role_id": role_id,
                "name": name,
                "is_primary": is_primary,
                "skill_level": skill_level,
                "sort": sort,
                "location_id": location_id,
                "department_id": department_id,
            }
    
    is_primary: MetaOapg.properties.is_primary
    role_id: MetaOapg.properties.role_id
    name: MetaOapg.properties.name
    skill_level: MetaOapg.properties.skill_level
    sort: MetaOapg.properties.sort
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_primary"]) -> MetaOapg.properties.is_primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skill_level"]) -> MetaOapg.properties.skill_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["role_id", "name", "is_primary", "skill_level", "sort", "location_id", "department_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_primary"]) -> MetaOapg.properties.is_primary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skill_level"]) -> MetaOapg.properties.skill_level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["role_id", "name", "is_primary", "skill_level", "sort", "location_id", "department_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_primary: typing.Union[MetaOapg.properties.is_primary, bool, ],
        role_id: typing.Union[MetaOapg.properties.role_id, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        skill_level: typing.Union[MetaOapg.properties.skill_level, decimal.Decimal, int, ],
        sort: typing.Union[MetaOapg.properties.sort, decimal.Decimal, int, ],
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        department_id: typing.Union[MetaOapg.properties.department_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserAssignmentsListRoleAssignmentsResponseDataItem':
        return super().__new__(
            cls,
            *args,
            is_primary=is_primary,
            role_id=role_id,
            name=name,
            skill_level=skill_level,
            sort=sort,
            location_id=location_id,
            department_id=department_id,
            _configuration=_configuration,
            **kwargs,
        )
