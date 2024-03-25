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


class TipPoolGetSettingsResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "tip_pool_contributions",
            "company_id",
            "sales_tip_percentage",
            "contribution_type",
            "name",
            "tip_pool_stakeholders",
            "distribution_type",
            "enabled",
            "location_id",
        }
        
        class properties:
            company_id = schemas.Int64Schema
            location_id = schemas.Int64Schema
            
            
            class contribution_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def POS_PERCENT_TIPS_AND_SALES(cls):
                    return cls("POS_PERCENT_TIPS_AND_SALES")
                
                @schemas.classproperty
                def MANUAL_ENTRY(cls):
                    return cls("MANUAL_ENTRY")
            
            
            class distribution_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def HOURS_WORKED(cls):
                    return cls("HOURS_WORKED")
                
                @schemas.classproperty
                def ROLE_PERCENT_HOURS_WORKED(cls):
                    return cls("ROLE_PERCENT_HOURS_WORKED")
                
                @schemas.classproperty
                def POINTS(cls):
                    return cls("POINTS")
            
            
            class sales_tip_percentage(
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
                ) -> 'sales_tip_percentage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            name = schemas.StrSchema
            enabled = schemas.BoolSchema
        
            @staticmethod
            def tip_pool_stakeholders() -> typing.Type['TipPoolGetSettingsResponseDataItemTipPoolStakeholders']:
                return TipPoolGetSettingsResponseDataItemTipPoolStakeholders
        
            @staticmethod
            def tip_pool_contributions() -> typing.Type['TipPoolGetSettingsResponseDataItemTipPoolContributions']:
                return TipPoolGetSettingsResponseDataItemTipPoolContributions
            
            
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
        
            @staticmethod
            def day_part_uuids() -> typing.Type['TipPoolGetSettingsResponseDataItemDayPartUuids']:
                return TipPoolGetSettingsResponseDataItemDayPartUuids
            
            
            class unmapped_contribution_method(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'unmapped_contribution_method':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def unmapped_contribution_filters() -> typing.Type['TipPoolGetSettingsResponseDataItemUnmappedContributionFilters']:
                return TipPoolGetSettingsResponseDataItemUnmappedContributionFilters
        
            @staticmethod
            def tip_pool_cadence_settings() -> typing.Type['TipPoolGetSettingsResponseDataItemTipPoolCadenceSettings']:
                return TipPoolGetSettingsResponseDataItemTipPoolCadenceSettings
            created = schemas.DateTimeSchema
            modified = schemas.DateTimeSchema
            __annotations__ = {
                "company_id": company_id,
                "location_id": location_id,
                "contribution_type": contribution_type,
                "distribution_type": distribution_type,
                "sales_tip_percentage": sales_tip_percentage,
                "name": name,
                "enabled": enabled,
                "tip_pool_stakeholders": tip_pool_stakeholders,
                "tip_pool_contributions": tip_pool_contributions,
                "uuid": uuid,
                "day_part_uuids": day_part_uuids,
                "unmapped_contribution_method": unmapped_contribution_method,
                "unmapped_contribution_filters": unmapped_contribution_filters,
                "tip_pool_cadence_settings": tip_pool_cadence_settings,
                "created": created,
                "modified": modified,
            }
    
    tip_pool_contributions: 'TipPoolGetSettingsResponseDataItemTipPoolContributions'
    company_id: MetaOapg.properties.company_id
    sales_tip_percentage: MetaOapg.properties.sales_tip_percentage
    contribution_type: MetaOapg.properties.contribution_type
    name: MetaOapg.properties.name
    tip_pool_stakeholders: 'TipPoolGetSettingsResponseDataItemTipPoolStakeholders'
    distribution_type: MetaOapg.properties.distribution_type
    enabled: MetaOapg.properties.enabled
    location_id: MetaOapg.properties.location_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contribution_type"]) -> MetaOapg.properties.contribution_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["distribution_type"]) -> MetaOapg.properties.distribution_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sales_tip_percentage"]) -> MetaOapg.properties.sales_tip_percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_pool_stakeholders"]) -> 'TipPoolGetSettingsResponseDataItemTipPoolStakeholders': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_pool_contributions"]) -> 'TipPoolGetSettingsResponseDataItemTipPoolContributions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["day_part_uuids"]) -> 'TipPoolGetSettingsResponseDataItemDayPartUuids': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unmapped_contribution_method"]) -> MetaOapg.properties.unmapped_contribution_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unmapped_contribution_filters"]) -> 'TipPoolGetSettingsResponseDataItemUnmappedContributionFilters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_pool_cadence_settings"]) -> 'TipPoolGetSettingsResponseDataItemTipPoolCadenceSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_id", "location_id", "contribution_type", "distribution_type", "sales_tip_percentage", "name", "enabled", "tip_pool_stakeholders", "tip_pool_contributions", "uuid", "day_part_uuids", "unmapped_contribution_method", "unmapped_contribution_filters", "tip_pool_cadence_settings", "created", "modified", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contribution_type"]) -> MetaOapg.properties.contribution_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["distribution_type"]) -> MetaOapg.properties.distribution_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sales_tip_percentage"]) -> MetaOapg.properties.sales_tip_percentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_pool_stakeholders"]) -> 'TipPoolGetSettingsResponseDataItemTipPoolStakeholders': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_pool_contributions"]) -> 'TipPoolGetSettingsResponseDataItemTipPoolContributions': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["day_part_uuids"]) -> typing.Union['TipPoolGetSettingsResponseDataItemDayPartUuids', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unmapped_contribution_method"]) -> typing.Union[MetaOapg.properties.unmapped_contribution_method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unmapped_contribution_filters"]) -> typing.Union['TipPoolGetSettingsResponseDataItemUnmappedContributionFilters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_pool_cadence_settings"]) -> typing.Union['TipPoolGetSettingsResponseDataItemTipPoolCadenceSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified"]) -> typing.Union[MetaOapg.properties.modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_id", "location_id", "contribution_type", "distribution_type", "sales_tip_percentage", "name", "enabled", "tip_pool_stakeholders", "tip_pool_contributions", "uuid", "day_part_uuids", "unmapped_contribution_method", "unmapped_contribution_filters", "tip_pool_cadence_settings", "created", "modified", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tip_pool_contributions: 'TipPoolGetSettingsResponseDataItemTipPoolContributions',
        company_id: typing.Union[MetaOapg.properties.company_id, decimal.Decimal, int, ],
        sales_tip_percentage: typing.Union[MetaOapg.properties.sales_tip_percentage, None, decimal.Decimal, int, float, ],
        contribution_type: typing.Union[MetaOapg.properties.contribution_type, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        tip_pool_stakeholders: 'TipPoolGetSettingsResponseDataItemTipPoolStakeholders',
        distribution_type: typing.Union[MetaOapg.properties.distribution_type, str, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
        uuid: typing.Union[MetaOapg.properties.uuid, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        day_part_uuids: typing.Union['TipPoolGetSettingsResponseDataItemDayPartUuids', schemas.Unset] = schemas.unset,
        unmapped_contribution_method: typing.Union[MetaOapg.properties.unmapped_contribution_method, None, str, schemas.Unset] = schemas.unset,
        unmapped_contribution_filters: typing.Union['TipPoolGetSettingsResponseDataItemUnmappedContributionFilters', schemas.Unset] = schemas.unset,
        tip_pool_cadence_settings: typing.Union['TipPoolGetSettingsResponseDataItemTipPoolCadenceSettings', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        modified: typing.Union[MetaOapg.properties.modified, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TipPoolGetSettingsResponseDataItem':
        return super().__new__(
            cls,
            *args,
            tip_pool_contributions=tip_pool_contributions,
            company_id=company_id,
            sales_tip_percentage=sales_tip_percentage,
            contribution_type=contribution_type,
            name=name,
            tip_pool_stakeholders=tip_pool_stakeholders,
            distribution_type=distribution_type,
            enabled=enabled,
            location_id=location_id,
            uuid=uuid,
            day_part_uuids=day_part_uuids,
            unmapped_contribution_method=unmapped_contribution_method,
            unmapped_contribution_filters=unmapped_contribution_filters,
            tip_pool_cadence_settings=tip_pool_cadence_settings,
            created=created,
            modified=modified,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.tip_pool_get_settings_response_data_item_day_part_uuids import TipPoolGetSettingsResponseDataItemDayPartUuids
from 7_shifts_python_sdk.model.tip_pool_get_settings_response_data_item_tip_pool_cadence_settings import TipPoolGetSettingsResponseDataItemTipPoolCadenceSettings
from 7_shifts_python_sdk.model.tip_pool_get_settings_response_data_item_tip_pool_contributions import TipPoolGetSettingsResponseDataItemTipPoolContributions
from 7_shifts_python_sdk.model.tip_pool_get_settings_response_data_item_tip_pool_stakeholders import TipPoolGetSettingsResponseDataItemTipPoolStakeholders
from 7_shifts_python_sdk.model.tip_pool_get_settings_response_data_item_unmapped_contribution_filters import TipPoolGetSettingsResponseDataItemUnmappedContributionFilters