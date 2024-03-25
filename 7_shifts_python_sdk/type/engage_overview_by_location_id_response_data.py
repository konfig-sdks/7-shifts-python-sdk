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

from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_employee_stats import EngageOverviewByLocationIdResponseDataEmployeeStats
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_engagement_scores import EngageOverviewByLocationIdResponseDataEngagementScores
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_location_stats import EngageOverviewByLocationIdResponseDataLocationStats
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_shift_feedback import EngageOverviewByLocationIdResponseDataShiftFeedback
from 7_shifts_python_sdk.type.engage_overview_by_location_id_response_data_tenure import EngageOverviewByLocationIdResponseDataTenure

class RequiredEngageOverviewByLocationIdResponseData(TypedDict):
    location_stats: EngageOverviewByLocationIdResponseDataLocationStats

    employee_stats: EngageOverviewByLocationIdResponseDataEmployeeStats

    engagement_scores: EngageOverviewByLocationIdResponseDataEngagementScores

    shift_feedback: EngageOverviewByLocationIdResponseDataShiftFeedback

    tenure: EngageOverviewByLocationIdResponseDataTenure

class OptionalEngageOverviewByLocationIdResponseData(TypedDict, total=False):
    pass

class EngageOverviewByLocationIdResponseData(RequiredEngageOverviewByLocationIdResponseData, OptionalEngageOverviewByLocationIdResponseData):
    pass
