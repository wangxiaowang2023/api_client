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

class InlineResponse20071(object):
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
        'kyc': 'CosmosStakingV1beta1QueryAllKycResponseKyc'
    }

    attribute_map = {
        'kyc': 'kyc'
    }

    def __init__(self, kyc=None):  # noqa: E501
        """InlineResponse20071 - a model defined in Swagger"""  # noqa: E501
        self._kyc = None
        self.discriminator = None
        if kyc is not None:
            self.kyc = kyc

    @property
    def kyc(self):
        """Gets the kyc of this InlineResponse20071.  # noqa: E501


        :return: The kyc of this InlineResponse20071.  # noqa: E501
        :rtype: CosmosStakingV1beta1QueryAllKycResponseKyc
        """
        return self._kyc

    @kyc.setter
    def kyc(self, kyc):
        """Sets the kyc of this InlineResponse20071.


        :param kyc: The kyc of this InlineResponse20071.  # noqa: E501
        :type: CosmosStakingV1beta1QueryAllKycResponseKyc
        """

        self._kyc = kyc

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
        if issubclass(InlineResponse20071, dict):
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
        if not isinstance(other, InlineResponse20071):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
