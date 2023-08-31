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

class CosmosBaseQueryV1beta1PageRequest(object):
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
        'key': 'str',
        'offset': 'str',
        'limit': 'str',
        'count_total': 'bool',
        'reverse': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'offset': 'offset',
        'limit': 'limit',
        'count_total': 'count_total',
        'reverse': 'reverse'
    }

    def __init__(self, key=None, offset=None, limit=None, count_total=None, reverse=None):  # noqa: E501
        """CosmosBaseQueryV1beta1PageRequest - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._offset = None
        self._limit = None
        self._count_total = None
        self._reverse = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if count_total is not None:
            self.count_total = count_total
        if reverse is not None:
            self.reverse = reverse

    @property
    def key(self):
        """Gets the key of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501

        key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set.  # noqa: E501

        :return: The key of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CosmosBaseQueryV1beta1PageRequest.

        key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set.  # noqa: E501

        :param key: The key of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def offset(self):
        """Gets the offset of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501

        offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set.  # noqa: E501

        :return: The offset of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CosmosBaseQueryV1beta1PageRequest.

        offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set.  # noqa: E501

        :param offset: The offset of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :type: str
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501

        limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app.  # noqa: E501

        :return: The limit of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CosmosBaseQueryV1beta1PageRequest.

        limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app.  # noqa: E501

        :param limit: The limit of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :type: str
        """

        self._limit = limit

    @property
    def count_total(self):
        """Gets the count_total of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501

        count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set.  # noqa: E501

        :return: The count_total of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :rtype: bool
        """
        return self._count_total

    @count_total.setter
    def count_total(self, count_total):
        """Sets the count_total of this CosmosBaseQueryV1beta1PageRequest.

        count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set.  # noqa: E501

        :param count_total: The count_total of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :type: bool
        """

        self._count_total = count_total

    @property
    def reverse(self):
        """Gets the reverse of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501

        reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43  # noqa: E501

        :return: The reverse of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reverse

    @reverse.setter
    def reverse(self, reverse):
        """Sets the reverse of this CosmosBaseQueryV1beta1PageRequest.

        reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43  # noqa: E501

        :param reverse: The reverse of this CosmosBaseQueryV1beta1PageRequest.  # noqa: E501
        :type: bool
        """

        self._reverse = reverse

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
        if issubclass(CosmosBaseQueryV1beta1PageRequest, dict):
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
        if not isinstance(other, CosmosBaseQueryV1beta1PageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other