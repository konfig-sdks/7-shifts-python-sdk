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


class CompaniesGetLaborSettingsResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "consecutive_days_multiplier",
            "consecutive_days_threshold",
            "jurisdiction",
            "premium_overtime_multiplier",
            "use_jurisdiction_minimum_wage_for_ot",
            "daily_overtime_multiplier",
            "auto_break_enabled",
            "overtime_enabled",
            "exception_cost_enabled",
            "auto_break_minutes_2",
            "wage_based_roles_enabled",
            "is_custom",
            "overtime_by_location_enabled",
            "weekly_overtime_threshold",
            "auto_break_hours",
            "regular_rate_of_pay_enabled",
            "company_id",
            "auto_break_minutes",
            "ot_alerts_buffer_minutes",
            "split_hours_on_holidays",
            "weekly_overtime_multiplier",
            "auto_break_hours_2",
            "premium_overtime_threshold",
            "ot_alerts_enabled",
            "daily_overtime_threshold",
        }
        
        class properties:
            company_id = schemas.IntSchema
            
            
            class consecutive_days_threshold(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'consecutive_days_threshold':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class consecutive_days_multiplier(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'consecutive_days_multiplier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            regular_rate_of_pay_enabled = schemas.BoolSchema
            exception_cost_enabled = schemas.BoolSchema
            overtime_by_location_enabled = schemas.BoolSchema
            auto_break_enabled = schemas.BoolSchema
            auto_break_hours = schemas.NumberSchema
            auto_break_minutes = schemas.IntSchema
            auto_break_hours_2 = schemas.NumberSchema
            auto_break_minutes_2 = schemas.IntSchema
            overtime_enabled = schemas.BoolSchema
            daily_overtime_threshold = schemas.NumberSchema
            daily_overtime_multiplier = schemas.NumberSchema
            
            
            class premium_overtime_threshold(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'premium_overtime_threshold':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class premium_overtime_multiplier(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'premium_overtime_multiplier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            weekly_overtime_threshold = schemas.NumberSchema
            weekly_overtime_multiplier = schemas.NumberSchema
            ot_alerts_enabled = schemas.BoolSchema
            
            
            class ot_alerts_buffer_minutes(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ot_alerts_buffer_minutes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            split_hours_on_holidays = schemas.BoolSchema
            wage_based_roles_enabled = schemas.BoolSchema
            
            
            class jurisdiction(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'jurisdiction':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            is_custom = schemas.BoolSchema
            use_jurisdiction_minimum_wage_for_ot = schemas.BoolSchema
            __annotations__ = {
                "company_id": company_id,
                "consecutive_days_threshold": consecutive_days_threshold,
                "consecutive_days_multiplier": consecutive_days_multiplier,
                "regular_rate_of_pay_enabled": regular_rate_of_pay_enabled,
                "exception_cost_enabled": exception_cost_enabled,
                "overtime_by_location_enabled": overtime_by_location_enabled,
                "auto_break_enabled": auto_break_enabled,
                "auto_break_hours": auto_break_hours,
                "auto_break_minutes": auto_break_minutes,
                "auto_break_hours_2": auto_break_hours_2,
                "auto_break_minutes_2": auto_break_minutes_2,
                "overtime_enabled": overtime_enabled,
                "daily_overtime_threshold": daily_overtime_threshold,
                "daily_overtime_multiplier": daily_overtime_multiplier,
                "premium_overtime_threshold": premium_overtime_threshold,
                "premium_overtime_multiplier": premium_overtime_multiplier,
                "weekly_overtime_threshold": weekly_overtime_threshold,
                "weekly_overtime_multiplier": weekly_overtime_multiplier,
                "ot_alerts_enabled": ot_alerts_enabled,
                "ot_alerts_buffer_minutes": ot_alerts_buffer_minutes,
                "split_hours_on_holidays": split_hours_on_holidays,
                "wage_based_roles_enabled": wage_based_roles_enabled,
                "jurisdiction": jurisdiction,
                "is_custom": is_custom,
                "use_jurisdiction_minimum_wage_for_ot": use_jurisdiction_minimum_wage_for_ot,
            }
    
    consecutive_days_multiplier: MetaOapg.properties.consecutive_days_multiplier
    consecutive_days_threshold: MetaOapg.properties.consecutive_days_threshold
    jurisdiction: MetaOapg.properties.jurisdiction
    premium_overtime_multiplier: MetaOapg.properties.premium_overtime_multiplier
    use_jurisdiction_minimum_wage_for_ot: MetaOapg.properties.use_jurisdiction_minimum_wage_for_ot
    daily_overtime_multiplier: MetaOapg.properties.daily_overtime_multiplier
    auto_break_enabled: MetaOapg.properties.auto_break_enabled
    overtime_enabled: MetaOapg.properties.overtime_enabled
    exception_cost_enabled: MetaOapg.properties.exception_cost_enabled
    auto_break_minutes_2: MetaOapg.properties.auto_break_minutes_2
    wage_based_roles_enabled: MetaOapg.properties.wage_based_roles_enabled
    is_custom: MetaOapg.properties.is_custom
    overtime_by_location_enabled: MetaOapg.properties.overtime_by_location_enabled
    weekly_overtime_threshold: MetaOapg.properties.weekly_overtime_threshold
    auto_break_hours: MetaOapg.properties.auto_break_hours
    regular_rate_of_pay_enabled: MetaOapg.properties.regular_rate_of_pay_enabled
    company_id: MetaOapg.properties.company_id
    auto_break_minutes: MetaOapg.properties.auto_break_minutes
    ot_alerts_buffer_minutes: MetaOapg.properties.ot_alerts_buffer_minutes
    split_hours_on_holidays: MetaOapg.properties.split_hours_on_holidays
    weekly_overtime_multiplier: MetaOapg.properties.weekly_overtime_multiplier
    auto_break_hours_2: MetaOapg.properties.auto_break_hours_2
    premium_overtime_threshold: MetaOapg.properties.premium_overtime_threshold
    ot_alerts_enabled: MetaOapg.properties.ot_alerts_enabled
    daily_overtime_threshold: MetaOapg.properties.daily_overtime_threshold
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consecutive_days_threshold"]) -> MetaOapg.properties.consecutive_days_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consecutive_days_multiplier"]) -> MetaOapg.properties.consecutive_days_multiplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regular_rate_of_pay_enabled"]) -> MetaOapg.properties.regular_rate_of_pay_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exception_cost_enabled"]) -> MetaOapg.properties.exception_cost_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtime_by_location_enabled"]) -> MetaOapg.properties.overtime_by_location_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_break_enabled"]) -> MetaOapg.properties.auto_break_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_break_hours"]) -> MetaOapg.properties.auto_break_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_break_minutes"]) -> MetaOapg.properties.auto_break_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_break_hours_2"]) -> MetaOapg.properties.auto_break_hours_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_break_minutes_2"]) -> MetaOapg.properties.auto_break_minutes_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtime_enabled"]) -> MetaOapg.properties.overtime_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daily_overtime_threshold"]) -> MetaOapg.properties.daily_overtime_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daily_overtime_multiplier"]) -> MetaOapg.properties.daily_overtime_multiplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["premium_overtime_threshold"]) -> MetaOapg.properties.premium_overtime_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["premium_overtime_multiplier"]) -> MetaOapg.properties.premium_overtime_multiplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekly_overtime_threshold"]) -> MetaOapg.properties.weekly_overtime_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekly_overtime_multiplier"]) -> MetaOapg.properties.weekly_overtime_multiplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ot_alerts_enabled"]) -> MetaOapg.properties.ot_alerts_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ot_alerts_buffer_minutes"]) -> MetaOapg.properties.ot_alerts_buffer_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["split_hours_on_holidays"]) -> MetaOapg.properties.split_hours_on_holidays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage_based_roles_enabled"]) -> MetaOapg.properties.wage_based_roles_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jurisdiction"]) -> MetaOapg.properties.jurisdiction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_custom"]) -> MetaOapg.properties.is_custom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_jurisdiction_minimum_wage_for_ot"]) -> MetaOapg.properties.use_jurisdiction_minimum_wage_for_ot: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_id", "consecutive_days_threshold", "consecutive_days_multiplier", "regular_rate_of_pay_enabled", "exception_cost_enabled", "overtime_by_location_enabled", "auto_break_enabled", "auto_break_hours", "auto_break_minutes", "auto_break_hours_2", "auto_break_minutes_2", "overtime_enabled", "daily_overtime_threshold", "daily_overtime_multiplier", "premium_overtime_threshold", "premium_overtime_multiplier", "weekly_overtime_threshold", "weekly_overtime_multiplier", "ot_alerts_enabled", "ot_alerts_buffer_minutes", "split_hours_on_holidays", "wage_based_roles_enabled", "jurisdiction", "is_custom", "use_jurisdiction_minimum_wage_for_ot", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consecutive_days_threshold"]) -> MetaOapg.properties.consecutive_days_threshold: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consecutive_days_multiplier"]) -> MetaOapg.properties.consecutive_days_multiplier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regular_rate_of_pay_enabled"]) -> MetaOapg.properties.regular_rate_of_pay_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exception_cost_enabled"]) -> MetaOapg.properties.exception_cost_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtime_by_location_enabled"]) -> MetaOapg.properties.overtime_by_location_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_break_enabled"]) -> MetaOapg.properties.auto_break_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_break_hours"]) -> MetaOapg.properties.auto_break_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_break_minutes"]) -> MetaOapg.properties.auto_break_minutes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_break_hours_2"]) -> MetaOapg.properties.auto_break_hours_2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_break_minutes_2"]) -> MetaOapg.properties.auto_break_minutes_2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtime_enabled"]) -> MetaOapg.properties.overtime_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daily_overtime_threshold"]) -> MetaOapg.properties.daily_overtime_threshold: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daily_overtime_multiplier"]) -> MetaOapg.properties.daily_overtime_multiplier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["premium_overtime_threshold"]) -> MetaOapg.properties.premium_overtime_threshold: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["premium_overtime_multiplier"]) -> MetaOapg.properties.premium_overtime_multiplier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekly_overtime_threshold"]) -> MetaOapg.properties.weekly_overtime_threshold: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekly_overtime_multiplier"]) -> MetaOapg.properties.weekly_overtime_multiplier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ot_alerts_enabled"]) -> MetaOapg.properties.ot_alerts_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ot_alerts_buffer_minutes"]) -> MetaOapg.properties.ot_alerts_buffer_minutes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["split_hours_on_holidays"]) -> MetaOapg.properties.split_hours_on_holidays: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage_based_roles_enabled"]) -> MetaOapg.properties.wage_based_roles_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jurisdiction"]) -> MetaOapg.properties.jurisdiction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_custom"]) -> MetaOapg.properties.is_custom: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_jurisdiction_minimum_wage_for_ot"]) -> MetaOapg.properties.use_jurisdiction_minimum_wage_for_ot: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_id", "consecutive_days_threshold", "consecutive_days_multiplier", "regular_rate_of_pay_enabled", "exception_cost_enabled", "overtime_by_location_enabled", "auto_break_enabled", "auto_break_hours", "auto_break_minutes", "auto_break_hours_2", "auto_break_minutes_2", "overtime_enabled", "daily_overtime_threshold", "daily_overtime_multiplier", "premium_overtime_threshold", "premium_overtime_multiplier", "weekly_overtime_threshold", "weekly_overtime_multiplier", "ot_alerts_enabled", "ot_alerts_buffer_minutes", "split_hours_on_holidays", "wage_based_roles_enabled", "jurisdiction", "is_custom", "use_jurisdiction_minimum_wage_for_ot", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        consecutive_days_multiplier: typing.Union[MetaOapg.properties.consecutive_days_multiplier, None, decimal.Decimal, int, float, ],
        consecutive_days_threshold: typing.Union[MetaOapg.properties.consecutive_days_threshold, None, decimal.Decimal, int, ],
        jurisdiction: typing.Union[MetaOapg.properties.jurisdiction, None, str, ],
        premium_overtime_multiplier: typing.Union[MetaOapg.properties.premium_overtime_multiplier, None, decimal.Decimal, int, float, ],
        use_jurisdiction_minimum_wage_for_ot: typing.Union[MetaOapg.properties.use_jurisdiction_minimum_wage_for_ot, bool, ],
        daily_overtime_multiplier: typing.Union[MetaOapg.properties.daily_overtime_multiplier, decimal.Decimal, int, float, ],
        auto_break_enabled: typing.Union[MetaOapg.properties.auto_break_enabled, bool, ],
        overtime_enabled: typing.Union[MetaOapg.properties.overtime_enabled, bool, ],
        exception_cost_enabled: typing.Union[MetaOapg.properties.exception_cost_enabled, bool, ],
        auto_break_minutes_2: typing.Union[MetaOapg.properties.auto_break_minutes_2, decimal.Decimal, int, ],
        wage_based_roles_enabled: typing.Union[MetaOapg.properties.wage_based_roles_enabled, bool, ],
        is_custom: typing.Union[MetaOapg.properties.is_custom, bool, ],
        overtime_by_location_enabled: typing.Union[MetaOapg.properties.overtime_by_location_enabled, bool, ],
        weekly_overtime_threshold: typing.Union[MetaOapg.properties.weekly_overtime_threshold, decimal.Decimal, int, float, ],
        auto_break_hours: typing.Union[MetaOapg.properties.auto_break_hours, decimal.Decimal, int, float, ],
        regular_rate_of_pay_enabled: typing.Union[MetaOapg.properties.regular_rate_of_pay_enabled, bool, ],
        company_id: typing.Union[MetaOapg.properties.company_id, decimal.Decimal, int, ],
        auto_break_minutes: typing.Union[MetaOapg.properties.auto_break_minutes, decimal.Decimal, int, ],
        ot_alerts_buffer_minutes: typing.Union[MetaOapg.properties.ot_alerts_buffer_minutes, None, decimal.Decimal, int, ],
        split_hours_on_holidays: typing.Union[MetaOapg.properties.split_hours_on_holidays, bool, ],
        weekly_overtime_multiplier: typing.Union[MetaOapg.properties.weekly_overtime_multiplier, decimal.Decimal, int, float, ],
        auto_break_hours_2: typing.Union[MetaOapg.properties.auto_break_hours_2, decimal.Decimal, int, float, ],
        premium_overtime_threshold: typing.Union[MetaOapg.properties.premium_overtime_threshold, None, decimal.Decimal, int, ],
        ot_alerts_enabled: typing.Union[MetaOapg.properties.ot_alerts_enabled, bool, ],
        daily_overtime_threshold: typing.Union[MetaOapg.properties.daily_overtime_threshold, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesGetLaborSettingsResponseData':
        return super().__new__(
            cls,
            *args,
            consecutive_days_multiplier=consecutive_days_multiplier,
            consecutive_days_threshold=consecutive_days_threshold,
            jurisdiction=jurisdiction,
            premium_overtime_multiplier=premium_overtime_multiplier,
            use_jurisdiction_minimum_wage_for_ot=use_jurisdiction_minimum_wage_for_ot,
            daily_overtime_multiplier=daily_overtime_multiplier,
            auto_break_enabled=auto_break_enabled,
            overtime_enabled=overtime_enabled,
            exception_cost_enabled=exception_cost_enabled,
            auto_break_minutes_2=auto_break_minutes_2,
            wage_based_roles_enabled=wage_based_roles_enabled,
            is_custom=is_custom,
            overtime_by_location_enabled=overtime_by_location_enabled,
            weekly_overtime_threshold=weekly_overtime_threshold,
            auto_break_hours=auto_break_hours,
            regular_rate_of_pay_enabled=regular_rate_of_pay_enabled,
            company_id=company_id,
            auto_break_minutes=auto_break_minutes,
            ot_alerts_buffer_minutes=ot_alerts_buffer_minutes,
            split_hours_on_holidays=split_hours_on_holidays,
            weekly_overtime_multiplier=weekly_overtime_multiplier,
            auto_break_hours_2=auto_break_hours_2,
            premium_overtime_threshold=premium_overtime_threshold,
            ot_alerts_enabled=ot_alerts_enabled,
            daily_overtime_threshold=daily_overtime_threshold,
            _configuration=_configuration,
            **kwargs,
        )
