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


class AuthenticationGenerateOAuthTokenResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "access_token",
            "token_type",
            "expires_in",
        }
        
        class properties:
            
            
            class token_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BEARER(cls):
                    return cls("Bearer")
            expires_in = schemas.IntSchema
            access_token = schemas.StrSchema
            refresh_token = schemas.StrSchema
            __annotations__ = {
                "token_type": token_type,
                "expires_in": expires_in,
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
    
    access_token: MetaOapg.properties.access_token
    token_type: MetaOapg.properties.token_type
    expires_in: MetaOapg.properties.expires_in
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_type"]) -> MetaOapg.properties.token_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token"]) -> MetaOapg.properties.refresh_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_type", "expires_in", "access_token", "refresh_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_type"]) -> MetaOapg.properties.token_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token"]) -> typing.Union[MetaOapg.properties.refresh_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_type", "expires_in", "access_token", "refresh_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access_token: typing.Union[MetaOapg.properties.access_token, str, ],
        token_type: typing.Union[MetaOapg.properties.token_type, str, ],
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, ],
        refresh_token: typing.Union[MetaOapg.properties.refresh_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticationGenerateOAuthTokenResponse':
        return super().__new__(
            cls,
            *args,
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            refresh_token=refresh_token,
            _configuration=_configuration,
            **kwargs,
        )