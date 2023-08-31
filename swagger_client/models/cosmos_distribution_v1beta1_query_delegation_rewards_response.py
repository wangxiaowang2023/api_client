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

class CosmosDistributionV1beta1QueryDelegationRewardsResponse(object):
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
        'rewards': 'list[CosmosDistributionV1beta1QueryDelegationRewardsResponseRewards]'
    }

    attribute_map = {
        'rewards': 'rewards'
    }

    def __init__(self, rewards=None):  # noqa: E501
        """CosmosDistributionV1beta1QueryDelegationRewardsResponse - a model defined in Swagger"""  # noqa: E501
        self._rewards = None
        self.discriminator = None
        if rewards is not None:
            self.rewards = rewards

    @property
    def rewards(self):
        """Gets the rewards of this CosmosDistributionV1beta1QueryDelegationRewardsResponse.  # noqa: E501

        rewards defines the rewards accrued by a delegation.  # noqa: E501

        :return: The rewards of this CosmosDistributionV1beta1QueryDelegationRewardsResponse.  # noqa: E501
        :rtype: list[CosmosDistributionV1beta1QueryDelegationRewardsResponseRewards]
        """
        return self._rewards

    @rewards.setter
    def rewards(self, rewards):
        """Sets the rewards of this CosmosDistributionV1beta1QueryDelegationRewardsResponse.

        rewards defines the rewards accrued by a delegation.  # noqa: E501

        :param rewards: The rewards of this CosmosDistributionV1beta1QueryDelegationRewardsResponse.  # noqa: E501
        :type: list[CosmosDistributionV1beta1QueryDelegationRewardsResponseRewards]
        """

        self._rewards = rewards

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
        if issubclass(CosmosDistributionV1beta1QueryDelegationRewardsResponse, dict):
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
        if not isinstance(other, CosmosDistributionV1beta1QueryDelegationRewardsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other