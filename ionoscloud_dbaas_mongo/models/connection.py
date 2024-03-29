# coding: utf-8

"""
    IONOS DBaaS MongoDB REST API

    With IONOS Cloud Database as a Service, you have the ability to quickly set up and manage a MongoDB database. You can also delete clusters, manage backups and users via the API.  MongoDB is an open source, cross-platform, document-oriented database program. Classified as a NoSQL database program, it uses JSON-like documents with optional schemas.  The MongoDB API allows you to create additional database clusters or modify existing ones. Both tools, the Data Center Designer (DCD) and the API use the same concepts consistently and are well suited for smooth and intuitive use.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_mongo.configuration import Configuration


class Connection(object):
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

        'datacenter_id': 'str',

        'lan_id': 'str',

        'cidr_list': 'list[str]',
    }

    attribute_map = {

        'datacenter_id': 'datacenterId',

        'lan_id': 'lanId',

        'cidr_list': 'cidrList',
    }

    def __init__(self, datacenter_id=None, lan_id=None, cidr_list=None, local_vars_configuration=None):  # noqa: E501
        """Connection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._datacenter_id = None
        self._lan_id = None
        self._cidr_list = None
        self.discriminator = None

        self.datacenter_id = datacenter_id
        self.lan_id = lan_id
        self.cidr_list = cidr_list


    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this Connection.  # noqa: E501

        The datacenter to which your cluster will be connected.  # noqa: E501

        :return: The datacenter_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this Connection.

        The datacenter to which your cluster will be connected.  # noqa: E501

        :param datacenter_id: The datacenter_id of this Connection.  # noqa: E501
        :type datacenter_id: str
        """
        if self.local_vars_configuration.client_side_validation and datacenter_id is None:  # noqa: E501
            raise ValueError("Invalid value for `datacenter_id`, must not be `None`")  # noqa: E501

        self._datacenter_id = datacenter_id

    @property
    def lan_id(self):
        """Gets the lan_id of this Connection.  # noqa: E501

        The numeric LAN ID with which you connect your cluster.  # noqa: E501

        :return: The lan_id of this Connection.  # noqa: E501
        :rtype: str
        """
        return self._lan_id

    @lan_id.setter
    def lan_id(self, lan_id):
        """Sets the lan_id of this Connection.

        The numeric LAN ID with which you connect your cluster.  # noqa: E501

        :param lan_id: The lan_id of this Connection.  # noqa: E501
        :type lan_id: str
        """
        if self.local_vars_configuration.client_side_validation and lan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `lan_id`, must not be `None`")  # noqa: E501

        self._lan_id = lan_id

    @property
    def cidr_list(self):
        """Gets the cidr_list of this Connection.  # noqa: E501

        The list of IPs for your cluster. All IPs must be in a /24 network. Note the following unavailable IP ranges: 10.233.114.0/24   # noqa: E501

        :return: The cidr_list of this Connection.  # noqa: E501
        :rtype: list[str]
        """
        return self._cidr_list

    @cidr_list.setter
    def cidr_list(self, cidr_list):
        """Sets the cidr_list of this Connection.

        The list of IPs for your cluster. All IPs must be in a /24 network. Note the following unavailable IP ranges: 10.233.114.0/24   # noqa: E501

        :param cidr_list: The cidr_list of this Connection.  # noqa: E501
        :type cidr_list: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cidr_list is None:  # noqa: E501
            raise ValueError("Invalid value for `cidr_list`, must not be `None`")  # noqa: E501

        self._cidr_list = cidr_list
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
        if not isinstance(other, Connection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Connection):
            return True

        return self.to_dict() != other.to_dict()
