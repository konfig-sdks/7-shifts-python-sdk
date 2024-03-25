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


class TaskManagementCreateTaskListTemplateResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "activated_at",
            "recurrence",
            "assignments",
            "company_id",
            "created",
            "task_templates",
            "description",
            "id",
            "title",
            "uuid",
            "status",
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
            id = schemas.IntSchema
            company_id = schemas.IntSchema
            uuid = schemas.StrSchema
            
            
            class status(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1
                    inclusive_minimum = 0
            
            
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
            
            
            class activated_at(
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
                ) -> 'activated_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def task_templates() -> typing.Type['TaskManagementCreateTaskListTemplateResponseDataTaskTemplates']:
                return TaskManagementCreateTaskListTemplateResponseDataTaskTemplates
        
            @staticmethod
            def assignments() -> typing.Type['TaskManagementCreateTaskListTemplateResponseDataAssignments']:
                return TaskManagementCreateTaskListTemplateResponseDataAssignments
            recurrence = schemas.StrSchema
            
            
            class due(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'^\d{4}-\d{2}-\d{2}$',
                            }]
                    
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
                ) -> 'due':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class time_frame(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "start",
                                "end",
                            }
                            
                            class properties:
                                
                                
                                class start(
                                    schemas.StrBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneStrMixin
                                ):
                                
                                
                                    class MetaOapg:
                                        regex=[{
                                            'pattern': r'^\d{2}:\d{2}:\d{2}$',
                                        }]
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[None, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'start':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                        )
                                
                                
                                class end(
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        regex=[{
                                            'pattern': r'^\d{2}:\d{2}:\d{2}$',
                                        }]
                                __annotations__ = {
                                    "start": start,
                                    "end": end,
                                }
                        
                        start: MetaOapg.properties.start
                        end: MetaOapg.properties.end
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["start", "end", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start", "end", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            start: typing.Union[MetaOapg.properties.start, None, str, ],
                            end: typing.Union[MetaOapg.properties.end, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'any_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                start=start,
                                end=end,
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
                ) -> 'time_frame':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "title": title,
                "description": description,
                "id": id,
                "company_id": company_id,
                "uuid": uuid,
                "status": status,
                "created": created,
                "activated_at": activated_at,
                "task_templates": task_templates,
                "assignments": assignments,
                "recurrence": recurrence,
                "due": due,
                "time_frame": time_frame,
            }
    
    activated_at: MetaOapg.properties.activated_at
    recurrence: MetaOapg.properties.recurrence
    assignments: 'TaskManagementCreateTaskListTemplateResponseDataAssignments'
    company_id: MetaOapg.properties.company_id
    created: MetaOapg.properties.created
    task_templates: 'TaskManagementCreateTaskListTemplateResponseDataTaskTemplates'
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    uuid: MetaOapg.properties.uuid
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activated_at"]) -> MetaOapg.properties.activated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["task_templates"]) -> 'TaskManagementCreateTaskListTemplateResponseDataTaskTemplates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignments"]) -> 'TaskManagementCreateTaskListTemplateResponseDataAssignments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurrence"]) -> MetaOapg.properties.recurrence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due"]) -> MetaOapg.properties.due: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_frame"]) -> MetaOapg.properties.time_frame: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "id", "company_id", "uuid", "status", "created", "activated_at", "task_templates", "assignments", "recurrence", "due", "time_frame", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activated_at"]) -> MetaOapg.properties.activated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["task_templates"]) -> 'TaskManagementCreateTaskListTemplateResponseDataTaskTemplates': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignments"]) -> 'TaskManagementCreateTaskListTemplateResponseDataAssignments': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurrence"]) -> MetaOapg.properties.recurrence: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due"]) -> typing.Union[MetaOapg.properties.due, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_frame"]) -> typing.Union[MetaOapg.properties.time_frame, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "id", "company_id", "uuid", "status", "created", "activated_at", "task_templates", "assignments", "recurrence", "due", "time_frame", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        activated_at: typing.Union[MetaOapg.properties.activated_at, None, str, datetime, ],
        recurrence: typing.Union[MetaOapg.properties.recurrence, str, ],
        assignments: 'TaskManagementCreateTaskListTemplateResponseDataAssignments',
        company_id: typing.Union[MetaOapg.properties.company_id, decimal.Decimal, int, ],
        created: typing.Union[MetaOapg.properties.created, None, str, datetime, ],
        task_templates: 'TaskManagementCreateTaskListTemplateResponseDataTaskTemplates',
        description: typing.Union[MetaOapg.properties.description, None, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, ],
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, ],
        due: typing.Union[MetaOapg.properties.due, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        time_frame: typing.Union[MetaOapg.properties.time_frame, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskManagementCreateTaskListTemplateResponseData':
        return super().__new__(
            cls,
            *args,
            activated_at=activated_at,
            recurrence=recurrence,
            assignments=assignments,
            company_id=company_id,
            created=created,
            task_templates=task_templates,
            description=description,
            id=id,
            title=title,
            uuid=uuid,
            status=status,
            due=due,
            time_frame=time_frame,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.task_management_create_task_list_template_response_data_assignments import TaskManagementCreateTaskListTemplateResponseDataAssignments
from 7_shifts_python_sdk.model.task_management_create_task_list_template_response_data_task_templates import TaskManagementCreateTaskListTemplateResponseDataTaskTemplates