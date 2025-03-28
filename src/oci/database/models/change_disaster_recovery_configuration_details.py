# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeDisasterRecoveryConfigurationDetails(object):
    """
    Details to update the cross-region Disaster Recovery (DR) details of the Standby Autonomous Database on shared Exadata infrastructure.
    """

    #: A constant which can be used with the disaster_recovery_type property of a ChangeDisasterRecoveryConfigurationDetails.
    #: This constant has a value of "ADG"
    DISASTER_RECOVERY_TYPE_ADG = "ADG"

    #: A constant which can be used with the disaster_recovery_type property of a ChangeDisasterRecoveryConfigurationDetails.
    #: This constant has a value of "BACKUP_BASED"
    DISASTER_RECOVERY_TYPE_BACKUP_BASED = "BACKUP_BASED"

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeDisasterRecoveryConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disaster_recovery_type:
            The value to assign to the disaster_recovery_type property of this ChangeDisasterRecoveryConfigurationDetails.
            Allowed values for this property are: "ADG", "BACKUP_BASED"
        :type disaster_recovery_type: str

        """
        self.swagger_types = {
            'disaster_recovery_type': 'str'
        }

        self.attribute_map = {
            'disaster_recovery_type': 'disasterRecoveryType'
        }

        self._disaster_recovery_type = None

    @property
    def disaster_recovery_type(self):
        """
        Gets the disaster_recovery_type of this ChangeDisasterRecoveryConfigurationDetails.
        Indicates the disaster recovery (DR) type of the Shared Autonomous Database.
        Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
        Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

        Allowed values for this property are: "ADG", "BACKUP_BASED"


        :return: The disaster_recovery_type of this ChangeDisasterRecoveryConfigurationDetails.
        :rtype: str
        """
        return self._disaster_recovery_type

    @disaster_recovery_type.setter
    def disaster_recovery_type(self, disaster_recovery_type):
        """
        Sets the disaster_recovery_type of this ChangeDisasterRecoveryConfigurationDetails.
        Indicates the disaster recovery (DR) type of the Shared Autonomous Database.
        Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
        Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.


        :param disaster_recovery_type: The disaster_recovery_type of this ChangeDisasterRecoveryConfigurationDetails.
        :type: str
        """
        allowed_values = ["ADG", "BACKUP_BASED"]
        if not value_allowed_none_or_none_sentinel(disaster_recovery_type, allowed_values):
            raise ValueError(
                "Invalid value for `disaster_recovery_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._disaster_recovery_type = disaster_recovery_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
