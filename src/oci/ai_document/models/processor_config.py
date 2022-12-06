# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProcessorConfig(object):
    """
    The configuration of a processor.
    """

    #: A constant which can be used with the processor_type property of a ProcessorConfig.
    #: This constant has a value of "GENERAL"
    PROCESSOR_TYPE_GENERAL = "GENERAL"

    def __init__(self, **kwargs):
        """
        Initializes a new ProcessorConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_document.models.GeneralProcessorConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param processor_type:
            The value to assign to the processor_type property of this ProcessorConfig.
            Allowed values for this property are: "GENERAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type processor_type: str

        """
        self.swagger_types = {
            'processor_type': 'str'
        }

        self.attribute_map = {
            'processor_type': 'processorType'
        }

        self._processor_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['processorType']

        if type == 'GENERAL':
            return 'GeneralProcessorConfig'
        else:
            return 'ProcessorConfig'

    @property
    def processor_type(self):
        """
        **[Required]** Gets the processor_type of this ProcessorConfig.
        The type of the processor.

        Allowed values for this property are: "GENERAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The processor_type of this ProcessorConfig.
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        """
        Sets the processor_type of this ProcessorConfig.
        The type of the processor.


        :param processor_type: The processor_type of this ProcessorConfig.
        :type: str
        """
        allowed_values = ["GENERAL"]
        if not value_allowed_none_or_none_sentinel(processor_type, allowed_values):
            processor_type = 'UNKNOWN_ENUM_VALUE'
        self._processor_type = processor_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
