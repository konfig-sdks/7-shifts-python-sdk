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

from 7_shifts_python_sdk.model.availability_update_reason_by_id422_response import AvailabilityUpdateReasonById422Response as AvailabilityUpdateReasonById422ResponseSchema
from 7_shifts_python_sdk.model.availability_update_reason_by_id400_response import AvailabilityUpdateReasonById400Response as AvailabilityUpdateReasonById400ResponseSchema
from 7_shifts_python_sdk.model.availability_update_reason_by_id404_response import AvailabilityUpdateReasonById404Response as AvailabilityUpdateReasonById404ResponseSchema
from 7_shifts_python_sdk.model.availability_update_reason_by_id403_response import AvailabilityUpdateReasonById403Response as AvailabilityUpdateReasonById403ResponseSchema
from 7_shifts_python_sdk.model.availability_update_reason_by_id_request import AvailabilityUpdateReasonByIdRequest as AvailabilityUpdateReasonByIdRequestSchema
from 7_shifts_python_sdk.model.availability_update_reason_by_id500_response import AvailabilityUpdateReasonById500Response as AvailabilityUpdateReasonById500ResponseSchema
from 7_shifts_python_sdk.model.availability_update_reason_by_id_response import AvailabilityUpdateReasonByIdResponse as AvailabilityUpdateReasonByIdResponseSchema

from 7_shifts_python_sdk.type.availability_update_reason_by_id400_response import AvailabilityUpdateReasonById400Response
from 7_shifts_python_sdk.type.availability_update_reason_by_id403_response import AvailabilityUpdateReasonById403Response
from 7_shifts_python_sdk.type.availability_update_reason_by_id422_response import AvailabilityUpdateReasonById422Response
from 7_shifts_python_sdk.type.availability_update_reason_by_id500_response import AvailabilityUpdateReasonById500Response
from 7_shifts_python_sdk.type.availability_update_reason_by_id_request import AvailabilityUpdateReasonByIdRequest
from 7_shifts_python_sdk.type.availability_update_reason_by_id404_response import AvailabilityUpdateReasonById404Response
from 7_shifts_python_sdk.type.availability_update_reason_by_id_response import AvailabilityUpdateReasonByIdResponse

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id422_response import AvailabilityUpdateReasonById422Response as AvailabilityUpdateReasonById422ResponsePydantic
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id404_response import AvailabilityUpdateReasonById404Response as AvailabilityUpdateReasonById404ResponsePydantic
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id403_response import AvailabilityUpdateReasonById403Response as AvailabilityUpdateReasonById403ResponsePydantic
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id400_response import AvailabilityUpdateReasonById400Response as AvailabilityUpdateReasonById400ResponsePydantic
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id_response import AvailabilityUpdateReasonByIdResponse as AvailabilityUpdateReasonByIdResponsePydantic
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id_request import AvailabilityUpdateReasonByIdRequest as AvailabilityUpdateReasonByIdRequestPydantic
from 7_shifts_python_sdk.pydantic.availability_update_reason_by_id500_response import AvailabilityUpdateReasonById500Response as AvailabilityUpdateReasonById500ResponsePydantic

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
AvailabilityReasonIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
        'availability_reason_id': typing.Union[AvailabilityReasonIdSchema, decimal.Decimal, int, ],
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
request_path_availability_reason_id = api_client.PathParameter(
    name="availability_reason_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AvailabilityReasonIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = AvailabilityUpdateReasonByIdRequestSchema


request_body_availability_update_reason_by_id_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'OAuth2',
    'OAuth2',
    'OAuth2',
    'cookieAuth',
]
SchemaFor200ResponseBodyApplicationJson = AvailabilityUpdateReasonByIdResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AvailabilityUpdateReasonByIdResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AvailabilityUpdateReasonByIdResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationProblemjson = AvailabilityUpdateReasonById400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: AvailabilityUpdateReasonById400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AvailabilityUpdateReasonById400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationProblemjson),
    },
)
SchemaFor403ResponseBodyApplicationProblemjson = AvailabilityUpdateReasonById403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: AvailabilityUpdateReasonById403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: AvailabilityUpdateReasonById403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationProblemjson),
    },
)
SchemaFor404ResponseBodyApplicationProblemjson = AvailabilityUpdateReasonById404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: AvailabilityUpdateReasonById404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: AvailabilityUpdateReasonById404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationProblemjson),
    },
)
SchemaFor422ResponseBodyApplicationProblemjson = AvailabilityUpdateReasonById422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: AvailabilityUpdateReasonById422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: AvailabilityUpdateReasonById422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationProblemjson),
    },
)
SchemaFor500ResponseBodyApplicationProblemjson = AvailabilityUpdateReasonById500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: AvailabilityUpdateReasonById500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: AvailabilityUpdateReasonById500Response


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
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _update_reason_by_id_mapped_args(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if reason is not None:
            _body["reason"] = reason
        if comments_required is not None:
            _body["comments_required"] = comments_required
        args.body = _body
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        if company_id is not None:
            _path_params["company_id"] = company_id
        if availability_reason_id is not None:
            _path_params["availability_reason_id"] = availability_reason_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_reason_by_id_oapg(
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
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Availability Reason
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
            request_path_availability_reason_id,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/company/{company_id}/availability_reasons/{availability_reason_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_availability_update_reason_by_id_request.serialize(body, content_type)
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


    def _update_reason_by_id_oapg(
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
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Availability Reason
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
            request_path_availability_reason_id,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/company/{company_id}/availability_reasons/{availability_reason_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_availability_update_reason_by_id_request.serialize(body, content_type)
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


class UpdateReasonByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_reason_by_id(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_reason_by_id_mapped_args(
            reason=reason,
            company_id=company_id,
            availability_reason_id=availability_reason_id,
            comments_required=comments_required,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aupdate_reason_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_reason_by_id(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_reason_by_id_mapped_args(
            reason=reason,
            company_id=company_id,
            availability_reason_id=availability_reason_id,
            comments_required=comments_required,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._update_reason_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateReasonById(BaseApi):

    async def aupdate_reason_by_id(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AvailabilityUpdateReasonByIdResponsePydantic:
        raw_response = await self.raw.aupdate_reason_by_id(
            reason=reason,
            company_id=company_id,
            availability_reason_id=availability_reason_id,
            comments_required=comments_required,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            **kwargs,
        )
        if validate:
            return AvailabilityUpdateReasonByIdResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AvailabilityUpdateReasonByIdResponsePydantic, raw_response.body)
    
    
    def update_reason_by_id(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AvailabilityUpdateReasonByIdResponsePydantic:
        raw_response = self.raw.update_reason_by_id(
            reason=reason,
            company_id=company_id,
            availability_reason_id=availability_reason_id,
            comments_required=comments_required,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        if validate:
            return AvailabilityUpdateReasonByIdResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AvailabilityUpdateReasonByIdResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_reason_by_id_mapped_args(
            reason=reason,
            company_id=company_id,
            availability_reason_id=availability_reason_id,
            comments_required=comments_required,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aupdate_reason_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        reason: str,
        company_id: int,
        availability_reason_id: int,
        comments_required: typing.Optional[typing.Optional[bool]] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_reason_by_id_mapped_args(
            reason=reason,
            company_id=company_id,
            availability_reason_id=availability_reason_id,
            comments_required=comments_required,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._update_reason_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

