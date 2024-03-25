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

from 7_shifts_python_sdk.model.roles_get_role403_response import RolesGetRole403Response as RolesGetRole403ResponseSchema
from 7_shifts_python_sdk.model.roles_get_role404_response import RolesGetRole404Response as RolesGetRole404ResponseSchema
from 7_shifts_python_sdk.model.roles_get_role500_response import RolesGetRole500Response as RolesGetRole500ResponseSchema
from 7_shifts_python_sdk.model.roles_get_role_response import RolesGetRoleResponse as RolesGetRoleResponseSchema

from 7_shifts_python_sdk.type.roles_get_role500_response import RolesGetRole500Response
from 7_shifts_python_sdk.type.roles_get_role404_response import RolesGetRole404Response
from 7_shifts_python_sdk.type.roles_get_role_response import RolesGetRoleResponse
from 7_shifts_python_sdk.type.roles_get_role403_response import RolesGetRole403Response

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.roles_get_role_response import RolesGetRoleResponse as RolesGetRoleResponsePydantic
from 7_shifts_python_sdk.pydantic.roles_get_role403_response import RolesGetRole403Response as RolesGetRole403ResponsePydantic
from 7_shifts_python_sdk.pydantic.roles_get_role404_response import RolesGetRole404Response as RolesGetRole404ResponsePydantic
from 7_shifts_python_sdk.pydantic.roles_get_role500_response import RolesGetRole500Response as RolesGetRole500ResponsePydantic

# Header params


class XApiVersionSchema(
    schemas.StrSchema
):
    pass
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
RoleIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
        'role_id': typing.Union[RoleIdSchema, decimal.Decimal, int, ],
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
request_path_role_id = api_client.PathParameter(
    name="role_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RoleIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = RolesGetRoleResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RolesGetRoleResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RolesGetRoleResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationProblemjson = RolesGetRole403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: RolesGetRole403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: RolesGetRole403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationProblemjson),
    },
)
SchemaFor404ResponseBodyApplicationProblemjson = RolesGetRole404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: RolesGetRole404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: RolesGetRole404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationProblemjson),
    },
)
SchemaFor500ResponseBodyApplicationProblemjson = RolesGetRole500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: RolesGetRole500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: RolesGetRole500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationProblemjson),
    },
)
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _get_role_mapped_args(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        if company_id is not None:
            _path_params["company_id"] = company_id
        if role_id is not None:
            _path_params["role_id"] = role_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aget_role_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Retrieve Role
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
            request_path_role_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/company/{company_id}/roles/{role_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_role_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve Role
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
            request_path_role_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/company/{company_id}/roles/{role_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetRoleRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_role(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_role_mapped_args(
            company_id=company_id,
            role_id=role_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aget_role_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get_role(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_role_mapped_args(
            company_id=company_id,
            role_id=role_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._get_role_oapg(
            header_params=args.header,
            path_params=args.path,
        )

class GetRole(BaseApi):

    async def aget_role(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> RolesGetRoleResponsePydantic:
        raw_response = await self.raw.aget_role(
            company_id=company_id,
            role_id=role_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            **kwargs,
        )
        if validate:
            return RolesGetRoleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RolesGetRoleResponsePydantic, raw_response.body)
    
    
    def get_role(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> RolesGetRoleResponsePydantic:
        raw_response = self.raw.get_role(
            company_id=company_id,
            role_id=role_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        if validate:
            return RolesGetRoleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(RolesGetRoleResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_role_mapped_args(
            company_id=company_id,
            role_id=role_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aget_role_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: int,
        role_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_role_mapped_args(
            company_id=company_id,
            role_id=role_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._get_role_oapg(
            header_params=args.header,
            path_params=args.path,
        )

