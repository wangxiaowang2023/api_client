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

class CosmosTxV1beta1SignerInfo(object):
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
        'public_key': 'dict(str, object)',
        'mode_info': 'CosmosTxV1beta1ModeInfo',
        'sequence': 'str'
    }

    attribute_map = {
        'public_key': 'public_key',
        'mode_info': 'mode_info',
        'sequence': 'sequence'
    }

    def __init__(self, public_key=None, mode_info=None, sequence=None):  # noqa: E501
        """CosmosTxV1beta1SignerInfo - a model defined in Swagger"""  # noqa: E501
        self._public_key = None
        self._mode_info = None
        self._sequence = None
        self.discriminator = None
        if public_key is not None:
            self.public_key = public_key
        if mode_info is not None:
            self.mode_info = mode_info
        if sequence is not None:
            self.sequence = sequence

    @property
    def public_key(self):
        """Gets the public_key of this CosmosTxV1beta1SignerInfo.  # noqa: E501

        public_key is the public key of the signer. It is optional for accounts that already exist in state. If unset, the verifier can use the required \\ signer address for this position and lookup the public key.  # noqa: E501

        :return: The public_key of this CosmosTxV1beta1SignerInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this CosmosTxV1beta1SignerInfo.

        public_key is the public key of the signer. It is optional for accounts that already exist in state. If unset, the verifier can use the required \\ signer address for this position and lookup the public key.  # noqa: E501

        :param public_key: The public_key of this CosmosTxV1beta1SignerInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._public_key = public_key

    @property
    def mode_info(self):
        """Gets the mode_info of this CosmosTxV1beta1SignerInfo.  # noqa: E501


        :return: The mode_info of this CosmosTxV1beta1SignerInfo.  # noqa: E501
        :rtype: CosmosTxV1beta1ModeInfo
        """
        return self._mode_info

    @mode_info.setter
    def mode_info(self, mode_info):
        """Sets the mode_info of this CosmosTxV1beta1SignerInfo.


        :param mode_info: The mode_info of this CosmosTxV1beta1SignerInfo.  # noqa: E501
        :type: CosmosTxV1beta1ModeInfo
        """

        self._mode_info = mode_info

    @property
    def sequence(self):
        """Gets the sequence of this CosmosTxV1beta1SignerInfo.  # noqa: E501

        sequence is the sequence of the account, which describes the number of committed transactions signed by a given address. It is used to prevent replay attacks.  # noqa: E501

        :return: The sequence of this CosmosTxV1beta1SignerInfo.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this CosmosTxV1beta1SignerInfo.

        sequence is the sequence of the account, which describes the number of committed transactions signed by a given address. It is used to prevent replay attacks.  # noqa: E501

        :param sequence: The sequence of this CosmosTxV1beta1SignerInfo.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

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
        if issubclass(CosmosTxV1beta1SignerInfo, dict):
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
        if not isinstance(other, CosmosTxV1beta1SignerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other