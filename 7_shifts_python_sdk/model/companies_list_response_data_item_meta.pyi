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


class CompaniesListResponseDataItemMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class signup_utm_source(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'signup_utm_source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class utm_source(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'utm_source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class signup_content_source(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'signup_content_source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            buy_now = schemas.BoolSchema
            trial_checklist_stored_locally = schemas.BoolSchema
            
            
            class employee_count_range(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employee_count_range':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            api_key = schemas.StrSchema
            __annotations__ = {
                "signup_utm_source": signup_utm_source,
                "utm_source": utm_source,
                "signup_content_source": signup_content_source,
                "buy_now": buy_now,
                "trial_checklist_stored_locally": trial_checklist_stored_locally,
                "employee_count_range": employee_count_range,
                "api_key": api_key,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signup_utm_source"]) -> MetaOapg.properties.signup_utm_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utm_source"]) -> MetaOapg.properties.utm_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signup_content_source"]) -> MetaOapg.properties.signup_content_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buy_now"]) -> MetaOapg.properties.buy_now: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trial_checklist_stored_locally"]) -> MetaOapg.properties.trial_checklist_stored_locally: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_count_range"]) -> MetaOapg.properties.employee_count_range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_key"]) -> MetaOapg.properties.api_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["signup_utm_source", "utm_source", "signup_content_source", "buy_now", "trial_checklist_stored_locally", "employee_count_range", "api_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signup_utm_source"]) -> typing.Union[MetaOapg.properties.signup_utm_source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utm_source"]) -> typing.Union[MetaOapg.properties.utm_source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signup_content_source"]) -> typing.Union[MetaOapg.properties.signup_content_source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buy_now"]) -> typing.Union[MetaOapg.properties.buy_now, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial_checklist_stored_locally"]) -> typing.Union[MetaOapg.properties.trial_checklist_stored_locally, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_count_range"]) -> typing.Union[MetaOapg.properties.employee_count_range, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_key"]) -> typing.Union[MetaOapg.properties.api_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["signup_utm_source", "utm_source", "signup_content_source", "buy_now", "trial_checklist_stored_locally", "employee_count_range", "api_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        signup_utm_source: typing.Union[MetaOapg.properties.signup_utm_source, None, str, schemas.Unset] = schemas.unset,
        utm_source: typing.Union[MetaOapg.properties.utm_source, None, str, schemas.Unset] = schemas.unset,
        signup_content_source: typing.Union[MetaOapg.properties.signup_content_source, None, str, schemas.Unset] = schemas.unset,
        buy_now: typing.Union[MetaOapg.properties.buy_now, bool, schemas.Unset] = schemas.unset,
        trial_checklist_stored_locally: typing.Union[MetaOapg.properties.trial_checklist_stored_locally, bool, schemas.Unset] = schemas.unset,
        employee_count_range: typing.Union[MetaOapg.properties.employee_count_range, None, str, schemas.Unset] = schemas.unset,
        api_key: typing.Union[MetaOapg.properties.api_key, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesListResponseDataItemMeta':
        return super().__new__(
            cls,
            *args,
            signup_utm_source=signup_utm_source,
            utm_source=utm_source,
            signup_content_source=signup_content_source,
            buy_now=buy_now,
            trial_checklist_stored_locally=trial_checklist_stored_locally,
            employee_count_range=employee_count_range,
            api_key=api_key,
            _configuration=_configuration,
            **kwargs,
        )
