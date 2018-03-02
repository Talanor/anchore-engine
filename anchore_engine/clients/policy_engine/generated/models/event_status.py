# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EventStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'event_id': 'str',
        'event_timestamp': 'datetime',
        'event_state': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_timestamp': 'event_timestamp',
        'event_state': 'event_state'
    }

    def __init__(self, event_id=None, event_timestamp=None, event_state=None):
        """
        EventStatus - a model defined in Swagger
        """

        self._event_id = None
        self._event_timestamp = None
        self._event_state = None

        if event_id is not None:
          self.event_id = event_id
        if event_timestamp is not None:
          self.event_timestamp = event_timestamp
        if event_state is not None:
          self.event_state = event_state

    @property
    def event_id(self):
        """
        Gets the event_id of this EventStatus.
        A generated event id for later use to query status of the event

        :return: The event_id of this EventStatus.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this EventStatus.
        A generated event id for later use to query status of the event

        :param event_id: The event_id of this EventStatus.
        :type: str
        """

        self._event_id = event_id

    @property
    def event_timestamp(self):
        """
        Gets the event_timestamp of this EventStatus.

        :return: The event_timestamp of this EventStatus.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """
        Sets the event_timestamp of this EventStatus.

        :param event_timestamp: The event_timestamp of this EventStatus.
        :type: datetime
        """

        self._event_timestamp = event_timestamp

    @property
    def event_state(self):
        """
        Gets the event_state of this EventStatus.
        State of the event, as defined by an enum

        :return: The event_state of this EventStatus.
        :rtype: str
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        """
        Sets the event_state of this EventStatus.
        State of the event, as defined by an enum

        :param event_state: The event_state of this EventStatus.
        :type: str
        """
        allowed_values = ["pending", "processing", "complete", "failed"]
        if event_state not in allowed_values:
            raise ValueError(
                "Invalid value for `event_state` ({0}), must be one of {1}"
                .format(event_state, allowed_values)
            )

        self._event_state = event_state

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EventStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
