# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkChannel(object):
    """
    Specifies the configuration needed when the target OCI resource, i.e., OKE cluster, resides
    in customer's private network.
    """

    #: A constant which can be used with the network_channel_type property of a NetworkChannel.
    #: This constant has a value of "PRIVATE_ENDPOINT_CHANNEL"
    NETWORK_CHANNEL_TYPE_PRIVATE_ENDPOINT_CHANNEL = "PRIVATE_ENDPOINT_CHANNEL"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkChannel object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.PrivateEndpointChannel`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_channel_type:
            The value to assign to the network_channel_type property of this NetworkChannel.
            Allowed values for this property are: "PRIVATE_ENDPOINT_CHANNEL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_channel_type: str

        """
        self.swagger_types = {
            'network_channel_type': 'str'
        }

        self.attribute_map = {
            'network_channel_type': 'networkChannelType'
        }

        self._network_channel_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['networkChannelType']

        if type == 'PRIVATE_ENDPOINT_CHANNEL':
            return 'PrivateEndpointChannel'
        else:
            return 'NetworkChannel'

    @property
    def network_channel_type(self):
        """
        **[Required]** Gets the network_channel_type of this NetworkChannel.
        Network channel type.

        Allowed values for this property are: "PRIVATE_ENDPOINT_CHANNEL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_channel_type of this NetworkChannel.
        :rtype: str
        """
        return self._network_channel_type

    @network_channel_type.setter
    def network_channel_type(self, network_channel_type):
        """
        Sets the network_channel_type of this NetworkChannel.
        Network channel type.


        :param network_channel_type: The network_channel_type of this NetworkChannel.
        :type: str
        """
        allowed_values = ["PRIVATE_ENDPOINT_CHANNEL"]
        if not value_allowed_none_or_none_sentinel(network_channel_type, allowed_values):
            network_channel_type = 'UNKNOWN_ENUM_VALUE'
        self._network_channel_type = network_channel_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
