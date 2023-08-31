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

class IbcCoreChannelV1Packet(object):
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
        'sequence': 'str',
        'source_port': 'str',
        'source_channel': 'str',
        'destination_port': 'str',
        'destination_channel': 'str',
        'data': 'str',
        'timeout_height': 'BlockHeightAfterWhichThePacketTimesOut',
        'timeout_timestamp': 'str'
    }

    attribute_map = {
        'sequence': 'sequence',
        'source_port': 'source_port',
        'source_channel': 'source_channel',
        'destination_port': 'destination_port',
        'destination_channel': 'destination_channel',
        'data': 'data',
        'timeout_height': 'timeout_height',
        'timeout_timestamp': 'timeout_timestamp'
    }

    def __init__(self, sequence=None, source_port=None, source_channel=None, destination_port=None, destination_channel=None, data=None, timeout_height=None, timeout_timestamp=None):  # noqa: E501
        """IbcCoreChannelV1Packet - a model defined in Swagger"""  # noqa: E501
        self._sequence = None
        self._source_port = None
        self._source_channel = None
        self._destination_port = None
        self._destination_channel = None
        self._data = None
        self._timeout_height = None
        self._timeout_timestamp = None
        self.discriminator = None
        if sequence is not None:
            self.sequence = sequence
        if source_port is not None:
            self.source_port = source_port
        if source_channel is not None:
            self.source_channel = source_channel
        if destination_port is not None:
            self.destination_port = destination_port
        if destination_channel is not None:
            self.destination_channel = destination_channel
        if data is not None:
            self.data = data
        if timeout_height is not None:
            self.timeout_height = timeout_height
        if timeout_timestamp is not None:
            self.timeout_timestamp = timeout_timestamp

    @property
    def sequence(self):
        """Gets the sequence of this IbcCoreChannelV1Packet.  # noqa: E501

        number corresponds to the order of sends and receives, where a Packet with an earlier sequence number must be sent and received before a Packet with a later sequence number.  # noqa: E501

        :return: The sequence of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this IbcCoreChannelV1Packet.

        number corresponds to the order of sends and receives, where a Packet with an earlier sequence number must be sent and received before a Packet with a later sequence number.  # noqa: E501

        :param sequence: The sequence of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def source_port(self):
        """Gets the source_port of this IbcCoreChannelV1Packet.  # noqa: E501

        identifies the port on the sending chain.  # noqa: E501

        :return: The source_port of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this IbcCoreChannelV1Packet.

        identifies the port on the sending chain.  # noqa: E501

        :param source_port: The source_port of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._source_port = source_port

    @property
    def source_channel(self):
        """Gets the source_channel of this IbcCoreChannelV1Packet.  # noqa: E501

        identifies the channel end on the sending chain.  # noqa: E501

        :return: The source_channel of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._source_channel

    @source_channel.setter
    def source_channel(self, source_channel):
        """Sets the source_channel of this IbcCoreChannelV1Packet.

        identifies the channel end on the sending chain.  # noqa: E501

        :param source_channel: The source_channel of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._source_channel = source_channel

    @property
    def destination_port(self):
        """Gets the destination_port of this IbcCoreChannelV1Packet.  # noqa: E501

        identifies the port on the receiving chain.  # noqa: E501

        :return: The destination_port of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this IbcCoreChannelV1Packet.

        identifies the port on the receiving chain.  # noqa: E501

        :param destination_port: The destination_port of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._destination_port = destination_port

    @property
    def destination_channel(self):
        """Gets the destination_channel of this IbcCoreChannelV1Packet.  # noqa: E501

        identifies the channel end on the receiving chain.  # noqa: E501

        :return: The destination_channel of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._destination_channel

    @destination_channel.setter
    def destination_channel(self, destination_channel):
        """Sets the destination_channel of this IbcCoreChannelV1Packet.

        identifies the channel end on the receiving chain.  # noqa: E501

        :param destination_channel: The destination_channel of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._destination_channel = destination_channel

    @property
    def data(self):
        """Gets the data of this IbcCoreChannelV1Packet.  # noqa: E501


        :return: The data of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this IbcCoreChannelV1Packet.


        :param data: The data of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def timeout_height(self):
        """Gets the timeout_height of this IbcCoreChannelV1Packet.  # noqa: E501


        :return: The timeout_height of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: BlockHeightAfterWhichThePacketTimesOut
        """
        return self._timeout_height

    @timeout_height.setter
    def timeout_height(self, timeout_height):
        """Sets the timeout_height of this IbcCoreChannelV1Packet.


        :param timeout_height: The timeout_height of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: BlockHeightAfterWhichThePacketTimesOut
        """

        self._timeout_height = timeout_height

    @property
    def timeout_timestamp(self):
        """Gets the timeout_timestamp of this IbcCoreChannelV1Packet.  # noqa: E501


        :return: The timeout_timestamp of this IbcCoreChannelV1Packet.  # noqa: E501
        :rtype: str
        """
        return self._timeout_timestamp

    @timeout_timestamp.setter
    def timeout_timestamp(self, timeout_timestamp):
        """Sets the timeout_timestamp of this IbcCoreChannelV1Packet.


        :param timeout_timestamp: The timeout_timestamp of this IbcCoreChannelV1Packet.  # noqa: E501
        :type: str
        """

        self._timeout_timestamp = timeout_timestamp

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
        if issubclass(IbcCoreChannelV1Packet, dict):
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
        if not isinstance(other, IbcCoreChannelV1Packet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other