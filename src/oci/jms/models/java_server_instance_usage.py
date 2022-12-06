# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaServerInstanceUsage(object):
    """
    Java Server instance usage during a specified time period.
    """

    #: A constant which can be used with the jvm_security_status property of a JavaServerInstanceUsage.
    #: This constant has a value of "UNKNOWN"
    JVM_SECURITY_STATUS_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the jvm_security_status property of a JavaServerInstanceUsage.
    #: This constant has a value of "UP_TO_DATE"
    JVM_SECURITY_STATUS_UP_TO_DATE = "UP_TO_DATE"

    #: A constant which can be used with the jvm_security_status property of a JavaServerInstanceUsage.
    #: This constant has a value of "UPDATE_REQUIRED"
    JVM_SECURITY_STATUS_UPDATE_REQUIRED = "UPDATE_REQUIRED"

    #: A constant which can be used with the jvm_security_status property of a JavaServerInstanceUsage.
    #: This constant has a value of "UPGRADE_REQUIRED"
    JVM_SECURITY_STATUS_UPGRADE_REQUIRED = "UPGRADE_REQUIRED"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaServerInstanceUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param server_instance_key:
            The value to assign to the server_instance_key property of this JavaServerInstanceUsage.
        :type server_instance_key: str

        :param fleet_id:
            The value to assign to the fleet_id property of this JavaServerInstanceUsage.
        :type fleet_id: str

        :param server_instance_name:
            The value to assign to the server_instance_name property of this JavaServerInstanceUsage.
        :type server_instance_name: str

        :param server_key:
            The value to assign to the server_key property of this JavaServerInstanceUsage.
        :type server_key: str

        :param server_name:
            The value to assign to the server_name property of this JavaServerInstanceUsage.
        :type server_name: str

        :param server_version:
            The value to assign to the server_version property of this JavaServerInstanceUsage.
        :type server_version: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this JavaServerInstanceUsage.
        :type managed_instance_id: str

        :param host_name:
            The value to assign to the host_name property of this JavaServerInstanceUsage.
        :type host_name: str

        :param jvm_key:
            The value to assign to the jvm_key property of this JavaServerInstanceUsage.
        :type jvm_key: str

        :param jvm_vendor:
            The value to assign to the jvm_vendor property of this JavaServerInstanceUsage.
        :type jvm_vendor: str

        :param jvm_distribution:
            The value to assign to the jvm_distribution property of this JavaServerInstanceUsage.
        :type jvm_distribution: str

        :param jvm_version:
            The value to assign to the jvm_version property of this JavaServerInstanceUsage.
        :type jvm_version: str

        :param jvm_security_status:
            The value to assign to the jvm_security_status property of this JavaServerInstanceUsage.
            Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type jvm_security_status: str

        :param approximate_deployed_application_count:
            The value to assign to the approximate_deployed_application_count property of this JavaServerInstanceUsage.
        :type approximate_deployed_application_count: int

        :param time_start:
            The value to assign to the time_start property of this JavaServerInstanceUsage.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this JavaServerInstanceUsage.
        :type time_end: datetime

        :param time_first_seen:
            The value to assign to the time_first_seen property of this JavaServerInstanceUsage.
        :type time_first_seen: datetime

        :param time_last_seen:
            The value to assign to the time_last_seen property of this JavaServerInstanceUsage.
        :type time_last_seen: datetime

        """
        self.swagger_types = {
            'server_instance_key': 'str',
            'fleet_id': 'str',
            'server_instance_name': 'str',
            'server_key': 'str',
            'server_name': 'str',
            'server_version': 'str',
            'managed_instance_id': 'str',
            'host_name': 'str',
            'jvm_key': 'str',
            'jvm_vendor': 'str',
            'jvm_distribution': 'str',
            'jvm_version': 'str',
            'jvm_security_status': 'str',
            'approximate_deployed_application_count': 'int',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'time_first_seen': 'datetime',
            'time_last_seen': 'datetime'
        }

        self.attribute_map = {
            'server_instance_key': 'serverInstanceKey',
            'fleet_id': 'fleetId',
            'server_instance_name': 'serverInstanceName',
            'server_key': 'serverKey',
            'server_name': 'serverName',
            'server_version': 'serverVersion',
            'managed_instance_id': 'managedInstanceId',
            'host_name': 'hostName',
            'jvm_key': 'jvmKey',
            'jvm_vendor': 'jvmVendor',
            'jvm_distribution': 'jvmDistribution',
            'jvm_version': 'jvmVersion',
            'jvm_security_status': 'jvmSecurityStatus',
            'approximate_deployed_application_count': 'approximateDeployedApplicationCount',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'time_first_seen': 'timeFirstSeen',
            'time_last_seen': 'timeLastSeen'
        }

        self._server_instance_key = None
        self._fleet_id = None
        self._server_instance_name = None
        self._server_key = None
        self._server_name = None
        self._server_version = None
        self._managed_instance_id = None
        self._host_name = None
        self._jvm_key = None
        self._jvm_vendor = None
        self._jvm_distribution = None
        self._jvm_version = None
        self._jvm_security_status = None
        self._approximate_deployed_application_count = None
        self._time_start = None
        self._time_end = None
        self._time_first_seen = None
        self._time_last_seen = None

    @property
    def server_instance_key(self):
        """
        **[Required]** Gets the server_instance_key of this JavaServerInstanceUsage.
        The internal identifier of the Java Server instance.


        :return: The server_instance_key of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._server_instance_key

    @server_instance_key.setter
    def server_instance_key(self, server_instance_key):
        """
        Sets the server_instance_key of this JavaServerInstanceUsage.
        The internal identifier of the Java Server instance.


        :param server_instance_key: The server_instance_key of this JavaServerInstanceUsage.
        :type: str
        """
        self._server_instance_key = server_instance_key

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this JavaServerInstanceUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this JavaServerInstanceUsage.
        The `OCID`__ of the related fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this JavaServerInstanceUsage.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def server_instance_name(self):
        """
        **[Required]** Gets the server_instance_name of this JavaServerInstanceUsage.
        The name of the Java Server instance.


        :return: The server_instance_name of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._server_instance_name

    @server_instance_name.setter
    def server_instance_name(self, server_instance_name):
        """
        Sets the server_instance_name of this JavaServerInstanceUsage.
        The name of the Java Server instance.


        :param server_instance_name: The server_instance_name of this JavaServerInstanceUsage.
        :type: str
        """
        self._server_instance_name = server_instance_name

    @property
    def server_key(self):
        """
        **[Required]** Gets the server_key of this JavaServerInstanceUsage.
        The internal identifier of the related Java Server.


        :return: The server_key of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._server_key

    @server_key.setter
    def server_key(self, server_key):
        """
        Sets the server_key of this JavaServerInstanceUsage.
        The internal identifier of the related Java Server.


        :param server_key: The server_key of this JavaServerInstanceUsage.
        :type: str
        """
        self._server_key = server_key

    @property
    def server_name(self):
        """
        Gets the server_name of this JavaServerInstanceUsage.
        The name of the Java Server.


        :return: The server_name of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """
        Sets the server_name of this JavaServerInstanceUsage.
        The name of the Java Server.


        :param server_name: The server_name of this JavaServerInstanceUsage.
        :type: str
        """
        self._server_name = server_name

    @property
    def server_version(self):
        """
        Gets the server_version of this JavaServerInstanceUsage.
        The version of the Java Server.


        :return: The server_version of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._server_version

    @server_version.setter
    def server_version(self, server_version):
        """
        Sets the server_version of this JavaServerInstanceUsage.
        The version of the Java Server.


        :param server_version: The server_version of this JavaServerInstanceUsage.
        :type: str
        """
        self._server_version = server_version

    @property
    def managed_instance_id(self):
        """
        **[Required]** Gets the managed_instance_id of this JavaServerInstanceUsage.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_id of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this JavaServerInstanceUsage.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_id: The managed_instance_id of this JavaServerInstanceUsage.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def host_name(self):
        """
        Gets the host_name of this JavaServerInstanceUsage.
        The host name of the related managed instance.


        :return: The host_name of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this JavaServerInstanceUsage.
        The host name of the related managed instance.


        :param host_name: The host_name of this JavaServerInstanceUsage.
        :type: str
        """
        self._host_name = host_name

    @property
    def jvm_key(self):
        """
        Gets the jvm_key of this JavaServerInstanceUsage.
        The internal identifier of the related Java Runtime.


        :return: The jvm_key of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._jvm_key

    @jvm_key.setter
    def jvm_key(self, jvm_key):
        """
        Sets the jvm_key of this JavaServerInstanceUsage.
        The internal identifier of the related Java Runtime.


        :param jvm_key: The jvm_key of this JavaServerInstanceUsage.
        :type: str
        """
        self._jvm_key = jvm_key

    @property
    def jvm_vendor(self):
        """
        Gets the jvm_vendor of this JavaServerInstanceUsage.
        The vendor of the Java Runtime.


        :return: The jvm_vendor of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._jvm_vendor

    @jvm_vendor.setter
    def jvm_vendor(self, jvm_vendor):
        """
        Sets the jvm_vendor of this JavaServerInstanceUsage.
        The vendor of the Java Runtime.


        :param jvm_vendor: The jvm_vendor of this JavaServerInstanceUsage.
        :type: str
        """
        self._jvm_vendor = jvm_vendor

    @property
    def jvm_distribution(self):
        """
        Gets the jvm_distribution of this JavaServerInstanceUsage.
        The distribution of the Java Runtime.


        :return: The jvm_distribution of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._jvm_distribution

    @jvm_distribution.setter
    def jvm_distribution(self, jvm_distribution):
        """
        Sets the jvm_distribution of this JavaServerInstanceUsage.
        The distribution of the Java Runtime.


        :param jvm_distribution: The jvm_distribution of this JavaServerInstanceUsage.
        :type: str
        """
        self._jvm_distribution = jvm_distribution

    @property
    def jvm_version(self):
        """
        Gets the jvm_version of this JavaServerInstanceUsage.
        The version of the Java Runtime.


        :return: The jvm_version of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._jvm_version

    @jvm_version.setter
    def jvm_version(self, jvm_version):
        """
        Sets the jvm_version of this JavaServerInstanceUsage.
        The version of the Java Runtime.


        :param jvm_version: The jvm_version of this JavaServerInstanceUsage.
        :type: str
        """
        self._jvm_version = jvm_version

    @property
    def jvm_security_status(self):
        """
        Gets the jvm_security_status of this JavaServerInstanceUsage.
        The security status of the Java Runtime.

        Allowed values for this property are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The jvm_security_status of this JavaServerInstanceUsage.
        :rtype: str
        """
        return self._jvm_security_status

    @jvm_security_status.setter
    def jvm_security_status(self, jvm_security_status):
        """
        Sets the jvm_security_status of this JavaServerInstanceUsage.
        The security status of the Java Runtime.


        :param jvm_security_status: The jvm_security_status of this JavaServerInstanceUsage.
        :type: str
        """
        allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
        if not value_allowed_none_or_none_sentinel(jvm_security_status, allowed_values):
            jvm_security_status = 'UNKNOWN_ENUM_VALUE'
        self._jvm_security_status = jvm_security_status

    @property
    def approximate_deployed_application_count(self):
        """
        Gets the approximate_deployed_application_count of this JavaServerInstanceUsage.
        The approximate count of deployed applications in the Java Server instance.


        :return: The approximate_deployed_application_count of this JavaServerInstanceUsage.
        :rtype: int
        """
        return self._approximate_deployed_application_count

    @approximate_deployed_application_count.setter
    def approximate_deployed_application_count(self, approximate_deployed_application_count):
        """
        Sets the approximate_deployed_application_count of this JavaServerInstanceUsage.
        The approximate count of deployed applications in the Java Server instance.


        :param approximate_deployed_application_count: The approximate_deployed_application_count of this JavaServerInstanceUsage.
        :type: int
        """
        self._approximate_deployed_application_count = approximate_deployed_application_count

    @property
    def time_start(self):
        """
        Gets the time_start of this JavaServerInstanceUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_start of this JavaServerInstanceUsage.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this JavaServerInstanceUsage.
        Lower bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_start: The time_start of this JavaServerInstanceUsage.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this JavaServerInstanceUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :return: The time_end of this JavaServerInstanceUsage.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this JavaServerInstanceUsage.
        Upper bound of the specified time period filter. JMS provides a view of the data that is _per day_. The query uses only the date element of the parameter.


        :param time_end: The time_end of this JavaServerInstanceUsage.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def time_first_seen(self):
        """
        Gets the time_first_seen of this JavaServerInstanceUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_first_seen of this JavaServerInstanceUsage.
        :rtype: datetime
        """
        return self._time_first_seen

    @time_first_seen.setter
    def time_first_seen(self, time_first_seen):
        """
        Sets the time_first_seen of this JavaServerInstanceUsage.
        The date and time the resource was _first_ reported to JMS.
        This is potentially _before_ the specified time period provided by the filters.
        For example, a resource can be first reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_first_seen: The time_first_seen of this JavaServerInstanceUsage.
        :type: datetime
        """
        self._time_first_seen = time_first_seen

    @property
    def time_last_seen(self):
        """
        Gets the time_last_seen of this JavaServerInstanceUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :return: The time_last_seen of this JavaServerInstanceUsage.
        :rtype: datetime
        """
        return self._time_last_seen

    @time_last_seen.setter
    def time_last_seen(self, time_last_seen):
        """
        Sets the time_last_seen of this JavaServerInstanceUsage.
        The date and time the resource was _last_ reported to JMS.
        This is potentially _after_ the specified time period provided by the filters.
        For example, a resource can be last reported to JMS before the start of a specified time period,
        if it is also reported during the time period.


        :param time_last_seen: The time_last_seen of this JavaServerInstanceUsage.
        :type: datetime
        """
        self._time_last_seen = time_last_seen

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
