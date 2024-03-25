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

from 7_shifts_python_sdk.model.time_off_get_total_hours200_response import TimeOffGetTotalHours200Response as TimeOffGetTotalHours200ResponseSchema
from 7_shifts_python_sdk.model.time_off_get_total_hours_response import TimeOffGetTotalHoursResponse as TimeOffGetTotalHoursResponseSchema

from 7_shifts_python_sdk.type.time_off_get_total_hours200_response import TimeOffGetTotalHours200Response
from 7_shifts_python_sdk.type.time_off_get_total_hours_response import TimeOffGetTotalHoursResponse

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.time_off_get_total_hours_response import TimeOffGetTotalHoursResponse as TimeOffGetTotalHoursResponsePydantic
from 7_shifts_python_sdk.pydantic.time_off_get_total_hours200_response import TimeOffGetTotalHours200Response as TimeOffGetTotalHours200ResponsePydantic

from . import path

# Query params
CompanyIdSchema = schemas.Int64Schema


class EmployeeIdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        min_items = 1
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmployeeIdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
DateStartSchema = schemas.StrSchema
DateEndSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
        'employee_id': typing.Union[EmployeeIdSchema, list, tuple, ],
        'date_start': typing.Union[DateStartSchema, str, ],
        'date_end': typing.Union[DateEndSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_company_id = api_client.QueryParameter(
    name="company_id",
    style=api_client.ParameterStyle.FORM,
    schema=CompanyIdSchema,
    required=True,
    explode=True,
)
request_query_employee_id = api_client.QueryParameter(
    name="employee_id",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdSchema,
    required=True,
    explode=True,
)
request_query_date_start = api_client.QueryParameter(
    name="date_start",
    style=api_client.ParameterStyle.FORM,
    schema=DateStartSchema,
    required=True,
    explode=True,
)
request_query_date_end = api_client.QueryParameter(
    name="date_end",
    style=api_client.ParameterStyle.FORM,
    schema=DateEndSchema,
    required=True,
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
SchemaFor200ResponseBodyApplicationJson = TimeOffGetTotalHours200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimeOffGetTotalHours200Response


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimeOffGetTotalHours200Response


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationProblemjson = TimeOffGetTotalHoursResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: TimeOffGetTotalHoursResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: TimeOffGetTotalHoursResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationProblemjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _get_total_hours_mapped_args(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if company_id is not None:
            _query_params["company_id"] = company_id
        if employee_id is not None:
            _query_params["employee_id"] = employee_id
        if date_start is not None:
            _query_params["date_start"] = date_start
        if date_end is not None:
            _query_params["date_end"] = date_end
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        args.query = _query_params
        args.header = _header_params
        return args

    async def _aget_total_hours_oapg(
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
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve Time Off Hours
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_company_id,
            request_query_employee_id,
            request_query_date_start,
            request_query_date_end,
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
            path_template='/v2/time_off/total_hours',
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
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


    def _get_total_hours_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve Time Off Hours
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_company_id,
            request_query_employee_id,
            request_query_date_start,
            request_query_date_end,
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
            path_template='/v2/time_off/total_hours',
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetTotalHoursRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_total_hours(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_total_hours_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            date_start=date_start,
            date_end=date_end,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aget_total_hours_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get_total_hours(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_total_hours_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            date_start=date_start,
            date_end=date_end,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._get_total_hours_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class GetTotalHours(BaseApi):

    async def aget_total_hours(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimeOffGetTotalHours200ResponsePydantic:
        raw_response = await self.raw.aget_total_hours(
            company_id=company_id,
            employee_id=employee_id,
            date_start=date_start,
            date_end=date_end,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            **kwargs,
        )
        if validate:
            return TimeOffGetTotalHours200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeOffGetTotalHours200ResponsePydantic, raw_response.body)
    
    
    def get_total_hours(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TimeOffGetTotalHours200ResponsePydantic:
        raw_response = self.raw.get_total_hours(
            company_id=company_id,
            employee_id=employee_id,
            date_start=date_start,
            date_end=date_end,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        if validate:
            return TimeOffGetTotalHours200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeOffGetTotalHours200ResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_total_hours_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            date_start=date_start,
            date_end=date_end,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aget_total_hours_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        company_id: int,
        employee_id: typing.List[int],
        date_start: str,
        date_end: str,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_total_hours_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            date_start=date_start,
            date_end=date_end,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._get_total_hours_oapg(
            query_params=args.query,
            header_params=args.header,
        )

