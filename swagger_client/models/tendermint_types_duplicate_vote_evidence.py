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

class TendermintTypesDuplicateVoteEvidence(object):
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
        'vote_a': 'CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA',
        'vote_b': 'CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA',
        'total_voting_power': 'str',
        'validator_power': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'vote_a': 'vote_a',
        'vote_b': 'vote_b',
        'total_voting_power': 'total_voting_power',
        'validator_power': 'validator_power',
        'timestamp': 'timestamp'
    }

    def __init__(self, vote_a=None, vote_b=None, total_voting_power=None, validator_power=None, timestamp=None):  # noqa: E501
        """TendermintTypesDuplicateVoteEvidence - a model defined in Swagger"""  # noqa: E501
        self._vote_a = None
        self._vote_b = None
        self._total_voting_power = None
        self._validator_power = None
        self._timestamp = None
        self.discriminator = None
        if vote_a is not None:
            self.vote_a = vote_a
        if vote_b is not None:
            self.vote_b = vote_b
        if total_voting_power is not None:
            self.total_voting_power = total_voting_power
        if validator_power is not None:
            self.validator_power = validator_power
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def vote_a(self):
        """Gets the vote_a of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501


        :return: The vote_a of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA
        """
        return self._vote_a

    @vote_a.setter
    def vote_a(self, vote_a):
        """Sets the vote_a of this TendermintTypesDuplicateVoteEvidence.


        :param vote_a: The vote_a of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA
        """

        self._vote_a = vote_a

    @property
    def vote_b(self):
        """Gets the vote_b of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501


        :return: The vote_b of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :rtype: CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA
        """
        return self._vote_b

    @vote_b.setter
    def vote_b(self, vote_b):
        """Sets the vote_b of this TendermintTypesDuplicateVoteEvidence.


        :param vote_b: The vote_b of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :type: CosmosBaseTendermintV1beta1BlockEvidenceDuplicateVoteEvidenceVoteA
        """

        self._vote_b = vote_b

    @property
    def total_voting_power(self):
        """Gets the total_voting_power of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501


        :return: The total_voting_power of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :rtype: str
        """
        return self._total_voting_power

    @total_voting_power.setter
    def total_voting_power(self, total_voting_power):
        """Sets the total_voting_power of this TendermintTypesDuplicateVoteEvidence.


        :param total_voting_power: The total_voting_power of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :type: str
        """

        self._total_voting_power = total_voting_power

    @property
    def validator_power(self):
        """Gets the validator_power of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501


        :return: The validator_power of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :rtype: str
        """
        return self._validator_power

    @validator_power.setter
    def validator_power(self, validator_power):
        """Sets the validator_power of this TendermintTypesDuplicateVoteEvidence.


        :param validator_power: The validator_power of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :type: str
        """

        self._validator_power = validator_power

    @property
    def timestamp(self):
        """Gets the timestamp of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501


        :return: The timestamp of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TendermintTypesDuplicateVoteEvidence.


        :param timestamp: The timestamp of this TendermintTypesDuplicateVoteEvidence.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if issubclass(TendermintTypesDuplicateVoteEvidence, dict):
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
        if not isinstance(other, TendermintTypesDuplicateVoteEvidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
