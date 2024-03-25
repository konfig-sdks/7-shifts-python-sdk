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


class AccountCreateTrialAccountRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "country",
            "firstname",
            "company_name",
            "email",
            "lastname",
            "utm_source",
        }
        
        class properties:
            
            
            class email(
                schemas.StrSchema
            ):
                pass
            
            
            class firstname(
                schemas.StrSchema
            ):
                pass
            
            
            class lastname(
                schemas.StrSchema
            ):
                pass
            
            
            class company_name(
                schemas.StrSchema
            ):
                pass
            
            
            class country(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CA(cls):
                    return cls("CA")
                
                @schemas.classproperty
                def US(cls):
                    return cls("US")
            
            
            class utm_source(
                schemas.StrSchema
            ):
                pass
            
            
            class mobile_phone(
                schemas.StrSchema
            ):
                pass
            
            
            class utm_campaign(
                schemas.StrSchema
            ):
                pass
            
            
            class utm_content(
                schemas.StrSchema
            ):
                pass
            
            
            class utm_medium(
                schemas.StrSchema
            ):
                pass
            
            
            class utm_term(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "email": email,
                "firstname": firstname,
                "lastname": lastname,
                "company_name": company_name,
                "country": country,
                "utm_source": utm_source,
                "mobile_phone": mobile_phone,
                "utm_campaign": utm_campaign,
                "utm_content": utm_content,
                "utm_medium": utm_medium,
                "utm_term": utm_term,
            }
    
    country: MetaOapg.properties.country
    firstname: MetaOapg.properties.firstname
    company_name: MetaOapg.properties.company_name
    email: MetaOapg.properties.email
    lastname: MetaOapg.properties.lastname
    utm_source: MetaOapg.properties.utm_source
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstname"]) -> MetaOapg.properties.firstname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastname"]) -> MetaOapg.properties.lastname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_name"]) -> MetaOapg.properties.company_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utm_source"]) -> MetaOapg.properties.utm_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobile_phone"]) -> MetaOapg.properties.mobile_phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utm_campaign"]) -> MetaOapg.properties.utm_campaign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utm_content"]) -> MetaOapg.properties.utm_content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utm_medium"]) -> MetaOapg.properties.utm_medium: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["utm_term"]) -> MetaOapg.properties.utm_term: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "firstname", "lastname", "company_name", "country", "utm_source", "mobile_phone", "utm_campaign", "utm_content", "utm_medium", "utm_term", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstname"]) -> MetaOapg.properties.firstname: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastname"]) -> MetaOapg.properties.lastname: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_name"]) -> MetaOapg.properties.company_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utm_source"]) -> MetaOapg.properties.utm_source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobile_phone"]) -> typing.Union[MetaOapg.properties.mobile_phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utm_campaign"]) -> typing.Union[MetaOapg.properties.utm_campaign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utm_content"]) -> typing.Union[MetaOapg.properties.utm_content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utm_medium"]) -> typing.Union[MetaOapg.properties.utm_medium, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["utm_term"]) -> typing.Union[MetaOapg.properties.utm_term, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "firstname", "lastname", "company_name", "country", "utm_source", "mobile_phone", "utm_campaign", "utm_content", "utm_medium", "utm_term", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        firstname: typing.Union[MetaOapg.properties.firstname, str, ],
        company_name: typing.Union[MetaOapg.properties.company_name, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        lastname: typing.Union[MetaOapg.properties.lastname, str, ],
        utm_source: typing.Union[MetaOapg.properties.utm_source, str, ],
        mobile_phone: typing.Union[MetaOapg.properties.mobile_phone, str, schemas.Unset] = schemas.unset,
        utm_campaign: typing.Union[MetaOapg.properties.utm_campaign, str, schemas.Unset] = schemas.unset,
        utm_content: typing.Union[MetaOapg.properties.utm_content, str, schemas.Unset] = schemas.unset,
        utm_medium: typing.Union[MetaOapg.properties.utm_medium, str, schemas.Unset] = schemas.unset,
        utm_term: typing.Union[MetaOapg.properties.utm_term, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountCreateTrialAccountRequest':
        return super().__new__(
            cls,
            *args,
            country=country,
            firstname=firstname,
            company_name=company_name,
            email=email,
            lastname=lastname,
            utm_source=utm_source,
            mobile_phone=mobile_phone,
            utm_campaign=utm_campaign,
            utm_content=utm_content,
            utm_medium=utm_medium,
            utm_term=utm_term,
            _configuration=_configuration,
            **kwargs,
        )
