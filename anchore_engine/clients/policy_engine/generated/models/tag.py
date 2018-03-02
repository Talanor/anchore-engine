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


class Tag(object):
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
        'user_id': 'str',
        'registry_name': 'str',
        'repository': 'str',
        'name': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'registry_name': 'registry_name',
        'repository': 'repository',
        'name': 'name'
    }

    def __init__(self, user_id=None, registry_name=None, repository=None, name=None):
        """
        Tag - a model defined in Swagger
        """

        self._user_id = None
        self._registry_name = None
        self._repository = None
        self._name = None

        if user_id is not None:
          self.user_id = user_id
        if registry_name is not None:
          self.registry_name = registry_name
        if repository is not None:
          self.repository = repository
        if name is not None:
          self.name = name

    @property
    def user_id(self):
        """
        Gets the user_id of this Tag.
        The catalog user id that scopes this tag value. NOT a username on the source registry

        :return: The user_id of this Tag.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Tag.
        The catalog user id that scopes this tag value. NOT a username on the source registry

        :param user_id: The user_id of this Tag.
        :type: str
        """

        self._user_id = user_id

    @property
    def registry_name(self):
        """
        Gets the registry_name of this Tag.
        The registry record name in the catalog to identify the repository. Scoped by the user_id. Eg. dockerhub

        :return: The registry_name of this Tag.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        """
        Sets the registry_name of this Tag.
        The registry record name in the catalog to identify the repository. Scoped by the user_id. Eg. dockerhub

        :param registry_name: The registry_name of this Tag.
        :type: str
        """

        self._registry_name = registry_name

    @property
    def repository(self):
        """
        Gets the repository of this Tag.
        Repository name, including any source registry user namespace for the tag. e.g. library/centos or bitnami/node

        :return: The repository of this Tag.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """
        Sets the repository of this Tag.
        Repository name, including any source registry user namespace for the tag. e.g. library/centos or bitnami/node

        :param repository: The repository of this Tag.
        :type: str
        """

        self._repository = repository

    @property
    def name(self):
        """
        Gets the name of this Tag.
        The name of the tag. e.g. latest, 8.0, or 5.4-alpine

        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tag.
        The name of the tag. e.g. latest, 8.0, or 5.4-alpine

        :param name: The name of this Tag.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
