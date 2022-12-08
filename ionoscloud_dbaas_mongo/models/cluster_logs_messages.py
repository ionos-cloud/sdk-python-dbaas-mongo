# coding: utf-8

"""
    IONOS DBaaS MongoDB REST API

    With IONOS Cloud Database as a Service, you have the ability to quickly set up and manage a MongoDB database. You can also delete clusters, manage backups and users via the API.   MongoDB is an open source, cross-platform, document-oriented database program. Classified as a NoSQL database program, it uses JSON-like documents with optional schemas.  The MongoDB API allows you to create additional database clusters or modify existing ones. Both tools, the Data Center Designer (DCD) and the API use the same concepts consistently and are well suited for smooth and intuitive use.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dbaas_mongo.configuration import Configuration


class ClusterLogsMessages(object):
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

        'time': 'datetime',

        'message': 'str',
    }

    attribute_map = {

        'time': 'time',

        'message': 'message',
    }

    def __init__(self, time=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ClusterLogsMessages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._message = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if message is not None:
            self.message = message


    @property
    def time(self):
        """Gets the time of this ClusterLogsMessages.  # noqa: E501


        :return: The time of this ClusterLogsMessages.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ClusterLogsMessages.


        :param time: The time of this ClusterLogsMessages.  # noqa: E501
        :type time: datetime
        """

        self._time = time

    @property
    def message(self):
        """Gets the message of this ClusterLogsMessages.  # noqa: E501


        :return: The message of this ClusterLogsMessages.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ClusterLogsMessages.


        :param message: The message of this ClusterLogsMessages.  # noqa: E501
        :type message: str
        """

        self._message = message
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
        if not isinstance(other, ClusterLogsMessages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterLogsMessages):
            return True

        return self.to_dict() != other.to_dict()
