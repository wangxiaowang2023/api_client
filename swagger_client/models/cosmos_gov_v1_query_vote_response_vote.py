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

class CosmosGovV1QueryVoteResponseVote(object):
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
        'proposal_id': 'str',
        'voter': 'str',
        'options': 'list[CosmosGovV1QueryVoteResponseVoteOptions]',
        'metadata': 'str'
    }

    attribute_map = {
        'proposal_id': 'proposal_id',
        'voter': 'voter',
        'options': 'options',
        'metadata': 'metadata'
    }

    def __init__(self, proposal_id=None, voter=None, options=None, metadata=None):  # noqa: E501
        """CosmosGovV1QueryVoteResponseVote - a model defined in Swagger"""  # noqa: E501
        self._proposal_id = None
        self._voter = None
        self._options = None
        self._metadata = None
        self.discriminator = None
        if proposal_id is not None:
            self.proposal_id = proposal_id
        if voter is not None:
            self.voter = voter
        if options is not None:
            self.options = options
        if metadata is not None:
            self.metadata = metadata

    @property
    def proposal_id(self):
        """Gets the proposal_id of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501

        proposal_id defines the unique id of the proposal.  # noqa: E501

        :return: The proposal_id of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this CosmosGovV1QueryVoteResponseVote.

        proposal_id defines the unique id of the proposal.  # noqa: E501

        :param proposal_id: The proposal_id of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :type: str
        """

        self._proposal_id = proposal_id

    @property
    def voter(self):
        """Gets the voter of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501

        voter is the voter address of the proposal.  # noqa: E501

        :return: The voter of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :rtype: str
        """
        return self._voter

    @voter.setter
    def voter(self, voter):
        """Sets the voter of this CosmosGovV1QueryVoteResponseVote.

        voter is the voter address of the proposal.  # noqa: E501

        :param voter: The voter of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :type: str
        """

        self._voter = voter

    @property
    def options(self):
        """Gets the options of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501

        options is the weighted vote options.  # noqa: E501

        :return: The options of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :rtype: list[CosmosGovV1QueryVoteResponseVoteOptions]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CosmosGovV1QueryVoteResponseVote.

        options is the weighted vote options.  # noqa: E501

        :param options: The options of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :type: list[CosmosGovV1QueryVoteResponseVoteOptions]
        """

        self._options = options

    @property
    def metadata(self):
        """Gets the metadata of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501

        metadata is any  arbitrary metadata to attached to the vote.  # noqa: E501

        :return: The metadata of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CosmosGovV1QueryVoteResponseVote.

        metadata is any  arbitrary metadata to attached to the vote.  # noqa: E501

        :param metadata: The metadata of this CosmosGovV1QueryVoteResponseVote.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

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
        if issubclass(CosmosGovV1QueryVoteResponseVote, dict):
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
        if not isinstance(other, CosmosGovV1QueryVoteResponseVote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
