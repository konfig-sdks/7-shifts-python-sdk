# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import 7_shifts_python_sdk
from 7_shifts_python_sdk.paths.v2_company_company_id_shifts_scheduled_id import get
from 7_shifts_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2CompanyCompanyIdShiftsScheduledId(ApiTestMixin, unittest.TestCase):
    """
    V2CompanyCompanyIdShiftsScheduledId unit test stubs
        List Scheduled Shifts
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
