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


class SnapshotListAllOf(object):
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

        'type': 'ResourceType',

        'id': 'str',

        'items': 'list[SnapshotResponse]',
    }

    attribute_map = {

        'type': 'type',

        'id': 'id',

        'items': 'items',
    }

    def __init__(self, type=None, id=None, items=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotListAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._items = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if items is not None:
            self.items = items


    @property
    def type(self):
        """Gets the type of this SnapshotListAllOf.  # noqa: E501


        :return: The type of this SnapshotListAllOf.  # noqa: E501
        :rtype: ResourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SnapshotListAllOf.


        :param type: The type of this SnapshotListAllOf.  # noqa: E501
        :type type: ResourceType
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this SnapshotListAllOf.  # noqa: E501

        The unique ID of the resource.  # noqa: E501

        :return: The id of this SnapshotListAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotListAllOf.

        The unique ID of the resource.  # noqa: E501

        :param id: The id of this SnapshotListAllOf.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def items(self):
        """Gets the items of this SnapshotListAllOf.  # noqa: E501


        :return: The items of this SnapshotListAllOf.  # noqa: E501
        :rtype: list[SnapshotResponse]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SnapshotListAllOf.


        :param items: The items of this SnapshotListAllOf.  # noqa: E501
        :type items: list[SnapshotResponse]
        """

        self._items = items
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
        if not isinstance(other, SnapshotListAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotListAllOf):
            return True

        return self.to_dict() != other.to_dict()
