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

class CosmwasmWasmV1ContractInfo(object):
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
        'code_id': 'str',
        'creator': 'str',
        'admin': 'str',
        'label': 'str',
        'created': 'CosmwasmWasmV1ContractInfoCreated',
        'ibc_port_id': 'str',
        'extension': 'dict(str, object)'
    }

    attribute_map = {
        'code_id': 'code_id',
        'creator': 'creator',
        'admin': 'admin',
        'label': 'label',
        'created': 'created',
        'ibc_port_id': 'ibc_port_id',
        'extension': 'extension'
    }

    def __init__(self, code_id=None, creator=None, admin=None, label=None, created=None, ibc_port_id=None, extension=None):  # noqa: E501
        """CosmwasmWasmV1ContractInfo - a model defined in Swagger"""  # noqa: E501
        self._code_id = None
        self._creator = None
        self._admin = None
        self._label = None
        self._created = None
        self._ibc_port_id = None
        self._extension = None
        self.discriminator = None
        if code_id is not None:
            self.code_id = code_id
        if creator is not None:
            self.creator = creator
        if admin is not None:
            self.admin = admin
        if label is not None:
            self.label = label
        if created is not None:
            self.created = created
        if ibc_port_id is not None:
            self.ibc_port_id = ibc_port_id
        if extension is not None:
            self.extension = extension

    @property
    def code_id(self):
        """Gets the code_id of this CosmwasmWasmV1ContractInfo.  # noqa: E501


        :return: The code_id of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: str
        """
        return self._code_id

    @code_id.setter
    def code_id(self, code_id):
        """Sets the code_id of this CosmwasmWasmV1ContractInfo.


        :param code_id: The code_id of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: str
        """

        self._code_id = code_id

    @property
    def creator(self):
        """Gets the creator of this CosmwasmWasmV1ContractInfo.  # noqa: E501


        :return: The creator of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CosmwasmWasmV1ContractInfo.


        :param creator: The creator of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def admin(self):
        """Gets the admin of this CosmwasmWasmV1ContractInfo.  # noqa: E501


        :return: The admin of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: str
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this CosmwasmWasmV1ContractInfo.


        :param admin: The admin of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: str
        """

        self._admin = admin

    @property
    def label(self):
        """Gets the label of this CosmwasmWasmV1ContractInfo.  # noqa: E501

        Label is optional metadata to be stored with a contract instance.  # noqa: E501

        :return: The label of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CosmwasmWasmV1ContractInfo.

        Label is optional metadata to be stored with a contract instance.  # noqa: E501

        :param label: The label of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def created(self):
        """Gets the created of this CosmwasmWasmV1ContractInfo.  # noqa: E501


        :return: The created of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: CosmwasmWasmV1ContractInfoCreated
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CosmwasmWasmV1ContractInfo.


        :param created: The created of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: CosmwasmWasmV1ContractInfoCreated
        """

        self._created = created

    @property
    def ibc_port_id(self):
        """Gets the ibc_port_id of this CosmwasmWasmV1ContractInfo.  # noqa: E501


        :return: The ibc_port_id of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: str
        """
        return self._ibc_port_id

    @ibc_port_id.setter
    def ibc_port_id(self, ibc_port_id):
        """Sets the ibc_port_id of this CosmwasmWasmV1ContractInfo.


        :param ibc_port_id: The ibc_port_id of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: str
        """

        self._ibc_port_id = ibc_port_id

    @property
    def extension(self):
        """Gets the extension of this CosmwasmWasmV1ContractInfo.  # noqa: E501

        Extension is an extension point to store custom metadata within the persistence model.  # noqa: E501

        :return: The extension of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this CosmwasmWasmV1ContractInfo.

        Extension is an extension point to store custom metadata within the persistence model.  # noqa: E501

        :param extension: The extension of this CosmwasmWasmV1ContractInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._extension = extension

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
        if issubclass(CosmwasmWasmV1ContractInfo, dict):
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
        if not isinstance(other, CosmwasmWasmV1ContractInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other