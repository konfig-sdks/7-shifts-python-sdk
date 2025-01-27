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


class TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Tip pool stakeholders (contributors and receivers)
    """


    class MetaOapg:
        required = {
            "stake_amount",
            "contribution_method",
            "department_id",
            "role_id",
            "stakeholder_type",
            "stakeholder_subtype",
        }
        
        class properties:
            
            
            class stakeholder_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONTRIBUTION(cls):
                    return cls("CONTRIBUTION")
                
                @schemas.classproperty
                def DISTRIBUTION(cls):
                    return cls("DISTRIBUTION")
            
            
            class stakeholder_subtype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ROLE(cls):
                    return cls("ROLE")
                
                @schemas.classproperty
                def DEPARTMENT(cls):
                    return cls("DEPARTMENT")
            
            
            class role_id(
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
                ) -> 'role_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
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
            
            
            class stake_amount(
                schemas.Float32Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'float'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stake_amount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class contribution_method(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contribution_method':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
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
        
            @staticmethod
            def filters() -> typing.Type['TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFilters']:
                return TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFilters
            __annotations__ = {
                "stakeholder_type": stakeholder_type,
                "stakeholder_subtype": stakeholder_subtype,
                "role_id": role_id,
                "department_id": department_id,
                "stake_amount": stake_amount,
                "contribution_method": contribution_method,
                "uuid": uuid,
                "tip_pool_settings_uuid": tip_pool_settings_uuid,
                "filters": filters,
            }
    
    stake_amount: MetaOapg.properties.stake_amount
    contribution_method: MetaOapg.properties.contribution_method
    department_id: MetaOapg.properties.department_id
    role_id: MetaOapg.properties.role_id
    stakeholder_type: MetaOapg.properties.stakeholder_type
    stakeholder_subtype: MetaOapg.properties.stakeholder_subtype
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stakeholder_type"]) -> MetaOapg.properties.stakeholder_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stakeholder_subtype"]) -> MetaOapg.properties.stakeholder_subtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stake_amount"]) -> MetaOapg.properties.stake_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contribution_method"]) -> MetaOapg.properties.contribution_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_pool_settings_uuid"]) -> MetaOapg.properties.tip_pool_settings_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filters"]) -> 'TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFilters': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stakeholder_type", "stakeholder_subtype", "role_id", "department_id", "stake_amount", "contribution_method", "uuid", "tip_pool_settings_uuid", "filters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stakeholder_type"]) -> MetaOapg.properties.stakeholder_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stakeholder_subtype"]) -> MetaOapg.properties.stakeholder_subtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stake_amount"]) -> MetaOapg.properties.stake_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contribution_method"]) -> MetaOapg.properties.contribution_method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_pool_settings_uuid"]) -> typing.Union[MetaOapg.properties.tip_pool_settings_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union['TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFilters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stakeholder_type", "stakeholder_subtype", "role_id", "department_id", "stake_amount", "contribution_method", "uuid", "tip_pool_settings_uuid", "filters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        stake_amount: typing.Union[MetaOapg.properties.stake_amount, None, decimal.Decimal, int, float, ],
        contribution_method: typing.Union[MetaOapg.properties.contribution_method, None, str, ],
        department_id: typing.Union[MetaOapg.properties.department_id, None, decimal.Decimal, int, ],
        role_id: typing.Union[MetaOapg.properties.role_id, None, decimal.Decimal, int, ],
        stakeholder_type: typing.Union[MetaOapg.properties.stakeholder_type, str, ],
        stakeholder_subtype: typing.Union[MetaOapg.properties.stakeholder_subtype, str, ],
        uuid: typing.Union[MetaOapg.properties.uuid, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        tip_pool_settings_uuid: typing.Union[MetaOapg.properties.tip_pool_settings_uuid, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        filters: typing.Union['TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFilters', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItem':
        return super().__new__(
            cls,
            *args,
            stake_amount=stake_amount,
            contribution_method=contribution_method,
            department_id=department_id,
            role_id=role_id,
            stakeholder_type=stakeholder_type,
            stakeholder_subtype=stakeholder_subtype,
            uuid=uuid,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            filters=filters,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.tip_pool_get_settings_response_data_item_tip_pool_stakeholders_item_filters import TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFilters
