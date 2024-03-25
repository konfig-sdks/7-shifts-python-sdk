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

from 7_shifts_python_sdk.model.time_off_update_time_off_by_id_request_hours import TimeOffUpdateTimeOffByIdRequestHours as TimeOffUpdateTimeOffByIdRequestHoursSchema
from 7_shifts_python_sdk.model.time_off_update_time_off_by_id200_response import TimeOffUpdateTimeOffById200Response as TimeOffUpdateTimeOffById200ResponseSchema
from 7_shifts_python_sdk.model.time_off_update_time_off_by_id_request import TimeOffUpdateTimeOffByIdRequest as TimeOffUpdateTimeOffByIdRequestSchema
from 7_shifts_python_sdk.model.time_off_update_time_off_by_id_response import TimeOffUpdateTimeOffByIdResponse as TimeOffUpdateTimeOffByIdResponseSchema

from 7_shifts_python_sdk.type.time_off_update_time_off_by_id200_response import TimeOffUpdateTimeOffById200Response
from 7_shifts_python_sdk.type.time_off_update_time_off_by_id_response import TimeOffUpdateTimeOffByIdResponse
from 7_shifts_python_sdk.type.time_off_update_time_off_by_id_request_hours import TimeOffUpdateTimeOffByIdRequestHours
from 7_shifts_python_sdk.type.time_off_update_time_off_by_id_request import TimeOffUpdateTimeOffByIdRequest

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.time_off_update_time_off_by_id_response import TimeOffUpdateTimeOffByIdResponse as TimeOffUpdateTimeOffByIdResponsePydantic
from 7_shifts_python_sdk.pydantic.time_off_update_time_off_by_id_request_hours import TimeOffUpdateTimeOffByIdRequestHours as TimeOffUpdateTimeOffByIdRequestHoursPydantic
from 7_shifts_python_sdk.pydantic.time_off_update_time_off_by_id200_response import TimeOffUpdateTimeOffById200Response as TimeOffUpdateTimeOffById200ResponsePydantic
from 7_shifts_python_sdk.pydantic.time_off_update_time_off_by_id_request import TimeOffUpdateTimeOffByIdRequest as TimeOffUpdateTimeOffByIdRequestPydantic

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
TimeOffIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'time_off_id': typing.Union[TimeOffIdSchema, decimal.Decimal, int, ],
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


request_path_time_off_id = api_client.PathParameter(
    name="time_off_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TimeOffIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TimeOffUpdateTimeOffByIdRequestSchema


request_body_time_off_update_time_off_by_id_request = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = TimeOffUpdateTimeOffById200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimeOffUpdateTimeOffById200Response


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimeOffUpdateTimeOffById200Response


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationProblemjson = TimeOffUpdateTimeOffByIdResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: TimeOffUpdateTimeOffByIdResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: TimeOffUpdateTimeOffByIdResponse


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

    def _update_time_off_by_id_mapped_args(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if user_id is not None:
            _body["user_id"] = user_id
        if from_date is not None:
            _body["from_date"] = from_date
        if to_date is not None:
            _body["to_date"] = to_date
        if partial is not None:
            _body["partial"] = partial
        if partial_from is not None:
            _body["partial_from"] = partial_from
        if partial_to is not None:
            _body["partial_to"] = partial_to
        if comments is not None:
            _body["comments"] = comments
        if status is not None:
            _body["status"] = status
        if status_action_message is not None:
            _body["status_action_message"] = status_action_message
        if category is not None:
            _body["category"] = category
        if hours is not None:
            _body["hours"] = hours
        args.body = _body
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        if time_off_id is not None:
            _path_params["time_off_id"] = time_off_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_time_off_by_id_oapg(
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
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update Time Off
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_time_off_id,
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
        method = 'patch'.upper()
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
            path_template='/v2/time_off/{time_off_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_time_off_update_time_off_by_id_request.serialize(body, content_type)
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


    def _update_time_off_by_id_oapg(
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
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update Time Off
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_time_off_id,
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
        method = 'patch'.upper()
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
            path_template='/v2/time_off/{time_off_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_time_off_update_time_off_by_id_request.serialize(body, content_type)
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


class UpdateTimeOffByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_time_off_by_id(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_time_off_by_id_mapped_args(
            time_off_id=time_off_id,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            partial=partial,
            partial_from=partial_from,
            partial_to=partial_to,
            comments=comments,
            status=status,
            status_action_message=status_action_message,
            category=category,
            hours=hours,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aupdate_time_off_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_time_off_by_id(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_time_off_by_id_mapped_args(
            time_off_id=time_off_id,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            partial=partial,
            partial_from=partial_from,
            partial_to=partial_to,
            comments=comments,
            status=status,
            status_action_message=status_action_message,
            category=category,
            hours=hours,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._update_time_off_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateTimeOffById(BaseApi):

    async def aupdate_time_off_by_id(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimeOffUpdateTimeOffById200ResponsePydantic:
        raw_response = await self.raw.aupdate_time_off_by_id(
            time_off_id=time_off_id,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            partial=partial,
            partial_from=partial_from,
            partial_to=partial_to,
            comments=comments,
            status=status,
            status_action_message=status_action_message,
            category=category,
            hours=hours,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            **kwargs,
        )
        if validate:
            return TimeOffUpdateTimeOffById200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeOffUpdateTimeOffById200ResponsePydantic, raw_response.body)
    
    
    def update_time_off_by_id(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TimeOffUpdateTimeOffById200ResponsePydantic:
        raw_response = self.raw.update_time_off_by_id(
            time_off_id=time_off_id,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            partial=partial,
            partial_from=partial_from,
            partial_to=partial_to,
            comments=comments,
            status=status,
            status_action_message=status_action_message,
            category=category,
            hours=hours,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        if validate:
            return TimeOffUpdateTimeOffById200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeOffUpdateTimeOffById200ResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_time_off_by_id_mapped_args(
            time_off_id=time_off_id,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            partial=partial,
            partial_from=partial_from,
            partial_to=partial_to,
            comments=comments,
            status=status,
            status_action_message=status_action_message,
            category=category,
            hours=hours,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return await self._aupdate_time_off_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        time_off_id: int,
        user_id: typing.Optional[int] = None,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        partial: typing.Optional[bool] = None,
        partial_from: typing.Optional[typing.Optional[str]] = None,
        partial_to: typing.Optional[typing.Optional[str]] = None,
        comments: typing.Optional[str] = None,
        status: typing.Optional[int] = None,
        status_action_message: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        hours: typing.Optional[TimeOffUpdateTimeOffByIdRequestHours] = None,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_time_off_by_id_mapped_args(
            time_off_id=time_off_id,
            user_id=user_id,
            from_date=from_date,
            to_date=to_date,
            partial=partial,
            partial_from=partial_from,
            partial_to=partial_to,
            comments=comments,
            status=status,
            status_action_message=status_action_message,
            category=category,
            hours=hours,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
        )
        return self._update_time_off_by_id_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

