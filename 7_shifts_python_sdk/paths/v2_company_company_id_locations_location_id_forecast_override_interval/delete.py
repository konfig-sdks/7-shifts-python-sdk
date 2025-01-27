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

from 7_shifts_python_sdk.model.forecast_overrides_sync_projected_sales_interval403_response import ForecastOverridesSyncProjectedSalesInterval403Response as ForecastOverridesSyncProjectedSalesInterval403ResponseSchema
from 7_shifts_python_sdk.model.forecast_overrides_sync_projected_sales_interval422_response import ForecastOverridesSyncProjectedSalesInterval422Response as ForecastOverridesSyncProjectedSalesInterval422ResponseSchema
from 7_shifts_python_sdk.model.forecast_overrides_sync_projected_sales_interval500_response import ForecastOverridesSyncProjectedSalesInterval500Response as ForecastOverridesSyncProjectedSalesInterval500ResponseSchema
from 7_shifts_python_sdk.model.forecast_overrides_sync_projected_sales_interval401_response import ForecastOverridesSyncProjectedSalesInterval401Response as ForecastOverridesSyncProjectedSalesInterval401ResponseSchema
from 7_shifts_python_sdk.model.forecast_overrides_sync_projected_sales_interval_response import ForecastOverridesSyncProjectedSalesIntervalResponse as ForecastOverridesSyncProjectedSalesIntervalResponseSchema
from 7_shifts_python_sdk.model.forecast_overrides_sync_projected_sales_interval_request import ForecastOverridesSyncProjectedSalesIntervalRequest as ForecastOverridesSyncProjectedSalesIntervalRequestSchema

from 7_shifts_python_sdk.type.forecast_overrides_sync_projected_sales_interval_request import ForecastOverridesSyncProjectedSalesIntervalRequest
from 7_shifts_python_sdk.type.forecast_overrides_sync_projected_sales_interval403_response import ForecastOverridesSyncProjectedSalesInterval403Response
from 7_shifts_python_sdk.type.forecast_overrides_sync_projected_sales_interval401_response import ForecastOverridesSyncProjectedSalesInterval401Response
from 7_shifts_python_sdk.type.forecast_overrides_sync_projected_sales_interval500_response import ForecastOverridesSyncProjectedSalesInterval500Response
from 7_shifts_python_sdk.type.forecast_overrides_sync_projected_sales_interval_response import ForecastOverridesSyncProjectedSalesIntervalResponse
from 7_shifts_python_sdk.type.forecast_overrides_sync_projected_sales_interval422_response import ForecastOverridesSyncProjectedSalesInterval422Response

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.forecast_overrides_sync_projected_sales_interval422_response import ForecastOverridesSyncProjectedSalesInterval422Response as ForecastOverridesSyncProjectedSalesInterval422ResponsePydantic
from 7_shifts_python_sdk.pydantic.forecast_overrides_sync_projected_sales_interval500_response import ForecastOverridesSyncProjectedSalesInterval500Response as ForecastOverridesSyncProjectedSalesInterval500ResponsePydantic
from 7_shifts_python_sdk.pydantic.forecast_overrides_sync_projected_sales_interval_response import ForecastOverridesSyncProjectedSalesIntervalResponse as ForecastOverridesSyncProjectedSalesIntervalResponsePydantic
from 7_shifts_python_sdk.pydantic.forecast_overrides_sync_projected_sales_interval_request import ForecastOverridesSyncProjectedSalesIntervalRequest as ForecastOverridesSyncProjectedSalesIntervalRequestPydantic
from 7_shifts_python_sdk.pydantic.forecast_overrides_sync_projected_sales_interval401_response import ForecastOverridesSyncProjectedSalesInterval401Response as ForecastOverridesSyncProjectedSalesInterval401ResponsePydantic
from 7_shifts_python_sdk.pydantic.forecast_overrides_sync_projected_sales_interval403_response import ForecastOverridesSyncProjectedSalesInterval403Response as ForecastOverridesSyncProjectedSalesInterval403ResponsePydantic

from . import path

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
# Path params
CompanyIdSchema = schemas.Int64Schema
LocationIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
        'location_id': typing.Union[LocationIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_id = api_client.PathParameter(
    name="company_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
request_path_location_id = api_client.PathParameter(
    name="location_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LocationIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ForecastOverridesSyncProjectedSalesIntervalRequestSchema


request_body_forecast_overrides_sync_projected_sales_interval_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2',
    'OAuth2',
    'OAuth2',
    'cookieAuth',
]


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
)
SchemaFor400ResponseBodyApplicationProblemjson = ForecastOverridesSyncProjectedSalesIntervalResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ForecastOverridesSyncProjectedSalesIntervalResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ForecastOverridesSyncProjectedSalesIntervalResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationProblemjson),
    },
)
SchemaFor401ResponseBodyApplicationProblemjson = ForecastOverridesSyncProjectedSalesInterval401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationProblemjson),
    },
)
SchemaFor403ResponseBodyApplicationProblemjson = ForecastOverridesSyncProjectedSalesInterval403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationProblemjson),
    },
)
SchemaFor422ResponseBodyApplicationProblemjson = ForecastOverridesSyncProjectedSalesInterval422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationProblemjson),
    },
)
SchemaFor500ResponseBodyApplicationProblemjson = ForecastOverridesSyncProjectedSalesInterval500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ForecastOverridesSyncProjectedSalesInterval500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationProblemjson),
    },
)
_status_code_to_response = {
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _sync_projected_sales_interval_mapped_args(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if start is not None:
            _body["start"] = start
        if end is not None:
            _body["end"] = end
        if report_type is not None:
            _body["report_type"] = report_type
        args.body = _body
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        if company_id is not None:
            _path_params["company_id"] = company_id
        if location_id is not None:
            _path_params["location_id"] = location_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _async_projected_sales_interval_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Sync Interval Projected Forecast Override
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_location_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        method = 'delete'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/company/{company_id}/locations/{location_id}/forecast_override_interval',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_forecast_overrides_sync_projected_sales_interval_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _sync_projected_sales_interval_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Sync Interval Projected Forecast Override
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_location_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        method = 'delete'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/company/{company_id}/locations/{location_id}/forecast_override_interval',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_forecast_overrides_sync_projected_sales_interval_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class SyncProjectedSalesIntervalRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def async_projected_sales_interval(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._sync_projected_sales_interval_mapped_args(
            start=start,
            end=end,
            company_id=company_id,
            location_id=location_id,
            report_type=report_type,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._async_projected_sales_interval_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def sync_projected_sales_interval(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._sync_projected_sales_interval_mapped_args(
            start=start,
            end=end,
            company_id=company_id,
            location_id=location_id,
            report_type=report_type,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._sync_projected_sales_interval_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class SyncProjectedSalesInterval(BaseApi):

    async def async_projected_sales_interval(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.async_projected_sales_interval(
            start=start,
            end=end,
            company_id=company_id,
            location_id=location_id,
            report_type=report_type,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            **kwargs,
        )
    
    
    def sync_projected_sales_interval(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.sync_projected_sales_interval(
            start=start,
            end=end,
            company_id=company_id,
            location_id=location_id,
            report_type=report_type,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._sync_projected_sales_interval_mapped_args(
            start=start,
            end=end,
            company_id=company_id,
            location_id=location_id,
            report_type=report_type,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._async_projected_sales_interval_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        start: datetime,
        end: datetime,
        company_id: int,
        location_id: int,
        report_type: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._sync_projected_sales_interval_mapped_args(
            start=start,
            end=end,
            company_id=company_id,
            location_id=location_id,
            report_type=report_type,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._sync_projected_sales_interval_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

