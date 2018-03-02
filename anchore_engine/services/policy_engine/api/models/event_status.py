# coding: utf-8


from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class EventStatus(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, event_id=None, event_timestamp=None, event_state=None):
        """
        EventStatus - a model defined in Swagger

        :param event_id: The event_id of this EventStatus.
        :type event_id: str
        :param event_timestamp: The event_timestamp of this EventStatus.
        :type event_timestamp: datetime
        :param event_state: The event_state of this EventStatus.
        :type event_state: str
        """
        self.swagger_types = {
            'event_id': str,
            'event_timestamp': datetime,
            'event_state': str
        }

        self.attribute_map = {
            'event_id': 'event_id',
            'event_timestamp': 'event_timestamp',
            'event_state': 'event_state'
        }

        self._event_id = event_id
        self._event_timestamp = event_timestamp
        self._event_state = event_state

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventStatus of this EventStatus.
        :rtype: EventStatus
        """
        return deserialize_model(dikt, cls)

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
        :type event_id: str
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
        :type event_timestamp: datetime
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
        :type event_state: str
        """
        allowed_values = ["pending", "processing", "complete", "failed"]
        if event_state not in allowed_values:
            raise ValueError(
                "Invalid value for `event_state` ({0}), must be one of {1}"
                .format(event_state, allowed_values)
            )

        self._event_state = event_state

