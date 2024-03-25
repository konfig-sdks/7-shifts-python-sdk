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


class ReportsGetWorkedHoursWagesResponseUsersItemTotal(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Hours and pay info for a shift or group of shifts
    """


    class MetaOapg:
        required = {
            "total_payment_tips",
            "overtime_hours",
            "holiday_pay",
            "tip_in",
            "total_tips",
            "regular_hours",
            "total_hours",
            "declared_tips",
            "holiday_hours",
            "credit_card_tips",
            "total_pay",
            "withheld_cc_amount",
            "auto_gratuity",
            "earned_tips",
            "regular_pay",
            "cash_tips",
            "compliance_exceptions_pay",
            "tip_out",
            "overtime_pay",
        }
        
        class properties:
            regular_hours = schemas.NumberSchema
            regular_pay = schemas.NumberSchema
            overtime_hours = schemas.NumberSchema
            overtime_pay = schemas.NumberSchema
            holiday_hours = schemas.NumberSchema
            holiday_pay = schemas.NumberSchema
            compliance_exceptions_pay = schemas.NumberSchema
            total_hours = schemas.NumberSchema
            total_pay = schemas.NumberSchema
            total_tips = schemas.NumberSchema
            cash_tips = schemas.NumberSchema
            credit_card_tips = schemas.NumberSchema
            total_payment_tips = schemas.NumberSchema
            declared_tips = schemas.NumberSchema
            auto_gratuity = schemas.NumberSchema
            withheld_cc_amount = schemas.NumberSchema
            tip_in = schemas.NumberSchema
            tip_out = schemas.NumberSchema
            earned_tips = schemas.NumberSchema
            premium_overtime_hours = schemas.NumberSchema
            non_premium_overtime_hours = schemas.NumberSchema
            premium_overtime_pay = schemas.NumberSchema
            non_premium_overtime_pay = schemas.NumberSchema
            pos_declared_tips = schemas.NumberSchema
            __annotations__ = {
                "regular_hours": regular_hours,
                "regular_pay": regular_pay,
                "overtime_hours": overtime_hours,
                "overtime_pay": overtime_pay,
                "holiday_hours": holiday_hours,
                "holiday_pay": holiday_pay,
                "compliance_exceptions_pay": compliance_exceptions_pay,
                "total_hours": total_hours,
                "total_pay": total_pay,
                "total_tips": total_tips,
                "cash_tips": cash_tips,
                "credit_card_tips": credit_card_tips,
                "total_payment_tips": total_payment_tips,
                "declared_tips": declared_tips,
                "auto_gratuity": auto_gratuity,
                "withheld_cc_amount": withheld_cc_amount,
                "tip_in": tip_in,
                "tip_out": tip_out,
                "earned_tips": earned_tips,
                "premium_overtime_hours": premium_overtime_hours,
                "non_premium_overtime_hours": non_premium_overtime_hours,
                "premium_overtime_pay": premium_overtime_pay,
                "non_premium_overtime_pay": non_premium_overtime_pay,
                "pos_declared_tips": pos_declared_tips,
            }
    
    total_payment_tips: MetaOapg.properties.total_payment_tips
    overtime_hours: MetaOapg.properties.overtime_hours
    holiday_pay: MetaOapg.properties.holiday_pay
    tip_in: MetaOapg.properties.tip_in
    total_tips: MetaOapg.properties.total_tips
    regular_hours: MetaOapg.properties.regular_hours
    total_hours: MetaOapg.properties.total_hours
    declared_tips: MetaOapg.properties.declared_tips
    holiday_hours: MetaOapg.properties.holiday_hours
    credit_card_tips: MetaOapg.properties.credit_card_tips
    total_pay: MetaOapg.properties.total_pay
    withheld_cc_amount: MetaOapg.properties.withheld_cc_amount
    auto_gratuity: MetaOapg.properties.auto_gratuity
    earned_tips: MetaOapg.properties.earned_tips
    regular_pay: MetaOapg.properties.regular_pay
    cash_tips: MetaOapg.properties.cash_tips
    compliance_exceptions_pay: MetaOapg.properties.compliance_exceptions_pay
    tip_out: MetaOapg.properties.tip_out
    overtime_pay: MetaOapg.properties.overtime_pay
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regular_hours"]) -> MetaOapg.properties.regular_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regular_pay"]) -> MetaOapg.properties.regular_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtime_hours"]) -> MetaOapg.properties.overtime_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtime_pay"]) -> MetaOapg.properties.overtime_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holiday_hours"]) -> MetaOapg.properties.holiday_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["holiday_pay"]) -> MetaOapg.properties.holiday_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compliance_exceptions_pay"]) -> MetaOapg.properties.compliance_exceptions_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_hours"]) -> MetaOapg.properties.total_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pay"]) -> MetaOapg.properties.total_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_tips"]) -> MetaOapg.properties.total_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cash_tips"]) -> MetaOapg.properties.cash_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credit_card_tips"]) -> MetaOapg.properties.credit_card_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_payment_tips"]) -> MetaOapg.properties.total_payment_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["declared_tips"]) -> MetaOapg.properties.declared_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_gratuity"]) -> MetaOapg.properties.auto_gratuity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withheld_cc_amount"]) -> MetaOapg.properties.withheld_cc_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_in"]) -> MetaOapg.properties.tip_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tip_out"]) -> MetaOapg.properties.tip_out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earned_tips"]) -> MetaOapg.properties.earned_tips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["premium_overtime_hours"]) -> MetaOapg.properties.premium_overtime_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["non_premium_overtime_hours"]) -> MetaOapg.properties.non_premium_overtime_hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["premium_overtime_pay"]) -> MetaOapg.properties.premium_overtime_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["non_premium_overtime_pay"]) -> MetaOapg.properties.non_premium_overtime_pay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pos_declared_tips"]) -> MetaOapg.properties.pos_declared_tips: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["regular_hours", "regular_pay", "overtime_hours", "overtime_pay", "holiday_hours", "holiday_pay", "compliance_exceptions_pay", "total_hours", "total_pay", "total_tips", "cash_tips", "credit_card_tips", "total_payment_tips", "declared_tips", "auto_gratuity", "withheld_cc_amount", "tip_in", "tip_out", "earned_tips", "premium_overtime_hours", "non_premium_overtime_hours", "premium_overtime_pay", "non_premium_overtime_pay", "pos_declared_tips", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regular_hours"]) -> MetaOapg.properties.regular_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regular_pay"]) -> MetaOapg.properties.regular_pay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtime_hours"]) -> MetaOapg.properties.overtime_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtime_pay"]) -> MetaOapg.properties.overtime_pay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holiday_hours"]) -> MetaOapg.properties.holiday_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["holiday_pay"]) -> MetaOapg.properties.holiday_pay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compliance_exceptions_pay"]) -> MetaOapg.properties.compliance_exceptions_pay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_hours"]) -> MetaOapg.properties.total_hours: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pay"]) -> MetaOapg.properties.total_pay: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_tips"]) -> MetaOapg.properties.total_tips: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cash_tips"]) -> MetaOapg.properties.cash_tips: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credit_card_tips"]) -> MetaOapg.properties.credit_card_tips: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_payment_tips"]) -> MetaOapg.properties.total_payment_tips: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["declared_tips"]) -> MetaOapg.properties.declared_tips: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_gratuity"]) -> MetaOapg.properties.auto_gratuity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withheld_cc_amount"]) -> MetaOapg.properties.withheld_cc_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_in"]) -> MetaOapg.properties.tip_in: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tip_out"]) -> MetaOapg.properties.tip_out: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earned_tips"]) -> MetaOapg.properties.earned_tips: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["premium_overtime_hours"]) -> typing.Union[MetaOapg.properties.premium_overtime_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["non_premium_overtime_hours"]) -> typing.Union[MetaOapg.properties.non_premium_overtime_hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["premium_overtime_pay"]) -> typing.Union[MetaOapg.properties.premium_overtime_pay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["non_premium_overtime_pay"]) -> typing.Union[MetaOapg.properties.non_premium_overtime_pay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pos_declared_tips"]) -> typing.Union[MetaOapg.properties.pos_declared_tips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["regular_hours", "regular_pay", "overtime_hours", "overtime_pay", "holiday_hours", "holiday_pay", "compliance_exceptions_pay", "total_hours", "total_pay", "total_tips", "cash_tips", "credit_card_tips", "total_payment_tips", "declared_tips", "auto_gratuity", "withheld_cc_amount", "tip_in", "tip_out", "earned_tips", "premium_overtime_hours", "non_premium_overtime_hours", "premium_overtime_pay", "non_premium_overtime_pay", "pos_declared_tips", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total_payment_tips: typing.Union[MetaOapg.properties.total_payment_tips, decimal.Decimal, int, float, ],
        overtime_hours: typing.Union[MetaOapg.properties.overtime_hours, decimal.Decimal, int, float, ],
        holiday_pay: typing.Union[MetaOapg.properties.holiday_pay, decimal.Decimal, int, float, ],
        tip_in: typing.Union[MetaOapg.properties.tip_in, decimal.Decimal, int, float, ],
        total_tips: typing.Union[MetaOapg.properties.total_tips, decimal.Decimal, int, float, ],
        regular_hours: typing.Union[MetaOapg.properties.regular_hours, decimal.Decimal, int, float, ],
        total_hours: typing.Union[MetaOapg.properties.total_hours, decimal.Decimal, int, float, ],
        declared_tips: typing.Union[MetaOapg.properties.declared_tips, decimal.Decimal, int, float, ],
        holiday_hours: typing.Union[MetaOapg.properties.holiday_hours, decimal.Decimal, int, float, ],
        credit_card_tips: typing.Union[MetaOapg.properties.credit_card_tips, decimal.Decimal, int, float, ],
        total_pay: typing.Union[MetaOapg.properties.total_pay, decimal.Decimal, int, float, ],
        withheld_cc_amount: typing.Union[MetaOapg.properties.withheld_cc_amount, decimal.Decimal, int, float, ],
        auto_gratuity: typing.Union[MetaOapg.properties.auto_gratuity, decimal.Decimal, int, float, ],
        earned_tips: typing.Union[MetaOapg.properties.earned_tips, decimal.Decimal, int, float, ],
        regular_pay: typing.Union[MetaOapg.properties.regular_pay, decimal.Decimal, int, float, ],
        cash_tips: typing.Union[MetaOapg.properties.cash_tips, decimal.Decimal, int, float, ],
        compliance_exceptions_pay: typing.Union[MetaOapg.properties.compliance_exceptions_pay, decimal.Decimal, int, float, ],
        tip_out: typing.Union[MetaOapg.properties.tip_out, decimal.Decimal, int, float, ],
        overtime_pay: typing.Union[MetaOapg.properties.overtime_pay, decimal.Decimal, int, float, ],
        premium_overtime_hours: typing.Union[MetaOapg.properties.premium_overtime_hours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        non_premium_overtime_hours: typing.Union[MetaOapg.properties.non_premium_overtime_hours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        premium_overtime_pay: typing.Union[MetaOapg.properties.premium_overtime_pay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        non_premium_overtime_pay: typing.Union[MetaOapg.properties.non_premium_overtime_pay, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pos_declared_tips: typing.Union[MetaOapg.properties.pos_declared_tips, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetWorkedHoursWagesResponseUsersItemTotal':
        return super().__new__(
            cls,
            *args,
            total_payment_tips=total_payment_tips,
            overtime_hours=overtime_hours,
            holiday_pay=holiday_pay,
            tip_in=tip_in,
            total_tips=total_tips,
            regular_hours=regular_hours,
            total_hours=total_hours,
            declared_tips=declared_tips,
            holiday_hours=holiday_hours,
            credit_card_tips=credit_card_tips,
            total_pay=total_pay,
            withheld_cc_amount=withheld_cc_amount,
            auto_gratuity=auto_gratuity,
            earned_tips=earned_tips,
            regular_pay=regular_pay,
            cash_tips=cash_tips,
            compliance_exceptions_pay=compliance_exceptions_pay,
            tip_out=tip_out,
            overtime_pay=overtime_pay,
            premium_overtime_hours=premium_overtime_hours,
            non_premium_overtime_hours=non_premium_overtime_hours,
            premium_overtime_pay=premium_overtime_pay,
            non_premium_overtime_pay=non_premium_overtime_pay,
            pos_declared_tips=pos_declared_tips,
            _configuration=_configuration,
            **kwargs,
        )
