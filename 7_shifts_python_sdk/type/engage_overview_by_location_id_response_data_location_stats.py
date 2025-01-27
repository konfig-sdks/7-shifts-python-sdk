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

from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_location_stats_lates import EngageOverviewByLocationIdResponseDataLocationStatsLates
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_location_stats_no_shows import EngageOverviewByLocationIdResponseDataLocationStatsNoShows
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_location_stats_shift_bids import EngageOverviewByLocationIdResponseDataLocationStatsShiftBids
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_location_stats_shift_drops import EngageOverviewByLocationIdResponseDataLocationStatsShiftDrops
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_location_stats_sick_shifts import EngageOverviewByLocationIdResponseDataLocationStatsSickShifts

class RequiredEngageOverviewByLocationIdResponseDataLocationStats(TypedDict):
    lates: EngageOverviewByLocationIdResponseDataLocationStatsLates

    no_shows: EngageOverviewByLocationIdResponseDataLocationStatsNoShows

    sick_shifts: EngageOverviewByLocationIdResponseDataLocationStatsSickShifts

    shift_bids: EngageOverviewByLocationIdResponseDataLocationStatsShiftBids

    shift_drops: EngageOverviewByLocationIdResponseDataLocationStatsShiftDrops

class OptionalEngageOverviewByLocationIdResponseDataLocationStats(TypedDict, total=False):
    pass

class EngageOverviewByLocationIdResponseDataLocationStats(RequiredEngageOverviewByLocationIdResponseDataLocationStats, OptionalEngageOverviewByLocationIdResponseDataLocationStats):
    pass
