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


class EngageOverviewByLocationIdResponseDataEngagementScores(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "least_engaged",
            "most_engaged",
        }
        
        class properties:
        
            @staticmethod
            def most_engaged() -> typing.Type['EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged']:
                return EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged
        
            @staticmethod
            def least_engaged() -> typing.Type['EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged']:
                return EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged
            __annotations__ = {
                "most_engaged": most_engaged,
                "least_engaged": least_engaged,
            }
    
    least_engaged: 'EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged'
    most_engaged: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["most_engaged"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["least_engaged"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["most_engaged", "least_engaged", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["most_engaged"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["least_engaged"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["most_engaged", "least_engaged", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        least_engaged: 'EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged',
        most_engaged: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EngageOverviewByLocationIdResponseDataEngagementScores':
        return super().__new__(
            cls,
            *args,
            least_engaged=least_engaged,
            most_engaged=most_engaged,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.engage_overview_by_location_id_response_data_engagement_scores_least_engaged import EngageOverviewByLocationIdResponseDataEngagementScoresLeastEngaged
from 7_shifts_python_sdk.model.engage_overview_by_location_id_response_data_engagement_scores_most_engaged import EngageOverviewByLocationIdResponseDataEngagementScoresMostEngaged
