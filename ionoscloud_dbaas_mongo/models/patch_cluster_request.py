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


class PatchClusterRequest(object):
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

        'metadata': 'Metadata',

        'properties': 'PatchClusterProperties',
    }

    attribute_map = {

        'metadata': 'metadata',

        'properties': 'properties',
    }

    def __init__(self, metadata=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """PatchClusterRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self._properties = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if properties is not None:
            self.properties = properties


    @property
    def metadata(self):
        """Gets the metadata of this PatchClusterRequest.  # noqa: E501


        :return: The metadata of this PatchClusterRequest.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PatchClusterRequest.


        :param metadata: The metadata of this PatchClusterRequest.  # noqa: E501
        :type metadata: Metadata
        """

        self._metadata = metadata

    @property
    def properties(self):
        """Gets the properties of this PatchClusterRequest.  # noqa: E501


        :return: The properties of this PatchClusterRequest.  # noqa: E501
        :rtype: PatchClusterProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PatchClusterRequest.


        :param properties: The properties of this PatchClusterRequest.  # noqa: E501
        :type properties: PatchClusterProperties
        """

        self._properties = properties
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
        if not isinstance(other, PatchClusterRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchClusterRequest):
            return True

        return self.to_dict() != other.to_dict()
