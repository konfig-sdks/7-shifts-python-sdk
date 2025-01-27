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


class ScheduleEventsListEventsResponseData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class all_of_0(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "event_type",
                            "id",
                        }
                        
                        class properties:
                            id = schemas.IntSchema
                            
                            
                            class event_type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "general": "GENERAL",
                                        "birthday": "BIRTHDAY",
                                        "work_anniversary": "WORK_ANNIVERSARY",
                                    }
                                
                                @schemas.classproperty
                                def GENERAL(cls):
                                    return cls("general")
                                
                                @schemas.classproperty
                                def BIRTHDAY(cls):
                                    return cls("birthday")
                                
                                @schemas.classproperty
                                def WORK_ANNIVERSARY(cls):
                                    return cls("work_anniversary")
                            __annotations__ = {
                                "id": id,
                                "event_type": event_type,
                            }
                    
                    event_type: MetaOapg.properties.event_type
                    id: MetaOapg.properties.id
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> MetaOapg.properties.event_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "event_type", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> MetaOapg.properties.event_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "event_type", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        event_type: typing.Union[MetaOapg.properties.event_type, str, ],
                        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            event_type=event_type,
                            id=id,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class all_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "end_date",
                            "start_time",
                            "location_ids",
                            "end_time",
                            "title",
                            "is_multi_day",
                            "start_date",
                        }
                        
                        class properties:
                            
                            
                            class title(
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    max_length = 100
                            
                            
                            class description(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'description':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                    )
                            
                            
                            class location_ids(
                                schemas.ListSchema
                            ):
                            
                            
                                class MetaOapg:
                                    items = schemas.IntSchema
                            
                                def __new__(
                                    cls,
                                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'location_ids':
                                    return super().__new__(
                                        cls,
                                        arg,
                                        _configuration=_configuration,
                                    )
                            
                                def __getitem__(self, i: int) -> MetaOapg.items:
                                    return super().__getitem__(i)
                            
                            
                            class start(
                                schemas.ListSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    
                                    class items(
                                        schemas.DictSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            required = {
                                                "date_time",
                                                "location_id",
                                            }
                                            
                                            class properties:
                                                location_id = schemas.IntSchema
                                                date_time = schemas.StrSchema
                                                __annotations__ = {
                                                    "location_id": location_id,
                                                    "date_time": date_time,
                                                }
                                        
                                        date_time: MetaOapg.properties.date_time
                                        location_id: MetaOapg.properties.location_id
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["date_time"]) -> MetaOapg.properties.date_time: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["location_id", "date_time", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["date_time"]) -> MetaOapg.properties.date_time: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["location_id", "date_time", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *args: typing.Union[dict, frozendict.frozendict, ],
                                            date_time: typing.Union[MetaOapg.properties.date_time, str, ],
                                            location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> 'items':
                                            return super().__new__(
                                                cls,
                                                *args,
                                                date_time=date_time,
                                                location_id=location_id,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                            
                                def __new__(
                                    cls,
                                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'start':
                                    return super().__new__(
                                        cls,
                                        arg,
                                        _configuration=_configuration,
                                    )
                            
                                def __getitem__(self, i: int) -> MetaOapg.items:
                                    return super().__getitem__(i)
                            
                            
                            class start_date(
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    regex=[{
                                        'pattern': r'^\d{4}-\d{2}-\d{2}$',
                                    }]
                            start_time = schemas.StrSchema
                            
                            
                            class end(
                                schemas.ListSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    
                                    class items(
                                        schemas.DictSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            required = {
                                                "date_time",
                                                "location_id",
                                            }
                                            
                                            class properties:
                                                location_id = schemas.IntSchema
                                                date_time = schemas.StrSchema
                                                __annotations__ = {
                                                    "location_id": location_id,
                                                    "date_time": date_time,
                                                }
                                        
                                        date_time: MetaOapg.properties.date_time
                                        location_id: MetaOapg.properties.location_id
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["date_time"]) -> MetaOapg.properties.date_time: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["location_id", "date_time", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["date_time"]) -> MetaOapg.properties.date_time: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["location_id", "date_time", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *args: typing.Union[dict, frozendict.frozendict, ],
                                            date_time: typing.Union[MetaOapg.properties.date_time, str, ],
                                            location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, ],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> 'items':
                                            return super().__new__(
                                                cls,
                                                *args,
                                                date_time=date_time,
                                                location_id=location_id,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                            
                                def __new__(
                                    cls,
                                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'end':
                                    return super().__new__(
                                        cls,
                                        arg,
                                        _configuration=_configuration,
                                    )
                            
                                def __getitem__(self, i: int) -> MetaOapg.items:
                                    return super().__getitem__(i)
                            
                            
                            class end_date(
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    regex=[{
                                        'pattern': r'^\d{4}-\d{2}-\d{2}$',
                                    }]
                            end_time = schemas.StrSchema
                            
                            
                            class color(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'color':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                    )
                            is_multi_day = schemas.BoolSchema
                            
                            
                            class recurrence(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'recurrence':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
                                    )
                            __annotations__ = {
                                "title": title,
                                "description": description,
                                "location_ids": location_ids,
                                "start": start,
                                "start_date": start_date,
                                "start_time": start_time,
                                "end": end,
                                "end_date": end_date,
                                "end_time": end_time,
                                "color": color,
                                "is_multi_day": is_multi_day,
                                "recurrence": recurrence,
                            }
                    
                    end_date: MetaOapg.properties.end_date
                    start_time: MetaOapg.properties.start_time
                    location_ids: MetaOapg.properties.location_ids
                    end_time: MetaOapg.properties.end_time
                    title: MetaOapg.properties.title
                    is_multi_day: MetaOapg.properties.is_multi_day
                    start_date: MetaOapg.properties.start_date
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["location_ids"]) -> MetaOapg.properties.location_ids: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["is_multi_day"]) -> MetaOapg.properties.is_multi_day: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["recurrence"]) -> MetaOapg.properties.recurrence: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "location_ids", "start", "start_date", "start_time", "end", "end_date", "end_time", "color", "is_multi_day", "recurrence", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["location_ids"]) -> MetaOapg.properties.location_ids: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["is_multi_day"]) -> MetaOapg.properties.is_multi_day: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["recurrence"]) -> typing.Union[MetaOapg.properties.recurrence, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "location_ids", "start", "start_date", "start_time", "end", "end_date", "end_time", "color", "is_multi_day", "recurrence", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        end_date: typing.Union[MetaOapg.properties.end_date, str, ],
                        start_time: typing.Union[MetaOapg.properties.start_time, str, ],
                        location_ids: typing.Union[MetaOapg.properties.location_ids, list, tuple, ],
                        end_time: typing.Union[MetaOapg.properties.end_time, str, ],
                        title: typing.Union[MetaOapg.properties.title, str, ],
                        is_multi_day: typing.Union[MetaOapg.properties.is_multi_day, bool, ],
                        start_date: typing.Union[MetaOapg.properties.start_date, str, ],
                        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
                        start: typing.Union[MetaOapg.properties.start, list, tuple, schemas.Unset] = schemas.unset,
                        end: typing.Union[MetaOapg.properties.end, list, tuple, schemas.Unset] = schemas.unset,
                        color: typing.Union[MetaOapg.properties.color, None, str, schemas.Unset] = schemas.unset,
                        recurrence: typing.Union[MetaOapg.properties.recurrence, None, str, schemas.Unset] = schemas.unset,
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            end_date=end_date,
                            start_time=start_time,
                            location_ids=location_ids,
                            end_time=end_time,
                            title=title,
                            is_multi_day=is_multi_day,
                            start_date=start_date,
                            description=description,
                            start=start,
                            end=end,
                            color=color,
                            recurrence=recurrence,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                @classmethod
                @functools.lru_cache()
                def all_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.all_of_0,
                        cls.all_of_1,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ScheduleEventsListEventsResponseData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
