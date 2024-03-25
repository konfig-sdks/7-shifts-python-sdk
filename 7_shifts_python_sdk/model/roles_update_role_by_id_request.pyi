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


class RolesUpdateRoleByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            department_id = schemas.IntSchema
            
            
            class sort(
                schemas.IntSchema
            ):
                pass
            
            
            class color(
                schemas.StrSchema
            ):
                pass
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class job_code(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def stations() -> typing.Type['RolesUpdateRoleByIdRequestStations']:
                return RolesUpdateRoleByIdRequestStations
            __annotations__ = {
                "department_id": department_id,
                "sort": sort,
                "color": color,
                "name": name,
                "job_code": job_code,
                "stations": stations,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_code"]) -> MetaOapg.properties.job_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stations"]) -> 'RolesUpdateRoleByIdRequestStations': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["department_id", "sort", "color", "name", "job_code", "stations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union[MetaOapg.properties.sort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_code"]) -> typing.Union[MetaOapg.properties.job_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stations"]) -> typing.Union['RolesUpdateRoleByIdRequestStations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["department_id", "sort", "color", "name", "job_code", "stations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        department_id: typing.Union[MetaOapg.properties.department_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sort: typing.Union[MetaOapg.properties.sort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        job_code: typing.Union[MetaOapg.properties.job_code, str, schemas.Unset] = schemas.unset,
        stations: typing.Union['RolesUpdateRoleByIdRequestStations', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RolesUpdateRoleByIdRequest':
        return super().__new__(
            cls,
            *args,
            department_id=department_id,
            sort=sort,
            color=color,
            name=name,
            job_code=job_code,
            stations=stations,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.roles_update_role_by_id_request_stations import RolesUpdateRoleByIdRequestStations