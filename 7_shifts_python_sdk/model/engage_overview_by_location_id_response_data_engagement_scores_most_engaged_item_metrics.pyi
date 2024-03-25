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


class EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetrics(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "lates",
            "total_shifts",
            "no_shows",
            "dropped_shifts",
            "shift_bids",
        }
        
        class properties:
        
            @staticmethod
            def shift_bids() -> typing.Type['EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids']:
                return EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids
        
            @staticmethod
            def dropped_shifts() -> typing.Type['EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts']:
                return EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts
        
            @staticmethod
            def no_shows() -> typing.Type['EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows']:
                return EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows
        
            @staticmethod
            def lates() -> typing.Type['EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates']:
                return EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates
            total_shifts = schemas.IntSchema
            __annotations__ = {
                "shift_bids": shift_bids,
                "dropped_shifts": dropped_shifts,
                "no_shows": no_shows,
                "lates": lates,
                "total_shifts": total_shifts,
            }
    
    lates: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates'
    total_shifts: MetaOapg.properties.total_shifts
    no_shows: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows'
    dropped_shifts: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts'
    shift_bids: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shift_bids"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dropped_shifts"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["no_shows"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lates"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_shifts"]) -> MetaOapg.properties.total_shifts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["shift_bids", "dropped_shifts", "no_shows", "lates", "total_shifts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shift_bids"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dropped_shifts"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["no_shows"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lates"]) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_shifts"]) -> MetaOapg.properties.total_shifts: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["shift_bids", "dropped_shifts", "no_shows", "lates", "total_shifts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lates: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates',
        total_shifts: typing.Union[MetaOapg.properties.total_shifts, decimal.Decimal, int, ],
        no_shows: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows',
        dropped_shifts: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts',
        shift_bids: 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetrics':
        return super().__new__(
            cls,
            *args,
            lates=lates,
            total_shifts=total_shifts,
            no_shows=no_shows,
            dropped_shifts=dropped_shifts,
            shift_bids=shift_bids,
            _configuration=_configuration,
            **kwargs,
        )

from 7_shifts_python_sdk.model.engage_overview_by_location_id_response_data_engagement_scores_most_engaged_item_metrics_dropped_shifts import EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsDroppedShifts
from 7_shifts_python_sdk.model.engage_overview_by_location_id_response_data_engagement_scores_most_engaged_item_metrics_lates import EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsLates
from 7_shifts_python_sdk.model.engage_overview_by_location_id_response_data_engagement_scores_most_engaged_item_metrics_no_shows import EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsNoShows
from 7_shifts_python_sdk.model.engage_overview_by_location_id_response_data_engagement_scores_most_engaged_item_metrics_shift_bids import EngageOverviewByLocationIdResponseDataEngagementScoresMostEngagedItemMetricsShiftBids
