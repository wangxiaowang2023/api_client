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

class CosmosStakingV1beta1QueryAllSiidResponseSiidNFT(object):
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
        'creator': 'str',
        'account': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'siid': 'str',
        'nft_id': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'account': 'account',
        'region_id': 'regionId',
        'region_name': 'regionName',
        'siid': 'siid',
        'nft_id': 'nft_id'
    }

    def __init__(self, creator=None, account=None, region_id=None, region_name=None, siid=None, nft_id=None):  # noqa: E501
        """CosmosStakingV1beta1QueryAllSiidResponseSiidNFT - a model defined in Swagger"""  # noqa: E501
        self._creator = None
        self._account = None
        self._region_id = None
        self._region_name = None
        self._siid = None
        self._nft_id = None
        self.discriminator = None
        if creator is not None:
            self.creator = creator
        if account is not None:
            self.account = account
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if siid is not None:
            self.siid = siid
        if nft_id is not None:
            self.nft_id = nft_id

    @property
    def creator(self):
        """Gets the creator of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501


        :return: The creator of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.


        :param creator: The creator of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def account(self):
        """Gets the account of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501


        :return: The account of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.


        :param account: The account of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def region_id(self):
        """Gets the region_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501


        :return: The region_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.


        :param region_id: The region_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501


        :return: The region_name of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.


        :param region_name: The region_name of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def siid(self):
        """Gets the siid of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501


        :return: The siid of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :rtype: str
        """
        return self._siid

    @siid.setter
    def siid(self, siid):
        """Sets the siid of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.


        :param siid: The siid of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :type: str
        """

        self._siid = siid

    @property
    def nft_id(self):
        """Gets the nft_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501


        :return: The nft_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :rtype: str
        """
        return self._nft_id

    @nft_id.setter
    def nft_id(self, nft_id):
        """Sets the nft_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.


        :param nft_id: The nft_id of this CosmosStakingV1beta1QueryAllSiidResponseSiidNFT.  # noqa: E501
        :type: str
        """

        self._nft_id = nft_id

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
        if issubclass(CosmosStakingV1beta1QueryAllSiidResponseSiidNFT, dict):
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
        if not isinstance(other, CosmosStakingV1beta1QueryAllSiidResponseSiidNFT):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other