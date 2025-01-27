# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from 7_shifts_python_sdk.paths.v2_company_company_id_availabilities.post import CreateNew
from 7_shifts_python_sdk.paths.v2_company_company_id_availability_reasons.post import CreateReason
from 7_shifts_python_sdk.paths.v2_company_company_id_availability_reasons_availability_reason_id.delete import DeleteReason
from 7_shifts_python_sdk.paths.v2_company_company_id_availabilities_availability_id.get import GetById
from 7_shifts_python_sdk.paths.v2_company_company_id_availabilities.get import ListAvailabilities
from 7_shifts_python_sdk.paths.v2_company_company_id_availability_reasons.get import ListReasons
from 7_shifts_python_sdk.paths.v2_company_company_id_availabilities_availability_id.delete import RemoveById
from 7_shifts_python_sdk.paths.v2_company_company_id_availabilities_availability_id.put import UpdateById
from 7_shifts_python_sdk.paths.v2_company_company_id_availability_reasons_availability_reason_id.put import UpdateReasonById
from 7_shifts_python_sdk.paths.v2_company_company_id_availabilities_availability_id_status.put import UpdateStatus
from 7_shifts_python_sdk.apis.tags.availability_api_raw import AvailabilityApiRaw


class AvailabilityApi(
    CreateNew,
    CreateReason,
    DeleteReason,
    GetById,
    ListAvailabilities,
    ListReasons,
    RemoveById,
    UpdateById,
    UpdateReasonById,
    UpdateStatus,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AvailabilityApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AvailabilityApiRaw(api_client)
