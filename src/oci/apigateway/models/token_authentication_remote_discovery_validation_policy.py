# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .token_authentication_validation_policy import TokenAuthenticationValidationPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TokenAuthenticationRemoteDiscoveryValidationPolicy(TokenAuthenticationValidationPolicy):
    """
    Instrospect Url based validation retrieved at run-time from a remote location
    to verify the provided token.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TokenAuthenticationRemoteDiscoveryValidationPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.TokenAuthenticationRemoteDiscoveryValidationPolicy.type` attribute
        of this class is ``REMOTE_DISCOVERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
            Allowed values for this property are: "STATIC_KEYS", "REMOTE_JWKS", "REMOTE_DISCOVERY"
        :type type: str

        :param additional_validation_policy:
            The value to assign to the additional_validation_policy property of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type additional_validation_policy: oci.apigateway.models.AdditionalValidationPolicy

        :param client_details:
            The value to assign to the client_details property of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type client_details: oci.apigateway.models.ClientAppDetails

        :param source_uri_details:
            The value to assign to the source_uri_details property of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type source_uri_details: oci.apigateway.models.SourceUriDetails

        :param is_ssl_verify_disabled:
            The value to assign to the is_ssl_verify_disabled property of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type is_ssl_verify_disabled: bool

        :param max_cache_duration_in_hours:
            The value to assign to the max_cache_duration_in_hours property of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type max_cache_duration_in_hours: int

        """
        self.swagger_types = {
            'type': 'str',
            'additional_validation_policy': 'AdditionalValidationPolicy',
            'client_details': 'ClientAppDetails',
            'source_uri_details': 'SourceUriDetails',
            'is_ssl_verify_disabled': 'bool',
            'max_cache_duration_in_hours': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'additional_validation_policy': 'additionalValidationPolicy',
            'client_details': 'clientDetails',
            'source_uri_details': 'sourceUriDetails',
            'is_ssl_verify_disabled': 'isSslVerifyDisabled',
            'max_cache_duration_in_hours': 'maxCacheDurationInHours'
        }

        self._type = None
        self._additional_validation_policy = None
        self._client_details = None
        self._source_uri_details = None
        self._is_ssl_verify_disabled = None
        self._max_cache_duration_in_hours = None
        self._type = 'REMOTE_DISCOVERY'

    @property
    def client_details(self):
        """
        **[Required]** Gets the client_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.

        :return: The client_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :rtype: oci.apigateway.models.ClientAppDetails
        """
        return self._client_details

    @client_details.setter
    def client_details(self, client_details):
        """
        Sets the client_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.

        :param client_details: The client_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type: oci.apigateway.models.ClientAppDetails
        """
        self._client_details = client_details

    @property
    def source_uri_details(self):
        """
        **[Required]** Gets the source_uri_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.

        :return: The source_uri_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :rtype: oci.apigateway.models.SourceUriDetails
        """
        return self._source_uri_details

    @source_uri_details.setter
    def source_uri_details(self, source_uri_details):
        """
        Sets the source_uri_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.

        :param source_uri_details: The source_uri_details of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type: oci.apigateway.models.SourceUriDetails
        """
        self._source_uri_details = source_uri_details

    @property
    def is_ssl_verify_disabled(self):
        """
        Gets the is_ssl_verify_disabled of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        Defines whether or not to uphold SSL verification.


        :return: The is_ssl_verify_disabled of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :rtype: bool
        """
        return self._is_ssl_verify_disabled

    @is_ssl_verify_disabled.setter
    def is_ssl_verify_disabled(self, is_ssl_verify_disabled):
        """
        Sets the is_ssl_verify_disabled of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        Defines whether or not to uphold SSL verification.


        :param is_ssl_verify_disabled: The is_ssl_verify_disabled of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type: bool
        """
        self._is_ssl_verify_disabled = is_ssl_verify_disabled

    @property
    def max_cache_duration_in_hours(self):
        """
        Gets the max_cache_duration_in_hours of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        The duration for which the introspect URL response should be cached before it is
        fetched again.


        :return: The max_cache_duration_in_hours of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :rtype: int
        """
        return self._max_cache_duration_in_hours

    @max_cache_duration_in_hours.setter
    def max_cache_duration_in_hours(self, max_cache_duration_in_hours):
        """
        Sets the max_cache_duration_in_hours of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        The duration for which the introspect URL response should be cached before it is
        fetched again.


        :param max_cache_duration_in_hours: The max_cache_duration_in_hours of this TokenAuthenticationRemoteDiscoveryValidationPolicy.
        :type: int
        """
        self._max_cache_duration_in_hours = max_cache_duration_in_hours

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
