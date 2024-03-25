# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from 7_shifts_python_sdk.paths.v2_company_company_id_departments.post import CreateNewDepartmentRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_departments_department_id.delete import DeleteByIdRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_departments_department_id.get import GetDepartmentRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_departments.get import ListRaw
from 7_shifts_python_sdk.paths.v2_company_company_id_departments_department_id.put import UpdateDepartmentRaw


class DepartmentsApiRaw(
    CreateNewDepartmentRaw,
    DeleteByIdRaw,
    GetDepartmentRaw,
    ListRaw,
    UpdateDepartmentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass