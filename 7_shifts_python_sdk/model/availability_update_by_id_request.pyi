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


class AvailabilityUpdateByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class week(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'week':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class week_to(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'week_to':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            repeat = schemas.BoolSchema
            mon = schemas.IntSchema
            mon_from = schemas.StrSchema
            mon_to = schemas.StrSchema
            
            
            class mon_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mon_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            mon_reason = schemas.StrSchema
            tue = schemas.IntSchema
            tue_from = schemas.StrSchema
            tue_to = schemas.StrSchema
            
            
            class tue_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tue_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            tue_reason = schemas.StrSchema
            wed = schemas.IntSchema
            wed_from = schemas.StrSchema
            wed_to = schemas.StrSchema
            
            
            class wed_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'wed_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            wed_reason = schemas.StrSchema
            thu = schemas.IntSchema
            thu_from = schemas.StrSchema
            thu_to = schemas.StrSchema
            
            
            class thu_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thu_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            thu_reason = schemas.StrSchema
            fri = schemas.IntSchema
            fri_from = schemas.StrSchema
            fri_to = schemas.StrSchema
            
            
            class fri_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fri_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            fri_reason = schemas.StrSchema
            sat = schemas.IntSchema
            sat_from = schemas.StrSchema
            sat_to = schemas.StrSchema
            
            
            class sat_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sat_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            sat_reason = schemas.StrSchema
            sun = schemas.IntSchema
            sun_from = schemas.StrSchema
            sun_to = schemas.StrSchema
            
            
            class sun_comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sun_comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            sun_reason = schemas.StrSchema
            __annotations__ = {
                "week": week,
                "week_to": week_to,
                "repeat": repeat,
                "mon": mon,
                "mon_from": mon_from,
                "mon_to": mon_to,
                "mon_comments": mon_comments,
                "mon_reason": mon_reason,
                "tue": tue,
                "tue_from": tue_from,
                "tue_to": tue_to,
                "tue_comments": tue_comments,
                "tue_reason": tue_reason,
                "wed": wed,
                "wed_from": wed_from,
                "wed_to": wed_to,
                "wed_comments": wed_comments,
                "wed_reason": wed_reason,
                "thu": thu,
                "thu_from": thu_from,
                "thu_to": thu_to,
                "thu_comments": thu_comments,
                "thu_reason": thu_reason,
                "fri": fri,
                "fri_from": fri_from,
                "fri_to": fri_to,
                "fri_comments": fri_comments,
                "fri_reason": fri_reason,
                "sat": sat,
                "sat_from": sat_from,
                "sat_to": sat_to,
                "sat_comments": sat_comments,
                "sat_reason": sat_reason,
                "sun": sun,
                "sun_from": sun_from,
                "sun_to": sun_to,
                "sun_comments": sun_comments,
                "sun_reason": sun_reason,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["week"]) -> MetaOapg.properties.week: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["week_to"]) -> MetaOapg.properties.week_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repeat"]) -> MetaOapg.properties.repeat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mon"]) -> MetaOapg.properties.mon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mon_from"]) -> MetaOapg.properties.mon_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mon_to"]) -> MetaOapg.properties.mon_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mon_comments"]) -> MetaOapg.properties.mon_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mon_reason"]) -> MetaOapg.properties.mon_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tue"]) -> MetaOapg.properties.tue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tue_from"]) -> MetaOapg.properties.tue_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tue_to"]) -> MetaOapg.properties.tue_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tue_comments"]) -> MetaOapg.properties.tue_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tue_reason"]) -> MetaOapg.properties.tue_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wed"]) -> MetaOapg.properties.wed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wed_from"]) -> MetaOapg.properties.wed_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wed_to"]) -> MetaOapg.properties.wed_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wed_comments"]) -> MetaOapg.properties.wed_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wed_reason"]) -> MetaOapg.properties.wed_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thu"]) -> MetaOapg.properties.thu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thu_from"]) -> MetaOapg.properties.thu_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thu_to"]) -> MetaOapg.properties.thu_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thu_comments"]) -> MetaOapg.properties.thu_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thu_reason"]) -> MetaOapg.properties.thu_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fri"]) -> MetaOapg.properties.fri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fri_from"]) -> MetaOapg.properties.fri_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fri_to"]) -> MetaOapg.properties.fri_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fri_comments"]) -> MetaOapg.properties.fri_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fri_reason"]) -> MetaOapg.properties.fri_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sat"]) -> MetaOapg.properties.sat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sat_from"]) -> MetaOapg.properties.sat_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sat_to"]) -> MetaOapg.properties.sat_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sat_comments"]) -> MetaOapg.properties.sat_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sat_reason"]) -> MetaOapg.properties.sat_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sun"]) -> MetaOapg.properties.sun: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sun_from"]) -> MetaOapg.properties.sun_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sun_to"]) -> MetaOapg.properties.sun_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sun_comments"]) -> MetaOapg.properties.sun_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sun_reason"]) -> MetaOapg.properties.sun_reason: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["week", "week_to", "repeat", "mon", "mon_from", "mon_to", "mon_comments", "mon_reason", "tue", "tue_from", "tue_to", "tue_comments", "tue_reason", "wed", "wed_from", "wed_to", "wed_comments", "wed_reason", "thu", "thu_from", "thu_to", "thu_comments", "thu_reason", "fri", "fri_from", "fri_to", "fri_comments", "fri_reason", "sat", "sat_from", "sat_to", "sat_comments", "sat_reason", "sun", "sun_from", "sun_to", "sun_comments", "sun_reason", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["week"]) -> typing.Union[MetaOapg.properties.week, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["week_to"]) -> typing.Union[MetaOapg.properties.week_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repeat"]) -> typing.Union[MetaOapg.properties.repeat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mon"]) -> typing.Union[MetaOapg.properties.mon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mon_from"]) -> typing.Union[MetaOapg.properties.mon_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mon_to"]) -> typing.Union[MetaOapg.properties.mon_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mon_comments"]) -> typing.Union[MetaOapg.properties.mon_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mon_reason"]) -> typing.Union[MetaOapg.properties.mon_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tue"]) -> typing.Union[MetaOapg.properties.tue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tue_from"]) -> typing.Union[MetaOapg.properties.tue_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tue_to"]) -> typing.Union[MetaOapg.properties.tue_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tue_comments"]) -> typing.Union[MetaOapg.properties.tue_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tue_reason"]) -> typing.Union[MetaOapg.properties.tue_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wed"]) -> typing.Union[MetaOapg.properties.wed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wed_from"]) -> typing.Union[MetaOapg.properties.wed_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wed_to"]) -> typing.Union[MetaOapg.properties.wed_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wed_comments"]) -> typing.Union[MetaOapg.properties.wed_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wed_reason"]) -> typing.Union[MetaOapg.properties.wed_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thu"]) -> typing.Union[MetaOapg.properties.thu, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thu_from"]) -> typing.Union[MetaOapg.properties.thu_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thu_to"]) -> typing.Union[MetaOapg.properties.thu_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thu_comments"]) -> typing.Union[MetaOapg.properties.thu_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thu_reason"]) -> typing.Union[MetaOapg.properties.thu_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fri"]) -> typing.Union[MetaOapg.properties.fri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fri_from"]) -> typing.Union[MetaOapg.properties.fri_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fri_to"]) -> typing.Union[MetaOapg.properties.fri_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fri_comments"]) -> typing.Union[MetaOapg.properties.fri_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fri_reason"]) -> typing.Union[MetaOapg.properties.fri_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sat"]) -> typing.Union[MetaOapg.properties.sat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sat_from"]) -> typing.Union[MetaOapg.properties.sat_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sat_to"]) -> typing.Union[MetaOapg.properties.sat_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sat_comments"]) -> typing.Union[MetaOapg.properties.sat_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sat_reason"]) -> typing.Union[MetaOapg.properties.sat_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sun"]) -> typing.Union[MetaOapg.properties.sun, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sun_from"]) -> typing.Union[MetaOapg.properties.sun_from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sun_to"]) -> typing.Union[MetaOapg.properties.sun_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sun_comments"]) -> typing.Union[MetaOapg.properties.sun_comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sun_reason"]) -> typing.Union[MetaOapg.properties.sun_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["week", "week_to", "repeat", "mon", "mon_from", "mon_to", "mon_comments", "mon_reason", "tue", "tue_from", "tue_to", "tue_comments", "tue_reason", "wed", "wed_from", "wed_to", "wed_comments", "wed_reason", "thu", "thu_from", "thu_to", "thu_comments", "thu_reason", "fri", "fri_from", "fri_to", "fri_comments", "fri_reason", "sat", "sat_from", "sat_to", "sat_comments", "sat_reason", "sun", "sun_from", "sun_to", "sun_comments", "sun_reason", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        week: typing.Union[MetaOapg.properties.week, None, str, schemas.Unset] = schemas.unset,
        week_to: typing.Union[MetaOapg.properties.week_to, None, str, schemas.Unset] = schemas.unset,
        repeat: typing.Union[MetaOapg.properties.repeat, bool, schemas.Unset] = schemas.unset,
        mon: typing.Union[MetaOapg.properties.mon, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        mon_from: typing.Union[MetaOapg.properties.mon_from, str, schemas.Unset] = schemas.unset,
        mon_to: typing.Union[MetaOapg.properties.mon_to, str, schemas.Unset] = schemas.unset,
        mon_comments: typing.Union[MetaOapg.properties.mon_comments, None, str, schemas.Unset] = schemas.unset,
        mon_reason: typing.Union[MetaOapg.properties.mon_reason, str, schemas.Unset] = schemas.unset,
        tue: typing.Union[MetaOapg.properties.tue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tue_from: typing.Union[MetaOapg.properties.tue_from, str, schemas.Unset] = schemas.unset,
        tue_to: typing.Union[MetaOapg.properties.tue_to, str, schemas.Unset] = schemas.unset,
        tue_comments: typing.Union[MetaOapg.properties.tue_comments, None, str, schemas.Unset] = schemas.unset,
        tue_reason: typing.Union[MetaOapg.properties.tue_reason, str, schemas.Unset] = schemas.unset,
        wed: typing.Union[MetaOapg.properties.wed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wed_from: typing.Union[MetaOapg.properties.wed_from, str, schemas.Unset] = schemas.unset,
        wed_to: typing.Union[MetaOapg.properties.wed_to, str, schemas.Unset] = schemas.unset,
        wed_comments: typing.Union[MetaOapg.properties.wed_comments, None, str, schemas.Unset] = schemas.unset,
        wed_reason: typing.Union[MetaOapg.properties.wed_reason, str, schemas.Unset] = schemas.unset,
        thu: typing.Union[MetaOapg.properties.thu, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        thu_from: typing.Union[MetaOapg.properties.thu_from, str, schemas.Unset] = schemas.unset,
        thu_to: typing.Union[MetaOapg.properties.thu_to, str, schemas.Unset] = schemas.unset,
        thu_comments: typing.Union[MetaOapg.properties.thu_comments, None, str, schemas.Unset] = schemas.unset,
        thu_reason: typing.Union[MetaOapg.properties.thu_reason, str, schemas.Unset] = schemas.unset,
        fri: typing.Union[MetaOapg.properties.fri, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fri_from: typing.Union[MetaOapg.properties.fri_from, str, schemas.Unset] = schemas.unset,
        fri_to: typing.Union[MetaOapg.properties.fri_to, str, schemas.Unset] = schemas.unset,
        fri_comments: typing.Union[MetaOapg.properties.fri_comments, None, str, schemas.Unset] = schemas.unset,
        fri_reason: typing.Union[MetaOapg.properties.fri_reason, str, schemas.Unset] = schemas.unset,
        sat: typing.Union[MetaOapg.properties.sat, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sat_from: typing.Union[MetaOapg.properties.sat_from, str, schemas.Unset] = schemas.unset,
        sat_to: typing.Union[MetaOapg.properties.sat_to, str, schemas.Unset] = schemas.unset,
        sat_comments: typing.Union[MetaOapg.properties.sat_comments, None, str, schemas.Unset] = schemas.unset,
        sat_reason: typing.Union[MetaOapg.properties.sat_reason, str, schemas.Unset] = schemas.unset,
        sun: typing.Union[MetaOapg.properties.sun, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sun_from: typing.Union[MetaOapg.properties.sun_from, str, schemas.Unset] = schemas.unset,
        sun_to: typing.Union[MetaOapg.properties.sun_to, str, schemas.Unset] = schemas.unset,
        sun_comments: typing.Union[MetaOapg.properties.sun_comments, None, str, schemas.Unset] = schemas.unset,
        sun_reason: typing.Union[MetaOapg.properties.sun_reason, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AvailabilityUpdateByIdRequest':
        return super().__new__(
            cls,
            *args,
            week=week,
            week_to=week_to,
            repeat=repeat,
            mon=mon,
            mon_from=mon_from,
            mon_to=mon_to,
            mon_comments=mon_comments,
            mon_reason=mon_reason,
            tue=tue,
            tue_from=tue_from,
            tue_to=tue_to,
            tue_comments=tue_comments,
            tue_reason=tue_reason,
            wed=wed,
            wed_from=wed_from,
            wed_to=wed_to,
            wed_comments=wed_comments,
            wed_reason=wed_reason,
            thu=thu,
            thu_from=thu_from,
            thu_to=thu_to,
            thu_comments=thu_comments,
            thu_reason=thu_reason,
            fri=fri,
            fri_from=fri_from,
            fri_to=fri_to,
            fri_comments=fri_comments,
            fri_reason=fri_reason,
            sat=sat,
            sat_from=sat_from,
            sat_to=sat_to,
            sat_comments=sat_comments,
            sat_reason=sat_reason,
            sun=sun,
            sun_from=sun_from,
            sun_to=sun_to,
            sun_comments=sun_comments,
            sun_reason=sun_reason,
            _configuration=_configuration,
            **kwargs,
        )
