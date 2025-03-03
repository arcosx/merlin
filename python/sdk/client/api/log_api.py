# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from client.api_client import ApiClient


class LogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def logs_get(self, cluster, namespace, component_type, **kwargs):  # noqa: E501
        """Retrieve log from a container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logs_get(cluster, namespace, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster: (required)
        :param str namespace: (required)
        :param str component_type: (required)
        :param str project_name:
        :param str model_id:
        :param str model_name:
        :param str version_id:
        :param str prediction_job_id:
        :param str container_name:
        :param str prefix:
        :param str follow:
        :param str previous:
        :param str since_seconds:
        :param str since_time:
        :param str timestamps:
        :param str tail_lines:
        :param str limit_bytes:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.logs_get_with_http_info(cluster, namespace, component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.logs_get_with_http_info(cluster, namespace, component_type, **kwargs)  # noqa: E501
            return data

    def logs_get_with_http_info(self, cluster, namespace, component_type, **kwargs):  # noqa: E501
        """Retrieve log from a container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logs_get_with_http_info(cluster, namespace, component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster: (required)
        :param str namespace: (required)
        :param str component_type: (required)
        :param str project_name:
        :param str model_id:
        :param str model_name:
        :param str version_id:
        :param str prediction_job_id:
        :param str container_name:
        :param str prefix:
        :param str follow:
        :param str previous:
        :param str since_seconds:
        :param str since_time:
        :param str timestamps:
        :param str tail_lines:
        :param str limit_bytes:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster', 'namespace', 'component_type', 'project_name', 'model_id', 'model_name', 'version_id', 'prediction_job_id', 'container_name', 'prefix', 'follow', 'previous', 'since_seconds', 'since_time', 'timestamps', 'tail_lines', 'limit_bytes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster' is set
        if ('cluster' not in params or
                params['cluster'] is None):
            raise ValueError("Missing the required parameter `cluster` when calling `logs_get`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `logs_get`")  # noqa: E501
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `logs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_name' in params:
            query_params.append(('project_name', params['project_name']))  # noqa: E501
        if 'model_id' in params:
            query_params.append(('model_id', params['model_id']))  # noqa: E501
        if 'model_name' in params:
            query_params.append(('model_name', params['model_name']))  # noqa: E501
        if 'version_id' in params:
            query_params.append(('version_id', params['version_id']))  # noqa: E501
        if 'prediction_job_id' in params:
            query_params.append(('prediction_job_id', params['prediction_job_id']))  # noqa: E501
        if 'cluster' in params:
            query_params.append(('cluster', params['cluster']))  # noqa: E501
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501
        if 'component_type' in params:
            query_params.append(('component_type', params['component_type']))  # noqa: E501
        if 'container_name' in params:
            query_params.append(('container_name', params['container_name']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501
        if 'follow' in params:
            query_params.append(('follow', params['follow']))  # noqa: E501
        if 'previous' in params:
            query_params.append(('previous', params['previous']))  # noqa: E501
        if 'since_seconds' in params:
            query_params.append(('since_seconds', params['since_seconds']))  # noqa: E501
        if 'since_time' in params:
            query_params.append(('since_time', params['since_time']))  # noqa: E501
        if 'timestamps' in params:
            query_params.append(('timestamps', params['timestamps']))  # noqa: E501
        if 'tail_lines' in params:
            query_params.append(('tail_lines', params['tail_lines']))  # noqa: E501
        if 'limit_bytes' in params:
            query_params.append(('limit_bytes', params['limit_bytes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
