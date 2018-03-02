# coding: utf-8


from .policy import Policy
from .whitelist import Whitelist
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PolicyBundleLight(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, image_id=None, policy=None, whitelists=None):
        """
        PolicyBundleLight - a model defined in Swagger

        :param image_id: The image_id of this PolicyBundleLight.
        :type image_id: str
        :param policy: The policy of this PolicyBundleLight.
        :type policy: Policy
        :param whitelists: The whitelists of this PolicyBundleLight.
        :type whitelists: List[Whitelist]
        """
        self.swagger_types = {
            'image_id': str,
            'policy': Policy,
            'whitelists': List[Whitelist]
        }

        self.attribute_map = {
            'image_id': 'image_id',
            'policy': 'policy',
            'whitelists': 'whitelists'
        }

        self._image_id = image_id
        self._policy = policy
        self._whitelists = whitelists

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PolicyBundleLight of this PolicyBundleLight.
        :rtype: PolicyBundleLight
        """
        return deserialize_model(dikt, cls)

    @property
    def image_id(self):
        """
        Gets the image_id of this PolicyBundleLight.

        :return: The image_id of this PolicyBundleLight.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this PolicyBundleLight.

        :param image_id: The image_id of this PolicyBundleLight.
        :type image_id: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")

        self._image_id = image_id

    @property
    def policy(self):
        """
        Gets the policy of this PolicyBundleLight.

        :return: The policy of this PolicyBundleLight.
        :rtype: Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this PolicyBundleLight.

        :param policy: The policy of this PolicyBundleLight.
        :type policy: Policy
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")

        self._policy = policy

    @property
    def whitelists(self):
        """
        Gets the whitelists of this PolicyBundleLight.

        :return: The whitelists of this PolicyBundleLight.
        :rtype: List[Whitelist]
        """
        return self._whitelists

    @whitelists.setter
    def whitelists(self, whitelists):
        """
        Sets the whitelists of this PolicyBundleLight.

        :param whitelists: The whitelists of this PolicyBundleLight.
        :type whitelists: List[Whitelist]
        """

        self._whitelists = whitelists

