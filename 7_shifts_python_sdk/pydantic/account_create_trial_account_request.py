# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class AccountCreateTrialAccountRequest(BaseModel):
    # The user's email
    email: str = Field(alias='email')

    # The user's first name
    firstname: str = Field(alias='firstname')

    # The user's last name
    lastname: str = Field(alias='lastname')

    # The company's name
    company_name: str = Field(alias='company_name')

    # The company's country
    country: Literal["CA", "US"] = Field(alias='country')

    # The UTM source
    utm_source: str = Field(alias='utm_source')

    # The user's mobile phone
    mobile_phone: typing.Optional[str] = Field(None, alias='mobile_phone')

    # The UTM campaign
    utm_campaign: typing.Optional[str] = Field(None, alias='utm_campaign')

    # The UTM content
    utm_content: typing.Optional[str] = Field(None, alias='utm_content')

    # The UTM medium
    utm_medium: typing.Optional[str] = Field(None, alias='utm_medium')

    # The UTM term
    utm_term: typing.Optional[str] = Field(None, alias='utm_term')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
