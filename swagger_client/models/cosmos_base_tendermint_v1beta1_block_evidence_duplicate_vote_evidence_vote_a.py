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

class CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA(object):
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
        'type': 'str',
        'height': 'str',
        'round': 'int',
        'block_id': 'BlockID1',
        'timestamp': 'datetime',
        'validator_address': 'str',
        'validator_index': 'int',
        'signature': 'str'
    }

    attribute_map = {
        'type': 'type',
        'height': 'height',
        'round': 'round',
        'block_id': 'block_id',
        'timestamp': 'timestamp',
        'validator_address': 'validator_address',
        'validator_index': 'validator_index',
        'signature': 'signature'
    }

    def __init__(self, type='SIGNED_MSG_TYPE_UNKNOWN', height=None, round=None, block_id=None, timestamp=None, validator_address=None, validator_index=None, signature=None):  # noqa: E501
        """CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._height = None
        self._round = None
        self._block_id = None
        self._timestamp = None
        self._validator_address = None
        self._validator_index = None
        self._signature = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if height is not None:
            self.height = height
        if round is not None:
            self.round = round
        if block_id is not None:
            self.block_id = block_id
        if timestamp is not None:
            self.timestamp = timestamp
        if validator_address is not None:
            self.validator_address = validator_address
        if validator_index is not None:
            self.validator_index = validator_index
        if signature is not None:
            self.signature = signature

    @property
    def type(self):
        """Gets the type of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501

        SignedMsgType is a type of signed message in the consensus.   - SIGNED_MSG_TYPE_PREVOTE: Votes  - SIGNED_MSG_TYPE_PROPOSAL: Proposals  # noqa: E501

        :return: The type of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.

        SignedMsgType is a type of signed message in the consensus.   - SIGNED_MSG_TYPE_PREVOTE: Votes  - SIGNED_MSG_TYPE_PROPOSAL: Proposals  # noqa: E501

        :param type: The type of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: str
        """
        allowed_values = ["SIGNED_MSG_TYPE_UNKNOWN", "SIGNED_MSG_TYPE_PREVOTE", "SIGNED_MSG_TYPE_PRECOMMIT", "SIGNED_MSG_TYPE_PROPOSAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def height(self):
        """Gets the height of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The height of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param height: The height of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def round(self):
        """Gets the round of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The round of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param round: The round of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def block_id(self):
        """Gets the block_id of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The block_id of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: BlockID1
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param block_id: The block_id of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: BlockID1
        """

        self._block_id = block_id

    @property
    def timestamp(self):
        """Gets the timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param timestamp: The timestamp of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def validator_address(self):
        """Gets the validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: str
        """
        return self._validator_address

    @validator_address.setter
    def validator_address(self, validator_address):
        """Sets the validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param validator_address: The validator_address of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: str
        """

        self._validator_address = validator_address

    @property
    def validator_index(self):
        """Gets the validator_index of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The validator_index of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: int
        """
        return self._validator_index

    @validator_index.setter
    def validator_index(self, validator_index):
        """Sets the validator_index of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param validator_index: The validator_index of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: int
        """

        self._validator_index = validator_index

    @property
    def signature(self):
        """Gets the signature of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501


        :return: The signature of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.


        :param signature: The signature of this CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA.  # noqa: E501
        :type: str
        """

        self._signature = signature

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
        if issubclass(CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA, dict):
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
        if not isinstance(other, CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other