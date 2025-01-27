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


class EngageOverviewByLocationIdResponseDataEmployeeStatsMostLate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "primary_role",
            "last_name",
            "id",
            "photo_url",
            "first_name",
        }
        
        class properties:
            id = schemas.IntSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            photo_url = schemas.StrSchema
            
            
            class primary_role(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'primary_role':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "photo_url": photo_url,
                "primary_role": primary_role,
            }
    
    primary_role: MetaOapg.properties.primary_role
    last_name: MetaOapg.properties.last_name
    id: MetaOapg.properties.id
    photo_url: MetaOapg.properties.photo_url
    first_name: MetaOapg.properties.first_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photo_url"]) -> MetaOapg.properties.photo_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_role"]) -> MetaOapg.properties.primary_role: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "first_name", "last_name", "photo_url", "primary_role", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photo_url"]) -> MetaOapg.properties.photo_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_role"]) -> MetaOapg.properties.primary_role: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "first_name", "last_name", "photo_url", "primary_role", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        primary_role: typing.Union[MetaOapg.properties.primary_role, None, str, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        photo_url: typing.Union[MetaOapg.properties.photo_url, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EngageOverviewByLocationIdResponseDataEmployeeStatsMostLate':
        return super().__new__(
            cls,
            *args,
            primary_role=primary_role,
            last_name=last_name,
            id=id,
            photo_url=photo_url,
            first_name=first_name,
            _configuration=_configuration,
            **kwargs,
        )
