# coding: utf-8

"""
    HTTP API Console

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20060(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'inflation': 'str'
    }

    attribute_map = {
        'inflation': 'inflation'
    }

    def __init__(self, inflation=None):  # noqa: E501
        """InlineResponse20060 - a model defined in Swagger"""  # noqa: E501
        self._inflation = None
        self.discriminator = None
        if inflation is not None:
            self.inflation = inflation

    @property
    def inflation(self):
        """Gets the inflation of this InlineResponse20060.  # noqa: E501

        inflation is the current minting inflation value.  # noqa: E501

        :return: The inflation of this InlineResponse20060.  # noqa: E501
        :rtype: str
        """
        return self._inflation

    @inflation.setter
    def inflation(self, inflation):
        """Sets the inflation of this InlineResponse20060.

        inflation is the current minting inflation value.  # noqa: E501

        :param inflation: The inflation of this InlineResponse20060.  # noqa: E501
        :type: str
        """

        self._inflation = inflation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse20060, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20060):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
