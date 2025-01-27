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

from 7_shifts_python_sdk.model.time_off_list200_response import TimeOffList200Response as TimeOffList200ResponseSchema
from 7_shifts_python_sdk.model.time_off_list_response import TimeOffListResponse as TimeOffListResponseSchema

from 7_shifts_python_sdk.type.time_off_list_response import TimeOffListResponse
from 7_shifts_python_sdk.type.time_off_list200_response import TimeOffList200Response

from ...api_client import Dictionary
from 7_shifts_python_sdk.pydantic.time_off_list200_response import TimeOffList200Response as TimeOffList200ResponsePydantic
from 7_shifts_python_sdk.pydantic.time_off_list_response import TimeOffListResponse as TimeOffListResponsePydantic

from . import path

# Query params
CompanyIdSchema = schemas.Int64Schema
LocationIdSchema = schemas.Int64Schema
UserIdSchema = schemas.Int64Schema
StatusSchema = schemas.Int64Schema


class CategorySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "paid": "PAID",
            "unpaid": "UNPAID",
            "paid_sick": "PAID_SICK",
        }
    
    @schemas.classproperty
    def PAID(cls):
        return cls("paid")
    
    @schemas.classproperty
    def UNPAID(cls):
        return cls("unpaid")
    
    @schemas.classproperty
    def PAID_SICK(cls):
        return cls("paid_sick")


class ToDateGteSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^\d{4}-\d{2}-\d{2}$',
        }]


class SortBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "created": "CREATED",
            "from_date": "FROM_DATE",
        }
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("created")
    
    @schemas.classproperty
    def FROM_DATE(cls):
        return cls("from_date")


class SortDirSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "asc": "ASC",
            "desc": "DESC",
        }
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")
CursorSchema = schemas.StrSchema
LimitSchema = schemas.Int64Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'company_id': typing.Union[CompanyIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'location_id': typing.Union[LocationIdSchema, decimal.Decimal, int, ],
        'user_id': typing.Union[UserIdSchema, decimal.Decimal, int, ],
        'status': typing.Union[StatusSchema, decimal.Decimal, int, ],
        'category': typing.Union[CategorySchema, str, ],
        'to_date_gte': typing.Union[ToDateGteSchema, str, ],
        'sort_by': typing.Union[SortBySchema, str, ],
        'sort_dir': typing.Union[SortDirSchema, str, ],
        'cursor': typing.Union[CursorSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
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
request_query_location_id = api_client.QueryParameter(
    name="location_id",
    style=api_client.ParameterStyle.FORM,
    schema=LocationIdSchema,
    explode=True,
)
request_query_user_id = api_client.QueryParameter(
    name="user_id",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_category = api_client.QueryParameter(
    name="category",
    style=api_client.ParameterStyle.FORM,
    schema=CategorySchema,
    explode=True,
)
request_query_to_date_gte = api_client.QueryParameter(
    name="to_date_gte",
    style=api_client.ParameterStyle.FORM,
    schema=ToDateGteSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_dir = api_client.QueryParameter(
    name="sort_dir",
    style=api_client.ParameterStyle.FORM,
    schema=SortDirSchema,
    explode=True,
)
request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
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
SchemaFor200ResponseBodyApplicationJson = TimeOffList200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimeOffList200Response


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimeOffList200Response


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationProblemjson = TimeOffListResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: TimeOffListResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: TimeOffListResponse


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

    def _list_mapped_args(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if company_id is not None:
            _query_params["company_id"] = company_id
        if location_id is not None:
            _query_params["location_id"] = location_id
        if user_id is not None:
            _query_params["user_id"] = user_id
        if status is not None:
            _query_params["status"] = status
        if category is not None:
            _query_params["category"] = category
        if to_date_gte is not None:
            _query_params["to_date_gte"] = to_date_gte
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        if sort_dir is not None:
            _query_params["sort_dir"] = sort_dir
        if cursor is not None:
            _query_params["cursor"] = cursor
        if limit is not None:
            _query_params["limit"] = limit
        if x_api_version is not None:
            _header_params["x-api-version"] = x_api_version
        if x_company_guid is not None:
            _header_params["x-company-guid"] = x_company_guid
        args.query = _query_params
        args.header = _header_params
        return args

    async def _alist_oapg(
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
        List Time Off
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
            request_query_location_id,
            request_query_user_id,
            request_query_status,
            request_query_category,
            request_query_to_date_gte,
            request_query_sort_by,
            request_query_sort_dir,
            request_query_cursor,
            request_query_limit,
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
            path_template='/v2/time_off',
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


    def _list_oapg(
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
        List Time Off
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
            request_query_location_id,
            request_query_user_id,
            request_query_status,
            request_query_category,
            request_query_to_date_gte,
            request_query_sort_by,
            request_query_sort_dir,
            request_query_cursor,
            request_query_limit,
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
            path_template='/v2/time_off',
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


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            company_id=company_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            user_id=user_id,
            status=status,
            category=category,
            to_date_gte=to_date_gte,
            sort_by=sort_by,
            sort_dir=sort_dir,
            cursor=cursor,
            limit=limit,
        )
        return await self._alist_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def list(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            company_id=company_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            user_id=user_id,
            status=status,
            category=category,
            to_date_gte=to_date_gte,
            sort_by=sort_by,
            sort_dir=sort_dir,
            cursor=cursor,
            limit=limit,
        )
        return self._list_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class List(BaseApi):

    async def alist(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimeOffList200ResponsePydantic:
        raw_response = await self.raw.alist(
            company_id=company_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            user_id=user_id,
            status=status,
            category=category,
            to_date_gte=to_date_gte,
            sort_by=sort_by,
            sort_dir=sort_dir,
            cursor=cursor,
            limit=limit,
            **kwargs,
        )
        if validate:
            return TimeOffList200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeOffList200ResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> TimeOffList200ResponsePydantic:
        raw_response = self.raw.list(
            company_id=company_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            user_id=user_id,
            status=status,
            category=category,
            to_date_gte=to_date_gte,
            sort_by=sort_by,
            sort_dir=sort_dir,
            cursor=cursor,
            limit=limit,
        )
        if validate:
            return TimeOffList200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeOffList200ResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            company_id=company_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            user_id=user_id,
            status=status,
            category=category,
            to_date_gte=to_date_gte,
            sort_by=sort_by,
            sort_dir=sort_dir,
            cursor=cursor,
            limit=limit,
        )
        return await self._alist_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        company_id: int,
        x_api_version: typing.Optional[str] = None,
        x_company_guid: typing.Optional[str] = None,
        location_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        to_date_gte: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_dir: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            company_id=company_id,
            x_api_version=x_api_version,
            x_company_guid=x_company_guid,
            location_id=location_id,
            user_id=user_id,
            status=status,
            category=category,
            to_date_gte=to_date_gte,
            sort_by=sort_by,
            sort_dir=sort_dir,
            cursor=cursor,
            limit=limit,
        )
        return self._list_oapg(
            query_params=args.query,
            header_params=args.header,
        )

