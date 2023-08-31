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

class CosmosTxV1beta1GetTxsEventResponsePagination(object):
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
        'next_key': 'str',
        'total': 'str'
    }

    attribute_map = {
        'next_key': 'next_key',
        'total': 'total'
    }

    def __init__(self, next_key=None, total=None):  # noqa: E501
        """CosmosTxV1beta1GetTxsEventResponsePagination - a model defined in Swagger"""  # noqa: E501
        self._next_key = None
        self._total = None
        self.discriminator = None
        if next_key is not None:
            self.next_key = next_key
        if total is not None:
            self.total = total

    @property
    def next_key(self):
        """Gets the next_key of this CosmosTxV1beta1GetTxsEventResponsePagination.  # noqa: E501

        next_key is the key to be passed to PageRequest.key to query the next page most efficiently. It will be empty if there are no more results.  # noqa: E501

        :return: The next_key of this CosmosTxV1beta1GetTxsEventResponsePagination.  # noqa: E501
        :rtype: str
        """
        return self._next_key

    @next_key.setter
    def next_key(self, next_key):
        """Sets the next_key of this CosmosTxV1beta1GetTxsEventResponsePagination.

        next_key is the key to be passed to PageRequest.key to query the next page most efficiently. It will be empty if there are no more results.  # noqa: E501

        :param next_key: The next_key of this CosmosTxV1beta1GetTxsEventResponsePagination.  # noqa: E501
        :type: str
        """

        self._next_key = next_key

    @property
    def total(self):
        """Gets the total of this CosmosTxV1beta1GetTxsEventResponsePagination.  # noqa: E501


        :return: The total of this CosmosTxV1beta1GetTxsEventResponsePagination.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CosmosTxV1beta1GetTxsEventResponsePagination.


        :param total: The total of this CosmosTxV1beta1GetTxsEventResponsePagination.  # noqa: E501
        :type: str
        """

        self._total = total

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
        if issubclass(CosmosTxV1beta1GetTxsEventResponsePagination, dict):
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
        if not isinstance(other, CosmosTxV1beta1GetTxsEventResponsePagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other