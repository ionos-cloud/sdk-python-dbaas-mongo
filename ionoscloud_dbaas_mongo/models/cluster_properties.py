# coding: utf-8

"""
    IONOS DBaaS MongoDB REST API

    With IONOS Cloud Database as a Service, you have the ability to quickly set up and manage a MongoDB database. You can also delete clusters, manage backups and users via the API.   MongoDB is an open source, cross-platform, document-oriented database program. Classified as a NoSQL database program, it uses JSON-like documents with optional schemas.  The MongoDB API allows you to create additional database clusters or modify existing ones. Both tools, the Data Center Designer (DCD) and the API use the same concepts consistently and are well suited for smooth and intuitive use.   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_mongo.configuration import Configuration


class ClusterProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {

        'display_name': 'str',

        'mongo_db_version': 'str',

        'location': 'str',

        'instances': 'int',

        'connections': 'list[Connection]',

        'maintenance_window': 'MaintenanceWindow',

        'template_id': 'str',

        'connection_string': 'str',
    }

    attribute_map = {

        'display_name': 'displayName',

        'mongo_db_version': 'mongoDBVersion',

        'location': 'location',

        'instances': 'instances',

        'connections': 'connections',

        'maintenance_window': 'maintenanceWindow',

        'template_id': 'templateID',

        'connection_string': 'connectionString',
    }

    def __init__(self, display_name=None, mongo_db_version=None, location=None, instances=None, connections=None, maintenance_window=None, template_id=None, connection_string=None, local_vars_configuration=None):  # noqa: E501
        """ClusterProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._mongo_db_version = None
        self._location = None
        self._instances = None
        self._connections = None
        self._maintenance_window = None
        self._template_id = None
        self._connection_string = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if mongo_db_version is not None:
            self.mongo_db_version = mongo_db_version
        if location is not None:
            self.location = location
        if instances is not None:
            self.instances = instances
        if connections is not None:
            self.connections = connections
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if template_id is not None:
            self.template_id = template_id
        if connection_string is not None:
            self.connection_string = connection_string


    @property
    def display_name(self):
        """Gets the display_name of this ClusterProperties.  # noqa: E501

        The name of your cluster.  # noqa: E501

        :return: The display_name of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ClusterProperties.

        The name of your cluster.  # noqa: E501

        :param display_name: The display_name of this ClusterProperties.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def mongo_db_version(self):
        """Gets the mongo_db_version of this ClusterProperties.  # noqa: E501

        The MongoDB version of your cluster.  # noqa: E501

        :return: The mongo_db_version of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._mongo_db_version

    @mongo_db_version.setter
    def mongo_db_version(self, mongo_db_version):
        """Sets the mongo_db_version of this ClusterProperties.

        The MongoDB version of your cluster.  # noqa: E501

        :param mongo_db_version: The mongo_db_version of this ClusterProperties.  # noqa: E501
        :type mongo_db_version: str
        """

        self._mongo_db_version = mongo_db_version

    @property
    def location(self):
        """Gets the location of this ClusterProperties.  # noqa: E501

        The physical location where the cluster will be created. This is the location where all your instances will be located. This property is immutable.   # noqa: E501

        :return: The location of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ClusterProperties.

        The physical location where the cluster will be created. This is the location where all your instances will be located. This property is immutable.   # noqa: E501

        :param location: The location of this ClusterProperties.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def instances(self):
        """Gets the instances of this ClusterProperties.  # noqa: E501

        The total number of instances in the cluster (one primary and n-1 secondaries).   # noqa: E501

        :return: The instances of this ClusterProperties.  # noqa: E501
        :rtype: int
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ClusterProperties.

        The total number of instances in the cluster (one primary and n-1 secondaries).   # noqa: E501

        :param instances: The instances of this ClusterProperties.  # noqa: E501
        :type instances: int
        """

        self._instances = instances

    @property
    def connections(self):
        """Gets the connections of this ClusterProperties.  # noqa: E501


        :return: The connections of this ClusterProperties.  # noqa: E501
        :rtype: list[Connection]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ClusterProperties.


        :param connections: The connections of this ClusterProperties.  # noqa: E501
        :type connections: list[Connection]
        """
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) > 1):
            raise ValueError("Invalid value for `connections`, number of items must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connections is not None and len(connections) < 1):
            raise ValueError("Invalid value for `connections`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._connections = connections

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this ClusterProperties.  # noqa: E501


        :return: The maintenance_window of this ClusterProperties.  # noqa: E501
        :rtype: MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this ClusterProperties.


        :param maintenance_window: The maintenance_window of this ClusterProperties.  # noqa: E501
        :type maintenance_window: MaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def template_id(self):
        """Gets the template_id of this ClusterProperties.  # noqa: E501

        The unique ID of the template, which specifies the number of cores, storage size, and memory.   # noqa: E501

        :return: The template_id of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ClusterProperties.

        The unique ID of the template, which specifies the number of cores, storage size, and memory.   # noqa: E501

        :param template_id: The template_id of this ClusterProperties.  # noqa: E501
        :type template_id: str
        """

        self._template_id = template_id

    @property
    def connection_string(self):
        """Gets the connection_string of this ClusterProperties.  # noqa: E501

        The connection string for your cluster.  # noqa: E501

        :return: The connection_string of this ClusterProperties.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this ClusterProperties.

        The connection string for your cluster.  # noqa: E501

        :param connection_string: The connection_string of this ClusterProperties.  # noqa: E501
        :type connection_string: str
        """

        self._connection_string = connection_string
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterProperties):
            return True

        return self.to_dict() != other.to_dict()
