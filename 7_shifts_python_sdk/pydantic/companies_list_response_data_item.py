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

from 7_shifts_python_sdk.pydantic.companies_list_response_data_item_meta import CompaniesListResponseDataItemMeta

class CompaniesListResponseDataItem(BaseModel):
    id: typing.Union[int, float] = Field(alias='id')

    name: str = Field(alias='name')

    country: str = Field(alias='country')

    photo: typing.Optional[str] = Field(alias='photo')

    plan_id: str = Field(alias='plan_id')

    created: datetime = Field(alias='created')

    modified: typing.Optional[datetime] = Field(alias='modified')

    expires: typing.Optional[datetime] = Field(alias='expires')

    days_to_expire: typing.Optional[typing.Union[int, float]] = Field(alias='days_to_expire')

    converted: typing.Optional[datetime] = Field(alias='converted')

    pos: typing.Optional[str] = Field(alias='pos')

    status: Literal["active", "trial", "cancelled", "delinquent", "expired", "unknown"] = Field(alias='status')

    start_week_on: typing.Optional[typing.Union[int, float]] = Field(alias='start_week_on')

    meta: typing.Optional[CompaniesListResponseDataItemMeta] = Field(None, alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
