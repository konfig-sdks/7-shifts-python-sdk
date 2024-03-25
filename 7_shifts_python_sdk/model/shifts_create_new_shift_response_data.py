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


class ShiftsCreateNewShiftResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "notes",
            "unassigned",
            "location_id",
            "role_id",
            "draft",
            "station",
            "modified",
            "end",
            "id",
            "attendance_status",
            "close",
            "publish_status",
            "station_name",
            "open_offer_type",
            "department_id",
            "created",
            "notified",
            "station_id",
            "unassigned_skill_level",
            "start",
            "late_minutes",
            "business_decline",
            "soft_deleted",
            "deleted",
            "user_id",
            "open",
        }
        
        class properties:
            id = schemas.IntSchema
            
            
            class user_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'user_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            start = schemas.DateTimeSchema
            end = schemas.DateTimeSchema
            close = schemas.BoolSchema
            business_decline = schemas.BoolSchema
            
            
            class department_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
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
            location_id = schemas.IntSchema
            
            
            class role_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
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
            notes = schemas.StrSchema
            draft = schemas.BoolSchema
            notified = schemas.BoolSchema
            open = schemas.BoolSchema
            unassigned = schemas.BoolSchema
            unassigned_skill_level = schemas.IntSchema
            
            
            class open_offer_type(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "all_location_members": "ALL_LOCATION_MEMBERS",
                        "all_role_members": "ALL_ROLE_MEMBERS",
                        "set_of_location_members": "SET_OF_LOCATION_MEMBERS",
                        "all_company_employees": "ALL_COMPANY_EMPLOYEES",
                    }
                
                @schemas.classproperty
                def ALL_LOCATION_MEMBERS(cls):
                    return cls("all_location_members")
                
                @schemas.classproperty
                def ALL_ROLE_MEMBERS(cls):
                    return cls("all_role_members")
                
                @schemas.classproperty
                def SET_OF_LOCATION_MEMBERS(cls):
                    return cls("set_of_location_members")
                
                @schemas.classproperty
                def ALL_COMPANY_EMPLOYEES(cls):
                    return cls("all_company_employees")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'open_offer_type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class attendance_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "none": "NONE",
                        "sick": "SICK",
                        "no_show": "NO_SHOW",
                        "late": "LATE",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
                
                @schemas.classproperty
                def SICK(cls):
                    return cls("sick")
                
                @schemas.classproperty
                def NO_SHOW(cls):
                    return cls("no_show")
                
                @schemas.classproperty
                def LATE(cls):
                    return cls("late")
            
            
            class publish_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "draft": "DRAFT",
                        "published": "PUBLISHED",
                        "draft_deleted": "DRAFT_DELETED",
                        "published_deleted": "PUBLISHED_DELETED",
                    }
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
                
                @schemas.classproperty
                def PUBLISHED(cls):
                    return cls("published")
                
                @schemas.classproperty
                def DRAFT_DELETED(cls):
                    return cls("draft_deleted")
                
                @schemas.classproperty
                def PUBLISHED_DELETED(cls):
                    return cls("published_deleted")
            
            
            class created(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'created':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class modified(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'modified':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            deleted = schemas.BoolSchema
            
            
            class soft_deleted(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'soft_deleted':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            station = schemas.IntSchema
            
            
            class station_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'station_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class station_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'station_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            hourly_wage = schemas.NumberSchema
            late_minuets = schemas.IntSchema
        
            @staticmethod
            def breaks() -> typing.Type['ShiftsCreateNewShiftResponseDataBreaks']:
                return ShiftsCreateNewShiftResponseDataBreaks
            __annotations__ = {
                "id": id,
                "user_id": user_id,
                "start": start,
                "end": end,
                "close": close,
                "business_decline": business_decline,
                "department_id": department_id,
                "location_id": location_id,
                "role_id": role_id,
                "notes": notes,
                "draft": draft,
                "notified": notified,
                "open": open,
                "unassigned": unassigned,
                "unassigned_skill_level": unassigned_skill_level,
                "open_offer_type": open_offer_type,
                "attendance_status": attendance_status,
                "publish_status": publish_status,
                "created": created,
                "modified": modified,
                "deleted": deleted,
                "soft_deleted": soft_deleted,
                "station": station,
                "station_name": station_name,
                "station_id": station_id,
                "hourly_wage": hourly_wage,
                "late_minuets": late_minuets,
                "breaks": breaks,
            }
    
    notes: MetaOapg.properties.notes
    unassigned: MetaOapg.properties.unassigned
    location_id: MetaOapg.properties.location_id
    role_id: MetaOapg.properties.role_id
    draft: MetaOapg.properties.draft
    station: MetaOapg.properties.station
    modified: MetaOapg.properties.modified
    end: MetaOapg.properties.end
    id: MetaOapg.properties.id
    attendance_status: MetaOapg.properties.attendance_status
    close: MetaOapg.properties.close
    publish_status: MetaOapg.properties.publish_status
    station_name: MetaOapg.properties.station_name
    open_offer_type: MetaOapg.properties.open_offer_type
    department_id: MetaOapg.properties.department_id
    created: MetaOapg.properties.created
    notified: MetaOapg.properties.notified
    station_id: MetaOapg.properties.station_id
    unassigned_skill_level: MetaOapg.properties.unassigned_skill_level
    start: MetaOapg.properties.start
    late_minutes: schemas.AnyTypeSchema
    business_decline: MetaOapg.properties.business_decline
    soft_deleted: MetaOapg.properties.soft_deleted
    deleted: MetaOapg.properties.deleted
    user_id: MetaOapg.properties.user_id
    open: MetaOapg.properties.open
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["close"]) -> MetaOapg.properties.close: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["business_decline"]) -> MetaOapg.properties.business_decline: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notified"]) -> MetaOapg.properties.notified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["open"]) -> MetaOapg.properties.open: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unassigned"]) -> MetaOapg.properties.unassigned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unassigned_skill_level"]) -> MetaOapg.properties.unassigned_skill_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["open_offer_type"]) -> MetaOapg.properties.open_offer_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendance_status"]) -> MetaOapg.properties.attendance_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_status"]) -> MetaOapg.properties.publish_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["soft_deleted"]) -> MetaOapg.properties.soft_deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["station"]) -> MetaOapg.properties.station: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["station_name"]) -> MetaOapg.properties.station_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["station_id"]) -> MetaOapg.properties.station_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourly_wage"]) -> MetaOapg.properties.hourly_wage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["late_minuets"]) -> MetaOapg.properties.late_minuets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breaks"]) -> 'ShiftsCreateNewShiftResponseDataBreaks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "start", "end", "close", "business_decline", "department_id", "location_id", "role_id", "notes", "draft", "notified", "open", "unassigned", "unassigned_skill_level", "open_offer_type", "attendance_status", "publish_status", "created", "modified", "deleted", "soft_deleted", "station", "station_name", "station_id", "hourly_wage", "late_minuets", "breaks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["close"]) -> MetaOapg.properties.close: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["business_decline"]) -> MetaOapg.properties.business_decline: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notified"]) -> MetaOapg.properties.notified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["open"]) -> MetaOapg.properties.open: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unassigned"]) -> MetaOapg.properties.unassigned: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unassigned_skill_level"]) -> MetaOapg.properties.unassigned_skill_level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["open_offer_type"]) -> MetaOapg.properties.open_offer_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendance_status"]) -> MetaOapg.properties.attendance_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_status"]) -> MetaOapg.properties.publish_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified"]) -> MetaOapg.properties.modified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["soft_deleted"]) -> MetaOapg.properties.soft_deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["station"]) -> MetaOapg.properties.station: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["station_name"]) -> MetaOapg.properties.station_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["station_id"]) -> MetaOapg.properties.station_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourly_wage"]) -> typing.Union[MetaOapg.properties.hourly_wage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["late_minuets"]) -> typing.Union[MetaOapg.properties.late_minuets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breaks"]) -> typing.Union['ShiftsCreateNewShiftResponseDataBreaks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "user_id", "start", "end", "close", "business_decline", "department_id", "location_id", "role_id", "notes", "draft", "notified", "open", "unassigned", "unassigned_skill_level", "open_offer_type", "attendance_status", "publish_status", "created", "modified", "deleted", "soft_deleted", "station", "station_name", "station_id", "hourly_wage", "late_minuets", "breaks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        notes: typing.Union[MetaOapg.properties.notes, str, ],
        unassigned: typing.Union[MetaOapg.properties.unassigned, bool, ],
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
        role_id: typing.Union[MetaOapg.properties.role_id, None, decimal.Decimal, int, ],
        draft: typing.Union[MetaOapg.properties.draft, bool, ],
        station: typing.Union[MetaOapg.properties.station, decimal.Decimal, int, ],
        modified: typing.Union[MetaOapg.properties.modified, None, str, datetime, ],
        end: typing.Union[MetaOapg.properties.end, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        attendance_status: typing.Union[MetaOapg.properties.attendance_status, str, ],
        close: typing.Union[MetaOapg.properties.close, bool, ],
        publish_status: typing.Union[MetaOapg.properties.publish_status, str, ],
        station_name: typing.Union[MetaOapg.properties.station_name, None, str, ],
        open_offer_type: typing.Union[MetaOapg.properties.open_offer_type, None, str, ],
        department_id: typing.Union[MetaOapg.properties.department_id, None, decimal.Decimal, int, ],
        created: typing.Union[MetaOapg.properties.created, None, str, datetime, ],
        notified: typing.Union[MetaOapg.properties.notified, bool, ],
        station_id: typing.Union[MetaOapg.properties.station_id, None, decimal.Decimal, int, ],
        unassigned_skill_level: typing.Union[MetaOapg.properties.unassigned_skill_level, decimal.Decimal, int, ],
        start: typing.Union[MetaOapg.properties.start, str, datetime, ],
        late_minutes: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        business_decline: typing.Union[MetaOapg.properties.business_decline, bool, ],
        soft_deleted: typing.Union[MetaOapg.properties.soft_deleted, None, str, ],
        deleted: typing.Union[MetaOapg.properties.deleted, bool, ],
        user_id: typing.Union[MetaOapg.properties.user_id, None, decimal.Decimal, int, ],
        open: typing.Union[MetaOapg.properties.open, bool, ],
        hourly_wage: typing.Union[MetaOapg.properties.hourly_wage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        late_minuets: typing.Union[MetaOapg.properties.late_minuets, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        breaks: typing.Union['ShiftsCreateNewShiftResponseDataBreaks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShiftsCreateNewShiftResponseData':
        return super().__new__(
            cls,
            *args,
            notes=notes,
            unassigned=unassigned,
            location_id=location_id,
            role_id=role_id,
            draft=draft,
            station=station,
            modified=modified,
            end=end,
            id=id,
            attendance_status=attendance_status,
            close=close,
            publish_status=publish_status,
            station_name=station_name,
            open_offer_type=open_offer_type,
            department_id=department_id,
            created=created,
            notified=notified,
            station_id=station_id,
            unassigned_skill_level=unassigned_skill_level,
            start=start,
            late_minutes=late_minutes,
            business_decline=business_decline,
            soft_deleted=soft_deleted,
            deleted=deleted,
            user_id=user_id,
            open=open,
            hourly_wage=hourly_wage,
            late_minuets=late_minuets,
            breaks=breaks,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.shifts_create_new_shift_response_data_breaks import ShiftsCreateNewShiftResponseDataBreaks
