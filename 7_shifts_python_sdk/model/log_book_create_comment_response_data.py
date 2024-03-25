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


class LogBookCreateCommentResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "log_book_id",
            "user_id",
            "created",
            "id",
            "message",
            "uuid",
        }
        
        class properties:
            id = schemas.IntSchema
            uuid = schemas.UUIDSchema
            log_book_id = schemas.IntSchema
            user_id = schemas.IntSchema
            message = schemas.StrSchema
            created = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "uuid": uuid,
                "log_book_id": log_book_id,
                "user_id": user_id,
                "message": message,
                "created": created,
            }
    
    log_book_id: MetaOapg.properties.log_book_id
    user_id: MetaOapg.properties.user_id
    created: MetaOapg.properties.created
    id: MetaOapg.properties.id
    message: MetaOapg.properties.message
    uuid: MetaOapg.properties.uuid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_book_id"]) -> MetaOapg.properties.log_book_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "uuid", "log_book_id", "user_id", "message", "created", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_book_id"]) -> MetaOapg.properties.log_book_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "uuid", "log_book_id", "user_id", "message", "created", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        log_book_id: typing.Union[MetaOapg.properties.log_book_id, decimal.Decimal, int, ],
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogBookCreateCommentResponseData':
        return super().__new__(
            cls,
            *args,
            log_book_id=log_book_id,
            user_id=user_id,
            created=created,
            id=id,
            message=message,
            uuid=uuid,
            _configuration=_configuration,
            **kwargs,
        )
