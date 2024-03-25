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


class TimeOffDeclineRequest200Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "hours",
            "comments",
            "company_id",
            "from_date",
            "amount_of_hours",
            "created",
            "status_action_user_id",
            "partial_to",
            "partial_from",
            "status_action_message",
            "to_date",
            "user_id",
            "id",
            "category",
            "partial",
            "status",
        }
        
        class properties:
            id = schemas.IntSchema
            user_id = schemas.IntSchema
            company_id = schemas.IntSchema
            from_date = schemas.StrSchema
            to_date = schemas.StrSchema
            partial = schemas.BoolSchema
            
            
            class partial_from(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'partial_from':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class partial_to(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'partial_to':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            comments = schemas.StrSchema
            status = schemas.IntSchema
            
            
            class status_action_user_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status_action_user_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            status_action_message = schemas.StrSchema
            category = schemas.StrSchema
            created = schemas.StrSchema
            amount_of_hours = schemas.NumberSchema
        
            @staticmethod
            def hours() -> typing.Type['TimeOffDeclineRequest200ResponseHours']:
                return TimeOffDeclineRequest200ResponseHours
            __annotations__ = {
                "id": id,
                "user_id": user_id,
                "company_id": company_id,
                "from_date": from_date,
                "to_date": to_date,
                "partial": partial,
                "partial_from": partial_from,
                "partial_to": partial_to,
                "comments": comments,
                "status": status,
                "status_action_user_id": status_action_user_id,
                "status_action_message": status_action_message,
                "category": category,
                "created": created,
                "amount_of_hours": amount_of_hours,
                "hours": hours,
            }
    
    hours: 'TimeOffDeclineRequest200ResponseHours'
    comments: MetaOapg.properties.comments
    company_id: MetaOapg.properties.company_id
    from_date: MetaOapg.properties.from_date
    amount_of_hours: MetaOapg.properties.amount_of_hours
    created: MetaOapg.properties.created
    status_action_user_id: MetaOapg.properties.status_action_user_id
    partial_to: MetaOapg.properties.partial_to
    partial_from: MetaOapg.properties.partial_from
    status_action_message: MetaOapg.properties.status_action_message
    to_date: MetaOapg.properties.to_date
    user_id: MetaOapg.properties.user_id
    id: MetaOapg.properties.id
    category: MetaOapg.properties.category
    partial: MetaOapg.properties.partial
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_date"]) -> MetaOapg.properties.from_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_date"]) -> MetaOapg.properties.to_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partial"]) -> MetaOapg.properties.partial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partial_from"]) -> MetaOapg.properties.partial_from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partial_to"]) -> MetaOapg.properties.partial_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_action_user_id"]) -> MetaOapg.properties.status_action_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_action_message"]) -> MetaOapg.properties.status_action_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_of_hours"]) -> MetaOapg.properties.amount_of_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> 'TimeOffDeclineRequest200ResponseHours': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "company_id", "from_date", "to_date", "partial", "partial_from", "partial_to", "comments", "status", "status_action_user_id", "status_action_message", "category", "created", "amount_of_hours", "hours", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_date"]) -> MetaOapg.properties.from_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_date"]) -> MetaOapg.properties.to_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partial"]) -> MetaOapg.properties.partial: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partial_from"]) -> MetaOapg.properties.partial_from: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partial_to"]) -> MetaOapg.properties.partial_to: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_action_user_id"]) -> MetaOapg.properties.status_action_user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_action_message"]) -> MetaOapg.properties.status_action_message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_of_hours"]) -> MetaOapg.properties.amount_of_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> 'TimeOffDeclineRequest200ResponseHours': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "company_id", "from_date", "to_date", "partial", "partial_from", "partial_to", "comments", "status", "status_action_user_id", "status_action_message", "category", "created", "amount_of_hours", "hours", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hours: 'TimeOffDeclineRequest200ResponseHours',
        comments: typing.Union[MetaOapg.properties.comments, str, ],
        company_id: typing.Union[MetaOapg.properties.company_id, decimal.Decimal, int, ],
        from_date: typing.Union[MetaOapg.properties.from_date, str, ],
        amount_of_hours: typing.Union[MetaOapg.properties.amount_of_hours, decimal.Decimal, int, float, ],
        created: typing.Union[MetaOapg.properties.created, str, ],
        status_action_user_id: typing.Union[MetaOapg.properties.status_action_user_id, None, decimal.Decimal, int, ],
        partial_to: typing.Union[MetaOapg.properties.partial_to, None, str, ],
        partial_from: typing.Union[MetaOapg.properties.partial_from, None, str, ],
        status_action_message: typing.Union[MetaOapg.properties.status_action_message, str, ],
        to_date: typing.Union[MetaOapg.properties.to_date, str, ],
        user_id: typing.Union[MetaOapg.properties.user_id, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        partial: typing.Union[MetaOapg.properties.partial, bool, ],
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffDeclineRequest200Response':
        return super().__new__(
            cls,
            *args,
            hours=hours,
            comments=comments,
            company_id=company_id,
            from_date=from_date,
            amount_of_hours=amount_of_hours,
            created=created,
            status_action_user_id=status_action_user_id,
            partial_to=partial_to,
            partial_from=partial_from,
            status_action_message=status_action_message,
            to_date=to_date,
            user_id=user_id,
            id=id,
            category=category,
            partial=partial,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.time_off_decline_request200_response_hours import TimeOffDeclineRequest200ResponseHours
