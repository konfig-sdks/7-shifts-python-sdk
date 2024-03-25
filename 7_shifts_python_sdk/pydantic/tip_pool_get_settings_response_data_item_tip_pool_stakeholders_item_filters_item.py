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


class TipPoolGetSettingsResponseDataItemTipPoolStakeholdersItemFiltersItem(BaseModel):
    # The type of stakeholder filter - whether it is from a revenue center, dining option, or sales category
    filter_type: Literal["DINING_OPTION", "REVENUE_CENTER", "SALES_CATEGORY"] = Field(alias='filter_type')

    # The ID that we will represent the filter with
    filter_value: typing.Optional[str] = Field(alias='filter_value')

    # The display name that the end user will see
    filter_name: str = Field(alias='filter_name')

    # Tip pool stakeholder filter UUID
    uuid: typing.Optional[typing.Optional[str]] = Field(None, alias='uuid')

    # Tip pool stakeholder UUID
    tip_pool_stakeholder_uuid: typing.Optional[typing.Optional[str]] = Field(None, alias='tip_pool_stakeholder_uuid')

    # Tip pool settings UUID
    tip_pool_settings_uuid: typing.Optional[typing.Optional[str]] = Field(None, alias='tip_pool_settings_uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )