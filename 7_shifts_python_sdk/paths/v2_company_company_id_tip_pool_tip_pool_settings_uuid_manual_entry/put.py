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

from 7_shifts_python_sdk.model.tip_pool_save_manual_entry401_response import TipPoolSaveManualEntry401Response as TipPoolSaveManualEntry401ResponseSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry_request_data import TipPoolSaveManualEntryRequestData as TipPoolSaveManualEntryRequestDataSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry403_response import TipPoolSaveManualEntry403Response as TipPoolSaveManualEntry403ResponseSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry500_response import TipPoolSaveManualEntry500Response as TipPoolSaveManualEntry500ResponseSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry422_response import TipPoolSaveManualEntry422Response as TipPoolSaveManualEntry422ResponseSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry_response import TipPoolSaveManualEntryResponse as TipPoolSaveManualEntryResponseSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry_request import TipPoolSaveManualEntryRequest as TipPoolSaveManualEntryRequestSchema
from 7_shifts_python_sdk.model.tip_pool_save_manual_entry400_response import TipPoolSaveManualEntry400Response as TipPoolSaveManualEntry400ResponseSchema

from 7_shifts_python_sdk.type.tip_pool_save_manual_entry401_response import TipPoolSaveManualEntry401Response
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry500_response import TipPoolSaveManualEntry500Response
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry_request_data import TipPoolSaveManualEntryRequestData
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry400_response import TipPoolSaveManualEntry400Response
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry_response import TipPoolSaveManualEntryResponse
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry_request import TipPoolSaveManualEntryRequest
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry422_response import TipPoolSaveManualEntry422Response
from 7_shifts_python_sdk.type.tip_pool_save_manual_entry403_response import TipPoolSaveManualEntry403Response

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry500_response import TipPoolSaveManualEntry500Response as TipPoolSaveManualEntry500ResponsePydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry_response import TipPoolSaveManualEntryResponse as TipPoolSaveManualEntryResponsePydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry400_response import TipPoolSaveManualEntry400Response as TipPoolSaveManualEntry400ResponsePydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry403_response import TipPoolSaveManualEntry403Response as TipPoolSaveManualEntry403ResponsePydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry_request_data import TipPoolSaveManualEntryRequestData as TipPoolSaveManualEntryRequestDataPydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry401_response import TipPoolSaveManualEntry401Response as TipPoolSaveManualEntry401ResponsePydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry_request import TipPoolSaveManualEntryRequest as TipPoolSaveManualEntryRequestPydantic
from 7_shifts_python_sdk.pydantic.tip_pool_save_manual_entry422_response import TipPoolSaveManualEntry422Response as TipPoolSaveManualEntry422ResponsePydantic

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
CompanyIdSchema = schemas.IntSchema
TipPoolSettingsUuidSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
        'tip_pool_settings_uuid': typing.Union[TipPoolSettingsUuidSchema, str, uuid.UUID, ],
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
request_path_tip_pool_settings_uuid = api_client.PathParameter(
    name="tip_pool_settings_uuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TipPoolSettingsUuidSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TipPoolSaveManualEntryRequestSchema


request_body_tip_pool_save_manual_entry_request = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = TipPoolSaveManualEntryResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TipPoolSaveManualEntryResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TipPoolSaveManualEntryResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationProblemjson = TipPoolSaveManualEntry400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: TipPoolSaveManualEntry400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: TipPoolSaveManualEntry400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationProblemjson),
    },
)
SchemaFor401ResponseBodyApplicationProblemjson = TipPoolSaveManualEntry401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: TipPoolSaveManualEntry401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: TipPoolSaveManualEntry401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationProblemjson),
    },
)
SchemaFor403ResponseBodyApplicationProblemjson = TipPoolSaveManualEntry403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: TipPoolSaveManualEntry403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: TipPoolSaveManualEntry403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationProblemjson),
    },
)
SchemaFor422ResponseBodyApplicationProblemjson = TipPoolSaveManualEntry422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: TipPoolSaveManualEntry422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: TipPoolSaveManualEntry422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationProblemjson),
    },
)
SchemaFor500ResponseBodyApplicationProblemjson = TipPoolSaveManualEntry500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: TipPoolSaveManualEntry500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: TipPoolSaveManualEntry500Response


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
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _save_manual_entry_mapped_args(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if object is not None:
            _body["object"] = object
        if data is not None:
            _body["data"] = data
        args.body = _body
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        if company_id is not None:
            _path_params["company_id"] = company_id
        if tip_pool_settings_uuid is not None:
            _path_params["tip_pool_settings_uuid"] = tip_pool_settings_uuid
        args.header = _header_params
        args.path = _path_params
        return args

    async def _asave_manual_entry_oapg(
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
        Saves manual entries for a tip pool
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
            request_path_tip_pool_settings_uuid,
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
            path_template='/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tip_pool_save_manual_entry_request.serialize(body, content_type)
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


    def _save_manual_entry_oapg(
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
        Saves manual entries for a tip pool
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
            request_path_tip_pool_settings_uuid,
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
            path_template='/v2/company/{company_id}/tip_pool/{tip_pool_settings_uuid}/manual_entry',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_tip_pool_save_manual_entry_request.serialize(body, content_type)
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


class SaveManualEntryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asave_manual_entry(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._save_manual_entry_mapped_args(
            data=data,
            company_id=company_id,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            object=object,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._asave_manual_entry_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def save_manual_entry(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._save_manual_entry_mapped_args(
            data=data,
            company_id=company_id,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            object=object,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._save_manual_entry_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class SaveManualEntry(BaseApi):

    async def asave_manual_entry(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TipPoolSaveManualEntryResponsePydantic:
        raw_response = await self.raw.asave_manual_entry(
            data=data,
            company_id=company_id,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            object=object,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            **kwargs,
        )
        if validate:
            return TipPoolSaveManualEntryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TipPoolSaveManualEntryResponsePydantic, raw_response.body)
    
    
    def save_manual_entry(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TipPoolSaveManualEntryResponsePydantic:
        raw_response = self.raw.save_manual_entry(
            data=data,
            company_id=company_id,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            object=object,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        if validate:
            return TipPoolSaveManualEntryResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TipPoolSaveManualEntryResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._save_manual_entry_mapped_args(
            data=data,
            company_id=company_id,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            object=object,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._asave_manual_entry_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        data: TipPoolSaveManualEntryRequestData,
        company_id: int,
        tip_pool_settings_uuid: str,
        object: typing.Optional[str] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._save_manual_entry_mapped_args(
            data=data,
            company_id=company_id,
            tip_pool_settings_uuid=tip_pool_settings_uuid,
            object=object,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._save_manual_entry_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

