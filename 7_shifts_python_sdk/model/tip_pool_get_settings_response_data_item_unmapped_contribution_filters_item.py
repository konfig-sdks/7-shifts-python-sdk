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


class TipPoolGetSettingsResponseDataItemUnmappedContributionFiltersItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "filter_name",
            "filter_value",
            "filter_type",
        }
        
        class properties:
            
            
            class filter_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DINING_OPTION": "DINING_OPTION",
                        "REVENUE_CENTER": "REVENUE_CENTER",
                        "SALES_CATEGORY": "SALES_CATEGORY",
                    }
                
                @schemas.classproperty
                def DINING_OPTION(cls):
                    return cls("DINING_OPTION")
                
                @schemas.classproperty
                def REVENUE_CENTER(cls):
                    return cls("REVENUE_CENTER")
                
                @schemas.classproperty
                def SALES_CATEGORY(cls):
                    return cls("SALES_CATEGORY")
            
            
            class filter_value(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'filter_value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            filter_name = schemas.StrSchema
            
            
            class uuid(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'uuid':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class tip_pool_settings_uuid(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tip_pool_settings_uuid':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "filter_type": filter_type,
                "filter_value": filter_value,
                "filter_name": filter_name,
                "uuid": uuid,
                "tip_pool_settings_uuid": tip_pool_settings_uuid,
            }
    
    filter_name: MetaOapg.properties.filter_name
    filter_value: MetaOapg.properties.filter_value
    filter_type: MetaOapg.properties.filter_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter_type"]) -> MetaOapg.properties.filter_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter_value"]) -> MetaOapg.properties.filter_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter_name"]) -> MetaOapg.properties.filter_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_pool_settings_uuid"]) -> MetaOapg.properties.tip_pool_settings_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["filter_type", "filter_value", "filter_name", "uuid", "tip_pool_settings_uuid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter_type"]) -> MetaOapg.properties.filter_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter_value"]) -> MetaOapg.properties.filter_value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter_name"]) -> MetaOapg.properties.filter_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_pool_settings_uuid"]) -> typing.Union[MetaOapg.properties.tip_pool_settings_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["filter_type", "filter_value", "filter_name", "uuid", "tip_pool_settings_uuid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        filter_name: typing.Union[MetaOapg.properties.filter_name, str, ],
        filter_value: typing.Union[MetaOapg.properties.filter_value, None, str, ],
        filter_type: typing.Union[MetaOapg.properties.filter_type, str, ],
        uuid: typing.Union[MetaOapg.properties.uuid, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        tip_pool_settings_uuid: typing.Union[MetaOapg.properties.tip_pool_settings_uuid, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TipPoolGetSettingsResponseDataItemUnmappedContributionFiltersItem':
        return super().__new__(
            cls,
            *args,
            filter_name=filter_name,
            filter_value=filter_value,
            filter_type=filter_type,
            uuid=uuid,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            _configuration=_configuration,
            **kwargs,
        )