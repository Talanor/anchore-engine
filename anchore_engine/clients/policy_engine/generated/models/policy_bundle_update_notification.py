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


class PolicyBundleUpdateNotification(object):
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
        'bundle_id': 'str',
        'event_timestamp': 'datetime'
    }

    attribute_map = {
        'bundle_id': 'bundle_id',
        'event_timestamp': 'event_timestamp'
    }

    def __init__(self, bundle_id=None, event_timestamp=None):
        """
        PolicyBundleUpdateNotification - a model defined in Swagger
        """

        self._bundle_id = None
        self._event_timestamp = None

        if bundle_id is not None:
          self.bundle_id = bundle_id
        if event_timestamp is not None:
          self.event_timestamp = event_timestamp

    @property
    def bundle_id(self):
        """
        Gets the bundle_id of this PolicyBundleUpdateNotification.

        :return: The bundle_id of this PolicyBundleUpdateNotification.
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """
        Sets the bundle_id of this PolicyBundleUpdateNotification.

        :param bundle_id: The bundle_id of this PolicyBundleUpdateNotification.
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def event_timestamp(self):
        """
        Gets the event_timestamp of this PolicyBundleUpdateNotification.
        The time of the external event. Should be set to when the event occurred, to the delivery time

        :return: The event_timestamp of this PolicyBundleUpdateNotification.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """
        Sets the event_timestamp of this PolicyBundleUpdateNotification.
        The time of the external event. Should be set to when the event occurred, to the delivery time

        :param event_timestamp: The event_timestamp of this PolicyBundleUpdateNotification.
        :type: datetime
        """

        self._event_timestamp = event_timestamp

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
        if not isinstance(other, PolicyBundleUpdateNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
