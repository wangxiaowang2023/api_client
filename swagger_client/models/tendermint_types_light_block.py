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

class TendermintTypesLightBlock(object):
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
        'signed_header': 'DeprecatedPleaseUseSdkBlockInsteadEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader',
        'validator_set': 'CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockValidatorSet'
    }

    attribute_map = {
        'signed_header': 'signed_header',
        'validator_set': 'validator_set'
    }

    def __init__(self, signed_header=None, validator_set=None):  # noqa: E501
        """TendermintTypesLightBlock - a model defined in Swagger"""  # noqa: E501
        self._signed_header = None
        self._validator_set = None
        self.discriminator = None
        if signed_header is not None:
            self.signed_header = signed_header
        if validator_set is not None:
            self.validator_set = validator_set

    @property
    def signed_header(self):
        """Gets the signed_header of this TendermintTypesLightBlock.  # noqa: E501


        :return: The signed_header of this TendermintTypesLightBlock.  # noqa: E501
        :rtype: DeprecatedPleaseUseSdkBlockInsteadEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader
        """
        return self._signed_header

    @signed_header.setter
    def signed_header(self, signed_header):
        """Sets the signed_header of this TendermintTypesLightBlock.


        :param signed_header: The signed_header of this TendermintTypesLightBlock.  # noqa: E501
        :type: DeprecatedPleaseUseSdkBlockInsteadEvidenceLightClientAttackEvidenceConflictingBlockSignedHeader
        """

        self._signed_header = signed_header

    @property
    def validator_set(self):
        """Gets the validator_set of this TendermintTypesLightBlock.  # noqa: E501


        :return: The validator_set of this TendermintTypesLightBlock.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockValidatorSet
        """
        return self._validator_set

    @validator_set.setter
    def validator_set(self, validator_set):
        """Sets the validator_set of this TendermintTypesLightBlock.


        :param validator_set: The validator_set of this TendermintTypesLightBlock.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1BlockEvidenceLightClientAttackEvidenceConflictingBlockValidatorSet
        """

        self._validator_set = validator_set

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
        if issubclass(TendermintTypesLightBlock, dict):
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
        if not isinstance(other, TendermintTypesLightBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other