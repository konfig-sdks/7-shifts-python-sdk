# coding: utf-8

"""
    7shifts API

    7shifts is a team management software designed for restaurants. We help managers and operators spend less time and effort scheduling their staff, reduce their monthly labor costs and improve team communication. The result is simplified team management, one shift at a time.  7shifts also offers free mobile apps (iOS and Android) allowing managers and employees to have everything at their fingertips.  Start your free trial or request a demo at www.7shifts.com.

    The version of the OpenAPI document: 2023-05-01
    Contact: api-support@7shifts.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from 7_shifts_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from 7_shifts_python_sdk.api_response import AsyncGeneratorResponse
from 7_shifts_python_sdk import api_client, exceptions
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

from 7_shifts_python_sdk.model.reports_get_worked_hours_wages_response import ReportsGetWorkedHoursWagesResponse as ReportsGetWorkedHoursWagesResponseSchema
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages401_response import ReportsGetWorkedHoursWages401Response as ReportsGetWorkedHoursWages401ResponseSchema
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages400_response import ReportsGetWorkedHoursWages400Response as ReportsGetWorkedHoursWages400ResponseSchema
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages403_response import ReportsGetWorkedHoursWages403Response as ReportsGetWorkedHoursWages403ResponseSchema
from 7_shifts_python_sdk.model.reports_get_worked_hours_wages500_response import ReportsGetWorkedHoursWages500Response as ReportsGetWorkedHoursWages500ResponseSchema

from 7_shifts_python_sdk.type.reports_get_worked_hours_wages401_response import ReportsGetWorkedHoursWages401Response
from 7_shifts_python_sdk.type.reports_get_worked_hours_wages500_response import ReportsGetWorkedHoursWages500Response
from 7_shifts_python_sdk.type.reports_get_worked_hours_wages_response import ReportsGetWorkedHoursWagesResponse
from 7_shifts_python_sdk.type.reports_get_worked_hours_wages400_response import ReportsGetWorkedHoursWages400Response
from 7_shifts_python_sdk.type.reports_get_worked_hours_wages403_response import ReportsGetWorkedHoursWages403Response

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages401_response import ReportsGetWorkedHoursWages401Response as ReportsGetWorkedHoursWages401ResponsePydantic
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages403_response import ReportsGetWorkedHoursWages403Response as ReportsGetWorkedHoursWages403ResponsePydantic
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages500_response import ReportsGetWorkedHoursWages500Response as ReportsGetWorkedHoursWages500ResponsePydantic
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages400_response import ReportsGetWorkedHoursWages400Response as ReportsGetWorkedHoursWages400ResponsePydantic
from 7_shifts_python_sdk.pydantic.reports_get_worked_hours_wages_response import ReportsGetWorkedHoursWagesResponse as ReportsGetWorkedHoursWagesResponsePydantic

from . import path

# Query params
PunchesSchema = schemas.BoolSchema
CompanyIdSchema = schemas.Int64Schema


class ModelFromSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\d{4}-\d{2}-\d{2}$',
        }]


class ToSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\d{4}-\d{2}-\d{2}$',
        }]
LocationIdSchema = schemas.Int64Schema
DepartmentIdSchema = schemas.Int64Schema
RoleIdSchema = schemas.Int64Schema
UserIdSchema = schemas.Int64Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'punches': typing.Union[PunchesSchema, bool, ],
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
        'from': typing.Union[ModelFromSchema, str, ],
        'to': typing.Union[ToSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'location_id': typing.Union[LocationIdSchema, decimal.Decimal, int, ],
        'department_id': typing.Union[DepartmentIdSchema, decimal.Decimal, int, ],
        'role_id': typing.Union[RoleIdSchema, decimal.Decimal, int, ],
        'user_id': typing.Union[UserIdSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_punches = api_client.QueryParameter(
    name="punches",
    style=api_client.ParameterStyle.FORM,
    schema=PunchesSchema,
    required=True,
    explode=True,
)
request_query_company_id = api_client.QueryParameter(
    name="company_id",
    style=api_client.ParameterStyle.FORM,
    schema=CompanyIdSchema,
    required=True,
    explode=True,
)
request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    required=True,
    explode=True,
)
request_query_to = api_client.QueryParameter(
    name="to",
    style=api_client.ParameterStyle.FORM,
    schema=ToSchema,
    required=True,
    explode=True,
)
request_query_location_id = api_client.QueryParameter(
    name="location_id",
    style=api_client.ParameterStyle.FORM,
    schema=LocationIdSchema,
    explode=True,
)
request_query_department_id = api_client.QueryParameter(
    name="department_id",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentIdSchema,
    explode=True,
)
request_query_role_id = api_client.QueryParameter(
    name="role_id",
    style=api_client.ParameterStyle.FORM,
    schema=RoleIdSchema,
    explode=True,
)
request_query_user_id = api_client.QueryParameter(
    name="user_id",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    explode=True,
)
# Header params


class XApiVersionSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\d{4}-\d{2}-\d{2}$',
        }]
XCompanyGuidSchema = schemas.UUIDSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-api-version': typing.Union[XApiVersionSchema, str, ],
        'x-company-guid': typing.Union[XCompanyGuidSchema, str, uuid.UUID, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_api_version = api_client.HeaderParameter(
    name="x-api-version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XApiVersionSchema,
)
request_header_x_company_guid = api_client.HeaderParameter(
    name="x-company-guid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XCompanyGuidSchema,
)
_auth = [
    'OAuth2',
    'OAuth2',
    'OAuth2',
    'cookieAuth',
]
SchemaFor200ResponseBodyApplicationJson = ReportsGetWorkedHoursWagesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReportsGetWorkedHoursWagesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReportsGetWorkedHoursWagesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationProblemjson = ReportsGetWorkedHoursWages400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ReportsGetWorkedHoursWages400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ReportsGetWorkedHoursWages400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationProblemjson),
    },
)
SchemaFor401ResponseBodyApplicationProblemjson = ReportsGetWorkedHoursWages401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ReportsGetWorkedHoursWages401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ReportsGetWorkedHoursWages401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationProblemjson),
    },
)
SchemaFor403ResponseBodyApplicationProblemjson = ReportsGetWorkedHoursWages403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ReportsGetWorkedHoursWages403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ReportsGetWorkedHoursWages403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationProblemjson),
    },
)
SchemaFor500ResponseBodyApplicationProblemjson = ReportsGetWorkedHoursWages500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ReportsGetWorkedHoursWages500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ReportsGetWorkedHoursWages500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationProblemjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _get_worked_hours_wages_mapped_args(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if punches is not None:
            _query_params["punches"] = punches
        if company_id is not None:
            _query_params["company_id"] = company_id
        if _from is not None:
            _query_params["from"] = _from
        if to is not None:
            _query_params["to"] = to
        if location_id is not None:
            _query_params["location_id"] = location_id
        if department_id is not None:
            _query_params["department_id"] = department_id
        if role_id is not None:
            _query_params["role_id"] = role_id
        if user_id is not None:
            _query_params["user_id"] = user_id
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        args.query = _query_params
        args.header = _header_params
        return args

    async def _aget_worked_hours_wages_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve Worked Hours &amp; Wages
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_punches,
            request_query_company_id,
            request_query__from,
            request_query_to,
            request_query_location_id,
            request_query_department_id,
            request_query_role_id,
            request_query_user_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_api_version,
            request_header_x_company_guid,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/reports/hours_and_wages',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_worked_hours_wages_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve Worked Hours &amp; Wages
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_punches,
            request_query_company_id,
            request_query__from,
            request_query_to,
            request_query_location_id,
            request_query_department_id,
            request_query_role_id,
            request_query_user_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_api_version,
            request_header_x_company_guid,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/reports/hours_and_wages',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetWorkedHoursWagesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_worked_hours_wages(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_worked_hours_wages_mapped_args(
            punches=punches,
            company_id=company_id,
            _from=_from,
            to=to,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            department_id=department_id,
            role_id=role_id,
            user_id=user_id,
        )
        return await self._aget_worked_hours_wages_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get_worked_hours_wages(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_worked_hours_wages_mapped_args(
            punches=punches,
            company_id=company_id,
            _from=_from,
            to=to,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            department_id=department_id,
            role_id=role_id,
            user_id=user_id,
        )
        return self._get_worked_hours_wages_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class GetWorkedHoursWages(BaseApi):

    async def aget_worked_hours_wages(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReportsGetWorkedHoursWagesResponsePydantic:
        raw_response = await self.raw.aget_worked_hours_wages(
            punches=punches,
            company_id=company_id,
            _from=_from,
            to=to,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            department_id=department_id,
            role_id=role_id,
            user_id=user_id,
            **kwargs,
        )
        if validate:
            return ReportsGetWorkedHoursWagesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportsGetWorkedHoursWagesResponsePydantic, raw_response.body)
    
    
    def get_worked_hours_wages(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ReportsGetWorkedHoursWagesResponsePydantic:
        raw_response = self.raw.get_worked_hours_wages(
            punches=punches,
            company_id=company_id,
            _from=_from,
            to=to,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            department_id=department_id,
            role_id=role_id,
            user_id=user_id,
        )
        if validate:
            return ReportsGetWorkedHoursWagesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportsGetWorkedHoursWagesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_worked_hours_wages_mapped_args(
            punches=punches,
            company_id=company_id,
            _from=_from,
            to=to,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            department_id=department_id,
            role_id=role_id,
            user_id=user_id,
        )
        return await self._aget_worked_hours_wages_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        punches: bool,
        company_id: int,
        _from: str,
        to: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        department_id: typing.Optional[int] = None,
        role_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_worked_hours_wages_mapped_args(
            punches=punches,
            company_id=company_id,
            _from=_from,
            to=to,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            department_id=department_id,
            role_id=role_id,
            user_id=user_id,
        )
        return self._get_worked_hours_wages_oapg(
            query_params=args.query,
            header_params=args.header,
        )

