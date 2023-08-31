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

class IbcCoreChannelV1QueryPacketAcknowledgementResponse(object):
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
        'acknowledgement': 'str',
        'proof': 'str',
        'proof_height': 'HeightAtWhichTheProofWasRetrieved'
    }

    attribute_map = {
        'acknowledgement': 'acknowledgement',
        'proof': 'proof',
        'proof_height': 'proof_height'
    }

    def __init__(self, acknowledgement=None, proof=None, proof_height=None):  # noqa: E501
        """IbcCoreChannelV1QueryPacketAcknowledgementResponse - a model defined in Swagger"""  # noqa: E501
        self._acknowledgement = None
        self._proof = None
        self._proof_height = None
        self.discriminator = None
        if acknowledgement is not None:
            self.acknowledgement = acknowledgement
        if proof is not None:
            self.proof = proof
        if proof_height is not None:
            self.proof_height = proof_height

    @property
    def acknowledgement(self):
        """Gets the acknowledgement of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501


        :return: The acknowledgement of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501
        :rtype: str
        """
        return self._acknowledgement

    @acknowledgement.setter
    def acknowledgement(self, acknowledgement):
        """Sets the acknowledgement of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.


        :param acknowledgement: The acknowledgement of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501
        :type: str
        """

        self._acknowledgement = acknowledgement

    @property
    def proof(self):
        """Gets the proof of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501


        :return: The proof of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501
        :rtype: str
        """
        return self._proof

    @proof.setter
    def proof(self, proof):
        """Sets the proof of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.


        :param proof: The proof of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501
        :type: str
        """

        self._proof = proof

    @property
    def proof_height(self):
        """Gets the proof_height of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501


        :return: The proof_height of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501
        :rtype: HeightAtWhichTheProofWasRetrieved
        """
        return self._proof_height

    @proof_height.setter
    def proof_height(self, proof_height):
        """Sets the proof_height of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.


        :param proof_height: The proof_height of this IbcCoreChannelV1QueryPacketAcknowledgementResponse.  # noqa: E501
        :type: HeightAtWhichTheProofWasRetrieved
        """

        self._proof_height = proof_height

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
        if issubclass(IbcCoreChannelV1QueryPacketAcknowledgementResponse, dict):
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
        if not isinstance(other, IbcCoreChannelV1QueryPacketAcknowledgementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other