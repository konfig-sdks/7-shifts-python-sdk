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


class CompaniesGetByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "country",
            "days_to_expire",
            "expires",
            "start_week_on",
            "created",
            "photo",
            "converted",
            "pos",
            "name",
            "modified",
            "id",
            "plan_id",
            "status",
        }
        
        class properties:
            id = schemas.NumberSchema
            name = schemas.StrSchema
            country = schemas.StrSchema
            
            
            class photo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'photo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            plan_id = schemas.StrSchema
            created = schemas.DateTimeSchema
            
            
            class modified(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'modified':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class expires(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expires':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class days_to_expire(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'days_to_expire':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class converted(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'converted':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class pos(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pos':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "active": "ACTIVE",
                        "trial": "TRIAL",
                        "cancelled": "CANCELLED",
                        "delinquent": "DELINQUENT",
                        "expired": "EXPIRED",
                        "unknown": "UNKNOWN",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def TRIAL(cls):
                    return cls("trial")
                
                @schemas.classproperty
                def CANCELLED(cls):
                    return cls("cancelled")
                
                @schemas.classproperty
                def DELINQUENT(cls):
                    return cls("delinquent")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("expired")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("unknown")
            
            
            class start_week_on(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'start_week_on':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def meta() -> typing.Type['CompaniesGetByIdResponseMeta']:
                return CompaniesGetByIdResponseMeta
            __annotations__ = {
                "id": id,
                "name": name,
                "country": country,
                "photo": photo,
                "plan_id": plan_id,
                "created": created,
                "modified": modified,
                "expires": expires,
                "days_to_expire": days_to_expire,
                "converted": converted,
                "pos": pos,
                "status": status,
                "start_week_on": start_week_on,
                "meta": meta,
            }
    
    country: MetaOapg.properties.country
    days_to_expire: MetaOapg.properties.days_to_expire
    expires: MetaOapg.properties.expires
    start_week_on: MetaOapg.properties.start_week_on
    created: MetaOapg.properties.created
    photo: MetaOapg.properties.photo
    converted: MetaOapg.properties.converted
    pos: MetaOapg.properties.pos
    name: MetaOapg.properties.name
    modified: MetaOapg.properties.modified
    id: MetaOapg.properties.id
    plan_id: MetaOapg.properties.plan_id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photo"]) -> MetaOapg.properties.photo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan_id"]) -> MetaOapg.properties.plan_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires"]) -> MetaOapg.properties.expires: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days_to_expire"]) -> MetaOapg.properties.days_to_expire: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["converted"]) -> MetaOapg.properties.converted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pos"]) -> MetaOapg.properties.pos: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_week_on"]) -> MetaOapg.properties.start_week_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'CompaniesGetByIdResponseMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "country", "photo", "plan_id", "created", "modified", "expires", "days_to_expire", "converted", "pos", "status", "start_week_on", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photo"]) -> MetaOapg.properties.photo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan_id"]) -> MetaOapg.properties.plan_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires"]) -> MetaOapg.properties.expires: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days_to_expire"]) -> MetaOapg.properties.days_to_expire: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["converted"]) -> MetaOapg.properties.converted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pos"]) -> MetaOapg.properties.pos: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_week_on"]) -> MetaOapg.properties.start_week_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['CompaniesGetByIdResponseMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "country", "photo", "plan_id", "created", "modified", "expires", "days_to_expire", "converted", "pos", "status", "start_week_on", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        days_to_expire: typing.Union[MetaOapg.properties.days_to_expire, None, decimal.Decimal, int, float, ],
        expires: typing.Union[MetaOapg.properties.expires, None, str, datetime, ],
        start_week_on: typing.Union[MetaOapg.properties.start_week_on, None, decimal.Decimal, int, float, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        photo: typing.Union[MetaOapg.properties.photo, None, str, ],
        converted: typing.Union[MetaOapg.properties.converted, None, str, datetime, ],
        pos: typing.Union[MetaOapg.properties.pos, None, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        modified: typing.Union[MetaOapg.properties.modified, None, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        plan_id: typing.Union[MetaOapg.properties.plan_id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        meta: typing.Union['CompaniesGetByIdResponseMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesGetByIdResponse':
        return super().__new__(
            cls,
            *args,
            country=country,
            days_to_expire=days_to_expire,
            expires=expires,
            start_week_on=start_week_on,
            created=created,
            photo=photo,
            converted=converted,
            pos=pos,
            name=name,
            modified=modified,
            id=id,
            plan_id=plan_id,
            status=status,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.companies_get_by_id_response_meta import CompaniesGetByIdResponseMeta