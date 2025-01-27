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


class TaskManagementCreateTaskListTemplateResponseDataTaskTemplatesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "description",
            "sort",
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            
            
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
            sort = schemas.IntSchema
            uuid = schemas.StrSchema
            created = schemas.DateTimeSchema
            
            
            class task_completion(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "unit",
                                "primitive_type",
                                "type",
                            }
                            
                            class properties:
                                
                                
                                class type(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "NUMBER": "NUMBER",
                                            "TEMPERATURE": "TEMPERATURE",
                                            "PHOTO": "PHOTO",
                                            "STRING": "STRING",
                                            "WEIGHT": "WEIGHT",
                                            "CHECKMARK": "CHECKMARK",
                                        }
                                    
                                    @schemas.classproperty
                                    def NUMBER(cls):
                                        return cls("NUMBER")
                                    
                                    @schemas.classproperty
                                    def TEMPERATURE(cls):
                                        return cls("TEMPERATURE")
                                    
                                    @schemas.classproperty
                                    def PHOTO(cls):
                                        return cls("PHOTO")
                                    
                                    @schemas.classproperty
                                    def STRING(cls):
                                        return cls("STRING")
                                    
                                    @schemas.classproperty
                                    def WEIGHT(cls):
                                        return cls("WEIGHT")
                                    
                                    @schemas.classproperty
                                    def CHECKMARK(cls):
                                        return cls("CHECKMARK")
                                
                                
                                class primitive_type(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "INTEGER": "INTEGER",
                                            "DECIMAL": "DECIMAL",
                                            "FILE": "FILE",
                                            "STRING": "STRING",
                                            "BOOLEAN": "BOOLEAN",
                                        }
                                    
                                    @schemas.classproperty
                                    def INTEGER(cls):
                                        return cls("INTEGER")
                                    
                                    @schemas.classproperty
                                    def DECIMAL(cls):
                                        return cls("DECIMAL")
                                    
                                    @schemas.classproperty
                                    def FILE(cls):
                                        return cls("FILE")
                                    
                                    @schemas.classproperty
                                    def STRING(cls):
                                        return cls("STRING")
                                    
                                    @schemas.classproperty
                                    def BOOLEAN(cls):
                                        return cls("BOOLEAN")
                                
                                
                                class unit(
                                    schemas.EnumBase,
                                    schemas.StrBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneStrMixin
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "C": "C",
                                            "F": "F",
                                            "KG": "KG",
                                        }
                                    
                                    @schemas.classproperty
                                    def C(cls):
                                        return cls("C")
                                    
                                    @schemas.classproperty
                                    def F(cls):
                                        return cls("F")
                                    
                                    @schemas.classproperty
                                    def KG(cls):
                                        return cls("KG")
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[None, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'unit':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                        )
                                __annotations__ = {
                                    "type": type,
                                    "primitive_type": primitive_type,
                                    "unit": unit,
                                }
                        
                        unit: MetaOapg.properties.unit
                        primitive_type: MetaOapg.properties.primitive_type
                        type: MetaOapg.properties.type
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["primitive_type"]) -> MetaOapg.properties.primitive_type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "primitive_type", "unit", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["primitive_type"]) -> MetaOapg.properties.primitive_type: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["unit"]) -> MetaOapg.properties.unit: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "primitive_type", "unit", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            unit: typing.Union[MetaOapg.properties.unit, None, str, ],
                            primitive_type: typing.Union[MetaOapg.properties.primitive_type, str, ],
                            type: typing.Union[MetaOapg.properties.type, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'any_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                unit=unit,
                                primitive_type=primitive_type,
                                type=type,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'task_completion':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "title": title,
                "description": description,
                "sort": sort,
                "uuid": uuid,
                "created": created,
                "task_completion": task_completion,
            }
    
    description: MetaOapg.properties.description
    sort: MetaOapg.properties.sort
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task_completion"]) -> MetaOapg.properties.task_completion: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "sort", "uuid", "created", "task_completion", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task_completion"]) -> typing.Union[MetaOapg.properties.task_completion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "sort", "uuid", "created", "task_completion", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, None, str, ],
        sort: typing.Union[MetaOapg.properties.sort, decimal.Decimal, int, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        task_completion: typing.Union[MetaOapg.properties.task_completion, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskManagementCreateTaskListTemplateResponseDataTaskTemplatesItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            sort=sort,
            title=title,
            uuid=uuid,
            created=created,
            task_completion=task_completion,
            _configuration=_configuration,
            **kwargs,
        )
