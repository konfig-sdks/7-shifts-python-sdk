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


class ReportsGetWorkedHoursWagesResponseUsersItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def user() -> typing.Type['ReportsGetWorkedHoursWagesResponseUsersItemUser']:
                return ReportsGetWorkedHoursWagesResponseUsersItemUser
        
            @staticmethod
            def weeks() -> typing.Type['ReportsGetWorkedHoursWagesResponseUsersItemWeeks']:
                return ReportsGetWorkedHoursWagesResponseUsersItemWeeks
        
            @staticmethod
            def roles() -> typing.Type['ReportsGetWorkedHoursWagesResponseUsersItemRoles']:
                return ReportsGetWorkedHoursWagesResponseUsersItemRoles
        
            @staticmethod
            def total() -> typing.Type['ReportsGetWorkedHoursWagesResponseUsersItemTotal']:
                return ReportsGetWorkedHoursWagesResponseUsersItemTotal
            salaried = schemas.BoolSchema
            __annotations__ = {
                "user": user,
                "weeks": weeks,
                "roles": roles,
                "total": total,
                "salaried": salaried,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'ReportsGetWorkedHoursWagesResponseUsersItemUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weeks"]) -> 'ReportsGetWorkedHoursWagesResponseUsersItemWeeks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> 'ReportsGetWorkedHoursWagesResponseUsersItemRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> 'ReportsGetWorkedHoursWagesResponseUsersItemTotal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaried"]) -> MetaOapg.properties.salaried: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", "weeks", "roles", "total", "salaried", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weeks"]) -> typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemWeeks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemTotal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaried"]) -> typing.Union[MetaOapg.properties.salaried, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", "weeks", "roles", "total", "salaried", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        user: typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemUser', schemas.Unset] = schemas.unset,
        weeks: typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemWeeks', schemas.Unset] = schemas.unset,
        roles: typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemRoles', schemas.Unset] = schemas.unset,
        total: typing.Union['ReportsGetWorkedHoursWagesResponseUsersItemTotal', schemas.Unset] = schemas.unset,
        salaried: typing.Union[MetaOapg.properties.salaried, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetWorkedHoursWagesResponseUsersItem':
        return super().__new__(
            cls,
            *args,
            user=user,
            weeks=weeks,
            roles=roles,
            total=total,
            salaried=salaried,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.reports_get_worked_hours_wages_response_users_item_roles import ReportsGetWorkedHoursWagesResponseUsersItemRoles
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages_response_users_item_total import ReportsGetWorkedHoursWagesResponseUsersItemTotal
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages_response_users_item_user import ReportsGetWorkedHoursWagesResponseUsersItemUser
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages_response_users_item_weeks import ReportsGetWorkedHoursWagesResponseUsersItemWeeks