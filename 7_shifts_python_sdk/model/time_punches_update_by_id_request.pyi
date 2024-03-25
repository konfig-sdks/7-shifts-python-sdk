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


class TimePunchesUpdateByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            department_id = schemas.IntSchema
            role_id = schemas.IntSchema
            clocked_in = schemas.DateTimeSchema
            clocked_out = schemas.DateTimeSchema
            notes = schemas.StrSchema
            
            
            class tips(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tips':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def breaks() -> typing.Type['TimePunchesUpdateByIdRequestBreaks']:
                return TimePunchesUpdateByIdRequestBreaks
            __annotations__ = {
                "department_id": department_id,
                "role_id": role_id,
                "clocked_in": clocked_in,
                "clocked_out": clocked_out,
                "notes": notes,
                "tips": tips,
                "breaks": breaks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clocked_in"]) -> MetaOapg.properties.clocked_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clocked_out"]) -> MetaOapg.properties.clocked_out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tips"]) -> MetaOapg.properties.tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breaks"]) -> 'TimePunchesUpdateByIdRequestBreaks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["department_id", "role_id", "clocked_in", "clocked_out", "notes", "tips", "breaks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role_id"]) -> typing.Union[MetaOapg.properties.role_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clocked_in"]) -> typing.Union[MetaOapg.properties.clocked_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clocked_out"]) -> typing.Union[MetaOapg.properties.clocked_out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tips"]) -> typing.Union[MetaOapg.properties.tips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breaks"]) -> typing.Union['TimePunchesUpdateByIdRequestBreaks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["department_id", "role_id", "clocked_in", "clocked_out", "notes", "tips", "breaks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        department_id: typing.Union[MetaOapg.properties.department_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        role_id: typing.Union[MetaOapg.properties.role_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        clocked_in: typing.Union[MetaOapg.properties.clocked_in, str, datetime, schemas.Unset] = schemas.unset,
        clocked_out: typing.Union[MetaOapg.properties.clocked_out, str, datetime, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        tips: typing.Union[MetaOapg.properties.tips, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        breaks: typing.Union['TimePunchesUpdateByIdRequestBreaks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimePunchesUpdateByIdRequest':
        return super().__new__(
            cls,
            *args,
            department_id=department_id,
            role_id=role_id,
            clocked_in=clocked_in,
            clocked_out=clocked_out,
            notes=notes,
            tips=tips,
            breaks=breaks,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.time_punches_update_by_id_request_breaks import TimePunchesUpdateByIdRequestBreaks
