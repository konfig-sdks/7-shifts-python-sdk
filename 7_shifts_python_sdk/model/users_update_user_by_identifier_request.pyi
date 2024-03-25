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


class UsersUpdateUserByIdentifierRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class first_name(
                schemas.StrSchema
            ):
                pass
            
            
            class last_name(
                schemas.StrSchema
            ):
                pass
            
            
            class preferred_first_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'preferred_first_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class preferred_last_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'preferred_last_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class email(
                schemas.StrSchema
            ):
                pass
            
            
            class mobile_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mobile_number':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class home_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'home_number':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class address(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class postal_zip(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postal_zip':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class city(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'city':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class prov_state(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'prov_state':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class notes(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class hire_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hire_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMPLOYEE(cls):
                    return cls("employee")
                
                @schemas.classproperty
                def ASST_MANAGER(cls):
                    return cls("asst_manager")
                
                @schemas.classproperty
                def MANAGER(cls):
                    return cls("manager")
            
            
            class employee_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'employee_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class punch_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'punch_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class birth_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'birth_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class language(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EN(cls):
                    return cls("en")
                
                @schemas.classproperty
                def ES(cls):
                    return cls("es")
                
                @schemas.classproperty
                def FR(cls):
                    return cls("fr")
            appear_as_employee = schemas.BoolSchema
            subscribe_to_updates = schemas.BoolSchema
            max_weekly_hours = schemas.IntSchema
            active = schemas.BoolSchema
            
            
            class pronouns(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pronouns':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class permissions_template_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'permissions_template_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "first_name": first_name,
                "last_name": last_name,
                "preferred_first_name": preferred_first_name,
                "preferred_last_name": preferred_last_name,
                "email": email,
                "mobile_number": mobile_number,
                "home_number": home_number,
                "address": address,
                "postal_zip": postal_zip,
                "city": city,
                "prov_state": prov_state,
                "notes": notes,
                "hire_date": hire_date,
                "type": type,
                "employee_id": employee_id,
                "punch_id": punch_id,
                "birth_date": birth_date,
                "language": language,
                "appear_as_employee": appear_as_employee,
                "subscribe_to_updates": subscribe_to_updates,
                "max_weekly_hours": max_weekly_hours,
                "active": active,
                "pronouns": pronouns,
                "permissions_template_id": permissions_template_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferred_first_name"]) -> MetaOapg.properties.preferred_first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferred_last_name"]) -> MetaOapg.properties.preferred_last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobile_number"]) -> MetaOapg.properties.mobile_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["home_number"]) -> MetaOapg.properties.home_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postal_zip"]) -> MetaOapg.properties.postal_zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prov_state"]) -> MetaOapg.properties.prov_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hire_date"]) -> MetaOapg.properties.hire_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_id"]) -> MetaOapg.properties.employee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["punch_id"]) -> MetaOapg.properties.punch_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birth_date"]) -> MetaOapg.properties.birth_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appear_as_employee"]) -> MetaOapg.properties.appear_as_employee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscribe_to_updates"]) -> MetaOapg.properties.subscribe_to_updates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_weekly_hours"]) -> MetaOapg.properties.max_weekly_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pronouns"]) -> MetaOapg.properties.pronouns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions_template_id"]) -> MetaOapg.properties.permissions_template_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "preferred_first_name", "preferred_last_name", "email", "mobile_number", "home_number", "address", "postal_zip", "city", "prov_state", "notes", "hire_date", "type", "employee_id", "punch_id", "birth_date", "language", "appear_as_employee", "subscribe_to_updates", "max_weekly_hours", "active", "pronouns", "permissions_template_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferred_first_name"]) -> typing.Union[MetaOapg.properties.preferred_first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferred_last_name"]) -> typing.Union[MetaOapg.properties.preferred_last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobile_number"]) -> typing.Union[MetaOapg.properties.mobile_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["home_number"]) -> typing.Union[MetaOapg.properties.home_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postal_zip"]) -> typing.Union[MetaOapg.properties.postal_zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prov_state"]) -> typing.Union[MetaOapg.properties.prov_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hire_date"]) -> typing.Union[MetaOapg.properties.hire_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_id"]) -> typing.Union[MetaOapg.properties.employee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["punch_id"]) -> typing.Union[MetaOapg.properties.punch_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birth_date"]) -> typing.Union[MetaOapg.properties.birth_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appear_as_employee"]) -> typing.Union[MetaOapg.properties.appear_as_employee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscribe_to_updates"]) -> typing.Union[MetaOapg.properties.subscribe_to_updates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_weekly_hours"]) -> typing.Union[MetaOapg.properties.max_weekly_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pronouns"]) -> typing.Union[MetaOapg.properties.pronouns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions_template_id"]) -> typing.Union[MetaOapg.properties.permissions_template_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "preferred_first_name", "preferred_last_name", "email", "mobile_number", "home_number", "address", "postal_zip", "city", "prov_state", "notes", "hire_date", "type", "employee_id", "punch_id", "birth_date", "language", "appear_as_employee", "subscribe_to_updates", "max_weekly_hours", "active", "pronouns", "permissions_template_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        preferred_first_name: typing.Union[MetaOapg.properties.preferred_first_name, None, str, schemas.Unset] = schemas.unset,
        preferred_last_name: typing.Union[MetaOapg.properties.preferred_last_name, None, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        mobile_number: typing.Union[MetaOapg.properties.mobile_number, None, str, schemas.Unset] = schemas.unset,
        home_number: typing.Union[MetaOapg.properties.home_number, None, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, None, str, schemas.Unset] = schemas.unset,
        postal_zip: typing.Union[MetaOapg.properties.postal_zip, None, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, None, str, schemas.Unset] = schemas.unset,
        prov_state: typing.Union[MetaOapg.properties.prov_state, None, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        hire_date: typing.Union[MetaOapg.properties.hire_date, None, str, date, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        employee_id: typing.Union[MetaOapg.properties.employee_id, None, str, schemas.Unset] = schemas.unset,
        punch_id: typing.Union[MetaOapg.properties.punch_id, None, str, schemas.Unset] = schemas.unset,
        birth_date: typing.Union[MetaOapg.properties.birth_date, None, str, date, schemas.Unset] = schemas.unset,
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        appear_as_employee: typing.Union[MetaOapg.properties.appear_as_employee, bool, schemas.Unset] = schemas.unset,
        subscribe_to_updates: typing.Union[MetaOapg.properties.subscribe_to_updates, bool, schemas.Unset] = schemas.unset,
        max_weekly_hours: typing.Union[MetaOapg.properties.max_weekly_hours, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        pronouns: typing.Union[MetaOapg.properties.pronouns, None, str, schemas.Unset] = schemas.unset,
        permissions_template_id: typing.Union[MetaOapg.properties.permissions_template_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersUpdateUserByIdentifierRequest':
        return super().__new__(
            cls,
            *args,
            first_name=first_name,
            last_name=last_name,
            preferred_first_name=preferred_first_name,
            preferred_last_name=preferred_last_name,
            email=email,
            mobile_number=mobile_number,
            home_number=home_number,
            address=address,
            postal_zip=postal_zip,
            city=city,
            prov_state=prov_state,
            notes=notes,
            hire_date=hire_date,
            type=type,
            employee_id=employee_id,
            punch_id=punch_id,
            birth_date=birth_date,
            language=language,
            appear_as_employee=appear_as_employee,
            subscribe_to_updates=subscribe_to_updates,
            max_weekly_hours=max_weekly_hours,
            active=active,
            pronouns=pronouns,
            permissions_template_id=permissions_template_id,
            _configuration=_configuration,
            **kwargs,
        )
